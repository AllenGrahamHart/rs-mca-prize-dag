#!/usr/bin/env python3
"""Verify every cell-12 Z2 finite assignment and family."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("check", NODE / "check.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def main():
    result = CHECK.verify_rows(
        12, "Z2", range(8), {index: 496 for index in range(8)},
        {index: 8 for index in range(8)}, 0,
    )
    CHECK.require(result == (7936, 128), f"cell12 Z2 totals {result}")
    print("RATE_HALF_KB_ZERO_LOOP_433_COMPLETE_CELL12_Z2_PASS comparisons=7936 families=128")


if __name__ == "__main__":
    main()
