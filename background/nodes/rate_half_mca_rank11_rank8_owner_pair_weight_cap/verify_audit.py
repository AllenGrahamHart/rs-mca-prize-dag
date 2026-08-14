#!/usr/bin/env python3
"""Independent audit of the rank-eight owner-pair weighted cap."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "478aa8e2affd878acaf36cd1fd313fcdb857b552e5edf28dda1e4ad1c59cb32c"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    p = json.loads(CONTRACT.read_text())["parameters"]
    outside = p["first_closed_n"] - p["fixed_subset_size"]
    pairs = outside * (outside - 1) // 2
    cap = (p["first_closed_n"] - p["first_closed_m"] + 1) * pairs
    require(pairs == p["coordinate_pair_resource"], "pair resource")
    require(cap == p["first_closed_weighted_cap"], "weighted cap")
    proof = (HERE / "proof.md").read_text()
    for pin in ("rank two", "uniquely", "sum_p q_p", "981105", "t_p q_p"):
        require(pin in proof, f"proof pin {pin}")
    print(
        "RATE_HALF_MCA_RANK11_RANK8_OWNER_PAIR_WEIGHT_CAP_AUDIT_PASS "
        f"pairs={pairs} cap={cap} proof_pins=5/5"
    )


if __name__ == "__main__":
    main()
