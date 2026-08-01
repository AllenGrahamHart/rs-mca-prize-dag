#!/usr/bin/env python3
"""Audit the (+,-) row of the zero-loop cell-2 classifier."""

import importlib.util
from pathlib import Path


NODE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location("check",NODE/"check.py")
CHECK=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


def main():
    b=CHECK.ROUTER.sp.symbols("b")
    q_points=tuple(sorted(CHECK.GUARD_POINTS+(
        (62153462,2097283074),(337249141,2097283074),
    )))
    result=CHECK.check_row(
        1,-1,4,4,b*b-399402603*b+1,(),q_points,(4,7,5)
    )
    print(f"RATE_HALF_KB_ZERO_LOOP_433_FINITE_POS_OPP_PASS result={result}")


if __name__=="__main__":
    main()
