#!/usr/bin/env python3
"""Independent audit of the moving-xi square-xi near chart.

The audit does not import the primary helper. It reconstructs the source by
``DomainMatrix.solve_den`` and derives the finite support from subresultant
sequences after solving the selected linear product branch.
"""

from __future__ import annotations

import argparse
import hashlib
from functools import reduce

import sympy as sp
from sympy.polys.matrices import DomainMatrix


def check(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def edge_vector(x, y):
    return sp.Matrix([x * y, -(x + y), 1])


def rows_at(x):
    return (
        sp.Matrix([[1, x, x**2, 0, 0]]),
        sp.Matrix([[0, 0, 0, 1 + x**2, x]]),
        sp.Matrix([[x**2, x, 1, 0, 0]]),
    )


def digest(polynomial: sp.Poly) -> str:
    payload = repr([
        (monomial, str(coefficient))
        for monomial, coefficient in polynomial.monic().terms()
    ]).encode("ascii")
    return hashlib.sha256(payload).hexdigest()[:16]


def numerator_poly(expression, b, c, d):
    numerator = sp.fraction(sp.cancel(expression))[0]
    return sp.Poly(numerator, b, c, d, domain=sp.QQ).primitive()[1]


def reduce_mod(polynomial: sp.Poly, variable, characteristic: int):
    _, integral = polynomial.clear_denoms(convert=True)
    return sp.Poly(
        integral.as_expr(), variable, modulus=characteristic
    ).monic()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("c_branch", type=int, choices=(0, 1))
    parser.add_argument("d_branch", type=int, choices=(0, 1))
    args = parser.parse_args()

    b, c, d = sp.symbols("b c d", nonzero=True)
    characteristic = 2130706433
    a = sp.Rational(2)
    w = 1 / c
    q0 = c * d
    q1 = -(c + d)
    odd0 = q0 - w
    odd2 = 1 - w * q0
    odd1 = q1 * (1 - w)
    z = sp.cancel(
        -(odd0 + a * odd1 + a**2 * odd2)
        / (odd2 + a * odd1 + a**2 * odd0)
    )
    odd_at_z = sp.Matrix([
        odd0 + z * odd2,
        (1 + z) * odd1,
        odd2 + z * odd0,
    ])
    ell1 = odd_at_z[2]
    ell0 = odd_at_z[1] + a * odd_at_z[2]
    fixed = edge_vector(a, 1 / a)
    moving = edge_vector(a, b)
    interpolation = sp.Matrix([
        sp.cancel(value)
        for value in (
            ((ell0 + b * ell1) * fixed
             + (ell0 + sp.Rational(1, 2) * ell1) * moving)
            / (b - sp.Rational(1, 2))
        )
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

    def residual(root):
        x0, x1, x2, x3, x4 = coefficients
        even0 = sp.cancel(x0 + root * x3 + root**2 * x2)
        even1 = sp.cancel(x1 + root * x4 + root**2 * x1)
        even2 = sp.cancel(x2 + root * x3 + root**2 * x0)
        local_odd0 = sp.cancel(odd0 + root * odd1 + root**2 * odd2)
        local_odd1 = sp.cancel(odd2 + root * odd1 + root**2 * odd0)
        check(
            sp.cancel(even0 + w * even1 + w**2 * even2) == 0,
            "even forced root",
        )
        check(
            sp.cancel(local_odd0 + w * local_odd1) == 0,
            "odd forced root",
        )
        leading = sp.cancel(even2**2)
        middle = sp.cancel(
            2 * even1 * even2 - local_odd1**2 + 2 * w * leading
        )
        constant = sp.cancel(even0**2 / w**2)
        return leading, middle, constant

    residual_c = residual(c)
    residual_d = residual(d)
    conditions = {
        ("c", "product"): residual_c[2] - residual_c[0] / b**2,
        ("c", "sum"): residual_c[1] + 2 * residual_c[0] / b,
        ("d", "product"): residual_d[2] - residual_d[0] / d**2,
        ("d", "sum"): residual_d[1] + 2 * residual_d[0] / d,
    }
    polynomials = {
        key: numerator_poly(value, b, c, d)
        for key, value in conditions.items()
    }
    finite_z = sp.Poly(
        4 * c**2 * d - 2 * c**2 - 3 * c * d + 3 * c + 2 * d - 4,
        b,
        c,
        d,
        domain=sp.QQ,
    ).monic()
    product_branches = {}
    for root_name in ("c", "d"):
        factorization = sp.factor_list(
            polynomials[(root_name, "product")].as_expr()
        )[1]
        cores = [
            sp.Poly(factor, b, c, d, domain=sp.QQ).primitive()[1]
            for factor, _ in factorization
            if sp.Poly(factor, b, c, d).degree(b) > 0
        ]
        other = [
            (sp.Poly(factor, b, c, d, domain=sp.QQ).monic(), exponent)
            for factor, exponent in factorization
            if sp.Poly(factor, b, c, d).degree(b) == 0
        ]
        check(len(cores) == 2, "product branch count")
        check(other == [(finite_z, 2)], "finite-z product factor")
        product_branches[root_name] = sorted(cores, key=digest)
    selected_c = product_branches["c"][args.c_branch]
    selected_d = product_branches["d"][args.d_branch]
    check(selected_c.degree(b) == 2, "c branch degree")
    check(selected_d.degree(b) == 1, "d branch degree")
    print("audit_stage=product_branches", flush=True)

    d_lead = sp.Poly(sp.diff(selected_d.as_expr(), b), c, d, domain=sp.QQ)
    d_constant = sp.Poly(
        selected_d.as_expr().subs(b, 0), c, d, domain=sp.QQ
    )
    b_value = sp.cancel(-d_constant.as_expr() / d_lead.as_expr())

    def substitute(polynomial):
        numerator = sp.fraction(
            sp.cancel(polynomial.as_expr().subs(b, b_value))
        )[0]
        return sp.Poly(numerator, c, d, domain=sp.QQ).primitive()[1]

    projected = [
        substitute(selected_c),
        substitute(polynomials[("c", "sum")]),
        substitute(polynomials[("d", "sum")]),
    ]
    common_input = reduce(sp.gcd, projected).monic()
    reconstruction_factor = 5 * c * d - 4 * c - 4 * d + 5
    expected_common = sp.Poly(
        (c - 1)**(2 if args.c_branch == 0 else 1)
        * (c * d - 1) * reconstruction_factor,
        c,
        d,
        domain=sp.QQ,
    ).monic()
    check(common_input == expected_common, "common forbidden component")
    reduced = [value.exquo(common_input).primitive()[1] for value in projected]

    def final_subresultant(left, right):
        sequence = sp.subresultants(left.as_expr(), right.as_expr(), c)
        value = sp.Poly(sequence[-1], c, d, domain=sp.QQ)
        check(value.degree(c) == 0, "generic subresultant degree")
        return sp.Poly(value.as_expr(), d, domain=sp.QQ).primitive()[1]

    eliminants = [
        final_subresultant(reduced[0], reduced[1]),
        final_subresultant(reduced[0], reduced[2]),
    ]
    common = sp.gcd(*eliminants).monic()
    support = {
        (0, 0): (
            (d - 2) * (d - 1) * (d + 1) * (2 * d - 1)
            * (17 * d**2 - 38 * d + 17)
        ),
        (0, 1): (
            (d - 2) * (d - 1) * (d + 1) * (d + 2)
            * (2 * d - 1) * (2 * d + 1) * (2 * d**2 - 9 * d + 1)
        ),
        (1, 0): (
            (d - 2) * (d - 1) * (d + 1) * (2 * d - 1)
            * (2 * d + 1) * (17 * d**2 - 38 * d + 17)
        ),
        (1, 1): (
            (d - 2) * (d - 1) * (d + 1) * (d + 2)
            * (2 * d - 1) * (2 * d + 1) * (2 * d**2 - 3 * d - 1)
        ),
    }[(args.c_branch, args.d_branch)]
    expected_support = sp.Poly(support, d, domain=sp.QQ).monic()
    check(common.sqf_part().monic() == expected_support, "subresultant support")
    modular_eliminants = [
        reduce_mod(value, d, characteristic) for value in eliminants
    ]
    modular_common = sp.gcd(*modular_eliminants).monic()
    check(
        modular_common.sqf_part().monic()
        == reduce_mod(expected_support, d, characteristic).sqf_part().monic(),
        "KoalaBear subresultant support",
    )
    print("audit_stage=subresultant_support", flush=True)

    exceptional = sp.Poly(
        sp.resultant(d_lead.as_expr(), d_constant.as_expr(), c),
        d,
        domain=sp.QQ,
    ).primitive()[1]
    expected_exception = (
        (d - 2)**3 * (d - 1)**5 * (d + 1)**5 * (2 * d - 1)**3
        * (17 * d**2 - 38 * d + 17)
        if args.d_branch == 0 else
        (d - 2)**2 * (d - 1)**7 * (d + 1)**5 * (d + 2)
        * (2 * d - 1)**2 * (2 * d + 1)
    )
    expected_exception_poly = sp.Poly(
        expected_exception, d, domain=sp.QQ
    ).monic()
    check(exceptional.monic() == expected_exception_poly, "exception support")
    check(
        reduce_mod(exceptional, d, characteristic)
        == reduce_mod(expected_exception_poly, d, characteristic),
        "KoalaBear exception support",
    )

    def integralize(expression, variables):
        _, integral = sp.Poly(
            expression, *variables, domain=sp.QQ
        ).clear_denoms(convert=True)
        return integral.as_expr()

    def assert_basis(expressions, variables, expected):
        actual_qq = sp.groebner(expressions, *variables, order="lex", domain=sp.QQ)
        expected_qq = sp.groebner(expected, *variables, order="lex", domain=sp.QQ)
        check(
            [value.as_expr() for value in actual_qq.polys]
            == [value.as_expr() for value in expected_qq.polys],
            "candidate basis over QQ",
        )
        actual_mod = sp.groebner(
            [integralize(value, variables) for value in expressions],
            *variables,
            order="lex",
            modulus=characteristic,
        )
        expected_mod = sp.groebner(
            [integralize(value, variables) for value in expected],
            *variables,
            order="lex",
            modulus=characteristic,
        )
        check(
            [value.as_expr() for value in actual_mod.polys]
            == [value.as_expr() for value in expected_mod.polys],
            "candidate basis over KoalaBear",
        )
        return actual_qq, actual_mod

    if args.d_branch == 0:
        q17 = 17 * d**2 - 38 * d + 17
        assert_basis(
            [
                selected_c.as_expr(), d_lead.as_expr(), d_constant.as_expr(),
                polynomials[("c", "sum")].as_expr(),
                polynomials[("d", "sum")].as_expr(), q17,
            ],
            (b, c, d),
            (b - sp.Rational(1, 2), 7 * c + 17 * d - 30, q17),
        )
    else:
        for candidate in (d + 2, 2 * d + 1):
            assert_basis(
                [
                    selected_c.as_expr(), d_lead.as_expr(), d_constant.as_expr(),
                    polynomials[("c", "sum")].as_expr(),
                    polynomials[("d", "sum")].as_expr(), candidate,
                ],
                (b, c, d),
                (sp.Integer(1),),
            )

    generic_candidates = {
        (0, 1): (
            2 * d**2 - 9 * d + 1,
            (c + 2 * d - 9, 2 * d**2 - 9 * d + 1),
        ),
        (1, 0): (
            2 * d + 1,
            (13 * c**2 + 12 * c - 28, 2 * d + 1),
        ),
        (1, 1): (
            2 * d**2 - 3 * d - 1,
            (c - 2 * d + 3, 2 * d**2 - 3 * d - 1),
        ),
    }
    if (args.c_branch, args.d_branch) in generic_candidates:
        candidate, relations = generic_candidates[(args.c_branch, args.d_branch)]
        saturation = sp.symbols("saturation")
        actual_qq, actual_mod = assert_basis(
            [
                *(value.as_expr() for value in reduced),
                candidate,
                saturation * d_lead.as_expr() - 1,
            ],
            (saturation, c, d),
            (*relations, saturation * d_lead.as_expr() - 1),
        )
        collision = sp.fraction(sp.cancel(b_value - sp.Rational(1, 2)))[0]
        check(actual_qq.reduce(collision)[1] == 0, "candidate b collision")
        _, integral_collision = sp.Poly(
            collision, c, d, domain=sp.QQ
        ).clear_denoms(convert=True)
        check(
            actual_mod.reduce(integral_collision.as_expr())[1] == 0,
            "KoalaBear candidate b collision",
        )

    overlap_candidates = {
        (0, 0): (
            (17 * d**2 - 38 * d + 17, (sp.Integer(1),), False),
        ),
        (0, 1): (
            (d + 2, (sp.Integer(1),), False),
            (2 * d + 1,
             (c - sp.Rational(14, 13), 2 * d + 1), True),
        ),
        (1, 0): (
            (17 * d**2 - 38 * d + 17, (sp.Integer(1),), False),
        ),
        (1, 1): (
            (d + 2, (sp.Integer(1),), False),
            (2 * d + 1, (sp.Integer(1),), False),
        ),
    }[(args.c_branch, args.d_branch)]
    for candidate, relations, forces_collision in overlap_candidates:
        saturation = sp.symbols("saturation")
        actual_qq, actual_mod = assert_basis(
            [
                *(value.as_expr() for value in reduced),
                candidate,
                saturation * d_lead.as_expr() - 1,
            ],
            (saturation, c, d),
            (
                *relations,
                *((saturation * d_lead.as_expr() - 1,)
                  if relations != (sp.Integer(1),) else ()),
            ),
        )
        if forces_collision:
            collision = sp.fraction(
                sp.cancel(b_value - sp.Rational(1, 2))
            )[0]
            check(actual_qq.reduce(collision)[1] == 0,
                  "overlap b collision")
            _, integral_collision = sp.Poly(
                collision, c, d, domain=sp.QQ
            ).clear_denoms(convert=True)
            check(
                actual_mod.reduce(integral_collision.as_expr())[1] == 0,
                "KoalaBear overlap b collision",
            )

    print(
        "KB_C2_112_NEAR_MOVING_XI_SQUARE_XI_AUDIT_PASS "
        f"pair={args.c_branch},{args.d_branch} characteristic={characteristic} "
        "fraction_free_source=true subresultant_projection=true",
        flush=True,
    )


if __name__ == "__main__":
    main()
