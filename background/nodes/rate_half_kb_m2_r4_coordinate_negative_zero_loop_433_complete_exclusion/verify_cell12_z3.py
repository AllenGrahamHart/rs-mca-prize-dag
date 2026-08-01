#!/usr/bin/env python3
"""Verify every cell-12 Z3 finite assignment and family."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("check", NODE / "check.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def main():
    assignments = {index: (1120 if index < 4 else 128) for index in range(8)}
    unresolved = {index: (16 if index < 4 else 0) for index in range(8)}
    result = CHECK.verify_rows(12, "Z3", range(8), assignments, unresolved, 1)
    CHECK.require(result == (9984, 128), f"cell12 Z3 totals {result}")
    print("RATE_HALF_KB_ZERO_LOOP_433_COMPLETE_CELL12_Z3_PASS comparisons=9984 families=128")


if __name__ == "__main__":
    main()
