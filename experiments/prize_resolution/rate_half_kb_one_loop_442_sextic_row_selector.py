#!/usr/bin/env python3
"""Select three unit-independent sextic eigenvalue rows in one sign quotient."""

import argparse
import importlib.util
import itertools
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MATE_PATH = ROOT / (
    "background/nodes/"
    "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_"
    "nonloop_singleton_sextic_mate_coordinate_compiler/verify.py"
)
SPEC = importlib.util.spec_from_file_location("mate", MATE_PATH)
MATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MATE)
P = MATE.PARENT.PRIME
SIZE = 6


def add(left, right):
    return [[(left[i][j]+right[i][j]) % P for j in range(SIZE)]
            for i in range(SIZE)]


def neg(value):
    return [[-value[i][j] % P for j in range(SIZE)]
            for i in range(SIZE)]


def sub(left, right):
    return add(left, neg(right))


def scale(scalar, value):
    return [[scalar*value[i][j] % P for j in range(SIZE)]
            for i in range(SIZE)]


def mul(left, right):
    return [[sum(left[i][k]*right[k][j] for k in range(SIZE)) % P
             for j in range(SIZE)] for i in range(SIZE)]


IDENTITY = [[int(i == j) for j in range(SIZE)] for i in range(SIZE)]
ZERO = [[0 for _ in range(SIZE)] for _ in range(SIZE)]


def power(value, exponent):
    result = IDENTITY
    base = value
    while exponent:
        if exponent & 1:
            result = mul(result, base)
        base = mul(base, base)
        exponent //= 2
    return result


def det_mod(value):
    work = [row[:] for row in value]
    determinant = 1
    for column in range(SIZE):
        pivot = next((row for row in range(column, SIZE)
                      if work[row][column] % P), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            determinant = -determinant
        pivot_value = work[column][column] % P
        determinant = determinant*pivot_value % P
        inverse = pow(pivot_value, -1, P)
        for row in range(column+1, SIZE):
            factor = work[row][column]*inverse % P
            for index in range(column, SIZE):
                work[row][index] = (
                    work[row][index]-factor*work[column][index]
                ) % P
    return determinant % P


def kdet3(entries):
    a, b, c = entries[0]
    d, e, f = entries[1]
    g, h, i = entries[2]
    return add(
        sub(mul(a, sub(mul(e, i), mul(f, h))),
            mul(b, sub(mul(d, i), mul(f, g)))),
        mul(c, sub(mul(d, h), mul(e, g))),
    )


def as_lists(matrix):
    return [[int(matrix[i, j]) % P for j in range(SIZE)]
            for i in range(SIZE)]


def build_action(epsilon_1, epsilon_2):
    b, r, t, d_c, vector, polynomial, matrix = MATE.quotient_data(
        epsilon_1, epsilon_2
    )
    x = r**2
    a_poly = x**2-6*x+1
    b_poly = (x+1)**2
    c_numerator = b*(b*a_poly+b_poly)
    c_coordinates = matrix(d_c).inv_mod(P)*vector(c_numerator)
    c_value = polynomial(c_coordinates % P)

    b_matrix = as_lists(matrix(b))
    c_matrix = as_lists(matrix(c_value))
    b_squared = mul(b_matrix, b_matrix)
    alpha = neg(mul(b_matrix, add(c_matrix, b_squared)))
    beta = mul(b_squared, sub(sub(c_matrix, b_squared),
                             scale(2, mul(b_matrix, c_matrix))))
    gamma = sub(add(c_matrix, scale(2, b_matrix)), b_squared)
    delta = add(mul(alpha, alpha), mul(beta, gamma))
    delta_cubed = power(delta, 3)

    powers = {
        "a": [power(alpha, exponent) for exponent in range(7)],
        "b": [power(beta, exponent) for exponent in range(7)],
        "g": [power(gamma, exponent) for exponent in range(7)],
    }
    action = [[ZERO for _ in range(7)] for _ in range(7)]
    for ell in range(7):
        for j in range(7):
            value = ZERO
            for q in range(max(0, ell-(6-j)), min(ell, j)+1):
                p = ell-q
                term = mul(
                    mul(powers["a"][6-j-p], powers["b"][p]),
                    mul(powers["g"][j-q], powers["a"][q]),
                )
                scalar = math.comb(6-j, p)*math.comb(j, q)
                if q % 2:
                    scalar = -scalar
                value = add(value, scale(scalar, term))
            if ell == j:
                value = sub(value, delta_cubed)
            action[ell][j] = value
    return action


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("epsilon_1", type=int, choices=(-1, 1))
    parser.add_argument("epsilon_2", type=int, choices=(-1, 1))
    arguments = parser.parse_args()

    action = build_action(arguments.epsilon_1, arguments.epsilon_2)
    for rows in itertools.combinations(range(7), 3):
        for columns in itertools.combinations(range(7), 3):
            minor = [[action[row][column] for column in columns]
                     for row in rows]
            norm = det_mod(kdet3(minor))
            if norm:
                print(
                    "SEXTIC_ROW_SELECTOR_PASS "
                    f"signs={arguments.epsilon_1},{arguments.epsilon_2} "
                    f"rows={rows} columns={columns} norm={norm}"
                )
                return
    raise RuntimeError("no unit 3x3 coefficient minor")


if __name__ == "__main__":
    main()
