#!/usr/bin/env python3
"""Replay the fixed-mixed off-common projection grid."""

import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
ROUTER = ROOT / (
    "critical/nodes/rate_half_band_closure/notes/"
    "kb_c2_112_aligned_positive_unramified_fixed_off_common.py"
)


completed = subprocess.run(
    [sys.executable, str(ROUTER), "--allocation", "mixed", "--finite-replay"],
    cwd=ROOT,
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    timeout=60,
    check=False,
)
marker = (
    "OFF_COMMON_FINITE_REPLAY_PASS allocation=mixed endpoints=5 boundary=5 "
    "minor_conic_empty=0 w_candidates=0"
)
if completed.returncode != 0 or marker not in completed.stdout:
    raise RuntimeError(f"off-common replay failed:\n{completed.stdout}")
if completed.stdout.count("OFF_COMMON_SCREEN_PASS allocation=mixed") != 20:
    raise RuntimeError("off-common branch count")

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_MIXED_"
    "OFF_COMMON_PASS branches=20 endpoints=5 boundary=5"
)
