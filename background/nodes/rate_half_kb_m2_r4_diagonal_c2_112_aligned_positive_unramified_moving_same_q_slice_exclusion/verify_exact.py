#!/usr/bin/env python3
"""Replay the exact moving-same deletion stages."""

import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
ROUTER = (
    ROOT / "critical/nodes/rate_half_band_closure/notes/"
    "kb_c2_112_aligned_positive_unramified_moving_router.py"
)
CASES = (
    (("--allocation", "same", "--linear-component"),
     "MOVING_LINEAR_EXCLUSION_PASS allocation=same"),
    (("--allocation", "same", "--component-resultant-screen", "--finite-replay"),
     "DIRECT_FINITE_COMPONENT_REPLAY_PASS allocation=same"),
    (("--allocation", "same", "--off-common-screen", "--finite-replay"),
     "OFF_COMMON_FINITE_REPLAY_PASS allocation=same"),
)


for arguments, marker in CASES:
    completed = subprocess.run(
        [sys.executable, str(ROUTER), *arguments],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=60,
        check=False,
    )
    if completed.returncode != 0 or marker not in completed.stdout:
        raise RuntimeError(f"exact replay failed for {arguments}:\n{completed.stdout}")

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_SAME_EXACT_PASS "
    "components=2 off_common=true"
)
