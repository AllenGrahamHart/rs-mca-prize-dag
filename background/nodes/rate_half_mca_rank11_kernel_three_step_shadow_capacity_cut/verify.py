#!/usr/bin/env python3
"""Verify the exact three-step shadow kernel interval."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "1645081d2c338bd79210f3417f2520c14bfc72d0351af70fbb042b3ecd408636"


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
    return int(max(left, right))


def lp_data(p: dict[str, int], kprime: int):
    nprime, mprime = p["n_offset"] + kprime, p["m_offset"] + kprime
    caps, shadow, containment, branches = [], [], [], []
    for d in range(1, 10):
        extension = comb(kprime - 10, d + 1)
        ambient = Fraction(
            comb(nprime, 10 - d) * record_cap(p, kprime, d) * extension // (d + 2),
            p["residual_record_floor"],
        )
        support = Fraction(comb(mprime, 10 - d) * extension // (d + 2))
        caps.append(min(ambient, support))
        branches.append("ambient" if ambient <= support else "record")
        shadow.append(Fraction(comb(d + 2, 2), comb(kprime - d - 9, 2)))
    shadow_budget = Fraction(comb(mprime, p["shadow_subset_size"]))
    e0 = comb(mprime - p["shadow_subset_size"], 2)
    for d in range(1, 10):
        if d == 1:
            containment.append(52 + Fraction(3 * e0, comb(kprime - 10, 2)))
        elif d == 2:
            containment.append(55 + Fraction(6 * p["rank8_independent_pair_floor"], comb(kprime - 11, 2)))
        else:
            containment.append(Fraction(55))
    return caps, shadow, containment, branches, shadow_budget, Fraction(e0) * shadow_budget


def raising(kprime: int, step: int, d: int) -> Fraction:
    return Fraction(
        comb(d + 2, step) * comb(67472 + d, step),
        comb(kprime - d - 11 + step, step),
    )


def multiplicity(step: int, d: int) -> int:
    return comb(9 - d + step, step)


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


def tree_factors(kprime: int, tree: list[list[int]]) -> tuple[list[Fraction], list[int]]:
    factors = [Fraction(0) for _ in range(9)]
    roots = [0 for _ in range(9)]
    factors[0] = factors[1] = Fraction(1)
    roots[0], roots[1] = 1, 2
    changed = True
    while changed:
        changed = False
        for step, source in tree:
            target = source - step
            source_index, target_index = source - 1, target - 1
            ratio = Fraction(multiplicity(step, source), raising(kprime, step, source))
            if roots[target_index] and not roots[source_index]:
                factors[source_index] = ratio * factors[target_index]
                roots[source_index] = roots[target_index]
                changed = True
            elif roots[source_index] and not roots[target_index]:
                factors[target_index] = factors[source_index] / ratio
                roots[target_index] = roots[source_index]
                changed = True
    require(all(roots), f"tree spans {kprime}")
    return factors, roots


def certificate(p: dict[str, object], kprime: int):
    caps, shadow, containment, branches, shadow_budget, containment_budget = lp_data(p, kprime)
    tree = p["dual_tree"]
    factors, roots = tree_factors(kprime, tree)
    x1 = caps[0]
    first_price = sum(containment[i] * factors[i] for i in range(9) if roots[i] == 1)
    second_price = sum(containment[i] * factors[i] for i in range(9) if roots[i] == 2)
    x2 = (containment_budget - first_price * x1) / second_price
    allocation = [
        factors[index] * (x1 if roots[index] == 1 else x2)
        for index in range(9)
    ]
    require(all(0 < value <= cap for value, cap in zip(allocation, caps)), f"primal caps K={kprime}")
    require(allocation[0] == caps[0], f"corank-one cap K={kprime}")
    require(all(allocation[index] < caps[index] for index in range(1, 9)), f"other caps slack K={kprime}")
    require(sum(containment[i] * allocation[i] for i in range(9)) == containment_budget, f"containment K={kprime}")
    require(sum(shadow[i] * allocation[i] for i in range(9)) < shadow_budget, f"shadow slack K={kprime}")

    tight = []
    for step in range(2, 9):
        for d in range(step + 1, 10):
            left = raising(kprime, step, d) * allocation[d - 1]
            right = multiplicity(step, d) * allocation[d - step - 1]
            require(left <= right, f"hierarchy t={step} d={d} K={kprime}")
            if left == right:
                tight.append([step, d])
    require(tight == p["tight_hierarchy_rows"], f"tight rows K={kprime}")

    matrix = []
    for d in range(1, 10):
        row = [containment[d - 1], Fraction(1 if d == 1 else 0)]
        for step, source in tree:
            coefficient = Fraction(0)
            if d == source:
                coefficient += raising(kprime, step, source)
            if d == source - step:
                coefficient -= multiplicity(step, source)
            row.append(coefficient)
        matrix.append(row)
    dual = solve_exact(matrix, [Fraction(1) for _ in range(9)])
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
    return (-(-demand.numerator // demand.denominator), capacity.numerator // capacity.denominator)


def validate(data: object, exhaustive: bool = True) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-three-step-shadow-capacity-cut-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_two_step_nineshadow_capacity_cut",
        "rate_half_mca_rank11_kernel_multistep_shadow_hierarchy",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["previous_closed_maximum"], p["replay_minimum"], p["closed_dimension_maximum"], p["first_open_dimension"]) == (18101, 18102, 18158, 18159), "interval")
    require(p["replay_rows"] == 58, "row count")
    require(p["dual_tree"] == [[2, 3], [2, 4], [2, 6], [2, 8], [3, 5], [2, 7], [2, 9]], "dual tree")
    require(p["active_individual_caps"] == [1], "active cap")
    require(p["active_shared_resources"] == ["full_containment"], "active resource")
    require(p["slack_shared_resources"] == ["rank_preserving_nine_shadow"], "slack resource")
    endpoint, wall = p["closed_dimension_maximum"], p["first_open_dimension"]
    endpoint_optimum, _, _, endpoint_branches = certificate(p, endpoint)
    wall_optimum, _, _, _ = certificate(p, wall)
    require(endpoint_branches == p["endpoint_individual_branch_pattern"], "branches")
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
        lambda item: item["parameters"].__setitem__("closed_dimension_maximum", 18159),
        lambda item: item["parameters"].__setitem__("first_open_dimension", 18160),
        lambda item: item["parameters"]["dual_tree"].pop(),
        lambda item: item["parameters"]["tight_hierarchy_rows"].pop(),
        lambda item: item["parameters"].__setitem__("endpoint_gap", item["parameters"]["endpoint_gap"] - 1),
        lambda item: item["parameters"].__setitem__("wall_excess", item["parameters"]["wall_excess"] - 1),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered, exhaustive=False)
        except (Reject, KeyError, TypeError, ValueError, StopIteration):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_THREE_STEP_SHADOW_CAPACITY_CUT_PASS "
        f"checked={result['checked']} endpoint_gap={result['gap']} wall_excess={result['wall']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
