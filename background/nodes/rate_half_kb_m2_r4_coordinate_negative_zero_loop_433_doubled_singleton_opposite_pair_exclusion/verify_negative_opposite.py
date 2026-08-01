#!/usr/bin/env python3
"""Audit the (-,+) row of the zero-loop 433 cell-1 exclusion."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("check", NODE / "check.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def main():
    roots = CHECK.check_row(
        -1,1,9,14,1,CHECK.GUARD_POINTS,(5,14,3)
    )
    print(f"RATE_HALF_KB_ZERO_LOOP_433_OPPOSITE_NEG_PASS roots={roots}")


if __name__ == "__main__":
    main()
