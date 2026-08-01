#!/usr/bin/env python3
"""Audit the (-,-) row of the zero-loop cell-2 classifier."""

import importlib.util
from pathlib import Path


NODE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location("check",NODE/"check.py")
CHECK=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def main():
    b=CHECK.ROUTER.sp.symbols("b")
    root_gcd=(
        b**8+502371476*b**7-181830825*b**6-372406267*b**5
        -987253675*b**4-372406267*b**3-181830825*b**2+502371476*b+1
    )
    packets=(
        (8467609,2130706431,399245749,583634934),
        (1061119412,1065353216,399245749,583634934),
        (1069587021,1065353216,1764884040,1547071505),
        (2122238824,2130706431,1764884040,1547071505),
    )
    q_points=tuple(sorted(CHECK.GUARD_POINTS+(
        (0,16711679),(325967730,1498820826),(1302367233,1498820826),
    )))
    result=CHECK.check_row(
        -1,-1,8,18,root_gcd,packets,q_points,(4,16,5)
    )
    print(f"RATE_HALF_KB_ZERO_LOOP_433_FINITE_NEG_SAME_PASS result={result}")


if __name__=="__main__":
    main()
