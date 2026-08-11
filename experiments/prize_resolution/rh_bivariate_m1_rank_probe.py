#!/usr/bin/env python3
"""Exact rank probe for the deficiency-aware matrix on the m=1 witness."""

from itertools import combinations


PRIME = 17
DOMAIN = tuple(range(1, 17))
Y0 = (1, 10, 16, 2, 14, 0, 3, 11)
Y1 = (0, 14, 9, 7, 13, 12, 15, 0)
SUPPORTS = {
    0: (1, 2, 5),
    1: (3, 7, 11),
    2: (9, 12, 13),
    4: (4, 6, 16),
    15: (8, 10, 15),
}


def inverse(value: int) -> int:
    return pow(value % PRIME, PRIME - 2, PRIME)


def syndrome(word: list[int]) -> tuple[int, ...]:
    return tuple(
        sum(word[x - 1] * pow(x, moment, PRIME) for x in DOMAIN) % PRIME
        for moment in range(8)
    )


def solve_support(support: tuple[int, ...], target: tuple[int, ...]) -> list[int]:
    rows = [
        [pow(x, moment, PRIME) for x in support] + [target[moment]]
        for moment in range(8)
    ]
    pivot_columns = []
    pivot_row = 0
    for column in range(len(support)):
        selected = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column]),
            None,
        )
        if selected is None:
            continue
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        scale = inverse(rows[pivot_row][column])
        rows[pivot_row] = [(entry * scale) % PRIME for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                (entry - factor * pivot) % PRIME
                for entry, pivot in zip(rows[row], rows[pivot_row])
            ]
        pivot_columns.append(column)
        pivot_row += 1

    assert all(not row[len(support)] for row in rows[pivot_row:])
    coefficients = [0] * len(support)
    for row, column in enumerate(pivot_columns):
        coefficients[column] = rows[row][len(support)]
    assert all(coefficients)
    word = [0] * 16
    for x, value in zip(support, coefficients):
        word[x - 1] = value
    assert syndrome(word) == target
    return word


def matrix_rank(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        selected = next(
            (row for row in range(rank, len(rows)) if rows[row][column]),
            None,
        )
        if selected is None:
            continue
        rows[rank], rows[selected] = rows[selected], rows[rank]
        scale = inverse(rows[rank][column])
        rows[rank] = [(entry * scale) % PRIME for entry in rows[rank]]
        for row in range(len(rows)):
            if row == rank or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                (entry - factor * pivot) % PRIME
                for entry, pivot in zip(rows[row], rows[rank])
            ]
        rank += 1
    return rank


def determinant(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    value = 1
    for column in range(len(rows)):
        selected = next(
            (row for row in range(column, len(rows)) if rows[row][column]),
            None,
        )
        if selected is None:
            return 0
        if selected != column:
            rows[column], rows[selected] = rows[selected], rows[column]
            value = -value
        pivot = rows[column][column]
        value = value * pivot % PRIME
        scale = inverse(pivot)
        for row in range(column + 1, len(rows)):
            factor = rows[row][column] * scale % PRIME
            for index in range(column, len(rows)):
                rows[row][index] = (
                    rows[row][index] - factor * rows[column][index]
                ) % PRIME
    return value % PRIME


def rank_five_certificate(matrix: list[list[int]]) -> tuple[tuple[int, ...], int, int]:
    for rows in combinations(range(15), 5):
        for omitted_column in range(6):
            columns = [column for column in range(6) if column != omitted_column]
            minor = [[matrix[row][column] for column in columns] for row in rows]
            value = determinant(minor)
            if value:
                return rows, omitted_column, value
    raise AssertionError("no nonzero rank-five minor")


def locator_coefficients(x: int) -> tuple[int, int]:
    q0 = (x**3 + 9 * x**2 + 7) % PRIME
    q1 = (4 * x**2 + 12 * x) % PRIME
    return q0, q1


def pair_matrix(
    first_slope: int,
    second_slope: int,
    representatives: dict[int, list[int]],
) -> tuple[list[list[int]], list[int], tuple[int, ...]]:
    first = representatives[first_slope]
    second = representatives[second_slope]
    slope_gap_inverse = inverse(second_slope - first_slope)
    c1 = [
        ((second[index] - first[index]) * slope_gap_inverse) % PRIME
        for index in range(16)
    ]
    c0 = [
        (first[index] - first_slope * c1[index]) % PRIME
        for index in range(16)
    ]
    assert syndrome(c0) == Y0
    assert syndrome(c1) == Y1

    support = tuple(
        sorted(set(SUPPORTS[first_slope]) | set(SUPPORTS[second_slope]))
    )
    assert len(support) == 6
    assert all(c0[x - 1] or c1[x - 1] for x in support)
    assert all(not c0[x - 1] and not c1[x - 1] for x in DOMAIN if x not in support)

    rows = []
    kernel = []
    bases = {}
    root_owner = {
        x: slope for slope, points in SUPPORTS.items() for x in points
    }
    for x in support:
        owner = root_owner[x]
        q0, q1 = locator_coefficients(x)
        assert (q0 + owner * q1) % PRIME == 0
        assert q1
        kernel.append(q1)
        linear = (c0[x - 1], c1[x - 1])
        root_factor = ((-owner) % PRIME, 1)
        bases[x] = (
            linear[0] * root_factor[0] % PRIME,
            (linear[0] + linear[1] * root_factor[0]) % PRIME,
            linear[1],
        )

    for moment in range(5):
        for degree in range(3):
            rows.append(
                [bases[x][degree] * pow(x, moment, PRIME) % PRIME for x in support]
            )
    assert all(sum(a * b for a, b in zip(row, kernel)) % PRIME == 0 for row in rows)
    return rows, kernel, support


def main() -> None:
    representatives = {}
    for slope, support in SUPPORTS.items():
        target = tuple((a + slope * b) % PRIME for a, b in zip(Y0, Y1))
        representatives[slope] = solve_support(support, target)

    records = []
    for first_slope, second_slope in combinations(SUPPORTS, 2):
        matrix, kernel, support = pair_matrix(
            first_slope,
            second_slope,
            representatives,
        )
        rank = matrix_rank(matrix)
        assert len(matrix) == 15
        assert len(matrix[0]) == 6
        assert rank == 5
        assert all(kernel)
        certificate = rank_five_certificate(matrix)
        records.append((first_slope, second_slope, support, rank, certificate))

    omitted = set(DOMAIN) - {
        x for support in SUPPORTS.values() for x in support
    }
    assert omitted == {14}
    q0_14, q1_14 = locator_coefficients(14)
    assert q0_14 and not q1_14

    for first, second, support, rank, certificate in records:
        print(
            f"pair=({first},{second}) W={support} shape=15x6 "
            f"rank={rank} nullity={6-rank} deficient_point_in_W={14 in support} "
            f"minor={certificate}"
        )
    print(
        "RATE_HALF_BIVARIATE_M1_RANK_PROBE_PASS "
        "pairs=10 ranks=5 nullities=1 deficient_point=14 outside_every_W"
    )


if __name__ == "__main__":
    main()
