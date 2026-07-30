#!/usr/bin/env python3
"""Direct normalized exclusion for the fixed-xi near mixed chart.

The ``--support-gcd`` path proves that the four residual conditions have only
forbidden projected support.  The other modes expose bounded intermediate
certificates and deliberately emit INCOMPLETE.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
DIRECT = HERE / "kb_c2_112_near_fixed_xi_square_direct.py"


def load_direct():
    spec = importlib.util.spec_from_file_location("near_square_direct", DIRECT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load direct square helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(polynomial: sp.Poly) -> str:
    payload = repr([
        (monomial, str(coefficient))
        for monomial, coefficient in polynomial.monic().terms()
    ])
    return hashlib.sha256(payload.encode("ascii")).hexdigest()[:16]


def factor_record(expression, b, c, d):
    numerator = sp.Poly(
        sp.fraction(sp.cancel(expression))[0], b, c, d, domain=sp.QQ
    ).primitive()[1]
    records = []
    for factor, exponent in sp.factor_list(numerator.as_expr())[1]:
        polynomial = sp.Poly(factor, b, c, d, domain=sp.QQ)
        records.append({
            "multiplicity": exponent,
            "degrees": tuple(polynomial.degree(value) for value in (b, c, d)),
            "terms": len(polynomial.terms()),
            "digest": digest(polynomial),
            "expression": str(polynomial.as_expr())
            if len(polynomial.terms()) <= 12 else None,
        })
    return numerator, records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--resultant", choices=("c", "d", "product", "sum")
    )
    parser.add_argument(
        "--projection",
        choices=("product_21", "product_65", "sum_11", "sum_43", "sum_108"),
    )
    parser.add_argument("--support-gcd", action="store_true")
    parser.add_argument("--support-gcd-opposite", action="store_true")
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
    determinant = sp.cancel(matrix.det(method="domain-ge"))
    expected_determinant = sp.cancel(
        3 * (c - 2)**2 * (c - 1)**5 * (c + 1)**5
        * (2 * c - 1)**2 * (d - 2)**2 * (2 * d - 1)**2
        * (c * d - 1)**2 * reconstruction_factor / (c**4 * h**6)
    )
    direct.require(
        sp.cancel(determinant - expected_determinant) == 0,
        "reconstruction determinant",
    )
    rhs = sp.Matrix([0, 0, *target])
    solution = [sp.cancel(value) for value in matrix.inv(method="DM") * rhs]
    print("stage=direct_reconstruction", flush=True)

    def residual(root):
        x0, x1, x2, x3, x4 = solution
        u0 = x0 + root * x3 + root**2 * x2
        u1 = x1 + root * x4 + root**2 * x1
        u2 = x2 + root * x3 + root**2 * x0
        v0 = f + root * m + root**2 * g
        v1 = g + root * m + root**2 * f
        direct.require(
            sp.cancel(u0 + w * u1 + w**2 * u2) == 0,
            "forced U square root",
        )
        direct.require(
            sp.cancel(v0 + w * v1) == 0,
            "forced V square root",
        )
        leading = sp.cancel(u2**2)
        linear = sp.cancel(2 * u1 * u2 - v1**2 + 2 * w * leading)
        constant = sp.cancel(u0**2 / w**2)
        return leading, linear, constant

    cores = {}
    for root_name, root in (("c", c), ("d", d)):
        leading, linear, constant = residual(root)
        equations = (
            constant - leading / (2 * d),
            linear + (sp.Rational(1, 2) + 1 / d) * leading,
        )
        for equation_name, equation in zip(("product", "sum"), equations):
            polynomial, factors = factor_record(equation, b, c, d)
            if equation_name == "product":
                polynomial = polynomial.exquo(
                    sp.Poly(h**2, b, c, d, domain=sp.QQ)
                )
            cores[(root_name, equation_name)] = polynomial.primitive()[1]
            print(
                f"stage={root_name}_{equation_name} "
                f"total_degree={polynomial.total_degree()} "
                f"terms={len(polynomial.terms())} factors={factors}",
                flush=True,
            )

    if args.resultant is not None:
        pairs = {
            "c": (("c", "product"), ("c", "sum")),
            "d": (("d", "product"), ("d", "sum")),
            "product": (("c", "product"), ("d", "product")),
            "sum": (("c", "sum"), ("d", "sum")),
        }
        left_key, right_key = pairs[args.resultant]
        resultant = sp.Poly(
            sp.resultant(
                cores[left_key].as_expr(), cores[right_key].as_expr(), b
            ),
            c,
            d,
            domain=sp.QQ,
        ).primitive()[1]
        print(
            f"stage=resultant_built pair={args.resultant} "
            f"degrees=({resultant.degree(c)},{resultant.degree(d)}) "
            f"terms={len(resultant.terms())} digest={digest(resultant)}",
            flush=True,
        )
        records = []
        for factor, exponent in sp.factor_list(resultant.as_expr())[1]:
            polynomial = sp.Poly(factor, c, d, domain=sp.QQ)
            records.append({
                "multiplicity": exponent,
                "degrees": (polynomial.degree(c), polynomial.degree(d)),
                "terms": len(polynomial.terms()),
                "digest": digest(polynomial),
                "expression": str(polynomial.as_expr())
                if len(polynomial.terms()) <= 12 else None,
            })
        print(
            f"stage=resultant_factored pair={args.resultant} factors={records}",
            flush=True,
        )

    if args.projection is not None:
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
        residual_curve = next(
            sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
            for factor, _ in sp.factor_list(within_c.as_expr())[1]
            if digest(sp.Poly(factor, c, d, domain=sp.QQ))
            == "505a3755961c27e5"
        )
        cross_kind = "product" if args.projection.startswith("product") else "sum"
        cross_left = cores[("c", cross_kind)]
        cross_right = cores[("d", cross_kind)]
        cross = sp.Poly(
            sp.resultant(cross_left.as_expr(), cross_right.as_expr(), b),
            c,
            d,
            domain=sp.QQ,
        ).primitive()[1]
        wanted_digest = {
            "product_21": "7ccfa732db02ed41",
            "product_65": "5ef911c4217e6e30",
            "sum_11": "773966e2c02b56db",
            "sum_43": "33cc7e9933b4137d",
            "sum_108": "a6c1f9d18c507e52",
        }[args.projection]
        cross_factor = next(
            sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
            for factor, _ in sp.factor_list(cross.as_expr())[1]
            if digest(sp.Poly(factor, c, d, domain=sp.QQ)) == wanted_digest
        )
        projection = sp.Poly(
            sp.resultant(
                residual_curve.as_expr(), cross_factor.as_expr(), c
            ),
            d,
            domain=sp.QQ,
        ).primitive()[1]
        print(
            f"stage=projection_built factor={args.projection} "
            f"degree={projection.degree()} terms={len(projection.terms())} "
            f"digest={digest(projection)}",
            flush=True,
        )
        records = []
        for factor, exponent in sp.factor_list(projection.as_expr())[1]:
            polynomial = sp.Poly(factor, d, domain=sp.QQ)
            records.append({
                "multiplicity": exponent,
                "degree": polynomial.degree(),
                "digest": digest(polynomial),
                "expression": str(polynomial.as_expr())
                if polynomial.degree() <= 8 else None,
            })
        print(
            f"stage=projection_factored factor={args.projection} "
            f"factors={records}",
            flush=True,
        )

    if args.support_gcd or args.support_gcd_opposite:
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
            direct.monic(value, c, d)
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
        within_unknown = [
            sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
            for factor, _ in sp.factor_list(within_c.as_expr())[1]
            if sp.Poly(factor, c, d, domain=sp.QQ).monic().as_expr()
            not in within_known
        ]
        direct.require(
            len(within_unknown) == 1
            and (within_unknown[0].degree(c), within_unknown[0].degree(d))
            == (8, 6),
            "within-fiber residual curve",
        )
        residual_curve = within_unknown[0]
        cross_known = {
            "product": {
                direct.monic(value, c, d)
                for value in (
                    2 * d - 1,
                    c - d,
                    c - 1,
                    c * d - 1,
                    reconstruction_factor,
                )
            },
            "sum": {
                direct.monic(value, c, d)
                for value in (
                    c - d,
                    c - 1,
                    c * d - 1,
                    reconstruction_factor,
                    h,
                )
            },
        }
        expected_unknown_degrees = {
            "product": {(2, 1), (6, 5)},
            "sum": {(1, 1), (4, 3), (10, 8)},
        }
        projections = {}
        eliminate_variable = d if args.support_gcd_opposite else c
        projection_variable = c if args.support_gcd_opposite else d
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
            direct.require(
                {(value.degree(c), value.degree(d)) for value in selected}
                == expected_unknown_degrees[kind]
                and len(selected) == len(expected_unknown_degrees[kind]),
                "projection factors",
            )
            aggregate = sp.Poly(1, projection_variable, domain=sp.QQ)
            for factor in selected:
                aggregate *= sp.Poly(
                    sp.resultant(
                        residual_curve.as_expr(), factor.as_expr(),
                        eliminate_variable,
                    ),
                    projection_variable,
                    domain=sp.QQ,
                ).primitive()[1]
            projections[kind] = aggregate.primitive()[1]
            print(
                f"stage=aggregate_projection kind={kind} "
                f"degree={projections[kind].degree()} "
                f"digest={digest(projections[kind])}",
                flush=True,
            )
        common = sp.gcd(projections["product"], projections["sum"]).sqf_part().monic()
        expected_expression = (
            (c - 2) * (c - 1) * (2 * c - 1)
            if args.support_gcd_opposite else
            (d - 2) * (d - 1) * (2 * d - 1)
        )
        expected_common = sp.Poly(
            expected_expression, projection_variable, domain=sp.QQ
        ).monic()
        direct.require(common == expected_common, "unexpected support gcd")
        characteristic = 2130706433
        modular_common = sp.gcd(
            direct.reduce_mod(
                projections["product"], projection_variable, characteristic
            ),
            direct.reduce_mod(
                projections["sum"], projection_variable, characteristic
            ),
        ).sqf_part().monic()
        direct.require(
            modular_common == direct.reduce_mod(
                expected_common, projection_variable, characteristic
            ),
            "deployed-characteristic support gcd",
        )
        records = []
        for factor, exponent in sp.factor_list(common.as_expr())[1]:
            polynomial = sp.Poly(factor, projection_variable, domain=sp.QQ)
            records.append({
                "multiplicity": exponent,
                "degree": polynomial.degree(),
                "digest": digest(polynomial),
                "expression": str(polynomial.as_expr())
                if polynomial.degree() <= 8 else None,
            })
        print(
            f"stage=support_gcd degree={common.degree()} "
            f"digest={digest(common)} factors={records} "
            f"variable={projection_variable} "
            f"modular_degree={modular_common.degree()} "
            f"modular_digest={digest(modular_common)} "
            f"characteristic={characteristic}",
            flush=True,
        )

    if args.support_gcd:
        print("KB_C2_112_NEAR_FIXED_XI_MIXED_DIRECT_PASS")
    else:
        print("KB_C2_112_NEAR_FIXED_XI_MIXED_DIRECT_PROBE_INCOMPLETE")


if __name__ == "__main__":
    main()
