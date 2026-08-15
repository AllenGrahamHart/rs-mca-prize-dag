#!/usr/bin/env python3
"""Verify the exact rank-eight nine-shadow kernel interval."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "bd95dca74b2f9018d78e9b89571d1175b7c5ad219bc48b6ec57167651d6835b3"


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


def resources_and_coefficients(
    p: dict[str, int], kprime: int, caps: list[Fraction]
) -> tuple[Fraction, Fraction, list[Fraction]]:
    shadow_budget = Fraction(comb(p["m_offset"] + kprime, p["shadow_subset_size"]))
    support_extensions = Fraction(comb(p["m_offset"] + kprime - p["shadow_subset_size"], 2))
    coefficients = []
    for index, cap in enumerate(caps):
        dimension = index + 1
        if not cap:
            coefficients.append(Fraction(0))
        elif dimension == 1:
            coefficients.append(52 + 3 * support_extensions / comb(kprime - 10, 2))
        elif dimension == 2:
            coefficients.append(
                55 + Fraction(6 * p["rank8_independent_pair_floor"], comb(kprime - 11, 2))
            )
        else:
            coefficients.append(Fraction(55))
    return shadow_budget, support_extensions * shadow_budget, coefficients


def dual_optimum(
    p: dict[str, int], kprime: int
) -> tuple[Fraction, Fraction, Fraction, list[int], list[int], list[int]]:
    weights, caps, _ = weights_caps_branches(p, kprime)
    shadow_budget, containment_budget, coefficients = resources_and_coefficients(p, kprime, caps)
    active = [index for index, cap in enumerate(caps) if cap]
    candidates = {(Fraction(0), Fraction(0))}
    for index in active:
        candidates.add((1 / weights[index], Fraction(0)))
        candidates.add((Fraction(0), 1 / coefficients[index]))
    for offset, left in enumerate(active):
        for right in active[offset + 1:]:
            determinant = weights[left] * coefficients[right] - weights[right] * coefficients[left]
            if not determinant:
                continue
            lam = (coefficients[right] - coefficients[left]) / determinant
            mu = (weights[left] - weights[right]) / determinant
            if lam >= 0 and mu >= 0:
                candidates.add((lam, mu))

    best = None
    best_data = None
    for lam, mu in sorted(candidates):
        value = lam * shadow_budget + mu * containment_budget
        tight, below, above = [], [], []
        for index in active:
            coverage = lam * weights[index] + mu * coefficients[index]
            if coverage == 1:
                tight.append(index + 1)
            elif coverage < 1:
                below.append(index + 1)
                value += (1 - coverage) * caps[index]
            else:
                above.append(index + 1)
        if best is None or value < best:
            best = value
            best_data = (lam, mu, tight, below, above)
    require(best is not None and best_data is not None, f"dual optimizer K={kprime}")
    return best, *best_data


def demand_ratio(p: dict[str, int], kprime: int) -> Fraction:
    return Fraction(
        p["lane_density_numerator"] * comb(p["m_offset"] + kprime, p["component_subset_size"]),
        p["lane_density_denominator"],
    )


def scaled_capacity(p: dict[str, int], optimum: Fraction) -> int:
    value = p["residual_record_floor"] * optimum
    return value.numerator // value.denominator


def demand_ceiling(p: dict[str, int], kprime: int) -> int:
    value = p["residual_record_floor"] * demand_ratio(p, kprime)
    return (value.numerator + value.denominator - 1) // value.denominator


def pattern_ranges(p: dict[str, int], end: int) -> list[list[object]]:
    output = []
    start = p["closed_dimension_minimum"]
    current = None
    for kprime in range(start, end + 1):
        _, _, _, tight, below, above = dual_optimum(p, kprime)
        pattern = [tight, below, above]
        if current is None:
            current = pattern
        elif pattern != current:
            output.append([start, kprime - 1, *current])
            start, current = kprime, pattern
    require(current is not None, "pattern ledger")
    output.append([start, end, *current])
    return output


def validate(data: object, exhaustive: bool = True) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-kernel-rank8-nineshadow-capacity-cut-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank11_kernel_nine_shadow_containment_capacity_cut",
            "rate_half_mca_rank11_kernel_rank8_nineshadow_extension_deficit",
        ],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["n_offset"], p["m_offset"]) == (1048576, 67472), "offsets")
    require(p["residual_record_floor"] == 274980728111260126, "record floor")
    require((p["lane_density_numerator"], p["lane_density_denominator"]) == (495405467, 10**9), "density")
    require((p["correction_dimension"], p["component_subset_size"], p["shadow_subset_size"]) == (10, 11, 9), "dimensions")
    require(p["rank8_independent_pair_floor"] == comb(67474, 2), "rank-eight pair floor")
    require((p["closed_dimension_minimum"], p["closed_dimension_maximum"], p["first_open_dimension"]) == (10, 17608, 17609), "interval")
    require((p["endpoint_tight_coranks"], p["endpoint_capped_coranks"], p["endpoint_zero_coranks"]) == ([2, 4], [1, 3], [5, 6, 7, 8, 9]), "endpoint pattern")

    endpoint = p["closed_dimension_maximum"]
    wall = p["first_open_dimension"]
    end_opt, end_lam, end_mu, end_tight, end_below, end_above = dual_optimum(p, endpoint)
    wall_opt, wall_lam, wall_mu, wall_tight, wall_below, wall_above = dual_optimum(p, wall)
    require((end_tight, end_below, end_above) == (p["endpoint_tight_coranks"], p["endpoint_capped_coranks"], p["endpoint_zero_coranks"]), "endpoint active set")
    require((wall_tight, wall_below, wall_above) == (p["endpoint_tight_coranks"], p["endpoint_capped_coranks"], p["endpoint_zero_coranks"]), "wall active set")
    require(weights_caps_branches(p, endpoint)[2] == p["endpoint_individual_branch_pattern"], "endpoint branches")
    require(end_lam == Fraction(p["endpoint_dual_lambda_numerator"], p["endpoint_dual_lambda_denominator"]), "endpoint lambda")
    require(end_mu == Fraction(p["endpoint_dual_mu_numerator"], p["endpoint_dual_mu_denominator"]), "endpoint mu")
    require(wall_lam == Fraction(p["wall_dual_lambda_numerator"], p["wall_dual_lambda_denominator"]), "wall lambda")
    require(wall_mu == Fraction(p["wall_dual_mu_numerator"], p["wall_dual_mu_denominator"]), "wall mu")
    require(end_opt == Fraction(p["endpoint_optimum_numerator"], p["endpoint_optimum_denominator"]), "endpoint optimum")
    require(wall_opt == Fraction(p["wall_optimum_numerator"], p["wall_optimum_denominator"]), "wall optimum")

    end_demand, end_cap = demand_ceiling(p, endpoint), scaled_capacity(p, end_opt)
    wall_demand, wall_cap = demand_ceiling(p, wall), scaled_capacity(p, wall_opt)
    require((end_demand, end_cap, end_demand - end_cap) == (p["endpoint_demand_ceiling"], p["endpoint_capacity"], p["endpoint_gap"]), "endpoint")
    require((wall_demand, wall_cap, wall_cap - wall_demand) == (p["wall_demand_ceiling"], p["wall_capacity"], p["wall_excess"]), "wall")
    require(demand_ratio(p, endpoint) > end_opt, "endpoint exact sign")
    require(demand_ratio(p, wall) < wall_opt, "wall exact sign")

    checked = 0
    if exhaustive:
        for kprime in range(p["closed_dimension_minimum"], endpoint + 1):
            require(demand_ratio(p, kprime) > dual_optimum(p, kprime)[0], f"capacity K={kprime}")
            checked += 1
        require(pattern_ranges(p, wall) == p["pattern_ledger"], "pattern ledger")
    require("remains open" in str(data.get("nonclaim")), "nonclaim")
    return {"checked": checked, "gap": end_demand - end_cap, "wall_excess": wall_cap - wall_demand}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("rank8_independent_pair_floor", 2276336600),
        lambda item: item["parameters"].__setitem__("closed_dimension_maximum", 17609),
        lambda item: item["parameters"].__setitem__("first_open_dimension", 17610),
        lambda item: item["parameters"]["endpoint_tight_coranks"].append(3),
        lambda item: item["parameters"].__setitem__("endpoint_optimum_denominator", 16755791041146967191306858),
        lambda item: item["parameters"].__setitem__("wall_excess", item["parameters"]["wall_excess"] - 1),
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
        "RATE_HALF_MCA_RANK11_KERNEL_RANK8_NINESHADOW_CAPACITY_CUT_PASS "
        f"checked={result['checked']} endpoint_gap={result['gap']} "
        f"wall_excess={result['wall_excess']} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
