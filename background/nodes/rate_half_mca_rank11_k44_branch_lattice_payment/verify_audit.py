#!/usr/bin/env python3
"""Independent arithmetic audit for the K'=44 branch-lattice payment."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
RECORD_FLOOR = 274980728111260126
DEPTHS = {2: 7, 3: 2, 4: 1, 5: 0}
DEFICITS = {support: comb(11 - support, 2) for support in range(2, 10)}
SOURCE_ORDER = (5, 4, 3, 2)
REFINED = {"c5_defect_2", "c5_defect_3"}


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


def base_caps(q: int, m: int) -> dict[int, int]:
    return {
        support: (
            defect_cap(q, m, support)
            if support <= 5
            else deletion_cap(m, support, q)
        )
        for support in range(2, 10)
    }


def terminal_caps(
    q: int, m: int, source: int, defect: int, inherited: dict[int, int]
) -> dict[int, int]:
    caps = dict(inherited)
    caps[source] = min(caps[source], deletion_cap(m, source, q - defect))
    for target in range(2, 10):
        if source + (defect + 1) * target - defect - 1 <= 10:
            carrier = q + source - 1 + defect * (target - 1)
            caps[target] = min(
                caps[target],
                comb(carrier, target) * comb(m - target, 11 - target),
            )
    return caps


def parent_leaves(kprime: int) -> dict[str, dict[int, int]]:
    q = kprime - 10
    m = 67472 + kprime
    inherited = base_caps(q, m)
    prefixes: list[str] = []
    leaves: dict[str, dict[int, int]] = {}
    for source in SOURCE_ORDER:
        for defect in range(10 - source):
            label = "__".join(prefixes + [f"c{source}_defect_{defect}"])
            leaves[label] = terminal_caps(q, m, source, defect, inherited)
        inherited = dict(inherited)
        inherited[source] = min(
            inherited[source], deletion_cap(m, source, q - (10 - source))
        )
        prefixes.append(f"c{source}_fallback")
    leaves["__".join(prefixes)] = inherited
    return leaves


def branch_premiums(kprime: int) -> dict[str, int]:
    q = kprime - 10
    m = 67472 + kprime
    leaves: dict[str, dict[int, int]] = {}
    for label, caps in parent_leaves(kprime).items():
        if label not in REFINED:
            leaves[label] = caps
            continue
        for defect in range(4):
            leaves[f"{label}__c6_defect_{defect}"] = terminal_caps(
                q, m, 6, defect, caps
            )
        fallback = dict(caps)
        fallback[6] = min(fallback[6], deletion_cap(m, 6, q - 4))
        leaves[f"{label}__c6_fallback"] = fallback
    return {
        label: sum(DEFICITS[support] * caps[support] for support in range(2, 10))
        for label, caps in leaves.items()
    }


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
    active = max(branches, key=branches.get)
    premium = branches[active]
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
    require(declared["active_branch"] == active == "c5_defect_2__c6_defect_2", "active")
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
        require(raw // 55 == gap - 1, "floor orientation")
    return gap, raw


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    gap44, _ = audit_row(44, p, False)
    gap45, _ = audit_row(45, p["K45_method_wall"], True)
    require(len(p["branch_premiums"]) == 35, "leaf count")
    print(
        "RATE_HALF_MCA_RANK11_K44_BRANCH_LATTICE_PAYMENT_AUDIT_PASS "
        f"gap={gap44} wall={-gap45} branches=70"
    )


if __name__ == "__main__":
    main()
