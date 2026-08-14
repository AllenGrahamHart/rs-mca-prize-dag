#!/usr/bin/env python3
"""Independent dual audit of the full-containment interval."""

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


def local_record_cap(p: dict[str, int], kprime: int, d: int) -> int:
    if d == 9:
        return p["rank9_record_cap"]
    r = 10 - d
    short = kprime - r
    left = Fraction(
        falling(p["n_offset"] + short, d + 1),
        (p["m_offset"] + short) * rising(p["m_offset"] + 1, d - 1),
    )
    right = Fraction(
        falling(p["n_offset"] + d, d + 1),
        rising(p["m_offset"] + 1, d),
    )
    value = max(left, right)
    return value.numerator // value.denominator


def individual_cap_sum(p: dict[str, int], kprime: int) -> Fraction:
    nprime = p["n_offset"] + kprime
    mprime = p["m_offset"] + kprime
    total = Fraction(0)
    for d in range(1, 10):
        if kprime - 10 < d + 1:
            continue
        r = 10 - d
        ext = comb(kprime - 10, d + 1)
        ambient = Fraction(
            comb(nprime, r) * local_record_cap(p, kprime, d) * ext // (d + 2),
            p["residual_record_floor"],
        )
        record = Fraction(comb(mprime, r) * ext // (d + 2))
        total += min(ambient, record)
    return total


def dual_shadow_bound(p: dict[str, int], kprime: int) -> Fraction | None:
    if kprime < 13:
        return None
    mprime = p["m_offset"] + kprime
    budget = Fraction(comb(mprime, 9))
    e0 = Fraction(comb(mprime - 9, 2))
    e1 = Fraction(comb(kprime - 10, 2))
    e2 = Fraction(comb(kprime - 11, 2))
    w1 = Fraction(3, e1)
    w2 = Fraction(6, e2)
    v1 = 52 + 3 * e0 / e1
    determinant = v1 * w2 - 55 * w1
    require(determinant > 0, f"determinant {kprime}")
    lam = (v1 - 55) / determinant
    mu = (w2 - w1) / determinant
    require(lam >= 0 and mu >= 0, f"dual signs {kprime}")
    require(lam * w1 + mu * v1 == 1, f"dual d1 {kprime}")
    require(lam * w2 + 55 * mu == 1, f"dual d2 {kprime}")
    for d in range(3, 10):
        if kprime - d - 9 < 2:
            continue
        wd = Fraction(comb(d + 2, 2), comb(kprime - d - 9, 2))
        require(lam * wd + 55 * mu >= 1, f"dual d={d} K={kprime}")
    return lam * budget + mu * e0 * budget


def demand_ratio(p: dict[str, int], kprime: int) -> Fraction:
    return Fraction(
        p["lane_density_numerator"] * comb(p["m_offset"] + kprime, 11),
        p["lane_density_denominator"],
    )


def audit_bound(p: dict[str, int], kprime: int) -> Fraction:
    individual = individual_cap_sum(p, kprime)
    dual = dual_shadow_bound(p, kprime)
    return individual if dual is None else min(individual, dual)


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    checked = 0
    for kprime in range(p["closed_dimension_minimum"], p["closed_dimension_maximum"] + 1):
        require(demand_ratio(p, kprime) > audit_bound(p, kprime), f"row {kprime}")
        checked += 1
    endpoint = dual_shadow_bound(p, p["closed_dimension_maximum"])
    wall = dual_shadow_bound(p, p["first_open_dimension"])
    require(endpoint is not None and wall is not None, "boundary duals")
    require(endpoint == Fraction(p["endpoint_optimum_numerator"], p["endpoint_optimum_denominator"]), "endpoint optimum")
    require(wall == Fraction(p["wall_optimum_numerator"], p["wall_optimum_denominator"]), "wall optimum")
    require(demand_ratio(p, p["closed_dimension_maximum"]) > endpoint, "endpoint sign")
    require(demand_ratio(p, p["first_open_dimension"]) < wall, "wall sign")
    endpoint_scaled = p["residual_record_floor"] * endpoint
    wall_scaled = p["residual_record_floor"] * wall
    require(endpoint_scaled.numerator // endpoint_scaled.denominator == p["endpoint_capacity"], "endpoint capacity")
    require(wall_scaled.numerator // wall_scaled.denominator == p["wall_capacity"], "wall capacity")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_CONTAINMENT_CAPACITY_CUT_AUDIT_PASS "
        f"checked={checked} active=1,2 wall={p['first_open_dimension']}"
    )


if __name__ == "__main__":
    main()
