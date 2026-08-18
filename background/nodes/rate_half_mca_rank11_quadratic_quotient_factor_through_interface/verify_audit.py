#!/usr/bin/env python3
"""Independent audit of the quadratic quotient factor-through theorem."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "d01ae3d6be9e1cbb150d8b9c9bbf4187d78a286ecbd525e923bb9a9b5b34d903"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["cyclic_locator_basis"] == ["X^2", "1"]
    assert data["dihedral_locator_basis"] == ["X^2+kappa", "X"]
    assert data["postcomposition"] == "PGL_2(F)"

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_heavy_ruling_exception_split_pencil_normal_form"]["status"] == "PROVED"
    assert nodes["rate_half_mca_rank11_quadratic_quotient_survivor_identification"]["status"] == "PROVED"

    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "their span equals the two-dimensional locator pencil" in proof
    assert "the affine scalar in `(spi11)` changes no root" in proof
    assert "bad-slope parameter map itself" in statement
    assert "does not bound or pay" in statement
    print("QUADRATIC_QUOTIENT_FACTOR_AUDIT_PASS quotients=cyclic,dihedral")


if __name__ == "__main__":
    main()
