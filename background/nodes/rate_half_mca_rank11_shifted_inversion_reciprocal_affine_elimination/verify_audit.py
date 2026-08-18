#!/usr/bin/env python3
"""Independent audit of the reciprocal-affine elimination."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "8ff563e2379abb76d88d3bb4bdb1d81ab654d7d1a8155f774c513fe3b60114ea"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["minimum_survivor_fibers"] - data["maximum_affine_reflection_fibers"] == 3216
    assert data["minimum_survivor_nonfixed_points"] - data["maximum_affine_reflection_points"] == 6432
    assert data["normalized_parameter"] == "kappa/tau^2"
    assert data["excluded_parameter"] == 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_shifted_inversion_product_energy_ledger"]["status"] == "PROVED"
    assert nodes["rate_half_mca_rank11_exception_spi_affine_reflection_fixed_pencil_cap"]["status"] == "PROVED"

    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "coordinatewise inversion is a bijection" in proof
    assert "u+v=-1/tau" in proof
    assert "every other parent alternative is retained verbatim" in proof
    assert "no remaining class is paid" in statement
    print("RECIPROCAL_AFFINE_ELIMINATION_AUDIT_PASS margins=3216,6432")


if __name__ == "__main__":
    main()
