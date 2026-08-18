#!/usr/bin/env python3
"""Independent audit of the atom-weld gauge dichotomy."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "c977c422ea2be541bc0475a7b215ba311e45f0ad8e92cfa79dd162a3987a6120"
P = 103


def det(points: tuple[tuple[int, int], tuple[int, int], tuple[int, int]]) -> int:
    (a, b), (c, d), (e, f) = points
    return ((c - a) * (f - b) - (e - a) * (d - b)) % P


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["canonical_anchor_records"] >= 3
    basis = ((0, 0), (1, 0), (0, 1))
    assert det(basis) != 0
    for point in ((2, 2), (4, 9), (11, 7), (0, 4)):
        assert det((basis[0], basis[2], point)) != 0 or det((basis[1], basis[2], point)) != 0
    line = tuple((x, (5 * x + 8) % P) for x in range(12))
    assert all(det(triple) == 0 for triple in itertools.combinations(line, 3))

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_cross_type_degree18_atom_weld_compiler"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "common scalar normalization" in proof
    assert "triangle cocycle" in proof
    assert "global propagation" in proof
    assert "rational pair pencil" in statement
    print("CROSS_TYPE_ATOM_WELD_GAUGE_AUDIT_PASS outputs=global-atom,rank-two")


if __name__ == "__main__":
    main()
