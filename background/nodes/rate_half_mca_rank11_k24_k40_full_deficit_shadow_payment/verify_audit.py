#!/usr/bin/env python3
"""Independent arithmetic audit of the K'=24..40 payment."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
RECORD_FLOOR = 274980728111260126


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def kernel_record_cap(kprime: int, corank: int) -> int:
    if corank == 1:
        return 8147918
    if corank == 9:
        return 61871313426630599
    rank = 10 - corank
    shortened = kprime - rank
    return int(
        max(
            Fraction(
                falling(1048576 + shortened, corank + 1),
                (67472 + shortened) * rising(67473, corank - 1),
            ),
            Fraction(
                falling(1048576 + corank, corank + 1),
                rising(67473, corank),
            ),
        )
    )


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    rows = p["rows"]
    checks = 0
    gaps = []
    for kprime in range(24, 42):
        n = 1048576 + kprime
        m = 67472 + kprime
        q = kprime - 10
        declared = rows[str(kprime)]
        kernel = sum(
            comb(n, 10 - corank)
            * kernel_record_cap(kprime, corank)
            * comb(q, corank + 1)
            for corank in range(1, 10)
        )
        marks = comb(n, 9) * declared["chart"]
        full_rank = (marks + RECORD_FLOOR * declared["premium"]) // 55
        total = kernel + full_rank
        demand = (
            990810934 * RECORD_FLOOR * comb(m, 11) + 10**9 - 1
        ) // 10**9
        gap = demand - total
        coefficient = 55 * 990810934 * comb(m, 11) - 10**9 * declared["premium"]
        raw = RECORD_FLOOR * coefficient - 10**9 * (55 * kernel + marks)
        require(gap == declared["gap"], f"gap {kprime}")
        require(declared["max_core"] == kprime - 1, f"core {kprime}")
        require(coefficient > 0, f"coefficient {kprime}")
        if kprime <= 40:
            require(gap > 0 and raw > 0, f"closed {kprime}")
            gaps.append(gap)
        else:
            require(gap < 0 and raw < 0, "wall")
        checks += 1

    require(min(gaps) == rows["40"]["gap"], "minimum closed gap")
    require(all(left > right for left, right in zip(gaps, gaps[1:])), "gap decrease")
    require(-rows["41"]["gap"] == p["K41_method_wall"]["capacity_excess"], "wall excess")
    print(
        "RATE_HALF_MCA_RANK11_K24_K40_FULL_DEFICIT_SHADOW_PAYMENT_AUDIT_PASS "
        f"checks={checks} minimum_gap={min(gaps)} wall={-rows['41']['gap']}"
    )


if __name__ == "__main__":
    main()
