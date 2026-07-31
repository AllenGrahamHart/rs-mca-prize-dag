#!/usr/bin/env python3
"""Independent exact audit of the forced outside product."""

from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    m, b = sp.symbols("m b")
    p6 = m**6 + 2*m**5 + 7*m**4 - 4*m**3 + 7*m**2 + 2*m + 1
    a_poly = 2*m**5 + 3*m**4 + 12*m**3 - 14*m**2 + 18*m + 3
    for epsilon in (-1, 1):
        b_poly = 4*b**2 + epsilon*a_poly*b + 4
        factors = (
            b*(m+1)**2-epsilon*(m-1)**2,
            b*(m-1)**2-epsilon*(m+1)**2,
        )
        for factor in factors:
            inner = sp.resultant(b_poly, factor, b)
            require(sp.resultant(p6, inner, m) == 2**32, "protected factor")

    text = (NODE / "statement.md").read_text()
    require("paired-product rank gate" in text and "twelve-row product interpolation" in text,
            "scope boundary")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_OUTSIDE_AUDIT_PASS "
        "protected_resultants=4 value=2^32"
    )


if __name__ == "__main__":
    main()
