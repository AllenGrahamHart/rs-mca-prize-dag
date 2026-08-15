#!/usr/bin/env python3
"""Verify the paving-matroid basis-floor contract arithmetic."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "e9090a0719eaabde0fe291fb61237841aae14b51765f5c482ba110632304e648"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> int:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "matroid-paving-basis-floor-v1", "schema")
    require(data.get("dependencies") == [], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("minimum_rank") == 2, "rank range")
    require(p.get("minimum_ground_size") == "m>=r", "ground range")
    require(p.get("basis_floor") == "C(m-1,r-1)", "basis floor")
    require(p.get("pascal_identity") is True, "Pascal identity")
    require(p.get("sharp") is True, "sharpness")
    ranks = p.get("audited_ranks")
    require(ranks == list(range(2, 11)), "audited ranks")
    checks = 0
    for rank in ranks:
        for size in range(rank + 1, rank + 25):
            deletion = comb(size - 2, rank - 1)
            contraction = comb(size - 2, rank - 2)
            require(deletion + contraction == comb(size - 1, rank - 1), "Pascal recurrence")
            checks += 1
        require(comb(rank - 1, rank - 1) == 1, "base case")
        require(comb(rank + 8 - 1, rank - 1) > 0, "coloop extremizer")
    require("does not establish" in str(data.get("nonclaim")), "nonclaim")
    return checks


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    checks = validate(data)
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("minimum_rank", 1),
        lambda item: item["parameters"].__setitem__("basis_floor", "C(m-2,r-1)"),
        lambda item: item["parameters"].__setitem__("pascal_identity", False),
        lambda item: item["parameters"].__setitem__("sharp", False),
        lambda item: item["parameters"].__setitem__("audited_ranks", list(range(2, 10))),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "MATROID_PAVING_BASIS_FLOOR_PASS "
        f"checks={checks} ranks=9 controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
