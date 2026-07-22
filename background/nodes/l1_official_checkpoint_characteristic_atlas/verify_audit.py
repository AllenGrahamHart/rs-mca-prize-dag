#!/usr/bin/env python3
"""Mutation audit for the official checkpoint characteristic atlas."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_checkpoint_characteristic_atlas"
ATLAS = Path(__file__).with_name("checkpoint_atlas.tsv")


def main() -> None:
    checks = 0
    with ATLAS.open(newline="") as source:
        rows = [
            {key: int(value) for key, value in row.items()}
            for row in csv.DictReader(source, delimiter="\t")
        ]

    assert len(rows) == 59
    assert min(row["s"] for row in rows) == 13
    assert max(row["s"] for row in rows) == 43
    assert all(row["s"] <= 44 for row in rows)
    checks += 4

    histogram = Counter(row["m"] for row in rows)
    assert histogram[1] == 33
    assert histogram[2] == 10
    assert sum(histogram[m] for m in histogram if m >= 3) == 16
    assert set(histogram) == {1, 2, 3, 4, 5, 7, 8, 16}
    checks += 4

    assert sum(row["m"] == 2 and row["remainder"] == 2 for row in rows) == 4
    assert sum(row["m"] == 2 and row["remainder"] != 2 for row in rows) == 6
    checks += 2

    # The smallest row pins both live low-multiplicity routes.
    first = [row for row in rows if row["n"] == 8192]
    assert [(row["p"], row["ord"], row["m"]) for row in first] == [
        (3583, 16, 2),
        (5119, 8, 1),
        (6143, 4, 1),
        (7681, 16, 1),
        (8191, 2, 1),
    ]
    checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    audit = (ROOT / "background" / "nodes" / NODE / "audit.md").read_text()
    assert "13<=s<=44" in statement
    assert "32 values" in statement
    assert "deterministic" in audit
    assert "does not create a new characteristic residue" in audit
    assert "Higher-width" in audit
    assert "theorem-empty" in audit
    checks += 6

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["l1_mixed_petal_amplification"]["status"] == "TARGET"
    checks += 2

    print(f"AUDIT_L1_OFFICIAL_CHECKPOINT_CHARACTERISTIC_ATLAS_PASS checks={checks}")


if __name__ == "__main__":
    main()
