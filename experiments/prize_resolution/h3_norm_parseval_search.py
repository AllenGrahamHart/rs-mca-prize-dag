#!/usr/bin/env python3
"""Find sharp odd-conjugate Parseval constants for product collisions."""

from __future__ import annotations

import collections
import itertools


def pair_vector(order: int, left: int, right: int) -> tuple[tuple[int, int], ...]:
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
    return tuple(sorted((key, value) for key, value in coefficients.items() if value))


def squared_distance(
    left: tuple[tuple[int, int], ...],
    right: tuple[tuple[int, int], ...],
) -> int:
    difference = collections.Counter(dict(left))
    difference.subtract(dict(right))
    return sum(value * value for value in difference.values())


def audit(
    order: int,
) -> tuple[
    int,
    tuple[tuple[int, int], tuple[int, int]],
    dict[int, int],
    dict[int, list[tuple[tuple[int, int], tuple[int, int]]]],
]:
    pairs = list(itertools.combinations_with_replacement(range(1, order), 2))
    vectors = [pair_vector(order, *pair) for pair in pairs]
    maximum = -1
    witness = None
    histogram: collections.Counter[int] = collections.Counter()
    top_witnesses: dict[int, list[tuple[tuple[int, int], tuple[int, int]]]] = {
        value: [] for value in (14, 16, 18, 20)
    }
    for first in range(len(pairs)):
        for second in range(first + 1, len(pairs)):
            value = squared_distance(vectors[first], vectors[second])
            histogram[value] += 1
            if value in top_witnesses and len(top_witnesses[value]) < 20:
                top_witnesses[value].append((pairs[first], pairs[second]))
            if value > maximum:
                maximum = value
                witness = (pairs[first], pairs[second])
    assert witness is not None
    return maximum, witness, dict(sorted(histogram.items())), top_witnesses


def main() -> None:
    for order in (4, 8, 16, 32, 64):
        maximum, witness, histogram, top_witnesses = audit(order)
        print(
            f"order={order} maximum={maximum} witness={witness} "
            f"top_histogram={list(histogram.items())[-6:]}"
        )
        if order == 64:
            for value, witnesses in top_witnesses.items():
                print(f"value={value} witnesses={witnesses}")
            pairs = list(itertools.combinations_with_replacement(range(1, order), 2))
            vectors = [pair_vector(order, *pair) for pair in pairs]
            half = order // 2

            def category(pair: tuple[int, int]) -> str:
                left, right = pair
                if left == right:
                    return "diagonal"
                if half in pair:
                    return "half_turn"
                if (left - right) % half == 0:
                    return "antipodal"
                if (left + right) % half == 0:
                    return "opposite_class"
                return "generic"

            edge_types: collections.Counter[tuple[str, str, int, int, int]] = (
                collections.Counter()
            )
            active: collections.Counter[str] = collections.Counter()
            for first in range(len(pairs)):
                left_norm = sum(value * value for _, value in vectors[first])
                for second in range(first + 1, len(pairs)):
                    distance = squared_distance(vectors[first], vectors[second])
                    if distance <= 10:
                        continue
                    right_norm = sum(value * value for _, value in vectors[second])
                    categories = tuple(sorted((category(pairs[first]), category(pairs[second]))))
                    edge_types[(*categories, left_norm, right_norm, distance)] += 1
                    active[category(pairs[first])] += 1
                    active[category(pairs[second])] += 1
            print(f"high_edge_active={dict(sorted(active.items()))}")
            for key, count in sorted(edge_types.items()):
                print(f"high_edge_type={key} count={count}")
    print("H3_NORM_PARSEVAL_SEARCH_PASS")


if __name__ == "__main__":
    main()
