#!/usr/bin/env python3
"""Finite-field witness audit of the constrained forced-mate formulas."""


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
    examples = (
        ("X2", 31, 22, 23, 0),
        ("N1", 31, 22, 4, 0),
        ("L1", 113, 15, 23, 74),
    )
    for name, prime, m, c, ell in examples:
        b = -c**3 % prime
        labels = {
            "X2": (-m*m, m, 1, m*m, -m),
            "N1": (-1, m, 1, m*m, -m),
            "L1": (ell, m, 1, -1, -m),
        }[name]
        products = (-1, -c*c, b, -b, b*c)
        xi = {"X2": -1, "N1": -m*m, "L1": -ell}[name] % prime
        if name == "X2":
            numerator = (-2*m**3*c + 3*m**3 - 16*m*m*c + 24*m*m
                         + 6*m*c - 9*m - 36*c + 32)
            forced = numerator * pow(22, -1, prime) % prime
        elif name == "N1":
            numerator = (2*m**3*c + 3*m**3 + 16*m*m*c + 24*m*m
                         - 6*m*c - 9*m + 36*c + 32)
            forced = numerator * pow(22, -1, prime) % prime
        else:
            forced = (3*c*c + 10) * pow(8, -1, prime) % prime
        common = [[-value, -value*label, 1, label]
                  for label, value in zip(labels, products)]
        candidate = [-forced, -forced*xi, 1, xi]
        if rank_mod(common, prime) != 3 or rank_mod((*common, candidate), prime) != 3:
            raise RuntimeError(f"witness Mobius rank {name}")
        if forced == 0:
            raise RuntimeError(f"witness forced nonzero {name}")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_CONSTRAINED_OUTSIDE_AUDIT_PASS "
        "finite_field_rows=3 mobius_ranks=3 forced_values=nonzero"
    )


if __name__ == "__main__":
    main()
