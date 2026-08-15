#!/usr/bin/env python3
"""Verify the K'=60..70 cross-support collision payments."""

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
CONTRACT_SHA256 = "edcce8ae674f96b095193af674e42b55a1370c21b32382e2de717c1b5fbd5a09"
PARENT_VERIFY = ROOT / "background/nodes/rate_half_mca_rank11_k54_k59_small_support_collision_payment/verify.py"
CROSS_VERIFY = ROOT / "background/nodes/rate_half_mca_sparse_circuit_cross_support_collision_charge/verify.py"
SUPPORTS = tuple(range(2, 10))
CLOSED_ROWS = tuple(range(60, 71))
WALL_ROW = 71


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


PARENT = load_module("small_collision_parent_for_cross", PARENT_VERIFY)
CROSS = load_module("cross_support_collision", CROSS_VERIFY)
LEDGER = PARENT.LEDGER


def maximal_vectors(rows: dict[tuple[int, ...], str]):
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
    return maximal


def exact_cross_caps(
    kprime: int, source: int, defect: int, baseline: dict[int, int]
) -> dict[int, int]:
    q = kprime - 10
    m = 67472 + kprime
    caps = PARENT.exact_collision_caps(kprime, source, defect, baseline)
    if defect < q:
        for target in SUPPORTS:
            if source + target <= 11:
                caps[target] = min(
                    caps[target],
                    CROSS.incidence_cap(kprime, m, source, target, defect),
                )
    return caps


def small_group(kprime: int, baseline: dict[int, int], left: int, right: int):
    q = kprime - 10
    m = 67472 + kprime
    rows: dict[tuple[int, ...], str] = {}
    for s_left in range(q + 1):
        caps_left = exact_cross_caps(kprime, left, s_left, baseline)
        for s_right in range(q + 1):
            caps_right = exact_cross_caps(kprime, right, s_right, baseline)
            vector = [
                min(baseline[target], caps_left[target], caps_right[target])
                for target in SUPPORTS
            ]
            if (left, right) == (4, 5) and s_left + s_right < q:
                vector[2] = min(
                    vector[2],
                    PARENT.PARENT.JOINT.cap_for_defects(
                        kprime, m, s_left, s_right
                    )[0],
                )
            rows[tuple(vector)] = f"s{left}={s_left}/s{right}={s_right}"
    return rows, maximal_vectors(rows)


def high_group(kprime: int, baseline: dict[int, int]):
    return PARENT.group69(kprime, baseline)


def vector_digest(rows: list[tuple[str, tuple[int, ...]]]) -> str:
    digest = hashlib.sha256()
    for label, vector in rows:
        digest.update(f"{label}:{','.join(map(str, vector))}\n".encode())
    return digest.hexdigest()


@lru_cache(maxsize=None)
def branch_summary(kprime: int) -> dict[str, Any]:
    q = kprime - 10
    m = 67472 + kprime
    baseline = PARENT.PARENT.CAPS.baseline_caps(q, m)
    raw23, maximal23 = small_group(kprime, baseline, 2, 3)
    raw45, maximal45 = small_group(kprime, baseline, 4, 5)
    raw69, maximal69 = high_group(kprime, baseline)
    maximum = (-1, "", ())
    frontier_sum = 0
    frontier_digest = hashlib.sha256()
    for left, middle, right in itertools.product(maximal23, maximal45, maximal69):
        caps = tuple(
            min(left[1][index], middle[1][index], right[1][index])
            for index in range(len(SUPPORTS))
        )
        premium = sum(
            LEDGER.DEFICITS[target] * caps[index]
            for index, target in enumerate(SUPPORTS)
        )
        label = f"{left[0]}/{middle[0]}/{right[0]}"
        frontier_digest.update(f"{label}:{premium}\n".encode())
        frontier_sum += premium
        if premium > maximum[0]:
            maximum = (premium, label, caps)
    active_parts = maximum[1].split("/")
    return {
        "group_raw_choice_counts": {
            "23": (q + 1) ** 2,
            "45": (q + 1) ** 2,
            "69": 120,
        },
        "group_unique_vector_counts": {
            "23": len(raw23),
            "45": len(raw45),
            "69": len(raw69),
        },
        "group_maximal_vector_counts": {
            "23": len(maximal23),
            "45": len(maximal45),
            "69": len(maximal69),
        },
        "group_maximal_digest_sha256": {
            "23": vector_digest(maximal23),
            "45": vector_digest(maximal45),
            "69": vector_digest(maximal69),
        },
        "represented_raw_leaf_count": (q + 1) ** 4 * 120,
        "frontier_leaf_count": len(maximal23) * len(maximal45) * len(maximal69),
        "frontier_premium_sum": frontier_sum,
        "frontier_digest_sha256": frontier_digest.hexdigest(),
        "active_small_defects": {
            str(support): int(active_parts[support - 2].split("=")[1])
            for support in range(2, 6)
        },
        "active_branch": maximum[1],
        "active_caps": {
            str(target): maximum[2][index]
            for index, target in enumerate(SUPPORTS)
        },
        "completion_premium": maximum[0],
    }


@lru_cache(maxsize=None)
def expected(kprime: int) -> dict[str, Any]:
    old = LEDGER.row(kprime)
    n = 1048576 + kprime
    m = 67472 + kprime
    summary = branch_summary(kprime)
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
        "schema": "rate-half-mca-rank11-k60-k70-cross-support-collision-payment-v1",
        "dependencies": [
            "rate_half_mca_rank11_k54_k59_small_support_collision_payment",
            "rate_half_mca_sparse_circuit_cross_support_collision_charge",
        ],
        "parameters": {
            "closed_rows": list(CLOSED_ROWS),
            "new_closed_prefix": [10, 70],
            "first_method_wall": WALL_ROW,
            "residual_record_floor": LEDGER.RECORD_FLOOR,
            "exact_source_defects": [2, 3, 4, 5],
            "cross_support_condition": "c+d<=11 and s_c<q",
            "high_support_order": [6, 7, 8, 9],
            "deficit_weights": {
                str(support): LEDGER.DEFICITS[support] for support in SUPPORTS
            },
            "rows": rows,
            "remaining_rank9_interval": [71, 15528],
        },
        "claim": (
            "Exact low-support defects and cross-support collision charges "
            "close every rank-nine component row K'=60..70."
        ),
        "nonclaim": (
            "The same payment fails at K'=71. No c+d>=12 collision cap, "
            "rank-eight, rank-eleven, active-v4, KoalaBear, or prize closure "
            "is asserted."
        ),
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data == contract(), "exact contract")
    p = data["parameters"]
    require(isinstance(p, dict), "parameters")
    rows = p["rows"]
    minimum_gap = None
    leaves = 0
    for kprime in CLOSED_ROWS:
        row = rows[str(kprime)]
        active = (kprime - 10 + 1) // 2
        require(
            row["active_small_defects"]
            == {str(support): active for support in range(2, 6)},
            "active defects",
        )
        require(row["active_branch"].endswith("c6F/c7F/c8F/c9F"), "active high")
        require(row["group_maximal_vector_counts"]["69"] == 7, "high frontier")
        require(row["gap"] > 0 and row["premium_ceiling_margin"] > 0, "closed sign")
        require(row["floor_record_raw_cross"] > 0, "closed raw")
        minimum_gap = row["gap"] if minimum_gap is None else min(minimum_gap, row["gap"])
        leaves += row["represented_raw_leaf_count"]
    wall = rows[str(WALL_ROW)]
    require(
        wall["active_small_defects"]
        == {str(support): 31 for support in range(2, 6)},
        "wall defects",
    )
    require(wall["active_branch"].endswith("c6F/c7F/c8F/c9F"), "wall high")
    require(wall["capacity_excess"] > 0, "wall sign")
    require(wall["premium_ceiling_margin"] < 0 and wall["floor_record_raw_cross"] < 0, "wall raw")
    require(
        minimum_gap
        == 854274172985042754802177028749324962520517760595473749602211,
        "minimum gap",
    )
    require(
        wall["capacity_excess"]
        == 824875968499878215752683873455674299360608616555107905777434,
        "wall excess",
    )
    require(p["remaining_rank9_interval"] == [71, 15528], "remaining")
    require("fails at K'=71" in str(data["nonclaim"]), "nonclaim")
    return {"rows": len(CLOSED_ROWS), "minimum_gap": int(minimum_gap), "leaves": leaves}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("closed_rows", [60]),
        lambda item: item["parameters"].__setitem__("cross_support_condition", "c+d<=12"),
        lambda item: item["parameters"]["rows"]["60"].__setitem__("active_small_defects", {}),
        lambda item: item["parameters"]["rows"]["70"].__setitem__("gap", 0),
        lambda item: item["parameters"]["rows"]["71"].__setitem__("capacity_excess", 0),
        lambda item: item["parameters"].__setitem__("remaining_rank9_interval", [72, 15528]),
        lambda item: item.__setitem__("nonclaim", "K'=71 closed"),
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
        "RATE_HALF_MCA_RANK11_K60_K70_CROSS_SUPPORT_COLLISION_PAYMENT_PASS "
        f"rows={result['rows']} minimum_gap={result['minimum_gap']} "
        f"represented_leaves={result['leaves']} controls={controls}"
    )


if __name__ == "__main__":
    main()
