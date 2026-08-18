#!/usr/bin/env python3
"""Independent audit of the dimension-two incidence exclusion."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "03ec061a245542f320e8fd1bb38c0d3b704b03b4639c414f496e87be25187c5d"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    q = data["selected_type_floor"]
    required = q * data["pair_core_size"]
    capacity = q * data["common_core_cap"] + data["noncommon_coordinate_multiplicity_cap"] * (
        data["n"] - data["common_core_cap"]
    )
    assert required == data["required_incidence"]
    assert capacity == data["capacity"]
    assert required - capacity == data["contradiction_margin"] > 0

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_affine_line_cap_direction_router"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "nonzero `f`-linear functional" in proof
    assert "one affine fiber" in proof
    assert "19356265" in statement
    assert "dimension three or four" in statement
    print("PAIR_PENCIL_DIM2_INCIDENCE_AUDIT_PASS margin=19356265")


if __name__ == "__main__":
    main()
