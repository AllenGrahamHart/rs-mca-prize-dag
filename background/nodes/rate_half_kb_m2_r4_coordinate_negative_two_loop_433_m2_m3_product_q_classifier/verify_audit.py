#!/usr/bin/env python3
"""Independently verify the guarded M2/M3 saturation."""

from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    m, b, c, z = sp.symbols("m b c z")
    u = m**4 + 6*m**2 + 1
    v = (m**2 - 1)**2
    p6 = m**6 + 2*m**5 + 7*m**4 - 4*m**3 + 7*m**2 + 2*m + 1
    a = 2*m**5 + 3*m**4 + 12*m**3 - 14*m**2 + 18*m + 3
    d = 2*m**5 + 5*m**4 + 16*m**3 - 2*m**2 + 6*m + 5
    e = a - 8
    guard = m*b*(b-1)*(b+1)*(m-1)*(m+1)*(m**2+1)

    for epsilon in (-1, 1):
        sign = 1 if epsilon == -1 else -1
        e1 = sp.expand(u*(b*c+1) + sign*v*(b+c))
        e2 = sp.expand((m+1)**2*(b**2-c**2) + sign*(m-1)**2*b*(1-c**2))
        q = sp.expand((4*m**2 if epsilon == -1 else (m**2+1)**2)*(c**2+b)**2
                      + c**2*(1+b)**2*v)
        saturated = sp.groebner((e1, e2, q, z*guard-1), z, c, b, m, order="lex")
        require(saturated.domain == sp.ZZ, "integral saturation")
        univariate = [poly.as_expr() for poly in saturated.polys
                      if not poly.as_expr().has(z, c, b)]
        require(len(univariate) == 1 and sp.expand(univariate[0]-p6) == 0,
                "unique sextic")
        b_poly = 4*b**2 + epsilon*a*b + 4
        c_poly = 8*c + b*d + epsilon*e
        require(saturated.reduce(b_poly)[1] == 0, "saturated quadratic")
        require(saturated.reduce(c_poly)[1] == 0, "saturated locator")

    statement = (NODE / "statement.md").read_text()
    require("total cap" in statement and "seven complementary" in statement,
            "frontier scope")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_M2_M3_AUDIT_PASS "
        "saturations=2 unique_univariate=P6"
    )


if __name__ == "__main__":
    main()
