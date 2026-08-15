#!/usr/bin/env python3
"""Independent dual-certificate audit of the nine-shadow interval."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def product(values) -> int:
    return prod(values)


def support_local_cap(p: dict[str, int], kprime: int, d: int) -> int:
    if d == 9:
        return p["rank9_record_cap"]
    r = 10 - d
    short = kprime - r
    left = Fraction(
        product(range(p["n_offset"] + short - d, p["n_offset"] + short + 1)),
        (p["m_offset"] + short) * product(range(p["m_offset"] + 1, p["m_offset"] + d)),
    )
    right = Fraction(
        product(range(p["n_offset"], p["n_offset"] + d + 1)),
        product(range(p["m_offset"] + 1, p["m_offset"] + d + 1)),
    )
    best = max(left, right)
    return best.numerator // best.denominator


def caps_and_weights(p: dict[str, int], kprime: int) -> tuple[list[Fraction], list[Fraction]]:
    caps = []
    weights = []
    nprime = p["n_offset"] + kprime
    mprime = p["m_offset"] + kprime
    for d in range(1, 10):
        r = 10 - d
        if kprime - 10 < d + 1:
            caps.append(Fraction(0))
            weights.append(Fraction(0))
            continue
        extension = comb(kprime - 10, d + 1)
        ambient_integer = comb(nprime, r) * support_local_cap(p, kprime, d) * extension // (d + 2)
        record_integer = comb(mprime, r) * extension // (d + 2)
        caps.append(min(Fraction(ambient_integer, p["residual_record_floor"]), Fraction(record_integer)))
        weights.append(Fraction(comb(d + 2, 2), comb(kprime - d - 9, 2)))
    return caps, weights


def dual_optimum(p: dict[str, int], kprime: int) -> tuple[Fraction, int]:
    caps, weights = caps_and_weights(p, kprime)
    budget = Fraction(comb(p["m_offset"] + kprime, 9))
    spent = Fraction(0)
    frontier = 0
    for index, (cap, weight) in enumerate(zip(caps, weights)):
        if cap and spent + weight * cap > budget:
            frontier = index
            break
        spent += weight * cap
    if not frontier:
        return sum(caps, Fraction(0)), 0
    lam = 1 / weights[frontier]
    dual = lam * budget
    for index in range(frontier):
        dual += (1 - lam * weights[index]) * caps[index]
    return dual, frontier + 1


def demand_ratio(p: dict[str, int], kprime: int) -> Fraction:
    return Fraction(
        p["lane_density_numerator"] * comb(p["m_offset"] + kprime, 11),
        p["lane_density_denominator"],
    )


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    checked = 0
    for kprime in range(p["closed_dimension_minimum"], p["closed_dimension_maximum"] + 1):
        optimum, _ = dual_optimum(p, kprime)
        require(demand_ratio(p, kprime) > optimum, f"row {kprime}")
        checked += 1
    endpoint, endpoint_frontier = dual_optimum(p, p["closed_dimension_maximum"])
    wall, wall_frontier = dual_optimum(p, p["first_open_dimension"])
    require(endpoint_frontier == wall_frontier == 2, "frontiers")
    require(demand_ratio(p, p["closed_dimension_maximum"]) > endpoint, "endpoint")
    require(demand_ratio(p, p["first_open_dimension"]) < wall, "wall")
    require((p["residual_record_floor"] * endpoint).denominator == 1, "endpoint integer")
    require((p["residual_record_floor"] * wall).denominator == 1, "wall integer")
    require(int(p["residual_record_floor"] * endpoint) == p["endpoint_capacity"], "endpoint capacity")
    require(int(p["residual_record_floor"] * wall) == p["wall_capacity"], "wall capacity")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_CAPACITY_CUT_AUDIT_PASS "
        f"checked={checked} frontier={endpoint_frontier} wall={p['first_open_dimension']}"
    )


if __name__ == "__main__":
    main()
