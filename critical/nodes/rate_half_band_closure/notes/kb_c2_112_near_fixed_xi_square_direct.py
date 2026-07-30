#!/usr/bin/env python3
"""Direct exact exclusion of near-aligned positive square charts.

The chart has ``a=xi=2``, ``eta=c``, ``ell=d``, and ``w=1/c``.  It uses the
fixed-moving internal template.  By default it assigns the residual over c
to ``(W-1/2)^2`` and the residual over d to ``(W-1/d)^2``; ``--swap``
interchanges those assignments.  A direct 5 by 5 solve keeps U and V in the
same normalization. Resultant gcds cover the generic endpoint-line pairs;
separate base resultants cover loci on which the selected left line vanishes
identically in b.
"""

from __future__ import annotations

import argparse
import hashlib

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def monic(expression, *variables):
    return sp.Poly(expression, *variables, domain=sp.QQ).monic().as_expr()


def digest_polynomial(polynomial: sp.Poly) -> str:
    value = polynomial.monic()
    payload = repr([
        (monomial, str(coefficient))
        for monomial, coefficient in value.terms()
    ]).encode("ascii")
    return hashlib.sha256(payload).hexdigest()[:16]


def reduce_mod(polynomial: sp.Poly, variable, characteristic):
    _, integral = polynomial.clear_denoms(convert=True)
    return sp.Poly(
        integral.as_expr(), variable, modulus=characteristic
    ).monic()


def edge(left, right):
    return sp.Matrix([left * right, -(left + right), 1])


def evaluation(point):
    return (
        sp.Matrix([1, point, point**2, 0, 0]).T,
        sp.Matrix([0, 0, 0, 1 + point**2, point]).T,
        sp.Matrix([point**2, point, 1, 0, 0]).T,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("left", type=int, choices=(0, 1))
    parser.add_argument("right", type=int, choices=(0, 1), nargs="?")
    parser.add_argument("--swap", action="store_true")
    args = parser.parse_args()
    b, c, d = sp.symbols("b c d", nonzero=True)
    characteristic = 2130706433
    a = sp.Rational(2)
    w = 1 / c
    p = c * d
    t = -(c + d)
    f = p - w
    g = 1 - w * p
    m = t * (1 - w)
    z = sp.cancel(-(f + m * a + g * a**2) / (g + m * a + f * a**2))

    h = 4 * c**2 * d - 2 * c**2 - 3 * c * d + 3 * c + 2 * d - 4
    z_numerator = c**2 * d - 2 * c**2 - 6 * c * d + 6 * c + 2 * d - 1
    require(sp.cancel(z + z_numerator / h) == 0, "incidence coordinate")

    v_at_z = sp.Matrix([f + g * z, m * (1 + z), g + f * z])
    l1 = v_at_z[2]
    l0 = v_at_z[1] + a * l1
    first = edge(a, 1 / a)
    second = edge(a, b)
    target = sp.Matrix([
        sp.cancel(value)
        for value in (
            ((l0 + b * l1) * first + (l0 + sp.Rational(1, 2) * l1) * second)
            / (b - sp.Rational(1, 2))
        )
    ])

    at_w = evaluation(w)
    at_z = evaluation(z)
    matrix = sp.Matrix.vstack(
        at_w[0] - p * at_w[2],
        at_w[1] - t * at_w[2],
        *at_z,
    )
    reconstruction_factor = 5 * c * d - 4 * c - 4 * d + 5
    if not args.swap:
        determinant = sp.cancel(matrix.det(method="domain-ge"))
        expected_determinant = sp.cancel(
            3 * (c - 2)**2 * (c - 1)**5 * (c + 1)**5
            * (2 * c - 1)**2 * (d - 2)**2 * (2 * d - 1)**2
            * (c * d - 1)**2 * reconstruction_factor / (c**4 * h**6)
        )
        require(sp.cancel(determinant - expected_determinant) == 0,
                "reconstruction determinant")

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
        if not args.swap:
            require(sp.cancel(u0 + w * u1 + w**2 * u2) == 0,
                    "forced U square root")
            require(sp.cancel(v0 + w * v1) == 0, "forced V square root")
        leading = sp.cancel(u2**2)
        linear = sp.cancel(2 * u1 * u2 - v1**2 + 2 * w * leading)
        constant = sp.cancel(u0**2 / w**2)
        return leading, linear, constant

    endpoint_lines = []
    middle_equations = []
    targets = (
        ((c, 1 / d), (d, sp.Rational(1, 2)))
        if args.swap else
        ((c, sp.Rational(1, 2)), (d, 1 / d))
    )
    for root, target_root in targets:
        leading, linear, constant = residual(root)
        endpoint = sp.cancel(constant - target_root**2 * leading)
        middle = sp.cancel(linear + 2 * target_root * leading)
        endpoint_numerator, _ = sp.fraction(endpoint)
        factors = sp.factor_list(endpoint_numerator)[1]
        local = [
            sp.Poly(factor, b, c, d, domain=sp.QQ)
            for factor, _ in factors
            if sp.Poly(factor, b, c, d).degree(b) == 1
        ]
        discarded = [
            (monic(factor, b, c, d), exponent)
            for factor, exponent in factors
            if sp.Poly(factor, b, c, d).degree(b) != 1
        ]
        require(len(local) == 2, "endpoint line split")
        require(discarded == [(monic(h, b, c, d), 2)],
                "finite-z endpoint factor")
        endpoint_lines.append(local)
        middle_equations.append(middle)
    print("stage=endpoint_lines", flush=True)

    known_endpoint = {
        monic(c - 1, c, d),
        monic(c * d - 1, c, d),
        monic(reconstruction_factor, c, d),
    }
    if args.swap:
        known_endpoint.update({monic(d - 1, c, d), monic(d + 1, c, d)})
    collision_d = sp.Poly(
        (d - 2) * (d - 1) * (d + 1) * (2 * d - 1), d, domain=sp.QQ
    ).monic()
    generic_rows = []
    for left_index in (args.left,):
        left = endpoint_lines[0][left_index]
        left_lead = sp.diff(left.as_expr(), b)
        left_constant = left.as_expr().subs(b, 0)
        b_value = sp.cancel(-left_constant / left_lead)
        wrong_lead = left.coeff_monomial(b)
        wrong_constant = left.coeff_monomial(1)
        wrong_b = sp.cancel(-wrong_constant / wrong_lead)
        require(sp.cancel(b_value - wrong_b) != 0,
                "exact-monomial coefficient mutation was not caught")
        substituted_middle = []
        for equation in middle_equations:
            numerator, _ = sp.fraction(sp.cancel(equation.subs(b, b_value)))
            substituted_middle.append(
                sp.Poly(numerator, c, d, domain=sp.QQ).primitive()[1]
            )

        right_indices = (args.right,) if args.right is not None else (0, 1)
        for right_index in right_indices:
            right = endpoint_lines[1][right_index]
            endpoint_resultant = sp.resultant(left.as_expr(), right.as_expr(), b)
            factors = [
                sp.Poly(factor, c, d, domain=sp.QQ)
                for factor, exponent in sp.factor_list(endpoint_resultant)[1]
                for _ in range(exponent)
            ]
            curves = [
                factor for factor in factors
                if factor.monic().as_expr() not in known_endpoint
            ]
            expected_factor_count = 5 if args.swap else 4
            require(len(factors) == expected_factor_count and len(curves) == 1,
                    "endpoint resultant split")
            curve = curves[0]
            resultants = [
                sp.Poly(
                    sp.resultant(curve.as_expr(), middle.as_expr(), c),
                    d, domain=sp.QQ,
                ).primitive()[1]
                for middle in substituted_middle
            ]
            common = sp.gcd(*resultants).monic()
            expected_generic = collision_d
            if args.swap and (left_index, right_index) == (1, 0):
                expected_generic = sp.Poly(
                    (d - 1) * (d + 1) * (2 * d - 1), d, domain=sp.QQ
                ).monic()
            require(common.sqf_part().monic() == expected_generic,
                    "generic branch has noncollision support")
            modular_resultants = [
                reduce_mod(value, d, characteristic)
                for value in resultants
            ]
            modular_common = sp.gcd(*modular_resultants).monic()
            require(
                modular_common.sqf_part().monic()
                == reduce_mod(expected_generic, d, characteristic),
                    "KoalaBear generic branch has noncollision support")
            generic_rows.append(
                (left_index, right_index, tuple(value.degree() for value in resultants),
                 common.degree(), digest_polynomial(common))
            )
            print(
                f"stage=generic pair={left_index},{right_index} "
                f"resultant_degrees={tuple(value.degree() for value in resultants)} "
                f"gcd_degree={common.degree()} digest={digest_polynomial(common)}",
                flush=True,
            )

    exceptional_rows = []
    for left_index in (args.left,):
        left = endpoint_lines[0][left_index]
        lead = sp.diff(left.as_expr(), b)
        constant = left.as_expr().subs(b, 0)
        base_resultant = sp.Poly(
            sp.resultant(lead, constant, c), d, domain=sp.QQ
        ).primitive()[1]
        if args.swap and left_index == 0:
            extra_factor = 17 * d**2 - 38 * d + 17
            expected_support = sp.Poly(
                collision_d.as_expr() * extra_factor, d, domain=sp.QQ
            ).monic()
        elif args.swap:
            expected_support = collision_d
        else:
            exceptional_data = (
                (sp.Rational(7, 5), sp.Rational(1, 5), 5 * d - 7),
                (sp.Rational(55, 53), sp.Rational(-5, 7), 53 * d - 55),
            )
            extra_d, extra_c, extra_factor = exceptional_data[left_index]
            expected_support = sp.Poly(
                collision_d.as_expr() * extra_factor, d, domain=sp.QQ
            ).monic()
        require(base_resultant.sqf_part().monic() == expected_support,
                "exceptional base support")
        modular_base = reduce_mod(
            base_resultant, d, characteristic
        ).sqf_part().monic()
        modular_expected = reduce_mod(
            expected_support, d, characteristic
        )
        require(modular_base == modular_expected,
                "KoalaBear exceptional base support")
        extra_description = "none"
        if args.swap and left_index == 0:
            extra_basis = sp.groebner(
                [lead, constant, extra_factor], c, d, order="lex"
            )
            require(extra_basis.reduce(reconstruction_factor)[1] == 0,
                    "swapped exceptional component is not z=1")
            extra_description = "quadratic-z=1"
        elif not args.swap:
            c_gcd = sp.gcd(
                sp.Poly(lead.subs(d, extra_d), c, domain=sp.QQ),
                sp.Poly(constant.subs(d, extra_d), c, domain=sp.QQ),
            ).monic()
            require(c_gcd == sp.Poly(c - extra_c, c, domain=sp.QQ).monic(),
                    "exceptional extra fiber")
            require(sp.cancel(
                reconstruction_factor.subs({c: extra_c, d: extra_d})
            ) == 0, "exceptional extra is z=1")
            extra_description = f"({extra_c},{extra_d})"
        exceptional_rows.append(
            (left_index, base_resultant.degree(), digest_polynomial(base_resultant))
        )
        print(
            f"stage=exception left={left_index} degree={base_resultant.degree()} "
            f"extra={extra_description} digest={digest_polynomial(base_resultant)}",
            flush=True,
        )

    expected_generic_rows = 1 if args.right is not None else 2
    require(len(generic_rows) == expected_generic_rows
            and len(exceptional_rows) == 1,
            "coverage accounting")
    print(
        "KB_C2_112_NEAR_FIXED_XI_SQUARE_DIRECT_PASS "
        f"left={args.left} right={args.right if args.right is not None else 'all'} "
        f"generic_pairs={expected_generic_rows} exceptional_left_lines=1 "
        f"residual_allocation={'swapped-square' if args.swap else 'direct-square'} "
        f"characteristic={characteristic} "
        "mutation_catches=1"
    )


if __name__ == "__main__":
    main()
