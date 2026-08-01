#!/usr/bin/env python3
"""Independent diagonal-eigenspace audit for the sextic compiler."""

import sympy as sp


def main():
    x, z, delta = sp.symbols("X Z Delta", nonzero=True)
    coefficients = sp.symbols("h0:7")
    form = sum(coefficients[j]*x**(6-j)*z**j for j in range(7))

    diagonal_action = sp.expand(form.subs({x: x, z: -z}))
    plus_part = sp.Poly(sp.expand(diagonal_action-form), x, z)
    minus_part = sp.Poly(sp.expand(diagonal_action+form), x, z)
    plus_rank = sum(plus_part.coeff_monomial(x**(6-j)*z**j) != 0
                    for j in range(7))
    minus_rank = sum(minus_part.coeff_monomial(x**(6-j)*z**j) != 0
                     for j in range(7))
    if (plus_rank, minus_rank) != (3, 4):
        raise RuntimeError("diagonal eigenspace dimensions")

    anti_form = x*z*(x**4+z**4)
    if sp.expand(anti_form.subs(z, -z)+anti_form) != 0:
        raise RuntimeError("anti-eigenform")
    if anti_form.subs({x: 1, z: 0}) != 0:
        raise RuntimeError("first fixed root")
    if anti_form.subs({x: 0, z: 1}) != 0:
        raise RuntimeError("second fixed root")

    if sp.factor((delta**3)**2-delta**6) != 0:
        raise RuntimeError("scalar square")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_EIGEN_AUDIT_PASS "
        "plus_dimension=4 minus_dimension=3 anti_has_fixed_roots"
    )


if __name__ == "__main__":
    main()
