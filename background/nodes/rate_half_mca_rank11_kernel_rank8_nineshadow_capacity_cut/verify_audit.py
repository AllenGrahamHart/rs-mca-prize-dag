#!/usr/bin/env python3
"""Independent primal-ledger audit of the rank-eight nine-shadow interval."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def support_local_cap(p: dict[str, int], kprime: int, d: int) -> int:
    if d == 9:
        return p["rank9_record_cap"]
    rank = 10 - d
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


def lp_data(
    p: dict[str, int], kprime: int
) -> tuple[list[Fraction], list[Fraction], list[Fraction], Fraction, Fraction]:
    nprime = p["n_offset"] + kprime
    mprime = p["m_offset"] + kprime
    caps, weights, coefficients = [], [], []
    for d in range(1, 10):
        if kprime - 10 < d + 1:
            caps.append(Fraction(0))
            weights.append(Fraction(0))
            coefficients.append(Fraction(0))
            continue
        extension = comb(kprime - 10, d + 1)
        ambient = Fraction(
            comb(nprime, 10 - d) * support_local_cap(p, kprime, d) * extension // (d + 2),
            p["residual_record_floor"],
        )
        record = Fraction(comb(mprime, 10 - d) * extension // (d + 2))
        caps.append(min(ambient, record))
        weights.append(Fraction(comb(d + 2, 2), comb(kprime - d - 9, 2)))
        coefficients.append(Fraction(0))
    shadow_budget = Fraction(comb(mprime, 9))
    e0 = Fraction(comb(mprime - 9, 2))
    for index, cap in enumerate(caps):
        d = index + 1
        if not cap:
            coefficients[index] = Fraction(0)
        elif d == 1:
            coefficients[index] = 52 + 3 * e0 / comb(kprime - 10, 2)
        elif d == 2:
            coefficients[index] = 55 + Fraction(
                6 * p["rank8_independent_pair_floor"], comb(kprime - 11, 2)
            )
        else:
            coefficients[index] = Fraction(55)
    return caps, weights, coefficients, shadow_budget, e0 * shadow_budget


def ledger_pattern(p: dict[str, object], kprime: int) -> tuple[list[int], list[int], list[int]]:
    for start, end, tight, capped, zero in p["pattern_ledger"]:
        if start <= kprime <= end:
            return tight, capped, zero
    raise ValueError(f"missing ledger row {kprime}")


def primal_certificate(
    p: dict[str, object], kprime: int
) -> tuple[Fraction, Fraction, Fraction, list[Fraction]]:
    caps, weights, coefficients, shadow_budget, containment_budget = lp_data(p, kprime)
    tight, capped, zero = ledger_pattern(p, kprime)
    active = {index + 1 for index, cap in enumerate(caps) if cap}
    require(active == set(tight) | set(capped) | set(zero), f"ledger partition K={kprime}")

    if not tight:
        lam, mu = Fraction(0), Fraction(0)
    elif len(tight) == 1:
        index = tight[0] - 1
        require(tight == [1], f"single tight K={kprime}")
        lam, mu = Fraction(0), 1 / coefficients[index]
    else:
        require(len(tight) == 2, f"tight count K={kprime}")
        left, right = tight[0] - 1, tight[1] - 1
        determinant = weights[left] * coefficients[right] - weights[right] * coefficients[left]
        lam = (coefficients[right] - coefficients[left]) / determinant
        mu = (weights[left] - weights[right]) / determinant
    require(lam >= 0 and mu >= 0, f"dual signs K={kprime}")

    for d in active:
        coverage = lam * weights[d - 1] + mu * coefficients[d - 1]
        if d in tight:
            require(coverage == 1, f"tight coverage d={d} K={kprime}")
        elif d in capped:
            require(coverage < 1, f"capped coverage d={d} K={kprime}")
        else:
            require(coverage > 1, f"zero coverage d={d} K={kprime}")

    allocation = [Fraction(0) for _ in range(9)]
    for d in capped:
        allocation[d - 1] = caps[d - 1]
    remaining_shadow = shadow_budget - sum(weights[i] * allocation[i] for i in range(9))
    remaining_containment = containment_budget - sum(
        coefficients[i] * allocation[i] for i in range(9)
    )
    if len(tight) == 1:
        index = tight[0] - 1
        allocation[index] = remaining_containment / coefficients[index]
    elif len(tight) == 2:
        left, right = tight[0] - 1, tight[1] - 1
        determinant = weights[left] * coefficients[right] - weights[right] * coefficients[left]
        allocation[left] = (
            remaining_shadow * coefficients[right] - weights[right] * remaining_containment
        ) / determinant
        allocation[right] = (
            weights[left] * remaining_containment - remaining_shadow * coefficients[left]
        ) / determinant
    require(all(0 <= value <= cap for value, cap in zip(allocation, caps)), f"primal bounds K={kprime}")
    require(sum(weights[i] * allocation[i] for i in range(9)) <= shadow_budget, f"shadow primal K={kprime}")
    require(
        sum(coefficients[i] * allocation[i] for i in range(9)) <= containment_budget,
        f"containment primal K={kprime}",
    )

    dual = lam * shadow_budget + mu * containment_budget
    for d in capped:
        coverage = lam * weights[d - 1] + mu * coefficients[d - 1]
        dual += (1 - coverage) * caps[d - 1]
    primal = sum(allocation, Fraction(0))
    require(primal == dual, f"strong duality K={kprime}")
    return primal, lam, mu, allocation


def demand_ratio(p: dict[str, int], kprime: int) -> Fraction:
    return Fraction(
        p["lane_density_numerator"] * comb(p["m_offset"] + kprime, 11),
        p["lane_density_denominator"],
    )


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    checked = 0
    for kprime in range(p["closed_dimension_minimum"], p["closed_dimension_maximum"] + 1):
        optimum, _, _, _ = primal_certificate(p, kprime)
        require(demand_ratio(p, kprime) > optimum, f"closed sign K={kprime}")
        checked += 1

    endpoint, end_lam, end_mu, end_allocation = primal_certificate(p, p["closed_dimension_maximum"])
    wall, wall_lam, wall_mu, wall_allocation = primal_certificate(p, p["first_open_dimension"])
    require(endpoint == Fraction(p["endpoint_optimum_numerator"], p["endpoint_optimum_denominator"]), "endpoint optimum")
    require(wall == Fraction(p["wall_optimum_numerator"], p["wall_optimum_denominator"]), "wall optimum")
    require(end_lam == Fraction(p["endpoint_dual_lambda_numerator"], p["endpoint_dual_lambda_denominator"]), "endpoint lambda")
    require(end_mu == Fraction(p["endpoint_dual_mu_numerator"], p["endpoint_dual_mu_denominator"]), "endpoint mu")
    require(wall_lam == Fraction(p["wall_dual_lambda_numerator"], p["wall_dual_lambda_denominator"]), "wall lambda")
    require(wall_mu == Fraction(p["wall_dual_mu_numerator"], p["wall_dual_mu_denominator"]), "wall mu")
    require([index + 1 for index, value in enumerate(end_allocation) if value] == [1, 2, 3, 4], "endpoint support")
    require([index + 1 for index, value in enumerate(wall_allocation) if value] == [1, 2, 3, 4], "wall support")
    require(demand_ratio(p, p["first_open_dimension"]) < wall, "wall sign")
    end_scaled = p["residual_record_floor"] * endpoint
    wall_scaled = p["residual_record_floor"] * wall
    require(end_scaled.numerator // end_scaled.denominator == p["endpoint_capacity"], "endpoint capacity")
    require(wall_scaled.numerator // wall_scaled.denominator == p["wall_capacity"], "wall capacity")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_RANK8_NINESHADOW_CAPACITY_CUT_AUDIT_PASS "
        f"checked={checked} patterns={len(p['pattern_ledger'])} wall={p['first_open_dimension']}"
    )


if __name__ == "__main__":
    main()
