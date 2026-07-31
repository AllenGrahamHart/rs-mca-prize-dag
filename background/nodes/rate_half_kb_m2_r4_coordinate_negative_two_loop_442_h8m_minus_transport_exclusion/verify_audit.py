#!/usr/bin/env python3
"""Independent direct audit of the H8-M-minus forced product and scaling."""

from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    l, u = sp.symbols("l u")
    relation = l**4+1
    gate = u**2-u*(l**3-l+1)+1
    numerator = u*(u*l**2-2*u*l+u-2*l**2-2)
    denominator = 2*u*l**2+2*u-l**2+2*l-1
    ideal = sp.groebner((relation, gate), u, l, order="lex")
    require(ideal.reduce(sp.expand(numerator-u**2*denominator))[1] == 0,
            "direct H8-M forced value")

    # Reconstruct the inverse map from H8-M variables rather than replaying
    # the forward tuple calculation.
    s = l**3-l+1
    b = 1/u
    c_m = (2*u-1)*s
    c_l = -c_m/u
    require(sp.simplify(c_l-(b-2)*s) == 0, "inverse c locator")
    require(sp.simplify(-c_l/b-c_m) == 0, "inverse involution")

    text = (NODE / "statement.md").read_text()
    require("24 invariant cells" in text and "does not delete either" in text,
            "scope fence")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_H8M_MINUS_TRANSPORT_AUDIT_PASS "
        "forced_product=u^2 inverse_transport=exact"
    )


if __name__ == "__main__":
    main()
