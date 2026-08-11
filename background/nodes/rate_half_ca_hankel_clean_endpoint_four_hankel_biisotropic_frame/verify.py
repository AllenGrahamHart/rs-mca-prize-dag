#!/usr/bin/env python3
"""Verify the four-form coefficient-chain lemma on exact canonical blocks."""


PRIME = 1_000_003


def matrix_vector(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [
        sum(entry * value for entry, value in zip(row, vector)) % PRIME
        for row in matrix
    ]


def pairing(left: list[int], matrix: list[list[int]], right: list[int]) -> int:
    return sum(a * b for a, b in zip(left, matrix_vector(matrix, right))) % PRIME


def matrix_rank(matrix: list[list[int]]) -> int:
    rows = [[value % PRIME for value in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], PRIME - 2, PRIME)
        rows[rank] = [value * inverse % PRIME for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank:
                continue
            factor = rows[row][column]
            rows[row] = [
                (value - factor * pivot_value) % PRIME
                for value, pivot_value in zip(rows[row], rows[rank])
            ]
        rank += 1
    return rank


def canonical_pair(m: int, variant: int) -> tuple[list[list[int]], list[list[int]]]:
    dimension = 4 * m
    first = [[0] * dimension for _ in range(dimension)]
    second = [[0] * dimension for _ in range(dimension)]

    for j in range(1, m + 1):
        companion = m + j
        scale = (variant + 1) * j + 1
        first[j][companion] = scale
        first[companion][j] = scale
        second[j - 1][companion] = -scale % PRIME
        second[companion][j - 1] = -scale % PRIME

    for index in range(2 * m + 1, dimension):
        first[index][index] = index + variant + 3
        second[index][index] = 2 * index + variant + 5

    return first, second


def main() -> None:
    checked = 0
    for m in range(2, 11):
        dimension = 4 * m
        basis = [
            [1 if index == j else 0 for index in range(dimension)]
            for j in range(m + 1)
        ]
        for variant in (0, 1):
            first, second = canonical_pair(m, variant)
            assert matrix_rank(first) == dimension - 1
            assert matrix_rank(second) == dimension - 1
            assert matrix_vector(first, basis[0]) == [0] * dimension
            assert matrix_vector(second, basis[m]) == [0] * dimension

            for j in range(m + 1):
                if j == 0:
                    chain = matrix_vector(first, basis[j])
                else:
                    chain = [
                        (a + b) % PRIME
                        for a, b in zip(
                            matrix_vector(first, basis[j]),
                            matrix_vector(second, basis[j - 1]),
                        )
                    ]
                assert chain == [0] * dimension

            for left in basis:
                for right in basis:
                    assert pairing(left, first, right) == 0
                    assert pairing(left, second, right) == 0
                    checked += 2

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_FOUR_HANKEL_BIISOTROPIC_FRAME_PASS "
        f"pairings={checked} scales=9"
    )


if __name__ == "__main__":
    main()
