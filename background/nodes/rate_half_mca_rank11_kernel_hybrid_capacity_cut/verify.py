#!/usr/bin/env python3
"""Verify the exact ambient/record kernel hybrid interval."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "ce3e5d908adba2db8ce0a12cd0f464d1d9b45b0602203f9f5a8adef7e0d51837"


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


def hybrid_terms(p: dict[str, int], kprime: int) -> list[tuple[int, int, str]]:
    nprime = p["n_offset"] + kprime
    mprime = p["m_offset"] + kprime
    extra = kprime - p["correction_dimension"]
    terms = []
    for dimension in range(1, p["correction_dimension"]):
        rank = p["correction_dimension"] - dimension
        extensions = comb(extra, dimension + 1) if extra >= dimension + 1 else 0
        divisor = p["basis_multiplicities"][dimension - 1]
        ambient = comb(nprime, rank) * record_cap(p, kprime, dimension) * extensions // divisor
        per_record = comb(mprime, rank) * extensions // divisor
        support = p["residual_record_floor"] * per_record
        terms.append((ambient, support, "ambient" if ambient <= support else "record"))
    return terms


def capacity(p: dict[str, int], kprime: int) -> int:
    return sum(min(ambient, support) for ambient, support, _ in hybrid_terms(p, kprime))


def demand_ceiling(p: dict[str, int], kprime: int) -> int:
    numerator = (
        p["lane_density_numerator"]
        * p["residual_record_floor"]
        * comb(p["m_offset"] + kprime, p["component_subset_size"])
    )
    denominator = p["lane_density_denominator"]
    return (numerator + denominator - 1) // denominator


def validate(data: object, exhaustive: bool = True) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-hybrid-capacity-cut-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_multibasis_capacity_cut",
        "rate_half_mca_rank11_kernel_record_support_capacity",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["n_offset"], p["m_offset"]) == (1048576, 67472), "offsets")
    require(p["residual_record_floor"] == 274980728111260126, "record floor")
    require((p["lane_density_numerator"], p["lane_density_denominator"]) == (495405467, 1000000000), "density")
    require((p["correction_dimension"], p["component_subset_size"]) == (10, 11), "dimensions")
    require(p["basis_multiplicities"] == list(range(3, 12)), "multiplicities")
    require((p["closed_dimension_minimum"], p["closed_dimension_maximum"], p["first_open_dimension"]) == (10, 11772, 11773), "interval")

    end, wall = p["closed_dimension_maximum"], p["first_open_dimension"]
    end_demand, end_cap = demand_ceiling(p, end), capacity(p, end)
    wall_demand, wall_cap = demand_ceiling(p, wall), capacity(p, wall)
    require([choice for _, _, choice in hybrid_terms(p, end)] == p["endpoint_branch_pattern"], "endpoint branches")
    require([choice for _, _, choice in hybrid_terms(p, wall)] == p["endpoint_branch_pattern"], "wall branches")
    require((end_demand, end_cap, end_demand - end_cap) == (
        p["endpoint_demand_ceiling"], p["endpoint_capacity"], p["endpoint_gap"]
    ), "endpoint")
    require((wall_demand, wall_cap, wall_cap - wall_demand) == (
        p["wall_demand_ceiling"], p["wall_capacity"], p["wall_excess"]
    ), "wall")
    require(end_demand > end_cap and wall_cap > wall_demand, "boundary signs")

    checked = 0
    if exhaustive:
        for kprime in range(p["closed_dimension_minimum"], end + 1):
            require(demand_ceiling(p, kprime) > capacity(p, kprime), f"capacity at {kprime}")
            checked += 1
    require("remains open" in str(data.get("nonclaim")), "nonclaim")
    return {"checked": checked, "gap": end_demand - end_cap, "wall_excess": wall_cap - wall_demand}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("residual_record_floor", 274980728111260125),
        lambda item: item["parameters"]["basis_multiplicities"].__setitem__(2, 4),
        lambda item: item["parameters"]["endpoint_branch_pattern"].__setitem__(2, "ambient"),
        lambda item: item["parameters"].__setitem__("closed_dimension_maximum", 11773),
        lambda item: item["parameters"].__setitem__("first_open_dimension", 11774),
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
        "RATE_HALF_MCA_RANK11_KERNEL_HYBRID_CAPACITY_CUT_PASS "
        f"checked={result['checked']} endpoint_gap={result['gap']} "
        f"wall_excess={result['wall_excess']} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
