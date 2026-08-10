#!/usr/bin/env python3
"""Small exact Cauchy-Binet cofactor audit over a prime field."""


from itertools import combinations


P = 101


def det(matrix):
    a = [[value % P for value in row] for row in matrix]
    value = 1
    for col in range(len(a)):
        pivot = next((row for row in range(col, len(a)) if a[row][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            value = -value
        pivot_value = a[col][col] % P
        value = value * pivot_value % P
        inverse = pow(pivot_value, P - 2, P)
        for row in range(col + 1, len(a)):
            factor = a[row][col] * inverse % P
            for j in range(col, len(a)):
                a[row][j] = (a[row][j] - factor * a[col][j]) % P
    return value % P


def matrix_rank(matrix, prime):
    rows = [[value % prime for value in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next(
            (row for row in range(rank, len(rows)) if rows[row][column]),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], prime - 2, prime)
        rows[rank] = [value * inverse % prime for value in rows[rank]]
        for row in range(len(rows)):
            if row == rank:
                continue
            factor = rows[row][column]
            rows[row] = [
                (value - factor * pivot_value) % prime
                for value, pivot_value in zip(rows[row], rows[rank])
            ]
        rank += 1
    return rank


def main():
    n = 4
    points = [1, 2, 4, 7, 11, 16]
    weights = [3, 5, 8, 13, 21, 34]
    v = [[pow(x, i, P) for x in points] for i in range(n)]
    matrix = [
        [sum(v[i][k] * weights[k] * v[j][k] for k in range(len(points))) % P
         for j in range(n)]
        for i in range(n)
    ]

    checks = 0
    for i in range(n):
        for j in range(n):
            minor = [
                [matrix[row][col] for col in range(n) if col != i]
                for row in range(n) if row != j
            ]
            left = ((-1) ** (i + j) * det(minor)) % P
            right = 0
            for chosen in combinations(range(len(points)), n - 1):
                rows_j = [[v[row][k] for k in chosen] for row in range(n) if row != j]
                rows_i = [[v[row][k] for k in chosen] for row in range(n) if row != i]
                product = 1
                for k in chosen:
                    product = product * weights[k] % P
                right += ((-1) ** (i + j)) * det(rows_j) * det(rows_i) * product
            assert left == right % P
            checks += 1

    # Exact m=1, F_17 boundary fixture: x_0=14 is the unique missing row.
    # The marked rank drop and Q(-;x_0) root both occur at infinity.
    prime = 17
    y0 = (1, 10, 16, 2, 14, 0, 3, 11)
    y1 = (0, 14, 9, 7, 13, 12, 15, 0)
    q0 = (7, 0, 9, 1)
    q1 = (0, 12, 4, 0)
    x0 = 14
    assert sum(q1[i] * pow(x0, i, prime) for i in range(4)) % prime == 0
    assert sum(q0[i] * pow(x0, i, prime) for i in range(4)) % prime != 0
    marked_infinity = [
        [(y1[i + j + 1] - x0 * y1[i + j]) % prime for j in range(4)]
        for i in range(4)
    ]
    assert matrix_rank(marked_infinity, prime) == 2
    for t in range(prime):
        y = [(a + t * b) % prime for a, b in zip(y0, y1)]
        marked = [
            [(y[i + j + 1] - x0 * y[i + j]) % prime for j in range(4)]
            for i in range(4)
        ]
        assert matrix_rank(marked, prime) == 3

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_MARKED_ADJUGATE_SUBSET_LEDGER_AUDIT_PASS "
        f"cofactors={checks} subsets={len(list(combinations(points, n - 1)))} "
        "fixture=F17_m1_infinity"
    )


if __name__ == "__main__":
    main()
