#!/usr/bin/env python3
"""Exact primary exclusion for one moving-xi near square allocation.

The proof mode treats the fixed-moving reconstruction with ``a=2``,
``xi=b``, ``eta=c``, ``ell=d``, and ``w=1/c`` and assigns the residual over
``c`` to ``(W-1/b)^2`` and the residual over ``d`` to ``(W-1/d)^2``. Other
modes retain bounded frontier diagnostics for the two unresolved allocations.
"""

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


def factor_records(polynomial: sp.Poly, b, c, d):
    records = []
    for factor, exponent in sp.factor_list(polynomial.as_expr())[1]:
        value = sp.Poly(factor, b, c, d, domain=sp.QQ).primitive()[1]
        records.append({
            "multiplicity": exponent,
            "degrees": tuple(value.degree(variable) for variable in (b, c, d)),
            "terms": len(value.terms()),
            "digest": digest(value),
            "expression": str(value.as_expr()) if len(value.terms()) <= 16 else None,
        })
    return records


def reduce_mod(polynomial: sp.Poly, *variables, characteristic: int):
    _, integral = polynomial.clear_denoms(convert=True)
    return sp.Poly(
        integral.as_expr(), *variables, modulus=characteristic
    ).monic()


def clear_bezout_denominator(left: sp.Poly, right: sp.Poly, c, d):
    field = sp.QQ.frac_field(d)
    left_field = sp.Poly(left.as_expr(), c, domain=field)
    right_field = sp.Poly(right.as_expr(), c, domain=field)
    bezout_left, bezout_right, gcd = sp.gcdex(left_field, right_field)
    if gcd.monic().as_expr() != 1:
        raise RuntimeError("nontrivial generic Bezout gcd")
    denominator = sp.Poly(1, d, domain=sp.QQ)
    for coefficient in bezout_left.all_coeffs() + bezout_right.all_coeffs():
        _, value = sp.fraction(sp.cancel(coefficient.as_expr()))
        denominator = sp.lcm(
            denominator, sp.Poly(value, d, domain=sp.QQ)
        )
    identity = sp.cancel(
        (bezout_left * left_field + bezout_right * right_field).as_expr()
        * denominator.as_expr() - denominator.as_expr()
    )
    if identity != 0:
        raise RuntimeError("Bezout identity failed")
    return denominator.primitive()[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--coefficient", type=int, choices=(1, 2, 3))
    parser.add_argument(
        "--allocation",
        choices=("square-xi", "square-ell", "mixed"),
    )
    parser.add_argument(
        "--square-xi-pair", type=int, choices=(0, 1), nargs=2,
        metavar=("C_BRANCH", "D_BRANCH"),
    )
    parser.add_argument(
        "--square-xi-fiber",
        choices=("q17", "q21", "q23", "dm2", "dmhalf"),
    )
    parser.add_argument(
        "--square-xi-exception", choices=("q17", "dm2", "dmhalf"),
    )
    parser.add_argument("--square-xi-opposite", action="store_true")
    parser.add_argument("--square-xi-bezout", action="store_true")
    parser.add_argument(
        "--square-xi-bezout-index", type=int, choices=(0, 1)
    )
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
    z = sp.cancel(-(f + m * a + g * a**2) / (g + m * a + f * a**2))

    h = 4 * c**2 * d - 2 * c**2 - 3 * c * d + 3 * c + 2 * d - 4
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
    reconstruction_factor = 5 * c * d - 4 * c - 4 * d + 5
    expected_determinant = sp.cancel(
        3 * (c - 2)**2 * (c - 1)**5 * (c + 1)**5
        * (2 * c - 1)**2 * (d - 2)**2 * (2 * d - 1)**2
        * (c * d - 1)**2 * reconstruction_factor / (c**4 * h**6)
    )
    direct.require(
        sp.cancel(matrix.det(method="domain-ge") - expected_determinant) == 0,
        "reconstruction determinant",
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
        v_constant = sp.cancel(f + root * m + root**2 * g)
        v_linear = sp.cancel(g + root * m + root**2 * f)
        direct.require(
            sp.cancel(constant + w * middle + w**2 * leading) == 0,
            "forced U square root",
        )
        direct.require(
            sp.cancel(v_constant + w * v_linear) == 0,
            "forced V square root",
        )
        return (
            sp.cancel(leading**2),
            sp.cancel(2 * middle * leading - v_linear**2 + 2 * w * leading**2),
            sp.cancel(constant**2 / w**2),
            constant,
            leading,
        )

    residual_c = residual_coefficients(c)
    residual_d = residual_coefficients(d)
    leading_c, middle_c, residual_constant_c, constant_c, u_leading_c = residual_c
    leading_d, middle_d, residual_constant_d, constant_d, u_leading_d = residual_d
    allocation = "square-xi" if args.square_xi_pair is not None else args.allocation
    if allocation is not None:
        kappa_xi = 1 / b
        kappa_ell = 1 / d
        if allocation == "mixed":
            conditions = {
                ("c", "product"): residual_constant_c - kappa_xi * kappa_ell * leading_c,
                ("c", "sum"): middle_c + (kappa_xi + kappa_ell) * leading_c,
                ("d", "product"): residual_constant_d - kappa_xi * kappa_ell * leading_d,
                ("d", "sum"): middle_d + (kappa_xi + kappa_ell) * leading_d,
            }
        else:
            target_c, target_d = (
                (kappa_xi, kappa_ell)
                if allocation == "square-xi"
                else (kappa_ell, kappa_xi)
            )
            conditions = {
                ("c", "product"): residual_constant_c - target_c**2 * leading_c,
                ("c", "sum"): middle_c + 2 * target_c * leading_c,
                ("d", "product"): residual_constant_d - target_d**2 * leading_d,
                ("d", "sum"): middle_d + 2 * target_d * leading_d,
            }
        condition_polynomials = {}
        for (root_name, condition_name), condition in conditions.items():
            numerator = sp.Poly(
                sp.fraction(sp.cancel(condition))[0], b, c, d, domain=sp.QQ
            ).primitive()[1]
            condition_polynomials[(root_name, condition_name)] = numerator
            print(
                f"KB_C2_112_NEAR_MOVING_XI_ALLOCATION allocation={allocation} "
                f"root={root_name} condition={condition_name} "
                f"degrees={tuple(numerator.degree(variable) for variable in (b,c,d))} "
                f"terms={len(numerator.terms())} digest={digest(numerator)} "
                f"factors={factor_records(numerator, b, c, d)}",
                flush=True,
            )
        if args.square_xi_pair is not None:
            branch_c, branch_d = args.square_xi_pair
            product_cores = {}
            for root_name in ("c", "d"):
                factors = [
                    sp.Poly(factor, b, c, d, domain=sp.QQ).primitive()[1]
                    for factor, _ in sp.factor_list(
                        condition_polynomials[(root_name, "product")].as_expr()
                    )[1]
                    if sp.Poly(factor, b, c, d).degree(b) > 0
                ]
                product_cores[root_name] = sorted(factors, key=digest)
            selected_c = product_cores["c"][branch_c]
            selected_d = product_cores["d"][branch_d]
            direct.require(selected_d.degree(b) == 1, "selected d branch is not linear")
            d_lead = sp.Poly(sp.diff(selected_d.as_expr(), b), c, d, domain=sp.QQ)
            d_constant = sp.Poly(
                selected_d.as_expr().subs(b, 0), c, d, domain=sp.QQ
            )
            if args.square_xi_exception is not None:
                candidate = {
                    "q17": 17 * d**2 - 38 * d + 17,
                    "dm2": d + 2,
                    "dmhalf": 2 * d + 1,
                }[args.square_xi_exception]
                basis = sp.groebner(
                    [
                        selected_c.as_expr(),
                        d_lead.as_expr(),
                        d_constant.as_expr(),
                        condition_polynomials[("c", "sum")].as_expr(),
                        condition_polynomials[("d", "sum")].as_expr(),
                        candidate,
                    ],
                    b,
                    c,
                    d,
                    order="lex",
                    domain=sp.QQ,
                )
                print(
                    "KB_C2_112_NEAR_MOVING_XI_SQUARE_XI_EXCEPTION "
                    f"pair={branch_c},{branch_d} "
                    f"fiber={args.square_xi_exception} "
                    f"basis={[value.as_expr() for value in basis.polys]}",
                    flush=True,
                )
                print("INCOMPLETE moving-xi square-xi exceptional fiber classified")
                return
            b_value = sp.cancel(-d_constant.as_expr() / d_lead.as_expr())

            def substitute(polynomial):
                numerator = sp.fraction(
                    sp.cancel(polynomial.as_expr().subs(b, b_value))
                )[0]
                return sp.Poly(numerator, c, d, domain=sp.QQ).primitive()[1]

            projected_inputs = [
                substitute(selected_c),
                substitute(condition_polynomials[("c", "sum")]),
                substitute(condition_polynomials[("d", "sum")]),
            ]
            print(
                "stage=square_xi_substitution "
                f"pair={branch_c},{branch_d} d_line_digest={digest(selected_d)} "
                f"input_degrees={[(value.degree(c), value.degree(d)) for value in projected_inputs]}",
                flush=True,
            )
            common_input = reduce(sp.gcd, projected_inputs).monic()
            print(
                "stage=square_xi_common_component "
                f"pair={branch_c},{branch_d} "
                f"degrees=({common_input.degree(c)},{common_input.degree(d)}) "
                f"terms={len(common_input.terms())} digest={digest(common_input)} "
                f"factor={sp.factor(common_input.as_expr())}",
                flush=True,
            )
            reduced_inputs = [
                value.exquo(common_input).primitive()[1]
                for value in projected_inputs
            ]
            if args.square_xi_bezout or args.square_xi_bezout_index is not None:
                audit_inputs = (
                    reduced_inputs[1:]
                    if args.square_xi_bezout_index is None else
                    (reduced_inputs[1 + args.square_xi_bezout_index],)
                )
                bezout_denominators = [
                    clear_bezout_denominator(
                        reduced_inputs[0], value, c, d
                    )
                    for value in audit_inputs
                ]
                bezout_common = reduce(sp.gcd, bezout_denominators).monic()
                print(
                    "KB_C2_112_NEAR_MOVING_XI_SQUARE_XI_BEZOUT "
                    f"pair={branch_c},{branch_d} "
                    f"denominator_degrees={tuple(value.degree() for value in bezout_denominators)} "
                    f"gcd_degree={bezout_common.degree()} "
                    f"gcd_factor={sp.factor(bezout_common.sqf_part().as_expr())}",
                    flush=True,
                )
                print("INCOMPLETE moving-xi square-xi Bezout audit factored")
                return
            if args.square_xi_opposite:
                opposite_resultants = [
                    sp.Poly(
                        sp.resultant(left.as_expr(), right.as_expr(), d),
                        c,
                        domain=sp.QQ,
                    ).primitive()[1]
                    for left, right in (
                        (reduced_inputs[0], reduced_inputs[1]),
                        (reduced_inputs[0], reduced_inputs[2]),
                        (reduced_inputs[1], reduced_inputs[2]),
                    )
                ]
                opposite_common = reduce(sp.gcd, opposite_resultants).monic()
                opposite_exception = sp.Poly(
                    sp.resultant(d_lead.as_expr(), d_constant.as_expr(), d),
                    c,
                    domain=sp.QQ,
                ).primitive()[1]
                print(
                    "KB_C2_112_NEAR_MOVING_XI_SQUARE_XI_OPPOSITE "
                    f"pair={branch_c},{branch_d} "
                    f"resultant_degrees={tuple(value.degree() for value in opposite_resultants)} "
                    f"gcd_degree={opposite_common.degree()} "
                    f"gcd_factor={sp.factor(opposite_common.sqf_part().as_expr())} "
                    f"exception_factor={sp.factor(opposite_exception.as_expr())}",
                    flush=True,
                )
                print("INCOMPLETE moving-xi square-xi opposite projection factored")
                return
            if args.square_xi_fiber is not None:
                candidate = {
                    "q17": 17 * d**2 - 38 * d + 17,
                    "q21": 2 * d**2 - 9 * d + 1,
                    "q23": 2 * d**2 - 3 * d - 1,
                    "dm2": d + 2,
                    "dmhalf": 2 * d + 1,
                }[args.square_xi_fiber]
                saturation = sp.symbols("saturation")
                basis = sp.groebner(
                    [
                        *(value.as_expr() for value in reduced_inputs),
                        candidate,
                        saturation * d_lead.as_expr() - 1,
                    ],
                    saturation,
                    c,
                    d,
                    order="lex",
                    domain=sp.QQ,
                )
                basis_values = [
                    sp.Poly(value, saturation, c, d, domain=sp.QQ)
                    for value in basis.polys
                ]

                if args.square_xi_fiber in ("q17", "dm2"):
                    print(
                        "KB_C2_112_NEAR_MOVING_XI_SQUARE_XI_FIBER "
                        f"pair={branch_c},{branch_d} "
                        f"fiber={args.square_xi_fiber} "
                        f"basis={[value.as_expr() for value in basis_values]}",
                        flush=True,
                    )
                    print("INCOMPLETE moving-xi square-xi generic fiber classified")
                    return

                if args.square_xi_fiber == "dmhalf":
                    fiber_d = -sp.Rational(1, 2)
                    modulus_c = sp.Poly(
                        13 * c**2 + 12 * c - 28, c, domain=sp.QQ
                    ).monic()

                    def quotient_reduce_c(expression):
                        numerator, denominator = sp.fraction(
                            sp.cancel(expression.subs(d, fiber_d))
                        )
                        numerator_poly = sp.Poly(
                            numerator, c, domain=sp.QQ
                        ).rem(modulus_c)
                        denominator_poly = sp.Poly(
                            denominator, c, domain=sp.QQ
                        ).rem(modulus_c)
                        inverse = sp.invert(denominator_poly, modulus_c)
                        return sp.Poly(
                            numerator_poly.as_expr() * inverse.as_expr(),
                            c,
                            domain=sp.QQ,
                        ).rem(modulus_c).as_expr()

                    fiber_b = quotient_reduce_c(b_value)
                    checks = {
                        "b-2": fiber_b - 2,
                        "2b-1": 2 * fiber_b - 1,
                        "b^2-1": fiber_b**2 - 1,
                        "b-c": fiber_b - c,
                        "b-d": fiber_b - fiber_d,
                        "bc-1": fiber_b * c - 1,
                        "bd-1": fiber_b * fiber_d - 1,
                        "c-d": c - fiber_d,
                        "cd-1": c * fiber_d - 1,
                        "z-1-factor": reconstruction_factor.subs(d, fiber_d),
                        "incidence-h": h.subs(d, fiber_d),
                    }
                    reduced_checks = {
                        name: quotient_reduce_c(value)
                        for name, value in checks.items()
                    }
                    print(
                        "KB_C2_112_NEAR_MOVING_XI_SQUARE_XI_FIBER "
                        f"pair={branch_c},{branch_d} fiber=dmhalf "
                        f"basis={[value.as_expr() for value in basis_values]} "
                        f"b={fiber_b} checks={reduced_checks}",
                        flush=True,
                    )
                    print("INCOMPLETE moving-xi square-xi rational fiber classified")
                    return

                fiber_c = {
                    "q21": 9 - 2 * d,
                    "q23": 2 * d - 3,
                }[args.square_xi_fiber]

                modulus = sp.Poly(candidate, d, domain=sp.QQ).monic()

                def quotient_reduce(expression):
                    numerator, denominator = sp.fraction(
                        sp.cancel(expression.subs(c, fiber_c))
                    )
                    numerator_poly = sp.Poly(numerator, d, domain=sp.QQ).rem(modulus)
                    denominator_poly = sp.Poly(denominator, d, domain=sp.QQ).rem(modulus)
                    inverse = sp.invert(denominator_poly, modulus)
                    return sp.Poly(
                        numerator_poly.as_expr() * inverse.as_expr(),
                        d,
                        domain=sp.QQ,
                    ).rem(modulus).as_expr()

                fiber_b = quotient_reduce(b_value)
                checks = {
                    "b-2": fiber_b - 2,
                    "2b-1": 2 * fiber_b - 1,
                    "b^2-1": fiber_b**2 - 1,
                    "b-c": fiber_b - fiber_c,
                    "b-d": fiber_b - d,
                    "bc-1": fiber_b * fiber_c - 1,
                    "bd-1": fiber_b * d - 1,
                    "c-d": fiber_c - d,
                    "cd-1": fiber_c * d - 1,
                    "z-1-factor": reconstruction_factor.subs(c, fiber_c),
                    "incidence-h": h.subs(c, fiber_c),
                }
                reduced_checks = {
                    name: quotient_reduce(value)
                    for name, value in checks.items()
                }
                print(
                    "KB_C2_112_NEAR_MOVING_XI_SQUARE_XI_FIBER "
                    f"pair={branch_c},{branch_d} fiber={args.square_xi_fiber} "
                    f"basis={[value.as_expr() for value in basis_values]} "
                    f"b={fiber_b} checks={reduced_checks}",
                    flush=True,
                )
                print("INCOMPLETE moving-xi square-xi candidate fiber classified")
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
            print(
                "KB_C2_112_NEAR_MOVING_XI_SQUARE_XI_PAIR "
                f"pair={branch_c},{branch_d} "
                f"resultant_degrees={tuple(value.degree() for value in resultants)} "
                f"gcd_degree={common.degree()} gcd_digest={digest(common)} "
                f"gcd_factor={sp.factor(common.sqf_part().as_expr())}",
                flush=True,
            )
            exceptional = sp.Poly(
                sp.resultant(d_lead.as_expr(), d_constant.as_expr(), c),
                d,
                domain=sp.QQ,
            ).primitive()[1]
            print(
                "stage=square_xi_linear_exception "
                f"pair={branch_c},{branch_d} degree={exceptional.degree()} "
                f"factor={sp.factor(exceptional.as_expr())}",
                flush=True,
            )
            if args.prove:
                characteristic = 2130706433
                support = {
                    (0, 0): (
                        (d - 2) * (d - 1) * (d + 1) * (2 * d - 1)
                        * (17 * d**2 - 38 * d + 17)
                    ),
                    (0, 1): (
                        (d - 2) * (d - 1) * (d + 1) * (d + 2)
                        * (2 * d - 1) * (2 * d + 1)
                        * (2 * d**2 - 9 * d + 1)
                    ),
                    (1, 0): (
                        (d - 2) * (d - 1) * (d + 1)
                        * (2 * d - 1) * (2 * d + 1)
                        * (17 * d**2 - 38 * d + 17)
                    ),
                    (1, 1): (
                        (d - 2) * (d - 1) * (d + 1) * (d + 2)
                        * (2 * d - 1) * (2 * d + 1)
                        * (2 * d**2 - 3 * d - 1)
                    ),
                }[(branch_c, branch_d)]
                expected_support = sp.Poly(support, d, domain=sp.QQ).monic()
                direct.require(
                    common.sqf_part().monic() == expected_support,
                    "moving-xi projected support",
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
                    "moving-xi KoalaBear projected support",
                )

                expected_exception = (
                    (d - 2)**3 * (d - 1)**5 * (d + 1)**5
                    * (2 * d - 1)**3 * (17 * d**2 - 38 * d + 17)
                    if branch_d == 0 else
                    (d - 2)**2 * (d - 1)**7 * (d + 1)**5 * (d + 2)
                    * (2 * d - 1)**2 * (2 * d + 1)
                )
                expected_exception_poly = sp.Poly(
                    expected_exception, d, domain=sp.QQ
                ).monic()
                direct.require(
                    exceptional.monic() == expected_exception_poly,
                    "moving-xi exceptional resultant",
                )
                direct.require(
                    reduce_mod(exceptional, d, characteristic=characteristic)
                    == reduce_mod(
                        expected_exception_poly,
                        d,
                        characteristic=characteristic,
                    ),
                    "moving-xi KoalaBear exceptional resultant",
                )

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
                        "moving-xi candidate basis over QQ",
                    )
                    def integralize(expression):
                        _, integral = sp.Poly(
                            expression, *variables, domain=sp.QQ
                        ).clear_denoms(convert=True)
                        return integral.as_expr()

                    actual_mod = sp.groebner(
                        [integralize(value) for value in expressions],
                        *variables,
                        order="lex",
                        modulus=characteristic,
                    )
                    expected_mod = sp.groebner(
                        [integralize(value) for value in expected],
                        *variables,
                        order="lex",
                        modulus=characteristic,
                    )
                    direct.require(
                        [value.as_expr() for value in actual_mod.polys]
                        == [value.as_expr() for value in expected_mod.polys],
                        "moving-xi candidate basis over KoalaBear",
                    )
                    return actual_qq, actual_mod

                if branch_d == 0:
                    q17 = 17 * d**2 - 38 * d + 17
                    assert_basis(
                        [
                            selected_c.as_expr(),
                            d_lead.as_expr(),
                            d_constant.as_expr(),
                            condition_polynomials[("c", "sum")].as_expr(),
                            condition_polynomials[("d", "sum")].as_expr(),
                            q17,
                        ],
                        (b, c, d),
                        (b - sp.Rational(1, 2),
                         7 * c + 17 * d - 30, q17),
                    )
                else:
                    for candidate in (d + 2, 2 * d + 1):
                        assert_basis(
                            [
                                selected_c.as_expr(),
                                d_lead.as_expr(),
                                d_constant.as_expr(),
                                condition_polynomials[("c", "sum")].as_expr(),
                                condition_polynomials[("d", "sum")].as_expr(),
                                candidate,
                            ],
                            (b, c, d),
                            (sp.Integer(1),),
                        )

                generic_candidates = {
                    (0, 1): (
                        2 * d**2 - 9 * d + 1,
                        (c + 2 * d - 9,
                         2 * d**2 - 9 * d + 1),
                    ),
                    (1, 0): (
                        2 * d + 1,
                        (13 * c**2 + 12 * c - 28, 2 * d + 1),
                    ),
                    (1, 1): (
                        2 * d**2 - 3 * d - 1,
                        (c - 2 * d + 3,
                         2 * d**2 - 3 * d - 1),
                    ),
                }
                if (branch_c, branch_d) in generic_candidates:
                    candidate, expected_relations = generic_candidates[
                        (branch_c, branch_d)
                    ]
                    saturation = sp.symbols("saturation")
                    actual_qq, actual_mod = assert_basis(
                        [
                            *(value.as_expr() for value in reduced_inputs),
                            candidate,
                            saturation * d_lead.as_expr() - 1,
                        ],
                        (saturation, c, d),
                        (
                            *expected_relations,
                            saturation * d_lead.as_expr() - 1,
                        ),
                    )
                    b_collision = sp.fraction(
                        sp.cancel(b_value - sp.Rational(1, 2))
                    )[0]
                    direct.require(
                        actual_qq.reduce(b_collision)[1] == 0,
                        "moving-xi candidate does not force b=1/2",
                    )
                    _, integral_collision = sp.Poly(
                        b_collision, c, d, domain=sp.QQ
                    ).clear_denoms(convert=True)
                    direct.require(
                        actual_mod.reduce(integral_collision.as_expr())[1] == 0,
                        "moving-xi KoalaBear candidate does not force b=1/2",
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
                }[(branch_c, branch_d)]
                for candidate, relations, forces_collision in overlap_candidates:
                    saturation = sp.symbols("saturation")
                    actual_qq, actual_mod = assert_basis(
                        [
                            *(value.as_expr() for value in reduced_inputs),
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
                        b_collision = sp.fraction(
                            sp.cancel(b_value - sp.Rational(1, 2))
                        )[0]
                        direct.require(
                            actual_qq.reduce(b_collision)[1] == 0,
                            "moving-xi overlap does not force b=1/2",
                        )
                        _, integral_collision = sp.Poly(
                            b_collision, c, d, domain=sp.QQ
                        ).clear_denoms(convert=True)
                        direct.require(
                            actual_mod.reduce(integral_collision.as_expr())[1] == 0,
                            "moving-xi KoalaBear overlap does not force b=1/2",
                        )

                print(
                    "KB_C2_112_NEAR_MOVING_XI_SQUARE_XI_PRIMARY_PASS "
                    f"pair={branch_c},{branch_d} characteristic={characteristic} "
                    "generic_and_exceptional_support=forbidden",
                    flush=True,
                )
                return
            print("INCOMPLETE moving-xi square-xi pair; exceptional fibers unclassified")
            return
        print("INCOMPLETE moving-xi allocation conditions factored")
        return

    product_leading = sp.cancel(leading_c * leading_d)
    product_coefficients = {
        3: sp.cancel(leading_c * middle_d + middle_c * leading_d),
        2: sp.cancel(
            leading_c * residual_constant_d
            + middle_c * middle_d
            + residual_constant_c * leading_d
        ),
        1: sp.cancel(
            middle_c * residual_constant_d
            + residual_constant_c * middle_d
        ),
    }
    target_coefficients = {
        3: -2 * (1 / b + 1 / d),
        2: 1 / b**2 + 4 / (b * d) + 1 / d**2,
        1: -2 * (1 / (b * d)) * (1 / b + 1 / d),
    }
    if args.coefficient is not None:
        mismatch = sp.cancel(
            product_coefficients[args.coefficient]
            - target_coefficients[args.coefficient] * product_leading
        )
        numerator = sp.Poly(
            sp.fraction(mismatch)[0], b, c, d, domain=sp.QQ
        ).primitive()[1]
        print(
            f"KB_C2_112_NEAR_MOVING_XI_PRODUCT_COEFFICIENT "
            f"coefficient={args.coefficient} "
            f"degrees={tuple(numerator.degree(variable) for variable in (b,c,d))} "
            f"terms={len(numerator.terms())} digest={digest(numerator)} "
            f"factors={factor_records(numerator, b, c, d)}",
            flush=True,
        )
        print("INCOMPLETE moving-xi product coefficient factored")
        return

    for sign in (1, -1):
        expression = sp.cancel(
            c**2 * b * d * constant_c * constant_d
            - sign * u_leading_c * u_leading_d
        )
        numerator = sp.Poly(
            sp.fraction(expression)[0], b, c, d, domain=sp.QQ
        ).primitive()[1]
        print(
            f"KB_C2_112_NEAR_MOVING_XI_COMMON_GATE sign={sign:+d} "
            f"degrees={tuple(numerator.degree(variable) for variable in (b,c,d))} "
            f"terms={len(numerator.terms())} digest={digest(numerator)} "
            f"factors={factor_records(numerator, b, c, d)}",
            flush=True,
        )
    print("INCOMPLETE moving-xi common gate factored; residual components remain")


if __name__ == "__main__":
    main()
