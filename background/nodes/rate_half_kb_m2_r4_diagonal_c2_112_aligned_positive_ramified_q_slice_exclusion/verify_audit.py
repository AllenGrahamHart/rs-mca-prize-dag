#!/usr/bin/env python3
"""Independent raw-norm audit of the ramified allocation equations."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SOURCE = (
    ROOT
    / "critical/nodes/rate_half_band_closure/notes/"
    "kb_c2_112_positive_qslice_symmetric.py"
)


def load_source():
    spec = importlib.util.spec_from_file_location("symmetric_audit", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError("source load")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pair_add(left, right):
    return tuple(sp.expand(a + b) for a, b in zip(left, right))


def pair_scale(scalar, pair):
    return tuple(sp.expand(scalar * value) for value in pair)


def pair_multiply(left, right, p, t):
    a0, a1 = left
    b0, b1 = right
    return (
        sp.expand(a0 * b0 - p * a1 * b1),
        sp.expand(a0 * b1 + a1 * b0 - t * a1 * b1),
    )


def allocation_equations(name, p, t, leading, middle, constant):
    root = (sp.Integer(0), sp.Integer(1))
    root_square = (-p, -t)
    if name == "same":
        first = pair_add(pair_multiply(root, middle, p, t),
                         pair_scale(2, leading))
        second = pair_add(pair_multiply(root_square, constant, p, t),
                          pair_scale(-1, leading))
    elif name == "swap":
        first = pair_add(pair_scale(p, middle),
                         pair_scale(2, pair_multiply(root, leading, p, t)))
        second = pair_add(pair_scale(p * p, constant),
                          pair_scale(-1, pair_multiply(
                              root_square, leading, p, t)))
    else:
        first = pair_add(pair_scale(p, middle), pair_scale(-t, leading))
        second = pair_add(pair_scale(p, constant), pair_scale(-1, leading))
    return (*first, *second)


source = load_source()
checked = 0
for template in ("fixed-moving", "moving-moving"):
    variables, _, coefficients, _, relative_scale = (
        source.reconstruct_fraction_free(template)
    )
    p, t, b, w = variables
    scale = sp.Symbol("lambda_scale")
    specialized = [sp.expand(value.subs(w, 0)) for value in coefficients]
    x0, x1, x2, x3, x4 = specialized

    scale_numerator = sp.expand(relative_scale[0].subs(w, 0))
    scale_denominator = sp.expand(relative_scale[1].subs(w, 0))
    scale_value = sp.cancel(scale_numerator / scale_denominator)
    expected = (
        3 * (2 * b - 1) * (p - 1) * (p + 2 * t + 4)
        if template == "fixed-moving"
        else -3 * (b - 1) * (b + 1) * (p - 1)
        * (p + 2 * t + 4) * (5 * p + 4 * t + 5)
    )
    require(sp.cancel(scale_value - expected) == 0, "normalization audit")

    leading_pair = (x2 - p * x0, x3 - t * x0)
    linear_pair = ((1 - p) * x1, x4 - t * x1)
    gamma_pair = pair_scale(scale, (1 - p * p, t * (1 - p)))
    leading = pair_multiply(leading_pair, leading_pair, p, t)
    constant = pair_multiply(linear_pair, linear_pair, p, t)
    middle = pair_add(
        pair_scale(2, pair_multiply(leading_pair, linear_pair, p, t)),
        pair_scale(-1, pair_multiply(gamma_pair, gamma_pair, p, t)),
    )

    # Directly reduce U and scaled V modulo q and divide the forced W^2.
    W = sp.Symbol("W")
    u_pair = (
        x0 + x1 * W + x2 * W**2
        - p * (x2 + x1 * W + x0 * W**2),
        x3 * (1 + W**2) + x4 * W
        - t * (x2 + x1 * W + x0 * W**2),
    )
    v_pair = (W * (1 - p * p), W * t * (1 - p))
    direct = pair_add(
        pair_multiply(u_pair, u_pair, p, t),
        pair_scale(-W, pair_multiply(
            pair_scale(scale, v_pair), pair_scale(scale, v_pair), p, t
        )),
    )
    predicted = tuple(
        sp.expand(constant[index] + middle[index] * W + leading[index] * W**2)
        for index in range(2)
    )
    for observed, wanted in zip(direct, predicted):
        quotient, remainder = sp.div(sp.Poly(observed, W), sp.Poly(W**2, W))
        require(remainder.is_zero, "forced W^2 division")
        require(sp.expand(quotient.as_expr() - wanted) == 0, "raw norm audit")

    for allocation in ("same", "swap", "mixed"):
        generated = source.ramified_allocation_equations(
            allocation, (p, t, b, w, scale), coefficients, relative_scale
        )
        expected_equations = allocation_equations(
            allocation, p, t, leading, middle, constant
        )
        require(all(
            sp.expand(generated[index].as_expr() - expected_equations[index]) == 0
            for index in range(4)
        ), f"allocation audit {template} {allocation}")
        checked += 1

print(
    "KB_C2_112_ALIGNED_POSITIVE_RAMIFIED_AUDIT_PASS "
    f"templates=2 allocations={checked} raw_norm=true"
)
