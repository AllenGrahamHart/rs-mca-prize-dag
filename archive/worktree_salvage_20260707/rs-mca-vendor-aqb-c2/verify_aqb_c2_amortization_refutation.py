#!/usr/bin/env python3
"""Replay the AQB c=2 amortization route-cut arithmetic."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


SIGMA_STAR = 8_592_912_738
D_EXTRA = 4_296_456_369
TARGET_GAIN_BITS = 429_645_547
FIBER_COORDINATES = 1 << 40

REPO = Path(__file__).resolve().parents[2]
ARTIFACT = (
    REPO
    / "experimental"
    / "data"
    / "certificates"
    / "aqb-c2-amortization-refutation"
    / "aqb_c2_amortization_refutation.json"
)


def weighted_average(weights: list[Fraction], values: list[int]) -> Fraction:
    assert len(weights) == len(values)
    assert sum(weights, Fraction(0, 1)) == 1
    return sum(w * v for w, v in zip(weights, values))


def check_convex_instance(weights: list[Fraction], values: list[int]) -> dict[str, object]:
    avg = weighted_average(weights, values)
    maximum = max(values)
    assert avg <= maximum
    return {
        "weights": [f"{w.numerator}/{w.denominator}" for w in weights],
        "fiber_counts": values,
        "average": f"{avg.numerator}/{avg.denominator}",
        "max_fiber": maximum,
        "average_le_max": True,
    }


def verify() -> dict[str, object]:
    assert SIGMA_STAR == 2 * D_EXTRA

    uniform_values = [3, 7, 11, 19]
    uniform_weights = [Fraction(1, len(uniform_values)) for _ in uniform_values]
    uniform_avg = weighted_average(uniform_weights, uniform_values)
    assert uniform_avg == Fraction(sum(uniform_values), len(uniform_values))

    examples = [
        check_convex_instance([Fraction(1, 2), Fraction(1, 2)], [10, 14]),
        check_convex_instance([Fraction(1, 5), Fraction(3, 5), Fraction(1, 5)], [4, 9, 20]),
        check_convex_instance(uniform_weights, uniform_values),
    ]

    per_fiber = Fraction(TARGET_GAIN_BITS, FIBER_COORDINATES)
    per_extra = Fraction(TARGET_GAIN_BITS, D_EXTRA)
    assert float(per_fiber) < 0.000391
    assert Fraction(99, 1000) < per_extra < Fraction(101, 1000)

    return {
        "schema": "aqb-c2-amortization-refutation-v1",
        "status": "COUNTEREXAMPLE_ROUTE_CUT",
        "sigma_star": SIGMA_STAR,
        "d_extra": D_EXTRA,
        "target_gain_bits": TARGET_GAIN_BITS,
        "sigma_star_equals_2d": True,
        "per_2_40_fiber_coordinate_bits": f"{per_fiber.numerator}/{per_fiber.denominator}",
        "per_extra_fiber_bits": f"{per_extra.numerator}/{per_extra.denominator}",
        "convex_combination_examples": examples,
        "conclusion": (
            "An averaged c=2 box family is a convex combination of single-box "
            "fiber counts; box-charge sharing alone cannot beat the plain floor."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true")
    args = parser.parse_args()

    cert = verify()
    if args.emit:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
        print(f"wrote {ARTIFACT.relative_to(REPO)}")
    print("PASS: AQB c=2 amortization refutation")


if __name__ == "__main__":
    main()
