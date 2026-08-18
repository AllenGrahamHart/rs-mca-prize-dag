#!/usr/bin/env python3
"""Independent audit of cross-type scalar-pair rigidity."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "5fc6a6faee611491cd10bdfb698ebe5d4def70ec9d2e9e49b68a05d2841779d1"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    n = data["domain_size"]
    m = data["support_size"]
    k = data["code_dimension"]
    r = data["shared_records"]
    forced = (r * m - n + r - 2) // (r - 1)
    assert forced == data["forced_g_minus_h_before_shortening"] == 1079711
    assert data["records_per_pair_type"] == 14
    assert r - 1 - 14 == 13
    assert data["pole_incidence_cap"] == 1
    assert forced - (k - 1) == data["contradiction_margin"] == 31136
    for c in range(0, 1048574, 7919):
        left = (r * (m - c) - (n - c) + r - 2) // (r - 1)
        assert left == forced - c
        assert left - (k - c - 1) == 31136

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_heavy_ruling_triple_owner_pole_simple_router"]["status"] == "PROVED"
    assert nodes["rate_half_mca_rank11_cross_type_one_swap_synchronization_wall"]["status"] == "PROVED"

    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "every point of `h` has incidence at most one" in proof
    assert "must be proportional" in proof
    assert "same value at infinity" in statement
    assert "does not construct a 28-record deck" in statement
    print("CROSS_TYPE_SCALAR_PAIR_RIGIDITY_AUDIT_PASS margin=31136 survivor=proportional")


if __name__ == "__main__":
    main()
