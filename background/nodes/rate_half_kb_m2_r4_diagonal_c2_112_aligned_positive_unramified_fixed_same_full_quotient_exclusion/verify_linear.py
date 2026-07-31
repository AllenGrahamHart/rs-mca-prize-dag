#!/usr/bin/env python3
"""Replay the fixed-same linear component exclusion."""

import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
COMPILER = ROOT / (
    "critical/nodes/rate_half_band_closure/notes/"
    "kb_c2_112_aligned_positive_unramified_flint.py"
)


completed = subprocess.run(
    [
        sys.executable,
        str(COMPILER),
        "fixed-moving",
        "--allocation", "same",
        "--linear-component",
    ],
    cwd=ROOT,
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    timeout=60,
    check=False,
)
marker = "LINEAR_COMPONENT_EXCLUSION_PASS template=fixed-moving allocation=same"
if completed.returncode != 0 or marker not in completed.stdout:
    raise RuntimeError(f"linear replay failed:\n{completed.stdout}")

print("KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_SAME_LINEAR_PASS")
