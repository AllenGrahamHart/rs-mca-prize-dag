#!/usr/bin/env python3
"""Independent audit of the rank-nine weighted component cap."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "d8000c85400cd931d846b9da91d7203720fb31cedce7abcd08318bf4879a22b5"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    p = json.loads(CONTRACT.read_text())["parameters"]
    d = p["n_offset"] - p["m_offset"]
    require(d == 981104 and p["fixed_owner_record_cap"] == d + 1, "fixed-owner cap")
    k = p["boundary_dimension"]
    n, m = p["n_offset"] + k, p["m_offset"] + k
    cap = (d + 1) * (m - p["component_subset_size"] + 1) * n
    require(cap == p["boundary_weighted_cap"], "boundary cap")
    proof = (HERE / "proof.md").read_text()
    for pin in ("unique owner point", "at least one lies", "pairwise disjoint", "981105"):
        require(pin in proof, f"proof pin {pin}")
    print(
        "RATE_HALF_MCA_RANK11_RANK9_WEIGHTED_COMPONENT_CAP_AUDIT_PASS "
        f"boundary_cap={cap} proof_pins=4/4"
    )


if __name__ == "__main__":
    main()
