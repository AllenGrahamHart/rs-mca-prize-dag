#!/usr/bin/env python3
"""Replay the LP4 affine-factor rank guardrail."""

from __future__ import annotations

import sympy as sp


X = sp.symbols("X")


def poly(b1: int, b2: int) -> sp.Expr:
    return sp.expand((X - 2) ** (2 * b1) * (X - 5) ** (2 * b2))


def main() -> None:
    labels = [(b1, b2) for b1 in range(3) for b2 in range(3)]
    polys = [poly(*label) for label in labels]
    mat = sp.Matrix(
        [[sp.Poly(item, X).coeff_monomial(X**degree) for item in polys] for degree in range(9)]
    )
    rank = mat.rank()
    if rank != 8:
        raise AssertionError(rank)

    coeffs = {
        (0, 0): 81,
        (0, 1): -18,
        (0, 2): 1,
        (1, 0): -18,
        (1, 1): -2,
        (1, 2): 0,
        (2, 0): 1,
        (2, 1): 0,
        (2, 2): 0,
    }
    relation = sp.expand(sum(coeffs[label] * poly(*label) for label in labels))
    if relation != 0:
        raise AssertionError(relation)

    print("LP4 affine-factor full-degree shortcut fails")
    print("A=1 B=3 H=2 roots=(2,5)")
    print("rank=8 expected_full_degree_rank=9")
    print("relation:")
    print("81 P00 - 18 P01 + P02 - 18 P10 - 2 P11 + P20 = 0")
    print("H3_REPEAT_BOUNDARY_LP4_RANK_GUARDRAIL_PASS")


if __name__ == "__main__":
    main()
