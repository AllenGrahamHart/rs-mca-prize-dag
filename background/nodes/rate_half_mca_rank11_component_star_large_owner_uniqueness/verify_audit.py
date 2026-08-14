#!/usr/bin/env python3
"""Independent audit of component-star owner uniqueness."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "731e65b2926b11ef0d192e11fb55e5eac280e0d93038270fe131d79b9ca7b076"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    p = json.loads(CONTRACT.read_text())["parameters"]
    delta = p["large_owner_deficiency_ceiling"]
    root_gaps = []
    for k_value in (p["K_prime_min"], 100, 10000, p["K_prime_max"]):
        support = k_value + p["d"]
        forced_intersection = support - 2 * delta
        root_cap = k_value - 1
        root_gaps.append(forced_intersection - root_cap)
    require(root_gaps == [22833] * len(root_gaps), "constant shortening gap")
    require(2 * delta < p["d"], "strict uniqueness threshold")
    proof = (HERE / "proof.md").read_text()
    require("within-support pair cores" in proof and "K'+22832" in proof, "proof scope")
    print(
        "RATE_HALF_MCA_RANK11_COMPONENT_STAR_LARGE_OWNER_UNIQUENESS_AUDIT_PASS "
        f"rows={len(root_gaps)} root_gap={root_gaps[0]}"
    )


if __name__ == "__main__":
    main()
