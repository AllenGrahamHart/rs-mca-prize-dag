#!/usr/bin/env python3
"""Exact branch projection for the unresolved moving-xi swapped square chart."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
from functools import reduce
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
DIRECT = HERE / "kb_c2_112_near_fixed_xi_square_direct.py"


def load_direct():
    spec = importlib.util.spec_from_file_location("near_square_direct", DIRECT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load direct reconstruction helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(polynomial: sp.Poly) -> str:
    payload = repr([
        (monomial, str(coefficient))
        for monomial, coefficient in polynomial.monic().terms()
    ]).encode("ascii")
    return hashlib.sha256(payload).hexdigest()[:16]


def numerator_poly(expression, *variables):
    numerator = sp.fraction(sp.cancel(expression))[0]
    return sp.Poly(numerator, *variables, domain=sp.QQ).primitive()[1]


def reduce_mod(polynomial: sp.Poly, *variables, characteristic: int):
    _, integral = polynomial.clear_denoms(convert=True)
    return sp.Poly(
        integral.as_expr(), *variables, modulus=characteristic
    ).monic()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("c_branch", type=int, choices=(0, 1))
    parser.add_argument("d_branch", type=int, choices=(0, 1))
    candidate_names = (
        "dmhalf", "q17", "q21", "q23", "q5", "q11", "q00cubic",
    )
    parser.add_argument("--fiber", choices=candidate_names)
    parser.add_argument("--exception", choices=candidate_names)
    parser.add_argument("--prove", action="store_true")
    args = parser.parse_args()

    direct = load_direct()
    b, c, d = sp.symbols("b c d", nonzero=True)
    a = sp.Rational(2)
    w = 1 / c
    p = c * d
    t = -(c + d)
    f = p - w
    g = 1 - w * p
    m = t * (1 - w)
    h = 4 * c**2 * d - 2 * c**2 - 3 * c * d + 3 * c + 2 * d - 4
    z = sp.cancel(-(f + m * a + g * a**2) / (g + m * a + f * a**2))

    v_at_z = sp.Matrix([f + g * z, m * (1 + z), g + f * z])
    l1 = v_at_z[2]
    l0 = v_at_z[1] + a * l1
    first = direct.edge(a, 1 / a)
    second = direct.edge(a, b)
    target = sp.Matrix([
        sp.cancel(value)
        for value in (
            ((l0 + b * l1) * first
             + (l0 + sp.Rational(1, 2) * l1) * second)
            / (b - sp.Rational(1, 2))
        )
    ])

    at_w = direct.evaluation(w)
    at_z = direct.evaluation(z)
    matrix = sp.Matrix.vstack(
        at_w[0] - p * at_w[2],
        at_w[1] - t * at_w[2],
        *at_z,
    )
    solution = [
        sp.cancel(value)
        for value in matrix.inv(method="DM") * sp.Matrix([0, 0, *target])
    ]
    print("stage=source_reconstruction", flush=True)

    def residual_coefficients(root):
        x0, x1, x2, x3, x4 = solution
        constant = sp.cancel(x0 + root * x3 + root**2 * x2)
        middle = sp.cancel(x1 + root * x4 + root**2 * x1)
        leading = sp.cancel(x2 + root * x3 + root**2 * x0)
        v_linear = sp.cancel(g + root * m + root**2 * f)
        return (
            sp.cancel(leading**2),
            sp.cancel(2 * middle * leading - v_linear**2 + 2 * w * leading**2),
            sp.cancel(constant**2 / w**2),
        )

    leading_c, middle_c, constant_c = residual_coefficients(c)
    leading_d, middle_d, constant_d = residual_coefficients(d)
    conditions = {
        ("c", "product"): constant_c - leading_c / d**2,
        ("c", "sum"): middle_c + 2 * leading_c / d,
        ("d", "product"): constant_d - leading_d / b**2,
        ("d", "sum"): middle_d + 2 * leading_d / b,
    }
    polynomials = {
        key: numerator_poly(value, b, c, d)
        for key, value in conditions.items()
    }

    product_cores = {}
    for root in ("c", "d"):
        cores = [
            sp.Poly(factor, b, c, d, domain=sp.QQ).primitive()[1]
            for factor, _ in sp.factor_list(
                polynomials[(root, "product")].as_expr()
            )[1]
            if sp.Poly(factor, b, c, d).degree(b) > 0
        ]
        product_cores[root] = sorted(cores, key=digest)

    selected_c = product_cores["c"][args.c_branch]
    selected_d = product_cores["d"][args.d_branch]
    direct.require(selected_c.degree(b) == 1, "selected c branch is not linear")
    c_lead = sp.Poly(sp.diff(selected_c.as_expr(), b), c, d, domain=sp.QQ)
    c_constant = sp.Poly(selected_c.as_expr().subs(b, 0), c, d, domain=sp.QQ)
    b_value = sp.cancel(-c_constant.as_expr() / c_lead.as_expr())

    def substitute(polynomial):
        return numerator_poly(polynomial.as_expr().subs(b, b_value), c, d)

    projected_inputs = [
        substitute(selected_d),
        substitute(polynomials[("c", "sum")]),
        substitute(polynomials[("d", "sum")]),
    ]
    common_input = reduce(sp.gcd, projected_inputs).monic()
    reconstruction_factor = 5 * c * d - 4 * c - 4 * d + 5
    expected_common = sp.Poly(
        (
            (c - 1)**2 if args.d_branch == 0
            else (c - 1) * (c + 1)
        )
        * (c * d - 1) * reconstruction_factor,
        c,
        d,
        domain=sp.QQ,
    ).monic()
    direct.require(common_input == expected_common, "common forbidden component")
    reduced_inputs = [
        value.exquo(common_input).primitive()[1]
        for value in projected_inputs
    ]
    print(
        "stage=square_ell_substitution "
        f"pair={args.c_branch},{args.d_branch} "
        f"c_line_digest={digest(selected_c)} "
        f"input_degrees={[(value.degree(c), value.degree(d)) for value in projected_inputs]}",
        flush=True,
    )
    print(
        "stage=square_ell_common_component "
        f"degrees=({common_input.degree(c)},{common_input.degree(d)}) "
        f"terms={len(common_input.terms())} digest={digest(common_input)} "
        f"factor={sp.factor(common_input.as_expr())}",
        flush=True,
    )

    candidates = {
        "dmhalf": 2 * d + 1,
        "q17": 17 * d**2 - 38 * d + 17,
        "q21": 2 * d**2 - 9 * d + 1,
        "q23": 2 * d**2 - 3 * d - 1,
        "q5": 5 * d**2 - 8 * d + 5,
        "q11": 11 * d**2 - 20 * d + 5,
        "q00cubic": 11 * d**3 - 21 * d**2 - 3 * d + 5,
    }
    if args.fiber is not None:
        saturation = sp.symbols("saturation")
        basis = sp.groebner(
            [
                *(value.as_expr() for value in reduced_inputs),
                candidates[args.fiber],
                saturation * c_lead.as_expr() - 1,
            ],
            saturation,
            c,
            d,
            order="lex",
            domain=sp.QQ,
        )
        collision = sp.fraction(
            sp.cancel(b_value - sp.Rational(1, 2))
        )[0]
        print(
            "KB_C2_112_NEAR_MOVING_XI_SQUARE_ELL_FIBER "
            f"pair={args.c_branch},{args.d_branch} fiber={args.fiber} "
            f"basis={[value.as_expr() for value in basis.polys]} "
            f"forces_b_half={basis.reduce(collision)[1] == 0}",
            flush=True,
        )
        return

    if args.exception is not None:
        basis = sp.groebner(
            [
                selected_d.as_expr(),
                c_lead.as_expr(),
                c_constant.as_expr(),
                polynomials[("c", "sum")].as_expr(),
                polynomials[("d", "sum")].as_expr(),
                candidates[args.exception],
            ],
            b,
            c,
            d,
            order="lex",
            domain=sp.QQ,
        )
        print(
            "KB_C2_112_NEAR_MOVING_XI_SQUARE_ELL_EXCEPTION "
            f"pair={args.c_branch},{args.d_branch} fiber={args.exception} "
            f"basis={[value.as_expr() for value in basis.polys]}",
            flush=True,
        )
        return

    resultants = [
        sp.Poly(
            sp.resultant(left.as_expr(), right.as_expr(), c),
            d,
            domain=sp.QQ,
        ).primitive()[1]
        for left, right in (
            (reduced_inputs[0], reduced_inputs[1]),
            (reduced_inputs[0], reduced_inputs[2]),
            (reduced_inputs[1], reduced_inputs[2]),
        )
    ]
    common = reduce(sp.gcd, resultants).monic()
    exceptional = sp.Poly(
        sp.resultant(c_lead.as_expr(), c_constant.as_expr(), c),
        d,
        domain=sp.QQ,
    ).primitive()[1]
    print(
        "KB_C2_112_NEAR_MOVING_XI_SQUARE_ELL_PAIR "
        f"pair={args.c_branch},{args.d_branch} "
        f"resultant_degrees={tuple(value.degree() for value in resultants)} "
        f"gcd_degree={common.degree()} gcd_digest={digest(common)} "
        f"gcd_factor={sp.factor(common.sqf_part().as_expr())}",
        flush=True,
    )
    print(
        "stage=square_ell_linear_exception "
        f"degree={exceptional.degree()} "
        f"factor={sp.factor(exceptional.as_expr())}",
        flush=True,
    )
    if not args.prove:
        return

    characteristic = 2130706433
    support = {
        (0, 0): (
            (d - 2) * (d - 1) * (d + 1) * (2 * d - 1) * (2 * d + 1)
            * (17 * d**2 - 38 * d + 17)
            * (11 * d**3 - 21 * d**2 - 3 * d + 5)
        ),
        (0, 1): (
            (d - 2) * (d - 1) * (d + 1) * (2 * d - 1)
            * (5 * d**2 - 8 * d + 5)
            * (17 * d**2 - 38 * d + 17)
        ),
        (1, 0): (
            (d - 2) * (d - 1) * (d + 1) * (2 * d - 1)
            * (2 * d**2 - 3 * d - 1) * (11 * d**2 - 20 * d + 5)
        ),
        (1, 1): (
            (d - 2) * (d - 1) * (d + 1) * (2 * d - 1) * (2 * d + 1)
            * (2 * d**2 - 9 * d + 1) * (5 * d**2 - 8 * d + 5)
        ),
    }[(args.c_branch, args.d_branch)]
    expected_support = sp.Poly(support, d, domain=sp.QQ).monic()
    direct.require(
        common.sqf_part().monic() == expected_support,
        "swapped square projected support",
    )
    modular_resultants = [
        reduce_mod(value, d, characteristic=characteristic)
        for value in resultants
        if not value.is_zero
    ]
    modular_common = reduce(sp.gcd, modular_resultants).monic()
    direct.require(
        modular_common.sqf_part().monic()
        == reduce_mod(
            expected_support, d, characteristic=characteristic
        ).sqf_part().monic(),
        "swapped square KoalaBear projected support",
    )

    expected_exception = (
        (d - 2)**3 * (d - 1)**5 * (d + 1)**5 * (2 * d - 1)**3
        * (17 * d**2 - 38 * d + 17)
        if args.c_branch == 0 else
        (d - 2)**3 * (d - 1)**7 * (d + 1)**5 * (2 * d - 1)**3
    )
    expected_exception_poly = sp.Poly(
        expected_exception, d, domain=sp.QQ
    ).monic()
    direct.require(
        exceptional.monic() == expected_exception_poly,
        "swapped square exceptional support",
    )
    direct.require(
        reduce_mod(exceptional, d, characteristic=characteristic)
        == reduce_mod(
            expected_exception_poly, d, characteristic=characteristic
        ),
        "swapped square KoalaBear exceptional support",
    )

    def integralize(expression, variables):
        _, integral = sp.Poly(
            expression, *variables, domain=sp.QQ
        ).clear_denoms(convert=True)
        return integral.as_expr()

    def assert_basis(expressions, variables, expected):
        actual_qq = sp.groebner(
            expressions, *variables, order="lex", domain=sp.QQ
        )
        expected_qq = sp.groebner(
            expected, *variables, order="lex", domain=sp.QQ
        )
        direct.require(
            [value.as_expr() for value in actual_qq.polys]
            == [value.as_expr() for value in expected_qq.polys],
            "swapped square candidate basis over QQ",
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
        direct.require(
            [value.as_expr() for value in actual_mod.polys]
            == [value.as_expr() for value in expected_mod.polys],
            "swapped square candidate basis over KoalaBear",
        )
        return actual_qq, actual_mod

    if args.c_branch == 0:
        q17 = 17 * d**2 - 38 * d + 17
        assert_basis(
            [
                selected_d.as_expr(),
                c_lead.as_expr(),
                c_constant.as_expr(),
                polynomials[("c", "sum")].as_expr(),
                polynomials[("d", "sum")].as_expr(),
                q17,
            ],
            (b, c, d),
            (b - sp.Rational(1, 2), 7 * c + 17 * d - 30, q17),
        )

    generic_candidates = {
        (0, 0): (
            (17 * d**2 - 38 * d + 17, (sp.Integer(1),), False),
            (2 * d + 1, (13 * c**2 + 12 * c - 28, 2 * d + 1), True),
            (11 * d**3 - 21 * d**2 - 3 * d + 5,
             (c - 1, 11 * d**3 - 21 * d**2 - 3 * d + 5), False),
        ),
        (0, 1): (
            (17 * d**2 - 38 * d + 17, (sp.Integer(1),), False),
            (5 * d**2 - 8 * d + 5,
             (c + 1, 5 * d**2 - 8 * d + 5), False),
        ),
        (1, 0): (
            (2 * d**2 - 3 * d - 1,
             (c - 2 * d + 3, 2 * d**2 - 3 * d - 1), True),
            (11 * d**2 - 20 * d + 5,
             (c - 1, 11 * d**2 - 20 * d + 5), False),
        ),
        (1, 1): (
            (2 * d + 1, (c - sp.Rational(14, 13), 2 * d + 1), True),
            (2 * d**2 - 9 * d + 1,
             (c + 2 * d - 9, 2 * d**2 - 9 * d + 1), True),
            (5 * d**2 - 8 * d + 5,
             (c + 1, 5 * d**2 - 8 * d + 5), False),
        ),
    }[(args.c_branch, args.d_branch)]
    for candidate, relations, forces_collision in generic_candidates:
        saturation = sp.symbols("saturation")
        actual_qq, actual_mod = assert_basis(
            [
                *(value.as_expr() for value in reduced_inputs),
                candidate,
                saturation * c_lead.as_expr() - 1,
            ],
            (saturation, c, d),
            (
                *relations,
                *((saturation * c_lead.as_expr() - 1,)
                  if relations != (sp.Integer(1),) else ()),
            ),
        )
        if forces_collision:
            collision = sp.fraction(
                sp.cancel(b_value - sp.Rational(1, 2))
            )[0]
            direct.require(
                actual_qq.reduce(collision)[1] == 0,
                "swapped square candidate does not force b=1/2",
            )
            _, integral_collision = sp.Poly(
                collision, c, d, domain=sp.QQ
            ).clear_denoms(convert=True)
            direct.require(
                actual_mod.reduce(integral_collision.as_expr())[1] == 0,
                "swapped square KoalaBear candidate does not force b=1/2",
            )

    print(
        "KB_C2_112_NEAR_MOVING_XI_SQUARE_ELL_PRIMARY_PASS "
        f"pair={args.c_branch},{args.d_branch} "
        f"characteristic={characteristic} support=forbidden",
        flush=True,
    )



if __name__ == "__main__":
    main()
