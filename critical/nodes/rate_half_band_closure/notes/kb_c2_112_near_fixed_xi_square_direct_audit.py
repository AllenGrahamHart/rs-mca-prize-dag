#!/usr/bin/env python3
"""Independent Bezout audit for near square-chart exclusions.

This checker does not import the primary implementation.  It obtains the
source coefficients by a fraction-free DomainMatrix solve.  On each generic
endpoint curve it computes two Bezout identities over Q(d)[c]; the gcd of
their cleared denominators has only forbidden label roots.  Exceptional left
lines are eliminated in d, the opposite direction from the primary check.
The ``--swap`` flag interchanges the two assigned residual roots.
"""

from __future__ import annotations

import argparse

import sympy as sp
from sympy.polys.matrices import DomainMatrix


def check(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError(label)


def edge_vector(x, y):
    return sp.Matrix([x * y, -x - y, 1])


def rows_at(x):
    return (
        sp.Matrix([[1, x, x**2, 0, 0]]),
        sp.Matrix([[0, 0, 0, 1 + x**2, x]]),
        sp.Matrix([[x**2, x, 1, 0, 0]]),
    )


def canonical(expression, *variables):
    return sp.Poly(expression, *variables, domain=sp.QQ).monic().as_expr()


def reduce_mod(polynomial: sp.Poly, variable, characteristic):
    _, integral = polynomial.clear_denoms(convert=True)
    return sp.Poly(
        integral.as_expr(), variable, modulus=characteristic
    ).monic()


def clear_bezout_denominator(curve, middle, c, d):
    field = sp.QQ.frac_field(d)
    curve_field = sp.Poly(curve.as_expr(), c, domain=field)
    middle_field = sp.Poly(middle.as_expr(), c, domain=field)
    left, right, gcd = sp.gcdex(curve_field, middle_field)
    check(gcd.monic().as_expr() == 1, "nontrivial curve-middle gcd")

    denominator = sp.Poly(1, d, domain=sp.QQ)
    for coefficient in left.all_coeffs() + right.all_coeffs():
        _, value = sp.fraction(sp.cancel(coefficient.as_expr()))
        denominator = sp.lcm(denominator, sp.Poly(value, d, domain=sp.QQ))
    identity = sp.cancel(
        (left * curve_field + right * middle_field).as_expr()
        * denominator.as_expr() - denominator.as_expr()
    )
    check(identity == 0, "Bezout identity")
    return denominator.primitive()[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("left", type=int, choices=(0, 1))
    parser.add_argument("right", type=int, choices=(0, 1))
    parser.add_argument("--swap", action="store_true")
    args = parser.parse_args()

    b, c, d = sp.symbols("b c d", nonzero=True)
    characteristic = 2130706433
    W = sp.Symbol("W")
    a = sp.Rational(2)
    w = 1 / c
    q0 = c * d
    q1 = -c - d
    v0 = q0 - w
    v2 = 1 - w * q0
    v1 = q1 * (1 - w)
    z = sp.cancel(-(v0 + a * v1 + a**2 * v2)
                  / (v2 + a * v1 + a**2 * v0))
    vz = sp.Matrix([v0 + z * v2, (1 + z) * v1, v2 + z * v0])
    ell1 = vz[2]
    ell0 = vz[1] + 2 * vz[2]
    fixed = edge_vector(a, 1 / a)
    moving = edge_vector(a, b)
    interpolation = sp.Matrix([
        sp.cancel(value)
        for value in ((ell0 + b * ell1) * fixed
                      + (ell0 + sp.Rational(1, 2) * ell1) * moving)
        / (b - sp.Rational(1, 2))
    ])

    at_w = rows_at(w)
    at_z = rows_at(z)
    source_matrix = sp.Matrix.vstack(
        at_w[0] - q0 * at_w[2],
        at_w[1] - q1 * at_w[2],
        *at_z,
    )
    source_rhs = sp.Matrix([0, 0, *interpolation])
    domain_matrix = DomainMatrix.from_Matrix(source_matrix)
    domain_rhs = DomainMatrix.from_Matrix(source_rhs)
    domain_matrix, domain_rhs = domain_matrix.unify(domain_rhs, fmt="dense")
    numerator, denominator = domain_matrix.solve_den(domain_rhs)
    check(
        domain_matrix.matmul(numerator) == domain_rhs.scalarmul(denominator),
        "fraction-free source identity",
    )
    denominator_expression = domain_matrix.domain.to_sympy(denominator)
    coefficients = [
        sp.cancel(value / denominator_expression)
        for value in numerator.to_Matrix()
    ]
    print("audit_stage=fraction_free_source", flush=True)

    def residual_coefficients(root):
        x0, x1, x2, x3, x4 = coefficients
        even0 = x0 + root * x3 + root**2 * x2
        even1 = x1 + root * x4 + root**2 * x1
        even2 = x2 + root * x3 + root**2 * x0
        odd0 = v0 + root * v1 + root**2 * v2
        odd1 = v2 + root * v1 + root**2 * v0
        norm4 = sp.cancel(even2**2)
        norm3 = sp.cancel(2 * even1 * even2 - odd1**2)
        norm0 = sp.cancel(even0**2)
        quotient2 = norm4
        quotient1 = sp.cancel(norm3 + 2 * w * norm4)
        quotient0 = sp.cancel(norm0 / w**2)
        check(sp.cancel(
            (even0 + even1 * W + even2 * W**2).subs(W, w)
        ) == 0, "even forced root")
        check(sp.cancel((odd0 + odd1 * W).subs(W, w)) == 0,
              "odd forced root")
        return quotient2, quotient1, quotient0

    line_pairs = []
    middle_conditions = []
    finite_z_factor = (
        4 * c**2 * d - 2 * c**2 - 3 * c * d + 3 * c + 2 * d - 4
    )
    targets = (
        ((c, 1 / d), (d, sp.Rational(1, 2)))
        if args.swap else
        ((c, sp.Rational(1, 2)), (d, 1 / d))
    )
    for root, wanted in targets:
        top, middle, bottom = residual_coefficients(root)
        ratio_condition = sp.cancel(bottom - wanted**2 * top)
        middle_condition = sp.cancel(middle + 2 * wanted * top)
        ratio_numerator, _ = sp.fraction(ratio_condition)
        factorization = sp.factor_list(ratio_numerator)[1]
        lines = [
            sp.Poly(value, b, c, d, domain=sp.QQ)
            for value, _ in factorization
            if sp.Poly(value, b, c, d).degree(b) == 1
        ]
        other = [
            (canonical(value, b, c, d), power)
            for value, power in factorization
            if sp.Poly(value, b, c, d).degree(b) != 1
        ]
        check(len(lines) == 2, "audit endpoint split")
        check(other == [(canonical(finite_z_factor, b, c, d), 2)],
              "audit finite-z saturation")
        line_pairs.append(lines)
        middle_conditions.append(middle_condition)
    print("audit_stage=endpoint_lines", flush=True)

    left_line = line_pairs[0][args.left]
    lead = sp.diff(left_line.as_expr(), b)
    constant = left_line.as_expr().subs(b, 0)
    b_generic = sp.cancel(-constant / lead)
    old_lead = left_line.coeff_monomial(b)
    old_constant = left_line.coeff_monomial(1)
    old_b = sp.cancel(-old_constant / old_lead)
    check(sp.cancel(b_generic - old_b) != 0,
          "audit exact-monomial mutation fence")
    middle_polynomials = []
    for condition in middle_conditions:
        value, _ = sp.fraction(sp.cancel(condition.subs(b, b_generic)))
        middle_polynomials.append(
            sp.Poly(value, c, d, domain=sp.QQ).primitive()[1]
        )

    known = {
        canonical(c - 1, c, d),
        canonical(c * d - 1, c, d),
        canonical(5 * c * d - 4 * c - 4 * d + 5, c, d),
    }
    if args.swap:
        known.update({canonical(d - 1, c, d), canonical(d + 1, c, d)})
    forbidden_d = sp.Poly(
        (d - 2) * (d - 1) * (d + 1) * (2 * d - 1), d, domain=sp.QQ
    ).monic()
    for right_index in (args.right,):
        right_line = line_pairs[1][right_index]
        endpoint_elimination = sp.resultant(
            left_line.as_expr(), right_line.as_expr(), b
        )
        factors = [
            sp.Poly(value, c, d, domain=sp.QQ)
            for value, power in sp.factor_list(endpoint_elimination)[1]
            for _ in range(power)
        ]
        curves = [value for value in factors
                  if value.monic().as_expr() not in known]
        expected_factor_count = 5 if args.swap else 4
        check(len(factors) == expected_factor_count and len(curves) == 1,
              "audit endpoint curve")
        denominators = [
            clear_bezout_denominator(curves[0], middle, c, d)
            for middle in middle_polynomials
        ]
        common = sp.gcd(*denominators).monic()
        expected_generic = forbidden_d
        if args.swap and (args.left, right_index) == (1, 0):
            expected_generic = sp.Poly(
                (d - 1) * (d + 1) * (2 * d - 1), d, domain=sp.QQ
            ).monic()
        check(common.sqf_part().monic() == expected_generic,
              "audit generic noncollision support")
        modular_denominators = [
            reduce_mod(value, d, characteristic)
            for value in denominators
        ]
        modular_common = sp.gcd(*modular_denominators).monic()
        check(
            modular_common.sqf_part().monic()
            == reduce_mod(expected_generic, d, characteristic),
              "audit KoalaBear generic support")
        print(
            f"audit_stage=generic pair={args.left},{right_index} "
            f"bezout_degrees={tuple(value.degree() for value in denominators)} "
            f"gcd_degree={common.degree()}",
            flush=True,
        )

    opposite = sp.Poly(
        sp.resultant(lead, constant, d), c, domain=sp.QQ
    ).primitive()[1]
    forbidden_c = sp.Poly(
        (c - 2) * (c - 1) * (c + 1) * (2 * c - 1), c, domain=sp.QQ
    )
    if args.swap and args.left == 0:
        exceptional_factor = 7 * c**2 - 22 * c + 7
        expected_support = (
            forbidden_c * sp.Poly(exceptional_factor, c, domain=sp.QQ)
        )
    elif args.swap:
        expected_support = (
            forbidden_c * sp.Poly((c + 2) * (2 * c + 1), c, domain=sp.QQ)
        )
    elif args.left == 0:
        expected_support = forbidden_c * sp.Poly(5 * c - 1, c, domain=sp.QQ)
    else:
        expected_support = (
            forbidden_c * sp.Poly((2 * c + 1) * (7 * c + 5), c, domain=sp.QQ)
        )
    check(opposite.sqf_part().monic() == expected_support.monic(),
          "audit exceptional opposite support")
    check(
        reduce_mod(opposite, c, characteristic).sqf_part().monic()
        == reduce_mod(expected_support, c, characteristic),
        "audit KoalaBear exceptional support",
    )
    if args.swap and args.left == 0:
        exceptional_basis = sp.groebner(
            [lead, constant, exceptional_factor], c, d, order="lex"
        )
        check(
            exceptional_basis.reduce(5 * c * d - 4 * c - 4 * d + 5)[1] == 0,
            "audit swapped exceptional component",
        )
    elif args.swap:
        for special_c, expected_d in (
            (sp.Rational(-1, 2), d - 2),
            (sp.Rational(-2), 2 * d - 1),
        ):
            d_gcd = sp.gcd(
                sp.Poly(lead.subs(c, special_c), d, domain=sp.QQ),
                sp.Poly(constant.subs(c, special_c), d, domain=sp.QQ),
            ).monic()
            check(
                d_gcd == sp.Poly(expected_d, d, domain=sp.QQ).monic(),
                "audit swapped exceptional fiber",
            )
    elif args.left == 1:
        minus_half = sp.Rational(-1, 2)
        d_gcd = sp.gcd(
            sp.Poly(lead.subs(c, minus_half), d, domain=sp.QQ),
            sp.Poly(constant.subs(c, minus_half), d, domain=sp.QQ),
        ).monic()
        expected = sp.Poly((d - 2) * (2 * d - 1), d, domain=sp.QQ).monic()
        check(d_gcd == expected, "audit c=-1/2 fiber")
    if not args.swap:
        exceptional_c = (
            sp.Rational(1, 5) if args.left == 0 else sp.Rational(-5, 7)
        )
        extra_d = (
            sp.Rational(7, 5) if args.left == 0 else sp.Rational(55, 53)
        )
        check(sp.cancel(
            (5 * c * d - 4 * c - 4 * d + 5).subs(
                {c: exceptional_c, d: extra_d}
            )
        ) == 0, "audit exceptional z=1 point")

    print(
        "KB_C2_112_NEAR_FIXED_XI_SQUARE_DIRECT_AUDIT_PASS "
        f"pair={args.left},{args.right} generic_pairs=1 "
        "opposite_exception_elimination=true "
        f"allocation={'swapped' if args.swap else 'direct'} "
        f"characteristic={characteristic} mutation_catches=1"
    )


if __name__ == "__main__":
    main()
