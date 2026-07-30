#!/usr/bin/env python3
"""Independent exact-rational replay of the two q-slice mismatches."""

from fractions import Fraction as F


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def trim(poly):
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def add(left, right):
    return trim([
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(max(len(left), len(right)))
    ])


def scale(poly, scalar):
    return trim([scalar * value for value in poly])


def multiply(left, right):
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(result)


def evaluate(poly, point):
    result = F(0)
    for value in reversed(poly):
        result = result * point + value
    return result


def divide_exact(dividend, divisor):
    work = trim(dividend)
    quotient = [F(0)] * (len(work) - len(divisor) + 1)
    while len(work) >= len(divisor) and work != [0]:
        shift = len(work) - len(divisor)
        coefficient = work[-1] / divisor[-1]
        quotient[shift] = coefficient
        for i, value in enumerate(divisor):
            work[i + shift] -= coefficient * value
        work = trim(work)
    require(work == [0], "polynomial division")
    return trim(quotient)


def monic(poly):
    return scale(poly, 1 / poly[-1])


def solve_unique(matrix, target):
    rows = [list(row) + [rhs] for row, rhs in zip(matrix, target)]
    columns = len(matrix[0])
    pivot_columns = []
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, len(rows))
                      if rows[row][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        value = rows[pivot_row][column]
        rows[pivot_row] = [entry / value for entry in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row:
                continue
            value = rows[row][column]
            if value:
                rows[row] = [left - value * right
                             for left, right in zip(rows[row], rows[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
    require(not any(all(value == 0 for value in row[:columns]) and row[-1]
                    for row in rows), "reconstruction consistency")
    require(len(pivot_columns) == columns, "reconstruction uniqueness")
    solution = [F(0)] * columns
    for row, column in enumerate(pivot_columns):
        solution[column] = rows[row][-1]
    return solution


def edge(left, right):
    return [left * right, -(left + right), F(1)]


def mismatch(template, c, d, w):
    a = F(2)
    p = c * d - 2 * c - 2 * d + 1
    q = 2 * c * d - c - d + 2
    require(p, "B-locus denominator")
    b = -q / p
    q0, q1 = c * d, -(c + d)
    f, g, m = q0 + w, -1 - w * q0, q1 * (1 + w)
    numerator = f + m * a - g * a * a
    denominator = g - m * a - f * a * a
    require(denominator, "incidence denominator")
    z = -numerator / denominator
    labels = (a, 1 / a, b, 1 / b, c, 1 / c,
              d, 1 / d, w, 1 / w, z, 1 / z)
    require(len(set(labels)) == 12, "fixture label distinctness")
    v = ([f, g], [m, -m], [-g, -f])
    vz = [evaluate(poly, z) for poly in v]
    l1, l0 = vz[2], vz[1] + a * vz[2]

    if template == "fixed-moving":
        first, second, r, s = edge(a, 1 / a), edge(a, b), 1 / a, b
    else:
        first, second, r, s = edge(a, b), edge(a, 1 / b), b, 1 / b
    target = [
        ((l0 + s * l1) * first[i] + (l0 + r * l1) * second[i]) / (s - r)
        for i in range(3)
    ]

    matrix = [
        [1 + q0 * w * w, w * (1 + q0), w * w + q0, 0],
        [q1 * w * w, q1 * w, q1, 1 - w * w],
        [1, z, z * z, 0],
        [0, 0, 0, 1 - z * z],
        [-z * z, -z, -1, 0],
    ]
    x0, x1, x2, x3 = solve_unique(
        matrix, [F(0), F(0), target[0], target[1], target[2]]
    )
    u = ([x0, x1, x2], [x3, 0, -x3], [-x2, -x1, -x0])

    residuals = []
    for root in (c, d):
        u_root = add(add(u[0], scale(u[1], root)), scale(u[2], root * root))
        v_root = add(add(v[0], scale(v[1], root)), scale(v[2], root * root))
        norm = add(multiply(u_root, u_root),
                   scale([0] + multiply(v_root, v_root), -1))
        residuals.append(divide_exact(norm, [w * w, -2 * w, 1]))
    observed = monic(multiply(*residuals))
    crossing = multiply([-1 / c, 1], [-1 / d, 1])
    expected = monic(multiply(crossing, crossing))
    return add(observed, scale(expected, -1))


def main() -> None:
    generic = ((F(3), F(7), F(5)), (F(4), F(6), F(9)))
    special = ((F(3), F(-1, 3), F(5)), (F(4), F(-1, 4), F(7)))
    checked = 0
    for template in ("fixed-moving", "moving-moving"):
        for c, d, w in generic:
            values = mismatch(template, c, d, w)
            require(values[0] == (c * d - 1) * (c * d + 1) / (c * c * d * d),
                    "constant mismatch identity")
            checked += 1
        for c, d, w in special:
            values = mismatch(template, c, d, w)
            require(values[1] - values[3] == 4 * (c * c - 1) / c,
                    "outer mismatch identity")
            checked += 1

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SOURCE_LINE_ALIGNED_NEGATIVE_Q_SLICE_EXCLUSION_AUDIT_PASS "
        f"exact_fixtures={checked} templates=2 identities=constant/outer"
    )


if __name__ == "__main__":
    main()
