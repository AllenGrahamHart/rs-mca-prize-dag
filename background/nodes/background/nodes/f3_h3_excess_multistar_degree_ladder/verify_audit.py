#!/usr/bin/env python3
"""Audit the excess ladder on complete small product fibers."""

from __future__ import annotations

import collections
import itertools
import math


def order_root(prime: int, order: int) -> int:
    exponent = (prime - 1) // order
    for base in range(2, prime):
        root = pow(base, exponent, prime)
        if pow(root, order // 2, prime) == prime - 1:
            return root
    raise AssertionError((prime, order))


def vector(pair: tuple[int, int], order: int) -> dict[int, int]:
    out: collections.Counter[int] = collections.Counter()
    half = order // 2
    for exponent, coefficient in (
        ((pair[0] + pair[1]) % order, 1),
        (pair[0], -1),
        (pair[1], -1),
    ):
        if exponent >= half:
            exponent -= half
            coefficient = -coefficient
        out[exponent] += coefficient
    return {key: value for key, value in out.items() if value}


def distance(left: dict[int, int], right: dict[int, int]) -> int:
    return sum(
        (left.get(key, 0) - right.get(key, 0)) ** 2
        for key in left.keys() | right.keys()
    )


def ladder(m: int) -> int:
    return math.ceil(2 * math.ceil(m * (m - 4) / 2) / m)


def main() -> None:
    checked = 0
    for order, prime in ((32, 97), (64, 193)):
        root = order_root(prime, order)
        powers = [pow(root, exponent, prime) for exponent in range(order)]
        pairs = list(itertools.combinations_with_replacement(range(1, order), 2))
        vectors = {pair: vector(pair, order) for pair in pairs}
        fibers: dict[int, list[tuple[int, int]]] = collections.defaultdict(list)
        for pair in pairs:
            target = (1 - powers[pair[0]]) * (1 - powers[pair[1]]) % prime
            fibers[target].append(pair)
        for fiber in fibers.values():
            small = [
                pair for pair in fiber
                if sum(value * value for value in vectors[pair].values()) <= 3
            ]
            if len(small) < 5:
                continue
            maximum = 0
            for center in small:
                score = 0
                for leaf in small:
                    if leaf == center:
                        continue
                    square = distance(vectors[center], vectors[leaf])
                    score += 2 if square == 4 else 1 if square == 6 else 0
                maximum = max(maximum, score)
            assert maximum >= ladder(len(small))
            checked += 1
    assert checked > 0
    print(f"AUDIT_F3_H3_EXCESS_MULTISTAR_DEGREE_LADDER_PASS fibers={checked}")


if __name__ == "__main__":
    main()
