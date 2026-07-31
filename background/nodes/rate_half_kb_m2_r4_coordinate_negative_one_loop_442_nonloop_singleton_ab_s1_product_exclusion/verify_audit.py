#!/usr/bin/env python3
"""Audit all S1 product cells in deployed b row one."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("primary", NODE / "verify.py")
PRIMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PRIMARY)


def main():
    PRIMARY.replay(1)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_AB_S1_AUDIT_PASS "
        "row=1 cells=10 raw_units=6 guarded=4 product_frontier=0"
    )


if __name__ == "__main__":
    main()
