#!/usr/bin/env python3
"""Replay the all-excess parameter-MDS gate and e=7 rank probes."""

import argparse
import random


OFFSETS = (0, 1, 7, 8, 14)
TRIALS = 50


def require(condition, message):
    if not condition:
        raise AssertionError(message)


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
    raise AssertionError("primitive root")


def multiply(left, right, modulus):
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] = (product[i + j] + a * b) % modulus
    return product


def root_polynomial(roots, modulus):
    polynomial = [1]
    for root in roots:
        polynomial = multiply(polynomial, [-root % modulus, 1], modulus)
    return polynomial


def matrix_rank(rows, columns, modulus):
    pivots = {}
    for input_row in rows:
        row = input_row[:]
        for column, pivot in pivots.items():
            if row[column]:
                scale = row[column]
                row = [
                    (left - scale * right) % modulus
                    for left, right in zip(row, pivot)
                ]
        for column, value in enumerate(row):
            if value:
                inverse = pow(value, modulus - 2, modulus)
                pivots[column] = [entry * inverse % modulus for entry in row]
                break
        if len(pivots) == columns:
            return columns
    return len(pivots)


def all_excess_matrix(incidence, domain, slopes, modulus):
    e = 7
    n = 7
    excesses = [
        n - sum(column in row for row in incidence)
        for column in range(len(slopes))
    ]
    require(sum(excesses) == e, "e=7 excess sum")

    slope_weights = []
    for index, slope in enumerate(slopes):
        derivative = 1
        for other_index, other in enumerate(slopes):
            if index != other_index:
                derivative = derivative * (slope - other) % modulus
        slope_weights.append(pow(derivative, modulus - 2, modulus))

    known = []
    columns = []
    for delta_index, excess in enumerate(excesses):
        roots = [
            domain[row]
            for row in range(len(domain))
            if delta_index in incidence[row]
        ]
        polynomial = root_polynomial(roots, modulus)
        require(len(polynomial) - 1 == n - excess, "known locator degree")
        known.append(polynomial)
        for residual_degree in range(excess + 1):
            columns.append((delta_index, residual_degree))
    require(len(columns) == 4 * e == 28, "all-excess column count")

    rows = []
    for coefficient in range(n + 1):
        for power in range(2 * e + 1):
            row = []
            for delta_index, residual_degree in columns:
                known_degree = coefficient - residual_degree
                known_coefficient = (
                    known[delta_index][known_degree]
                    if 0 <= known_degree < len(known[delta_index])
                    else 0
                )
                row.append(
                    known_coefficient
                    * pow(slopes[delta_index], power, modulus)
                    * slope_weights[delta_index]
                    % modulus
                )
            rows.append(row)
    require(len(rows) == 120, "e=7 parity row count")
    return rows, len(columns)


def switched_copy(base, rng):
    incidence = [row.copy() for row in base]
    for _ in range(120):
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


def positive_equivalence_fixture(modulus):
    slopes = list(range(1, 8))
    coefficients = []
    for slope in slopes:
        coefficients.extend([
            (3 + 2 * slope + slope * slope) % modulus,
            (5 + slope) % modulus,
            (7 + 4 * slope + 2 * slope * slope) % modulus,
            (11 + 3 * slope) % modulus,
        ])

    rows = []
    for x_coefficient in range(4):
        for power in range(4):
            row = []
            for slope_index, slope in enumerate(slopes):
                derivative = 1
                for other in slopes:
                    if other != slope:
                        derivative = derivative * (slope - other) % modulus
                for residual_degree in range(4):
                    row.append(
                        (1 if residual_degree == x_coefficient else 0)
                        * pow(slope, power, modulus)
                        * pow(derivative, modulus - 2, modulus)
                        % modulus
                    )
            rows.append(row)
    require(
        all(
            sum(left * right for left, right in zip(row, coefficients))
            % modulus == 0
            for row in rows
        ),
        "positive all-excess equivalence fixture",
    )
    corrupted = coefficients[:]
    corrupted[0] = (corrupted[0] + 1) % modulus
    require(
        any(
            sum(left * right for left, right in zip(row, corrupted))
            % modulus
            for row in rows
        ),
        "corrupted all-excess fixture",
    )


def replay(mutation=None):
    mutation = mutation or {}
    trials = mutation.get("trials", TRIALS)
    offsets = mutation.get("offsets", OFFSETS)
    require(trials == TRIALS and offsets == OFFSETS, "fixture controls")

    histograms = {}
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
            {(row + offset) % 21 for offset in offsets}
            for row in range(28)
        ]
        rows, columns = all_excess_matrix(base, domain, slopes, modulus)
        require(matrix_rank(rows, columns, modulus) == 28, "base full rank")

        rng = random.Random(20260813)
        histogram = {}
        for _ in range(trials):
            switched = switched_copy(base, rng)
            rows, columns = all_excess_matrix(
                switched, domain, slopes, modulus
            )
            rank = matrix_rank(rows, columns, modulus)
            histogram[rank] = histogram.get(rank, 0) + 1
        require(histogram == {28: trials}, "switched rank histogram")
        histograms[modulus] = histogram
        positive_equivalence_fixture(modulus)

    official_e = 183251937963
    official_n = (3 * official_e - 7) // 2
    require(4 * official_e == 733007751852, "official column count")
    require(
        (official_n + 1) * (2 * official_e + 1)
        == 100743818300944219985234,
        "official row count",
    )
    return histograms


def tamper_selftest():
    mutations = [
        {"trials": TRIALS - 1},
        {"offsets": (0, 1, 7, 8, 13)},
    ]
    rejected = 0
    for mutation in mutations:
        try:
            replay(mutation)
        except (AssertionError, IndexError):
            rejected += 1
    require(rejected == len(mutations), "hostile mutation rejection")
    return rejected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    histograms = replay()
    suffix = ""
    if args.tamper_selftest:
        suffix = f" mutations={tamper_selftest()}/2"
    print(
        "RATE_HALF_SHAPE_A_ALL_EXCESS_PARAMETER_MDS_GATE_PASS "
        f"histograms={histograms}{suffix}"
    )


if __name__ == "__main__":
    main()
