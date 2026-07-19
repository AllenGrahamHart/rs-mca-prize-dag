#!/usr/bin/env python3
"""Verify the antipodal primitive quotient gate and DAG wiring."""

from __future__ import annotations

import json
from itertools import permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_primitive_quotient_gate"
DEPENDENCY = "rate_half_list_budget_three_antipodal_mobius_weld"
CONSUMER = "rate_half_list_adjacent_crossing"


def determinant(matrix: list[list[int]]) -> int:
    total = 0
    for permutation in permutations(range(4)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(4)
            for j in range(i + 1, 4)
        )
        term = 1
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += (-1 if inversions % 2 else 1) * term
    return total


def arithmetic_check() -> None:
    for exponent in range(4, 40):
        d = 1 << exponent
        s = d // 4
        degree = s - 1
        assert degree % 2 == 1
        for quotient_exponent in range(1, exponent + 1):
            quotient_degree = 1 << quotient_exponent
            assert degree % quotient_degree != 0

    values = (2, 3, 5, 7)
    matrix = [[1, value, value**2, value**3] for value in values]
    expected = 1
    for left in range(4):
        for right in range(left + 1, 4):
            expected *= values[right] - values[left]
    assert determinant(matrix) == expected != 0


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (
        ROOT / "background" / "nodes" / NODE / "statement.md"
    ).read_text()
    for marker in (
        "deg f=r=s-1",
        "g(Y^m)",
        "g(Y^m+Y^(-m))",
        "four cosets",
        "does not exclude a primitive, nonperiodic solution",
    ):
        assert marker in statement


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "RATE_HALF_LIST_B3_ANTIPODAL_PRIMITIVE_QUOTIENT_GATE_PASS "
        "dyadic_degrees=4..39 pullbacks=cyclic+dihedral coset_rank=4"
    )


if __name__ == "__main__":
    main()
