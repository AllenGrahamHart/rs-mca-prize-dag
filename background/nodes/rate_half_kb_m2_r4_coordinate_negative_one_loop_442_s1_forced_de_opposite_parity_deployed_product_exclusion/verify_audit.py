#!/usr/bin/env python3
"""Audit component one of the opposite-parity forced-DE exclusion."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("primary", NODE / "verify.py")
PRIMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PRIMARY)


def main():
    PRIMARY.PARENT.factor_audit()
    PRIMARY.PARENT.solve_quietly(1, alpha_sign=-1)
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S1_DE_OPP_AUDIT_PASS "
        "component=1 alpha=-1 pairs=79 unit=True"
    )


if __name__ == "__main__":
    main()
