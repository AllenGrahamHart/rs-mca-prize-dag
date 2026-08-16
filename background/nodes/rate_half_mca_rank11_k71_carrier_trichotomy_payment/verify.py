#!/usr/bin/env python3
"""Verify the K'=71 carrier-position trichotomy payment."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import itertools
import json
import re
import sys
from functools import lru_cache
from math import comb
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "3c56c182cdb219df31cc4e98913b8e52ce625ec94c21d1fe48deab534ba6c0fc"
PARENT_VERIFY = ROOT / "background/nodes/rate_half_mca_rank11_k60_k70_cross_support_collision_payment/verify.py"
MULTI_VERIFY = ROOT / "background/nodes/rate_half_mca_sparse_circuit_multicarrier_collision_charge/verify.py"
TRICHOTOMY_VERIFY = ROOT / "background/nodes/rate_half_mca_sparse_circuit_k71_carrier_position_trichotomy/verify.py"
SUPPORTS = tuple(range(2, 10))
CLOSED_ROW = 71
WALL_ROW = 72


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


PARENT = load_module("cross_collision_parent_for_k71", PARENT_VERIFY)
MULTI = load_module("multicarrier_collision_for_k71", MULTI_VERIFY)
TRICHOTOMY = load_module("carrier_trichotomy_for_k71", TRICHOTOMY_VERIFY)
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


def charged_vector(
    kprime: int,
    vector: tuple[int, ...] | list[int],
    union: int,
    dimension: int,
) -> tuple[int, ...]:
    m = 67472 + kprime
    result = list(vector)
    for target in SUPPORTS:
        if dimension + 1 - target <= 0:
            continue
        result[target - 2] = min(
            result[target - 2],
            MULTI.incidence_cap(kprime, m, union, dimension, target),
        )
    return tuple(result)


def base23_vector(
    kprime: int,
    baseline: dict[int, int],
    s2: int,
    s3: int,
) -> tuple[int, ...]:
    caps2 = PARENT.exact_cross_caps(kprime, 2, s2, baseline)
    caps3 = PARENT.exact_cross_caps(kprime, 3, s3, baseline)
    return tuple(
        min(baseline[target], caps2[target], caps3[target])
        for target in SUPPORTS
    )


def position23_group(kprime: int, baseline: dict[int, int]):
    q = kprime - 10
    ordinary: dict[tuple[int, ...], str] = {}
    one_step: list[tuple[int, int, tuple[int, ...]]] = []
    impossible = 0
    position_cases = 0
    for s2 in range(q + 1):
        for s3 in range(q + 1):
            vector = base23_vector(kprime, baseline, s2, s3)
            M2 = q - s2
            M3 = q - s3
            if M2 > 0 and M3 > 0 and M3 <= M2:
                if s2 + s3 < q:
                    impossible += 1
                    continue
                b2 = M2 + 1
                b3 = M3 + 2
                transverse = charged_vector(kprime, vector, b2 + b3, 7)
                anchor = charged_vector(kprime, vector, b2 + b3 - 1, 8)
                ordinary[transverse] = f"s2={s2}/s3={s3}/T23"
                ordinary[anchor] = f"s2={s2}/s3={s3}/A23"
                position_cases += 2
            elif M2 > 0 and M3 == M2 + 1:
                one_step.append((s2, s3, vector))
                position_cases += 1
            else:
                ordinary[vector] = f"s2={s2}/s3={s3}/U23"
                position_cases += 1
    return ordinary, maximal_vectors(ordinary), one_step, impossible, position_cases


def exact45_rows(kprime: int, baseline: dict[int, int]):
    q = kprime - 10
    m = 67472 + kprime
    exact = []
    unique: dict[tuple[int, ...], str] = {}
    for s4 in range(q + 1):
        caps4 = PARENT.exact_cross_caps(kprime, 4, s4, baseline)
        for s5 in range(q + 1):
            caps5 = PARENT.exact_cross_caps(kprime, 5, s5, baseline)
            vector = [
                min(baseline[target], caps4[target], caps5[target])
                for target in SUPPORTS
            ]
            if s4 + s5 < q:
                vector[2] = min(
                    vector[2],
                    PARENT.PARENT.PARENT.JOINT.cap_for_defects(
                        kprime, m, s4, s5
                    )[0],
                )
            item = tuple(vector)
            exact.append((s4, s5, item))
            unique[item] = f"s4={s4}/s5={s5}"
    return exact, unique, maximal_vectors(unique)


def premium(vector: tuple[int, ...]) -> int:
    return sum(
        LEDGER.DEFICITS[target] * vector[target - 2]
        for target in SUPPORTS
    )


def combine(*vectors: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(min(values) for values in zip(*vectors))


@lru_cache(maxsize=None)
def branch_summary(kprime: int) -> dict[str, Any]:
    q = kprime - 10
    m = 67472 + kprime
    baseline = PARENT.PARENT.PARENT.CAPS.baseline_caps(q, m)
    raw23, front23, one_step, impossible, position_cases = position23_group(
        kprime, baseline
    )
    exact45, raw45, front45 = exact45_rows(kprime, baseline)
    raw69, front69 = PARENT.high_group(kprime, baseline)
    maximum = (-1, "", ())
    ordinary_leaves = 0
    one_step_leaves = 0
    trichotomy_leaves = 0
    trichotomy_max = {name: -1 for name in TRICHOTOMY.six_cases(1)}

    for left, middle, right in itertools.product(front23, front45, front69):
        caps = combine(left[1], middle[1], right[1])
        value = premium(caps)
        label = f"{left[0]}/{middle[0]}/{right[0]}/plain"
        ordinary_leaves += 1
        if value > maximum[0]:
            maximum = (value, label, caps)

    for s2, s3, left in one_step:
        M2 = q - s2
        cases = TRICHOTOMY.six_cases(M2)
        for s4, s5, middle in exact45:
            M4 = q - s4
            for right in front69:
                caps = combine(left, middle, right[1])
                base_label = (
                    f"s2={s2}/s3={s3}/s4={s4}/s5={s5}/{right[0]}"
                )
                if M4 == M2 + 1:
                    for geometry, row in cases.items():
                        candidate = charged_vector(
                            kprime,
                            caps,
                            row["union_size"],
                            row["fixed_dimension"],
                        )
                        value = premium(candidate)
                        trichotomy_max[geometry] = max(
                            trichotomy_max[geometry], value
                        )
                        trichotomy_leaves += 1
                        if value > maximum[0]:
                            maximum = (
                                value,
                                f"{base_label}/{geometry}",
                                candidate,
                            )
                else:
                    value = premium(caps)
                    one_step_leaves += 1
                    if value > maximum[0]:
                        maximum = (value, f"{base_label}/plain", caps)

    defects = {
        support: int(re.search(rf"s{support}=([0-9]+)", maximum[1]).group(1))
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
        "trichotomy_case_max_premium": trichotomy_max,
        "active_small_defects": {str(key): value for key, value in defects.items()},
        "active_branch": maximum[1],
        "active_caps": {
            str(target): maximum[2][target - 2] for target in SUPPORTS
        },
        "completion_premium": maximum[0],
    }


@lru_cache(maxsize=None)
def expected(kprime: int) -> dict[str, Any]:
    old = LEDGER.row(kprime)
    n = 1048576 + kprime
    m = 67472 + kprime
    summary = branch_summary(kprime)
    completion = int(summary["completion_premium"])
    marks = int(old["marks"])
    kernel = int(old["kernel"])
    full_rank = (marks + LEDGER.RECORD_FLOOR * completion) // 55
    total = kernel + full_rank
    demand = LEDGER.RECORD_FLOOR * comb(m, 11) - comb(n, 11)
    coefficient = 55 * comb(m, 11) - completion
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
        "premium_ceiling_margin": ceiling - completion,
        "full_rank_capacity": full_rank,
        "total_capacity": total,
        "required_component_incidence": demand,
        "gap": demand - total,
        "record_coefficient_cross": coefficient,
        "floor_record_raw_cross": raw,
    }


def contract() -> dict[str, object]:
    closed = expected(CLOSED_ROW)
    wall = expected(WALL_ROW)
    wall["capacity_excess"] = -wall.pop("gap")
    return {
        "schema": "rate-half-mca-rank11-k71-carrier-trichotomy-payment-v1",
        "dependencies": [
            "rate_half_mca_rank11_k60_k70_cross_support_collision_payment",
            "rate_half_mca_sparse_circuit_multicarrier_collision_charge",
            "rate_half_mca_sparse_circuit_k71_carrier_position_trichotomy",
        ],
        "parameters": {
            "closed_rows": [71],
            "new_closed_prefix": [10, 71],
            "first_method_wall": 72,
            "remaining_rank9_interval": [72, 15528],
            "deficit_weights": {
                str(target): LEDGER.DEFICITS[target] for target in SUPPORTS
            },
            "rows": {"71": closed, "72": wall},
        },
        "claim": (
            "Carrier-position pruning and all six one-step geometry cases "
            "close K'=71 with a positive exact integral gap."
        ),
        "nonclaim": (
            "The same complete payment fails at K'=72. No rank-eight, "
            "chronology, rank-eleven, KoalaBear, or prize closure is claimed."
        ),
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data == contract(), "exact contract")
    p = data["parameters"]
    closed = p["rows"]["71"]
    wall = p["rows"]["72"]
    require(closed["gap"] == 118872281099445772155993127155914865045379156488810154591370, "K71 gap")
    require(closed["premium_ceiling_margin"] == 23776122440930417094576446937038395558574009, "K71 margin")
    require(closed["active_small_defects"] == {"2": 33, "3": 31, "4": 31, "5": 31}, "K71 active")
    require(closed["support23_impossible_pair_count"] == 961, "K71 impossible")
    require(wall["capacity_excess"] == 4821537739796415753639473905341364357966460110033651367468100, "K72 wall")
    require(wall["premium_ceiling_margin"] < 0, "K72 premium")
    require(wall["active_small_defects"] == {"2": 33, "3": 31, "4": 31, "5": 31}, "K72 active")
    require(p["remaining_rank9_interval"] == [72, 15528], "remaining")
    require("fails at K'=72" in str(data["nonclaim"]), "nonclaim")
    return {
        "gap": int(closed["gap"]),
        "wall": int(wall["capacity_excess"]),
        "impossible": int(closed["support23_impossible_pair_count"]),
    }


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("closed_rows", [71, 72]),
        lambda item: item["parameters"].__setitem__("remaining_rank9_interval", [71, 15528]),
        lambda item: item["parameters"]["rows"]["71"].__setitem__("gap", 0),
        lambda item: item["parameters"]["rows"]["71"].__setitem__("support23_impossible_pair_count", 962),
        lambda item: item["parameters"]["rows"]["71"]["trichotomy_case_max_premium"].__setitem__("N34", 0),
        lambda item: item["parameters"]["rows"]["72"].__setitem__("capacity_excess", 0),
        lambda item: item.__setitem__("nonclaim", "K'=72 closed"),
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
        "RATE_HALF_MCA_RANK11_K71_CARRIER_TRICHOTOMY_PAYMENT_PASS "
        f"gap={result['gap']} wall={result['wall']} "
        f"impossible={result['impossible']} controls={controls}"
    )


if __name__ == "__main__":
    main()
