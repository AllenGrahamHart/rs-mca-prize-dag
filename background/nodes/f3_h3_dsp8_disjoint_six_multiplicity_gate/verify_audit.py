#!/usr/bin/env python3
"""Audit the disjoint-distance-six gate on complete small product fibers."""

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


def antipodal(pair: tuple[int, int], order: int) -> bool:
    return (pair[0] - pair[1]) % order == order // 2


def d0(m: int) -> int:
    return math.ceil(m * (m - 4) / 2) - 2 * m - 6


def da(m: int) -> int:
    return math.ceil(m * (m - 2) / 2) - 4 * (m - 1) - 8


def main() -> None:
    checked = 0
    minimum = {False: None, True: None}
    for order, prime in ((32, 97), (64, 193)):
        root = order_root(prime, order)
        powers = [pow(root, exponent, prime) for exponent in range(order)]
        pairs = list(itertools.combinations_with_replacement(range(1, order), 2))
        vectors = {pair: vector(pair, order) for pair in pairs}
        fibers: dict[int, list[tuple[int, int]]] = collections.defaultdict(list)
        for pair in pairs:
            target = (1 - powers[pair[0]]) * (1 - powers[pair[1]]) % prime
            fibers[target].append(pair)

        for target, fiber in fibers.items():
            diagonal = sum(left == right for left, right in fiber)
            product_count = 2 * len(fiber) - diagonal
            if target in (0, 1) or product_count < 25:
                continue
            small = [
                pair for pair in fiber
                if sum(value * value for value in vectors[pair].values()) <= 3
            ]
            has_antipodal = any(antipodal(pair, order) for pair in small)
            disjoint_edges = 0
            degrees = collections.Counter()
            generic = [pair for pair in small if not antipodal(pair, order)]
            for left, right in itertools.combinations(generic, 2):
                if distance(vectors[left], vectors[right]) != 6:
                    continue
                if vectors[left].keys().isdisjoint(vectors[right].keys()):
                    disjoint_edges += 1
                    degrees[left] += 1
                    degrees[right] += 1
            bound = da(len(small)) if has_antipodal else d0(len(small))
            assert disjoint_edges >= bound
            if product_count >= 33:
                threshold = 5 if has_antipodal else 7
                assert max(degrees.values(), default=0) >= threshold
            prior = minimum[has_antipodal]
            minimum[has_antipodal] = (
                disjoint_edges if prior is None else min(prior, disjoint_edges)
            )
            checked += 1

    assert checked > 0
    print(
        "AUDIT_F3_H3_DSP8_DISJOINT_SIX_MULTIPLICITY_GATE_PASS "
        f"fibers={checked} minima={minimum}"
    )


if __name__ == "__main__":
    main()
