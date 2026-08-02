#!/usr/bin/env python3
"""Node-local verifier for the deployed cell-5 rational lift atlas."""

import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
runpy.run_path(str(
    ROOT / "experiments/prize_resolution/"
    "check_rate_half_kb_positive_433_1a_cell5_lift_atlas.py"
), run_name="__main__")
