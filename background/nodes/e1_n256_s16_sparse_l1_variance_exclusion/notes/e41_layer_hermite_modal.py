#!/usr/bin/env python3
"""Derive the layered M3 cap and cubic candidates for V=82."""

from __future__ import annotations

import modal


app = modal.App("e1-n256-e41-layer-hermite")
image = modal.Image.debian_slim().pip_install("sympy")


@app.function(image=image, cpu=1.0, memory=256, timeout=60)
def derive() -> dict[str, object]:
    import itertools

    import sympy as sp

    def layer_cap(counts: tuple[int, ...]) -> int:
        sizes = [
            2 * sum(counts[level:])
            for level in range(len(counts))
            if sum(counts[level:])
        ]
        total = 0
        for first, second, third in itertools.product(sizes, repeat=3):
            total += min(
                first * second - min(first, second),
                first * third - min(first, third),
                second * third - min(second, third),
            )
        return total

    profiles = []
    for counts in itertools.product(
        range(42), range(11), range(5), range(3), range(2), range(2)
    ):
        l1_norm = sum((index + 1) * count for index, count in enumerate(counts))
        energy = sum(
            (index + 1) ** 2 * count for index, count in enumerate(counts)
        )
        if energy == 41 and l1_norm <= 23 and sum(counts) <= 21:
            profiles.append(
                {
                    "counts_n1_through_n6": counts,
                    "l1_norm": l1_norm,
                    "support_size": sum(counts),
                    "layer_cap": layer_cap(counts),
                }
            )
    profiles.sort(key=lambda row: row["layer_cap"], reverse=True)
    third_moment_cap = profiles[0]["layer_cap"]

    y = sp.symbols("y")
    log_a, log_b = sp.symbols("log_a log_b")
    coefficients = sp.symbols("c0:4")
    polynomial = sum(coefficients[index] * y**index for index in range(4))
    raw_second = 16**2 + 82
    raw_third = 16**3 + 3 * 16 * 82 + third_moment_cap
    target = sp.Rational(125, 32) * sp.log(2)
    candidates = []

    for left in range(12, 17):
        for right in range(50, 65):
            solution = sp.solve(
                (
                    sp.Eq(polynomial.subs(y, left), log_a),
                    sp.Eq(
                        sp.diff(polynomial, y).subs(y, left),
                        sp.Rational(1, left),
                    ),
                    sp.Eq(polynomial.subs(y, right), log_b),
                    sp.Eq(
                        sp.diff(polynomial, y).subs(y, right),
                        sp.Rational(1, right),
                    ),
                ),
                coefficients,
                rational=True,
            )
            expected = sp.expand(
                solution[coefficients[0]]
                + 16 * solution[coefficients[1]]
                + raw_second * solution[coefficients[2]]
                + raw_third * solution[coefficients[3]]
            )
            exact_expected = expected.subs(
                {log_a: sp.log(left), log_b: sp.log(right)}
            )
            leading = solution[coefficients[3]].subs(
                {log_a: sp.log(left), log_b: sp.log(right)}
            )
            candidates.append(
                {
                    "left": left,
                    "right": right,
                    "leading_positive": bool(leading > 0),
                    "leading_expression": str(solution[coefficients[3]]),
                    "expected_expression": str(expected),
                    "target_margin": str(sp.N(target - exact_expected, 60)),
                    "numeric_margin": float(target - exact_expected),
                    "coefficients": [str(solution[value]) for value in coefficients],
                }
            )
    candidates.sort(key=lambda row: row["numeric_margin"], reverse=True)

    return {
        "complete": True,
        "energy": 41,
        "variance": 82,
        "l1_ceiling": 23,
        "profile_count": len(profiles),
        "largest_layer_caps": profiles[:12],
        "third_moment_cap": third_moment_cap,
        "raw_second": raw_second,
        "raw_third_at_cap": raw_third,
        "best_candidates": candidates[:12],
    }


@app.local_entrypoint()
def main() -> None:
    print("E1_N256_E41_LAYER_HERMITE " + repr(derive.remote()))
