#!/usr/bin/env python3
"""Verify the shifted-value gate, official arithmetic, and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_next_to_maximal_belyi_shifted_value_gate"
SUPPLIER = "l1_mersenne_next_to_maximal_exceptional_reduction"
CONSUMER = "l1_mixed_petal_amplification"
ROWS = (
    (8191, 8),
    (131071, 8),
    (524287, 8),
    (2147483647, 8),
    (8191, 16),
)


def main() -> None:
    checks = 0
    for p, m in ROWS:
        assert (p + 1) % m == 0
        e = ((m - 1) * p - 1) // m
        assert m * e + 1 == (m - 1) * p
        assert e < p - 1 < 2 * e
        assert p > m
        checks += 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert (SUPPLIER, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    checks += 4

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in ("(BSG1)", "(BSG2)", "(BSG3)", "(BSG4)", "(BSG5)",
                   "(BSG2a)", "(BSG2b)", "P(W) divides W^n-1",
                   "c` and `theta` in the prime field",
                   "z!=0", "quadratic-field-normalized residue"):
        assert anchor in statement
        checks += 1

    print(f"L1_MERSENNE_NEXT_TO_MAXIMAL_BELYI_SHIFTED_VALUE_GATE_PASS checks={checks}")


if __name__ == "__main__":
    main()
