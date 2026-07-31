#!/usr/bin/env python3
"""Replay the fixed-mixed full quotient rejection."""

import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PROBE = ROOT / (
    "critical/nodes/rate_half_band_closure/notes/"
    "kb_c2_112_aligned_positive_unramified_fixed_mixed_degree5_full_quotient_probe.py"
)


completed = subprocess.run(
    [sys.executable, str(PROBE)],
    cwd=ROOT,
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    timeout=60,
    check=False,
)
marker = "FULL_QUOTIENT_PROBE_PASS tested=4 rejected=4 survived=0"
if completed.returncode != 0 or marker not in completed.stdout:
    raise RuntimeError(f"full quotient replay failed:\n{completed.stdout}")

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_MIXED_"
    "QUOTIENT_PASS q_slice_survivors=4 rejected=4"
)
