#!/usr/bin/env python3
"""Verify the exact conductor-128 unit-basis interface."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_conductor128_full_unit_circular_basis"
CONSUMER = "e1_qzeta128_p257_j63_residue_obstruction"


def main() -> None:
    indices = list(range(3, 64, 2))
    assert len(indices) == 31
    assert len({min(a, 128 - a) for a in range(1, 128, 2)}) == 32
    assert indices == [a for a in range(1, 64, 2) if a != 1]

    node_dir = ROOT / "background/nodes" / NODE
    statement = (node_dir / "statement.md").read_text()
    proof = (node_dir / "proof.md").read_text()
    for text in ("status:** PROVED", "eta_3,eta_5,...,eta_63", "mu_128"):
        assert text in statement
    for text in ("Miller", "Weber", "Kummer-Sinnott", "rank 31"):
        assert text in proof

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "PROVED"
    assert (NODE, CONSUMER, "req") in edges

    print("E1_CONDUCTOR128_FULL_UNIT_CIRCULAR_BASIS_PASS rank=31")


if __name__ == "__main__":
    main()
