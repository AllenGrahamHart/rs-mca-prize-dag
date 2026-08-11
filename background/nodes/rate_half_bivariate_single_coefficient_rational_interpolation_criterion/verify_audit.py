#!/usr/bin/env python3
"""Independent explicit examples for the rational rank criterion."""


def matrix_rank(rows, prime):
    rows = [list(row) for row in rows]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column] % prime),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = pow(rows[rank][column], prime - 2, prime)
        rows[rank] = [value * scale % prime for value in rows[rank]]
        for row in range(rank + 1, len(rows)):
            factor = rows[row][column]
            if factor:
                rows[row] = [
                    (value - factor * base) % prime
                    for value, base in zip(rows[row], rows[rank])
                ]
        rank += 1
    return rank


def two_block(points, values, s, prime):
    return [
        [pow(x, degree, prime) for x in points] for degree in range(s)
    ] + [
        [value * pow(x, degree, prime) % prime for x, value in zip(points, values)]
        for degree in range(s)
    ]


def main() -> None:
    prime = 97
    points = [1, 2, 3, 4, 5, 6, 7]
    s = 5
    # r=2: h=(2X+3)/(X+4) supplies an exact certificate.
    rational = [(2 * x + 3) * pow(x + 4, prime - 2, prime) % prime for x in points]
    assert matrix_rank(two_block(points, rational, s, prime), prime) == 6 < 7

    # Cubic data do not admit numerator/denominator degree below two here.
    nonrational = [(x**3 + x + 1) % prime for x in points]
    assert matrix_rank(two_block(points, nonrational, s, prime), prime) == 7

    # Puncturing the last point and adding its clone preserves the rational
    # failure and can turn a one-point-corrupted rational datum into failure.
    corrupted = rational[:]
    corrupted[-1] = (corrupted[-1] + 1) % prime
    matrix = two_block(points, corrupted, s, prime)
    clone = [0] * s + [pow(points[-1], degree, prime) for degree in range(s)]
    augmented = [row + [clone[index]] for index, row in enumerate(matrix)]
    assert matrix_rank(augmented, prime) < len(points) + 1

    print(
        "RATE_HALF_BIVARIATE_SINGLE_COEFFICIENT_RATIONAL_INTERPOLATION_"
        "CRITERION_AUDIT_PASS examples=3"
    )


if __name__ == "__main__":
    main()
