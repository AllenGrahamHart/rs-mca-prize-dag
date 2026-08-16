#!/usr/bin/env python3
"""Independent replay of the K'=71 carrier-trichotomy payment."""

from __future__ import annotations

import importlib.util
import itertools
import json
import re
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
PARENT_AUDIT = ROOT / "background/nodes/rate_half_mca_rank11_k60_k70_cross_support_collision_payment/verify_audit.py"
SUPPORTS = tuple(range(2, 10))
WEIGHTS = {support: comb(11 - support, 2) for support in SUPPORTS}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_parent():
    spec = importlib.util.spec_from_file_location("cross_audit_for_k71", PARENT_AUDIT)
    need(spec is not None and spec.loader is not None, "parent")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


OLD = load_parent()
BASE = OLD.BASE


def maximal(rows: dict[tuple[int, ...], str]):
    vectors = list(rows)
    result = [
        (rows[vector], vector)
        for vector in vectors
        if not any(
            other != vector
            and all(left <= right for left, right in zip(vector, other))
            for other in vectors
        )
    ]
    result.sort()
    return result


def fixed_union_count(K: int, m: int, union: int, dimension: int, target: int) -> int:
    intersection = dimension + 1 - target
    need(intersection > 0, "positive fixed intersection")
    budget = K - intersection - union
    total = comb(union, target)
    for external in range(1, target + 1):
        deletion_count = comb(union, target - external) * comb(
            m - union, external - 1
        )
        completions = max(0, budget - external + 1)
        total += deletion_count * completions // external
    return total


def charge(K: int, vector: tuple[int, ...], union: int, dimension: int):
    m = 67472 + K
    result = list(vector)
    for target in SUPPORTS:
        if target > dimension:
            continue
        cap = fixed_union_count(K, m, union, dimension, target) * comb(
            m - target, 11 - target
        )
        result[target - 2] = min(result[target - 2], cap)
    return tuple(result)


def low23(K: int, baseline: dict[int, int], s2: int, s3: int):
    cap2 = OLD.exact_caps(K, 2, s2, baseline)
    cap3 = OLD.exact_caps(K, 3, s3, baseline)
    return tuple(min(baseline[t], cap2[t], cap3[t]) for t in SUPPORTS)


def classify23(K: int, baseline: dict[int, int]):
    q = K - 10
    ordinary = {}
    one_step = []
    impossible = 0
    position_cases = 0
    for s2 in range(q + 1):
        for s3 in range(q + 1):
            vector = low23(K, baseline, s2, s3)
            M2, M3 = q - s2, q - s3
            if M2 > 0 and M3 > 0 and M3 <= M2:
                if s2 + s3 < q:
                    impossible += 1
                    continue
                b2, b3 = M2 + 1, M3 + 2
                transverse = charge(K, vector, b2 + b3, 7)
                anchor = charge(K, vector, b2 + b3 - 1, 8)
                ordinary[transverse] = f"s2={s2}/s3={s3}/T23"
                ordinary[anchor] = f"s2={s2}/s3={s3}/A23"
                position_cases += 2
            elif M2 > 0 and M3 == M2 + 1:
                one_step.append((s2, s3, vector))
                position_cases += 1
            else:
                ordinary[vector] = f"s2={s2}/s3={s3}/U23"
                position_cases += 1
    return ordinary, maximal(ordinary), one_step, impossible, position_cases


def all45(K: int, baseline: dict[int, int]):
    q = K - 10
    m = 67472 + K
    exact = []
    unique = {}
    for s4 in range(q + 1):
        cap4 = OLD.exact_caps(K, 4, s4, baseline)
        for s5 in range(q + 1):
            cap5 = OLD.exact_caps(K, 5, s5, baseline)
            vector = [min(baseline[t], cap4[t], cap5[t]) for t in SUPPORTS]
            if s4 + s5 < q:
                vector[2] = min(
                    vector[2], BASE.joint_support4_cap(K, m, s4, s5)
                )
            item = tuple(vector)
            exact.append((s4, s5, item))
            unique[item] = f"s4={s4}/s5={s5}"
    return exact, unique, maximal(unique)


def six_cases(M2: int):
    b2, b3, b4 = M2 + 1, M2 + 3, M2 + 4
    return {
        "T23": (b2 + b3, 7),
        "A23": (b2 + b3 - 1, 8),
        "T24": (b2 + b4, 6),
        "A24": (b2 + b4 - 1, 7),
        "N34": (b2 + 5, 6),
        "N34A": (b2 + 4, 7),
    }


def combine(*vectors):
    return tuple(min(values) for values in zip(*vectors))


def premium(vector):
    return sum(WEIGHTS[target] * vector[target - 2] for target in SUPPORTS)


def replay(K: int):
    q = K - 10
    m = 67472 + K
    baseline = BASE.baseline_caps(q, m)
    raw23, front23, one_step, impossible, position_cases = classify23(K, baseline)
    exact45, raw45, front45 = all45(K, baseline)
    raw69, front69 = OLD.PARENT.group_high(K, baseline)
    best = (-1, "", ())
    ordinary_leaves = 0
    one_step_leaves = 0
    trichotomy_leaves = 0
    geometry_max = {name: -1 for name in six_cases(1)}

    for left, middle, right in itertools.product(front23, front45, front69):
        vector = combine(left[1], middle[1], right[1])
        value = premium(vector)
        ordinary_leaves += 1
        if value > best[0]:
            best = (value, f"{left[0]}/{middle[0]}/{right[0]}/plain", vector)

    for s2, s3, left in one_step:
        M2 = q - s2
        cases = six_cases(M2)
        for s4, s5, middle in exact45:
            M4 = q - s4
            for right in front69:
                vector = combine(left, middle, right[1])
                prefix = f"s2={s2}/s3={s3}/s4={s4}/s5={s5}/{right[0]}"
                if M4 == M2 + 1:
                    for name, (union, dimension) in cases.items():
                        candidate = charge(K, vector, union, dimension)
                        value = premium(candidate)
                        geometry_max[name] = max(geometry_max[name], value)
                        trichotomy_leaves += 1
                        if value > best[0]:
                            best = (value, f"{prefix}/{name}", candidate)
                else:
                    value = premium(vector)
                    one_step_leaves += 1
                    if value > best[0]:
                        best = (value, f"{prefix}/plain", vector)

    defects = {
        str(support): int(re.search(rf"s{support}=([0-9]+)", best[1]).group(1))
        for support in range(2, 6)
    }
    return {
        "raw_defect_leaf_count": (q + 1) ** 4 * 120,
        "support23_unique_vector_count": len(raw23),
        "support23_maximal_vector_count": len(front23),
        "support23_one_step_pair_count": len(one_step),
        "support23_impossible_pair_count": impossible,
        "support23_position_case_count": position_cases,
        "support45_unique_vector_count": len(raw45),
        "support45_maximal_vector_count": len(front45),
        "support69_unique_vector_count": len(raw69),
        "support69_maximal_vector_count": len(front69),
        "ordinary_frontier_leaf_count": ordinary_leaves,
        "one_step_plain_leaf_count": one_step_leaves,
        "trichotomy_leaf_count": trichotomy_leaves,
        "trichotomy_case_max_premium": geometry_max,
        "active_small_defects": defects,
        "active_branch": best[1],
        "active_caps": {
            str(target): best[2][target - 2] for target in SUPPORTS
        },
        "completion_premium": best[0],
    }


def audit_row(K: int, declared: dict[str, object], wall: bool) -> int:
    q = K - 10
    n = 1048576 + K
    m = 67472 + K
    kernel = sum(
        comb(n, 10 - d) * BASE.kernel_record_cap(K, d) * comb(q, d + 1)
        for d in range(1, 10)
    )
    charts = {core: BASE.chart(K, core) for core in range(9, K)}
    max_core = max(charts, key=charts.get)
    marks = comb(n, 9) * charts[max_core]
    summary = replay(K)
    completion = summary["completion_premium"]
    full = (marks + BASE.RECORD_FLOOR * completion) // 55
    total = kernel + full
    demand = BASE.RECORD_FLOOR * comb(m, 11) - comb(n, 11)
    gap = demand - total
    coefficient = 55 * comb(m, 11) - completion
    raw = BASE.RECORD_FLOOR * coefficient - 55 * comb(n, 11) - 55 * kernel - marks
    ceiling = (
        BASE.RECORD_FLOOR * 55 * comb(m, 11)
        - 55 * comb(n, 11)
        - 55 * kernel
        - marks
        - 1
    ) // BASE.RECORD_FLOOR
    need(declared["n"] == n and declared["m"] == m and declared["q"] == q, "row")
    need(declared["max_core"] == max_core and declared["chart"] == charts[max_core], "chart")
    need(declared["kernel_capacity"] == kernel and declared["rank_nine_marks"] == marks, "fixed")
    for key, value in summary.items():
        need(declared[key] == value, f"summary {key}")
    need(declared["safe_premium_ceiling"] == ceiling, "ceiling")
    need(declared["premium_ceiling_margin"] == ceiling - completion, "margin")
    need(declared["full_rank_capacity"] == full and declared["total_capacity"] == total, "capacity")
    need(declared["required_component_incidence"] == demand, "demand")
    need(declared["record_coefficient_cross"] == coefficient, "coefficient")
    need(declared["floor_record_raw_cross"] == raw, "raw")
    if wall:
        need(declared["capacity_excess"] == -gap and gap < 0, "wall")
    else:
        need(declared["gap"] == gap and gap > 0, "closed")
    return gap


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    rows = data["parameters"]["rows"]
    gap = audit_row(71, rows["71"], False)
    wall = audit_row(72, rows["72"], True)
    need(data["parameters"]["remaining_rank9_interval"] == [72, 15528], "remaining")
    need(gap == 118872281099445772155993127155914865045379156488810154591370, "gap")
    need(-wall == 4821537739796415753639473905341364357966460110033651367468100, "wall excess")
    print(
        "RATE_HALF_MCA_RANK11_K71_CARRIER_TRICHOTOMY_PAYMENT_AUDIT_PASS "
        f"gap={gap} wall={-wall}"
    )


if __name__ == "__main__":
    main()
