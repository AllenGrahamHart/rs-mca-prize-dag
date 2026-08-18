#!/usr/bin/env python3
"""Independent audit of the quadratic quotient population router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "ec7a5f0f4d30192ffd155c02c644d28c74c7e902c9eff425ff457e6976ca09e5"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    complement = data["official_domain_order"] - (data["official_agreement"] - 2)
    assert complement == 981106
    assert complement // 2 == data["quotient_type_cap"] == 490553
    assert 519 * 490553 == data["floor_predecessor_capacity"] < data["synchronized_residual_records"]
    assert 520 * 490553 == data["floor_capacity"] >= data["synchronized_residual_records"]

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_nonzero_affine_reflection_mass_router"]["status"] == "PROVED"
    assert nodes["rate_half_mca_rank11_quadratic_quotient_factor_through_interface"]["status"] == "PROVED"

    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "pairwise-disjoint exception locators" in proof
    assert "the first-owner partition" in proof
    assert "ceil(255011043/490553)=520" in statement
    assert "distinct first-owned pair types carry" in statement
    assert "not one exceptional pencil" in statement
    print("QUADRATIC_QUOTIENT_POPULATION_AUDIT_PASS cap=490553 floor=520")


if __name__ == "__main__":
    main()
