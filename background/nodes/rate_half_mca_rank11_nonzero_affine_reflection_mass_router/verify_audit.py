#!/usr/bin/env python3
"""Independent audit of the nonzero affine-reflection mass router."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "d85fb9f733083381b0e8137972dfd8562fcc1646c80abae355fa27f9bd1593a8"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    mass = data["triple_owner_mass"]
    types = data["maximum_pair_types"]
    charge = data["nonzero_affine_fixed_pencil_cap"]
    assert data["maximum_small_type_records"] < charge
    charged = types * charge
    residual = mass - charged
    assert charged == 67348594
    assert residual == 255011043
    quotient, remainder = divmod(residual, types)
    assert (quotient, remainder) == (4369, 31834)
    assert quotient + 1 == 4370 >= data["synchronization_threshold"]

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_multi_anchor_exchange_split_pencil_synchronization"]["status"] == "PROVED"
    assert nodes["rate_half_mca_rank11_exception_spi_affine_reflection_fixed_pencil_cap"]["status"] == "PROVED"

    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    frontier = " ".join((HERE / "frontier.md").read_text().lower().split())
    assert "first-owner pair types have disjoint record currencies" in proof
    assert "does not assert equality of pencils across types" in proof
    assert "does not close this koalabear threshold" in frontier
    assert "does not pay" in data["nonclaim"].lower()
    print("RANK11_AFFINE_MASS_ROUTER_AUDIT_PASS residual=255011043 forced=4370")


if __name__ == "__main__":
    main()
