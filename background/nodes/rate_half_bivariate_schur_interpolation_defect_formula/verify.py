#!/usr/bin/env python3
"""Compare direct Schur elimination with the interpolation-defect formula."""


def inverse(value: int, prime: int) -> int:
    return pow(value % prime, prime - 2, prime)


def poly_multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] = (output[i + j] + a * b) % prime
    return output


def invert_matrix(matrix: list[list[int]], prime: int) -> list[list[int]]:
    size = len(matrix)
    rows = [
        matrix[row][:] + [int(row == column) for column in range(size)]
        for row in range(size)
    ]
    for column in range(size):
        pivot = next(row for row in range(column, size) if rows[row][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        scale = inverse(rows[column][column], prime)
        rows[column] = [entry * scale % prime for entry in rows[column]]
        for row in range(size):
            if row == column or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [
                (entry - factor * base) % prime
                for entry, base in zip(rows[row], rows[column])
            ]
    return [row[size:] for row in rows]


def matrix_product(left: list[list[int]], right: list[list[int]], prime: int):
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(len(right))) % prime
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def lagrange_weight(points: list[int], pivot: int, value: int, prime: int) -> int:
    numerator = 1
    denominator = 1
    for point in points:
        if point == pivot:
            continue
        numerator = numerator * (value - point) % prime
        denominator = denominator * (pivot - point) % prime
    return numerator * inverse(denominator, prime) % prime


def check_case(m: int, points: list[int], deficits: list[int], prime: int) -> None:
    columns = []
    blocks = []
    highest_polys = {}
    leading = {}
    for point, deficit in zip(points, deficits):
        roots = tuple((point + 2 + 3 * index) % prime for index in range(m - deficit))
        mu = (5 * point + 1) % prime
        c1 = (7 * point + 3) % prime or 1
        linear = [(-c1 * mu) % prime, c1]
        root_poly = [1]
        for root in roots:
            root_poly = poly_multiply(root_poly, [(-root) % prime, 1], prime)
        base = poly_multiply(linear, root_poly, prime)
        block = []
        for clone in range(deficit + 1):
            block.append(len(columns))
            columns.append((point, clone, [0] * clone + base))
        blocks.append(block)
        highest_polys[point] = [entry * inverse(c1, prime) % prime for entry in columns[block[-1]][2]]
        leading[point] = c1

    matrix = []
    for moment in range(4 * m + 1):
        for parameter_degree in range(m + 2):
            matrix.append(
                [
                    pow(point, moment, prime)
                    * (poly[parameter_degree] if parameter_degree < len(poly) else 0)
                    % prime
                    for point, _, poly in columns
                ]
            )

    size = 4 * m + 1
    pivot_points = points[:size]
    pivot_columns = [blocks[index][-1] for index in range(size)]
    residual_columns = [index for index in range(len(columns)) if index not in pivot_columns]
    top_rows = [moment * (m + 2) + m + 1 for moment in range(size)]
    lower_rows = [row for row in range(len(matrix)) if row not in top_rows]
    v = [[matrix[row][column] for column in pivot_columns] for row in top_rows]
    b = [[matrix[row][column] for column in residual_columns] for row in top_rows]
    c = [[matrix[row][column] for column in pivot_columns] for row in lower_rows]
    d = [[matrix[row][column] for column in residual_columns] for row in lower_rows]
    correction = matrix_product(matrix_product(c, invert_matrix(v, prime), prime), b, prime)
    direct = [
        [(entry - correction[row][column]) % prime for column, entry in enumerate(values)]
        for row, values in enumerate(d)
    ]

    formula = []
    for residual_column in residual_columns:
        point, clone, poly = columns[residual_column]
        is_highest = residual_column == blocks[points.index(point)][-1]
        values = []
        for moment in range(size):
            for parameter_degree in range(m + 1):
                if not is_highest:
                    value = pow(point, moment, prime) * (
                        poly[parameter_degree] if parameter_degree < len(poly) else 0
                    )
                else:
                    h_x = highest_polys[point][parameter_degree]
                    interpolated = sum(
                        lagrange_weight(pivot_points, pivot, point, prime)
                        * pow(pivot, moment, prime)
                        * highest_polys[pivot][parameter_degree]
                        for pivot in pivot_points
                    )
                    value = leading[point] * (
                        pow(point, moment, prime) * h_x - interpolated
                    )
                values.append(value % prime)
        formula.append(values)

    transposed_direct = [
        [direct[row][column] for row in range(len(direct))]
        for column in range(len(residual_columns))
    ]
    assert formula == transposed_direct


def main() -> None:
    check_case(1, [1, 2, 3, 4, 5, 6], [0] * 6, 101)
    check_case(2, list(range(1, 13)), [1] + [0] * 11, 193)
    check_case(3, list(range(1, 19)), [0, 1, 2] + [0] * 15, 257)
    print("RATE_HALF_BIVARIATE_SCHUR_INTERPOLATION_DEFECT_FORMULA_PASS cases=3")


if __name__ == "__main__":
    main()
