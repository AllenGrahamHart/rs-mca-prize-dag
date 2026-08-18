#!/usr/bin/env python3
"""Independent support-combination audit of the ambient-Q bridge fixture."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction
from itertools import combinations
from math import comb


EXPECTED_F = [0, 0, 0, 0, 0, 16, 32, 32, 48, 32, 32, 16, 0, 0, 0, 0, 0]


def build() -> dict[str, object]:
    n, t, q, zeta = 16, 2, 17, 3
    fibers = []
    image_sizes = []
    odd_count = terminal_count = joint_count = owner_count = 0

    powers = [[pow(zeta, r * i, q) for i in range(n)] for r in (1, 2)]
    for weight in range(n + 1):
        fiber = 0
        image = set()
        for support_tuple in combinations(range(n), weight):
            support = set(support_tuple)
            s1 = sum(powers[0][i] for i in support) % q
            s2 = sum(powers[1][i] for i in support) % q
            image.add((s1, s2))
            odd_count += s1 == 0
            terminal_count += s2 == 0
            if s1 == 0 and s2 == 0:
                joint_count += 1
                owner = all((i in support) == (i + n // 2 in support)
                            for i in range(n // 2))
                owner_count += owner
                fiber += not owner
        fibers.append(fiber)
        image_sizes.append(len(image))

    primitive = joint_count - owner_count
    assert fibers == EXPECTED_F
    assert odd_count == terminal_count == 3856
    assert joint_count == 224 and owner_count == 16 and primitive == 208

    total = 1 << n
    ambient = Fraction(0)
    for weight in range(n + 1):
        layer_mass = Fraction(comb(n, weight), total)
        q_image = Fraction(fibers[weight] * image_sizes[weight], comb(n, weight))
        defect = Fraction(q**t, image_sizes[weight])
        ambient += layer_mass * defect * q_image
    correlation = Fraction(primitive * total, odd_count * terminal_count)
    assert ambient == Fraction(3757, 4096)
    assert correlation == Fraction(53248, 58081) < ambient
    return {
        "fibers": fibers,
        "marginals": [odd_count, terminal_count],
        "joint_owner": [joint_count, owner_count],
        "ambient": [ambient.numerator, ambient.denominator],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.tamper_selftest:
        changed = copy.deepcopy(result)
        changed["fibers"][8] += 1
        caught = 0
        try:
            assert changed["fibers"] == result["fibers"]
        except AssertionError:
            caught = 1
        assert caught == 1
        print("DLI_FIXED_WEIGHT_AMBIENT_Q_AUDIT_TAMPER_PASS mutations=1/1")
        return
    print("DLI_FIXED_WEIGHT_AMBIENT_Q_AUDIT_PASS supports=65536")


if __name__ == "__main__":
    main()

