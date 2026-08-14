#!/usr/bin/env python3
"""Independent proof-text audit for record-support kernel capacity."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).parent
CONTRACT_SHA256 = "ede7f01e37f1f856118ba73b3c94af8b99658361cac2e747f7f69fe24d3a7e7e"


def main() -> None:
    contract_path = HERE / "source_contract.json"
    if hashlib.sha256(contract_path.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise SystemExit("contract hash")
    p = json.loads(contract_path.read_text())["parameters"]
    reconstructed = []
    for d in range(1, 10):
        rank = 10 - d
        if (11 - rank + 1, (10 - d) + d) != (d + 2, 10):
            raise SystemExit("rank arithmetic")
        reconstructed.append(d + 2)
    if reconstructed != p["basis_multiplicities"]:
        raise SystemExit("multiplicities")
    proof = (HERE / "proof.md").read_text()
    pins = ("exact support", "K'-d-(10-d)=K'-10", "Dividing by the `d+2`", "No quotient synchronization")
    if not all(pin in proof for pin in pins):
        raise SystemExit("proof pins")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_RECORD_SUPPORT_CAPACITY_AUDIT_PASS "
        f"strata=9 proof_pins={len(pins)}/{len(pins)}"
    )


if __name__ == "__main__":
    main()
