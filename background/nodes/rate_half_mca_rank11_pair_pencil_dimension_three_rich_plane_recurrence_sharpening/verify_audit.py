#!/usr/bin/env python3
"""Independent audit of the dimension-three rich-plane sharpening."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "62ff582fb5bdd34dbb15a7d8b73618f01139e7db68fb3a150af15e17c5f918ea"


def capacity(k_prime: int) -> int:
    n_prime = 1048576 + k_prime
    return 188 * n_prime + 60 * (k_prime - 2)


def demand(k_prime: int) -> int:
    return 520 * (67470 + k_prime)


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert 3 * 188 - 3 * 15 == 519 <= 520
    assert 3 * 189 - 3 * 15 == 522 > 520
    assert 218 - 188 == 30

    kmax = data["residual_dimension_ceiling"]
    assert kmax == 595763
    assert capacity(kmax) - demand(kmax) == data["endpoint_capacity_slack"] == 232
    assert demand(kmax + 1) - capacity(kmax + 1) == data["adjacent_capacity_deficit"] == 40
    assert capacity(kmax + 1) - capacity(kmax) == 248
    assert demand(kmax + 1) - demand(kmax) == 520
    assert 1048576 - kmax == data["common_core_floor"] == 452813

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    parent = "rate_half_mca_rank11_pair_pencil_affine_plane_cap_218_sharpening"
    assert nodes[parent]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    audit = " ".join((HERE / "audit.md").read_text().lower().split())
    assert "3*189-3*15=522" in proof
    assert "deg g<=k'-2" in proof
    assert "not records" in audit
    assert "not the prize's safe-and-adjacent-unsafe certificate" in audit
    print("RANK11_D3_RICH_PLANE_AUDIT_PASS Kmax=595763 core=452813 next_deficit=40")


if __name__ == "__main__":
    main()
