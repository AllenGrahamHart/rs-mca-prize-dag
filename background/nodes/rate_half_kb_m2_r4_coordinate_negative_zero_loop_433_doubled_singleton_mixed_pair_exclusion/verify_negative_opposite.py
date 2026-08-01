#!/usr/bin/env python3
"""Audit the (-,+) row of the zero-loop 433 cell-0 exclusion."""

import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("check", NODE / "check.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def main():
    b = CHECK.ROUTER_MODULE.sp.symbols("b")
    extra = (
        (908031539, 681314713),
        (1517828908, 681314713),
    )
    q_points = tuple(sorted(CHECK.GUARD_POINTS+extra))
    root_gcd = (
        b**4-295154008*b**3+359782351*b**2-295154008*b+1
    )
    result = CHECK.check_row(
        -1, 1, root_gcd, q_points, (5, 16, 5)
    )
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_MIXED_NEGATIVE_OPPOSITE_PASS "
        f"eps=-1,1 roots={result[1]} packets=0"
    )


if __name__ == "__main__":
    main()
