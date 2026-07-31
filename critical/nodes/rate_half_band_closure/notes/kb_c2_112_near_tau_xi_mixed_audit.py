#!/usr/bin/env python3
"""Independent opposite-projection audit for the reciprocal-xi mixed chart."""

from __future__ import annotations

import hashlib

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


def monic(expression, *variables):
    return sp.Poly(expression, *variables, domain=sp.QQ).monic().as_expr()


def reduce_mod(polynomial: sp.Poly, variable, characteristic):
    _, integral = polynomial.clear_denoms(convert=True)
    return sp.Poly(
        integral.as_expr(), variable, modulus=characteristic
    ).monic()


def digest(polynomial: sp.Poly) -> str:
    payload = repr([
        (term, str(coefficient))
        for term, coefficient in polynomial.monic().terms()
    ])
    return hashlib.sha256(payload.encode("ascii")).hexdigest()[:16]


def main() -> None:
    b, c, d = sp.symbols("b c d", nonzero=True)
    W = sp.Symbol("W")
    a = sp.Rational(2)
    w = 1 / c
    q0 = c * d
    q1 = -c - d
    v0 = q0 - w
    v2 = 1 - w * q0
    v1 = q1 * (1 - w)
    z = sp.cancel(
        -(v0 + a * v1 + a**2 * v2)
        / (v2 + a * v1 + a**2 * v0)
    )
    finite_z_factor = (
        4 * c**2 * d - 2 * c**2 - 3 * c * d + 3 * c + 2 * d - 4
    )
    reconstruction_factor = 5 * c * d - 4 * c - 4 * d + 5

    vz = sp.Matrix([v0 + z * v2, (1 + z) * v1, v2 + z * v0])
    ell1 = vz[2]
    ell0 = vz[1] + 2 * vz[2]
    fixed = edge_vector(a, 1 / a)
    moving = edge_vector(a, b)
    interpolation = sp.Matrix([
        sp.cancel(value)
        for value in (
            (ell0 + b * ell1) * fixed
            + (ell0 + sp.Rational(1, 2) * ell1) * moving
        ) / (b - sp.Rational(1, 2))
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
        check(
            sp.cancel((even0 + even1 * W + even2 * W**2).subs(W, w)) == 0,
            "even forced root",
        )
        check(
            sp.cancel((odd0 + odd1 * W).subs(W, w)) == 0,
            "odd forced root",
        )
        top = sp.cancel(even2**2)
        middle = sp.cancel(2 * even1 * even2 - odd1**2 + 2 * w * top)
        bottom = sp.cancel(even0**2 / w**2)
        return top, middle, bottom

    cores = {}
    for root_name, root in (("c", c), ("d", d)):
        top, middle, bottom = residual_coefficients(root)
        conditions = {
            "product": sp.cancel(bottom - 2 * top / d),
            "sum": sp.cancel(
                middle + (sp.Integer(2) + 1 / d) * top
            ),
        }
        for kind, condition in conditions.items():
            polynomial = sp.Poly(
                sp.fraction(condition)[0], b, c, d, domain=sp.QQ
            ).primitive()[1]
            factors = [
                (sp.Poly(factor, b, c, d, domain=sp.QQ), exponent)
                for factor, exponent in sp.factor_list(polynomial.as_expr())[1]
            ]
            if kind == "product":
                finite = [
                    exponent for factor, exponent in factors
                    if factor.monic().as_expr()
                    == monic(finite_z_factor, b, c, d)
                ]
                unknown = [
                    factor.primitive()[1]
                    for factor, _ in factors
                    if factor.monic().as_expr()
                    != monic(finite_z_factor, b, c, d)
                ]
                check(finite == [2] and len(unknown) == 1,
                      "product factorization")
                core = unknown[0]
                check(
                    (core.degree(b), core.degree(c), core.degree(d))
                    == (2, 6, 5),
                    "product core degree",
                )
            else:
                check(len(factors) == 1 and factors[0][1] == 1,
                      "sum factorization")
                core = factors[0][0].primitive()[1]
                check(
                    (core.degree(b), core.degree(c), core.degree(d))
                    == (2, 10, 7),
                    "sum core degree",
                )
            cores[(root_name, kind)] = core
    print("audit_stage=mixed_cores", flush=True)

    within_c = sp.Poly(
        sp.resultant(
            cores[("c", "product")].as_expr(),
            cores[("c", "sum")].as_expr(),
            b,
        ),
        c,
        d,
        domain=sp.QQ,
    ).primitive()[1]
    within_known = {
        monic(value, c, d)
        for value in (
            d,
            d - 2,
            2 * d - 1,
            c * d - 1,
            reconstruction_factor,
            c - 1,
            c + 1,
        )
    }
    residuals = [
        sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
        for factor, _ in sp.factor_list(within_c.as_expr())[1]
        if sp.Poly(factor, c, d, domain=sp.QQ).monic().as_expr()
        not in within_known
    ]
    check(
        len(residuals) == 1
        and (residuals[0].degree(c), residuals[0].degree(d)) == (8, 6),
        "within-fiber residual curve",
    )
    residual_curve = residuals[0]

    cross_known = {
        "product": {
            monic(value, c, d)
            for value in (
                d - 2,
                c - d,
                c - 1,
                c * d - 1,
                reconstruction_factor,
            )
        },
        "sum": {
            monic(value, c, d)
            for value in (
                c - d,
                c - 1,
                c * d - 1,
                reconstruction_factor,
                finite_z_factor,
            )
        },
    }
    expected_degrees = {
        "product": {(2, 1), (6, 5)},
        "sum": {(1, 1), (4, 3), (10, 8)},
    }
    projections = {}
    for kind in ("product", "sum"):
        cross = sp.Poly(
            sp.resultant(
                cores[("c", kind)].as_expr(),
                cores[("d", kind)].as_expr(),
                b,
            ),
            c,
            d,
            domain=sp.QQ,
        ).primitive()[1]
        selected = [
            sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
            for factor, _ in sp.factor_list(cross.as_expr())[1]
            if sp.Poly(factor, c, d, domain=sp.QQ).monic().as_expr()
            not in cross_known[kind]
        ]
        check(
            {(value.degree(c), value.degree(d)) for value in selected}
            == expected_degrees[kind]
            and len(selected) == len(expected_degrees[kind]),
            "cross factor classification",
        )
        aggregate = sp.Poly(1, c, domain=sp.QQ)
        for factor in selected:
            aggregate *= sp.Poly(
                sp.resultant(
                    residual_curve.as_expr(), factor.as_expr(), d
                ),
                c,
                domain=sp.QQ,
            ).primitive()[1]
        projections[kind] = aggregate.primitive()[1]
        print(
            f"audit_stage=projection kind={kind} "
            f"degree={projections[kind].degree()} "
            f"digest={digest(projections[kind])}",
            flush=True,
        )

    expected = sp.Poly(
        (c - 2) * (c - 1) * (2 * c - 1), c, domain=sp.QQ
    ).monic()
    common = sp.gcd(
        projections["product"], projections["sum"]
    ).sqf_part().monic()
    check(common == expected, "opposite support gcd")
    characteristic = 2130706433
    modular_common = sp.gcd(
        reduce_mod(projections["product"], c, characteristic),
        reduce_mod(projections["sum"], c, characteristic),
    ).sqf_part().monic()
    check(
        modular_common == reduce_mod(expected, c, characteristic),
        "opposite deployed-characteristic support gcd",
    )
    print(
        "KB_C2_112_NEAR_TAU_XI_MIXED_AUDIT_PASS "
        f"support_degree={common.degree()} characteristic={characteristic}"
    )


if __name__ == "__main__":
    main()
