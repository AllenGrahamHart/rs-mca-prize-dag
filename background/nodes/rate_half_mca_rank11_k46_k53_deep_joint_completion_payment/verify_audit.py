#!/usr/bin/env python3
"""Independent audit of the K'=46..53 deep joint payments."""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
PARENT_AUDIT = ROOT / "background/nodes/rate_half_mca_rank11_k45_full_completion_product_payment/verify_audit.py"
SUPPORTS = tuple(range(2, 10))
OTHER_SUPPORTS = (2, 3, 6, 7, 8, 9)
DEFICITS = {support: comb(11 - support, 2) for support in SUPPORTS}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_parent():
    spec = importlib.util.spec_from_file_location("k45_independent_for_deep", PARENT_AUDIT)
    need(spec is not None and spec.loader is not None, "parent")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


P = load_parent()


def source_options(kprime: int, support: int, baseline: dict[int, int]):
    q = kprime - 10
    m = 67472 + kprime
    rows = [
        (f"c{support}d{defect}", P.terminal_caps(q, m, support, defect, baseline))
        for defect in range(10 - support)
    ]
    fallback = dict(baseline)
    fallback[support] = min(
        fallback[support], P.deletion_cap(m, support, q - (10 - support))
    )
    rows.append((f"c{support}F", fallback))
    return rows


def exact_caps(q: int, m: int, support: int, defect: int, baseline: dict[int, int]):
    if defect <= 9 - support:
        return P.terminal_caps(q, m, support, defect, baseline)
    caps = dict(baseline)
    caps[support] = min(caps[support], P.deletion_cap(m, support, q - defect))
    return caps


def maximal_other(kprime: int, baseline: dict[int, int]):
    rows = {}
    for choices in itertools.product(
        *(source_options(kprime, support, baseline) for support in OTHER_SUPPORTS)
    ):
        caps = dict(baseline)
        labels = []
        for support, (label, local) in zip(OTHER_SUPPORTS, choices):
            labels.append(label)
            for target in SUPPORTS:
                caps[target] = min(caps[target], local[target])
        rows[tuple(caps[target] for target in SUPPORTS)] = "/".join(labels)
    vectors = list(rows)
    maximal = [
        (rows[vector], vector)
        for vector in vectors
        if not any(
            other != vector
            and all(left <= right for left, right in zip(vector, other))
            for other in vectors
        )
    ]
    maximal.sort()
    return rows, maximal


def branch(kprime: int) -> dict[str, object]:
    q = kprime - 10
    m = 67472 + kprime
    baseline = P.baseline_caps(q, m)
    raw, maximal = maximal_other(kprime, baseline)
    digest = hashlib.sha256()
    other_digest = hashlib.sha256()
    for label, vector in maximal:
        other_digest.update(f"{label}:{','.join(map(str, vector))}\n".encode())
    total = 0
    maximum = (-1, -1, -1, "", ())
    max_joint = (-1, "")
    max_nonjoint = (-1, "")
    joint_count = 0
    tightened = 0
    for s4 in range(q + 1):
        a = exact_caps(q, m, 4, s4, baseline)
        for s5 in range(q + 1):
            b = exact_caps(q, m, 5, s5, baseline)
            pair = [min(baseline[t], a[t], b[t]) for t in SUPPORTS]
            joint = s4 + s5 < q
            if joint:
                joint_count += 1
                cap = P.joint_support4_cap(kprime, m, s4, s5)
                if cap < pair[2]:
                    tightened += 1
                pair[2] = min(pair[2], cap)
            local = (-1, "", ())
            for label, vector in maximal:
                caps = tuple(min(pair[i], vector[i]) for i in range(8))
                premium = sum(DEFICITS[t] * caps[i] for i, t in enumerate(SUPPORTS))
                if premium > local[0]:
                    local = (premium, label, caps)
            digest.update(f"{s4},{s5}:{local[0]}:{local[1]}\n".encode())
            total += local[0]
            labels = local[1].split("/")
            full = "/".join((labels[0], labels[1], f"c4d{s4}", f"c5d{s5}", *labels[2:]))
            if local[0] > maximum[0]:
                maximum = (local[0], s4, s5, full, local[2])
            bucket = max_joint if joint else max_nonjoint
            if local[0] > bucket[0]:
                if joint:
                    max_joint = (local[0], full)
                else:
                    max_nonjoint = (local[0], full)
    pairs = (q + 1) ** 2
    return {
        "exact_pair_count": pairs,
        "joint_pair_count": joint_count,
        "nonjoint_pair_count": pairs - joint_count,
        "joint_tightened_pair_count": tightened,
        "other_raw_branch_count": 8640,
        "other_unique_vector_count": len(raw),
        "other_maximal_vector_count": len(maximal),
        "other_maximal_digest_sha256": other_digest.hexdigest(),
        "raw_leaf_count": pairs * 8640,
        "pair_maximum_sum": total,
        "pair_maximum_digest_sha256": digest.hexdigest(),
        "maximum_joint_premium": max_joint[0],
        "maximum_joint_branch": max_joint[1],
        "maximum_nonjoint_premium": max_nonjoint[0],
        "maximum_nonjoint_branch": max_nonjoint[1],
        "active_s4": maximum[1],
        "active_s5": maximum[2],
        "active_branch": maximum[3],
        "active_caps": {str(t): maximum[4][i] for i, t in enumerate(SUPPORTS)},
        "completion_premium": maximum[0],
    }


def audit_row(kprime: int, declared: dict[str, object], wall: bool) -> int:
    q = kprime - 10
    n = 1048576 + kprime
    m = 67472 + kprime
    kernel = sum(
        comb(n, 10 - d) * P.kernel_record_cap(kprime, d) * comb(q, d + 1)
        for d in range(1, 10)
    )
    charts = {core: P.chart(kprime, core) for core in range(9, kprime)}
    max_core = max(charts, key=charts.get)
    marks = comb(n, 9) * charts[max_core]
    summary = branch(kprime)
    premium = int(summary["completion_premium"])
    full = (marks + P.RECORD_FLOOR * premium) // 55
    total = kernel + full
    demand = P.RECORD_FLOOR * comb(m, 11) - comb(n, 11)
    gap = demand - total
    coefficient = 55 * comb(m, 11) - premium
    raw = P.RECORD_FLOOR * coefficient - 55 * comb(n, 11) - 55 * kernel - marks
    ceiling = (
        P.RECORD_FLOOR * 55 * comb(m, 11)
        - 55 * comb(n, 11) - 55 * kernel - marks - 1
    ) // P.RECORD_FLOOR
    need(declared["n"] == n and declared["m"] == m and declared["q"] == q, "row")
    need(declared["max_core"] == max_core, "core")
    need(declared["chart"] == charts[max_core], "chart")
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
    gaps = [audit_row(k, rows[str(k)], False) for k in range(46, 54)]
    wall = audit_row(54, rows["54"], True)
    need(data["parameters"]["remaining_rank9_interval"] == [54, 15528], "remaining")
    print(
        "RATE_HALF_MCA_RANK11_K46_K53_DEEP_JOINT_COMPLETION_PAYMENT_AUDIT_PASS "
        f"rows=8 minimum_gap={min(gaps)} wall={-wall}"
    )


if __name__ == "__main__":
    main()
