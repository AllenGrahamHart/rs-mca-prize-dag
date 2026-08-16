#!/usr/bin/env python3
"""Independent audit of the K'=54..59 collision payments."""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
PARENT_AUDIT = ROOT / "background/nodes/rate_half_mca_rank11_k46_k53_deep_joint_completion_payment/verify_audit.py"
SUPPORTS = tuple(range(2, 10))
DEFICITS = {support: comb(11 - support, 2) for support in SUPPORTS}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_parent():
    spec = importlib.util.spec_from_file_location("deep_audit_for_collision", PARENT_AUDIT)
    need(spec is not None and spec.loader is not None, "parent")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PARENT = load_parent()
BASE = PARENT.P


def collision_count(K: int, m: int, c: int, s: int) -> int:
    q = K - 10
    if s == q:
        return 0
    b = q + c - 1 - s
    if s == 0:
        return comb(b, c)
    N = m - b
    total = comb(b, c)
    for j in range(1, c + 1):
        total += comb(b, c - j) * comb(N, j - 1) * (s + c - j) // j
    return total


def collision_cap(K: int, m: int, c: int, s: int) -> int:
    return collision_count(K, m, c, s) * comb(m - c, 11 - c)


def exact_caps(K: int, c: int, s: int, baseline: dict[int, int]):
    q = K - 10
    m = 67472 + K
    if s <= 9 - c:
        caps = BASE.terminal_caps(q, m, c, s, baseline)
    else:
        caps = dict(baseline)
        ceiling = q - s
        caps[c] = min(
            caps[c], 0 if ceiling == 0 else BASE.deletion_cap(m, c, ceiling)
        )
    caps[c] = min(caps[c], collision_cap(K, m, c, s))
    return caps


def maximal(rows: dict[tuple[int, ...], str]):
    vectors = list(rows)
    result = [
        (rows[v], v)
        for v in vectors
        if not any(
            w != v and all(a <= b for a, b in zip(v, w))
            for w in vectors
        )
    ]
    result.sort()
    return result


def group_small(K: int, baseline: dict[int, int], left: int, right: int):
    q = K - 10
    rows = {}
    for s_left in range(q + 1):
        a = exact_caps(K, left, s_left, baseline)
        for s_right in range(q + 1):
            b = exact_caps(K, right, s_right, baseline)
            vector = [min(baseline[t], a[t], b[t]) for t in SUPPORTS]
            if (left, right) == (4, 5) and s_left + s_right < q:
                vector[2] = min(
                    vector[2], BASE.joint_support4_cap(K, 67472 + K, s_left, s_right)
                )
            rows[tuple(vector)] = f"s{left}={s_left}/s{right}={s_right}"
    return rows, maximal(rows)


def group_high(K: int, baseline: dict[int, int]):
    rows = {}
    for choices in itertools.product(
        *(PARENT.source_options(K, c, baseline) for c in (6, 7, 8, 9))
    ):
        caps = dict(baseline)
        labels = []
        for c, (label, local) in zip((6, 7, 8, 9), choices):
            labels.append(label)
            for target in SUPPORTS:
                caps[target] = min(caps[target], local[target])
        rows[tuple(caps[t] for t in SUPPORTS)] = "/".join(labels)
    return rows, maximal(rows)


def digest(rows) -> str:
    value = hashlib.sha256()
    for label, vector in rows:
        value.update(f"{label}:{','.join(map(str, vector))}\n".encode())
    return value.hexdigest()


def branch(K: int) -> dict[str, object]:
    q = K - 10
    m = 67472 + K
    baseline = BASE.baseline_caps(q, m)
    raw23, front23 = group_small(K, baseline, 2, 3)
    raw45, front45 = group_small(K, baseline, 4, 5)
    raw69, front69 = group_high(K, baseline)
    maximum = (-1, "", ())
    total = 0
    stream = hashlib.sha256()
    for a, b, c in itertools.product(front23, front45, front69):
        caps = tuple(min(a[1][i], b[1][i], c[1][i]) for i in range(8))
        premium = sum(DEFICITS[t] * caps[i] for i, t in enumerate(SUPPORTS))
        label = f"{a[0]}/{b[0]}/{c[0]}"
        stream.update(f"{label}:{premium}\n".encode())
        total += premium
        if premium > maximum[0]:
            maximum = (premium, label, caps)
    parts = maximum[1].split("/")
    return {
        "group_raw_choice_counts": {"23": (q + 1) ** 2, "45": (q + 1) ** 2, "69": 120},
        "group_unique_vector_counts": {"23": len(raw23), "45": len(raw45), "69": len(raw69)},
        "group_maximal_vector_counts": {"23": len(front23), "45": len(front45), "69": len(front69)},
        "group_maximal_digest_sha256": {"23": digest(front23), "45": digest(front45), "69": digest(front69)},
        "represented_raw_leaf_count": (q + 1) ** 4 * 120,
        "frontier_leaf_count": len(front23) * len(front45) * len(front69),
        "frontier_premium_sum": total,
        "frontier_digest_sha256": stream.hexdigest(),
        "active_small_defects": {str(c): int(parts[c - 2].split("=")[1]) for c in range(2, 6)},
        "active_branch": maximum[1],
        "active_caps": {str(t): maximum[2][i] for i, t in enumerate(SUPPORTS)},
        "completion_premium": maximum[0],
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
    summary = branch(K)
    premium = int(summary["completion_premium"])
    full = (marks + BASE.RECORD_FLOOR * premium) // 55
    total = kernel + full
    demand = BASE.RECORD_FLOOR * comb(m, 11) - comb(n, 11)
    gap = demand - total
    coefficient = 55 * comb(m, 11) - premium
    raw = BASE.RECORD_FLOOR * coefficient - 55 * comb(n, 11) - 55 * kernel - marks
    ceiling = (
        BASE.RECORD_FLOOR * 55 * comb(m, 11)
        - 55 * comb(n, 11) - 55 * kernel - marks - 1
    ) // BASE.RECORD_FLOOR
    need(declared["n"] == n and declared["m"] == m and declared["q"] == q, "row")
    need(declared["max_core"] == max_core and declared["chart"] == charts[max_core], "chart")
    need(declared["kernel_capacity"] == kernel and declared["rank_nine_marks"] == marks, "fixed")
    for key, value in summary.items():
        need(declared[key] == value, f"branch {key}")
    need(declared["safe_premium_ceiling"] == ceiling, "ceiling")
    need(declared["premium_ceiling_margin"] == ceiling - premium, "margin")
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
    gaps = [audit_row(K, rows[str(K)], False) for K in range(54, 60)]
    wall = audit_row(60, rows["60"], True)
    need(data["parameters"]["remaining_rank9_interval"] == [60, 15528], "remaining")
    print(
        "RATE_HALF_MCA_RANK11_K54_K59_SMALL_SUPPORT_COLLISION_PAYMENT_AUDIT_PASS "
        f"rows=6 minimum_gap={min(gaps)} wall={-wall}"
    )


if __name__ == "__main__":
    main()
