#!/usr/bin/env python3
"""Node verifier for generic reducedness of the localized signed pair."""

import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
runpy.run_path(
    str(
        ROOT
        / "experiments/prize_resolution/"
        "check_rate_half_kb_positive_433_1a_cell5_pair_localized_operator.py"
    ),
    run_name="__main__",
)
