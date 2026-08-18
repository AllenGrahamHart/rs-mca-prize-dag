#!/usr/bin/env python3
"""Independent audit of the affine-line cap and direction router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "a2f83ea90cb88bfd0d170fec234a3f9b9d505133db50831a935097214211287e"


def choose2(value: int) -> int:
    return value * (value - 1) // 2


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    s, n, K = data["pair_core_size"], data["n"], data["K"]
    assert data["affine_line_cap"] == (n - K + 1) // (s - K + 1)
    blocks, remainder = divmod(data["selected_type_floor"], data["affine_line_cap"])
    pair_cap = blocks * choose2(data["affine_line_cap"]) + choose2(remainder)
    assert pair_cap == data["pairs_per_projective_direction_cap"]
    assert 37 * pair_cap < choose2(data["selected_type_floor"]) <= 38 * pair_cap

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_coprime_direction_normal_form"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "outside `j_l` the `t` cores are pairwise disjoint" in proof
    assert "parallel affine lines" in proof
    assert "dimension-one branch is impossible" in statement
    assert "not full splitting" in statement
    print("PAIR_PENCIL_AFFINE_LINE_CAP_AUDIT_PASS line=15 directions=38")


if __name__ == "__main__":
    main()
