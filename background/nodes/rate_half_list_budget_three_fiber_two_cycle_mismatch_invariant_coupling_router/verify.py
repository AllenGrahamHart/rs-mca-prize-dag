#!/usr/bin/env python3
"""Verify the finite binary-quartic mismatch coupling router."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_two_cycle_mismatch_invariant_coupling_router"
DEPENDENCY = "rate_half_list_budget_three_fiber_two_cycle_boundary_transfer"
CONSUMER = "rate_half_list_adjacent_crossing"


def invariants(coefficients: tuple[int, int, int, int, int]) -> tuple[int, int]:
    a, b, c, d, e = coefficients
    invariant_i = 12 * a * e - 3 * b * d + c * c
    invariant_j = (
        72 * a * c * e
        + 9 * b * c * d
        - 27 * a * d * d
        - 27 * b * b * e
        - 2 * c * c * c
    )
    return invariant_i, invariant_j


def c1_invariants(a_square: int, b_square: int, d_square: int, u: int) -> tuple[int, int]:
    invariant_i = (
        a_square * a_square
        + b_square * d_square
        + 3 * a_square * (b_square + d_square)
        - 8 * a_square * u
    )
    invariant_j = 2 * (a_square - u) * (
        a_square * a_square
        + b_square * d_square
        + 16 * a_square * u
        - 9 * a_square * (b_square + d_square)
    )
    return invariant_i, invariant_j


def c2_invariants(a_square: int, b_square: int) -> tuple[int, int]:
    invariant_i = a_square * a_square + 14 * a_square * b_square + b_square * b_square
    invariant_j = 2 * (a_square + b_square) * (
        a_square * a_square - 34 * a_square * b_square + b_square * b_square
    )
    return invariant_i, invariant_j


def same_modulus(left: tuple[int, int], right: tuple[int, int]) -> bool:
    left_i, left_j = left
    right_i, right_j = right
    return left_i**3 * right_j**2 == right_i**3 * left_j**2


def formula_check() -> None:
    for a_root, b_root, d_root in ((1, 2, 3), (2, -3, 5), (3, 4, -7)):
        a_square = a_root * a_root
        b_square = b_root * b_root
        d_square = d_root * d_root
        u = b_root * d_root
        s = b_root + d_root
        direct = invariants((1, -s, u - a_square, a_square * s, -a_square * u))
        assert direct == c1_invariants(a_square, b_square, d_square, u)

    for a_root, b_root in ((1, 2), (2, 5), (3, -7)):
        a_square = a_root * a_root
        b_square = b_root * b_root
        direct = invariants((1, 0, -a_square - b_square, 0, a_square * b_square))
        assert direct == c2_invariants(a_square, b_square)


def anharmonic_factor_check() -> None:
    # Both sides have degree at most six in each variable, so this 8x8 exact
    # interpolation grid proves the displayed polynomial identity.
    for lam in range(8):
        for mu in range(8):
            left = (
                (lam * lam - lam + 1) ** 3 * mu * mu * (1 - mu) ** 2
                - (mu * mu - mu + 1) ** 3 * lam * lam * (1 - lam) ** 2
            )
            right = (
                (lam - mu)
                * (lam * mu - 1)
                * (lam + mu - 1)
                * (lam * mu - lam + 1)
                * (lam * mu - lam - mu)
                * (lam * mu - mu + 1)
            )
            assert left == right


def packet_count_check() -> None:
    roots = (1, 4, 9, 16)
    square_roots = {1: 1, 4: 2, 9: 3, 16: 4}
    c2_packet = [c2_invariants(*pair) for pair in combinations(roots, 2)]
    assert len(c2_packet) == 6

    c1_packet = []
    for repeated in roots:
        for residual in roots:
            if repeated == residual:
                continue
            remaining = [root for root in roots if root not in (repeated, residual)]
            b_square, d_square = remaining
            positive_u = square_roots[b_square] * square_roots[d_square]
            for u in (positive_u, -positive_u):
                c1_packet.append(c1_invariants(repeated, b_square, d_square, u))
    assert len(c1_packet) == 24

    true_c1 = c1_invariants(1, 4, 9, 6)
    wrong_sign = c1_invariants(1, 4, 9, -6)
    assert same_modulus(true_c1, true_c1)
    assert not same_modulus(true_c1, wrong_sign)

    true_c2 = c2_invariants(1, 4)
    wrong_pair = c2_invariants(9, 16)
    assert not same_modulus(true_c2, wrong_pair)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    proof = (here / "proof.md").read_text()
    for marker in (
        "4*3*2=24",
        "binom(4,2)=6",
        "union has 30 indexed tests",
        "I_O^3 J_*^2=I_*^3 J_O^2",
        "does not prove any equation",
    ):
        assert marker in statement
    for marker in (
        "six anharmonic transforms",
        "global negation",
        "unique\nfractional-linear map",
    ):
        assert marker in proof


def main() -> None:
    formula_check()
    anharmonic_factor_check()
    packet_count_check()
    packet_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_MISMATCH_INVARIANT_COUPLING_PASS "
        "c1_classes=24 c2_classes=6 interpolation_checks=64 mutations=2"
    )


if __name__ == "__main__":
    main()
