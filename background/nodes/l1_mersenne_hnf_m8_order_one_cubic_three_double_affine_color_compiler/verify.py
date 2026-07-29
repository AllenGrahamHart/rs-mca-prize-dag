#!/usr/bin/env python3
"""Check the combinatorial and depressed-cubic affine-color compiler."""

from __future__ import annotations

import json
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_color_compiler"
DEPENDENCIES = {
    "l1_mersenne_hnf_m8_order_one_cubic_three_double_linear_remainder_reduction",
    "l1_mersenne_hnf_m8_cubic_three_two_one_role_polynomial_compiler",
}
CONSUMER = "l1_mixed_petal_amplification"


def rotate(subset: frozenset[int], shift: int) -> frozenset[int]:
    return frozenset((value + shift) % 8 for value in subset)


def reflect(subset: frozenset[int]) -> frozenset[int]:
    return frozenset((-value) % 8 for value in subset)


def orbit(subset: frozenset[int], include_reflection: bool) -> frozenset[frozenset[int]]:
    out = {rotate(subset, shift) for shift in range(8)}
    if include_reflection:
        mirrored = reflect(subset)
        out.update(rotate(mirrored, shift) for shift in range(8))
    return frozenset(out)


def canonical_orbits(include_reflection: bool) -> set[frozenset[frozenset[int]]]:
    subsets = (frozenset(values) for values in combinations(range(8), 3))
    return {orbit(subset, include_reflection) for subset in subsets}


def main() -> None:
    assert len(list(combinations(range(8), 3))) == 56
    cyclic = canonical_orbits(False)
    dihedral = canonical_orbits(True)
    assert len(cyclic) == 7
    assert all(len(item) == 8 for item in cyclic)
    assert len(dihedral) == 5

    # For the normalized triple (0,1,lambda), check (TAC1)--(TAC2).
    for lam in (F(2), F(-1), F(3, 2)):
        e1, e2, e3 = 1 + lam, lam, F(0)
        p = e2 - e1**2 / 3
        q = e3 - e1 * e2 / 3 + 2 * e1**3 / 27
        a = lam**2 - lam + 1
        b = (lam + 1) * (2 * lam - 1) * (lam - 2)
        assert p == -a / 3
        assert q == b / 27
        assert 27 * a**3 * q**2 + b**2 * p**3 == 0

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    for dependency in DEPENDENCIES:
        assert statuses[dependency] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(TAC2)", "(TAC3)", "(TAC4)", "(TAC6)"):
        assert anchor in statement
    for anchor in ("seven oriented", "five classes", "four stated equations"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_CUBIC_THREE_DOUBLE_AFFINE_COLOR_COMPILER_PASS")


if __name__ == "__main__":
    main()
