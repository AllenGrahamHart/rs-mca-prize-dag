#!/usr/bin/env python3
"""Run the independent exact moving-mixed survivor verifier."""

import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
VERIFIER = ROOT / (
    "critical/nodes/rate_half_band_closure/notes/"
    "kb_c2_112_aligned_positive_unramified_moving_mixed_survivor_verify.py"
)


completed = subprocess.run(
    [sys.executable, str(VERIFIER)],
    cwd=ROOT,
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    timeout=60,
    check=False,
)
marker = "SURVIVOR_VERIFY_PASS total=4 deployed_field=2"
if completed.returncode != 0 or marker not in completed.stdout:
    raise RuntimeError(f"independent survivor replay failed:\n{completed.stdout}")

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_MIXED_"
    "SURVIVOR_AUDIT_PASS total=4 deployed_field=2"
)
