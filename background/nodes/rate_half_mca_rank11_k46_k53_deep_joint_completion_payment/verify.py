#!/usr/bin/env python3
"""Verify the K'=46..53 deep joint completion payments."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import itertools
import json
import sys
from functools import lru_cache
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "9c1f1aa7bfe20879f792cac64748da44436f8db6ed4996bfcc36da79527121a5"
PARENT_VERIFY = ROOT / "background/nodes/rate_half_mca_rank11_k45_full_completion_product_payment/verify.py"
SUPPORTS = tuple(range(2, 10))
OTHER_SUPPORTS = (2, 3, 6, 7, 8, 9)
CLOSED_ROWS = tuple(range(46, 54))
WALL_ROW = 54


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, f"module {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PARENT = load_module("k45_parent_for_deep_joint", PARENT_VERIFY)
LEDGER = PARENT.LEDGER
CAPS = PARENT.CAPS
JOINT = PARENT.JOINT


def exact_source_caps(
    q: int, m: int, support: int, defect: int, baseline: dict[int, int]
) -> dict[int, int]:
    if defect <= 9 - support:
        return PARENT.PARENT.terminal_caps(q, m, support, defect, baseline)
    caps = dict(baseline)
    caps[support] = min(
        caps[support], CAPS.deletion_cap(m, support, q - defect)
    )
    return caps


def other_branch_vectors(kprime: int, baseline: dict[int, int]):
    rows: dict[tuple[int, ...], str] = {}
    for choices in itertools.product(
        *(PARENT.source_options(kprime, support, baseline) for support in OTHER_SUPPORTS)
    ):
        caps = dict(baseline)
        labels = []
        for support, (label, _defect, local) in zip(OTHER_SUPPORTS, choices):
            labels.append(label)
            for target in SUPPORTS:
                caps[target] = min(caps[target], local[target])
        rows[tuple(caps[target] for target in SUPPORTS)] = "/".join(labels)
    return rows


def maximal_other_vectors(kprime: int, baseline: dict[int, int]):
    rows = other_branch_vectors(kprime, baseline)
    vectors = list(rows)
    maximal = []
    for vector in vectors:
        dominated = any(
            other != vector
            and all(left <= right for left, right in zip(vector, other))
            for other in vectors
        )
        if not dominated:
            maximal.append((rows[vector], vector))
    maximal.sort()
    return rows, maximal


def full_label(other_label: str, s4: int, s5: int) -> str:
    labels = other_label.split("/")
    return "/".join((labels[0], labels[1], f"c4d{s4}", f"c5d{s5}", *labels[2:]))


@lru_cache(maxsize=None)
def deep_summary(kprime: int) -> dict[str, Any]:
    q = kprime - 10
    m = 67472 + kprime
    baseline = CAPS.baseline_caps(q, m)
    all_other, maximal_other = maximal_other_vectors(kprime, baseline)
    other_digest = hashlib.sha256()
    for label, vector in maximal_other:
        other_digest.update(f"{label}:{','.join(map(str, vector))}\n".encode())

    pair_digest = hashlib.sha256()
    pair_sum = 0
    joint_pairs = 0
    joint_tightened = 0
    maximum = (-1, "", -1, -1, ())
    maximum_joint = (-1, "")
    maximum_nonjoint = (-1, "")

    for s4 in range(q + 1):
        caps4 = exact_source_caps(q, m, 4, s4, baseline)
        for s5 in range(q + 1):
            caps5 = exact_source_caps(q, m, 5, s5, baseline)
            pair_caps = [
                min(baseline[target], caps4[target], caps5[target])
                for target in SUPPORTS
            ]
            joint = s4 + s5 < q
            if joint:
                joint_pairs += 1
                cap = JOINT.cap_for_defects(kprime, m, s4, s5)[0]
                if cap < pair_caps[2]:
                    joint_tightened += 1
                pair_caps[2] = min(pair_caps[2], cap)

            pair_max = (-1, "", ())
            for other_label, other_caps in maximal_other:
                final_caps = tuple(
                    min(pair_caps[index], other_caps[index])
                    for index in range(len(SUPPORTS))
                )
                premium = sum(
                    LEDGER.DEFICITS[target] * final_caps[index]
                    for index, target in enumerate(SUPPORTS)
                )
                if premium > pair_max[0]:
                    pair_max = (premium, other_label, final_caps)
            label = full_label(pair_max[1], s4, s5)
            pair_digest.update(f"{s4},{s5}:{pair_max[0]}:{pair_max[1]}\n".encode())
            pair_sum += pair_max[0]
            if pair_max[0] > maximum[0]:
                maximum = (pair_max[0], label, s4, s5, pair_max[2])
            bucket = maximum_joint if joint else maximum_nonjoint
            if pair_max[0] > bucket[0]:
                if joint:
                    maximum_joint = (pair_max[0], label)
                else:
                    maximum_nonjoint = (pair_max[0], label)

    pair_count = (q + 1) ** 2
    return {
        "exact_pair_count": pair_count,
        "joint_pair_count": joint_pairs,
        "nonjoint_pair_count": pair_count - joint_pairs,
        "joint_tightened_pair_count": joint_tightened,
        "other_raw_branch_count": 9 * 8 * 5 * 4 * 3 * 2,
        "other_unique_vector_count": len(all_other),
        "other_maximal_vector_count": len(maximal_other),
        "other_maximal_digest_sha256": other_digest.hexdigest(),
        "raw_leaf_count": pair_count * 9 * 8 * 5 * 4 * 3 * 2,
        "pair_maximum_sum": pair_sum,
        "pair_maximum_digest_sha256": pair_digest.hexdigest(),
        "maximum_joint_premium": maximum_joint[0],
        "maximum_joint_branch": maximum_joint[1],
        "maximum_nonjoint_premium": maximum_nonjoint[0],
        "maximum_nonjoint_branch": maximum_nonjoint[1],
        "active_s4": maximum[2],
        "active_s5": maximum[3],
        "active_branch": maximum[1],
        "active_caps": {
            str(target): maximum[4][index]
            for index, target in enumerate(SUPPORTS)
        },
        "completion_premium": maximum[0],
    }


@lru_cache(maxsize=None)
def expected(kprime: int) -> dict[str, Any]:
    old = LEDGER.row(kprime)
    n = 1048576 + kprime
    m = 67472 + kprime
    summary = deep_summary(kprime)
    premium = int(summary["completion_premium"])
    marks = int(old["marks"])
    kernel = int(old["kernel"])
    full_rank = (marks + LEDGER.RECORD_FLOOR * premium) // 55
    total = kernel + full_rank
    demand = LEDGER.RECORD_FLOOR * comb(m, 11) - comb(n, 11)
    coefficient = 55 * comb(m, 11) - premium
    raw = (
        LEDGER.RECORD_FLOOR * coefficient
        - 55 * comb(n, 11)
        - 55 * kernel
        - marks
    )
    ceiling = (
        LEDGER.RECORD_FLOOR * 55 * comb(m, 11)
        - 55 * comb(n, 11)
        - 55 * kernel
        - marks
        - 1
    ) // LEDGER.RECORD_FLOOR
    return {
        "n": n,
        "m": m,
        "q": kprime - 10,
        "max_core": int(old["max_core"]),
        "chart": int(old["chart"]),
        "kernel_capacity": kernel,
        "rank_nine_marks": marks,
        **summary,
        "safe_premium_ceiling": ceiling,
        "premium_ceiling_margin": ceiling - premium,
        "full_rank_capacity": full_rank,
        "total_capacity": total,
        "required_component_incidence": demand,
        "gap": demand - total,
        "record_coefficient_cross": coefficient,
        "floor_record_raw_cross": raw,
    }


def contract() -> dict[str, object]:
    rows = {str(kprime): expected(kprime) for kprime in (*CLOSED_ROWS, WALL_ROW)}
    wall = dict(rows[str(WALL_ROW)])
    wall["capacity_excess"] = -wall.pop("gap")
    rows[str(WALL_ROW)] = wall
    return {
        "schema": "rate-half-mca-rank11-k46-k53-deep-joint-completion-payment-v1",
        "dependencies": [
            "rate_half_mca_rank11_k45_full_completion_product_payment",
            "rate_half_mca_sparse_circuit_support45_deep_defect_partition",
        ],
        "parameters": {
            "closed_rows": list(CLOSED_ROWS),
            "new_closed_prefix": [10, 53],
            "first_method_wall": WALL_ROW,
            "residual_record_floor": LEDGER.RECORD_FLOOR,
            "exact_support_defects": [4, 5],
            "other_support_order": list(OTHER_SUPPORTS),
            "deficit_weights": {
                str(support): LEDGER.DEFICITS[support] for support in SUPPORTS
            },
            "rows": rows,
            "remaining_rank9_interval": [54, 15528],
        },
        "claim": (
            "The exact deep support-four/support-five defect partition and joint "
            "charge close every rank-nine component row K'=46..53."
        ),
        "nonclaim": (
            "The same payment fails at K'=54. No rank-eight, rank-eleven, "
            "active-v4, KoalaBear, or prize closure is asserted."
        ),
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data == contract(), "exact contract")
    p = data["parameters"]
    require(isinstance(p, dict), "parameters")
    rows = p["rows"]
    require(isinstance(rows, dict), "rows")
    minimum_gap = None
    leaves = 0
    for kprime in CLOSED_ROWS:
        row = rows[str(kprime)]
        q = kprime - 10
        active = (q - 1) // 2
        require(row["active_s4"] == row["active_s5"] == active, "active defects")
        require(row["active_branch"].endswith("c6F/c7F/c8F/c9F"), "active other")
        require(row["other_maximal_vector_count"] == 9, "Pareto count")
        require(row["gap"] > 0 and row["premium_ceiling_margin"] > 0, "closed sign")
        require(row["floor_record_raw_cross"] > 0, "closed raw")
        minimum_gap = row["gap"] if minimum_gap is None else min(minimum_gap, row["gap"])
        leaves += row["raw_leaf_count"]
    wall = rows[str(WALL_ROW)]
    require(wall["active_s4"] == wall["active_s5"] == 21, "wall defects")
    require(wall["other_maximal_vector_count"] == 9, "wall Pareto")
    require(wall["capacity_excess"] > 0, "wall sign")
    require(wall["premium_ceiling_margin"] < 0 and wall["floor_record_raw_cross"] < 0, "wall raw")
    require(p["remaining_rank9_interval"] == [54, 15528], "remaining")
    require("fails at K'=54" in str(data["nonclaim"]), "nonclaim")
    return {"rows": len(CLOSED_ROWS), "minimum_gap": int(minimum_gap), "leaves": leaves}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("closed_rows", [46]),
        lambda item: item["parameters"]["rows"]["46"].__setitem__("exact_pair_count", 0),
        lambda item: item["parameters"]["rows"]["46"].__setitem__("other_maximal_vector_count", 8),
        lambda item: item["parameters"]["rows"]["53"].__setitem__("gap", 0),
        lambda item: item["parameters"]["rows"]["54"].__setitem__("capacity_excess", 0),
        lambda item: item["parameters"].__setitem__("remaining_rank9_interval", [53, 15528]),
        lambda item: item.__setitem__("nonclaim", "K'=54 closed"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (Reject, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "tamper controls")
    return rejected


def main() -> None:
    if sys.argv[1:] == ["--write"]:
        CONTRACT.write_text(json.dumps(contract(), indent=2) + "\n")
        print(f"WROTE {CONTRACT}")
        return
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    controls = tamper_selftest(data)
    print(
        "RATE_HALF_MCA_RANK11_K46_K53_DEEP_JOINT_COMPLETION_PAYMENT_PASS "
        f"rows={result['rows']} minimum_gap={result['minimum_gap']} "
        f"raw_leaves={result['leaves']} controls={controls}"
    )


if __name__ == "__main__":
    main()
