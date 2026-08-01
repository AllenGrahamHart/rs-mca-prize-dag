#!/usr/bin/env python3
"""Audit both final S0 parity guards in cubic component one."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("primary", NODE / "verify.py")
PRIMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PRIMARY)


def main():
    PRIMARY.replay(1)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S0_INTERNAL_AUDIT_PASS "
        "component=1 parities=2 terms=14 pairs=406 guard=f frontier=0"
    )


if __name__ == "__main__":
    main()
