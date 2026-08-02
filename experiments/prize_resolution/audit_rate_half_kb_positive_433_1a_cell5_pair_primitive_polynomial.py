#!/usr/bin/env python3
"""Hostile mutations for the localized-pair primitive polynomial."""

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


HERE = Path(__file__).parent
CHECKER = HERE / "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial.py"
PRIMITIVE = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial_result.json"
)
PAYLOAD = json.loads(PRIMITIVE.read_text())


def rejected(payload):
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "primitive.json"
        path.write_text(json.dumps(payload, sort_keys=True))
        process = subprocess.run(
            [sys.executable, str(CHECKER), "--primitive", str(path)],
            capture_output=True,
            text=True,
            timeout=20,
        )
    return process.returncode != 0


dropped = copy.deepcopy(PAYLOAD)
dropped["coefficients"] = dropped["coefficients"][1:]
assert rejected(dropped), "checker accepted dropped primitive coefficient"

coefficient = copy.deepcopy(PAYLOAD)
coefficient["coefficients"][0]["numerator"][0] = (
    coefficient["coefficients"][0]["numerator"][0] + 1
) % 2130706433
assert rejected(coefficient), "checker accepted changed primitive coefficient"

provenance = copy.deepcopy(PAYLOAD)
provenance["operator_sha256"] = "0" * 64
assert rejected(provenance), "checker accepted changed operator provenance"

print(
    "RATE_HALF_KB_POSITIVE_433_1A_CELL5_PRIMITIVE_POLYNOMIAL_MUTATION_PASS "
    "rejected=dropped_coefficient,changed_coefficient,changed_provenance"
)
