#!/usr/bin/env python3
"""Verify both DLI spectral-hypothesis separation counterexamples."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
from itertools import product


EXPECTED = {
    "one_a": 160,
    "one_b": 388,
    "one_joint": 20,
    "one_owner": 4,
    "one_ratio_num": 8192,
    "one_ratio_den": 485,
    "pure_marginals": [3856, 1296, 5124],
    "pure_joint": 20,
    "pure_owner": 4,
    "tensor2_num": 2251799813685248,
    "tensor2_den": 208440030324267,
}


def event(word: tuple[int, ...], frequencies: tuple[int, ...], zeta: int, q: int) -> bool:
    return all(
        sum(word[i] * pow(zeta, frequency * i, q) for i in range(len(word))) % q == 0
        for frequency in frequencies
    )


def build() -> dict[str, object]:
    n, q, zeta = 16, 17, 3
    one_sets = ((2, 3), (4, 6))
    pure_sets = ((1,), (2, 6), (4,))
    one_counts = [0, 0]
    pure_counts = [0, 0, 0]
    one_joint = one_owner = pure_joint = pure_owner = 0

    for word in product((0, 1), repeat=n):
        one = [event(word, row, zeta, q) for row in one_sets]
        pure = [event(word, row, zeta, q) for row in pure_sets]
        owner = all(word[i] == word[i + n // 2] for i in range(n // 2))
        for index, value in enumerate(one):
            one_counts[index] += value
        for index, value in enumerate(pure):
            pure_counts[index] += value
        if all(one):
            one_joint += 1
            one_owner += owner
        if all(pure):
            pure_joint += 1
            pure_owner += owner

    one_ratio = Fraction(
        (one_joint - one_owner) * (1 << n),
        one_counts[0] * one_counts[1],
    )
    constant = Fraction(
        pure_joint * (1 << (2 * n)),
        pure_counts[0] * pure_counts[1] * pure_counts[2],
    )
    tensor2 = constant**2 * (1 - Fraction(pure_owner, pure_joint) ** 2)
    result = {
        "one_a": one_counts[0],
        "one_b": one_counts[1],
        "one_joint": one_joint,
        "one_owner": one_owner,
        "one_ratio_num": one_ratio.numerator,
        "one_ratio_den": one_ratio.denominator,
        "pure_marginals": pure_counts,
        "pure_joint": pure_joint,
        "pure_owner": pure_owner,
        "tensor2_num": tensor2.numerator,
        "tensor2_den": tensor2.denominator,
    }
    assert result == EXPECTED
    assert one_ratio * one_ratio > 2 * n
    assert tensor2 * tensor2 > 2 * (2 * n)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["one_owner"] += 1
        caught = 0
        try:
            assert changed == result
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_SPECTRAL_HYPOTHESIS_NO_GO_TAMPER_PASS mutations=1/1")
        return
    print(
        "DLI_SPECTRAL_HYPOTHESIS_NO_GO_PASS "
        "one_sided=8192/485 valuation_tensor2=2251799813685248/208440030324267"
    )


if __name__ == "__main__":
    main()
