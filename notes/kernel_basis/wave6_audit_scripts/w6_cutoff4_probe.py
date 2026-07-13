#!/usr/bin/env python3
"""Probe whether low-norm shifted-pair geometry alone forces cutoff four."""

from __future__ import annotations

import collections
import itertools


def pair_vector(order: int, left: int, right: int) -> dict[int, int]:
    half = order // 2
    coefficients: collections.Counter[int] = collections.Counter()
    for exponent, coefficient in (
        ((left + right) % order, 1),
        (left, -1),
        (right, -1),
    ):
        if exponent >= half:
            exponent -= half
            coefficient = -coefficient
        coefficients[exponent] += coefficient
    return {key: value for key, value in coefficients.items() if value}


def norm_squared(vector: dict[int, int]) -> int:
    return sum(value * value for value in vector.values())


def squared_distance(left: dict[int, int], right: dict[int, int]) -> int:
    return sum(
        (left.get(key, 0) - right.get(key, 0)) ** 2
        for key in left.keys() | right.keys()
    )


def find_clique(adjacency: list[int], target: int) -> list[int] | None:
    chosen: list[int] = []

    def search(candidates: int) -> bool:
        if len(chosen) == target:
            return True
        if candidates.bit_count() < target - len(chosen):
            return False

        while candidates:
            if candidates.bit_count() < target - len(chosen):
                return False
            bit = candidates & -candidates
            vertex = bit.bit_length() - 1
            candidates ^= bit
            chosen.append(vertex)
            if search(candidates & adjacency[vertex]):
                return True
            chosen.pop()
        return False

    universe = (1 << len(adjacency)) - 1
    return chosen.copy() if search(universe) else None


def audit(
    order: int, require_disjoint_pairs: bool
) -> tuple[int, list[tuple[int, int]], list[int]]:
    rows = []
    for pair in itertools.combinations_with_replacement(range(1, order), 2):
        vector = pair_vector(order, *pair)
        if norm_squared(vector) <= 3:
            rows.append((pair, vector))

    adjacency = [0] * len(rows)
    for left in range(len(rows)):
        for right in range(left + 1, len(rows)):
            pair_left = set(rows[left][0])
            pair_right = set(rows[right][0])
            disjoint = pair_left.isdisjoint(pair_right)
            if (
                squared_distance(rows[left][1], rows[right][1]) > 4
                and (disjoint or not require_disjoint_pairs)
            ):
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left

    witness_indices = find_clique(adjacency, 7)
    witness_pairs = [rows[index][0] for index in witness_indices or []]
    witness_norms = [norm_squared(rows[index][1]) for index in witness_indices or []]
    if witness_indices:
        for left, right in itertools.combinations(witness_indices, 2):
            assert squared_distance(rows[left][1], rows[right][1]) >= 6
    return len(rows), witness_pairs, witness_norms


def main() -> None:
    for order in (16, 32, 64):
        for require_disjoint_pairs in (False, True):
            vertex_count, witness_pairs, witness_norms = audit(
                order, require_disjoint_pairs
            )
            print(
                f"order={order} low_vertices={vertex_count} "
                f"matching={require_disjoint_pairs} "
                f"cutoff4_k7_exists={bool(witness_pairs)} "
                f"pairs={witness_pairs} norms={witness_norms}"
            )
    print("H3_PARSEVAL_CUTOFF4_PROBE_PASS")


if __name__ == "__main__":
    main()
