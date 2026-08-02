#!/usr/bin/env python3
"""Verify the generic cell-5 signed-pair colored exclusion."""

import hashlib
import json
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
basis_path = EXPERIMENTS / (
    "rate_half_kb_positive_433_1a_cell5_pair_function_field_julia_basis_result.json"
)
basis_raw = basis_path.read_bytes()
assert hashlib.sha256(basis_raw).hexdigest() == (
    "576df7138502bf60657c7386d7dbc6eb6a4b9ea60a8f65d3745af3f5fd91820d"
)
basis = json.loads(basis_raw)
assert isinstance(basis, list) and len(basis) == 1
assert basis[0]["status"] == "COMPLETE" and basis[0]["returncode"] == 0
assert basis[0]["field"] == "GF(2130706433)(t)"
assert basis[0]["chart_index"] == 2 and basis[0]["stage"] == "squared-export"
assert basis[0]["program_sha256"] == (
    "fbe8f00d663dd381c1fb1f57e231a04e0645e0c6b839368386f22aaee88737ba"
)
assert "DENOMINATOR_GCD_DEGREES 0,0" in basis[0]["stdout"].splitlines()
runpy.run_path(
    str(EXPERIMENTS / "check_rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd.py"),
    run_name="__main__",
)
runpy.run_path(
    str(EXPERIMENTS / "audit_rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd.py"),
    run_name="__main__",
)
print("positive 433-1a cell-5 generic sign-row colored exclusion verified")
