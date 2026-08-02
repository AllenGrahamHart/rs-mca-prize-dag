#!/usr/bin/env python3
"""Hostile mutations for the generic signed-pair guard-unit checker."""

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


HERE = Path(__file__).parent
CHECKER = HERE / "check_rate_half_kb_positive_433_1a_cell5_pair_generic_guard_units.py"
COORDINATE_MAP = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json"
)
FACTORIZATION = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json"
)
ATLAS = HERE / "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"
MAP_PAYLOAD = json.loads(COORDINATE_MAP.read_text())
FACTOR_PAYLOAD = json.loads(FACTORIZATION.read_text())
ATLAS_PAYLOAD = json.loads(ATLAS.read_text())


def rejected(map_payload=MAP_PAYLOAD, factor_payload=FACTOR_PAYLOAD, atlas_payload=ATLAS_PAYLOAD):
    with tempfile.TemporaryDirectory() as directory:
        map_path = Path(directory) / "map.json"
        factor_path = Path(directory) / "factors.json"
        atlas_path = Path(directory) / "atlas.json"
        map_path.write_text(json.dumps(map_payload, sort_keys=True))
        factor_path.write_text(json.dumps(factor_payload, sort_keys=True))
        atlas_path.write_text(json.dumps(atlas_payload, indent=2))
        process = subprocess.run(
            [
                sys.executable,
                str(CHECKER),
                "--coordinate-map",
                str(map_path),
                "--factorization",
                str(factor_path),
                "--atlas",
                str(atlas_path),
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
    return process.returncode != 0


coordinate = copy.deepcopy(MAP_PAYLOAD)
coordinate[0]["coordinates"][0]["numerator"][0] = (
    coordinate[0]["coordinates"][0]["numerator"][0] + 1
) % 2130706433
assert rejected(map_payload=coordinate), "checker accepted changed coordinate map"

factor = copy.deepcopy(FACTOR_PAYLOAD)
factor["factors"][0]["numerator"][0] = (
    factor["factors"][0]["numerator"][0] + 1
) % 2130706433
assert rejected(factor_payload=factor), "checker accepted changed residue factor"

atlas = copy.deepcopy(ATLAS_PAYLOAD)
atlas["r_chart"]["constant"] = atlas["r_chart"]["constant"] + "+1"
assert rejected(atlas_payload=atlas), "checker accepted changed lift atlas"

print(
    "RATE_HALF_KB_POSITIVE_433_1A_CELL5_GENERIC_GUARD_UNITS_MUTATION_PASS "
    "rejected=changed_coordinate,changed_factor,changed_atlas"
)
