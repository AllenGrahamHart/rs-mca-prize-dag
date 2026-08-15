#!/usr/bin/env python3
"""Independent omitted-pair audit for the full-deficit ledger."""

from __future__ import annotations

import json
from itertools import combinations
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    pairs = tuple(combinations(range(11), 2))
    shadows = []
    deficits = []
    for support in range(2, 12):
        circuit = set(range(support))
        rank9 = sum(bool(circuit & set(pair)) for pair in pairs)
        rank8 = sum(not (circuit & set(pair)) for pair in pairs)
        require(rank9 + rank8 == len(pairs), "partition")
        require(rank8 == comb(11 - support, 2), "deficit")
        shadows.append(rank9)
        deficits.append(rank8)
    require(shadows == p["rank9_shadow_counts"], "shadow table")
    require(deficits == p["deficit_weights"], "deficit table")
    require(min(shadows[-2:]) == 55, "zero-deficit supports")
    print(
        "RATE_HALF_MCA_RANK9_FULL_CIRCUIT_DEFICIT_LEDGER_AUDIT_PASS "
        f"pairs={len(pairs)} supports={len(shadows)}"
    )


if __name__ == "__main__":
    main()
