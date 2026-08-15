#!/usr/bin/env python3
"""Independent arithmetic audit for the K'=45 full completion product."""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
RECORD_FLOOR = 274980728111260126
SUPPORTS = tuple(range(2, 10))
DEPTHS = {2: 7, 3: 2, 4: 1, 5: 0}
DEFICITS = {support: comb(11 - support, 2) for support in SUPPORTS}


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
    candidates = [deletion_cap(m, support, q - depth - 1)]
    candidates.extend(
        comb(q + (defect + 1) * (support - 1), support)
        * comb(m - support, 11 - support)
        for defect in range(1, depth + 1)
    )
    return max(candidates)


def baseline_caps(q: int, m: int) -> dict[int, int]:
    return {
        support: (
            defect_cap(q, m, support)
            if support <= 5
            else deletion_cap(m, support, q)
        )
        for support in SUPPORTS
    }


def terminal_caps(
    q: int, m: int, source: int, defect: int, baseline: dict[int, int]
) -> dict[int, int]:
    caps = dict(baseline)
    caps[source] = min(caps[source], deletion_cap(m, source, q - defect))
    for target in SUPPORTS:
        if source + (defect + 1) * target - defect - 1 <= 10:
            carrier = q + source - 1 + defect * (target - 1)
            caps[target] = min(
                caps[target],
                comb(carrier, target) * comb(m - target, 11 - target),
            )
    return caps


def joint_support4_cap(K: int, m: int, s4: int, s5: int) -> int:
    candidates = []
    for delta in range(min(s4, s5) + 1):
        for t in range(4, 7):
            b = K - t - delta
            outside = m - b
            if delta == 0:
                count = comb(b, 4)
            else:
                count = comb(b, 4) + sum(
                    comb(b, 4 - j)
                    * comb(outside, j - 1)
                    * (delta + 4 - j)
                    // j
                    for j in range(1, 5)
                )
            candidates.append(count * comb(m - 4, 7))
    return max(candidates)


def branch_summary(kprime: int) -> dict[str, object]:
    q = kprime - 10
    m = 67472 + kprime
    baseline = baseline_caps(q, m)
    option_table = {}
    for support in SUPPORTS:
        options = [
            (f"c{support}d{defect}", defect, terminal_caps(q, m, support, defect, baseline))
            for defect in range(10 - support)
        ]
        fallback = dict(baseline)
        fallback[support] = min(
            fallback[support], deletion_cap(m, support, q - (10 - support))
        )
        options.append((f"c{support}F", None, fallback))
        option_table[support] = options

    digest = hashlib.sha256()
    premium_sum = 0
    leaf_count = 0
    joint_count = 0
    tightened_count = 0
    maxima = {
        "all": (-1, ""),
        "before": (-1, ""),
        "joint": (-1, ""),
        "nonjoint": (-1, ""),
    }
    for choices in itertools.product(*(option_table[support] for support in SUPPORTS)):
        caps = dict(baseline)
        defects = {}
        labels = []
        for support, (label, defect, local) in zip(SUPPORTS, choices):
            labels.append(label)
            defects[support] = defect
            for target in SUPPORTS:
                caps[target] = min(caps[target], local[target])
        label = "/".join(labels)
        before = sum(DEFICITS[target] * caps[target] for target in SUPPORTS)
        if before > maxima["before"][0]:
            maxima["before"] = (before, label)
        paired = defects[4] is not None and defects[5] is not None
        if paired:
            joint_count += 1
            require(q > int(defects[4]) + int(defects[5]), "joint overlap condition")
            cap = joint_support4_cap(kprime, m, int(defects[4]), int(defects[5]))
            if cap < caps[4]:
                tightened_count += 1
            caps[4] = min(caps[4], cap)
        premium = sum(DEFICITS[target] * caps[target] for target in SUPPORTS)
        key = "joint" if paired else "nonjoint"
        if premium > maxima[key][0]:
            maxima[key] = (premium, label)
        if premium > maxima["all"][0]:
            maxima["all"] = (premium, label)
        digest.update(f"{label}:{premium}\n".encode())
        premium_sum += premium
        leaf_count += 1

    return {
        "option_counts": {str(support): len(option_table[support]) for support in SUPPORTS},
        "leaf_count": leaf_count,
        "joint_branch_count": joint_count,
        "nonjoint_branch_count": leaf_count - joint_count,
        "joint_tightened_count": tightened_count,
        "maximum_before_joint": maxima["before"][0],
        "maximum_before_joint_branch": maxima["before"][1],
        "maximum_joint_premium": maxima["joint"][0],
        "maximum_joint_branch": maxima["joint"][1],
        "maximum_nonjoint_premium": maxima["nonjoint"][0],
        "maximum_nonjoint_branch": maxima["nonjoint"][1],
        "active_branch": maxima["all"][1],
        "completion_premium": maxima["all"][0],
        "premium_sum": premium_sum,
        "branch_digest_sha256": digest.hexdigest(),
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
    max_core = max(charts, key=charts.get)
    chart_cap = charts[max_core]
    marks = comb(n, 9) * chart_cap
    summary = branch_summary(kprime)
    premium = int(summary["completion_premium"])
    full_rank = (marks + RECORD_FLOOR * premium) // 55
    total = kernel + full_rank
    demand = RECORD_FLOOR * comb(m, 11) - comb(n, 11)
    gap = demand - total
    coefficient = 55 * comb(m, 11) - premium
    raw = RECORD_FLOOR * coefficient - 55 * comb(n, 11) - 55 * kernel - marks
    ceiling = (
        RECORD_FLOOR * 55 * comb(m, 11)
        - 55 * comb(n, 11)
        - 55 * kernel
        - marks
        - 1
    ) // RECORD_FLOOR

    require(declared["n"] == n and declared["m"] == m and declared["q"] == q, "row")
    require(declared["max_core"] == max_core == kprime - 1, "core")
    require(declared["chart"] == chart_cap, "chart")
    require(declared["kernel_capacity"] == kernel, "kernel")
    require(declared["rank_nine_marks"] == marks, "marks")
    for key, value in summary.items():
        require(declared[key] == value, f"branch {key}")
    require(declared["safe_premium_ceiling"] == ceiling, "ceiling")
    require(declared["premium_ceiling_margin"] == ceiling - premium, "margin")
    require(declared["full_rank_capacity"] == full_rank, "full rank")
    require(declared["total_capacity"] == total, "total")
    require(declared["required_component_incidence"] == demand, "demand")
    require(declared["record_coefficient_cross"] == coefficient, "coefficient")
    require(declared["floor_record_raw_cross"] == raw, "raw")
    if wall:
        require(declared["capacity_excess"] == -gap and gap < 0 and raw < 0, "wall")
    else:
        require(declared["gap"] == gap and gap > 0 and raw > 0, "closed")
        require(raw // 55 == gap - 1, "floor orientation")
    return gap, int(summary["leaf_count"])


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    gap, leaves45 = audit_row(45, p["K45"], False)
    wall, leaves46 = audit_row(46, p["K46_method_wall"], True)
    require(leaves45 == leaves46 == 362880, "leaf totals")
    require(p["remaining_rank9_interval"] == [46, 15528], "remaining")
    print(
        "RATE_HALF_MCA_RANK11_K45_FULL_COMPLETION_PRODUCT_PAYMENT_AUDIT_PASS "
        f"leaves={leaves45 + leaves46} gap={gap} wall={-wall}"
    )


if __name__ == "__main__":
    main()
