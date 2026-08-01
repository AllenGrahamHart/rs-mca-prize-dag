#!/usr/bin/env python3
"""Exact loop-q exclusion for the aligned one-loop 442 families."""

import sympy as sp


PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def is_zero(basis, expression):
    return basis.reduce(sp.expand(expression))[1] == 0


def is_unit(relations, variables, extra):
    basis = sp.groebner(
        [*relations, extra], *variables, order="grevlex", modulus=PRIME
    )
    return len(basis.polys) == 1 and basis.polys[0].as_expr() == 1


def verify_family_a():
    w, r, iota = sp.symbols("w r iota")
    relations = (iota**2+1, r**2+r+1)
    variables = (iota, r)
    basis = sp.groebner(
        relations, *variables, order="grevlex", modulus=PRIME
    )
    b = iota*r
    c = iota*r**2
    scale = (1-c)*(1-iota)
    b_0 = b*scale
    b_2 = scale*w
    a_1 = -(1+b)*(w-c)*(w-iota)
    labels = (c, 1, -1, r**2, -r**2)
    products = (-b**2, b, -b, c, -c)
    q_values = (0, 1+b, iota*(1-b), r*(1+c), iota*r*(1-c))
    for label, product, q_value in zip(labels, products, q_values):
        require(
            is_zero(basis, b_0-product*b_2.subs(w, label)),
            "family A product interpolation",
        )
        require(
            is_zero(
                basis,
                a_1.subs(w, label)+q_value*b_2.subs(w, label),
            ),
            "family A q interpolation",
        )
    require(is_zero(basis, b**2*c**2-1), "family A product norm")
    require(
        is_zero(basis, b_0-r*b_2.subs(w, iota)),
        "family A second-loop product",
    )
    for sign_product in (1, -1):
        require(
            is_unit(relations, variables, r**2+sign_product),
            "family A S1 contradiction",
        )
    require(
        is_unit(relations, variables, b**2-r),
        "family A S2 contradiction",
    )
    for forbidden in (1+b, c-iota, scale):
        require(
            is_unit(relations, variables, forbidden),
            "family A protected factor",
        )


def verify_family_b():
    w, b, iota = sp.symbols("w b iota")
    relations = (iota**2+1, iota*b**2+b-iota)
    variables = (iota, b)
    basis = sp.groebner(
        relations, *variables, order="grevlex", modulus=PRIME
    )
    c = iota-b
    r = -1-iota*b
    scale = 1-iota
    b_0 = b*scale*w
    b_2 = scale
    a_1 = -(w+b)*(w-iota)
    labels = (-b, 1, -1, r**2, -r**2)
    products = (-b**2, b, -b, c, -c)
    q_values = (0, 1+b, iota*(1-b), r*(1+c), iota*r*(1-c))
    for label, product, q_value in zip(labels, products, q_values):
        require(
            is_zero(basis, b_0.subs(w, label)-product*b_2),
            "family B product interpolation",
        )
        require(
            is_zero(basis, a_1.subs(w, label)+q_value*b_2),
            "family B q interpolation",
        )
    require(is_zero(basis, b**2*c**2-1), "family B product norm")
    require(
        is_zero(basis, b_0.subs(w, iota)-iota*b*b_2),
        "family B second-loop product",
    )
    for sign_product in (1, -1):
        require(
            is_unit(relations, variables, b**2-sign_product),
            "family B S1 contradiction",
        )
    require(
        is_unit(relations, variables, b**2-iota*b),
        "family B S2 contradiction",
    )
    for forbidden in (scale, b+iota):
        require(
            is_unit(relations, variables, forbidden),
            "family B protected factor",
        )


def verify():
    verify_family_a()
    verify_family_b()


def main():
    verify()
    print(
        "RATE_HALF_KB_ONE_LOOP_442_ALIGNED_LOOP_Q_PASS "
        "families=2 retained_product_branches=3 loop_q_survivors=0"
    )


if __name__ == "__main__":
    main()
