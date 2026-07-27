#!/usr/bin/env python3
"""Falsify low-variance-implies-proper-conductor in a bounded toy quotient."""

from __future__ import annotations

import json
import math
import time
from collections import Counter
from itertools import combinations, product


HALF = 8
DEADLINE_SECONDS = 52.0


def variance(coefficients: tuple[int, ...]) -> int:
    half = len(coefficients)
    autocorrelation = [0] * half
    support = [index for index, value in enumerate(coefficients) if value]
    for left in support:
        for right in support:
            quotient, residue = divmod(left - right, half)
            autocorrelation[residue] += (
                -1 if quotient % 2 else 1
            ) * coefficients[left] * coefficients[right]
    autocorrelation[0] -= 16
    return sum(value * value for value in autocorrelation)


def main() -> None:
    started = time.monotonic()
    histogram = Counter()
    examples: dict[int, tuple[int, ...]] = {}
    completed = 0
    for support in combinations(range(HALF), 7):
        for heavy in combinations(support, 3):
            magnitudes = [0] * HALF
            for index in support:
                magnitudes[index] = 2 if index in heavy else 1
            tail = support[1:]
            for tail_signs in product((-1, 1), repeat=6):
                if time.monotonic() - started > DEADLINE_SECONDS:
                    print(
                        "E1_N256_S16_CONDUCTOR_FALSIFIER "
                        + json.dumps(
                            {"complete": False, "completed": completed},
                            sort_keys=True,
                        )
                    )
                    return
                signs = {support[0]: 1, **dict(zip(tail, tail_signs))}
                coefficients = tuple(
                    magnitudes[index] * signs.get(index, 0)
                    for index in range(HALF)
                )
                value = variance(coefficients)
                histogram[value] += 1
                examples.setdefault(value, coefficients)
                completed += 1

    candidates = []
    for toy_coefficients in examples.values():
        embedded = [0] * 128
        for index, value in enumerate(toy_coefficients):
            if value:
                embedded[16 * index] = value
        support = [index for index, value in enumerate(embedded) if value]
        for source in support:
            for step in (-1, 1):
                target = source + step
                if not 0 <= target < 128 or embedded[target]:
                    continue
                perturbed = embedded.copy()
                perturbed[target] = perturbed[source]
                perturbed[source] = 0
                new_support = [
                    index for index, value in enumerate(perturbed) if value
                ]
                conductor_gcd = math.gcd(
                    256, *(index - new_support[0] for index in new_support)
                )
                if conductor_gcd == 1:
                    candidates.append(
                        (variance(tuple(perturbed)), tuple(perturbed))
                    )

    best_variance, best_vector = min(candidates)
    payload = {
        "complete": True,
        "completed": completed,
        "toy_minimum": min(histogram),
        "toy_low_variances": [
            value for value in sorted(histogram) if 0 < value <= 134
        ],
        "best_full_conductor_variance": best_variance,
        "best_full_conductor_nonzero": [
            [index, value]
            for index, value in enumerate(best_vector)
            if value
        ],
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }
    print(
        "E1_N256_S16_CONDUCTOR_FALSIFIER "
        + json.dumps(payload, sort_keys=True)
    )


if __name__ == "__main__":
    main()
