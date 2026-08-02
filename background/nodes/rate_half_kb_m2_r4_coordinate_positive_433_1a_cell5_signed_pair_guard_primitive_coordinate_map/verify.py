#!/usr/bin/env python3
"""Node verifier for the signed-pair primitive coordinate map."""

import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
runpy.run_path(
    str(
        ROOT
        / "experiments/prize_resolution"
        / "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map.py"
    ),
    run_name="__main__",
)
