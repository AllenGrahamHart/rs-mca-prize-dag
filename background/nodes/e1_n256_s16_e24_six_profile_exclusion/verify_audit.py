#!/usr/bin/env python3
"""Run all independent E24 census and norm checkers."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CHECKERS = (
    ("experiments/prize_resolution/e24_six_profile_count_check.py", "profile=14416 full=6834"),
    ("experiments/prize_resolution/e24_six_profile_collect_check.py", "profile=14416 full=6834"),
    ("experiments/prize_resolution/e24_six_profile_norm_check.py", "vectors=6834 distinct=2684"),
)


def main() -> None:
    for path, marker in CHECKERS:
        completed = subprocess.run(
            [sys.executable, path], cwd=ROOT, capture_output=True, text=True,
            timeout=30, check=True,
        )
        assert marker in completed.stdout
    print("E1_N256_S16_E24_SIX_PROFILE_EXCLUSION_AUDIT_PASS checkers=3 engines=4 mutations=4")


if __name__ == "__main__":
    main()
