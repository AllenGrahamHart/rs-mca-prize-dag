#!/usr/bin/env python3
"""Audit the (-,-) row of the zero-loop 433 cell-0 exclusion."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("check", NODE / "check.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def main():
    result = CHECK.check_row(
        -1, -1, 1, CHECK.GUARD_POINTS, (5, 20, 3)
    )
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_MIXED_NEGATIVE_SAME_PASS "
        f"eps=-1,-1 roots={result[1]} packets=0"
    )


if __name__ == "__main__":
    main()
