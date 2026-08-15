#!/usr/bin/env python3
"""Independent ratio-turn audit of the integer-gap envelope."""

from __future__ import annotations

import json
from fractions import Fraction
from math import prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def product(low: int, high: int) -> int:
    return prod(range(low, high + 1))


def value(r: int, w: int, dimension: int, t: int) -> Fraction:
    numerator = product(r + t, r + dimension + t)
    denominator = (w + dimension + t) * product(w + 1, w + dimension - 1)
    return Fraction(numerator, denominator)


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    r, w = p["R"], p["w"]
    maximum_t = p["official_K_prime_maximum"] - p["correction_dimension"]
    checks = 0
    for dimension in range(2, 10):
        turn = (r - (dimension + 1) * (w + dimension)) // dimension
        points = sorted({
            1,
            2,
            max(1, turn),
            max(1, turn + 1),
            maximum_t - 1,
            maximum_t,
        })
        endpoint_max = max(value(r, w, dimension, 1), value(r, w, dimension, maximum_t))
        for t in points:
            require(value(r, w, dimension, t) <= endpoint_max, "sampled endpoint envelope")
            checks += 1
        for t in (1, max(1, turn), max(1, turn + 1), maximum_t - 1):
            ratio_sign = dimension * t + (dimension + 1) * (w + dimension) - r
            comparison = value(r, w, dimension, t + 1) - value(r, w, dimension, t)
            require((comparison > 0) == (ratio_sign > 0), "ratio sign")
            require((comparison == 0) == (ratio_sign == 0), "ratio zero")
            checks += 1
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_PROJECTIVE_PAVING_INTEGER_GAP_FENCE_AUDIT_PASS "
        f"dimensions=8 checks={checks}"
    )


if __name__ == "__main__":
    main()
