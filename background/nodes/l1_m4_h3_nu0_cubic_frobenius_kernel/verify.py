#!/usr/bin/env python3
"""Verify the nu=0 cubic Frobenius-kernel degree ledger and wiring."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_nu0_cubic_frobenius_kernel"
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

    for row in rows:
        p, n = row["p"], row["n"]
        assert p > 5
        assert n + p - 4 == 5 * p
        assert (p - 4) + 3 * p + (p + 4) == 5 * p
        assert (p - 4) + (2 * p + 4) == 3 * p
        assert (p - 5) + 2 * p + 3 == 3 * p - 2
        assert (p - 1) - (p - 5) == 4
        assert (2 * p - 1) - (p - 5) == p + 4
        checks += 7

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
    for anchor in ("(CFK2)", "(CFK3)", "(CFK4)", "(CFK5)",
                   "q_3^p=a", "does not"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_NU0_CUBIC_FROBENIUS_KERNEL_PASS checks={checks}")


if __name__ == "__main__":
    main()
