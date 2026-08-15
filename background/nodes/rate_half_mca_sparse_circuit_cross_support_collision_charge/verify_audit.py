#!/usr/bin/env python3
"""Independent audit of the cross-support collision arithmetic."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def count(K: int, m: int, c: int, d: int, s: int) -> int:
    q = K - 10
    need(0 <= s < q and c + d <= 11, "domain")
    b = q + c - 1 - s
    if s == 0:
        return comb(b, d)
    N = m - b
    total = comb(b, d)
    for j in range(1, d + 1):
        deletions = comb(b, d - j) * comb(N, j - 1)
        total += deletions * (s + d - j) // j
    return total


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    need(p["source_support_range"] == [2, 5], "sources")
    need(p["target_support_range"] == [2, 9], "targets")
    need(p["empty_source_nonclaim"] == "s=q gives no target cap", "empty")
    samples = p["K60_defect25_samples"]
    checks = 0
    for c in range(2, 6):
        for d in range(2, 10):
            if c + d > 11:
                continue
            row = samples[str(c)][str(d)]
            value = count(60, 67532, c, d, 25)
            need(row["intersection_dimension"] == 12 - c - d > 0, "dimension")
            need(row["source_carrier_size"] == 50 + c - 1 - 25, "carrier")
            need(row["target_outside_budget"] == 25 + d - 1, "outside")
            need(row["target_support_count"] == value, "count")
            need(
                row["target_incidence_cap"]
                == value * comb(67532 - d, 11 - d),
                "incidence",
            )
            need(count(60, 67532, c, d, 0) == comb(50 + c - 1, d), "zero")
            checks += 1
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_CROSS_SUPPORT_COLLISION_CHARGE_AUDIT_PASS "
        f"checks={checks}"
    )


if __name__ == "__main__":
    main()
