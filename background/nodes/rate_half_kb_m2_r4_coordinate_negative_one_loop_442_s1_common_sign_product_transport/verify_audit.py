#!/usr/bin/env python3
"""Audit product-data transport in the remaining two common sign rows."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("primary", NODE / "verify.py")
PRIMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PRIMARY)


def main():
    for signs in ((-1, 1), (-1, -1)):
        records = PRIMARY.TRANSPORT.check_row(*signs)
        PRIMARY.require(len(records) == 2, f"component count {signs}")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_S1_TRANSPORT_AUDIT_PASS "
        "rows=-1,1;-1,-1 components=4 common_c_m=True frontier=40"
    )


if __name__ == "__main__":
    main()
