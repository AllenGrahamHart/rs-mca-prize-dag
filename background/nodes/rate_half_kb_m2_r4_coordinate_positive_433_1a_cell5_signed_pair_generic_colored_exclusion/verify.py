#!/usr/bin/env python3
"""Verify the generic cell-5 signed-pair colored exclusion."""

import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
runpy.run_path(
    str(EXPERIMENTS / "check_rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd.py"),
    run_name="__main__",
)
runpy.run_path(
    str(EXPERIMENTS / "audit_rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd.py"),
    run_name="__main__",
)
print("positive 433-1a cell-5 generic signed-pair colored exclusion verified")
