#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    checks = (
        ("experiments/prize_resolution/e13_four_profile_census_check.py", "profile=820 full=136"),
        ("experiments/prize_resolution/e13_four_profile_norm_check.py", "odd_hits=4 engines=2 mutations=1"),
        ("experiments/prize_resolution/e13_large_odd_candidate_check.py", "primes=0 congruent=4 eligible=0"),
    )
    for path, marker in checks:
        run = subprocess.run([sys.executable, path], cwd=ROOT, capture_output=True,
                             text=True, timeout=30, check=True)
        assert marker in run.stdout
    print("E1_N256_S16_E13_FOUR_PROFILE_EXCLUSION_AUDIT_PASS checkers=3 engines=6 mutations=3")


if __name__ == "__main__":
    main()
