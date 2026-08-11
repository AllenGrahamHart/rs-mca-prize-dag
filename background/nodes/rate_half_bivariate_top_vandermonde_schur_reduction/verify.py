#!/usr/bin/env python3
"""Check top-slice rank and Schur rank identities on synthetic matrices."""


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


def inverse_matrix(matrix: list[list[int]], prime: int) -> list[list[int]]:
    size = len(matrix)
    rows = [
        matrix[row][:] + [int(row == column) for column in range(size)]
        for row in range(size)
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size) if rows[row][column] % prime)
        rows[column], rows[pivot] = rows[pivot], rows[column]
        scale = inverse(rows[column][column], prime)
        rows[column] = [entry * scale % prime for entry in rows[column]]
        for row in range(size):
            if row == column or not rows[row][column] % prime:
                continue
            factor = rows[row][column]
            rows[row] = [
                (entry - factor * base) % prime
                for entry, base in zip(rows[row], rows[column])
            ]
    return [row[size:] for row in rows]


def multiply(left: list[list[int]], right: list[list[int]], prime: int):
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right))) % prime
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def subtract(left: list[list[int]], right: list[list[int]], prime: int):
    return [
        [(a - b) % prime for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def synthetic_matrix(m: int, points: list[int], deficits: list[int], prime: int):
    columns = []
    highest = []
    for point, deficit in zip(points, deficits):
        degree = m - deficit
        roots = [((point + 3 * index) % prime) for index in range(degree)]
        poly = [1]
        for root in roots:
            updated = [0] * (len(poly) + 1)
            for index, value in enumerate(poly):
                updated[index] = (updated[index] - root * value) % prime
                updated[index + 1] = (updated[index + 1] + value) % prime
            poly = updated
        linear = [(-2 * point) % prime, 1]
        base = [0] * (len(poly) + 1)
        for i, a in enumerate(poly):
            for j, b in enumerate(linear):
                base[i + j] = (base[i + j] + a * b) % prime
        block = []
        for clone in range(deficit + 1):
            block.append(len(columns))
            columns.append((point, [0] * clone + base))
        highest.append(block[-1])

    matrix = []
    for moment in range(4 * m + 1):
        for parameter_degree in range(m + 2):
            matrix.append(
                [
                    pow(point, moment, prime)
                    * (poly[parameter_degree] if parameter_degree < len(poly) else 0)
                    % prime
                    for point, poly in columns
                ]
            )
    return matrix, highest


def check_case(m: int, points: list[int], deficits: list[int], prime: int) -> None:
    matrix, highest = synthetic_matrix(m, points, deficits, prime)
    top_rows = [moment * (m + 2) + (m + 1) for moment in range(4 * m + 1)]
    pivot_columns = highest[: 4 * m + 1]
    residual_columns = [
        column for column in range(len(matrix[0])) if column not in pivot_columns
    ]
    lower_rows = [row for row in range(len(matrix)) if row not in top_rows]

    v = [[matrix[row][column] for column in pivot_columns] for row in top_rows]
    b = [[matrix[row][column] for column in residual_columns] for row in top_rows]
    c = [[matrix[row][column] for column in pivot_columns] for row in lower_rows]
    d = [[matrix[row][column] for column in residual_columns] for row in lower_rows]
    schur = subtract(d, multiply(multiply(c, inverse_matrix(v, prime), prime), b, prime), prime)

    assert rank(v, prime) == 4 * m + 1
    assert len(residual_columns) == len(points) + sum(deficits) - (4 * m + 1)
    assert rank(matrix, prime) == 4 * m + 1 + rank(schur, prime)


def main() -> None:
    check_case(1, [1, 2, 3, 4, 5, 6], [0] * 6, 101)
    check_case(2, list(range(1, 13)), [1] + [0] * 11, 193)
    check_case(3, list(range(1, 19)), [0, 1, 2] + [0] * 15, 257)
    print("RATE_HALF_BIVARIATE_TOP_VANDERMONDE_SCHUR_REDUCTION_PASS cases=3")


if __name__ == "__main__":
    main()
