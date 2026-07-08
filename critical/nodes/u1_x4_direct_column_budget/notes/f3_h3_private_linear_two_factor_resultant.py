#!/usr/bin/env python3
"""Explain the two-factor private-linear rank loss by a resultant relation."""

from __future__ import annotations

from fractions import Fraction
from itertools import product

import sympy as sp

from f3_h3_private_linear_two_factor_guardrail import RELATION


X, U, V = sp.symbols("X U V")
ALPHA, BETA, GAMMA, DELTA = sp.symbols("alpha beta gamma delta")


def resultant_relation() -> sp.Poly:
    f = (X - ALPHA) ** 2 - U * (X - BETA) ** 2
    g = (X - GAMMA) ** 2 - V * (X - DELTA) ** 2
    return sp.Poly(sp.resultant(f, g, X), U, V)


def coefficient_vector(params: tuple[int, int, int, int]) -> tuple[int, ...]:
    alpha, beta, gamma, delta = params
    poly = resultant_relation().as_expr().subs(
        {ALPHA: alpha, BETA: beta, GAMMA: gamma, DELTA: delta}
    )
    p = sp.Poly(sp.expand(poly), U, V)
    return tuple(int(p.coeff_monomial(U**i * V**j)) for i in range(3) for j in range(3))


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_pow_linear(root: int, exponent: int) -> list[int]:
    out = [1]
    factor = [-root, 1]
    for _ in range(exponent):
        out = poly_mul(out, factor)
    return out


def rows(params: tuple[int, int, int, int]) -> list[list[int]]:
    alpha, beta, gamma, delta = params
    pairs = ((alpha, beta), (gamma, delta))
    out = []
    for b_exponents in product(range(3), repeat=2):
        base = [1]
        for b_exp, (zero, pole) in zip(b_exponents, pairs):
            base = poly_mul(base, poly_pow_linear(zero, 2 * b_exp))
            base = poly_mul(base, poly_pow_linear(pole, 2 * (2 - b_exp)))
        out.append(base)
    return out


def rank_over_q(items: list[list[int]]) -> int:
    width = max(len(row) for row in items)
    mat = [
        [Fraction(value) for value in row + [0] * (width - len(row))]
        for row in items
    ]
    rank = 0
    for col in range(width):
        pivot = None
        for row in range(rank, len(mat)):
            if mat[row][col]:
                pivot = row
                break
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inv = 1 / mat[rank][col]
        mat[rank] = [value * inv for value in mat[rank]]
        for row in range(len(mat)):
            if row == rank or not mat[row][col]:
                continue
            factor = mat[row][col]
            mat[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(mat[row], mat[rank])
            ]
        rank += 1
    return rank


def relation_polynomial(params: tuple[int, int, int, int]) -> list[int]:
    coeffs = coefficient_vector(params)
    items = rows(params)
    width = max(len(row) for row in items)
    out = [0] * width
    for coeff, row in zip(coeffs, items):
        padded = row + [0] * (width - len(row))
        for index, value in enumerate(padded):
            out[index] += coeff * value
    return out


def main() -> None:
    relation = resultant_relation()
    if relation.degree(U) != 2 or relation.degree(V) != 2:
        raise AssertionError(relation)
    if len(relation.terms()) != 9:
        raise AssertionError(relation.terms())

    sample = (2, 3, 5, 7)
    if coefficient_vector(sample) != RELATION:
        raise AssertionError((coefficient_vector(sample), RELATION))

    checks = (
        sample,
        (2, 5, 3, 11),
        (1, 4, 6, 9),
        (2, 7, 11, 19),
        (10, 27, 19, 15),
    )
    for params in checks:
        if params[0] == params[1] or params[2] == params[3]:
            raise AssertionError(params)
        if any(relation_polynomial(params)):
            raise AssertionError(("relation failed", params, relation_polynomial(params)))
        rank = rank_over_q(rows(params))
        if rank != 8:
            raise AssertionError((params, rank))

    print("h=3 private-linear two-factor resultant relation")
    print("resultant degree: deg_U=2 deg_V=2 terms=9")
    print(f"sample coefficient vector: {coefficient_vector(sample)}")
    for params in checks:
        print(f"params={params}: relation_zero=True rank=8")
    print("structural consequence: A=1,B=3,H=2 two-factor span has rank <= 8")
    print("H3_PRIVATE_LINEAR_TWO_FACTOR_RESULTANT_PASS")


if __name__ == "__main__":
    main()
