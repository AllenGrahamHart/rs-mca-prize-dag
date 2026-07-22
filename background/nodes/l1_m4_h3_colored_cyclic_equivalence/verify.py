#!/usr/bin/env python3
"""Verify the m=4 colored cyclic-code equivalence ledger and wiring."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_m4_h3_colored_cyclic_equivalence"
SUPPLIERS = {
    "l1_mersenne_checkpoint_cyclotomic_normal_form",
    "l1_official_max_split_value_complement_census",
}
CONSUMER = "l1_mixed_petal_amplification"


def primitive_cube_root(p: int) -> int:
    for value in range(2, min(p, 1000)):
        if pow(value, 3, p) == 1 and value != 1:
            return value
    # The official primes are large; derive a root from any noncube if the
    # tiny deterministic prefix happened not to contain one.
    for value in range(2, p):
        root = pow(value, (p - 1) // 3, p)
        if root != 1:
            return root
    raise AssertionError("no primitive cube root")


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
        assert p % 3 == 1
        omega = primitive_cube_root(p)
        assert omega != 1 and pow(omega, 3, p) == 1
        assert (1 + omega + omega * omega) % p == 0
        assert n - 3 * p == p + 4
        checks += 4

    for p in (7, 13, 31):
        if p % 3 != 1:
            continue
        omega = primitive_cube_root(p)
        solutions = []
        for s0 in range(p):
            for s1 in range(p):
                for s2 in range(p):
                    first = (s0 + omega * s1 + omega * omega * s2) % p
                    second = (s0 + omega * omega * s1 + omega * s2) % p
                    if first == second == 0:
                        solutions.append((s0, s1, s2))
        assert all(s0 == s1 == s2 for s0, s1, s2 in solutions)
        assert len(solutions) == p
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
    for anchor in ("(CC3-1)", "(CC3-2)", "(CC3-3)",
                   "coefficientwise squaring", "does not prove"):
        assert anchor in statement
        checks += 1

    print(f"L1_M4_H3_COLORED_CYCLIC_EQUIVALENCE_PASS checks={checks}")


if __name__ == "__main__":
    main()
