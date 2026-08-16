#!/usr/bin/env python3
"""Independent audit of the small-support collision arithmetic."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def count(K: int, m: int, c: int, s: int) -> int:
    q = K - 10
    if s == q:
        return 0
    b = q + c - 1 - s
    if s == 0:
        return comb(b, c)
    N = m - b
    total = comb(b, c)
    for j in range(1, c + 1):
        deletions = comb(b, c - j) * comb(N, j - 1)
        total += deletions * (s + c - j) // j
    return total


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    need(p["support_range"] == [2, 5], "supports")
    samples = p["K54_defect22_samples"]
    checks = 0
    for c in range(2, 6):
        row = samples[str(c)]
        value = count(54, 67526, c, 22)
        need(row["intersection_dimension"] == 12 - 2 * c > 0, "dimension")
        need(row["carrier_size"] == 44 + c - 1 - 22, "carrier")
        need(row["outside_budget"] == 22 + c - 1, "outside")
        need(row["support_count"] == value, "count")
        need(row["incidence_cap"] == value * comb(67526 - c, 11 - c), "incidence")
        need(count(54, 67526, c, 44) == 0, "empty")
        checks += c
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_SMALL_SUPPORT_SELF_COLLISION_CHARGE_AUDIT_PASS "
        f"checks={checks}"
    )


if __name__ == "__main__":
    main()
