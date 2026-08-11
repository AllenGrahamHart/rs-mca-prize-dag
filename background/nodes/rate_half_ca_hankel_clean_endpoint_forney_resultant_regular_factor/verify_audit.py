#!/usr/bin/env python3
"""Exact F_17 replay of the canonical numerator and resultant."""


P_FIELD = 17
Y_0 = (1, 10, 16, 2, 14, 0, 3, 11)
Y_1 = (0, 14, 9, 7, 13, 12, 15, 0)
Q_0 = (7, 0, 9, 1)
Q_1 = (0, 12, 4, 0)
RHO = 3


def polymul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P_FIELD
    return out


def det(matrix):
    a = [[value % P_FIELD for value in row] for row in matrix]
    value = 1
    for column in range(len(a)):
        pivot = next(
            (row for row in range(column, len(a)) if a[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            a[column], a[pivot] = a[pivot], a[column]
            value = -value
        pivot_value = a[column][column]
        value = value * pivot_value % P_FIELD
        inverse = pow(pivot_value, P_FIELD - 2, P_FIELD)
        for row in range(column + 1, len(a)):
            factor = a[row][column] * inverse % P_FIELD
            for j in range(column, len(a)):
                a[row][j] = (a[row][j] - factor * a[column][j]) % P_FIELD
    return value % P_FIELD


def resultant(first, second):
    m = len(first) - 1
    n = len(second) - 1
    rows = []
    for shift in range(n):
        row = [0] * (m + n)
        for i, coefficient in enumerate(reversed(first)):
            row[shift + i] = coefficient
        rows.append(row)
    for shift in range(m):
        row = [0] * (m + n)
        for i, coefficient in enumerate(reversed(second)):
            row[shift + i] = coefficient
        rows.append(row)
    return det(rows)


def main():
    values = []
    for t in range(P_FIELD):
        y = [(a + t * b) % P_FIELD for a, b in zip(Y_0, Y_1)]
        q = [(a + t * b) % P_FIELD for a, b in zip(Q_0, Q_1)]
        reciprocal = list(reversed(q))
        numerator_z = polymul(reciprocal, list(y[:RHO]))[:RHO]
        numerator_x = list(reversed(numerator_z))
        assert len(numerator_x) == RHO
        values.append(resultant(q, numerator_x))

    assert values == [12] * P_FIELD
    mutated = list(values)
    mutated[9] = (mutated[9] + 1) % P_FIELD
    assert len(set(mutated)) > 1
    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_FORNEY_RESULTANT_REGULAR_FACTOR_AUDIT_PASS "
        f"fixture=F17_m1 parameters={P_FIELD} resultant={values[0]}"
    )


if __name__ == "__main__":
    main()
