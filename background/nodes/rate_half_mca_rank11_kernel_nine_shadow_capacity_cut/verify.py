#!/usr/bin/env python3
"""Verify the exact rank-eleven kernel nine-shadow interval."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "1bbf5e021b422c8124ac339fc14cf79e50b0368d4b42cd1b22fd4a59307ca75e"


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


def individual_caps(p: dict[str, int], kprime: int, dimension: int) -> tuple[Fraction, Fraction]:
    nprime = p["n_offset"] + kprime
    mprime = p["m_offset"] + kprime
    rank = p["correction_dimension"] - dimension
    extra = kprime - p["correction_dimension"]
    if extra < dimension + 1:
        return Fraction(0), Fraction(0)
    extensions = comb(extra, dimension + 1)
    divisor = dimension + 2
    ambient = comb(nprime, rank) * record_cap(p, kprime, dimension) * extensions // divisor
    support = comb(mprime, rank) * extensions // divisor
    return Fraction(ambient, p["residual_record_floor"]), Fraction(support)


def weights_and_caps(p: dict[str, int], kprime: int) -> tuple[list[Fraction], list[Fraction], list[str]]:
    weights = []
    caps = []
    branches = []
    for dimension in range(1, p["correction_dimension"]):
        ambient, record = individual_caps(p, kprime, dimension)
        cap = min(ambient, record)
        caps.append(cap)
        branches.append("ambient" if ambient <= record else "record")
        if cap:
            available = kprime - dimension - p["shadow_subset_size"]
            require(available >= 2, f"extension d={dimension}")
            weights.append(Fraction(comb(dimension + 2, 2), comb(available, 2)))
        else:
            weights.append(Fraction(0))
    return weights, caps, branches


def optimum(p: dict[str, int], kprime: int) -> tuple[Fraction, int, list[Fraction]]:
    weights, caps, _ = weights_and_caps(p, kprime)
    remaining = Fraction(comb(p["m_offset"] + kprime, p["shadow_subset_size"]))
    total = Fraction(0)
    allocation = []
    frontier = 0
    positive_weights = [weight for weight in weights if weight]
    require(positive_weights == sorted(positive_weights), "weight order")
    for dimension, (weight, cap) in enumerate(zip(weights, caps), 1):
        if not cap:
            allocation.append(Fraction(0))
            continue
        take = min(cap, remaining / weight)
        allocation.append(take)
        total += take
        remaining -= weight * take
        if take < cap and not frontier:
            frontier = dimension
    return total, frontier, allocation


def scaled_capacity(p: dict[str, int], kprime: int) -> int:
    value = p["residual_record_floor"] * optimum(p, kprime)[0]
    return value.numerator // value.denominator


def demand_ratio(p: dict[str, int], kprime: int) -> Fraction:
    return Fraction(
        p["lane_density_numerator"] * comb(p["m_offset"] + kprime, p["component_subset_size"]),
        p["lane_density_denominator"],
    )


def demand_ceiling(p: dict[str, int], kprime: int) -> int:
    value = p["residual_record_floor"] * demand_ratio(p, kprime)
    return (value.numerator + value.denominator - 1) // value.denominator


def validate(data: object, exhaustive: bool = True) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-nine-shadow-capacity-cut-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_hybrid_capacity_cut",
        "rate_half_mca_rank11_kernel_nine_shadow_coupling",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["n_offset"], p["m_offset"]) == (1048576, 67472), "offsets")
    require(p["residual_record_floor"] == 274980728111260126, "record floor")
    require((p["lane_density_numerator"], p["lane_density_denominator"]) == (495405467, 10**9), "density")
    require((p["correction_dimension"], p["component_subset_size"], p["shadow_subset_size"]) == (10, 11, 9), "dimensions")
    require((p["closed_dimension_minimum"], p["closed_dimension_maximum"], p["first_open_dimension"]) == (10, 15445, 15446), "interval")

    end = p["closed_dimension_maximum"]
    wall = p["first_open_dimension"]
    end_opt, end_frontier, end_allocation = optimum(p, end)
    wall_opt, wall_frontier, wall_allocation = optimum(p, wall)
    require(weights_and_caps(p, end)[2] == p["endpoint_individual_branch_pattern"], "endpoint branches")
    require(weights_and_caps(p, wall)[2] == p["endpoint_individual_branch_pattern"], "wall branches")
    require(end_frontier == wall_frontier == p["endpoint_frontier_corank"] == 2, "frontier")
    require(end_allocation[0] == weights_and_caps(p, end)[1][0] and 0 < end_allocation[1] < weights_and_caps(p, end)[1][1], "endpoint allocation")
    require(all(value == 0 for value in end_allocation[2:]), "endpoint tail")
    require(all(value == 0 for value in wall_allocation[2:]), "wall tail")

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
        lambda item: item["parameters"].__setitem__("closed_dimension_maximum", 15446),
        lambda item: item["parameters"].__setitem__("first_open_dimension", 15447),
        lambda item: item["parameters"].__setitem__("endpoint_frontier_corank", 3),
        lambda item: item["parameters"]["endpoint_individual_branch_pattern"].__setitem__(4, "ambient"),
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
        "RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_CAPACITY_CUT_PASS "
        f"checked={result['checked']} endpoint_gap={result['gap']} "
        f"wall_excess={result['wall_excess']} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
