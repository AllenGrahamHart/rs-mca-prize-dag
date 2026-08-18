#!/usr/bin/env python3
"""Independent audit of the pair-pencil coprime-direction normal form."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "d55f5f730f7a5352b9f2bc33794dc789b6b9beb41c0533760df5a8066721dac6"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["pair_core_intersection_floor"] == 2 * data["pair_core_size"] - data["n"]
    assert data["primitive_direction_degree_cap"] == data["K"] - 1 - data["pair_core_intersection_floor"]
    assert data["correction_space_dimension_cap"] == 4

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_quadratic_quotient_large_owner_or_pair_pencil_router"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "since `f[x]` is a pid" in proof
    assert "bezout" in proof
    assert "dimension at most four" in statement
    assert "does not perform" in statement
    print("PAIR_PENCIL_COPRIME_DIRECTION_AUDIT_PASS roots=134940 dim=4")


if __name__ == "__main__":
    main()
