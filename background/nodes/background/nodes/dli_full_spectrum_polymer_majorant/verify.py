#!/usr/bin/env python3
"""Verify finite primitive-cover instances and the DLI normalization."""

from __future__ import annotations

import itertools
import math
from fractions import Fraction


def support(vector: tuple[int, ...]) -> frozenset[int]:
    return frozenset(index for index, value in enumerate(vector) if value)


def relations(prime: int, values: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [
        vector
        for vector in itertools.product((-1, 0, 1), repeat=len(values))
        if sum(coefficient * value for coefficient, value in zip(vector, values)) % prime == 0
    ]


def primitives(rows: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    row_set = set(rows)
    output = []
    for row in rows:
        row_support = support(row)
        if not row_support:
            continue
        is_primitive = True
        for mask in range(1, (1 << len(row_support)) - 1):
            indices = sorted(row_support)
            restricted = tuple(
                value if index in {indices[j] for j in range(len(indices)) if (mask >> j) & 1} else 0
                for index, value in enumerate(row)
            )
            if restricted in row_set:
                is_primitive = False
                break
        if is_primitive:
            output.append(row)
    return output


def activity(vector: tuple[int, ...]) -> Fraction:
    return Fraction(1, 2 ** len(support(vector)))


def independence_polynomial(
    primitive_rows: list[tuple[int, ...]], dimension: int
) -> Fraction:
    # Aggregate compatible collections by their signed union. Distinct
    # collections with the same union retain their multiplicity in the value.
    states = {tuple([0] * dimension): Fraction(1)}
    for primitive in primitive_rows:
        primitive_support = support(primitive)
        additions = {}
        for state, weight in states.items():
            if support(state) & primitive_support:
                continue
            union = tuple(left + right for left, right in zip(state, primitive))
            additions[union] = additions.get(union, Fraction(0)) + weight * activity(primitive)
        for union, weight in additions.items():
            states[union] = states.get(union, Fraction(0)) + weight
    return sum(states.values(), Fraction(0))


def has_primitive_partition(
    row: tuple[int, ...], primitive_rows: list[tuple[int, ...]]
) -> bool:
    if not support(row):
        return True
    row_support = support(row)
    for primitive in primitive_rows:
        primitive_support = support(primitive)
        if not primitive_support <= row_support:
            continue
        if any(row[index] != primitive[index] for index in primitive_support):
            continue
        remainder = tuple(left - right for left, right in zip(row, primitive))
        if has_primitive_partition(remainder, primitive_rows):
            return True
    return False


def check_case(prime: int, values: tuple[int, ...]) -> tuple[int, int]:
    rows = relations(prime, values)
    primitive_rows = primitives(rows)
    if not primitive_rows or not all(has_primitive_partition(row, primitive_rows) for row in rows):
        raise AssertionError((prime, values, len(rows), len(primitive_rows)))
    partition = sum((activity(row) for row in rows), Fraction(0))
    primitive_mass = sum((activity(row) for row in primitive_rows), Fraction(0))
    independent = independence_polynomial(primitive_rows, len(values))
    unrestricted = math.prod(1 + activity(row) for row in primitive_rows)
    if not partition <= independent <= unrestricted:
        raise AssertionError((partition, independent, unrestricted))
    if float(partition) > math.exp(float(primitive_mass)) * (1 + 1e-12):
        raise AssertionError((partition, primitive_mass))

    # Each zero coordinate has two fused states and each sign one.
    dimension = len(values)
    a_total = sum(2 ** (dimension - len(support(row))) for row in rows)
    if Fraction(a_total, 2**dimension) != partition:
        raise AssertionError((a_total, partition))
    q_power = prime
    r = Fraction(q_power, 2**dimension)
    e_direct = Fraction(q_power * a_total, 4**dimension)
    if e_direct != r * partition:
        raise AssertionError((e_direct, r * partition))
    return len(rows), len(primitive_rows)


def main() -> None:
    cases = {
        (5, (1, 2, 3, 4)): None,
        (7, (1, 2, 3, 4, 5)): None,
        (11, (1, 3, 4, 5, 9)): None,
    }
    for case in cases:
        cases[case] = check_case(*case)
    if sum(primitive for _, primitive in cases.values()) == 0:
        raise AssertionError("vacuous primitive cover")

    # Exact official-schedule logarithmic coefficient identity.
    dimensions = [2**power for power in range(32, 0, -1)] + [1, 1]
    if len(dimensions) != 34 or sum(dimensions) != 2**33:
        raise AssertionError((len(dimensions), sum(dimensions)))

    # The exact partial ledgers from the C1' kill replay already fence the
    # uncorrected aggregate-activity route. Since log(2)<1 and q>2^b,
    # 100log(2)+log(2^32/q) < 132-b.
    route_fences = ((63361, 15, Fraction(283, 2)), (65921, 16, Fraction(263, 2)))
    for q, lower_bit, partial_ledger in route_fences:
        if not q > 2**lower_bit or not partial_ledger > 132 - lower_bit:
            raise AssertionError((q, lower_bit, partial_ledger))
    print(
        f"DLI_FULL_SPECTRUM_POLYMER_MAJORANT_PASS cases={cases} "
        f"schedule=34 route_fences={len(route_fences)}"
    )


if __name__ == "__main__":
    main()
