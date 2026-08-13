#!/usr/bin/env python3
"""Replay arbitrary static omitted-recurrence runs over F_101."""

import argparse
from itertools import combinations


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def multiply(left, right, prime):
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] = (product[i + j] + a * b) % prime
    return product


def evaluate(poly, value, prime):
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % prime
    return result


def determinant(matrix, prime):
    work = [[entry % prime for entry in row] for row in matrix]
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
    work = [[entry % prime for entry in row] for row in matrix]
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
        work[row] = [entry * inverse % prime for entry in work[row]]
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


def replay(mutation=None):
    mutation = mutation or {}
    prime = mutation.get("prime", 101)
    d = mutation.get("d", 3)
    n = mutation.get("n", 3)
    source = list(range(1, mutation.get("source_stop", 9)))
    roots = mutation.get("roots", [20, 21, 22])
    auxiliary_root = mutation.get("auxiliary_root", 30)

    require(prime == 101, "fixture field")
    require(d == 3 and n == 3, "fixture dimensions")
    require(len(source) == d + n + 2 == 8, "source count")
    require(len(roots) == d and len(set(roots)) == d, "Q roots")
    require(
        len(set(source + roots + [auxiliary_root])) == len(source) + d + 1,
        "point separation",
    )

    locator = [1]
    for root in roots:
        locator = multiply(locator, [-root % prime, 1], prime)
    source_locator = [1]
    for point in source:
        source_locator = multiply(
            source_locator, [-point % prime, 1], prime
        )

    cases = 0
    residue_checks = 0
    subset_checks = 0
    for drop in range(n + 1):
        residual = [1]
        for _ in range(n - drop):
            residual = multiply(
                residual, [-auxiliary_root % prime, 1], prime
            )

        weights = []
        for point in source:
            denominator = (
                evaluate(locator, point, prime)
                * evaluate(
                    [
                        index * coefficient % prime
                        for index, coefficient in enumerate(source_locator)
                    ][1:],
                    point,
                    prime,
                )
            ) % prime
            require(denominator != 0, "nonzero source denominator")
            weights.append(
                evaluate(residual, point, prime)
                * pow(denominator, prime - 2, prime)
                % prime
            )
        require(all(weights), "all source weights nonzero")

        moment_limit = 2 * (d + 1 + drop)
        moments = [
            sum(
                weight * pow(point, power, prime)
                for point, weight in zip(source, weights)
            ) % prime
            for power in range(moment_limit + 1)
        ]
        middle = [
            [moments[i + j] for j in range(d + 1)]
            for i in range(d + 1)
        ]
        require(rank(middle, prime) == d, "exact middle corank one")
        require(
            all(
                sum(middle[i][j] * locator[j] for j in range(d + 1))
                % prime == 0
                for i in range(d + 1)
            ),
            "locator kernel",
        )

        defects = [
            sum(locator[i] * moments[i + j] for i in range(d + 1))
            % prime
            for j in range(d + 1, d + 2 + drop)
        ]
        require(defects[:drop] == [0] * drop, "initial zero run")
        require(defects[drop] == residual[-1] == 1, "first omitted defect")

        for left in range(d):
            for right in range(d):
                source_pairing = moments[left + right]
                root_pairing = 0
                for root in roots:
                    q_derivative = 1
                    for other in roots:
                        if other != root:
                            q_derivative = q_derivative * (root - other) % prime
                    coefficient = (
                        evaluate(residual, root, prime)
                        * pow(
                            q_derivative
                            * evaluate(source_locator, root, prime)
                            % prime,
                            prime - 2,
                            prime,
                        )
                    ) % prime
                    root_pairing = (
                        root_pairing
                        - coefficient * pow(root, left + right, prime)
                    ) % prime
                require(source_pairing == root_pairing, "residue pairing")
                residue_checks += 1

        regular_factor = determinant(
            [row[:d] for row in middle[:d]], prime
        )
        require(regular_factor != 0, "nonzero adjugate scalar")
        for s in range(drop + 1):
            vector = [moments[d + 1 + s + i] for i in range(d + 1)]
            defect = defects[s]
            for column in range(d + 1):
                replaced = [row[:] for row in middle]
                for row in range(d + 1):
                    replaced[row][column] = vector[row]
                require(
                    determinant(replaced, prime)
                    == regular_factor * locator[column] * defect % prime,
                    "replacement minor",
                )

            exponents = list(range(d + 1)) + [d + 1 + s]
            bordered = [
                [moments[left + right] for right in exponents]
                for left in exponents
            ]
            bordered_value = determinant(bordered, prime)
            require(
                bordered_value
                == -regular_factor * defect * defect % prime,
                "bordered square",
            )

            source_sum = 0
            for subset in combinations(range(len(source)), d + 2):
                alternant = determinant([
                    [pow(source[index], exponent, prime) for index in subset]
                    for exponent in exponents
                ], prime)
                subset_weight = 1
                for index in subset:
                    subset_weight = subset_weight * weights[index] % prime
                source_sum = (
                    source_sum + alternant * alternant * subset_weight
                ) % prime
                subset_checks += 1
            require(source_sum == bordered_value, "source Cauchy-Binet")
        cases += 1

    require(cases == 4, "drop case count")
    require(residue_checks == 36, "residue check count")
    require(subset_checks == 560, "source subset check count")
    return cases, residue_checks, subset_checks


def tamper_selftest():
    mutations = [
        {"prime": 103},
        {"d": 2},
        {"n": 2},
        {"source_stop": 8},
        {"roots": [20, 21, 21]},
        {"auxiliary_root": 8},
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
    cases, residue_checks, subset_checks = replay()
    suffix = ""
    if args.tamper_selftest:
        suffix = f" mutations={tamper_selftest()}/6"
    print(
        "RATE_HALF_SHAPE_A_STATIC_ARBITRARY_DROP_FENCE_PASS "
        f"cases={cases} residues={residue_checks} "
        f"subsets={subset_checks}{suffix}"
    )


if __name__ == "__main__":
    main()
