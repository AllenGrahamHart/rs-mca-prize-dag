#!/usr/bin/env python3
"""Replay the Plucker and two-generator gates on the exact toy witness."""

from __future__ import annotations

import importlib.util
from itertools import combinations
from pathlib import Path


SOURCE = (
    Path(__file__).resolve().parents[1]
    / "rate_half_list_budget_three_split_pencil_normal_form"
    / "verify_audit.py"
)
SPEC = importlib.util.spec_from_file_location("split_audit", SOURCE)
SPLIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(SPLIT)


def fixture():
    words = tuple(
        tuple(SPLIT.evaluate(poly, x) for x in SPLIT.DOMAIN)
        for poly in SPLIT.POLYS
    )
    supports = tuple(
        {index for index, value in enumerate(word) if value == SPLIT.RECEIVED[index]}
        for word in words
    )
    triple = {i: [] for i in range(4)}
    edges = {edge: [] for edge in combinations(range(4), 2)}
    full: list[int] = []
    singleton: list[int] = []
    for coordinate, x in enumerate(SPLIT.DOMAIN):
        members = tuple(i for i, support in enumerate(supports) if coordinate in support)
        if len(members) == 4:
            full.append(x)
        elif len(members) == 3:
            triple[next(i for i in range(4) if i not in members)].append(x)
        elif len(members) == 2:
            edges[tuple(sorted(members))].append(x)
        elif len(members) == 1:
            singleton.append(x)
        else:
            raise AssertionError

    A = {i: SPLIT.locator(roots) for i, roots in triple.items()}
    E = {edge: SPLIT.locator(roots) for edge, roots in edges.items()}
    J = SPLIT.locator(full)
    W = SPLIT.locator(singleton)
    R = SPLIT.product([W, J, *E.values()])
    Z = SPLIT.locator(list(SPLIT.DOMAIN))
    B = {}
    for i, j in combinations(range(4), 2):
        k, l = tuple(index for index in range(4) if index not in (i, j))
        pair = SPLIT.product([J, A[k], A[l], E[i, j]])
        difference = SPLIT.subtract(SPLIT.POLYS[j], SPLIT.POLYS[i])
        quotient, remainder = SPLIT.divide(difference, pair)
        assert remainder == (0,)
        B[i, j] = SPLIT.multiply(E[i, j], quotient)
    return A, B, R, Z


def plucker(B):
    return SPLIT.add(
        SPLIT.subtract(
            SPLIT.multiply(B[0, 1], B[2, 3]),
            SPLIT.multiply(B[0, 2], B[1, 3]),
        ),
        SPLIT.multiply(B[0, 3], B[1, 2]),
    )


def main() -> None:
    A, B, R, Z = fixture()
    assert plucker(B) == (0,)

    u = (B[0, 1], (0,), SPLIT.negate(B[1, 2]), SPLIT.negate(B[1, 3]))
    v = ((0,), B[0, 1], B[0, 2], B[0, 3])
    minors = 0
    for i, j in combinations(range(4), 2):
        minor = SPLIT.subtract(SPLIT.multiply(u[i], v[j]), SPLIT.multiply(u[j], v[i]))
        assert minor == SPLIT.multiply(B[0, 1], B[i, j])
        minors += 1

    for i in range(4):
        left = SPLIT.multiply(B[0, 1], A[i])
        right = SPLIT.add(SPLIT.multiply(A[0], u[i]), SPLIT.multiply(A[1], v[i]))
        assert left == right

    n2 = SPLIT.subtract(SPLIT.multiply(A[1], B[0, 2]), SPLIT.multiply(A[0], B[1, 2]))
    n3 = SPLIT.subtract(SPLIT.multiply(A[1], B[0, 3]), SPLIT.multiply(A[0], B[1, 3]))
    left = SPLIT.product([R, A[0], A[1], n2, n3])
    right = SPLIT.product([B[0, 1], B[0, 1], Z])
    assert left == right

    wrong_sign = SPLIT.subtract(
        SPLIT.subtract(
            SPLIT.multiply(B[0, 1], B[2, 3]),
            SPLIT.multiply(B[0, 2], B[1, 3]),
        ),
        SPLIT.multiply(B[0, 3], B[1, 2]),
    )
    assert wrong_sign != (0,)
    mutated = dict(B)
    mutated[2, 3] = SPLIT.add(mutated[2, 3], (1,))
    assert plucker(mutated) != (0,)

    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_PLUCKER_EDGE_GATE_PASS "
        f"plucker=1/1 minors={minors} pencil=4/4 factorization=1/1 mutations=2/2"
    )


if __name__ == "__main__":
    main()
