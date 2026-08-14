#!/usr/bin/env python3
"""Verify the exact kernel multi-basis capacity interval."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "47cd5f4ee795bc82161711e65e1fdbfd70cc86d0947854a4ed9aa320508b8a64"


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
    shortened_n = p["n_offset"] + shortened_k
    shortened_m = p["m_offset"] + shortened_k
    endpoint_zero = Fraction(
        falling(shortened_n, dimension + 1),
        shortened_m * rising(p["m_offset"] + 1, dimension - 1),
    )
    endpoint_max = Fraction(
        falling(p["n_offset"] + dimension, dimension + 1),
        rising(p["m_offset"] + 1, dimension),
    )
    value = max(endpoint_zero, endpoint_max)
    return value.numerator // value.denominator


def capacity(p: dict[str, int], kprime: int) -> int:
    nprime = p["n_offset"] + kprime
    extra = kprime - p["correction_dimension"]
    total = 0
    for dimension in range(1, p["correction_dimension"]):
        rank = p["correction_dimension"] - dimension
        extensions = comb(extra, dimension + 1) if extra >= dimension + 1 else 0
        decorated = comb(nprime, rank) * record_cap(p, kprime, dimension) * extensions
        total += decorated // p["basis_multiplicities"][dimension - 1]
    return total


def demand_ceiling(p: dict[str, int], kprime: int) -> int:
    mprime = p["m_offset"] + kprime
    numerator = (
        p["lane_density_numerator"]
        * p["residual_record_floor"]
        * comb(mprime, p["component_subset_size"])
    )
    denominator = p["lane_density_denominator"]
    return (numerator + denominator - 1) // denominator


def validate(data: object, exhaustive: bool = True) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-multibasis-capacity-cut-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_rankstratified_capacity_cut",
        "rate_half_mca_rank11_kernel_multibasis_decoration_compression",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["n_offset"], p["m_offset"]) == (1048576, 67472), "row offsets")
    require(p["residual_record_floor"] == 274980728111260126, "record floor")
    require((p["lane_density_numerator"], p["lane_density_denominator"]) == (495405467, 1000000000), "lane density")
    require((p["correction_dimension"], p["component_subset_size"]) == (10, 11), "dimensions")
    require(p["rank9_record_cap"] == 61871313426630599, "rank-nine cap")
    require(p["basis_multiplicities"] == list(range(3, 12)), "multiplicities")
    require((p["closed_dimension_minimum"], p["closed_dimension_maximum"], p["first_open_dimension"]) == (10, 11641, 11642), "interval")

    end = p["closed_dimension_maximum"]
    wall = p["first_open_dimension"]
    end_demand, end_cap = demand_ceiling(p, end), capacity(p, end)
    wall_demand, wall_cap = demand_ceiling(p, wall), capacity(p, wall)
    require(end_demand == p["endpoint_demand_ceiling"], "endpoint demand")
    require(end_cap == p["endpoint_capacity"], "endpoint capacity")
    require(end_demand - end_cap == p["endpoint_gap"] > 0, "endpoint gap")
    require(wall_demand == p["wall_demand_ceiling"], "wall demand")
    require(wall_cap == p["wall_capacity"], "wall capacity")
    require(wall_cap - wall_demand == p["wall_excess"] > 0, "wall excess")

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
        lambda item: item["parameters"]["basis_multiplicities"].__setitem__(0, 2),
        lambda item: item["parameters"].__setitem__("lane_density_numerator", 495405466),
        lambda item: item["parameters"].__setitem__("closed_dimension_maximum", 11642),
        lambda item: item["parameters"].__setitem__("first_open_dimension", 11643),
        lambda item: item["parameters"].__setitem__("endpoint_gap", item["parameters"]["endpoint_gap"] - 1),
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
        "RATE_HALF_MCA_RANK11_KERNEL_MULTIBASIS_CAPACITY_CUT_PASS "
        f"checked={result['checked']} endpoint_gap={result['gap']} "
        f"wall_excess={result['wall_excess']} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
