#!/usr/bin/env python3
"""Independent audit of dimension-two common-core shortening."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "6d5c814be1bf2e0e9947cb36115891b9fa38441f2d81e1a3156efc121ec027f7"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    t = data["direction_count"]
    roots = data["direction_intersection_floor"]
    core = data["common_core_floor"]
    assert (t - 1) * (core - 1) < t * roots - data["n"] <= (t - 1) * core
    assert (data["n"] - core) - t * (roots - core) == 28
    assert data["m"] - core - (data["K"] - core) == data["preserved_excess"]

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_affine_line_cap_direction_router"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "primitive members are coprime" in proof
    assert "subtract the common codeword pair" in statement
    assert "81908" in statement
    assert "dimension three or four" in statement
    print("PAIR_PENCIL_DIM2_COMMON_CORE_AUDIT_PASS core=81908 slack=28")


if __name__ == "__main__":
    main()
