#!/usr/bin/env python3
"""Verify the joint sparse/high rank-nine shadow ledger."""

from __future__ import annotations

import copy
import hashlib
import json
from itertools import product
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "2f9446f4efd0a3cbb393a74f78f77384dee26f2f3d5fdddb53ba1b4b71762013"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank9-sparse-shadow-joint-ledger-v1",
        "schema",
    )
    require(data.get("dependencies") == [], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["component_subset_size"], p["shadow_subset_size"]) == (11, 9), "sizes")
    require(p["total_shadow_count"] == comb(11, 2) == 55, "shadow total")
    require(p["high_support_minimum"] == 6, "high support")
    require(p["baseline_shadow_cost"] == 45, "baseline")
    supports = list(p["low_supports"])
    require(supports == [2, 3, 4, 5], "low supports")
    shadows = [55 - comb(11 - support, 2) for support in supports]
    require(p["rank9_shadow_counts"] == shadows == [19, 27, 34, 40], "shadow counts")
    premiums = [45 - shadow for shadow in shadows]
    require(p["premium_weights"] == premiums == [26, 18, 11, 5], "premiums")
    require(p["shadow_formula"] == "55-C(11-c,2)", "shadow formula")
    require("max_a" in p["joint_capacity_formula"], "branch maximum")

    feasible_checks = 0
    for global_marks in range(0, 91, 7):
        for limits in product(range(3), repeat=4):
            premium = sum(weight * limit for weight, limit in zip(premiums, limits))
            bound = (global_marks + premium) // 45
            for incidences in product(*(range(limit + 1) for limit in limits)):
                used_low = sum(shadow * count for shadow, count in zip(shadows, incidences))
                for high in range(4):
                    if used_low + 45 * high <= global_marks:
                        require(high + sum(incidences) <= bound, "feasible ledger point")
                        feasible_checks += 1
    require("No rank-nine chart capacity" in str(data.get("nonclaim")), "nonclaim")
    return {"feasible_checks": feasible_checks}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("total_shadow_count", 54),
        lambda item: item["parameters"].__setitem__("baseline_shadow_cost", 44),
        lambda item: item["parameters"].__setitem__("high_support_minimum", 7),
        lambda item: item["parameters"]["rank9_shadow_counts"].__setitem__(0, 18),
        lambda item: item["parameters"]["rank9_shadow_counts"].__setitem__(3, 39),
        lambda item: item["parameters"]["premium_weights"].__setitem__(1, 19),
        lambda item: item["parameters"].__setitem__("joint_capacity_formula", "floor(G/45)+R*sum(L)"),
        lambda item: item.__setitem__("nonclaim", "all capacities supplied"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (KeyError, Reject, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "hostile mutation rejection")
    print(
        "PASS joint sparse/high rank-nine shadow ledger primary: "
        f"{result['feasible_checks']} feasible integer points, "
        f"{rejected}/{len(mutations)} hostile mutations"
    )


if __name__ == "__main__":
    main()
