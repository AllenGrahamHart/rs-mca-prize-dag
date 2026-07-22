#!/usr/bin/env python3
"""Verify the m=4, h=3 Mason defect arithmetic and DAG wiring."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_mason_defect_budget"
SUPPLIERS = {
    "l1_m4_h3_colored_cyclic_equivalence",
    "l1_official_max_split_value_complement_census",
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

    for row in rows:
        p, n = row["p"], row["n"]
        u = n - 3 * p
        assert u == p + 4 and p > 4
        for nu in range(5):
            left = n - 3 * nu
            radical_ceiling = ((p - nu + u) +
                               (p + u - 3 * nu))
            assert radical_ceiling - left == 4 - nu
            wronskian_cap = (p + u - 3 * nu) - 2 * (p - nu)
            assert wronskian_cap == 4 - nu
            a_zero_ceiling = (p - nu + u) + (u - 3 * nu)
            assert left - a_zero_ceiling == p - 4 + nu > 0
            a_zero_wronskian_cap = (u - 3 * nu) - 2 * (p - nu)
            assert a_zero_wronskian_cap == 4 - p - nu < 0
            checks += 5

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
    for anchor in ("(MDB3)", "(MDB4)", "(MDB5)", "(MDB7)",
                   "deg H<=4-nu", "divides H",
                   "delta_A+delta_B<=deg H<=4-nu",
                   "does not prove"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_MASON_DEFECT_BUDGET_PASS checks={checks}")


if __name__ == "__main__":
    main()
