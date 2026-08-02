#!/usr/bin/env python3
"""Verify the first finite-candidate exclusion batch."""

import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
runpy.run_path(
    str(
        ROOT
        / "experiments/prize_resolution/check_rate_half_kb_positive_433_1a_cell5_finite_candidate_batch.py"
    ),
    run_name="__main__",
)
print("positive 433-1a cell-5 finite candidate first batch verified")
