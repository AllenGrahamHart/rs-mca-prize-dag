#!/usr/bin/env python3
"""Exact e=7 weld-rank probe on two smooth cyclic grids."""

import random


OFFSETS = (0, 1, 7, 8, 14)
TRIALS = 100


def prime_factors(value):
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(modulus):
    factors = prime_factors(modulus - 1)
    for candidate in range(2, modulus):
        if all(
            pow(candidate, (modulus - 1) // factor, modulus) != 1
            for factor in factors
        ):
            return candidate
    raise AssertionError("primitive root not found")


def polynomial_value(roots, value, modulus):
    result = 1
    for root in roots:
        result = result * (value - root) % modulus
    return result


def matrix_rank(rows, columns, modulus):
    pivots = {}
    for source in rows:
        row = source[:]
        for column, pivot in pivots.items():
            if row[column]:
                factor = row[column]
                row = [
                    (left - factor * right) % modulus
                    for left, right in zip(row, pivot)
                ]
        for column, value in enumerate(row):
            if value:
                inverse = pow(value, -1, modulus)
                pivots[column] = [entry * inverse % modulus for entry in row]
                break
        if len(pivots) == columns:
            return columns
    return len(pivots)


def weld_rank(incidence, domain, slopes, modulus):
    column_rows = [
        [row for row in range(28) if column in incidence[row]]
        for column in range(21)
    ]
    zero_columns = [
        column for column, rows in enumerate(column_rows) if len(rows) == 7
    ]
    assert len(zero_columns) == 14

    rows = []
    for column in zero_columns:
        t = slopes[column]
        fiber_roots = [domain[row] for row in column_rows[column]]
        nonincident = [row for row in range(28) if row not in column_rows[column]]
        anchor = nonincident[0]
        anchor_fiber = polynomial_value(fiber_roots, domain[anchor], modulus)
        anchor_row = polynomial_value(
            [slopes[index] for index in incidence[anchor]], t, modulus
        )
        for row_index in nonincident[1:]:
            row = [0] * 28
            row_value = polynomial_value(
                [slopes[index] for index in incidence[row_index]], t, modulus
            )
            fiber_value = polynomial_value(
                fiber_roots, domain[row_index], modulus
            )
            row[row_index] = row_value * anchor_fiber % modulus
            row[anchor] = -anchor_row * fiber_value % modulus
            rows.append(row)
    return matrix_rank(rows, 28, modulus)


def switched_copy(base, rng):
    incidence = [row.copy() for row in base]
    for _ in range(300):
        first, second = rng.sample(range(28), 2)
        left = rng.choice(tuple(incidence[first]))
        right = rng.choice(tuple(incidence[second]))
        if (
            left != right
            and right not in incidence[first]
            and left not in incidence[second]
        ):
            incidence[first].remove(left)
            incidence[first].add(right)
            incidence[second].remove(right)
            incidence[second].add(left)
    return incidence


for modulus in (337, 421):
    generator = primitive_root(modulus)
    domain = [
        pow(generator, (modulus - 1) // 28 * exponent, modulus)
        for exponent in range(28)
    ]
    slopes = [
        pow(generator, (modulus - 1) // 21 * exponent, modulus)
        for exponent in range(21)
    ]
    base = [
        {(row + offset) % 21 for offset in OFFSETS}
        for row in range(28)
    ]
    assert weld_rank(base, domain, slopes, modulus) == 28

    rng = random.Random(20260811)
    histogram = {}
    for _ in range(TRIALS):
        incidence = switched_copy(base, rng)
        value = weld_rank(incidence, domain, slopes, modulus)
        histogram[value] = histogram.get(value, 0) + 1
    assert histogram == {28: TRIALS}
    print("RATE_HALF_SCALAR_WELD_PROBE", modulus, histogram)

print("RATE_HALF_SCALAR_WELD_PROBE_PASS")
