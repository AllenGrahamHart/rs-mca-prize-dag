#!/usr/bin/env python3
"""Independent chart-boundary audit for the 433 M1 exclusion."""

from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    r = sp.symbols("r")
    boundary_q = r**5-r+2
    require(sp.resultant(r**6+1,boundary_q,r) == 4, "boundary resultant")
    statement = (NODE/"statement.md").read_text()
    require("M2,M3" in statement and "other seven" in statement, "frontier")
    print("RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_M1_AUDIT_PASS boundary_resultant=4")


if __name__ == "__main__":
    main()
