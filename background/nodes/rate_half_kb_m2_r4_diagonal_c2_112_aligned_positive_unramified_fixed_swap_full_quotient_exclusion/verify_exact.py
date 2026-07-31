#!/usr/bin/env python3
"""Replay the fixed-swap quotient and off-common exclusions."""

import subprocess
import sys
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NOTES = ROOT / "critical/nodes/rate_half_band_closure/notes"
QUOTIENT = NOTES / (
    "kb_c2_112_aligned_positive_unramified_fixed_swap_full_quotient_probe.py"
)
OFF_COMMON = NOTES / "kb_c2_112_aligned_positive_unramified_fixed_off_common.py"


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
    [sys.executable, str(QUOTIENT)],
    "FULL_QUOTIENT_PROBE_PASS tested=1 rejected=1 survived=0",
)
run(
    [sys.executable, str(OFF_COMMON), "--allocation", "swap", "--finite-replay"],
    "OFF_COMMON_FINITE_REPLAY_PASS allocation=swap endpoints=9 boundary=9",
)

print(
    "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_SWAP_EXACT_PASS "
    "q_slice_survivors=1 rejected=1 off_common=true"
)
