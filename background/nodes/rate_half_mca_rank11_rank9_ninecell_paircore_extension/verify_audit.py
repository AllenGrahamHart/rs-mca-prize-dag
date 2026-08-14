#!/usr/bin/env python3
"""Independent audit of the nine-cell pair-core extension."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "8d91c142853cbc92720abb7372d677287dd1e83d3755e12361d322a617d2fe78"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    n, m, j = p["n"], p["m"], 2 * p["m"] - p["n"] - 1
    coefficient = n - m + 1
    checks = 0
    for core in range(2 * m - n, m):
        multiplicity = (n - core) // (m - core)
        require(
            multiplicity * (multiplicity - 1)
            <= coefficient * (core - j),
            f"owner core {core}",
        )
        checks += 1
    resource = coefficient * (n - 9)
    cap = 1434405
    require(resource == p["ordered_pair_resource_ceiling"], "resource")
    require(cap * (cap - 1) <= resource < (cap + 1) * cap, "bracket")
    proof = (HERE / "proof.md").read_text()
    require("2057517483015" in proof and "j=|J|>=9" in proof, "proof scope")
    print(
        "RATE_HALF_MCA_RANK11_RANK9_NINECELL_PAIRCORE_EXTENSION_AUDIT_PASS "
        f"core_checks={checks} resource={resource} cap={cap}"
    )


if __name__ == "__main__":
    main()
