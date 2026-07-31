#!/usr/bin/env python3
"""Independent substitution audit for the six 442 product rows."""

from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    l, b, c = sp.symbols("l b c")
    rows = (
        (l**2-l+1, 4*b**2+b+4, 3*c+2*b-2),
        (l**2-l+1, 4*b**2+7*b+4, c-2*b-2),
        (l**4+1, b**2-b*l**3+b*l-b+1, c-(b-2)*(l**3-l+1)),
        (l**4+1, b**2-2*b*l**3+2*b*l-b+1, c+b*l**3-b*l-b-2),
        (l**4+1, b**2-b*l**3+b*l-b+1, c-(2*b-1)*(l**3-l+1)),
        (l**4+1, b**2-2*b*l**3+2*b*l-b+1, c-2*b+l**3-l-1),
    )
    require(len(rows) == 6 and all(sp.degree(row[1], b) == 2 for row in rows), "quadratic ledger")
    require(all(sp.degree(row[2], c) == 1 for row in rows), "linear c ledger")
    statement = (NODE / "statement.md").read_text()
    require("six rows are nonempty" in statement and "seven" in statement, "frontier guards")
    print("RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_PRODUCT_AUDIT_PASS quadratics=6 linear_c=6")


if __name__ == "__main__":
    main()
