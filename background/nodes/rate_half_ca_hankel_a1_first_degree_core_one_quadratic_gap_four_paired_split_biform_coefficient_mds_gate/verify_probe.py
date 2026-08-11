#!/usr/bin/env python3
"""Exact e=7 coefficient-MDS rank probe on two smooth cyclic grids."""

import random


OFFSETS = (0, 1, 7, 8, 14)
TRIALS = 250


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


def root_polynomial(roots, modulus):
    coefficients = [1]
    for root in roots:
        updated = [0] * (len(coefficients) + 1)
        for index, coefficient in enumerate(coefficients):
            updated[index] = (updated[index] - root * coefficient) % modulus
            updated[index + 1] = (updated[index + 1] + coefficient) % modulus
        coefficients = updated
    return coefficients


def matrix_rank(rows, columns, modulus):
    pivots = {}
    for row in rows:
        row = row[:]
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


def coefficient_rank(incidence, domain, slopes, modulus):
    weights = []
    for index, x in enumerate(domain):
        derivative = 1
        for other_index, y in enumerate(domain):
            if index != other_index:
                derivative = derivative * (x - y) % modulus
        weights.append(pow(derivative, -1, modulus))

    row_coefficients = [
        root_polynomial([slopes[column] for column in row], modulus)
        for row in incidence
    ]
    rows = []
    for coefficient in range(6):
        for power in range(20):
            rows.append(
                [
                    row_coefficients[index][coefficient]
                    * pow(domain[index], power, modulus)
                    * weights[index]
                    % modulus
                    for index in range(28)
                ]
            )
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
    column_degrees = [
        sum(column in row for row in base)
        for column in range(21)
    ]
    assert sorted(column_degrees) == [6] * 7 + [7] * 14
    assert coefficient_rank(base, domain, slopes, modulus) == 28

    rng = random.Random(20260811)
    histogram = {}
    for _ in range(TRIALS):
        incidence = switched_copy(base, rng)
        rank = coefficient_rank(incidence, domain, slopes, modulus)
        histogram[rank] = histogram.get(rank, 0) + 1
    assert histogram == {28: TRIALS}
    print("RATE_HALF_COEFFICIENT_MDS_PROBE", modulus, histogram)

print("RATE_HALF_QUADRATIC_PAIRED_COEFFICIENT_MDS_PROBE_PASS")
