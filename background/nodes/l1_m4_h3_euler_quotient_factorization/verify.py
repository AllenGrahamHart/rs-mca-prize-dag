#!/usr/bin/env python3
"""Verify the Euler quotient factorization degree ledger and wiring."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_euler_quotient_factorization"
SUPPLIER = "l1_m4_h3_cartier_resonance_reduction"
CONSUMER = "l1_mixed_petal_amplification"


def main() -> None:
    checks = 0
    atlas = (ROOT / "background" / "nodes" /
             "l1_official_checkpoint_characteristic_atlas" /
             "checkpoint_atlas.tsv")
    with atlas.open() as handle:
        rows = [{key: int(value) for key, value in row.items()}
                for row in csv.DictReader(handle, delimiter="\t")]
    rows = [row for row in rows
            if row["m"] == 4 and row["n"] == 4 * (row["p"] + 1)]
    assert len(rows) == 4

    for row in rows:
        p = row["p"]
        for nu in range(4):
            assert (4 - 3 * nu) % p != 0
            for h in range(4 - nu):
                degree_v = p + h - 4
                assert p - 4 <= degree_v <= p - nu - 1
                left_degree = (p + 4) + p + degree_v
                assert left_degree == 3 * p + h
                checks += 3

    # Coefficient identity 3(Y^3+aY+b)-Y(3Y^2+a)=2aY+3b.
    cubic = {3: 1, 1: 1, 0: 1}
    derivative = {2: 3, 0: 1}
    left = {degree: 3 * value for degree, value in cubic.items()}
    for degree, value in derivative.items():
        left[degree + 1] = left.get(degree + 1, 0) - value
    assert {degree: value for degree, value in left.items() if value} == {1: 2, 0: 3}
    checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert (SUPPLIER, NODE, "req") in edges
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges
    checks += 5

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(EQF3)", "(EQF4)", "(EQF5)", "H(0)!=0",
                   "deg V=p+h-4", "does not exclude"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_EULER_QUOTIENT_FACTORIZATION_PASS checks={checks}")


if __name__ == "__main__":
    main()
