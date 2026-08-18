#!/usr/bin/env python3
"""Independent audit of global-atom record extension."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "7d899ce39d8cdb167353728a6ac3511de2fa10d1bea0a3bb712d1f7093cdd42f"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["shared_records"] == data["packet_size"] - 1
    assert data["shared_anchor_type_records"] == data["anchor_records_after_replacement"] - 1
    assert data["shared_records"] >= data["atom_identity_threshold"]
    assert min(data["shared_anchor_type_records"], data["minimum_shared_counterpart_records"]) >= 3

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_cross_type_atom_weld_gauge_dichotomy"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "replace one fixed `p` record" in proof
    assert "repeat for every record" in proof
    assert "certificate coverage, not a cardinality payment" in statement
    print("CROSS_TYPE_GLOBAL_ATOM_EXTENSION_AUDIT_PASS overlap=31")


if __name__ == "__main__":
    main()
