#!/usr/bin/env python3
"""Verify the nu=2 multiplicity normal form and DAG wiring."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_nu2_prime_field_belyi_normal_form"
SUPPLIER = "l1_m4_h3_tangent_radical_exclusion"
CONSUMER = "l1_mixed_petal_amplification"


def check_triple(p: int, triple: tuple[int, int, int]) -> None:
    e1, e2, e3 = triple
    assert sum(triple) == p and len(set(triple)) == 3
    d = ((e2 - e3) % p, (e3 - e1) % p, (e1 - e2) % p)
    assert all(d)
    assert sum(d) % p == 0
    assert (e1 * d[0] + e2 * d[1] + e3 * d[2]) % p == 0


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
        for triple in ((1, 2, p - 3), (1, 3, p - 4), (2, 3, p - 5)):
            check_triple(p, triple)
            checks += 4

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
    for anchor in ("(PBN3)", "(PBN4)", "(PBN6)", "(PBN8)",
                   "pairwise distinct", "does not prove"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_NU2_PRIME_FIELD_BELYI_NORMAL_FORM_PASS checks={checks}")


if __name__ == "__main__":
    main()
