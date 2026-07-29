#!/usr/bin/env python3
"""Check the official color-degree Bézout thresholds."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_order_one_color_degree_barrier"
DEPENDENCY = "l1_mersenne_hnf_order_one_frobenius_gate"
CONSUMER = "l1_mixed_petal_amplification"


def first_nonconstant_degree(root_count: int) -> int:
    degree = 1
    while degree * (degree + 1) < root_count:
        degree += 1
    return degree


def main() -> None:
    assert first_nonconstant_degree(6) == 2
    assert first_nonconstant_degree(14) == 4
    assert [degree * (degree + 1) for degree in (1, 2, 3, 4)] == [2, 6, 12, 20]

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
        assert first_nonconstant_degree(m - 2) == (2 if m == 8 else 4)

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    assert "H<=d(d+1)" in statement
    for anchor in ("Bézout", "no common component", "2,6,12<14"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_ORDER_ONE_COLOR_DEGREE_BARRIER_PASS h7>=2 h15>=4")


if __name__ == "__main__":
    main()
