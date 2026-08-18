#!/usr/bin/env python3
"""Exact small-row replay of the fixed-weight ambient-Q bridge."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
from itertools import product
from math import comb


EXPECTED_F = [0, 0, 0, 0, 0, 16, 32, 32, 48, 32, 32, 16, 0, 0, 0, 0, 0]
EXPECTED_IMAGES = [1, 16, 120, 272, 289, 289, 289, 289, 289,
                   289, 289, 289, 289, 272, 120, 16, 1]


def build() -> dict[str, object]:
    n, t, q, zeta = 16, 2, 17, 3
    marginal_odd = 0
    marginal_terminal = 0
    joint = 0
    primitive = 0
    fibers = [0] * (n + 1)
    images = [set() for _ in range(n + 1)]

    for word in product((0, 1), repeat=n):
        syndrome = tuple(
            sum(word[i] * pow(zeta, r * i, q) for i in range(n)) % q
            for r in range(1, t + 1)
        )
        weight = sum(word)
        images[weight].add(syndrome)

        pair_sums = [word[i] + word[i + n // 2] for i in range(n // 2)]
        pair_diffs = [word[i] - word[i + n // 2] for i in range(n // 2)]
        odd = sum(pair_diffs[i] * pow(zeta, i, q) for i in range(n // 2)) % q == 0
        zeta_one = pow(zeta, 2, q)
        terminal = sum(
            pair_sums[i] * pow(zeta_one, i, q) for i in range(n // 2)
        ) % q == 0
        assert (syndrome == (0, 0)) == (odd and terminal)

        marginal_odd += odd
        marginal_terminal += terminal
        if syndrome == (0, 0):
            joint += 1
            owner = all(word[i] == word[i + n // 2] for i in range(n // 2))
            if not owner:
                primitive += 1
                fibers[weight] += 1

    image_sizes = [len(image) for image in images]
    assert fibers == EXPECTED_F
    assert image_sizes == EXPECTED_IMAGES
    assert marginal_odd == marginal_terminal == 3856
    assert joint == 224 and primitive == 208
    assert fibers == fibers[::-1]
    assert image_sizes == image_sizes[::-1]
    assert sum(fibers[: t + 1]) == sum(fibers[n - t :]) == 0

    total = 1 << n
    assert marginal_odd * q >= total
    assert marginal_terminal * q >= total
    denominator = Fraction(marginal_odd, total) * Fraction(marginal_terminal, total)
    correlation = Fraction(primitive, total) / denominator
    ambient_average = Fraction(q**t * primitive, total)
    assert correlation == Fraction(53248, 58081)
    assert ambient_average == Fraction(3757, 4096)
    assert correlation < ambient_average

    dictionary = Fraction(0)
    for weight, fiber in enumerate(fibers):
        mass = Fraction(comb(n, weight), total)
        image = image_sizes[weight]
        kappa_img = Fraction(fiber * image, comb(n, weight))
        image_defect = Fraction(q**t, image)
        dictionary += mass * image_defect * kappa_img
    assert dictionary == ambient_average

    return {
        "marginals": [marginal_odd, marginal_terminal],
        "joint": joint,
        "primitive": primitive,
        "fibers": fibers,
        "images": image_sizes,
        "correlation": [correlation.numerator, correlation.denominator],
        "ambient_average": [ambient_average.numerator, ambient_average.denominator],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["marginals"][0] -= 1
        caught = 0
        try:
            assert changed["marginals"][0] * 17 >= 1 << 16
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_FIXED_WEIGHT_AMBIENT_Q_TAMPER_PASS mutations=1/1")
        return
    print(
        "DLI_FIXED_WEIGHT_AMBIENT_Q_PASS "
        "row=(16,2,17) J=53248/58081 Kamb=3757/4096"
    )


if __name__ == "__main__":
    main()
