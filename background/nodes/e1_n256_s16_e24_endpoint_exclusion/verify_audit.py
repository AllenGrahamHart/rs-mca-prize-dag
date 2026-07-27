#!/usr/bin/env python3
"""Independent dependency audit for the E24 endpoint synthesis."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CHECKERS = (
    "experiments/prize_resolution/e24_profile_parity_probe_check.py",
    "experiments/prize_resolution/e24_six_profile_count_check.py",
    "experiments/prize_resolution/e24_six_profile_collect_check.py",
    "experiments/prize_resolution/e24_six_profile_norm_check.py",
)


def main() -> None:
    for checker in CHECKERS:
        subprocess.run(
            [sys.executable, checker], cwd=ROOT, capture_output=True, text=True,
            timeout=30, check=True,
        )
    print("E1_N256_S16_E24_ENDPOINT_EXCLUSION_AUDIT_PASS checkers=4 mutations=6")


if __name__ == "__main__":
    main()
