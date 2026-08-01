#!/usr/bin/env python3
"""Finite-field replay of the one-loop affine-line weld."""


def rank_mod(matrix, prime):
    matrix = [[value % prime for value in row] for row in matrix]
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(rank, len(matrix))
                      if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], -1, prime)
        matrix[rank] = [value*inverse % prime for value in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank:
                continue
            scalar = matrix[row][column]
            matrix[row] = [
                (matrix[row][index] - scalar*matrix[rank][index]) % prime
                for index in range(len(matrix[0]))
            ]
        rank += 1
    return rank


def main():
    prime = 101
    h = 2
    labels = (3, 5, 7, 11)
    n0, n1, d0, d1 = 13, 17, 19, 23
    c0, c1 = 29, 31

    def p(value):
        return (n0+n1*value)*pow(d0+d1*value, -1, prime) % prime

    rows = []
    for value in labels:
        q = -(value-h)*(c0+c1*value)*pow(d0+d1*value, -1, prime) % prime
        w = q*pow(p(h)-p(value), -1, prime) % prime
        rows.append((1, value, w))
    if rank_mod(rows, prime) != 2:
        raise RuntimeError("finite-field affine-line rank")
    for third in labels[2:]:
        if rank_mod((rows[0], rows[1], rows[labels.index(third)]), prime) != 2:
            raise RuntimeError("finite-field scalar weld")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_PRODUCT_Q_WELD_AUDIT_PASS "
        "prime=101 nonloops=4 rank=2"
    )


if __name__ == "__main__":
    main()
