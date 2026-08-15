#!/usr/bin/env python3
"""Independent omitted-pair and branch audit for the joint ledger."""

from __future__ import annotations

import json
from itertools import combinations, product
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    ground = set(range(11))
    omitted_pairs = list(combinations(range(11), 2))
    shadow_counts = []
    for support in range(2, 10):
        circuit = set(range(support))
        rank9 = sum(bool(circuit & set(pair)) for pair in omitted_pairs)
        rank8 = sum(not (circuit & set(pair)) for pair in omitted_pairs)
        require(rank9 + rank8 == len(omitted_pairs), "shadow partition")
        require(rank8 == len(list(combinations(ground - circuit, 2))), "rank-eight pairs")
        shadow_counts.append(rank9)
    require(shadow_counts == [19, 27, 34, 40, 45, 49, 52, 54], "full shadow table")
    require(shadow_counts[:4] == p["rank9_shadow_counts"], "contract low shadows")
    require(min(shadow_counts[4:]) == p["baseline_shadow_cost"], "high minimum")

    branch_checks = 0
    branches = ((2, 0, 1, 1), (0, 2, 2, 0))
    weights = tuple(p["premium_weights"])
    branch_premium = max(sum(w * cap for w, cap in zip(weights, branch)) for branch in branches)
    for first in branches:
        for second in branches:
            limits = tuple(left + right for left, right in zip(first, second))
            for incidences in product(*(range(limit + 1) for limit in limits)):
                actual_premium = sum(w * count for w, count in zip(weights, incidences))
                require(actual_premium <= 2 * branch_premium, "mixed branch premium")
                branch_checks += 1
    print(
        "PASS joint sparse/high rank-nine shadow ledger independent: "
        f"shadow table {shadow_counts}, {branch_checks} mixed-branch checks"
    )


if __name__ == "__main__":
    main()
