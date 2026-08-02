#!/usr/bin/env python3
"""Verify the final eight raw-basis fiber exclusions."""

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
sys.path.insert(0, str(EXPERIMENTS))
import check_rate_half_kb_positive_433_1a_cell5_raw_fiber_replay as checker


checker.verify()
print("positive 433-1a cell-5 raw-basis fiber exclusion verified")
