#!/usr/bin/env python3
"""Verify the exact two-step nine-shadow kernel interval."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "2e8396fb8eb41b2d3d4d9f8f6e13ab52bd51f814b348d2fcb00b98dbc04caaae"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def record_cap(p: dict[str, int], kprime: int, d: int) -> int:
    if d == 9:
        return p["rank9_record_cap"]
    rank = p["correction_dimension"] - d
    shortened = kprime - rank
    left = Fraction(
        falling(p["n_offset"] + shortened, d + 1),
        (p["m_offset"] + shortened) * rising(p["m_offset"] + 1, d - 1),
    )
    right = Fraction(
        falling(p["n_offset"] + d, d + 1),
        rising(p["m_offset"] + 1, d),
    )
    value = max(left, right)
    return value.numerator // value.denominator


def lp_data(p: dict[str, int], kprime: int):
    nprime, mprime = p["n_offset"] + kprime, p["m_offset"] + kprime
    caps, weights, coefficients, branches = [], [], [], []
    for d in range(1, 10):
        extension = comb(kprime - 10, d + 1)
        ambient = Fraction(
            comb(nprime, 10 - d) * record_cap(p, kprime, d) * extension // (d + 2),
            p["residual_record_floor"],
        )
        support = Fraction(comb(mprime, 10 - d) * extension // (d + 2))
        caps.append(min(ambient, support))
        branches.append("ambient" if ambient <= support else "record")
        weights.append(Fraction(comb(d + 2, 2), comb(kprime - d - 9, 2)))
        coefficients.append(Fraction(0))
    shadow_budget = Fraction(comb(mprime, p["shadow_subset_size"]))
    e0 = Fraction(comb(mprime - p["shadow_subset_size"], 2))
    for index in range(9):
        d = index + 1
        if d == 1:
            coefficients[index] = 52 + 3 * e0 / comb(kprime - 10, 2)
        elif d == 2:
            coefficients[index] = 55 + Fraction(
                6 * p["rank8_independent_pair_floor"], comb(kprime - 11, 2)
            )
        else:
            coefficients[index] = Fraction(55)
    return caps, weights, coefficients, branches, shadow_budget, e0 * shadow_budget


def solve_exact(matrix: list[list[Fraction]], right: list[Fraction]) -> list[Fraction]:
    size = len(right)
    augmented = [list(row) + [value] for row, value in zip(matrix, right)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if augmented[row][column]), None)
        require(pivot is not None, f"dual pivot {column}")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            scale = augmented[row][column]
            augmented[row] = [
                left - scale * pivot_value
                for left, pivot_value in zip(augmented[row], augmented[column])
            ]
    return [augmented[index][-1] for index in range(size)]


def certificate(p: dict[str, int], kprime: int):
    caps, weights, coefficients, branches, shadow_budget, containment_budget = lp_data(p, kprime)
    raising, multiplicity = {}, {}
    factors = [Fraction(0) for _ in range(9)]
    factors[0] = factors[1] = Fraction(1)
    for d in range(3, 10):
        raising[d] = Fraction(
            comb(d + 2, 2) * comb(p["m_offset"] + d, 2),
            comb(kprime - d - 9, 2),
        )
        multiplicity[d] = comb(11 - d, 2)
        factors[d - 1] = Fraction(multiplicity[d], raising[d]) * factors[d - 3]

    odd_base = caps[0]
    odd_containment = sum(
        coefficients[index] * factors[index] for index in range(0, 9, 2)
    )
    even_containment = sum(
        coefficients[index] * factors[index] for index in range(1, 9, 2)
    )
    even_base = (containment_budget - odd_containment * odd_base) / even_containment
    allocation = [
        factor * (odd_base if index % 2 == 0 else even_base)
        for index, factor in enumerate(factors)
    ]
    require(all(value > 0 for value in allocation), f"positive allocation K={kprime}")
    require(all(value <= cap for value, cap in zip(allocation, caps)), f"cap bounds K={kprime}")
    require(allocation[0] == caps[0], f"corank-one cap K={kprime}")
    require(all(allocation[index] < caps[index] for index in range(1, 9)), f"other caps slack K={kprime}")
    require(sum(weights[i] * allocation[i] for i in range(9)) < shadow_budget, f"shadow slack K={kprime}")
    require(
        sum(coefficients[i] * allocation[i] for i in range(9)) == containment_budget,
        f"containment equality K={kprime}",
    )
    for d in range(3, 10):
        require(
            raising[d] * allocation[d - 1] == multiplicity[d] * allocation[d - 3],
            f"hierarchy equality d={d} K={kprime}",
        )

    # Variables: containment multiplier, corank-one cap multiplier, then H_3,...,H_9.
    dual_matrix = []
    for d in range(1, 10):
        row = [coefficients[d - 1], Fraction(1 if d == 1 else 0)] + [
            Fraction(0) for _ in range(7)
        ]
        if d >= 3:
            row[d - 1] += raising[d]
        if d + 2 <= 9:
            row[d + 1] -= multiplicity[d + 2]
        dual_matrix.append(row)
    dual = solve_exact(dual_matrix, [Fraction(1) for _ in range(9)])
    require(all(value >= 0 for value in dual), f"dual signs K={kprime}")
    optimum = sum(allocation, Fraction(0))
    require(dual[0] * containment_budget + dual[1] * caps[0] == optimum, f"strong duality K={kprime}")
    return optimum, allocation, dual, branches


def demand_ratio(p: dict[str, int], kprime: int) -> Fraction:
    return Fraction(
        p["lane_density_numerator"] * comb(p["m_offset"] + kprime, p["component_subset_size"]),
        p["lane_density_denominator"],
    )


def integer_values(p: dict[str, int], kprime: int, optimum: Fraction) -> tuple[int, int]:
    demand = p["residual_record_floor"] * demand_ratio(p, kprime)
    capacity = p["residual_record_floor"] * optimum
    return (
        -(-demand.numerator // demand.denominator),
        capacity.numerator // capacity.denominator,
    )


def validate(data: object, exhaustive: bool = True) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-two-step-nineshadow-capacity-cut-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_rank8_nineshadow_capacity_cut",
        "rate_half_mca_rank11_kernel_two_step_nineshadow_hierarchy",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["previous_closed_maximum"], p["replay_minimum"], p["closed_dimension_maximum"], p["first_open_dimension"]) == (17608, 17609, 18101, 18102), "interval")
    require(p["replay_rows"] == 494, "row count")
    require(p["active_individual_caps"] == [1], "active cap")
    require(p["active_shared_resources"] == ["full_containment"], "active shared resource")
    require(p["slack_shared_resources"] == ["rank_preserving_nine_shadow"], "slack shared resource")
    require(p["active_hierarchy_coranks"] == list(range(3, 10)), "active hierarchy")
    require(p["positive_coranks"] == list(range(1, 10)), "positive coranks")

    endpoint = p["closed_dimension_maximum"]
    wall = p["first_open_dimension"]
    endpoint_optimum, _, _, endpoint_branches = certificate(p, endpoint)
    wall_optimum, _, _, _ = certificate(p, wall)
    require(endpoint_branches == p["endpoint_individual_branch_pattern"], "endpoint branches")
    require(endpoint_optimum == Fraction(p["endpoint_optimum_numerator"], p["endpoint_optimum_denominator"]), "endpoint optimum")
    require(wall_optimum == Fraction(p["wall_optimum_numerator"], p["wall_optimum_denominator"]), "wall optimum")
    endpoint_demand, endpoint_capacity = integer_values(p, endpoint, endpoint_optimum)
    wall_demand, wall_capacity = integer_values(p, wall, wall_optimum)
    require((endpoint_demand, endpoint_capacity, endpoint_demand - endpoint_capacity) == (p["endpoint_demand_ceiling"], p["endpoint_capacity"], p["endpoint_gap"]), "endpoint integers")
    require((wall_demand, wall_capacity, wall_capacity - wall_demand) == (p["wall_demand_ceiling"], p["wall_capacity"], p["wall_excess"]), "wall integers")
    require(demand_ratio(p, endpoint) > endpoint_optimum, "endpoint sign")
    require(demand_ratio(p, wall) < wall_optimum, "wall sign")

    checked = 1
    if exhaustive:
        for kprime in range(p["replay_minimum"], endpoint + 1):
            optimum, _, _, branches = certificate(p, kprime)
            require(demand_ratio(p, kprime) > optimum, f"closed sign K={kprime}")
            require(branches == p["endpoint_individual_branch_pattern"], f"branches K={kprime}")
            checked += 1
    require(checked == (p["replay_rows"] if exhaustive else 1), "checked rows")
    require("remains open" in str(data.get("nonclaim")), "nonclaim")
    return {"checked": checked, "gap": endpoint_demand - endpoint_capacity, "wall": wall_capacity - wall_demand}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("closed_dimension_maximum", 18102),
        lambda item: item["parameters"].__setitem__("first_open_dimension", 18103),
        lambda item: item["parameters"]["active_hierarchy_coranks"].pop(),
        lambda item: item["parameters"].__setitem__("endpoint_gap", item["parameters"]["endpoint_gap"] - 1),
        lambda item: item["parameters"].__setitem__("wall_excess", item["parameters"]["wall_excess"] - 1),
        lambda item: item["parameters"]["active_individual_caps"].append(3),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered, exhaustive=False)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_TWO_STEP_NINESHADOW_CAPACITY_CUT_PASS "
        f"checked={result['checked']} endpoint_gap={result['gap']} wall_excess={result['wall']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
