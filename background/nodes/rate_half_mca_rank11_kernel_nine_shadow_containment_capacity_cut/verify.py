#!/usr/bin/env python3
"""Verify the full-containment nine-shadow kernel interval."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "7d56dc863b2bb327c392b33405098b5163a305e4a909a007482e32bfbd00f7e4"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def record_cap(p: dict[str, int], kprime: int, dimension: int) -> int:
    if dimension == 9:
        return p["rank9_record_cap"]
    rank = p["correction_dimension"] - dimension
    shortened_k = kprime - rank
    endpoint_zero = Fraction(
        falling(p["n_offset"] + shortened_k, dimension + 1),
        (p["m_offset"] + shortened_k) * rising(p["m_offset"] + 1, dimension - 1),
    )
    endpoint_max = Fraction(
        falling(p["n_offset"] + dimension, dimension + 1),
        rising(p["m_offset"] + 1, dimension),
    )
    value = max(endpoint_zero, endpoint_max)
    return value.numerator // value.denominator


def weights_caps_branches(
    p: dict[str, int], kprime: int
) -> tuple[list[Fraction], list[Fraction], list[str]]:
    nprime = p["n_offset"] + kprime
    mprime = p["m_offset"] + kprime
    extra = kprime - p["correction_dimension"]
    weights = []
    caps = []
    branches = []
    for dimension in range(1, p["correction_dimension"]):
        rank = p["correction_dimension"] - dimension
        if extra < dimension + 1:
            weights.append(Fraction(0))
            caps.append(Fraction(0))
            branches.append("ambient")
            continue
        extensions = comb(extra, dimension + 1)
        divisor = dimension + 2
        ambient_integer = comb(nprime, rank) * record_cap(p, kprime, dimension) * extensions // divisor
        record_integer = comb(mprime, rank) * extensions // divisor
        ambient = Fraction(ambient_integer, p["residual_record_floor"])
        record = Fraction(record_integer)
        caps.append(min(ambient, record))
        branches.append("ambient" if ambient <= record else "record")
        weights.append(Fraction(comb(dimension + 2, 2), comb(kprime - dimension - 9, 2)))
    return weights, caps, branches


def lower_qmax(
    budget: Fraction,
    weights: list[Fraction],
    caps: list[Fraction],
) -> Fraction:
    total = Fraction(0)
    for weight, cap in zip(weights[1:], caps[1:]):
        if not cap:
            continue
        take = min(cap, max(Fraction(0), budget) / weight)
        total += take
        budget -= weight * take
    return total


def resources(
    p: dict[str, int], kprime: int
) -> tuple[Fraction, Fraction, Fraction]:
    mprime = p["m_offset"] + kprime
    shadow_budget = Fraction(comb(mprime, p["shadow_subset_size"]))
    support_extensions = Fraction(comb(mprime - p["shadow_subset_size"], 2))
    rank9_extensions = Fraction(comb(kprime - 10, 2))
    return shadow_budget, support_extensions, rank9_extensions


def optimum(
    p: dict[str, int], kprime: int
) -> tuple[Fraction, list[Fraction]]:
    weights, caps, _ = weights_caps_branches(p, kprime)
    budget, support_extensions, rank9_extensions = resources(p, kprime)
    if not caps[0]:
        remaining = budget
        allocation = []
        for weight, cap in zip(weights, caps):
            if not cap:
                allocation.append(Fraction(0))
                continue
            take = min(cap, remaining / weight)
            allocation.append(take)
            remaining -= weight * take
        return sum(allocation, Fraction(0)), allocation

    rank9_coefficient = 52 + 3 * support_extensions / rank9_extensions
    candidates = {Fraction(0), caps[0]}
    cumulative_weighted_cap = Fraction(0)
    cumulative_cap = Fraction(0)
    for index in range(1, 9):
        weight = weights[index]
        cap = caps[index]
        if not cap:
            continue
        kink = (budget - cumulative_weighted_cap) / weights[0]
        if 0 <= kink <= caps[0]:
            candidates.add(kink)
        denominator = rank9_coefficient / 55 - weights[0] / weight
        numerator = (
            support_extensions * budget / 55
            - cumulative_cap
            - (budget - cumulative_weighted_cap) / weight
        )
        if denominator:
            crossing = numerator / denominator
            if 0 <= crossing <= caps[0]:
                candidates.add(crossing)
        cumulative_weighted_cap += weight * cap
        cumulative_cap += cap

    all_lower_crossing = (
        support_extensions * budget - 55 * cumulative_cap
    ) / rank9_coefficient
    if 0 <= all_lower_crossing <= caps[0]:
        candidates.add(all_lower_crossing)

    best = Fraction(-1)
    best_allocation: list[Fraction] = []
    for x1 in candidates:
        if weights[0] * x1 > budget:
            continue
        qmax = lower_qmax(budget - weights[0] * x1, weights, caps)
        cmax = (support_extensions * budget - rank9_coefficient * x1) / 55
        lower_target = max(Fraction(0), min(qmax, cmax, sum(caps[1:], Fraction(0))))
        remaining_count = lower_target
        remaining_shadow = budget - weights[0] * x1
        allocation = [x1]
        for weight, cap in zip(weights[1:], caps[1:]):
            if not cap:
                allocation.append(Fraction(0))
                continue
            take = min(cap, remaining_count, remaining_shadow / weight)
            allocation.append(take)
            remaining_count -= take
            remaining_shadow -= weight * take
        require(remaining_count == 0, "lower allocation")
        value = sum(allocation, Fraction(0))
        if value > best:
            best = value
            best_allocation = allocation
    require(best >= 0 and len(best_allocation) == 9, "optimizer")
    return best, best_allocation


def demand_ratio(p: dict[str, int], kprime: int) -> Fraction:
    return Fraction(
        p["lane_density_numerator"] * comb(p["m_offset"] + kprime, p["component_subset_size"]),
        p["lane_density_denominator"],
    )


def scaled_capacity(p: dict[str, int], kprime: int) -> int:
    value = p["residual_record_floor"] * optimum(p, kprime)[0]
    return value.numerator // value.denominator


def demand_ceiling(p: dict[str, int], kprime: int) -> int:
    value = p["residual_record_floor"] * demand_ratio(p, kprime)
    return (value.numerator + value.denominator - 1) // value.denominator


def validate(data: object, exhaustive: bool = True) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-nine-shadow-containment-capacity-cut-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_nine_shadow_capacity_cut",
        "rate_half_mca_rank11_kernel_nine_shadow_containment_coupling",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["n_offset"], p["m_offset"]) == (1048576, 67472), "offsets")
    require(p["residual_record_floor"] == 274980728111260126, "record floor")
    require((p["lane_density_numerator"], p["lane_density_denominator"]) == (495405467, 10**9), "density")
    require((p["correction_dimension"], p["component_subset_size"], p["shadow_subset_size"]) == (10, 11, 9), "dimensions")
    require((p["closed_dimension_minimum"], p["closed_dimension_maximum"], p["first_open_dimension"]) == (10, 15670, 15671), "interval")

    end = p["closed_dimension_maximum"]
    wall = p["first_open_dimension"]
    end_opt, end_allocation = optimum(p, end)
    wall_opt, wall_allocation = optimum(p, wall)
    require(end_opt == Fraction(p["endpoint_optimum_numerator"], p["endpoint_optimum_denominator"]), "endpoint optimum")
    require(wall_opt == Fraction(p["wall_optimum_numerator"], p["wall_optimum_denominator"]), "wall optimum")
    require(weights_caps_branches(p, end)[2] == p["endpoint_individual_branch_pattern"], "endpoint branches")
    require(weights_caps_branches(p, wall)[2] == p["endpoint_individual_branch_pattern"], "wall branches")
    require(p["endpoint_active_coranks"] == [1, 2], "active coranks")
    require(all(value > 0 for value in end_allocation[:2]) and all(value == 0 for value in end_allocation[2:]), "endpoint support")
    require(all(value > 0 for value in wall_allocation[:2]) and all(value == 0 for value in wall_allocation[2:]), "wall support")

    for kprime, allocation in ((end, end_allocation), (wall, wall_allocation)):
        weights, caps, _ = weights_caps_branches(p, kprime)
        budget, e0, e1 = resources(p, kprime)
        v1 = 52 + 3 * e0 / e1
        require(sum(weight * value for weight, value in zip(weights, allocation)) == budget, f"nine equality {kprime}")
        require(v1 * allocation[0] + 55 * sum(allocation[1:], Fraction(0)) == e0 * budget, f"containment equality {kprime}")
        require(all(value < cap for value, cap in zip(allocation[:2], caps[:2])), f"individual slack {kprime}")

    end_demand, end_cap = demand_ceiling(p, end), scaled_capacity(p, end)
    wall_demand, wall_cap = demand_ceiling(p, wall), scaled_capacity(p, wall)
    require((end_demand, end_cap, end_demand - end_cap) == (
        p["endpoint_demand_ceiling"], p["endpoint_capacity"], p["endpoint_gap"]
    ), "endpoint")
    require((wall_demand, wall_cap, wall_cap - wall_demand) == (
        p["wall_demand_ceiling"], p["wall_capacity"], p["wall_excess"]
    ), "wall")
    require(demand_ratio(p, end) > end_opt, "endpoint exact sign")
    require(demand_ratio(p, wall) < wall_opt, "wall exact sign")

    checked = 0
    if exhaustive:
        for kprime in range(p["closed_dimension_minimum"], end + 1):
            require(demand_ratio(p, kprime) > optimum(p, kprime)[0], f"capacity at {kprime}")
            checked += 1
    require("remains open" in str(data.get("nonclaim")), "nonclaim")
    return {"checked": checked, "gap": end_demand - end_cap, "wall_excess": wall_cap - wall_demand}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("residual_record_floor", 274980728111260125),
        lambda item: item["parameters"].__setitem__("shadow_subset_size", 8),
        lambda item: item["parameters"].__setitem__("closed_dimension_maximum", 15671),
        lambda item: item["parameters"].__setitem__("first_open_dimension", 15672),
        lambda item: item["parameters"]["endpoint_active_coranks"].append(3),
        lambda item: item["parameters"]["endpoint_individual_branch_pattern"].__setitem__(4, "ambient"),
        lambda item: item["parameters"].__setitem__("endpoint_optimum_denominator", 3820255350),
        lambda item: item["parameters"].__setitem__("wall_excess", item["parameters"]["wall_excess"] - 1),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered, exhaustive=False)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_CONTAINMENT_CAPACITY_CUT_PASS "
        f"checked={result['checked']} endpoint_gap={result['gap']} "
        f"wall_excess={result['wall_excess']} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
