#!/usr/bin/env python3
"""Audit interpolation defects on all ten exact m=1 pair matrices."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PROBE = ROOT / "experiments/prize_resolution/rh_bivariate_m1_rank_probe.py"


def load_probe():
    spec = importlib.util.spec_from_file_location("m1_probe_for_defects", PROBE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def lagrange(points, pivot, value, prime):
    numerator = 1
    denominator = 1
    for point in points:
        if point == pivot:
            continue
        numerator = numerator * (value - point) % prime
        denominator = denominator * (pivot - point) % prime
    return numerator * pow(denominator, prime - 2, prime) % prime


def main() -> None:
    probe = load_probe()
    representatives = {}
    for slope, support in probe.SUPPORTS.items():
        target = tuple(
            (a + slope * b) % probe.PRIME for a, b in zip(probe.Y0, probe.Y1)
        )
        representatives[slope] = probe.solve_support(support, target)

    checks = 0
    slopes = tuple(probe.SUPPORTS)
    for first_index, first in enumerate(slopes):
        for second in slopes[first_index + 1 :]:
            matrix, _, support = probe.pair_matrix(first, second, representatives)
            pivots = list(support[:5])
            value = support[5]
            for parameter_degree in range(2):
                top = {
                    x: matrix[2][column] for column, x in enumerate(support)
                }
                coefficients = {
                    x: matrix[parameter_degree][column] * pow(top[x], 15, 17) % 17
                    for column, x in enumerate(support)
                }
                for moment in range(5):
                    defect = (
                        pow(value, moment, 17) * coefficients[value]
                        - sum(
                            lagrange(pivots, pivot, value, 17)
                            * pow(pivot, moment, 17)
                            * coefficients[pivot]
                            for pivot in pivots
                        )
                    ) % 17
                    assert defect == 0
                    checks += 1

    print(
        "RATE_HALF_BIVARIATE_SCHUR_INTERPOLATION_DEFECT_FORMULA_AUDIT_PASS "
        f"zero_defects={checks}"
    )


if __name__ == "__main__":
    main()
