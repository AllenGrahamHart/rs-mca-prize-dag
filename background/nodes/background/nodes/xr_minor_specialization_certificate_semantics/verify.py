#!/usr/bin/env python3
"""Tiny sanity check for XR minor-specialization certificate semantics."""

from __future__ import annotations

from itertools import permutations

P = 101
NVAR = 2
Monomial = tuple[int, ...]
Poly = dict[Monomial, int]


def norm(poly: Poly) -> Poly:
    return {m: c % P for m, c in poly.items() if c % P}


def const(c: int) -> Poly:
    return norm({(0,) * NVAR: c})


def var(i: int) -> Poly:
    m = [0] * NVAR
    m[i] = 1
    return {tuple(m): 1}


def add(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, 0) + c
    return norm(out)


def scale(a: Poly, c: int) -> Poly:
    return norm({m: c * v for m, v in a.items()})


def mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(x + y for x, y in zip(ma, mb))
            out[m] = out.get(m, 0) + ca * cb
    return norm(out)


def eval_poly(poly: Poly, point: tuple[int, ...]) -> int:
    total = 0
    for monomial, coeff in poly.items():
        term = coeff
        for x, power in zip(point, monomial):
            term = term * pow(x, power, P)
        total += term
    return total % P


def parity(perm: tuple[int, ...]) -> int:
    inv = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            inv += perm[i] > perm[j]
    return -1 if inv % 2 else 1


def det_poly(matrix: list[list[Poly]]) -> Poly:
    n = len(matrix)
    total: Poly = {}
    for perm in permutations(range(n)):
        term = const(parity(perm))
        for row, col in enumerate(perm):
            term = mul(term, matrix[row][col])
        total = add(total, term)
    return total


def det_mod(matrix: list[list[int]]) -> int:
    n = len(matrix)
    total = 0
    for perm in permutations(range(n)):
        term = parity(perm)
        for row, col in enumerate(perm):
            term *= matrix[row][col]
        total += term
    return total % P


def main() -> None:
    zero = const(0)
    one = const(1)
    x = var(0)
    y = var(1)

    minor = [
        [x, one, zero],
        [y, one, one],
        [one, zero, y],
    ]
    determinant = det_poly(minor)
    point = (3, 5)
    specialized = [
        [eval_poly(entry, point) for entry in row]
        for row in minor
    ]

    value_from_polynomial = eval_poly(determinant, point)
    value_from_matrix = det_mod(specialized)
    assert value_from_polynomial == value_from_matrix
    assert value_from_polynomial != 0
    assert determinant
    assert eval_poly({}, point) == 0

    print(
        "xr minor-specialization semantics check passed:",
        {"point": point, "det": value_from_polynomial},
    )


if __name__ == "__main__":
    main()
