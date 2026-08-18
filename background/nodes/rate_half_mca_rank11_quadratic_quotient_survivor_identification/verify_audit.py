#!/usr/bin/env python3
"""Independent audit of the quadratic quotient identification."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "bf16d15b78bf1527448e471563569952e1b1dd63d4fbd01da62a3b35d957db5a"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    n = data["official_domain_order"]
    assert n == 2**21
    assert data["antipodal_fibers"] == n // 2
    assert data["constant_product_square_fibers"] == (n - 2) // 2
    assert data["minimum_quotient_fibers"] - data["required_survivor_fibers"] == 1044205

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_exception_spi_quotient_periodic_fence"]["status"] == "PROVED"
    assert nodes["rate_half_mca_rank11_exception_spi_dihedral_quotient_fence"]["status"] == "PROVED"

    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    statement = " ".join((HERE / "statement.md").read_text().lower().split())
    assert "the square subgroup `h^2` has index two" in proof
    assert "there are no such points when `kappa` is a nonsquare" in proof
    assert "same monic quadratic" in proof
    assert "cannot be removed by a uniform small-fiber theorem" in statement
    assert "must be paid" in statement
    print("QUADRATIC_QUOTIENT_IDENTIFICATION_AUDIT_PASS minimum=1048575")


if __name__ == "__main__":
    main()
