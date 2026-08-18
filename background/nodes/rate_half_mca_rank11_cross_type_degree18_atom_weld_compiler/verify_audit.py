#!/usr/bin/env python3
"""Independent audit of the degree-18 atom-weld compiler."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "8482df87726c964e3469bb112130f601bbbbbfc1353d4bddcd8f998efa4a851f"


def margin(shared: int) -> int:
    forced = (shared * 1116048 - 2097152 + shared - 2) // (shared - 1)
    return forced - 1048575


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    rows = []
    for t in range(1, 5):
        counterpart = 17 - 3 * t
        other = 3 * (t - 1)
        shared = 2 * counterpart + other
        rows.append((t, counterpart, other, shared, margin(shared)))
    actual = [
        (
            row["secondary_types"],
            row["counterpart_records"],
            row["other_records"],
            row["shared_records"],
            row["identity_margin"],
        )
        for row in data["profiles"]
    ]
    assert actual == rows
    assert [row[3] for row in rows] == [28, 25, 22, 19]
    assert min(row[1] for row in rows) == 5

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_cross_type_pole_simple_atom_identity"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "start the component-span greedy algorithm" in proof
    assert "the complete packet intersection is `j_3`" in proof
    assert "projectively identical" in statement
    assert "does not identify welds" in statement
    print("CROSS_TYPE_DEGREE18_ATOM_WELD_AUDIT_PASS overlaps=28,25,22,19")


if __name__ == "__main__":
    main()
