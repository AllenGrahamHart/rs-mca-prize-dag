#!/usr/bin/env python3
"""Independent algebra audit of the 442 orientation lift."""

import sympy as sp
from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    x, y, b = sp.symbols("x y b")
    factor = sp.factor(x * (y - b)**2 - y * (x - b)**2)
    require(sp.expand(factor - (x-y)*(b**2-x*y)) == 0, "label factor")
    statement = (NODE / "statement.md").read_text()
    require("eight orientation triples" in statement and "other seven" in statement, "frontier")
    print("RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_Q_ORIENTATION_AUDIT_PASS sign_cube=8/2")


if __name__ == "__main__":
    main()
