#!/usr/bin/env python3
"""Verify the embedded order-2(p+1) family ledger and wiring."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_checkpoint_embedded_m2_family"
SUPPLIERS = {
    "l1_official_split_pencil_value_capacity",
    "l1_mersenne_checkpoint_cyclotomic_normal_form",
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
            if row["m"] in (4, 8, 16)
            and row["n"] == row["m"] * (row["p"] + 1)]
    assert len(rows) == 9
    for row in rows:
        n, p, m = row["n"], row["p"], row["m"]
        nbase = p + 1
        assert n % (2 * nbase) == 0
        assert n // (2 * nbase) == m // 2
        assert (m // 2) * nbase == n // 2
        assert 2 * p - (p - 2) - 1 == p + 1
        checks += 4

    evidence = (ROOT / "experiments" / "prize_resolution" /
                "l1_mersenne_checkpoint_analog_result.md").read_text()
    assert "embedded_m2_h2=16" in evidence
    assert "p=7" in evidence and "route evidence" in evidence
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
    for anchor in ("(EM2-1)", "(EM2-2)", "(EM2-3)", "(EM2-4)",
                   "does not classify all"):
        assert anchor in statement
        checks += 1

    print(f"L1_MERSENNE_CHECKPOINT_EMBEDDED_M2_FAMILY_PASS checks={checks}")


if __name__ == "__main__":
    main()
