#!/usr/bin/env python3
"""Independent finite-field replay of the exact averaged-XR moment."""

from fractions import Fraction
from itertools import combinations, product


def rank_mod(matrix, p):
    work = [[value % p for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][col]), None
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        inv = pow(work[pivot_row][col], -1, p)
        work[pivot_row] = [(inv * value) % p for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][col]:
                continue
            factor = work[row][col]
            work[row] = [
                (left - factor * right) % p
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def inverse_mod(matrix, p):
    size = len(matrix)
    work = [
        [value % p for value in row]
        + [int(row_index == col) for col in range(size)]
        for row_index, row in enumerate(matrix)
    ]
    for col in range(size):
        pivot = next(row for row in range(col, size) if work[row][col])
        work[col], work[pivot] = work[pivot], work[col]
        inv = pow(work[col][col], -1, p)
        work[col] = [(inv * value) % p for value in work[col]]
        for row in range(size):
            if row == col or not work[row][col]:
                continue
            factor = work[row][col]
            work[row] = [
                (left - factor * right) % p
                for left, right in zip(work[row], work[col])
            ]
    return [row[size:] for row in work]


def pi_matrix(points, support, k, t, p):
    support = tuple(support)
    size = k + t
    vandermonde = [
        [pow(points[index], degree, p) for degree in range(size)]
        for index in support
    ]
    inverse = inverse_mod(vandermonde, p)
    matrix = []
    for degree in range(k, size):
        row = [0] * len(points)
        for local_index, global_index in enumerate(support):
            row[global_index] = inverse[degree][local_index]
        matrix.append(row)
    return matrix


def apply(matrix, vector, p):
    return tuple(
        sum(value * vector[index] for index, value in enumerate(row)) % p
        for row in matrix
    )


def is_zero(vector):
    return all(value == 0 for value in vector)


def rank_sweep():
    configurations = (
        (5, 5, 1, 2),
        (7, 7, 1, 3),
        (7, 7, 2, 2),
        (11, 8, 3, 2),
        (11, 8, 2, 3),
        (7, 6, 3, 1),
    )
    checked = 0
    mutation_kills = 0
    distance_histogram = {}
    for p, n, k, t in configurations:
        points = list(range(n))
        supports = list(combinations(range(n), k + t))
        matrices = {
            support: pi_matrix(points, support, k, t, p) for support in supports
        }
        for support_s in supports:
            for support_t in supports:
                distance = len(set(support_s) - set(support_t))
                actual = rank_mod(
                    matrices[support_s] + matrices[support_t], p
                )
                expected = t + min(distance, t)
                assert actual == expected, (
                    p,
                    n,
                    k,
                    t,
                    support_s,
                    support_t,
                    actual,
                    expected,
                )
                distance_histogram[distance] = distance_histogram.get(distance, 0) + 1
                checked += 1
                if t >= 2:
                    wrong = t + min(distance, t - 1)
                    mutation_kills += int(actual != wrong)
    assert mutation_kills > 0
    return checked, mutation_kills, distance_histogram


def brute_pair_counts():
    p, n, k, t = 5, 5, 1, 2
    points = list(range(n))
    support_s = (0, 1, 2)
    representatives = ((0, 1, 3), (0, 3, 4))
    matrix_s = pi_matrix(points, support_s, k, t, p)
    checked = 0
    for support_t in representatives:
        matrix_t = pi_matrix(points, support_t, k, t, p)
        distance = len(set(support_s) - set(support_t))
        joint_rank = t + min(distance, t)
        words = product(range(p), repeat=n)
        both_kernel = 0
        outside_both = 0
        for word in words:
            in_s = is_zero(apply(matrix_s, word, p))
            in_t = is_zero(apply(matrix_t, word, p))
            both_kernel += int(in_s and in_t)
            outside_both += int(not in_s and not in_t)
        assert both_kernel == p ** (n - joint_rank)
        assert outside_both == (
            p**n - 2 * p ** (n - t) + p ** (n - joint_rank)
        )
        observed = Fraction(both_kernel * outside_both, p ** (2 * n))
        alpha = Fraction(1, p**joint_rank)
        expected = alpha * (1 - 2 * Fraction(1, p**t) + alpha)
        assert observed == expected
        checked += 1
    return checked


def occupancy_sweep():
    checked = 0
    for slope_count in range(1, 7):
        for counts in product(range(5), repeat=slope_count):
            occupied = sum(value > 0 for value in counts)
            incidences = sum(counts)
            ordered_collisions = sum(value * (value - 1) for value in counts)
            assert 2 * occupied >= 2 * incidences - ordered_collisions
            checked += 1
    return checked


def main():
    ranks, mutations, distances = rank_sweep()
    pair_counts = brute_pair_counts()
    occupancies = occupancy_sweep()
    print(
        "AVERAGED_XR_EXACT_MOMENT_PASS "
        f"rank_pairs={ranks} distances={sorted(distances)} "
        f"pair_counts={pair_counts} occupancy_vectors={occupancies} "
        f"mutation_kills={mutations}"
    )


if __name__ == "__main__":
    main()
