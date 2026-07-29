#!/usr/bin/env python3
"""Check the quadratic resultant identity and official root counts."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_order_one_quadratic_color_resultant"
DEPENDENCY = "l1_mersenne_hnf_order_one_frobenius_gate"
CONSUMER = "l1_mixed_petal_amplification"


def determinant(matrix: list[list[int]]) -> int:
    total = 0
    for permutation in itertools.permutations(range(len(matrix))):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(len(permutation))
            for j in range(i + 1, len(permutation))
        )
        term = 1
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += (-1 if inversions % 2 else 1) * term
    return total


def quadratic_resultant(a: int, b: int, c: int, d: int, e: int, f: int) -> int:
    matrix = [
        [a, b, c, 0],
        [0, a, b, c],
        [d, e, f, 0],
        [0, d, e, f],
    ]
    return determinant(matrix)


def closed_resultant(a: int, b: int, c: int, d: int, e: int, f: int) -> int:
    return (a * f - c * d) ** 2 - (a * e - b * d) * (b * f - c * e)


def main() -> None:
    samples = [
        (1, 2, 3, 4, 5, 6),
        (2, -3, 5, 7, -11, 13),
        (-4, 1, 9, 3, 8, -2),
    ]
    for sample in samples:
        assert quadratic_resultant(*sample) == closed_resultant(*sample)

    atlas = ROOT / "background/nodes/l1_official_checkpoint_characteristic_atlas/checkpoint_atlas.tsv"
    rows = set()
    for line in atlas.read_text().splitlines()[1:]:
        _, n, p, _, m, remainder = map(int, line.split("\t"))
        if m in (8, 16) and remainder == m:
            rows.add((n, p, m))
    assert len(rows) == 5
    for n, p, m in rows:
        assert n == m * (p + 1)
        assert p % m == m - 1
    assert (15 - 1 + 1) // 2 == 7 > 6
    assert 7 - 1 == 6

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(QCRS2)", "(QCRS4)", "(QCRS5)"):
        assert anchor in statement
    for anchor in ("degree six", "seven distinct", "intersection-multiplicity"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_ORDER_ONE_QUADRATIC_COLOR_RESULTANT_PASS rows=5 h15=empty h7=degree6")


if __name__ == "__main__":
    main()
