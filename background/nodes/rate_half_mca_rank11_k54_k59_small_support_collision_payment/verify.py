#!/usr/bin/env python3
"""Verify the K'=54..59 small-support collision payments."""

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
CONTRACT_SHA256 = "3eac696cd20b5468cbfe7565f14fef6964b72b793800ef810d9db72fa17b9922"
PARENT_VERIFY = ROOT / "background/nodes/rate_half_mca_rank11_k46_k53_deep_joint_completion_payment/verify.py"
COLLISION_VERIFY = ROOT / "background/nodes/rate_half_mca_sparse_circuit_small_support_self_collision_charge/verify.py"
SUPPORTS = tuple(range(2, 10))
CLOSED_ROWS = tuple(range(54, 60))
WALL_ROW = 60


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


PARENT = load_module("deep_joint_parent_for_collision", PARENT_VERIFY)
COLLISION = load_module("small_support_collision", COLLISION_VERIFY)
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


def exact_collision_caps(
    kprime: int, support: int, defect: int, baseline: dict[int, int]
) -> dict[int, int]:
    q = kprime - 10
    m = 67472 + kprime
    caps = PARENT.exact_source_caps(q, m, support, defect, baseline)
    caps[support] = min(
        caps[support], COLLISION.incidence_cap(kprime, m, support, defect)
    )
    return caps


def group23(kprime: int, baseline: dict[int, int]):
    q = kprime - 10
    rows: dict[tuple[int, ...], str] = {}
    for s2 in range(q + 1):
        caps2 = exact_collision_caps(kprime, 2, s2, baseline)
        for s3 in range(q + 1):
            caps3 = exact_collision_caps(kprime, 3, s3, baseline)
            vector = tuple(
                min(baseline[target], caps2[target], caps3[target])
                for target in SUPPORTS
            )
            rows[vector] = f"s2={s2}/s3={s3}"
    return rows, maximal_vectors(rows)


def group45(kprime: int, baseline: dict[int, int]):
    q = kprime - 10
    m = 67472 + kprime
    rows: dict[tuple[int, ...], str] = {}
    for s4 in range(q + 1):
        caps4 = exact_collision_caps(kprime, 4, s4, baseline)
        for s5 in range(q + 1):
            caps5 = exact_collision_caps(kprime, 5, s5, baseline)
            vector = [
                min(baseline[target], caps4[target], caps5[target])
                for target in SUPPORTS
            ]
            if s4 + s5 < q:
                vector[2] = min(
                    vector[2],
                    PARENT.JOINT.cap_for_defects(kprime, m, s4, s5)[0],
                )
            rows[tuple(vector)] = f"s4={s4}/s5={s5}"
    return rows, maximal_vectors(rows)


def group69(kprime: int, baseline: dict[int, int]):
    rows: dict[tuple[int, ...], str] = {}
    for choices in itertools.product(
        *(PARENT.PARENT.source_options(kprime, support, baseline)
          for support in (6, 7, 8, 9))
    ):
        caps = dict(baseline)
        labels = []
        for support, (label, _defect, local) in zip((6, 7, 8, 9), choices):
            labels.append(label)
            for target in SUPPORTS:
                caps[target] = min(caps[target], local[target])
        rows[tuple(caps[target] for target in SUPPORTS)] = "/".join(labels)
    return rows, maximal_vectors(rows)


def vector_digest(rows: list[tuple[str, tuple[int, ...]]]) -> str:
    digest = hashlib.sha256()
    for label, vector in rows:
        digest.update(f"{label}:{','.join(map(str, vector))}\n".encode())
    return digest.hexdigest()


@lru_cache(maxsize=None)
def branch_summary(kprime: int) -> dict[str, Any]:
    q = kprime - 10
    m = 67472 + kprime
    baseline = PARENT.CAPS.baseline_caps(q, m)
    raw23, maximal23 = group23(kprime, baseline)
    raw45, maximal45 = group45(kprime, baseline)
    raw69, maximal69 = group69(kprime, baseline)
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
        "schema": "rate-half-mca-rank11-k54-k59-small-support-collision-payment-v1",
        "dependencies": [
            "rate_half_mca_rank11_k46_k53_deep_joint_completion_payment",
            "rate_half_mca_sparse_circuit_small_support_self_collision_charge",
        ],
        "parameters": {
            "closed_rows": list(CLOSED_ROWS),
            "new_closed_prefix": [10, 59],
            "first_method_wall": WALL_ROW,
            "residual_record_floor": LEDGER.RECORD_FLOOR,
            "exact_support_defects": [2, 3, 4, 5],
            "high_support_order": [6, 7, 8, 9],
            "deficit_weights": {
                str(support): LEDGER.DEFICITS[support] for support in SUPPORTS
            },
            "rows": rows,
            "remaining_rank9_interval": [60, 15528],
        },
        "claim": (
            "Exact support-2..5 defects and same-source collision charges "
            "close every rank-nine component row K'=54..59."
        ),
        "nonclaim": (
            "The same payment fails at K'=60. No support-six collision cap, "
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
        active = (kprime - 10) // 2
        require(
            row["active_small_defects"]
            == {str(support): active for support in range(2, 6)},
            "active defects",
        )
        require(row["active_branch"].endswith("c6F/c7F/c8F/c9F"), "active high")
        require(row["group_maximal_vector_counts"] == {"23": 1, "45": 1, "69": 7}, "frontiers")
        require(row["gap"] > 0 and row["premium_ceiling_margin"] > 0, "closed sign")
        require(row["floor_record_raw_cross"] > 0, "closed raw")
        minimum_gap = row["gap"] if minimum_gap is None else min(minimum_gap, row["gap"])
        leaves += row["represented_raw_leaf_count"]
    wall = rows[str(WALL_ROW)]
    require(wall["active_small_defects"] == {str(support): 25 for support in range(2, 6)}, "wall defects")
    require(wall["group_maximal_vector_counts"] == {"23": 1, "45": 1, "69": 7}, "wall frontiers")
    require(wall["capacity_excess"] > 0, "wall sign")
    require(wall["premium_ceiling_margin"] < 0 and wall["floor_record_raw_cross"] < 0, "wall raw")
    require(p["remaining_rank9_interval"] == [60, 15528], "remaining")
    require("fails at K'=60" in str(data["nonclaim"]), "nonclaim")
    return {"rows": len(CLOSED_ROWS), "minimum_gap": int(minimum_gap), "leaves": leaves}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("closed_rows", [54]),
        lambda item: item["parameters"]["rows"]["54"]["group_maximal_vector_counts"].__setitem__("23", 2),
        lambda item: item["parameters"]["rows"]["54"].__setitem__("active_small_defects", {}),
        lambda item: item["parameters"]["rows"]["59"].__setitem__("gap", 0),
        lambda item: item["parameters"]["rows"]["60"].__setitem__("capacity_excess", 0),
        lambda item: item["parameters"].__setitem__("remaining_rank9_interval", [59, 15528]),
        lambda item: item.__setitem__("nonclaim", "K'=60 closed"),
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
        "RATE_HALF_MCA_RANK11_K54_K59_SMALL_SUPPORT_COLLISION_PAYMENT_PASS "
        f"rows={result['rows']} minimum_gap={result['minimum_gap']} "
        f"represented_leaves={result['leaves']} controls={controls}"
    )


if __name__ == "__main__":
    main()
