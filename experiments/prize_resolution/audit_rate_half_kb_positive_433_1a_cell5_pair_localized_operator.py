#!/usr/bin/env python3
"""Hostile mutations for the localized signed-pair operator certificate."""

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


HERE = Path(__file__).parent
CHECKER = HERE / "check_rate_half_kb_positive_433_1a_cell5_pair_localized_operator.py"
OPERATOR = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_localized_operator_merged_result.json"
)
PAYLOAD = json.loads(OPERATOR.read_text())


def rejected(payload):
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "operator.json"
        path.write_text(json.dumps(payload, sort_keys=True))
        process = subprocess.run(
            [sys.executable, str(CHECKER), "--operator", str(path)],
            capture_output=True,
            text=True,
            timeout=20,
        )
    return process.returncode != 0


dropped = copy.deepcopy(PAYLOAD)
dropped["entries"] = dropped["entries"][1:]
assert rejected(dropped), "checker accepted dropped operator entry"

coordinate = copy.deepcopy(PAYLOAD)
entry = next(item for item in coordinate["entries"] if item["kind"] == "C")
entry["numerator"][0] = (entry["numerator"][0] + 1) % 2130706433
assert rejected(coordinate), "checker accepted changed operator coordinate"

target = copy.deepcopy(PAYLOAD)
entry = next(item for item in target["entries"] if item["kind"] == "W")
entry["numerator"][0] = (entry["numerator"][0] + 1) % 2130706433
assert rejected(target), "checker accepted changed operator target"

print(
    "RATE_HALF_KB_POSITIVE_433_1A_CELL5_LOCALIZED_OPERATOR_MUTATION_PASS "
    "rejected=dropped_entry,changed_coordinate,changed_target"
)
