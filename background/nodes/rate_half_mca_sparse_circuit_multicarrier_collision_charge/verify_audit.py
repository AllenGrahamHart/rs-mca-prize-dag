#!/usr/bin/env python3
"""Independent audit of the fixed-union collision arithmetic."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def recount(K: int, m: int, union: int, dimension: int, target: int) -> int:
    r = dimension + 1 - target
    budget = K - r - union
    total = comb(union, target)
    for external in range(1, target + 1):
        deletion_count = comb(union, target - external) * comb(
            m - union, external - 1
        )
        completions = max(0, budget - (external - 1))
        total += deletion_count * completions // external
    return total


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    samples = data["parameters"]["K71_samples"]
    checks = 0
    for row in samples.values():
        K = row["K"]
        m = row["m"]
        union = row["union_size"]
        dimension = row["fixed_dimension"]
        for target_text, value in row["targets"].items():
            target = int(target_text)
            count = recount(K, m, union, dimension, target)
            need(value["target_support_count"] == count, "count")
            need(
                value["target_incidence_cap"]
                == count * comb(m - target, 11 - target),
                "incidence",
            )
            checks += 1
    need(checks == 29, "check census")
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_MULTICARRIER_COLLISION_CHARGE_AUDIT_PASS "
        f"checks={checks}"
    )


if __name__ == "__main__":
    main()
