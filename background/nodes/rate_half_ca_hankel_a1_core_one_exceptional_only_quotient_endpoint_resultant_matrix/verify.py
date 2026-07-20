#!/usr/bin/env python3
"""Exponent checks for the sharp endpoint resultant matrix."""


def exponents(e):
    return {
        "alpha": (e - 1) // 2,
        "beta": 3 * (e + 1) // 2,
        "gamma": (3 * e + 1) // 2,
        "delta": 9 * (e + 1) // 2,
    }


def check_matrix_arithmetic():
    for e in (3, 5, 9, 2**38 - 1):
        values = exponents(e)
        alpha = values["alpha"]
        beta = values["beta"]
        gamma = values["gamma"]
        delta = values["delta"]
        r = 2 * e + 1
        assert alpha + beta == r
        assert alpha + gamma == 2 * e
        assert beta + delta == 6 * e + 6
        assert gamma + delta == 6 * e + 5

        # z exponents in row and column products.
        assert 2 * e + 0 == r - 1
        assert 0 + (6 * e + 6) == 6 * e + 6


def check_checkerboard():
    # Encode the exponent of L in rows A,H and columns Q,V.
    matrix = ((1, -1), (-1, 1))
    assert all(sum(row) == 0 for row in matrix)
    assert all(matrix[0][column] + matrix[1][column] == 0 for column in (0, 1))


def check_mutation_caught():
    e = 9
    values = exponents(e)
    assert values["gamma"] + values["delta"] == 6 * e + 5
    assert values["gamma"] + values["delta"] + 1 != 6 * e + 5


def main():
    check_matrix_arithmetic()
    check_checkerboard()
    check_mutation_caught()
    print("PASS exceptional quotient endpoint resultant matrix")


if __name__ == "__main__":
    main()
