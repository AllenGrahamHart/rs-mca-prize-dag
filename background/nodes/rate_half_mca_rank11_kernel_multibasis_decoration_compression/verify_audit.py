#!/usr/bin/env python3
"""Independent proof-text audit for kernel basis multiplicity."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).parent
CONTRACT_SHA256 = "2db1ee7ecda1fb2498203ee3eec190f732d149e21e1aa8df87d8e52aafd16f52"


def main() -> None:
    contract_path = HERE / "source_contract.json"
    if hashlib.sha256(contract_path.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise SystemExit("contract hash")
    data = json.loads(contract_path.read_text())
    p = data["parameters"]
    multiplicities = []
    for d in range(1, 10):
        r = 10 - d
        outside = 11 - r
        multiplicities.append(1 + outside)
    if multiplicities != p["basis_multiplicities"]:
        raise SystemExit("multiplicity reconstruction")
    proof = (HERE / "proof.md").read_text()
    pins = (
        "has no loops",
        "fundamental circuit",
        "pairwise distinct",
        "did not use the canonical choice",
        "(d+2)I_d<=D_d",
    )
    if not all(pin in proof for pin in pins):
        raise SystemExit("proof pins")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_MULTIBASIS_DECORATION_COMPRESSION_AUDIT_PASS "
        f"multiplicities={multiplicities[0]}..{multiplicities[-1]} proof_pins={len(pins)}/{len(pins)}"
    )


if __name__ == "__main__":
    main()
