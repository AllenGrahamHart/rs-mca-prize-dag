#!/usr/bin/env python3
"""Verify every cell-13 Z2 finite assignment and family."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("check", NODE / "check.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def main():
    result = CHECK.verify_rows(
        13, "Z2", range(4), {index: 496 for index in range(4)},
        {index: 8 for index in range(4)}, 2,
    )
    CHECK.require(result == (3968, 64), f"cell13 totals {result}")
    print("RATE_HALF_KB_ZERO_LOOP_433_COMPLETE_CELL13_PASS comparisons=3968 families=64")


if __name__ == "__main__":
    main()
