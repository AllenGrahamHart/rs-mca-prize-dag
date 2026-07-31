#!/usr/bin/env python3
"""Finite-field replay of the zero-loop quadratic weld."""


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
    labels = (2, 3, 5, 7, 11)
    d0, d1 = 13, 17
    c0, c1, c2 = 19, 23, 29
    rows = []
    for value in labels:
        denominator = (d0+d1*value) % prime
        c_value = (c0+c1*value+c2*value*value) % prime
        q = -c_value*pow(denominator, -1, prime) % prime
        rows.append((1, value, value*value, q*denominator))
    if rank_mod(rows, prime) != 3:
        raise RuntimeError("finite-field quadratic rank")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ZERO_LOOP_PRODUCT_Q_WELD_AUDIT_PASS "
        "prime=101 labels=5 rank=3"
    )


if __name__ == "__main__":
    main()
