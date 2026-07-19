#!/usr/bin/env python3
"""Replay the primitive-matching truncation and production caps."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import factorial


def independence_polynomial(
    supports: tuple[frozenset[int], ...], activities: tuple[Fraction, ...]
) -> Fraction:
    total = Fraction(0)
    for size in range(len(supports) + 1):
        for indices in combinations(range(len(supports)), size):
            occupied: set[int] = set()
            weight = Fraction(1)
            for index in indices:
                if occupied.intersection(supports[index]):
                    break
                occupied.update(supports[index])
                weight *= activities[index]
            else:
                total += weight
    return total


def truncated_exp(value: Fraction, cap: int) -> Fraction:
    return sum((value**size / factorial(size) for size in range(cap + 1)), Fraction(0))


def balanced_clique_pressure(value: Fraction, cap: int) -> Fraction:
    return (1 + value / cap) ** cap


def check_hypergraph(
    coordinate_count: int,
    minimum_support: int,
    supports: tuple[frozenset[int], ...],
) -> tuple[Fraction, Fraction, Fraction, int]:
    if any(len(support) < minimum_support for support in supports):
        raise AssertionError("minimum support")
    activities = tuple(Fraction(1, 2 ** len(support)) for support in supports)
    primitive_mass = sum(activities, Fraction(0))
    cap = coordinate_count // minimum_support
    independence = independence_polynomial(supports, activities)
    balanced = balanced_clique_pressure(primitive_mass, cap)
    majorant = truncated_exp(primitive_mass, cap)
    if not independence <= balanced <= majorant:
        raise AssertionError(
            (coordinate_count, minimum_support, independence, balanced, majorant)
        )
    return independence, balanced, majorant, cap


def production_minimum(order: int) -> int:
    if order == 1:
        return 5
    if order == 2:
        return 6
    if order == 4:
        return 9
    if order >= 8 and order & (order - 1) == 0:
        return 2 * order + 1
    raise AssertionError(order)


def main() -> None:
    cases = (
        (6, 2, (frozenset((0, 1)), frozenset((2, 3)), frozenset((4, 5)))),
        (8, 2, (frozenset((0, 1)), frozenset((2, 3)), frozenset((0, 4)), frozenset((5, 6, 7)))),
        (9, 3, (frozenset((0, 1, 2)), frozenset((3, 4, 5)), frozenset((6, 7, 8)), frozenset((0, 3, 6)))),
        (12, 4, tuple(frozenset(support) for support in combinations(range(6), 4))),
    )
    hypergraph_rows = [check_hypergraph(*case) for case in cases]
    if not all(
        independence <= balanced <= majorant
        for independence, balanced, majorant, _ in hypergraph_rows
    ):
        raise AssertionError(hypergraph_rows)
    if hypergraph_rows[0][0] != hypergraph_rows[0][1]:
        raise AssertionError(("balanced equality", hypergraph_rows[0]))

    schedule = [2**power for power in range(32, 0, -1)] + [1, 1]
    caps = []
    for order in schedule:
        minimum = production_minimum(order)
        cap = 256 * order // minimum
        caps.append(cap)
        if cap * minimum > 256 * order or (cap + 1) * minimum <= 256 * order:
            raise AssertionError((order, minimum, cap))
    if len(schedule) != 34 or sum(schedule) != 2**33:
        raise AssertionError((len(schedule), sum(schedule)))
    if caps[-2:] != [51, 51] or caps[-3] != 85 or caps[-4] != 113:
        raise AssertionError(caps[-4:])
    if max(caps) != 127 or caps[29] != 120:
        raise AssertionError((max(caps), caps[29]))

    # Omitting either pressure correction must be detectable on finite data.
    value = Fraction(9, 2)
    if not truncated_exp(value, 3) < truncated_exp(value, 4):
        raise AssertionError("truncation mutation")
    if not balanced_clique_pressure(value, 3) < truncated_exp(value, 3):
        raise AssertionError("balanced-pressure mutation")
    print(
        "DLI_PRIMITIVE_MATCHING_TRUNCATION_MAJORANT_PASS "
        f"hypergraphs={len(cases)} schedule={len(schedule)} max_cap={max(caps)} "
        f"terminal_caps={caps[-4:]} mutations=2/2"
    )


if __name__ == "__main__":
    main()
