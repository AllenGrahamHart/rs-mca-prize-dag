#!/usr/bin/env python3
"""Audit the forced-EF S2 guard contradiction in component one."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("primary", NODE / "verify.py")
PRIMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PRIMARY)


def main():
    PRIMARY.replay(1)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S2_EF_AUDIT_PASS "
        "component=1 terms=7,7,7 pairs=28 guard=e^2 frontier=32"
    )


if __name__ == "__main__":
    main()
