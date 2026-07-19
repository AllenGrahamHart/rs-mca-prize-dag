#!/usr/bin/env python3
"""Audit the weighted-degree conclusion on complete small finite rows."""

from __future__ import annotations

import collections
import itertools


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


def main() -> None:
    checked = 0
    witnessed = 0
    for order, prime in ((32, 97), (64, 193)):
        root = order_root(prime, order)
        powers = [pow(root, exponent, prime) for exponent in range(order)]
        pairs = list(itertools.combinations_with_replacement(range(1, order), 2))
        vectors = {pair: vector(pair, order) for pair in pairs}
        pairs = [
            pair for pair in pairs
            if sum(value * value for value in vectors[pair].values()) <= 3
        ]
        fibers: dict[int, list[tuple[int, int]]] = collections.defaultdict(list)
        for pair in pairs:
            target = (1 - powers[pair[0]]) * (1 - powers[pair[1]]) % prime
            fibers[target].append(pair)
        for fiber in fibers.values():
            if len(fiber) < 7:
                continue
            for selected in itertools.combinations(fiber, 7):
                checked += 1
                scores = []
                for center in selected:
                    score = 0
                    for leaf in selected:
                        if leaf == center:
                            continue
                        square = distance(vectors[center], vectors[leaf])
                        score += 2 if square == 4 else 1 if square == 6 else 0
                    scores.append(score)
                assert max(scores) >= 4
                witnessed += max(scores) >= 4
    assert checked > 0
    assert witnessed == checked
    print(
        "AUDIT_F3_H3_WEIGHTED_MULTISTAR_ROUTER_PASS "
        f"seven_subsets={checked} witnessed={witnessed}"
    )


if __name__ == "__main__":
    main()
