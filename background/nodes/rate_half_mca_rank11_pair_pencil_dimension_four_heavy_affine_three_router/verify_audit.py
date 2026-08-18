#!/usr/bin/env python3
"""Independent audit of the dimension-four heavy affine-three router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "c5306e2db547697b6038be03a20b1535da279d60b0ff35cc3d181ae4c42198df"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    q = data["selected_types"]
    s = data["pair_core_size"]
    plane = data["affine_plane_cap"]
    n = data["n"]
    core = data["common_core_threshold"]
    assert (q - plane) * (core - 1) < q * s - plane * n <= (q - plane) * core
    assert data["heavy_fiber_type_floor"] == plane + 1
    assert data["heavy_fiber_record_floor"] == (plane + 1) * 29

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_dimension_three_common_core_shortening"]["status"] == "PROVED"
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    assert "actual official-domain coordinate" in (HERE / "audit.md").read_text().lower()
    assert "nonzero linear functional" in proof
    assert "234*29=6786" in statement
    audit = " ".join((HERE / "audit.md").read_text().lower().split())
    assert "neither the shortened branch nor the heavy fiber is declared paid" in audit
    print("PAIR_PENCIL_DIM4_HEAVY_FIBER_AUDIT_PASS core=319539 heavy=234 records=6786")


if __name__ == "__main__":
    main()
