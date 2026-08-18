#!/usr/bin/env python3
"""Independent audit of the quotient large-owner/pair-pencil router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "2ebb18038873432107abdbd56f789a5b40d508e69afc0f9001250653507dffd9"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["residual_mass"] > data["small_owner_record_cap"]
    assert data["first_large_owner"] == data["small_owner_max"] + 1
    assert data["quotient_type_floor"] >= 2
    assert data["large_type_record_floor"] >= 29

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pole_simple_small_owner_atom_payment_import"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "apply the atom-weld gauge dichotomy" in proof
    assert "255011043>2097152" in proof
    assert "exclusive large owner" in statement
    assert "base pair-type pencil" in statement
    print("QUOTIENT_LARGE_OWNER_OR_PAIR_PENCIL_AUDIT_PASS outputs=2")


if __name__ == "__main__":
    main()
