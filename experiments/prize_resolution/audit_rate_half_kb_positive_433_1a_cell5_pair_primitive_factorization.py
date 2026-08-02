#!/usr/bin/env python3
"""Hostile mutations for the localized-pair primitive factorization."""

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


HERE = Path(__file__).parent
CHECKER = HERE / "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization.py"
FACTORIZATION = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json"
)
PAYLOAD = json.loads(FACTORIZATION.read_text())


def rejected(payload):
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "factorization.json"
        path.write_text(json.dumps(payload, sort_keys=True))
        process = subprocess.run(
            [sys.executable, str(CHECKER), "--factorization", str(path)],
            capture_output=True,
            text=True,
            timeout=20,
        )
    return process.returncode != 0


dropped = copy.deepcopy(PAYLOAD)
dropped["factors"] = dropped["factors"][1:]
assert rejected(dropped), "checker accepted dropped factor coefficient"

coefficient = copy.deepcopy(PAYLOAD)
coefficient["factors"][0]["numerator"][0] = (
    coefficient["factors"][0]["numerator"][0] + 1
) % 2130706433
assert rejected(coefficient), "checker accepted changed factor coefficient"

multiplicity = copy.deepcopy(PAYLOAD)
multiplicity["factors"][0]["multiplicity"] = 2
assert rejected(multiplicity), "checker accepted changed multiplicity"

print(
    "RATE_HALF_KB_POSITIVE_433_1A_CELL5_PRIMITIVE_FACTORIZATION_MUTATION_PASS "
    "rejected=dropped_coefficient,changed_coefficient,changed_multiplicity"
)
