#!/usr/bin/env python3
"""Replay the fixed-mixed raw linear-rank ledger."""

import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
ROUTER = ROOT / (
    "critical/nodes/rate_half_band_closure/notes/"
    "kb_c2_112_aligned_positive_unramified_fixed_mixed_linear_router.py"
)


completed = subprocess.run(
    [sys.executable, str(ROUTER), "--finite-replay"],
    cwd=ROOT,
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    timeout=60,
    check=False,
)
marker = (
    "LINEAR_FINITE_REPLAY_PASS norm_factors=10 skipped_degree=0 "
    "deployed_endpoints=10 boundary=13 empty=3 survivors=0"
)
if completed.returncode != 0 or marker not in completed.stdout:
    raise RuntimeError(f"linear replay failed:\n{completed.stdout}")

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_MIXED_"
    "LINEAR_PASS norm_factors=10 survivors=0"
)
