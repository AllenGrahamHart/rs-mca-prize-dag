#!/usr/bin/env python3
"""Hostile mutations for the signed-pair primitive coordinate-map packet."""

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


HERE = Path(__file__).parent
CHECKER = HERE / "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map.py"
COORDINATE_MAP = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json"
)
COORDINATE_COLUMNS = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_coordinate_columns_result.json"
)
MAP_PAYLOAD = json.loads(COORDINATE_MAP.read_text())
COLUMN_PAYLOAD = json.loads(COORDINATE_COLUMNS.read_text())


def rejected(map_payload=MAP_PAYLOAD, column_payload=COLUMN_PAYLOAD):
    with tempfile.TemporaryDirectory() as directory:
        map_path = Path(directory) / "map.json"
        column_path = Path(directory) / "columns.json"
        map_path.write_text(json.dumps(map_payload, sort_keys=True))
        column_path.write_text(json.dumps(column_payload, sort_keys=True))
        process = subprocess.run(
            [
                sys.executable,
                str(CHECKER),
                "--coordinate-map",
                str(map_path),
                "--coordinate-columns",
                str(column_path),
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
    return process.returncode != 0


dropped = copy.deepcopy(MAP_PAYLOAD)
dropped[0]["coordinates"] = dropped[0]["coordinates"][1:]
assert rejected(dropped), "checker accepted dropped coordinate"

coefficient = copy.deepcopy(MAP_PAYLOAD)
coefficient[0]["coordinates"][0]["numerator"][0] = (
    coefficient[0]["coordinates"][0]["numerator"][0] + 1
) % 2130706433
assert rejected(coefficient), "checker accepted changed coordinate coefficient"

provenance = copy.deepcopy(MAP_PAYLOAD)
provenance[0]["operator_sha256"] = "0" * 64
assert rejected(provenance), "checker accepted changed operator provenance"

column = copy.deepcopy(COLUMN_PAYLOAD)
coordinate = next(item for item in column[0]["entries"] if item["kind"] == "C")
coordinate["numerator"][0] = (coordinate["numerator"][0] + 1) % 2130706433
assert rejected(MAP_PAYLOAD, column), "checker accepted changed source coordinate column"

print(
    "RATE_HALF_KB_POSITIVE_433_1A_CELL5_PRIMITIVE_COORDINATE_MAP_MUTATION_PASS "
    "rejected=dropped_coordinate,changed_coefficient,changed_provenance,changed_column"
)
