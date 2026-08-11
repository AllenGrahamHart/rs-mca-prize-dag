#!/usr/bin/env python3
"""Verify rational-interpolation equivalence against direct matrix ranks."""


def inverse(value: int, prime: int) -> int:
    return pow(value % prime, prime - 2, prime)


def rank(matrix: list[list[int]], prime: int) -> int:
    rows = [row[:] for row in matrix]
    output = 0
    for column in range(len(rows[0])):
        pivot = next(
            (row for row in range(output, len(rows)) if rows[row][column] % prime),
            None,
        )
        if pivot is None:
            continue
        rows[output], rows[pivot] = rows[pivot], rows[output]
        scale = inverse(rows[output][column], prime)
        rows[output] = [entry * scale % prime for entry in rows[output]]
        for row in range(len(rows)):
            if row == output or not rows[row][column] % prime:
                continue
            factor = rows[row][column]
            rows[row] = [
                (entry - factor * base) % prime
                for entry, base in zip(rows[row], rows[output])
            ]
        output += 1
    return output


def check(points: list[int], s: int, values: list[int], prime: int, puncture=None):
    n = len(points)
    r = n - s
    vandermonde = [[pow(x, degree, prime) for x in points] for degree in range(s)]
    lower = [
        [values[index] * pow(x, degree, prime) % prime for index, x in enumerate(points)]
        for degree in range(s)
    ]
    matrix = vandermonde + lower
    interpolation_rows = []
    for index, x in enumerate(points):
        if index == puncture:
            continue
        interpolation_rows.append(
            [
                values[index] * pow(x, degree, prime) % prime
                for degree in range(r)
            ]
            + [(-pow(x, degree, prime)) % prime for degree in range(r)]
        )

    if puncture is None:
        full_matrix = rank(matrix, prime) == n
    else:
        clone = [0] * s + [pow(points[puncture], degree, prime) for degree in range(s)]
        augmented = [row[:] for row in matrix]
        for row_index, value in enumerate(clone):
            augmented[row_index].append(value)
        full_matrix = rank(augmented, prime) == n + 1
    rational_certificate = rank(interpolation_rows, prime) < 2 * r
    assert full_matrix == (not rational_certificate)


def main() -> None:
    prime = 101
    for r in (1, 2, 3, 4):
        s = 5
        points = list(range(1, s + r + 1))
        if r == 1:
            rational = [3 for _ in points]
        else:
            rational = [
                (3 * x + 4) * inverse(x + 7, prime) % prime for x in points
            ]
        check(points, s, rational, prime)
        check(points, s, rational, prime, puncture=len(points) - 1)

        # If Q=P*X^r at these points, Q-P*X^r has more roots than its
        # degree because r<s. Hence this datum has no allowed certificate.
        nonrational = [pow(x, r, prime) for x in points]
        check(points, s, nonrational, prime)
        check(points, s, nonrational, prime, puncture=len(points) - 1)

    print(
        "RATE_HALF_BIVARIATE_SINGLE_COEFFICIENT_RATIONAL_INTERPOLATION_"
        "CRITERION_PASS cases=16"
    )


if __name__ == "__main__":
    main()
