#!/usr/bin/env python3
"""Verify the K'=10 rank-nine split-pencil payment."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "029b609ad2401fa9c9e689bdff2496fff2b202f2d00acb6010b64eac67acf881"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-rank9-minimal-shortening-split-pencil-payment-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_dense_locator_component_incidence_dichotomy",
        "rate_half_mca_rank11_dense_root_highspan_saturation",
        "rate_half_mca_rank11_rank9_residual_petal_capacity_cut",
        "rate_half_mca_weighted_split_pencil_selected_support_cap",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    k = int(p["K_prime"])
    n, m = int(p["n_prime"]), int(p["m_prime"])
    require(k == 10, "K prime")
    require((n, m) == (1048576 + k, 67472 + k), "row")
    require(p["correction_dimension"] == k == 10, "dimension equality")
    require(p["fixed_subset_size"] == 9, "fixed subset")
    require(p["kernel_zero_count"] == p["common_core_size"] == 9, "root/core")
    a, total = m - 9, n - 9
    require(p["selected_outside_mass_A"] == a == 67473, "A")
    require(p["petal_total_ceiling_S"] == total == 1048577, "S")
    require(p["petal_size_ceiling"] == a - 1 == 67472, "petal ceiling")

    threshold = a // 2 + 1
    heavy_count = total // threshold
    clean = (a - 2) * total * total // 8
    balanced = comb(total, 2)
    collision = comb(heavy_count, 2) * comb(a - 1, 2)
    capacity = clean + balanced + collision
    require(p["heavy_threshold"] == threshold == 33737, "heavy threshold")
    require(p["heavy_count"] == heavy_count == 31, "heavy count")
    require(p["clean_dominant_cap"] == clean == 9273161316835569, "clean")
    require(p["balanced_cap"] == balanced == 549756338176, "balanced")
    require(p["heavy_collision_cap"] == collision == 1058433770040, "collision")
    require(p["total_capacity"] == capacity == 9274769506943785, "capacity")

    numerator = (
        int(p["component_density_numerator"])
        * int(p["residual_record_floor"])
        * comb(m, 9)
        * comb(m - 9, 2)
    )
    denominator = int(p["component_density_denominator"]) * comb(n, 9)
    demand = ceil_div(numerator, denominator)
    raw = numerator - capacity * denominator
    require(p["component_density_numerator"] == 990810934, "full density")
    require(p["component_density_denominator"] == 10**9, "density denominator")
    require(p["weighted_demand"] == demand == 11736940042024039, "demand")
    require(p["raw_demand_capacity_cross"] == raw > 0, "raw crossing")
    require(p["demand_capacity_gap"] == demand - capacity == 2462170535080254, "gap")
    require(p["newly_closed_rows"] == [10, 10], "closed row")
    require(p["remaining_rank9_interval"] == [11, 15528], "remaining interval")
    require("No rank-nine row K'>=11" in str(data.get("nonclaim")), "nonclaim")
    return {"capacity": capacity, "demand": demand, "gap": demand - capacity}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("K_prime", 11),
        lambda item: item["parameters"].__setitem__("correction_dimension", 9),
        lambda item: item["parameters"].__setitem__("common_core_size", 10),
        lambda item: item["parameters"].__setitem__("component_density_numerator", 495405467),
        lambda item: item["parameters"].__setitem__("heavy_count", 32),
        lambda item: item["parameters"].__setitem__("total_capacity", result["capacity"] + 1),
        lambda item: item["parameters"].__setitem__("weighted_demand", result["demand"] - 1),
        lambda item: item.__setitem__("nonclaim", "all rows closed"),
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
        "PASS K10 split-pencil payment primary: "
        f"capacity {result['capacity']}, demand {result['demand']}, "
        f"gap {result['gap']}, {rejected}/{len(mutations)} hostile mutations"
    )


if __name__ == "__main__":
    main()
