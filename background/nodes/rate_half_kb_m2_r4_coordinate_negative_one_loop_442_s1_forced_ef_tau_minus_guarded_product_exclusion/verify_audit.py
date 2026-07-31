#!/usr/bin/env python3
"""Audit tau-minus forced-EF guard emptiness in cubic component one."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("primary", NODE / "verify.py")
PRIMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PRIMARY)


def main():
    PRIMARY.PARENT.PARENT.factor_audit()
    PRIMARY.PARENT.replay(1, delta_sign=1, expected_terms=(17, 17, 17))
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S1_EF_MINUS_AUDIT_PASS "
        "component=1 ef_signs=2 terms=17 guard=e pairs=435"
    )


if __name__ == "__main__":
    main()
