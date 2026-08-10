#!/usr/bin/env python3
"""Replay the four Hankel chains on the exact F_17 m=1 witness."""


PRIME = 17
Y_0 = (1, 10, 16, 2, 14, 0, 3, 11)
Y_1 = (0, 14, 9, 7, 13, 12, 15, 0)
Q_0 = (7, 0, 9, 1)
Q_1 = (0, 12, 4, 0)


def matrix_vector(matrix: list[list[int]], vector: tuple[int, ...]) -> list[int]:
    return [
        sum(entry * value for entry, value in zip(row, vector)) % PRIME
        for row in matrix
    ]


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


def add_scaled(first: tuple[int, ...], second: tuple[int, ...], scale: int) -> tuple[int, ...]:
    return tuple((a + scale * b) % PRIME for a, b in zip(first, second))


def main() -> None:
    # Send the generic old slopes 3 and 5 to the two homogeneous endpoints.
    y_left = add_scaled(Y_0, Y_1, 3)
    y_right = add_scaled(Y_0, Y_1, 5)
    q_left = add_scaled(Q_0, Q_1, 3)
    q_right = add_scaled(Q_0, Q_1, 5)
    zero = [0] * 4
    checked = 0

    for epsilon in (0, 1):
        left = [
            [y_left[row + column + epsilon] for column in range(4)]
            for row in range(4)
        ]
        right = [
            [y_right[row + column + epsilon] for column in range(4)]
            for row in range(4)
        ]
        assert matrix_rank(left) == 3
        assert matrix_rank(right) == 3
        assert matrix_vector(left, q_left) == zero
        assert matrix_vector(right, q_right) == zero
        assert [
            (a + b) % PRIME
            for a, b in zip(
                matrix_vector(left, q_right),
                matrix_vector(right, q_left),
            )
        ] == zero

        for q_a in (q_left, q_right):
            for q_b in (q_left, q_right):
                for matrix in (left, right):
                    assert sum(
                        a * b for a, b in zip(q_a, matrix_vector(matrix, q_b))
                    ) % PRIME == 0
                    checked += 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_FOUR_HANKEL_BIISOTROPIC_FRAME_"
        f"AUDIT_PASS witness=F17_m1 pairings={checked}"
    )


if __name__ == "__main__":
    main()
