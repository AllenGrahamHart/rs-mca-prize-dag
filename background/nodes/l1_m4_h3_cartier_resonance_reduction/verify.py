#!/usr/bin/env python3
"""Verify the Cartier resonance reduction and DAG wiring."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_cartier_resonance_reduction"
SUPPLIER = "l1_m4_h3_mason_defect_budget"
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
        choices = (p - 4, p - 1, 2, 5, 8)
        for nu, s in enumerate(choices):
            ell = n - 3 * nu
            assert (s + ell) % p == 0
            old_top = s - 1 + 2 * (p - nu) + (4 - nu)
            expected = 3 * p - 1 if nu <= 1 else 2 * p - 1
            assert old_top == expected and (old_top + 1) % p == 0
            checks += 3

        shifts = (p - 5, p - 2, 1, 4)
        resonances = ((p - 1, 2 * p - 1),
                      (p - 1, 2 * p - 1),
                      (p - 1,), (p - 1,))
        expected_sources = ((4, p + 4), (1, p + 1),
                            (p - 2,), (p - 5,))
        for shift, slots, sources in zip(shifts, resonances, expected_sources):
            assert tuple(slot - shift for slot in slots) == sources
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
    for anchor in ("(CRR2)", "(CRR3)", "(CRR4)", "(CRR5)",
                   "nu in {0,1,2,3}",
                   "delta_A+delta_B<=deg H<=3-nu",
                   "does not exclude"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_CARTIER_RESONANCE_REDUCTION_PASS checks={checks}")


if __name__ == "__main__":
    main()
