#!/usr/bin/env python3
"""Bounded exact probes for the unresolved moving-xi mixed chart."""

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


def fp2_frobenius_six_gcd(
    expression, b_relation, b_quadratic, b, c, d,
    characteristic, linear, constant
):
    """Return gcd(C, X^(p^6)-X) over F_p[t]/(t^2+linear*t+constant)."""

    modulus = characteristic
    linear %= modulus
    constant %= modulus
    zero = (0, 0)
    one = (1, 0)

    def fadd(left, right):
        return ((left[0] + right[0]) % modulus,
                (left[1] + right[1]) % modulus)

    def fsub(left, right):
        return ((left[0] - right[0]) % modulus,
                (left[1] - right[1]) % modulus)

    def fmul(left, right):
        return (
            (left[0] * right[0] - constant * left[1] * right[1]) % modulus,
            (left[0] * right[1] + left[1] * right[0]
             - linear * left[1] * right[1]) % modulus,
        )

    def finv(value):
        norm = (
            value[0] * value[0]
            - linear * value[0] * value[1]
            + constant * value[1] * value[1]
        ) % modulus
        if norm == 0:
            raise ZeroDivisionError("zero in F_p2")
        scale = pow(norm, -1, modulus)
        return (
            (value[0] - linear * value[1]) * scale % modulus,
            -value[1] * scale % modulus,
        )

    def trim(polynomial):
        result = list(polynomial)
        while result and result[-1] == zero:
            result.pop()
        return result

    def padd(left, right):
        size = max(len(left), len(right))
        return trim([
            fadd(left[index] if index < len(left) else zero,
                 right[index] if index < len(right) else zero)
            for index in range(size)
        ])

    def psub(left, right):
        size = max(len(left), len(right))
        return trim([
            fsub(left[index] if index < len(left) else zero,
                 right[index] if index < len(right) else zero)
            for index in range(size)
        ])

    def pmul(left, right):
        if not left or not right:
            return []
        result = [zero] * (len(left) + len(right) - 1)
        for i, left_value in enumerate(left):
            for j, right_value in enumerate(right):
                result[i + j] = fadd(
                    result[i + j], fmul(left_value, right_value)
                )
        return trim(result)

    def pdivmod(dividend, divisor):
        remainder = trim(dividend)
        divisor = trim(divisor)
        if not divisor:
            raise ZeroDivisionError("zero polynomial")
        quotient = [zero] * max(0, len(remainder) - len(divisor) + 1)
        inverse_lead = finv(divisor[-1])
        while len(remainder) >= len(divisor):
            shift = len(remainder) - len(divisor)
            coefficient = fmul(remainder[-1], inverse_lead)
            quotient[shift] = coefficient
            subtraction = [zero] * shift + [
                fmul(coefficient, value) for value in divisor
            ]
            remainder = psub(remainder, subtraction)
        return trim(quotient), remainder

    def pmonic(polynomial):
        polynomial = trim(polynomial)
        if not polynomial:
            return []
        scale = finv(polynomial[-1])
        return [fmul(scale, value) for value in polynomial]

    def pgcd(left, right):
        left = trim(left)
        right = trim(right)
        while right:
            _, remainder = pdivmod(left, right)
            left, right = right, remainder
        return pmonic(left)

    def ppowmod(base, exponent, modulus_polynomial):
        power = [one]
        base = pdivmod(base, modulus_polynomial)[1]
        while exponent:
            if exponent & 1:
                power = pdivmod(
                    pmul(power, base), modulus_polynomial
                )[1]
            exponent >>= 1
            if exponent:
                base = pdivmod(
                    pmul(base, base), modulus_polynomial
                )[1]
        return power

    def fpow(value, exponent):
        result = one
        base = value
        while exponent:
            if exponent & 1:
                result = fmul(result, base)
            exponent >>= 1
            if exponent:
                base = fmul(base, base)
        return result

    def evaluate(expression_value, c_value, d_value):
        source_value = sp.Poly(expression_value, c, d, domain=sp.QQ)
        _, integral_value = source_value.clear_denoms(convert=True)
        result = zero
        for (c_degree, d_degree), raw in sp.Poly(
            integral_value.as_expr(), c, d, domain=sp.ZZ
        ).terms():
            coefficient = (int(raw) % modulus, 0)
            term = fmul(
                coefficient,
                fmul(fpow(c_value, c_degree), fpow(d_value, d_degree)),
            )
            result = fadd(result, term)
        return result

    source = sp.Poly(expression, c, d, domain=sp.QQ)
    _, integral = source.clear_denoms(convert=True)
    integral_mod = sp.Poly(integral.as_expr(), c, d, modulus=modulus)
    coefficients = [zero] * (integral_mod.degree(c) + 1)
    for (c_degree, d_degree), raw_coefficient in integral_mod.terms():
        coefficient = int(raw_coefficient) % modulus
        if d_degree == 0:
            value = (coefficient, 0)
        elif d_degree == 1:
            value = (0, coefficient)
        elif d_degree == 2:
            value = (-coefficient * constant % modulus,
                     -coefficient * linear % modulus)
        else:
            raise RuntimeError("F_p2 coefficient degree")
        coefficients[c_degree] = fadd(coefficients[c_degree], value)
    polynomial = pmonic(coefficients)
    x_polynomial = [zero, one]

    def x_power_mod(exponent):
        return ppowmod(x_polynomial, exponent, polynomial)

    fixed = psub(x_power_mod(modulus**6), x_polynomial)
    common = pgcd(polynomial, fixed)
    base_fixed = psub(x_power_mod(modulus**2), x_polynomial)
    base_common = pgcd(common, base_fixed)
    extension_common, remainder = pdivmod(common, base_common)
    if remainder:
        raise RuntimeError("F_p2 component division")
    extension_common = pmonic(extension_common)
    def split_linear(polynomial_value, output):
        polynomial_value = pmonic(polynomial_value)
        degree = len(polynomial_value) - 1
        if degree == 1:
            output.append(polynomial_value)
            return
        for seed in range(1, 65):
            trial = [(seed % modulus, seed * seed % modulus), one]
            powered = ppowmod(
                trial, (modulus**2 - 1) // 2, polynomial_value
            )
            divisor = pgcd(polynomial_value, psub(powered, [one]))
            divisor_degree = len(divisor) - 1
            if 0 < divisor_degree < degree:
                quotient, split_remainder = pdivmod(
                    polynomial_value, divisor
                )
                if split_remainder:
                    raise RuntimeError("F_p2 split remainder")
                split_linear(divisor, output)
                split_linear(quotient, output)
                return
        raise RuntimeError("deterministic F_p2 split failed")

    linear_factors = []
    split_linear(base_common, linear_factors)
    c_roots = sorted(
        [fsub(zero, factor[0]) for factor in linear_factors]
    )
    relation_source = sp.Poly(b_relation, b, c, d, domain=sp.QQ)
    _, relation_integral = relation_source.clear_denoms(convert=True)
    relation_in_b = sp.Poly(relation_integral.as_expr(), b)
    relation_lead = relation_in_b.coeff_monomial(b)
    relation_constant = relation_in_b.coeff_monomial(1)
    quadratic_source = sp.Poly(b_quadratic, b, c, d, domain=sp.QQ)
    _, quadratic_integral = quadratic_source.clear_denoms(convert=True)
    quadratic_in_b = sp.Poly(quadratic_integral.as_expr(), b)
    quadratic_coefficients = [
        quadratic_in_b.coeff_monomial(b**degree) for degree in range(3)
    ]
    d_root = (0, 1)
    half = (pow(2, -1, modulus), 0)
    field_points = []
    for c_root in c_roots:
        lead_value = evaluate(relation_lead, c_root, d_root)
        constant_value = evaluate(relation_constant, c_root, d_root)
        if lead_value == zero:
            quadratic_values = [
                evaluate(value, c_root, d_root)
                for value in quadratic_coefficients
            ]
            quadratic_polynomial = pmonic(quadratic_values)
            b_fixed = psub(
                ppowmod(x_polynomial, modulus**2, quadratic_polynomial),
                x_polynomial,
            )
            b_common = pgcd(quadratic_polynomial, b_fixed)
            b_factors = []
            if len(b_common) > 1:
                split_linear(b_common, b_factors)
            field_points.append({
                "c": c_root,
                "linear_b_lead_zero": True,
                "linear_b_constant_zero": constant_value == zero,
                "quadratic_b_degree": len(quadratic_polynomial) - 1,
                "quadratic_b_fp2_degree": len(b_common) - 1,
                "quadratic_b_roots": [
                    fsub(zero, factor[0]) for factor in b_factors
                ],
            })
            continue
        b_root = fmul(fsub(zero, constant_value), finv(lead_value))
        reconstruction = fadd(
            fsub(
                fsub(fmul((5, 0), fmul(c_root, d_root)),
                     fmul((4, 0), c_root)),
                fmul((4, 0), d_root),
            ),
            (5, 0),
        )
        incidence = fadd(
            fsub(
                fadd(
                    fsub(
                        fmul((4, 0), fmul(fmul(c_root, c_root), d_root)),
                        fmul((2, 0), fmul(c_root, c_root)),
                    ),
                    fmul((3, 0), c_root),
                ),
                fmul((3, 0), fmul(c_root, d_root)),
            ),
            fsub(fmul((2, 0), d_root), (4, 0)),
        )
        field_points.append({
            "b": b_root,
            "c": c_root,
            "d": d_root,
            "forbidden": {
                "b=0": b_root == zero,
                "b=2": b_root == (2, 0),
                "b=1/2": b_root == half,
                "b=+/-1": b_root in ((1, 0), (modulus - 1, 0)),
                "c=+/-1": c_root in ((1, 0), (modulus - 1, 0)),
                "d=+/-1": d_root in ((1, 0), (modulus - 1, 0)),
                "b=c": b_root == c_root,
                "b=d": b_root == d_root,
                "c=d": c_root == d_root,
                "bc=1": fmul(b_root, c_root) == one,
                "bd=1": fmul(b_root, d_root) == one,
                "cd=1": fmul(c_root, d_root) == one,
                "z=1": reconstruction == zero,
                "finite-incidence": incidence == zero,
            },
        })
    payload = repr(common).encode("ascii")
    return {
        "polynomial_degree": len(polynomial) - 1,
        "gcd_degree": len(common) - 1,
        "gcd_digest": hashlib.sha256(payload).hexdigest()[:16],
        "gcd_coefficients": common if len(common) <= 5 else None,
        "fp2_degree": len(base_common) - 1,
        "fp2_coefficients": base_common if len(base_common) <= 5 else None,
        "relative_degree_three_part": len(extension_common) - 1,
        "relative_degree_three_coefficients": (
            extension_common if len(extension_common) <= 5 else None
        ),
        "fp2_linear_factors": linear_factors,
        "fp2_points": field_points,
    }


def fpn_field_fiber(
    expression, b_relation, b_quadratic, b, c, d,
    characteristic, modulus_coefficients
):
    """Classify a zero-dimensional fiber over a printed F_(p^n) model."""

    modulus = characteristic
    relation = tuple(value % modulus for value in modulus_coefficients)
    extension_degree = len(relation)
    zero = (0,) * extension_degree
    one = (1,) + (0,) * (extension_degree - 1)

    def fadd(left, right):
        return tuple((x + y) % modulus for x, y in zip(left, right))

    def fsub(left, right):
        return tuple((x - y) % modulus for x, y in zip(left, right))

    def fmul(left, right):
        product = [0] * (2 * extension_degree - 1)
        for i, x in enumerate(left):
            for j, y in enumerate(right):
                product[i + j] = (product[i + j] + x * y) % modulus
        for degree in range(2 * extension_degree - 2, extension_degree - 1, -1):
            coefficient = product[degree]
            if coefficient:
                for index, value in enumerate(relation):
                    product[degree - extension_degree + index] = (
                        product[degree - extension_degree + index]
                        - coefficient * value
                    ) % modulus
        return tuple(product[:extension_degree])

    def fpow(value, exponent):
        result = one
        base = value
        while exponent:
            if exponent & 1:
                result = fmul(result, base)
            exponent >>= 1
            if exponent:
                base = fmul(base, base)
        return result

    def finv(value):
        if value == zero:
            raise ZeroDivisionError("zero in extension field")
        return fpow(value, modulus**extension_degree - 2)

    def trim(polynomial):
        result = list(polynomial)
        while result and result[-1] == zero:
            result.pop()
        return result

    def psub(left, right):
        size = max(len(left), len(right))
        return trim([
            fsub(left[index] if index < len(left) else zero,
                 right[index] if index < len(right) else zero)
            for index in range(size)
        ])

    def pmul(left, right):
        if not left or not right:
            return []
        result = [zero] * (len(left) + len(right) - 1)
        for i, x in enumerate(left):
            for j, y in enumerate(right):
                result[i + j] = fadd(result[i + j], fmul(x, y))
        return trim(result)

    def pdivmod(dividend, divisor):
        remainder = trim(dividend)
        divisor = trim(divisor)
        if not divisor:
            raise ZeroDivisionError("zero polynomial")
        quotient = [zero] * max(0, len(remainder) - len(divisor) + 1)
        inverse_lead = finv(divisor[-1])
        while len(remainder) >= len(divisor):
            shift = len(remainder) - len(divisor)
            coefficient = fmul(remainder[-1], inverse_lead)
            quotient[shift] = coefficient
            remainder = psub(
                remainder,
                [zero] * shift + [fmul(coefficient, x) for x in divisor],
            )
        return trim(quotient), remainder

    def pmonic(polynomial):
        polynomial = trim(polynomial)
        if not polynomial:
            return []
        scale = finv(polynomial[-1])
        return [fmul(scale, value) for value in polynomial]

    def pgcd(left, right):
        left = trim(left)
        right = trim(right)
        while right:
            left, right = right, pdivmod(left, right)[1]
        return pmonic(left)

    def ppowmod(base, exponent, modulus_polynomial):
        power = [one]
        base = pdivmod(base, modulus_polynomial)[1]
        while exponent:
            if exponent & 1:
                power = pdivmod(pmul(power, base), modulus_polynomial)[1]
            exponent >>= 1
            if exponent:
                base = pdivmod(pmul(base, base), modulus_polynomial)[1]
        return power

    def evaluate(expression_value, c_value, d_value):
        source = sp.Poly(expression_value, c, d, domain=sp.QQ)
        _, integral = source.clear_denoms(convert=True)
        result = zero
        for (c_degree, d_degree), raw in sp.Poly(
            integral.as_expr(), c, d, domain=sp.ZZ
        ).terms():
            coefficient = (int(raw) % modulus,) + (0,) * (extension_degree - 1)
            result = fadd(
                result,
                fmul(
                    coefficient,
                    fmul(fpow(c_value, c_degree), fpow(d_value, d_degree)),
                ),
            )
        return result

    source = sp.Poly(expression, c, d, domain=sp.QQ)
    _, integral = source.clear_denoms(convert=True)
    source_mod = sp.Poly(integral.as_expr(), c, d, modulus=modulus)
    coefficients = [zero] * (source_mod.degree(c) + 1)
    for (c_degree, d_degree), raw in source_mod.terms():
        if d_degree >= extension_degree:
            raise RuntimeError("extension coefficient degree")
        value = [0] * extension_degree
        value[d_degree] = int(raw) % modulus
        coefficients[c_degree] = fadd(coefficients[c_degree], tuple(value))
    polynomial = pmonic(coefficients)
    x_polynomial = [zero, one]
    field_order = modulus**extension_degree
    target_order = modulus**6
    fixed = psub(
        ppowmod(x_polynomial, target_order, polynomial), x_polynomial
    )
    common = pgcd(polynomial, fixed)
    base_fixed = psub(
        ppowmod(x_polynomial, field_order, polynomial), x_polynomial
    )
    base_common = pgcd(common, base_fixed)
    relative_common, relative_remainder = pdivmod(common, base_common)
    if relative_remainder:
        raise RuntimeError("extension relative component division")
    relative_common = pmonic(relative_common)

    def split_linear(polynomial_value, output):
        polynomial_value = pmonic(polynomial_value)
        degree = len(polynomial_value) - 1
        if degree == 1:
            output.append(polynomial_value)
            return
        for seed in range(1, 129):
            constant_value = tuple(
                pow(seed, index + 1, modulus)
                for index in range(extension_degree)
            )
            powered = ppowmod(
                [constant_value, one],
                (field_order - 1) // 2,
                polynomial_value,
            )
            divisor = pgcd(polynomial_value, psub(powered, [one]))
            divisor_degree = len(divisor) - 1
            if 0 < divisor_degree < degree:
                quotient, remainder = pdivmod(polynomial_value, divisor)
                if remainder:
                    raise RuntimeError("extension split remainder")
                split_linear(divisor, output)
                split_linear(quotient, output)
                return
        raise RuntimeError("deterministic extension split failed")

    factors = []
    if len(base_common) > 1:
        split_linear(base_common, factors)
    c_roots = sorted(fsub(zero, factor[0]) for factor in factors)
    d_root = (0, 1) + (0,) * (extension_degree - 2)
    relation_source = sp.Poly(b_relation, b, c, d, domain=sp.QQ)
    _, relation_integral = relation_source.clear_denoms(convert=True)
    relation_in_b = sp.Poly(relation_integral.as_expr(), b)
    relation_lead = relation_in_b.coeff_monomial(b)
    relation_constant = relation_in_b.coeff_monomial(1)
    quadratic_source = sp.Poly(b_quadratic, b, c, d, domain=sp.QQ)
    _, quadratic_integral = quadratic_source.clear_denoms(convert=True)
    quadratic_in_b = sp.Poly(quadratic_integral.as_expr(), b)
    quadratic_coefficients = [
        quadratic_in_b.coeff_monomial(b**degree) for degree in range(3)
    ]
    points = []
    relative_b_degrees = []
    for c_root in c_roots:
        lead = evaluate(relation_lead, c_root, d_root)
        constant_value = evaluate(relation_constant, c_root, d_root)
        b_roots = []
        if lead != zero:
            b_roots = [fmul(fsub(zero, constant_value), finv(lead))]
        else:
            b_polynomial = pmonic([
                evaluate(value, c_root, d_root)
                for value in quadratic_coefficients
            ])
            b_fixed = psub(
                ppowmod(x_polynomial, target_order, b_polynomial), x_polynomial
            )
            b_common = pgcd(b_polynomial, b_fixed)
            b_base_fixed = psub(
                ppowmod(x_polynomial, field_order, b_polynomial), x_polynomial
            )
            b_base_common = pgcd(b_common, b_base_fixed)
            b_relative, b_relative_remainder = pdivmod(
                b_common, b_base_common
            )
            if b_relative_remainder:
                raise RuntimeError("relative b component division")
            b_relative = pmonic(b_relative)
            relative_b_degrees.append({
                "c": c_root,
                "target_degree": len(b_common) - 1,
                "base_degree": len(b_base_common) - 1,
                "relative_degree": len(b_relative) - 1,
            })
            b_factors = []
            if len(b_base_common) > 1:
                split_linear(b_base_common, b_factors)
            b_roots = [fsub(zero, factor[0]) for factor in b_factors]
        for b_root in b_roots:
            reconstruction = fadd(
                fsub(
                    fsub(fmul((5,) + zero[1:], fmul(c_root, d_root)),
                         fmul((4,) + zero[1:], c_root)),
                    fmul((4,) + zero[1:], d_root),
                ),
                (5,) + zero[1:],
            )
            half = (pow(2, -1, modulus),) + zero[1:]
            points.append({
                "b": b_root,
                "c": c_root,
                "d": d_root,
                "forbidden": {
                    "b=0": b_root == zero,
                    "b=2": b_root == (2,) + zero[1:],
                    "b=1/2": b_root == half,
                    "b=+/-1": b_root in (
                        one, (modulus - 1,) + zero[1:]
                    ),
                    "c=+/-1": c_root in (
                        one, (modulus - 1,) + zero[1:]
                    ),
                    "b=c": b_root == c_root,
                    "b=d": b_root == d_root,
                    "c=d": c_root == d_root,
                    "bc=1": fmul(b_root, c_root) == one,
                    "bd=1": fmul(b_root, d_root) == one,
                    "cd=1": fmul(c_root, d_root) == one,
                    "z=1": reconstruction == zero,
                },
            })
    return {
        "extension_degree": extension_degree,
        "c_polynomial_degree": len(polynomial) - 1,
        "c_field_gcd_degree": len(common) - 1,
        "c_base_field_degree": len(base_common) - 1,
        "c_relative_extension_degree": len(relative_common) - 1,
        "c_linear_factors": len(factors),
        "relative_b_degrees": relative_b_degrees,
        "points": points,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "resultant",
        choices=(
            "c", "d", "product", "sum",
            "within00", "within01", "within10", "within11",
            "within11mod",
            "fiber-d17", "fiber-q3",
            "fiber-w01", "fiber-w10",
            "field-w01-l", "field-w01-q0", "field-w01-q1",
            "field-w10-l0", "field-w10-l1", "field-w10-s6",
            "high-p0", "high-p1", "high-s0", "high-s1", "high-s2",
            "high-g00", "high-g01", "high-g10", "high-g11",
            "field-hp0-l0", "field-hp0-l1",
            "field-hp0-q0", "field-hp0-q1", "field-hp0-q2",
            "field-hp1-l0", "field-hp1-q0", "field-hp1-q1",
            "field-hp1-r0", "field-hp1-r1", "field-hp1-s6",
        ),
    )
    args = parser.parse_args()

    direct = load_direct()
    b, c, d = sp.symbols("b c d", nonzero=True)
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
    fixed = direct.edge(a, 1 / a)
    moving = direct.edge(a, b)
    interpolation = sp.Matrix([
        sp.cancel(value)
        for value in (
            ((ell0 + b * ell1) * fixed
             + (ell0 + sp.Rational(1, 2) * ell1) * moving)
            / (b - sp.Rational(1, 2))
        )
    ])

    at_w = direct.evaluation(w)
    at_z = direct.evaluation(z)
    source_matrix = sp.Matrix.vstack(
        at_w[0] - q0 * at_w[2],
        at_w[1] - q1 * at_w[2],
        *at_z,
    )
    solution = [
        sp.cancel(value)
        for value in source_matrix.inv(method="DM")
        * sp.Matrix([0, 0, *interpolation])
    ]
    print("stage=source_reconstruction", flush=True)

    def residual(root):
        x0, x1, x2, x3, x4 = solution
        even0 = sp.cancel(x0 + root * x3 + root**2 * x2)
        even1 = sp.cancel(x1 + root * x4 + root**2 * x1)
        even2 = sp.cancel(x2 + root * x3 + root**2 * x0)
        local_odd1 = sp.cancel(odd2 + root * odd1 + root**2 * odd0)
        leading = sp.cancel(even2**2)
        middle = sp.cancel(
            2 * even1 * even2 - local_odd1**2 + 2 * w * leading
        )
        constant = sp.cancel(even0**2 / w**2)
        return leading, middle, constant

    h = 4 * c**2 * d - 2 * c**2 - 3 * c * d + 3 * c + 2 * d - 4
    cores = {}
    for root_name, root in (("c", c), ("d", d)):
        leading, middle, constant = residual(root)
        equations = {
            "product": constant - leading / (b * d),
            "sum": middle + (1 / b + 1 / d) * leading,
        }
        for kind, equation in equations.items():
            numerator = sp.fraction(sp.cancel(equation))[0]
            polynomial = sp.Poly(
                numerator, b, c, d, domain=sp.QQ
            ).primitive()[1]
            if kind == "product":
                polynomial = polynomial.exquo(
                    sp.Poly(h**2, b, c, d, domain=sp.QQ)
                ).primitive()[1]
            cores[(root_name, kind)] = polynomial
            print(
                f"stage={root_name}_{kind} "
                f"degrees={tuple(polynomial.degree(x) for x in (b,c,d))} "
                f"terms={len(polynomial.terms())} digest={digest(polynomial)}",
                flush=True,
            )

    field_candidates = {
        "field-w01-l": d - 616787200,
        "field-w01-q0": d**2 - 746249270 * d - 422041203,
        "field-w01-q1": d**2 - 588829660 * d + 482711260,
        "field-w10-l0": d + 288571956,
        "field-w10-l1": d - 487213652,
        "field-w10-s6": (
            d**6 + 714848107 * d**5 + 703111546 * d**4
            + 252897233 * d**3 + 344006764 * d**2
            - 1006662141 * d - 110939493
        ),
        "field-hp0-l0": d + 927463048,
        "field-hp0-l1": d + 80227901,
        "field-hp0-q0": d**2 + 958999809 * d + 65368811,
        "field-hp0-q1": d**2 - 826991582 * d - 202957287,
        "field-hp0-q2": d**2 - 80227901 * d - 730078611,
        "field-hp1-l0": d + 895796957,
        "field-hp1-q0": d**2 + 8543134 * d - 269706851,
        "field-hp1-q1": d**2 - 832867459 * d - 841426149,
        "field-hp1-r0": (
            d**3 + 720406365 * d**2 + 262219802 * d + 854470722
        ),
        "field-hp1-r1": (
            d**3 - 562719028 * d**2 + 744345501 * d + 69494986
        ),
        "field-hp1-s6": (
            d**6 - 346957095 * d**5 + 367719326 * d**4
            + 829539208 * d**3 + 382622521 * d**2
            - 497110350 * d + 206580260
        ),
    }
    if args.resultant in field_candidates:
        characteristic = 2130706433

        def integralize(polynomial):
            _, integral = polynomial.clear_denoms(convert=True)
            return integral.as_expr()

        basis = sp.groebner(
            [
                *(integralize(value) for value in cores.values()),
                field_candidates[args.resultant],
            ],
            b,
            c,
            d,
            order="lex",
            modulus=characteristic,
        )
        records = []
        for value in basis.polys:
            record = {
                "degrees": tuple(value.degree(x) for x in (b, c, d)),
                "terms": len(value.terms()),
                "digest": digest(value),
            }
            active = [x for x in (b, c, d) if value.degree(x) > 0]
            if len(active) == 1:
                factors = sp.factor_list(
                    value.as_expr(), modulus=characteristic
                )[1]
                record["factor_degrees"] = [
                    (sp.Poly(factor, active[0], modulus=characteristic).degree(),
                     exponent)
                    for factor, exponent in factors
                ]
            records.append(record)
        field_points = []
        extension_points = None
        d_candidate = sp.Poly(
            field_candidates[args.resultant], d, modulus=characteristic
        )
        basis_is_unit = (
            len(basis.polys) == 1 and basis.polys[0].as_expr() == 1
        )
        if d_candidate.degree() == 2 and not basis_is_unit:
            c_relation = next(
                value for value in basis.polys
                if value.degree(b) == 0 and value.degree(c) > 0
            )
            b_relation = next(
                value for value in basis.polys if value.degree(b) == 1
            )
            b_quadratic = next(
                value for value in basis.polys if value.degree(b) == 2
            )
            d_coefficients = [
                int(value) % characteristic
                for value in d_candidate.monic().all_coeffs()
            ]
            extension_points = fp2_frobenius_six_gcd(
                c_relation.as_expr(),
                b_relation.as_expr(),
                b_quadratic.as_expr(),
                b,
                c,
                d,
                characteristic,
                d_coefficients[1],
                d_coefficients[2],
            )
        if d_candidate.degree() in (3, 6) and not basis_is_unit:
            c_relation = next(
                value for value in basis.polys
                if value.degree(b) == 0 and value.degree(c) > 0
            )
            b_relation = next(
                value for value in basis.polys if value.degree(b) == 1
            )
            b_quadratic = next(
                value for value in basis.polys if value.degree(b) == 2
            )
            d_coefficients = [
                int(value) % characteristic
                for value in d_candidate.monic().all_coeffs()
            ]
            extension_points = fpn_field_fiber(
                c_relation.as_expr(),
                b_relation.as_expr(),
                b_quadratic.as_expr(),
                b,
                c,
                d,
                characteristic,
                list(reversed(d_coefficients[1:])),
            )
        if d_candidate.degree() == 1 and [
            value for value in basis.polys
            if value.degree(b) == 0 and value.degree(c) > 0
            and value.degree(d) == 0
        ]:
            d_coefficients = [int(value) % characteristic
                              for value in d_candidate.all_coeffs()]
            d_value = (
                -d_coefficients[1]
                * pow(d_coefficients[0], -1, characteristic)
            ) % characteristic
            c_eliminant = next(
                value for value in basis.polys
                if value.degree(b) == 0 and value.degree(c) > 0
                and value.degree(d) == 0
            )
            for c_factor, c_exponent in sp.factor_list(
                c_eliminant.as_expr(), modulus=characteristic
            )[1]:
                c_polynomial = sp.Poly(c_factor, c, modulus=characteristic)
                if c_polynomial.degree() != 1:
                    field_points.append({
                        "c_factor_degree": c_polynomial.degree(),
                        "c_multiplicity": c_exponent,
                    })
                    continue
                c_coefficients = [int(value) % characteristic
                                  for value in c_polynomial.all_coeffs()]
                c_value = (
                    -c_coefficients[1]
                    * pow(c_coefficients[0], -1, characteristic)
                ) % characteristic
                b_polynomials = [
                    sp.Poly(
                        value.as_expr().subs({c: c_value, d: d_value}),
                        b,
                        modulus=characteristic,
                    )
                    for value in cores.values()
                ]
                b_common = b_polynomials[0]
                for value in b_polynomials[1:]:
                    b_common = sp.gcd(b_common, value)
                for b_factor, b_exponent in sp.factor_list(
                    b_common.monic().as_expr(), modulus=characteristic
                )[1]:
                    b_polynomial = sp.Poly(
                        b_factor, b, modulus=characteristic
                    )
                    if b_polynomial.degree() != 1:
                        field_points.append({
                            "c": c_value,
                            "b_factor_degree": b_polynomial.degree(),
                        })
                        continue
                    b_coefficients = [int(value) % characteristic
                                      for value in b_polynomial.all_coeffs()]
                    b_value = (
                        -b_coefficients[1]
                        * pow(b_coefficients[0], -1, characteristic)
                    ) % characteristic
                    half = pow(2, -1, characteristic)
                    reconstruction = (
                        5 * c_value * d_value - 4 * c_value
                        - 4 * d_value + 5
                    ) % characteristic
                    incidence = (
                        4 * c_value**2 * d_value - 2 * c_value**2
                        - 3 * c_value * d_value + 3 * c_value
                        + 2 * d_value - 4
                    ) % characteristic
                    field_points.append({
                        "b": b_value,
                        "c": c_value,
                        "d": d_value,
                        "multiplicities": (b_exponent, c_exponent),
                        "forbidden": {
                            "b=0": b_value == 0,
                            "b=2": b_value == 2,
                            "b=1/2": b_value == half,
                            "b=+/-1": b_value in (1, characteristic - 1),
                            "c=+/-1": c_value in (1, characteristic - 1),
                            "d=+/-1": d_value in (1, characteristic - 1),
                            "b=c": b_value == c_value,
                            "b=d": b_value == d_value,
                            "c=d": c_value == d_value,
                            "bc=1": b_value * c_value % characteristic == 1,
                            "bd=1": b_value * d_value % characteristic == 1,
                            "cd=1": c_value * d_value % characteristic == 1,
                            "z=1": reconstruction == 0,
                            "finite-incidence": incidence == 0,
                        },
                    })
        print(
            f"stage=mixed_field_fiber fiber={args.resultant} "
            f"basis={records} points={field_points} "
            f"extension={extension_points}",
            flush=True,
        )
        print("INCOMPLETE moving-xi mixed field fiber classified")
        return

    high_cross = {
        "high-p0": ("product", "ddb8e78f19e438e9"),
        "high-p1": ("product", "9274da18c1badf2f"),
        "high-s0": ("sum", "ee2af867169ac2c1"),
        "high-s1": ("sum", "681883ebcea0c350"),
        "high-s2": ("sum", "4942738e6e3bfaea"),
    }
    if args.resultant in high_cross:
        characteristic = 2130706433
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
        high_component = next(
            sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
            for factor, _ in sp.factor_list(within_c.as_expr())[1]
            if digest(sp.Poly(factor, c, d, domain=sp.QQ))
            == "842d5d9a084f107e"
        )
        kind, wanted_digest = high_cross[args.resultant]
        explicit_cross = {
            "high-p0": c**2 * d - 2,
            "high-s0": 2 * c * d - 2 * d - 1,
            "high-s1": (
                30*c**5*d**4 - 7*c**5*d**3 - 36*c**5*d**2
                + 24*c**5*d - 4*c**5 - 99*c**4*d**4
                + 128*c**4*d**3 + 42*c**4*d**2 - 84*c**4*d
                + 20*c**4 + 75*c**3*d**4 - 145*c**3*d**3
                - 60*c**3*d**2 + 165*c**3*d - 49*c**3
                - 27*c**2*d**4 + 116*c**2*d**3 - 27*c**2*d**2
                - 150*c**2*d + 74*c**2 + 12*c*d**4
                - 82*c*d**3 + 96*c*d**2 + 45*c*d - 64*c
                + 8*d**3 - 15*d**2 - 18*d + 32
            ),
        }
        if args.resultant in explicit_cross:
            cross_component = sp.Poly(
                explicit_cross[args.resultant], c, d, domain=sp.QQ
            )
        else:
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
            cross_component = next(
                sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
                for factor, _ in sp.factor_list(cross.as_expr())[1]
                if digest(sp.Poly(factor, c, d, domain=sp.QQ)) == wanted_digest
            )
        direct.require(
            digest(cross_component) == wanted_digest,
            "pinned high-cross component",
        )
        print(
            f"stage=high_cross_components factor={args.resultant} "
            f"high_degrees=({high_component.degree(c)},{high_component.degree(d)}) "
            f"cross_degrees=({cross_component.degree(c)},{cross_component.degree(d)})",
            flush=True,
        )
        coefficient_domain = sp.GF(characteristic).poly_ring(d)
        high_mod = sp.Poly(
            high_component.as_expr(), c, domain=coefficient_domain
        )
        cross_mod = sp.Poly(
            cross_component.as_expr(), c, domain=coefficient_domain
        )
        projection_expression = high_mod.resultant(cross_mod)
        projection = sp.Poly(
            projection_expression.as_expr(), d, modulus=characteristic
        ).monic()
        print(
            f"stage=high_cross_projection factor={args.resultant} "
            f"degree={projection.degree()} terms={len(projection.terms())} "
            f"digest={digest(projection)}",
            flush=True,
        )
        factors = sp.factor_list(
            projection.as_expr(), modulus=characteristic
        )[1]
        print(
            f"stage=high_cross_factors factor={args.resultant} "
            f"factors={[(sp.Poly(value, d, modulus=characteristic).degree(), exponent, str(sp.Poly(value, d, modulus=characteristic).as_expr()) if sp.Poly(value, d, modulus=characteristic).degree() <= 6 else None) for value, exponent in factors]}",
            flush=True,
        )
        print("INCOMPLETE moving-xi mixed high-cross support")
        return

    if args.resultant in ("high-g00", "high-g01", "high-g10", "high-g11"):
        characteristic = 2130706433
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
        high_component = next(
            sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
            for factor, _ in sp.factor_list(within_c.as_expr())[1]
            if digest(sp.Poly(factor, c, d, domain=sp.QQ))
            == "842d5d9a084f107e"
        )
        coefficient_domain = sp.GF(characteristic).poly_ring(d)
        high_mod = sp.Poly(
            high_component.as_expr(), c, domain=coefficient_domain
        )
        product_index = int(args.resultant[-2])
        sum_index = int(args.resultant[-1])
        if product_index == 0:
            product_component = sp.Poly(c**2 * d - 2, c, d, domain=sp.QQ)
        else:
            product_cross = sp.Poly(
                sp.resultant(
                    cores[("c", "product")].as_expr(),
                    cores[("d", "product")].as_expr(),
                    b,
                ),
                c,
                d,
                domain=sp.QQ,
            ).primitive()[1]
            product_component = next(
                sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
                for factor, _ in sp.factor_list(product_cross.as_expr())[1]
                if digest(sp.Poly(factor, c, d, domain=sp.QQ))
                == "9274da18c1badf2f"
            )
        sum_component = sp.Poly(
            (
                2*c*d - 2*d - 1 if sum_index == 0 else
                30*c**5*d**4 - 7*c**5*d**3 - 36*c**5*d**2
                + 24*c**5*d - 4*c**5 - 99*c**4*d**4
                + 128*c**4*d**3 + 42*c**4*d**2 - 84*c**4*d
                + 20*c**4 + 75*c**3*d**4 - 145*c**3*d**3
                - 60*c**3*d**2 + 165*c**3*d - 49*c**3
                - 27*c**2*d**4 + 116*c**2*d**3 - 27*c**2*d**2
                - 150*c**2*d + 74*c**2 + 12*c*d**4
                - 82*c*d**3 + 96*c*d**2 + 45*c*d - 64*c
                + 8*d**3 - 15*d**2 - 18*d + 32
            ),
            c,
            d,
            domain=sp.QQ,
        )
        projections = []
        for cross_component in (product_component, sum_component):
            cross_mod = sp.Poly(
                cross_component.as_expr(), c, domain=coefficient_domain
            )
            value = high_mod.resultant(cross_mod)
            projections.append(sp.Poly(
                value.as_expr(), d, modulus=characteristic
            ).monic())
        common = sp.gcd(*projections).sqf_part().monic()
        factors = sp.factor_list(
            common.as_expr(), modulus=characteristic
        )[1]
        print(
            f"stage=high_cross_gcd pair={product_index},{sum_index} "
            f"degrees={tuple(value.degree() for value in projections)} "
            f"gcd_degree={common.degree()} gcd_digest={digest(common)} "
            f"factors={[(sp.Poly(value, d, modulus=characteristic).degree(), exponent, str(sp.Poly(value, d, modulus=characteristic).as_expr()) if sp.Poly(value, d, modulus=characteristic).degree() <= 6 else None) for value, exponent in factors]}",
            flush=True,
        )
        print("INCOMPLETE moving-xi mixed high-cross pair support")
        return

    if args.resultant in ("fiber-d17", "fiber-q3"):
        candidate = {
            "fiber-d17": 19 * d - 17,
            "fiber-q3": 2 * d**3 - 19 * d**2 + 19 * d - 14,
        }[args.resultant]
        basis = sp.groebner(
            [
                cores[("c", "product")].as_expr(),
                cores[("c", "sum")].as_expr(),
                cores[("d", "product")].as_expr(),
                cores[("d", "sum")].as_expr(),
                candidate,
            ],
            b,
            c,
            d,
            order="lex",
            domain=sp.QQ,
        )
        records = []
        for value in basis.polys:
            polynomial = sp.Poly(value, b, c, d, domain=sp.QQ)
            record = {
                "degrees": tuple(polynomial.degree(x) for x in (b, c, d)),
                "terms": len(polynomial.terms()),
                "digest": digest(polynomial),
            }
            active = [
                x for x in (b, c, d) if polynomial.degree(x) > 0
            ]
            if len(active) == 1:
                _, integral = sp.Poly(
                    polynomial.as_expr(), active[0], domain=sp.QQ
                ).clear_denoms(convert=True)
                factors = sp.factor_list(
                    integral.as_expr(), modulus=2130706433
                )[1]
                record["modular_factor_degrees"] = [
                    (sp.Poly(factor, active[0], modulus=2130706433).degree(), exponent)
                    for factor, exponent in factors
                ]
                record["modular_factors"] = [
                    (str(sp.Poly(
                        factor, active[0], modulus=2130706433
                    ).as_expr()), exponent)
                    for factor, exponent in factors
                ]
            records.append(record)
        deployed_points = []
        if args.resultant == "fiber-d17":
            characteristic = 2130706433
            c_eliminant = next(
                sp.Poly(value.as_expr(), c, domain=sp.QQ)
                for value in basis.polys
                if value.degree(b) == 0
                and value.degree(c) == 8
                and value.degree(d) == 0
            )
            _, c_integral = c_eliminant.clear_denoms(convert=True)
            c_factors = sp.factor_list(
                c_integral.as_expr(), modulus=characteristic
            )[1]
            d_value = 17 * pow(19, -1, characteristic) % characteristic
            for c_factor, c_exponent in c_factors:
                c_polynomial = sp.Poly(c_factor, c, modulus=characteristic)
                if c_polynomial.degree() != 1:
                    continue
                c_coefficients = [int(value) % characteristic
                                  for value in c_polynomial.all_coeffs()]
                c_value = (
                    -c_coefficients[1]
                    * pow(c_coefficients[0], -1, characteristic)
                ) % characteristic
                b_polynomials = [
                    sp.Poly(
                        polynomial.as_expr().subs({c: c_value, d: d_value}),
                        b,
                        modulus=characteristic,
                    )
                    for polynomial in cores.values()
                ]
                b_common = b_polynomials[0]
                for polynomial in b_polynomials[1:]:
                    b_common = sp.gcd(b_common, polynomial)
                b_common = b_common.monic()
                for b_factor, b_exponent in sp.factor_list(
                    b_common.as_expr(), modulus=characteristic
                )[1]:
                    b_polynomial = sp.Poly(
                        b_factor, b, modulus=characteristic
                    )
                    if b_polynomial.degree() != 1:
                        deployed_points.append({
                            "c": c_value,
                            "c_multiplicity": c_exponent,
                            "b_factor_degree": b_polynomial.degree(),
                            "b_multiplicity": b_exponent,
                        })
                        continue
                    b_coefficients = [int(value) % characteristic
                                      for value in b_polynomial.all_coeffs()]
                    b_value = (
                        -b_coefficients[1]
                        * pow(b_coefficients[0], -1, characteristic)
                    ) % characteristic
                    half = pow(2, -1, characteristic)
                    reconstruction = (
                        5 * c_value * d_value - 4 * c_value
                        - 4 * d_value + 5
                    ) % characteristic
                    incidence = (
                        4 * c_value**2 * d_value - 2 * c_value**2
                        - 3 * c_value * d_value + 3 * c_value
                        + 2 * d_value - 4
                    ) % characteristic
                    deployed_points.append({
                        "b": b_value,
                        "c": c_value,
                        "d": d_value,
                        "multiplicities": (b_exponent, c_exponent),
                        "forbidden": {
                            "b=2": b_value == 2,
                            "b=1/2": b_value == half,
                            "b=+/-1": b_value in (1, characteristic - 1),
                            "c=+/-1": c_value in (1, characteristic - 1),
                            "d=+/-1": d_value in (1, characteristic - 1),
                            "b=c": b_value == c_value,
                            "b=d": b_value == d_value,
                            "c=d": c_value == d_value,
                            "bc=1": b_value * c_value % characteristic == 1,
                            "bd=1": b_value * d_value % characteristic == 1,
                            "cd=1": c_value * d_value % characteristic == 1,
                            "z=1": reconstruction == 0,
                            "finite-incidence": incidence == 0,
                        },
                    })
        if args.resultant == "fiber-q3":
            characteristic = 2130706433
            d_eliminant = next(
                sp.Poly(value.as_expr(), d, domain=sp.QQ)
                for value in basis.polys
                if value.degree(b) == 0
                and value.degree(c) == 0
                and value.degree(d) == 3
            )
            _, d_integral = d_eliminant.clear_denoms(convert=True)
            d_factors = sp.factor_list(
                d_integral.as_expr(), modulus=characteristic
            )[1]
            c_relation = next(
                value for value in basis.polys
                if value.degree(b) == 0 and value.degree(c) == 10
            )
            b_relation = next(
                value for value in basis.polys
                if value.degree(b) == 1
            )
            b_quadratic = next(
                value for value in basis.polys
                if value.degree(b) == 2
            )
            _, c_relation_integral = sp.Poly(
                c_relation.as_expr(), c, d, domain=sp.QQ
            ).clear_denoms(convert=True)
            for d_factor, d_exponent in d_factors:
                d_polynomial = sp.Poly(d_factor, d, modulus=characteristic)
                if d_polynomial.degree() == 2:
                    coefficients = [int(value) % characteristic
                                    for value in d_polynomial.monic().all_coeffs()]
                    deployed_points.append({
                        "d_factor": str(d_polynomial.monic().as_expr()),
                        "d_multiplicity": d_exponent,
                        "fp2_frobenius_six": fp2_frobenius_six_gcd(
                            c_relation.as_expr(),
                            b_relation.as_expr(),
                            b_quadratic.as_expr(),
                            b,
                            c,
                            d,
                            characteristic,
                            coefficients[1],
                            coefficients[2],
                        ),
                    })
                    continue
                if d_polynomial.degree() != 1:
                    continue
                coefficients = [int(value) % characteristic
                                for value in d_polynomial.all_coeffs()]
                d_value = (
                    -coefficients[1] * pow(coefficients[0], -1, characteristic)
                ) % characteristic
                specialized = sp.Poly(
                    c_relation_integral.as_expr().subs(d, d_value),
                    c,
                    modulus=characteristic,
                )
                c_factors = sp.factor_list(specialized.as_expr())[1]
                deployed_points.append({
                    "d": d_value,
                    "d_multiplicity": d_exponent,
                    "c_factors": [
                        {
                            "degree": sp.Poly(
                                factor, c, modulus=characteristic
                            ).degree(),
                            "multiplicity": exponent,
                            "expression": str(sp.Poly(
                                factor, c, modulus=characteristic
                            ).as_expr()),
                        }
                        for factor, exponent in c_factors
                    ],
                })
        print(
            f"stage=mixed_fiber fiber={args.resultant[6:]} "
            f"basis={records} deployed_points={deployed_points}",
            flush=True,
        )
        print("INCOMPLETE moving-xi mixed fiber classified")
        return

    pairs = {
        "c": (("c", "product"), ("c", "sum")),
        "d": (("d", "product"), ("d", "sum")),
        "product": (("c", "product"), ("d", "product")),
        "sum": (("c", "sum"), ("d", "sum")),
    }
    if args.resultant.startswith("within") or args.resultant.startswith("fiber-w"):
        components = {}
        for root_name in ("c", "d"):
            within = sp.Poly(
                sp.resultant(
                    cores[(root_name, "product")].as_expr(),
                    cores[(root_name, "sum")].as_expr(),
                    b,
                ),
                c,
                d,
                domain=sp.QQ,
            ).primitive()[1]
            selected = [
                sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
                for factor, _ in sp.factor_list(within.as_expr())[1]
                if (
                    sp.Poly(factor, c, d).degree(c),
                    sp.Poly(factor, c, d).degree(d),
                ) in ((3, 2), (16, 14))
            ]
            direct.require(len(selected) == 2, "within component count")
            components[root_name] = sorted(
                selected, key=lambda value: value.degree(c)
            )
        if args.resultant == "within11mod":
            left_index, right_index = 1, 1
        else:
            left_index = int(args.resultant[-2])
            right_index = int(args.resultant[-1])
        left = components["c"][left_index]
        right = components["d"][right_index]
        print(
            "stage=within_components "
            f"pair={left_index},{right_index} "
            f"left_degrees=({left.degree(c)},{left.degree(d)}) "
            f"left_digest={digest(left)} "
            f"right_degrees=({right.degree(c)},{right.degree(d)}) "
            f"right_digest={digest(right)}",
            flush=True,
        )
        if args.resultant == "within11mod":
            characteristic = 2130706433
            coefficient_domain = sp.GF(characteristic).poly_ring(d)
            left_mod = sp.Poly(left.as_expr(), c, domain=coefficient_domain)
            right_mod = sp.Poly(right.as_expr(), c, domain=coefficient_domain)
            print("stage=within_modular_resultant_start pair=1,1", flush=True)
            projection_expression = left_mod.resultant(right_mod)
            projection = sp.Poly(
                projection_expression.as_expr(), d, modulus=characteristic
            ).monic()
            print(
                "stage=within_modular_projection_built pair=1,1 "
                f"degree={projection.degree()} terms={len(projection.terms())} "
                f"digest={digest(projection)}",
                flush=True,
            )
            factors = sp.factor_list(
                projection.as_expr(), modulus=characteristic
            )[1]
            print(
                "stage=within_modular_projection_factored pair=1,1 "
                f"degrees={[(sp.Poly(value, d, modulus=characteristic).degree(), exponent) for value, exponent in factors]}",
                flush=True,
            )
            print("INCOMPLETE moving-xi mixed high-high modular support")
            return
        projection = sp.Poly(
            sp.resultant(left.as_expr(), right.as_expr(), c),
            d,
            domain=sp.QQ,
        ).primitive()[1]
        print(
            "stage=within_projection_built "
            f"pair={left_index},{right_index} degree={projection.degree()} "
            f"terms={len(projection.terms())} digest={digest(projection)}",
            flush=True,
        )
        records = []
        for factor, exponent in sp.factor_list(projection.as_expr())[1]:
            polynomial = sp.Poly(factor, d, domain=sp.QQ).primitive()[1]
            records.append({
                "multiplicity": exponent,
                "degree": polynomial.degree(),
                "digest": digest(polynomial),
                "expression": str(polynomial.as_expr())
                if polynomial.degree() <= 12 else None,
            })
        print(
            f"stage=within_projection_factored pair={left_index},{right_index} "
            f"factors={records}",
            flush=True,
        )
        if args.resultant.startswith("fiber-w"):
            candidate = next(
                sp.Poly(factor, d, domain=sp.QQ).primitive()[1]
                for factor, _ in sp.factor_list(projection.as_expr())[1]
                if sp.Poly(factor, d).degree() == 40
            )
            print(
                "stage=within_degree40_fiber "
                f"pair={left_index},{right_index} digest={digest(candidate)}",
                flush=True,
            )
            _, integral_candidate = candidate.clear_denoms(convert=True)
            modular_factors = sp.factor_list(
                integral_candidate.as_expr(), modulus=2130706433
            )[1]
            print(
                "stage=within_degree40_modular_factors "
                f"pair={left_index},{right_index} "
                f"factors={[(sp.Poly(value, d, modulus=2130706433).degree(), exponent, str(sp.Poly(value, d, modulus=2130706433).as_expr()) if sp.Poly(value, d, modulus=2130706433).degree() <= 6 else None) for value, exponent in modular_factors]}",
                flush=True,
            )
            print("INCOMPLETE moving-xi mixed degree-40 field support classified")
            return
        print("INCOMPLETE moving-xi mixed within intersection factored")
        return

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
        polynomial = sp.Poly(factor, c, d, domain=sp.QQ).primitive()[1]
        records.append({
            "multiplicity": exponent,
            "degrees": (polynomial.degree(c), polynomial.degree(d)),
            "terms": len(polynomial.terms()),
            "digest": digest(polynomial),
            "expression": str(polynomial.as_expr())
            if len(polynomial.terms()) <= 120 else None,
        })
    print(
        f"stage=resultant_factored pair={args.resultant} factors={records}",
        flush=True,
    )
    print("INCOMPLETE moving-xi mixed resultant factored")


if __name__ == "__main__":
    main()
