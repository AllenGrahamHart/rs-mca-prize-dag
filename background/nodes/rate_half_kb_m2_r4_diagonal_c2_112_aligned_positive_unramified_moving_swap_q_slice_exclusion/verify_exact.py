#!/usr/bin/env python3
"""Replay the three exact deletion stages with per-stage timeouts."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
ROUTER = (
    ROOT
    / "critical/nodes/rate_half_band_closure/notes/"
    "kb_c2_112_aligned_positive_unramified_moving_router.py"
)
CASES = (
    (
        ("--allocation", "swap", "--linear-component"),
        "MOVING_LINEAR_EXCLUSION_PASS allocation=swap",
    ),
    (
        ("--allocation", "swap", "--component", "--finite-replay"),
        "SWAP_FINITE_COMPONENT_REPLAY_PASS",
    ),
    (
        ("--allocation", "swap", "--off-common-screen", "--finite-replay"),
        "SWAP_OFF_COMMON_FINITE_REPLAY_PASS",
    ),
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
        raise RuntimeError(
            f"exact replay failed for {arguments}:\n{completed.stdout}"
        )

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_SWAP_EXACT_PASS "
    "components=2 off_common=true"
)
