#!/usr/bin/env python3
"""Mutation audit for the complete cell-5 sign-row partition."""

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
sys.path.insert(0, str(EXPERIMENTS))
import check_rate_half_kb_positive_433_1a_cell5_complete_sign_row as checker


bad = list(checker.raw.FIBERS)
bad[-1] = bad[-1] + 1
try:
    checker.verify(raw_values=bad)
except checker.CertificateError:
    pass
else:
    raise AssertionError("partition mutation accepted")

print("positive 433-1a cell-5 complete sign-row audit verified mutations=1")
