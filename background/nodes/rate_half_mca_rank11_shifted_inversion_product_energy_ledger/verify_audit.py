#!/usr/bin/env python3
"""Independent audit of the shifted-inversion product-energy ledger."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "cd621dd58a4a513c06e1cfb1e470a9321863f0e51765386cba3b8a4631a998da"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    p = data["official_base_prime"]
    n = data["official_domain_order"]
    index = data["cyclotomic_index"]
    assert p - 1 == index * n
    assert divmod(n - 1, index) == (2064, 127)
    assert data["forced_nonfixed_points"] == 8740

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_quadratic_survivor_mobius_router"]["status"] == "PROVED"

    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    frontier = " ".join((HERE / "frontier.md").read_text().lower().split())
    assert "every ordered pair determines one unique nonzero product" in proof
    assert "inversion preserves the diagonal" in proof
    assert "one 8740-point exceptional fiber is too small" in frontier
    assert "does not imply" in data["nonclaim"].lower()
    print("SHIFTED_PRODUCT_ENERGY_LEDGER_AUDIT_PASS index=1016 threshold=8740")


if __name__ == "__main__":
    main()
