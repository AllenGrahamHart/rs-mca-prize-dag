#!/usr/bin/env python3
"""Independent arithmetic audit for the K'=42 cross-support payment."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
RECORD_FLOOR = 274980728111260126
DEPTHS = {2: 7, 3: 2, 4: 1, 5: 0}
DEFICITS = {support: comb(11 - support, 2) for support in range(2, 10)}


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
    zero = Fraction(
        falling(1048576 + shortened, corank + 1),
        (67472 + shortened) * rising(67473, corank - 1),
    )
    endpoint = Fraction(
        falling(1048576 + corank, corank + 1), rising(67473, corank)
    )
    return int(max(zero, endpoint))


def chart(kprime: int, core: int) -> int:
    n = 1048576 + kprime
    m = 67472 + kprime
    petal = m - core
    total = n - core
    offset = core - 9
    light = total - 8 * (petal - 1)
    clean = 8 * light * (comb(petal - 1, 2) + offset * petal)
    heavy_minimum = petal // 2 + 1
    heavy_count = total // heavy_minimum
    cross = petal * petal // 4
    balanced = comb(total, 2) * (cross + offset * petal) // cross
    collision = comb(heavy_count, 2) * (comb(petal - 1, 2) + offset * petal)
    return clean + balanced + collision


def completion_value(m: int, support: int, completions: int) -> int:
    return completions * comb(m - support + 1 - completions, 11 - support)


def deletion_cap(m: int, support: int, ceiling: int) -> int:
    return (
        comb(m, support - 1)
        * max(completion_value(m, support, b) for b in range(ceiling + 1))
        // support
    )


def defect_cap(q: int, m: int, support: int) -> int:
    depth = DEPTHS[support]
    deletion = deletion_cap(m, support, q - depth - 1)
    carriers = [
        comb(q + (defect + 1) * (support - 1), support)
        * comb(m - support, 11 - support)
        for defect in range(1, depth + 1)
    ]
    return max([deletion] + carriers)


def universal_cap(q: int, m: int, support: int) -> int:
    return deletion_cap(m, support, q)


def branch_premiums(kprime: int) -> dict[str, int]:
    q = kprime - 10
    m = 67472 + kprime
    base = {
        support: (
            defect_cap(q, m, support)
            if support <= 5
            else universal_cap(q, m, support)
        )
        for support in range(2, 10)
    }
    result = {}
    for defect in range(5):
        caps = dict(base)
        caps[5] = min(caps[5], deletion_cap(m, 5, q - defect))
        for target in range(2, 10):
            if 5 + (defect + 1) * target - defect - 1 <= 10:
                cross = comb(q + 4 + defect * (target - 1), target) * comb(
                    m - target, 11 - target
                )
                caps[target] = min(caps[target], cross)
        result[f"defect_{defect}"] = sum(
            DEFICITS[support] * caps[support] for support in range(2, 10)
        )
    caps = dict(base)
    caps[5] = min(caps[5], deletion_cap(m, 5, q - 5))
    result["fallback"] = sum(
        DEFICITS[support] * caps[support] for support in range(2, 10)
    )
    return result


def audit_row(kprime: int, declared: dict[str, object], wall: bool) -> tuple[int, int]:
    n = 1048576 + kprime
    m = 67472 + kprime
    q = kprime - 10
    kernel = sum(
        comb(n, 10 - corank)
        * kernel_record_cap(kprime, corank)
        * comb(q, corank + 1)
        for corank in range(1, 10)
    )
    charts = {core: chart(kprime, core) for core in range(9, kprime)}
    maximizing_core = max(charts, key=charts.get)
    chart_cap = charts[maximizing_core]
    marks = comb(n, 9) * chart_cap
    branches = branch_premiums(kprime)
    premium = max(branches.values())
    full_rank = (marks + RECORD_FLOOR * premium) // 55
    total = kernel + full_rank
    demand = RECORD_FLOOR * comb(m, 11) - comb(n, 11)
    gap = demand - total
    coefficient = 55 * comb(m, 11) - premium
    raw = RECORD_FLOOR * coefficient - 55 * comb(n, 11) - 55 * kernel - marks

    require(declared["n"] == n and declared["m"] == m and declared["q"] == q, "row")
    require(maximizing_core == kprime - 1, "last core maximizes")
    require(declared["max_core"] == maximizing_core, "core")
    require(declared["chart"] == chart_cap, "chart")
    require(declared["kernel_capacity"] == kernel, "kernel")
    require(declared["rank_nine_marks"] == marks, "marks")
    require(declared["branch_premiums"] == branches, "branches")
    require(declared["completion_premium"] == premium, "premium")
    require(declared["full_rank_capacity"] == full_rank, "full rank")
    require(declared["total_capacity"] == total, "total")
    require(declared["required_component_incidence"] == demand, "demand")
    require(declared["record_coefficient_cross"] == coefficient and coefficient > 0, "coefficient")
    require(declared["floor_record_raw_cross"] == raw, "raw")
    if wall:
        require(declared["capacity_excess"] == -gap and gap < 0 and raw < 0, "wall")
    else:
        require(declared["isolated_global_cap"] == comb(n, 11), "isolated")
        require(declared["gap"] == gap and gap > 0 and raw > 0, "closed")
        require(raw // 55 == gap - 1 and raw % 55 == 51, "floor orientation")
    return gap, raw


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    gap42, _ = audit_row(42, p, False)
    gap43, _ = audit_row(43, p["K43_method_wall"], True)
    require(max(p["branch_premiums"], key=p["branch_premiums"].get) == "fallback", "K42 active")
    require(
        max(p["K43_method_wall"]["branch_premiums"], key=p["K43_method_wall"]["branch_premiums"].get)
        == "fallback",
        "K43 active",
    )
    print(
        "RATE_HALF_MCA_RANK11_K42_CROSS_SUPPORT_DEFECT_PAYMENT_AUDIT_PASS "
        f"gap={gap42} wall={-gap43} branches=12"
    )


if __name__ == "__main__":
    main()
