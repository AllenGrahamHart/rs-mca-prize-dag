#!/usr/bin/env python3
"""Independent checker wrapper for the E25 nine-profile exclusion."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CHECKERS = (
    ("experiments/prize_resolution/e25_nine_profile_census_check.py", "profile=31686 exceptions=31280 full=16984"),
    ("experiments/prize_resolution/e25_nine_profile_norm_check.py", "vectors=16984 distinct=3727 max_bits=249 candidates=0"),
)


def main() -> None:
    for path, marker in CHECKERS:
        completed = subprocess.run(
            [sys.executable, path], cwd=ROOT, capture_output=True, text=True, check=True
        )
        assert marker in completed.stdout
    print("E1_N256_S16_E25_NINE_PROFILE_EXCLUSION_AUDIT_PASS checkers=2 engines=4")


if __name__ == "__main__":
    main()
