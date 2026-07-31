#!/usr/bin/env python3
"""Test deployed moving-mixed q-slice survivors against full quotient norms.

For a degree-three survivor, adjoin ``b`` through
``b^2-trace*b+1``.  This quadratic algebra embeds in the deployed degree-six
field.  The script reconstructs ``H=U+X*V`` and its norm
``G=U^2-W*V^2``.  It then tests the squared forms of both identities

    Q_J ~ K_5^2 q,       q Q_I ~ R_7^2.

A mismatch is a rigorous rejection.  Passage is only a necessary check,
because taking the source-deck norm forgets the sign of each descended form.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import flint
import sympy as sp


DEPLOYED_PRIME = 2130706433
HERE = Path(__file__).resolve().parent
SOURCE = HERE / "kb_c2_112_positive_qslice_symmetric.py"
SOURCE_SHA256 = "bc5f958f834d978b2bb2e054cafd8ee47f46469b26c9798257f10436cc8eb45d"
SURVIVORS = (
    HERE / "kb_c2_112_aligned_positive_unramified_moving_mixed_survivors.json"
)
SURVIVORS_SHA256 = (
    "c02e649960b35e3d264472c3c1aa69cfd71d48930df8844c281b901b3e5a5f36"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_source():
    require(file_sha256(SOURCE) == SOURCE_SHA256, "source hash")
    spec = importlib.util.spec_from_file_location("positive_qslice", SOURCE)
    require(spec is not None and spec.loader is not None, "source loader")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class QuadraticAlgebra:
    """Pairs ``a+b*B`` with ``B^2=trace*B-1`` over one finite field."""

    def __init__(self, field, trace):
        self.field = field
        self.trace = trace
        self.zero = (field.zero(), field.zero())
        self.one = (field.one(), field.zero())
        self.generator = (field.zero(), field.one())

    def base(self, value):
        coefficient = self.field(value) if isinstance(value, int) else value
        return (coefficient, self.field.zero())

    def add(self, left, right):
        return (left[0] + right[0], left[1] + right[1])

    def neg(self, value):
        return (-value[0], -value[1])

    def sub(self, left, right):
        return self.add(left, self.neg(right))

    def mul(self, left, right):
        product_b = left[1] * right[1]
        return (
            left[0] * right[0] - product_b,
            left[0] * right[1] + left[1] * right[0]
            + self.trace * product_b,
        )

    def pow(self, value, exponent: int):
        result = self.one
        base = value
        while exponent:
            if exponent & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            exponent >>= 1
        return result


def trim(poly, algebra):
    result = list(poly)
    while result and result[-1] == algebra.zero:
        result.pop()
    return result


def poly_add(left, right, algebra, sign=1):
    result = [algebra.zero for _ in range(max(len(left), len(right)))]
    for index, coefficient in enumerate(left):
        result[index] = algebra.add(result[index], coefficient)
    for index, coefficient in enumerate(right):
        value = coefficient if sign == 1 else algebra.neg(coefficient)
        result[index] = algebra.add(result[index], value)
    return trim(result, algebra)


def poly_scale(poly, scalar, algebra):
    return trim([algebra.mul(value, scalar) for value in poly], algebra)


def poly_mul(left, right, algebra):
    if not left or not right:
        return []
    result = [algebra.zero for _ in range(len(left) + len(right) - 1)]
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            result[left_index + right_index] = algebra.add(
                result[left_index + right_index],
                algebra.mul(left_coefficient, right_coefficient),
            )
    return trim(result, algebra)


def poly_pow(poly, exponent: int, algebra):
    result = [algebra.one]
    base = poly
    while exponent:
        if exponent & 1:
            result = poly_mul(result, base, algebra)
        base = poly_mul(base, base, algebra)
        exponent >>= 1
    return result


def linear(root, algebra):
    return [algebra.neg(root), algebra.one]


def quadratic(a, c, algebra):
    return [c, a, algebra.one]


def evaluate_expression(expression, symbols, values, algebra):
    polynomial = sp.Poly(expression, *symbols, domain=sp.QQ)
    result = algebra.zero
    for monomial, coefficient in polynomial.terms():
        numerator = int(coefficient.p)
        denominator = int(coefficient.q)
        term = algebra.base(
            numerator * pow(denominator, -1, DEPLOYED_PRIME)
        )
        for value, exponent in zip(values, monomial):
            term = algebra.mul(term, algebra.pow(value, exponent))
        result = algebra.add(result, term)
    return result


def t_convolution(left, right, algebra):
    result = [[] for _ in range(len(left) + len(right) - 1)]
    for left_index, left_coefficient in enumerate(left):
        for right_index, right_coefficient in enumerate(right):
            result[left_index + right_index] = poly_add(
                result[left_index + right_index],
                poly_mul(left_coefficient, right_coefficient, algebra),
                algebra,
            )
    return result


def quadratic_resultant(g_coefficients, a, c, algebra):
    """Return ``Res_T(T^2+aT+c,G)`` as a polynomial in W."""
    remainder = [list(item) for item in g_coefficients]
    for degree in range(len(remainder) - 1, 1, -1):
        leading = remainder[degree]
        remainder[degree] = []
        remainder[degree - 1] = poly_add(
            remainder[degree - 1],
            poly_scale(leading, a, algebra),
            algebra,
            sign=-1,
        )
        remainder[degree - 2] = poly_add(
            remainder[degree - 2],
            poly_scale(leading, c, algebra),
            algebra,
            sign=-1,
        )
    r0, r1 = remainder[:2]
    return poly_add(
        poly_add(
            poly_mul(r0, r0, algebra),
            poly_scale(poly_mul(r0, r1, algebra), a, algebra),
            algebra,
            sign=-1,
        ),
        poly_scale(poly_mul(r1, r1, algebra), c, algebra),
        algebra,
    )


def require_associate(left, right, algebra, message):
    left = trim(left, algebra)
    right = trim(right, algebra)
    require(left and right, f"{message}: zero polynomial")
    require(len(left) == len(right), f"{message}: degree mismatch")
    left_lead = left[-1]
    right_lead = right[-1]
    require(
        all(
            algebra.mul(left_coefficient, right_lead)
            == algebra.mul(right_coefficient, left_lead)
            for left_coefficient, right_coefficient in zip(left, right)
        ),
        f"{message}: coefficient mismatch",
    )


def associate_at_root(left, right, root, algebra):
    def specialize(coefficient):
        return coefficient[0] + coefficient[1] * root

    left_values = [specialize(coefficient) for coefficient in left]
    right_values = [specialize(coefficient) for coefficient in right]
    while left_values and left_values[-1] == algebra.field.zero():
        left_values.pop()
    while right_values and right_values[-1] == algebra.field.zero():
        right_values.pop()
    if not left_values or not right_values or len(left_values) != len(right_values):
        return False
    return all(
        left_coefficient * right_values[-1]
        == right_coefficient * left_values[-1]
        for left_coefficient, right_coefficient in zip(left_values, right_values)
    )


def build_g(source, p_base, t_base, trace_base, w_base, algebra):
    variables, odd, coefficients, _, relative_scale = (
        source.reconstruct_fraction_free("moving-moving")
    )
    p_symbol, t_symbol, b_symbol, w_symbol = variables
    symbols = (b_symbol, p_symbol, t_symbol, w_symbol)
    values = (algebra.generator, p_base, t_base, w_base)
    x0, x1, x2, x3, x4 = [
        evaluate_expression(item, symbols, values, algebra)
        for item in coefficients
    ]
    f, g, m = [
        evaluate_expression(item, symbols, values, algebra) for item in odd
    ]
    scale_numerator = evaluate_expression(
        relative_scale[0], symbols, values, algebra
    )
    scale_denominator = evaluate_expression(
        relative_scale[1], symbols, values, algebra
    )
    require(scale_denominator[1] == algebra.field.zero(), "scale denominator")
    require(scale_denominator[0] != algebra.field.zero(), "zero scale denominator")
    inverse_denominator = algebra.base(algebra.field.one() / scale_denominator[0])
    scale = algebra.mul(scale_numerator, inverse_denominator)
    f, g, m = (algebra.mul(scale, value) for value in (f, g, m))

    zero = algebra.zero
    u_coefficients = (
        [x0, x1, x2],
        [x3, x4, x3],
        [x2, x1, x0],
    )
    v_coefficients = (
        [f, g],
        [m, m],
        [g, f],
    )
    u_square = t_convolution(u_coefficients, u_coefficients, algebra)
    v_square = t_convolution(v_coefficients, v_coefficients, algebra)
    for index in range(len(v_square)):
        v_square[index] = [zero, *v_square[index]]
    return [
        poly_add(u_value, v_value, algebra, sign=-1)
        for u_value, v_value in zip(u_square, v_square)
    ]


def run_survivor(source, record):
    prime_context = flint.fmpz_mod_poly_ctx(DEPLOYED_PRIME)
    modulus = prime_context(record["modulus"])
    require(modulus.degree() == 3, "probe is pinned to deployed degree-three data")
    field = flint.fq_default_ctx(modulus=modulus, fq_type="FQ_NMOD")
    trace_value = field(record["trace"])
    p_value = field(record["p"])
    t_value = field(record["t"])
    w_value = field(record["w"])
    algebra = QuadraticAlgebra(field, trace_value)
    p = algebra.base(p_value)
    t = algebra.base(t_value)
    trace = algebra.base(trace_value)
    w = algebra.base(w_value)
    one = algebra.one
    two_inverse = algebra.base(field(2) ** -1)
    p_inverse = algebra.base(p_value ** -1)
    w_inverse = algebra.base(w_value ** -1)

    g_coefficients = build_g(source, p, t, trace, w, algebra)
    fixed = (algebra.neg(algebra.mul(algebra.base(5), two_inverse)), one)
    moving = (algebra.neg(trace), one)
    crossing = (t, p)
    resultant_j = [one]
    for a, c in (fixed, moving, crossing):
        resultant_j = poly_mul(
            resultant_j,
            quadratic_resultant(g_coefficients, a, c, algebra),
            algebra,
        )

    alpha_value = p_value + 2 * t_value + 4
    beta_value = 1 + 2 * t_value + 4 * p_value
    z_value = (w_value * beta_value - alpha_value) / (
        beta_value - w_value * alpha_value
    )
    z = algebra.base(z_value)
    z_inverse = algebra.base(z_value ** -1)
    forced = (algebra.neg(algebra.add(w, w_inverse)), one)
    internal = (algebra.neg(algebra.add(z, z_inverse)), one)
    reciprocal_crossing = (
        algebra.mul(t, p_inverse),
        p_inverse,
    )
    resultant_i = [one]
    for a, c in (forced, internal, reciprocal_crossing):
        resultant_i = poly_mul(
            resultant_i,
            quadratic_resultant(g_coefficients, a, c, algebra),
            algebra,
        )

    q = quadratic(t, p, algebra)
    fixed_poly = quadratic(fixed[0], fixed[1], algebra)
    moving_poly = quadratic(moving[0], moving[1], algebra)
    reciprocal_crossing_poly = quadratic(
        reciprocal_crossing[0], reciprocal_crossing[1], algebra
    )
    internal_poly = poly_mul(linear(z, algebra), linear(z_inverse, algebra), algebra)
    k5 = poly_mul(
        linear(w, algebra),
        poly_mul(internal_poly, reciprocal_crossing_poly, algebra),
        algebra,
    )
    p_j = poly_mul(q, poly_mul(fixed_poly, moving_poly, algebra), algebra)
    r7 = poly_mul(p_j, linear(w_inverse, algebra), algebra)
    q_slice = quadratic_resultant(g_coefficients, t, p, algebra)
    q_slice_target = poly_mul(
        poly_pow(linear(w, algebra), 4, algebra),
        poly_pow(reciprocal_crossing_poly, 2, algebra),
        algebra,
    )
    require_associate(q_slice, q_slice_target, algebra, "q-slice control")
    first_target = poly_mul(poly_pow(k5, 4, algebra), poly_pow(q, 2, algebra), algebra)
    second_left = poly_mul(poly_pow(q, 2, algebra), resultant_i, algebra)
    second_target = poly_pow(r7, 4, algebra)

    discriminant = trace_value**2 - 4
    require(
        discriminant ** ((DEPLOYED_PRIME**modulus.degree() - 1) // 2)
        == field.one(),
        "moving quadratic does not split in the survivor field",
    )
    square_root = discriminant.sqrt()
    inverse_two = field(2) ** -1
    b_roots = (
        (trace_value + square_root) * inverse_two,
        (trace_value - square_root) * inverse_two,
    )
    require(b_roots[0] * b_roots[1] == field.one(), "reciprocal b roots")
    first_outcomes = tuple(
        associate_at_root(resultant_j, first_target, root, algebra)
        for root in b_roots
    )
    second_outcomes = tuple(
        associate_at_root(second_left, second_target, root, algebra)
        for root in b_roots
    )
    require(
        all(not (first and second)
            for first, second in zip(first_outcomes, second_outcomes)),
        "full quotient survivor orientation",
    )
    print(
        f"mixed_survivor={record['factor_index']} degree=3 "
        "q_slice=PASS "
        "first_quotient_norm="
        f"{','.join(str(value).upper() for value in first_outcomes)} "
        "second_quotient_norm="
        f"{','.join(str(value).upper() for value in second_outcomes)}",
        flush=True,
    )
    return first_outcomes, second_outcomes


def main() -> None:
    require(flint.__version__ == "0.9.0", "python-flint version")
    require(file_sha256(SURVIVORS) == SURVIVORS_SHA256, "survivor hash")
    payload = json.loads(SURVIVORS.read_text(encoding="ascii"))
    source = load_source()
    records = [
        item for item in payload["survivors"]
        if len(item["modulus"]) - 1 == 3
    ]
    require(tuple(item["factor_index"] for item in records) == (3, 5), "records")
    outcomes = [run_survivor(source, record) for record in records]
    orientations = sum(len(first) for first, _ in outcomes)
    rejected = sum(
        not (first and second)
        for first_values, second_values in outcomes
        for first, second in zip(first_values, second_values)
    )
    print(
        "KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_MIXED_"
        f"FULL_QUOTIENT_NORM_PROBE_PASS traces=2 orientations={orientations} "
        f"rejected={rejected} survived={orientations - rejected}",
        flush=True,
    )


if __name__ == "__main__":
    main()
