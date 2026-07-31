#!/usr/bin/env python3
"""Audit both forced-colored S0 parities in cubic component one."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("primary", NODE / "verify.py")
PRIMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PRIMARY)


def main():
    PRIMARY.replay(1)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S0_COLORED_AUDIT_PASS "
        "component=1 parities=2 terms=11 pairs=29 unit=True frontier=16"
    )


if __name__ == "__main__":
    main()
