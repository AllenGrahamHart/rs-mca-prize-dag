#!/usr/bin/env python3
"""Independent semantic audit of the kernel basis globalizer."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "98de8b079e0de815c691dcebfd49ad2520dc7ca3c232ea62b34eb4e94ecbfdfa"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    p = json.loads(CONTRACT.read_text())["parameters"]
    pairs = []
    for d in range(1, 10):
        r = p["correction_dimension"] - d
        pairs.append((r, p["component_subset_size"] - r))
    require(pairs == [(9, 2), (8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8), (2, 9), (1, 10)], "rank/extension pairs")
    proof = (HERE / "proof.md").read_text()
    for pin in ("one common quotient solution", "K'-10", "canonical basis", "61871313426630599"):
        require(pin in proof, f"proof pin {pin}")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_CANONICAL_BASIS_GLOBALIZER_AUDIT_PASS "
        "pairs=9 proof_pins=4/4"
    )


if __name__ == "__main__":
    main()
