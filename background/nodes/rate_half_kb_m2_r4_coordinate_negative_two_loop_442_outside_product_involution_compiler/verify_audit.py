#!/usr/bin/env python3
"""Independent exact audit of the 442 forced-product norms."""

from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    l, b = sp.symbols("l b")
    rows = (
        (l**2-l+1, 4*b**2+b+4,
         b*l**2+b-l**2+2*l-1, b*l**2-2*b*l+b-l**2-1, 49),
        (l**2-l+1, 4*b**2+7*b+4,
         b*l**2+b-l**2+2*l-1, b*l**2-2*b*l+b-l**2-1, 1),
        (l**4+1, b**2-b*l**3+b*l-b+1,
         2*b*l**2+2*b-l**2+2*l-1, b*l**2-2*b*l+b-2*l**2-2, 784),
        (l**4+1, b**2-2*b*l**3+2*b*l-b+1,
         2*b*l**2+2*b-l**2+2*l-1, b*l**2-2*b*l+b-2*l**2-2, 8464),
        (l**4+1, b**2-b*l**3+b*l-b+1,
         b*l**2-2*b*l+b-2*l**2-2, 2*b*l**2+2*b-l**2+2*l-1, 784),
        (l**4+1, b**2-2*b*l**3+2*b*l-b+1,
         b*l**2-2*b*l+b-2*l**2-2, 2*b*l**2+2*b-l**2+2*l-1, 8464),
    )
    for relation, b_gate, numerator, denominator, expected in rows:
        for factor in (numerator, denominator):
            inner = sp.resultant(b_gate, factor, b)
            require(sp.resultant(relation, inner, l) == expected, "protected norm")

    statement = (NODE / "statement.md").read_text()
    require("{2,7,23}" in statement and "twelve-row Mobius" in statement,
            "scope and characteristic fence")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_OUTSIDE_AUDIT_PASS "
        "protected_norms=12 values=1,49,784,8464"
    )


if __name__ == "__main__":
    main()
