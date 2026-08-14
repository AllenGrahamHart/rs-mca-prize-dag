#!/usr/bin/env python3
"""Independent recurrence audit of the two-step hierarchy capacity."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def short_fall(value: int, length: int) -> int:
    return prod(value - offset for offset in range(length))


def short_rise(value: int, length: int) -> int:
    return prod(value + offset for offset in range(length))


def local_record_cap(p: dict[str, int], kprime: int, rank: int) -> int:
    d = 10 - rank
    if d == 9:
        return p["rank9_record_cap"]
    shortened = kprime - rank
    first = Fraction(
        short_fall(p["n_offset"] + shortened, d + 1),
        (p["m_offset"] + shortened) * short_rise(p["m_offset"] + 1, d - 1),
    )
    second = Fraction(
        short_fall(p["n_offset"] + d, d + 1),
        short_rise(p["m_offset"] + 1, d),
    )
    return int(max(first, second))


def audit_data(p: dict[str, int], kprime: int):
    nprime, mprime = p["n_offset"] + kprime, p["m_offset"] + kprime
    caps, shadow_weights, containment_weights = [], [], []
    for rank in range(9, 0, -1):
        d = 10 - rank
        extensions = comb(kprime - 10, d + 1)
        ambient = Fraction(
            comb(nprime, rank) * local_record_cap(p, kprime, rank) * extensions // (d + 2),
            p["residual_record_floor"],
        )
        support = Fraction(comb(mprime, rank) * extensions // (d + 2))
        caps.append(min(ambient, support))
        shadow_weights.append(Fraction(comb(d + 2, 2), comb(kprime - d - 9, 2)))
        if d == 1:
            e0 = comb(mprime - 9, 2)
            containment_weights.append(52 + Fraction(3 * e0, comb(kprime - 10, 2)))
        elif d == 2:
            containment_weights.append(55 + Fraction(6 * comb(67474, 2), comb(kprime - 11, 2)))
        else:
            containment_weights.append(Fraction(55))
    shadow_budget = Fraction(comb(mprime, 9))
    containment_budget = Fraction(comb(mprime - 9, 2) * comb(mprime, 9))
    return caps, shadow_weights, containment_weights, shadow_budget, containment_budget


def recurrence_certificate(p: dict[str, int], kprime: int):
    caps, shadow, containment, shadow_budget, containment_budget = audit_data(p, kprime)
    raising = {
        d: Fraction(comb(d + 2, 2) * comb(67472 + d, 2), comb(kprime - d - 9, 2))
        for d in range(3, 10)
    }
    multiplicity = {d: comb(11 - d, 2) for d in range(3, 10)}

    factors = [Fraction(1), Fraction(1)] + [Fraction(0) for _ in range(7)]
    for d in range(3, 10):
        factors[d - 1] = multiplicity[d] * factors[d - 3] / raising[d]
    odd_base = caps[0]
    odd_price = sum(containment[index] * factors[index] for index in range(0, 9, 2))
    even_price = sum(containment[index] * factors[index] for index in range(1, 9, 2))
    even_base = (containment_budget - odd_price * odd_base) / even_price
    allocation = [
        factor * (odd_base if index % 2 == 0 else even_base)
        for index, factor in enumerate(factors)
    ]

    def hierarchy_multipliers(mu: Fraction) -> dict[int, Fraction]:
        values: dict[int, Fraction] = {}
        for parity_top in (9, 8):
            for d in range(parity_top, 2, -2):
                child = multiplicity[d + 2] * values[d + 2] if d + 2 <= 9 else Fraction(0)
                values[d] = (1 - mu * containment[d - 1] + child) / raising[d]
        return values

    def even_equation(mu: Fraction) -> Fraction:
        values = hierarchy_multipliers(mu)
        return mu * containment[1] - multiplicity[4] * values[4] - 1

    at_zero, at_one = even_equation(Fraction(0)), even_equation(Fraction(1))
    mu = -at_zero / (at_one - at_zero)
    hierarchy_dual = hierarchy_multipliers(mu)
    eta = 1 - mu * containment[0] + multiplicity[3] * hierarchy_dual[3]
    require(mu >= 0 and eta >= 0, f"base dual signs K={kprime}")
    require(all(value >= 0 for value in hierarchy_dual.values()), f"hierarchy dual signs K={kprime}")

    for d in range(1, 10):
        coverage = mu * containment[d - 1]
        if d == 1:
            coverage += eta
        if d >= 3:
            coverage += raising[d] * hierarchy_dual[d]
        if d + 2 <= 9:
            coverage -= multiplicity[d + 2] * hierarchy_dual[d + 2]
        require(coverage == 1, f"dual equality d={d} K={kprime}")

    require(all(0 < value <= cap for value, cap in zip(allocation, caps)), f"primal bounds K={kprime}")
    require(allocation[0] == caps[0], f"cap equality K={kprime}")
    require(sum(shadow[i] * allocation[i] for i in range(9)) < shadow_budget, f"shadow slack K={kprime}")
    require(sum(containment[i] * allocation[i] for i in range(9)) == containment_budget, f"containment equality K={kprime}")
    for d in range(3, 10):
        require(raising[d] * allocation[d - 1] == multiplicity[d] * allocation[d - 3], f"hierarchy primal d={d} K={kprime}")
    optimum = sum(allocation, Fraction(0))
    require(mu * containment_budget + eta * caps[0] == optimum, f"strong duality K={kprime}")
    return optimum


def demand_ratio(p: dict[str, int], kprime: int) -> Fraction:
    return Fraction(p["lane_density_numerator"] * comb(p["m_offset"] + kprime, 11), p["lane_density_denominator"])


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    checked = 0
    for kprime in range(p["replay_minimum"], p["closed_dimension_maximum"] + 1):
        require(demand_ratio(p, kprime) > recurrence_certificate(p, kprime), f"closed row K={kprime}")
        checked += 1
    endpoint = recurrence_certificate(p, p["closed_dimension_maximum"])
    wall = recurrence_certificate(p, p["first_open_dimension"])
    require(endpoint == Fraction(p["endpoint_optimum_numerator"], p["endpoint_optimum_denominator"]), "endpoint optimum")
    require(wall == Fraction(p["wall_optimum_numerator"], p["wall_optimum_denominator"]), "wall optimum")
    require(demand_ratio(p, p["first_open_dimension"]) < wall, "wall sign")
    endpoint_scaled = p["residual_record_floor"] * endpoint
    wall_scaled = p["residual_record_floor"] * wall
    require(endpoint_scaled.numerator // endpoint_scaled.denominator == p["endpoint_capacity"], "endpoint capacity")
    require(wall_scaled.numerator // wall_scaled.denominator == p["wall_capacity"], "wall capacity")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_TWO_STEP_NINESHADOW_CAPACITY_CUT_AUDIT_PASS "
        f"checked={checked + 1} wall={p['first_open_dimension']} recurrences=7"
    )


if __name__ == "__main__":
    main()
