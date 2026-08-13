#!/usr/bin/env python3
"""Replay the omitted-recurrence bordered-Hankel identities."""

import argparse
from itertools import combinations


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def determinant(matrix, prime):
    work = [[value % prime for value in row] for row in matrix]
    value = 1
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            value = -value
        pivot_value = work[column][column]
        value = value * pivot_value % prime
        inverse = pow(pivot_value, prime - 2, prime)
        for row in range(column + 1, len(work)):
            if not work[row][column]:
                continue
            scale = work[row][column] * inverse % prime
            for index in range(column, len(work)):
                work[row][index] = (
                    work[row][index] - scale * work[column][index]
                ) % prime
    return value % prime


def rank(matrix, prime):
    work = [[value % prime for value in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next(
            (index for index in range(row, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        inverse = pow(work[row][column], prime - 2, prime)
        work[row] = [value * inverse % prime for value in work[row]]
        for index in range(len(work)):
            if index == row or not work[index][column]:
                continue
            scale = work[index][column]
            work[index] = [
                (left - scale * right) % prime
                for left, right in zip(work[index], work[row])
            ]
        row += 1
        if row == len(work):
            break
    return row


def solve(matrix, right, prime):
    augmented = [
        [value % prime for value in row] + [target % prime]
        for row, target in zip(matrix, right)
    ]
    size = len(matrix)
    for column in range(size):
        pivot = next(
            row for row in range(column, size) if augmented[row][column]
        )
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        inverse = pow(augmented[column][column], prime - 2, prime)
        augmented[column] = [value * inverse % prime for value in augmented[column]]
        for row in range(size):
            if row == column or not augmented[row][column]:
                continue
            scale = augmented[row][column]
            augmented[row] = [
                (left - scale * right_value) % prime
                for left, right_value in zip(augmented[row], augmented[column])
            ]
    return [augmented[index][-1] for index in range(size)]


def replay(mutation=None):
    mutation = mutation or {}
    e = mutation.get("e", (2**39 + 1) // 3)
    d = mutation.get("d", 3 * e - 2)
    source_count = mutation.get("source_count", 824633720830)
    off_count = mutation.get("off_count", 3 * e)
    padding_count = mutation.get("padding_count", e - 7)
    regular_count = mutation.get("regular_count", 2 * e + 7)
    determinant_degree = mutation.get("determinant_degree", 3 * e)

    require(e == 183251937963, "official e")
    require(d == 549755813887, "official d")
    require(source_count == 824633720830, "source count")
    require(d + 2 == off_count == 549755813889, "border/source degree")
    require(padding_count == 183251937956, "padding flag size")
    require(regular_count == 366503875933, "regular flag size")
    require(padding_count + regular_count == off_count, "flag partition")
    require(determinant_degree == 549755813889, "bordered determinant degree")

    prime = 101
    moments = [1, 0, 1, 0, 1, 2, 3, 4, 5]
    fixture_d = 2
    M = [
        [moments[i + j] for j in range(fixture_d + 1)]
        for i in range(fixture_d + 1)
    ]
    q = [-1, 0, 1]
    require(rank(M, prime) == fixture_d, "fixture middle rank")
    require(
        all(
            sum(M[i][j] * q[j] for j in range(fixture_d + 1)) % prime == 0
            for i in range(fixture_d + 1)
        ),
        "fixture kernel",
    )

    defects = []
    for s in (0, 1):
        exponent = fixture_d + 1 + s
        vector = [moments[exponent + i] for i in range(fixture_d + 1)]
        defect = sum(left * right for left, right in zip(q, vector)) % prime
        defects.append(defect)
        for column in range(fixture_d + 1):
            replaced = [row[:] for row in M]
            for row in range(fixture_d + 1):
                replaced[row][column] = vector[row]
            require(
                determinant(replaced, prime) == q[column] * defect % prime,
                "replacement-minor identity",
            )

        exponents = list(range(fixture_d + 1)) + [exponent]
        bordered = [
            [moments[left + right] for right in exponents]
            for left in exponents
        ]
        require(
            determinant(bordered, prime) == -defect * defect % prime,
            "bordered determinant square",
        )

    require(defects == [2, 2], "fixture defects")

    points = list(range(1, 10))
    vandermonde = [
        [pow(point, power, prime) for point in points]
        for power in range(len(points))
    ]
    weights = solve(vandermonde, moments, prime)
    require(
        all(
            sum(weight * pow(point, power, prime)
                for point, weight in zip(points, weights)) % prime
            == moments[power] % prime
            for power in range(len(moments))
        ),
        "source moment reconstruction",
    )

    subset_checks = 0
    for s, defect in enumerate(defects):
        exponents = list(range(fixture_d + 1)) + [fixture_d + 1 + s]
        source_sum = 0
        for subset in combinations(range(len(points)), fixture_d + 2):
            alternant = determinant(
                [[pow(points[index], exponent, prime) for index in subset]
                 for exponent in exponents],
                prime,
            )
            weight = 1
            for index in subset:
                weight = weight * weights[index] % prime
            source_sum = (source_sum + alternant * alternant * weight) % prime
            subset_checks += 1
        require(source_sum == -defect * defect % prime, "source subset sum")

    return d, regular_count, subset_checks


def tamper_selftest():
    mutations = [
        {"e": 183251937964},
        {"d": 549755813886},
        {"source_count": 824633720829},
        {"off_count": 549755813888},
        {"padding_count": 183251937955},
        {"regular_count": 366503875932},
        {"determinant_degree": 549755813888},
    ]
    rejected = 0
    for mutation in mutations:
        try:
            replay(mutation)
        except AssertionError:
            rejected += 1
    require(rejected == len(mutations), "hostile mutation rejection")
    return rejected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    d, regular_count, subset_checks = replay()
    suffix = ""
    if args.tamper_selftest:
        suffix = f" mutations={tamper_selftest()}/7"
    print(
        "RATE_HALF_SHAPE_A_BORDERED_HANKEL_FLAG_PASS "
        f"d={d} regular={regular_count} subset_checks={subset_checks}{suffix}"
    )


if __name__ == "__main__":
    main()
