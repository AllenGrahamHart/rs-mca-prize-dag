#!/usr/bin/env python3
"""Independent finite-field audit of the distance-four router."""

from __future__ import annotations

import collections
import itertools


def order_root(prime: int, order: int) -> int:
    for base in range(2, prime):
        root = pow(base, (prime - 1) // order, prime)
        if pow(root, order // 2, prime) == prime - 1:
            return root
    raise AssertionError("no root")


def vector(pair: tuple[int, int], order: int) -> dict[int, int]:
    half = order // 2
    out: dict[int, int] = {}
    for exponent, coefficient in (
        ((pair[0] + pair[1]) % order, 1),
        (pair[0], -1),
        (pair[1], -1),
    ):
        if exponent >= half:
            exponent -= half
            coefficient = -coefficient
        out[exponent] = out.get(exponent, 0) + coefficient
    return {key: value for key, value in out.items() if value}


def norm(value: dict[int, int]) -> int:
    return sum(coefficient * coefficient for coefficient in value.values())


def distance(left: dict[int, int], right: dict[int, int]) -> int:
    return sum((left.get(key, 0) - right.get(key, 0)) ** 2 for key in left.keys() | right.keys())


def cross_relation(left: tuple[int, int], right: tuple[int, int], powers: list[int], prime: int) -> bool:
    left_roots = [powers[left[0]], powers[left[1]]]
    right_roots = [powers[right[0]], powers[right[1]]]
    for matched, other in ((0, 1), (1, 0)):
        y = left_roots[matched]
        x = left_roots[other]
        if right_roots[0] * right_roots[1] % prime == -y % prime:
            for u in right_roots:
                if u * x * (1 - y) % prime == (u * u - y) % prime:
                    return True
    for matched, other in ((0, 1), (1, 0)):
        y = right_roots[matched]
        x = right_roots[other]
        if left_roots[0] * left_roots[1] % prime == -y % prime:
            for u in left_roots:
                if u * x * (1 - y) % prime == (u * u - y) % prime:
                    return True
    return False


def main() -> None:
    generic_edges = 0
    antipodal_edges = 0
    for order, prime in ((32, 641), (64, 3_329)):
        row_generic = 0
        row_antipodal = 0
        half = order // 2
        root = order_root(prime, order)
        powers = [pow(root, exponent, prime) for exponent in range(order)]
        pairs = [
            pair for pair in itertools.combinations_with_replacement(range(1, order), 2)
            if pair[0] != pair[1] and half not in pair
        ]
        vectors = {pair: vector(pair, order) for pair in pairs}
        fibers: dict[int, list[tuple[int, int]]] = collections.defaultdict(list)
        for pair in pairs:
            target = (1 - powers[pair[0]]) * (1 - powers[pair[1]]) % prime
            fibers[target].append(pair)
        for fiber in fibers.values():
            for left, right in itertools.combinations(fiber, 2):
                if distance(vectors[left], vectors[right]) != 4:
                    continue
                if norm(vectors[left]) == 1 or norm(vectors[right]) == 1:
                    antipodal = left if norm(vectors[left]) == 1 else right
                    other = right if antipodal == left else left
                    x = powers[antipodal[0]]
                    assert powers[antipodal[1]] == -x % prime
                    u, v = powers[other[0]], powers[other[1]]
                    assert x * x % prime == (u + v - u * v) % prime
                    antipodal_edges += 1
                    row_antipodal += 1
                    continue
                assert norm(vectors[left]) == norm(vectors[right]) == 3
                assert cross_relation(left, right, powers, prime)
                generic_edges += 1
                row_generic += 1
        assert row_generic + row_antipodal <= (3 * order * order + order) // 2
    assert generic_edges > 0
    print(
        "AUDIT_F3_H3_DISTANCE_FOUR_CROSS_OVERLAP_ROUTER_PASS "
        f"generic_edges={generic_edges} antipodal_edges={antipodal_edges} rows=2"
    )


if __name__ == "__main__":
    main()
