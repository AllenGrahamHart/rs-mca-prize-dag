#!/usr/bin/env python3
"""Exhaust the distance-six signed-support taxonomy on two exact rows."""

from __future__ import annotations

import collections
import itertools


def order_root(prime: int, order: int) -> int:
    for base in range(2, prime):
        root = pow(base, (prime - 1) // order, prime)
        if pow(root, order // 2, prime) == prime - 1:
            return root
    raise AssertionError((prime, order))


def vector(pair: tuple[int, int], order: int) -> dict[int, int]:
    half = order // 2
    out: collections.Counter[int] = collections.Counter()
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


def norm(value: dict[int, int]) -> int:
    return sum(coefficient * coefficient for coefficient in value.values())


def distance(left: dict[int, int], right: dict[int, int]) -> int:
    return sum(
        (left.get(key, 0) - right.get(key, 0)) ** 2
        for key in left.keys() | right.keys()
    )


def generic_type(
    left: tuple[int, int],
    right: tuple[int, int],
    powers: list[int],
    prime: int,
) -> set[str]:
    matches = set()
    for first, second in ((left, right), (right, left)):
        for x_exp, y_exp in itertools.permutations(first):
            for u_exp, v_exp in itertools.permutations(second):
                x, y = powers[x_exp], powers[y_exp]
                u, v = powers[u_exp], powers[v_exp]
                if u * v % prime != -x % prime:
                    continue
                if y == -u % prime:
                    expected_x = 2 * u * u * pow(1 + u * u, -1, prime) % prime
                    expected_v = -2 * u * pow(1 + u * u, -1, prime) % prime
                    assert (x, v) == (expected_x, expected_v)
                    matches.add("root-antipodal")
                if x * y % prime == u:
                    expected_x = (1 + y * y) * pow(2 * y * y, -1, prime) % prime
                    assert x == expected_x and v == -pow(y, -1, prime) % prime
                    matches.add("cross-chain")
    return matches


def antipodal_type(
    antipodal: tuple[int, int],
    generic: tuple[int, int],
    powers: list[int],
    prime: int,
) -> set[str]:
    square = powers[antipodal[0]] ** 2 % prime
    u, v = powers[generic[0]], powers[generic[1]]
    matches = set()
    if u * v % prime == square:
        assert (u + v) % prime == 2 * square % prime
        matches.add("product")
    for root, other in ((u, v), (v, u)):
        if root == -square % prime:
            assert other * (1 + square) % prime == 2 * square % prime
            matches.add("root")
    return matches


def main() -> None:
    totals = collections.Counter()
    maximum_generic_overlap = 0
    maximum_antipodal_degree = 0

    for order, prime in ((32, 97), (64, 193)):
        root = order_root(prime, order)
        powers = [pow(root, exponent, prime) for exponent in range(order)]
        pairs = list(itertools.combinations_with_replacement(range(1, order), 2))
        vectors = {pair: vector(pair, order) for pair in pairs}
        small = [pair for pair in pairs if norm(vectors[pair]) <= 3]
        fibers: dict[int, list[tuple[int, int]]] = collections.defaultdict(list)
        for pair in small:
            target = (1 - powers[pair[0]]) * (1 - powers[pair[1]]) % prime
            fibers[target].append(pair)

        for fiber in fibers.values():
            generic_overlap = 0
            antipodal_degree = 0
            for left, right in itertools.combinations(fiber, 2):
                if distance(vectors[left], vectors[right]) != 6:
                    continue
                left_norm, right_norm = norm(vectors[left]), norm(vectors[right])
                common = set(vectors[left]) & set(vectors[right])
                if left_norm == right_norm == 3:
                    if not common:
                        totals["generic-disjoint"] += 1
                        continue
                    products = sorted(vectors[left][key] * vectors[right][key] for key in common)
                    assert len(common) == 2 and products == [-1, 1]
                    matches = generic_type(left, right, powers, prime)
                    assert len(matches) == 1
                    totals[next(iter(matches))] += 1
                    generic_overlap += 1
                else:
                    assert sorted((left_norm, right_norm)) == [1, 3]
                    assert len(common) == 1
                    key = next(iter(common))
                    assert vectors[left][key] * vectors[right][key] == -1
                    antipodal = left if left_norm == 1 else right
                    generic = right if left_norm == 1 else left
                    matches = antipodal_type(antipodal, generic, powers, prime)
                    assert len(matches) == 1
                    totals[f"antipodal-{next(iter(matches))}"] += 1
                    antipodal_degree += 1

            assert generic_overlap <= 6
            assert antipodal_degree <= 2
            maximum_generic_overlap = max(maximum_generic_overlap, generic_overlap)
            maximum_antipodal_degree = max(maximum_antipodal_degree, antipodal_degree)

    assert totals["root-antipodal"] and totals["cross-chain"]
    assert totals["antipodal-product"] and totals["antipodal-root"]
    print(
        "AUDIT_F3_H3_DISTANCE_SIX_SUPPORT_OVERLAP_PAYMENT_PASS "
        f"edges={sum(totals.values())} classes={dict(totals)} "
        f"fiber_max={maximum_generic_overlap}+{maximum_antipodal_degree}"
    )


if __name__ == "__main__":
    main()
