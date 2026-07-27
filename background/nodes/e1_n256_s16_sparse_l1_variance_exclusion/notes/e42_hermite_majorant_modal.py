#!/usr/bin/env python3
"""Find a rational-node cubic Hermite majorant for the M3<=3660 endpoint."""

from __future__ import annotations

import modal


app = modal.App("e1-n256-e42-hermite-majorant")
image = modal.Image.debian_slim().pip_install("sympy")


@app.function(image=image, cpu=1.0, memory=256, timeout=60)
def derive() -> dict[str, object]:
    import itertools

    import sympy as sp

    y = sp.symbols("y")
    log_a, log_b = sp.symbols("log_a log_b")
    coefficients = sp.symbols("c0:4")
    polynomial = sum(coefficients[index] * y**index for index in range(4))
    rows = []

    for left, right in ((14, 60), (14, 61), (14, 62), (15, 60), (15, 61)):
        solution = sp.solve(
            (
                sp.Eq(polynomial.subs(y, left), log_a),
                sp.Eq(sp.diff(polynomial, y).subs(y, left), sp.Rational(1, left)),
                sp.Eq(polynomial.subs(y, right), log_b),
                sp.Eq(sp.diff(polynomial, y).subs(y, right), sp.Rational(1, right)),
            ),
            coefficients,
            rational=True,
        )
        expected = sp.expand(
            solution[coefficients[0]]
            + 16 * solution[coefficients[1]]
            + 340 * solution[coefficients[2]]
            + 11788 * solution[coefficients[3]]
        )
        exact_expected = expected.subs(
            {log_a: sp.log(left), log_b: sp.log(right)}
        )
        target = sp.Rational(125, 32) * sp.log(2)
        rows.append(
            {
                "left": left,
                "right": right,
                "leading_coefficient": str(solution[coefficients[3]]),
                "expected_expression": str(expected),
                "target_margin_80_digits": str(sp.N(target - exact_expected, 80)),
                "coefficients": [str(solution[value]) for value in coefficients],
            }
        )

    layer_caps = []
    for counts in itertools.product(
        range(43), range(11), range(5), range(3), range(2), range(2)
    ):
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        energy = sum(
            (index + 1) ** 2 * count for index, count in enumerate(counts)
        )
        if energy != 42 or l1_norm > 24 or sum(counts) > 21:
            continue
        layer_sizes = [
            2 * sum(counts[level:])
            for level in range(len(counts))
            if sum(counts[level:])
        ]
        cap = 0
        for first in layer_sizes:
            for second in layer_sizes:
                for third in layer_sizes:
                    pair_bounds = (
                        first * second - min(first, second),
                        first * third - min(first, third),
                        second * third - min(second, third),
                    )
                    cap += min(pair_bounds)
        layer_caps.append(
            {
                "counts_n1_through_n6": counts,
                "l1_norm": l1_norm,
                "support_size": sum(counts),
                "layer_sizes": layer_sizes,
                "third_moment_cap": cap,
            }
        )
    layer_caps.sort(key=lambda row: row["third_moment_cap"], reverse=True)

    return {
        "complete": True,
        "third_moment_cap": 3660,
        "partition_count": len(layer_caps),
        "largest_layer_caps": layer_caps[:12],
        "rows": rows,
    }


@app.local_entrypoint()
def main() -> None:
    print("E1_N256_E42_HERMITE_MAJORANT " + repr(derive.remote()))
