#!/usr/bin/env python3
"""Replay the fast exact moving-mixed full-quotient stages."""

import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"
ROUTER = NOTES / "kb_c2_112_aligned_positive_unramified_moving_router.py"
FULL_QUOTIENT = NOTES / (
    "kb_c2_112_aligned_positive_unramified_moving_mixed_full_quotient_probe.py"
)
OFF_COMMON = NOTES / (
    "kb_c2_112_aligned_positive_unramified_moving_mixed_off_common.py"
)


def run(command, marker):
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=60,
        check=False,
    )
    if completed.returncode != 0 or marker not in completed.stdout:
        raise RuntimeError(f"exact replay failed for {command}:\n{completed.stdout}")


run(
    [sys.executable, str(ROUTER), "--allocation", "mixed", "--linear-component"],
    "MOVING_LINEAR_EXCLUSION_PASS allocation=mixed",
)
run(
    [sys.executable, str(FULL_QUOTIENT)],
    "orientations=4 rejected=4 survived=0",
)
run(
    [sys.executable, str(OFF_COMMON), "--finite-replay"],
    "OFF_COMMON_FINITE_REPLAY_PASS endpoints=6 boundary=6",
)

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_MIXED_EXACT_PASS "
    "deployed_orientations=4 rejected=4 off_common=true"
)
