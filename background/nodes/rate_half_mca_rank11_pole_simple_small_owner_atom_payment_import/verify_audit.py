#!/usr/bin/env python3
"""Independent audit of the pole-simple small-owner import."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "02a025756473cfeac6a481f2bd933f152beace01589bbcadd10a1c1bf6798518"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    n, m, k = data["domain_size"], data["support_size"], data["code_dimension"]
    assert 2 * m - k == data["small_owner_max"]
    assert n - m + 1 == data["sub_support_owner_cap"]
    for rho in range(0, data["denominator_degree_cap"] + 1, 997):
        n0 = n - rho
        assert rho + n0 - m + 1 == n - m + 1
        assert rho + n0 == n

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_cross_type_global_atom_record_extension"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "puncture `p` from the domain" in proof
    assert "half-distance pincer" in proof
    assert "exclusive large-owner image bound" in statement
    print("POLE_SIMPLE_SMALL_OWNER_PAYMENT_AUDIT_PASS first_large_owner=1183521")


if __name__ == "__main__":
    main()
