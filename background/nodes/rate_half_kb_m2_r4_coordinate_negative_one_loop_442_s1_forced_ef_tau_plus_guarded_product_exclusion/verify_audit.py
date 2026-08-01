#!/usr/bin/env python3
"""Audit tau-plus forced-EF guard emptiness in cubic component one."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("primary", NODE / "verify.py")
PRIMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PRIMARY)


def main():
    PRIMARY.PARENT.factor_audit()
    PRIMARY.replay(1)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S1_EF_PLUS_AUDIT_PASS "
        "component=1 ef_signs=2 terms=19 guard=e pairs=435"
    )


if __name__ == "__main__":
    main()
