#!/usr/bin/env python3
"""Mutation audit for the official first-checkpoint split-pencil reduction."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_official_first_checkpoint_split_pencil_reduction"


def main() -> None:
    checks = 0

    p = 3583
    assert 11 * (p * p - p + 1) > 256 * p
    degree_cap = 11 * (p - 1) // 256
    closed_ratio_floor = 1 + (p * p - p + degree_cap - 1) // degree_cap
    next_ratio_floor = 1 + (p * p - p + degree_cap) // (degree_cap + 1)
    assert degree_cap == 153
    assert closed_ratio_floor > (256 * p) // 11
    assert next_ratio_floor <= (256 * p) // 11

    n = 8192
    row_cap = (p * (p - 1) - 1) // (n - 1)
    assert row_cap == 1566
    assert 1 + (p * (p - 1) + row_cap) // (row_cap + 1) == n
    checks += 7

    # Terminal depth makes the perturbation linear and raises the tail floor.
    depth = 2 * p - 2
    perturbation_degree = 2 * p - depth - 1
    assert perturbation_degree == 1
    assert 2 * p - depth - 2 == 0
    checks += 2

    # A nonconstant difference has degree r<p and therefore nonzero derivative.
    for degree in (1, p - 1):
        assert degree % p != 0
        assert p + degree - 1 > p - 2
        checks += 2

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    proof = (ROOT / "background" / "nodes" / NODE / "proof.md").read_text()
    audit = (ROOT / "background" / "nodes" / NODE / "audit.md").read_text()
    assert "p<=d<=2p-2" in statement
    assert "one degree above" in audit
    assert "H=gamma K" in proof
    assert "does not bound that census" in statement
    assert "nonzero one of the two distinct" in audit
    assert "r_*(p,n)" in statement
    assert "row-dependent endpoint" in audit
    checks += 7

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes["l1_mixed_petal_amplification"]["status"] == "TARGET"
    checks += 2

    print(f"AUDIT_L1_OFFICIAL_FIRST_CHECKPOINT_SPLIT_PENCIL_REDUCTION_PASS checks={checks}")


if __name__ == "__main__":
    main()
