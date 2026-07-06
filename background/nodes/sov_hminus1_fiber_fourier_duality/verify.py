#!/usr/bin/env python3
"""Replay finite Fourier fiber inversion on a tiny prime-field sample."""

from __future__ import annotations

import cmath
import math
from collections import Counter


def character(q: int, x: int) -> complex:
    return cmath.exp(2j * math.pi * (x % q) / q)


def main() -> None:
    q = 7
    values = [(i * i + 3 * i + 1) % q for i in range(31)]
    counts = Counter(values)

    sums = {
        xi: sum(character(q, xi * value) for value in values)
        for xi in range(q)
    }

    for a in range(q):
        reconstructed = sum(
            character(q, -xi * a) * sums[xi]
            for xi in range(q)
        ) / q
        assert abs(reconstructed.imag) < 1e-9
        assert round(reconstructed.real) == counts[a]

    fourier_bound = len(values) / q + sum(abs(sums[xi]) for xi in range(1, q)) / q
    assert max(counts.values()) <= fourier_bound + 1e-9

    print(
        "sov h-1 Fourier fiber-duality check passed:",
        {"max_fiber": max(counts.values()), "bound": round(fourier_bound, 6)},
    )


if __name__ == "__main__":
    main()
