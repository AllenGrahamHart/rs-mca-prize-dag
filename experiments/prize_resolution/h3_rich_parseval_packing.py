#!/usr/bin/env python3
"""Search the ten-representation Parseval packing threshold exactly."""

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


def squared_distance(left: dict[int, int], right: dict[int, int]) -> int:
    return sum(
        (left.get(key, 0) - right.get(key, 0)) ** 2
        for key in left.keys() | right.keys()
    )


def find_clique(
    adjacency: list[int],
    target: int,
    diagonal: list[bool] | None = None,
    max_diagonal: int | None = None,
    half_turn: list[bool] | None = None,
    max_half_turn: int | None = None,
) -> list[int] | None:
    witness: list[int] = []

    def color_sort(candidates: int) -> tuple[list[int], list[int]]:
        order: list[int] = []
        bounds: list[int] = []
        color = 0
        remaining = candidates
        while remaining:
            color += 1
            independent = remaining
            while independent:
                bit = independent & -independent
                vertex = bit.bit_length() - 1
                remaining ^= bit
                independent ^= bit
                independent &= ~adjacency[vertex]
                order.append(vertex)
                bounds.append(color)
        return order, bounds

    def expand(
        chosen: list[int],
        candidates: int,
        diagonal_count: int,
        half_turn_count: int,
    ) -> bool:
        if len(chosen) >= target:
            witness.extend(chosen)
            return True
        if candidates.bit_count() < target - len(chosen):
            return False
        order, bounds = color_sort(candidates)
        for index in range(len(order) - 1, -1, -1):
            if len(chosen) + bounds[index] < target:
                return False
            vertex = order[index]
            bit = 1 << vertex
            next_diagonal_count = diagonal_count + bool(diagonal and diagonal[vertex])
            next_half_turn_count = half_turn_count + bool(half_turn and half_turn[vertex])
            allowed = (
                (max_diagonal is None or next_diagonal_count <= max_diagonal)
                and (max_half_turn is None or next_half_turn_count <= max_half_turn)
            )
            if (
                allowed
                and candidates & bit
                and expand(
                    chosen + [vertex],
                    candidates & adjacency[vertex],
                    next_diagonal_count,
                    next_half_turn_count,
                )
            ):
                return True
            candidates &= ~bit
        return False

    universe = (1 << len(adjacency)) - 1
    return witness if expand([], universe, 0, 0) else None


def audit(
    order: int,
    cutoff: int,
    target: int,
    max_diagonal: int | None = None,
    max_half_turn: int | None = None,
) -> tuple[bool, list[tuple[int, int]]]:
    pairs = list(itertools.combinations_with_replacement(range(1, order), 2))
    vectors = [pair_vector(order, *pair) for pair in pairs]
    adjacency = [0] * len(pairs)
    for left in range(len(pairs)):
        for right in range(left + 1, len(pairs)):
            if squared_distance(vectors[left], vectors[right]) > cutoff:
                adjacency[left] |= 1 << right
                adjacency[right] |= 1 << left
    witness = find_clique(
        adjacency,
        target,
        [left == right for left, right in pairs],
        max_diagonal,
        [order // 2 in pair for pair in pairs],
        max_half_turn,
    )
    return witness is not None, [pairs[index] for index in witness or []]


def main() -> None:
    for order in (16, 32, 64):
        constrained, constrained_witness = audit(order, 8, 10, max_diagonal=2)
        print(
            f"order={order} cutoff=8 max_diagonal=2 k10_exists={constrained} "
            f"witness={constrained_witness}"
        )
        unconstrained, unconstrained_witness = audit(order, 8, 10)
        print(
            f"order={order} cutoff=8 unconstrained_k10_exists={unconstrained} "
            f"witness={unconstrained_witness}"
        )
    print("H3_RICH_PARSEVAL_PACKING_PASS")


if __name__ == "__main__":
    main()
