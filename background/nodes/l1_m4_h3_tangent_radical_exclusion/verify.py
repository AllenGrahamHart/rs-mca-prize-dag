#!/usr/bin/env python3
"""Verify the tangent-radical case ledger and DAG wiring."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_tangent_radical_exclusion"
SUPPLIERS = {
    "l1_m4_h3_cartier_resonance_reduction",
    "l1_m4_h3_euler_quotient_factorization",
}
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

    excluded = {(1, 0), (1, 1), (2, 0), (3, 0)}
    surviving = {(1, 2), (2, 1)}
    for row in rows:
        p = row["p"]
        seen_excluded = set()
        seen_surviving = set()
        for nu in (1, 2, 3):
            for eta in range(4 - nu):
                degree_v = p + eta - 4
                radical_upper = nu + eta
                radical_lower = p - degree_v
                condition = nu + 2 * eta >= 4
                assert condition == (radical_lower <= radical_upper)
                pair = (nu, eta)
                (seen_surviving if condition else seen_excluded).add(pair)
                checks += 2
        assert seen_excluded == excluded
        assert seen_surviving == surviving
        checks += 2

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in SUPPLIERS:
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges
    checks += 3

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(TRE2)", "(TRE4)", "(TRE5)", "(TRE6)", "(TRE7)",
                   "nu+2eta>=4", "does not exclude"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_TANGENT_RADICAL_EXCLUSION_PASS checks={checks}")


if __name__ == "__main__":
    main()
