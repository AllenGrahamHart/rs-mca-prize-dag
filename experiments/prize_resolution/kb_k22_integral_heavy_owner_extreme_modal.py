#!/usr/bin/env python3
"""Parallel Modal scan for the K'=22 integral heavy-owner refinement."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb

import modal


app = modal.App("rs-mca-kb-k22-integral-heavy-owner-extreme")
image = modal.Image.debian_slim()

K_PRIME = 22
N = 1048576 + K_PRIME
M = 67472 + K_PRIME
QUOTIENT = K_PRIME - 10
RECORD_FLOOR = 274980728111260126
DENSITY_NUMERATOR = 990810934
DENSITY_DENOMINATOR = 10**9
OLD_KERNEL = 4544755400241440301976843848483621233979526109437329236980
OLD_CORANK_ONE_CAP = 16295594
NEW_CORANK_ONE_CAP = 8147918
PREMIUM = 5579560234662661302007958073521631030576667405


def phi_float(petal_mass: int, offset: int, weight: int) -> float:
    c0 = comb(petal_mass, 2) + offset * petal_mass
    return c0 / (petal_mass - weight) - weight


def phi_exact(petal_mass: int, offset: int, weight: int) -> Fraction:
    c0 = comb(petal_mass, 2) + offset * petal_mass
    return Fraction(c0, petal_mass - weight) - weight


def extreme_weights(
    heavy_budget: int, count: int, heavy_min: int, heavy_max: int
) -> tuple[int, int, int]:
    """Return full-max count, one residual weight, and min-weight count."""
    width = heavy_max - heavy_min
    excess = heavy_budget - count * heavy_min
    full = min(count, excess // width)
    if full == count:
        return full, 0, 0
    residual = heavy_min + excess - full * width
    return full, residual, count - full - 1


@app.function(image=image, cpu=1, memory=512, timeout=60)
def scan_core(core: int) -> dict[str, object]:
    petal_mass = M - core
    total = N - core
    offset = core - 9
    heavy_min = petal_mass // 2 + 1
    heavy_max = petal_mass - 1

    best_value = -1.0
    best = None
    checked = 0
    for light in range(total + 1):
        heavy_budget = total - light
        max_count = heavy_budget // heavy_min
        for count in range(1, max_count + 1):
            full, residual, minimum = extreme_weights(
                heavy_budget, count, heavy_min, heavy_max
            )
            density = full * phi_float(petal_mass, offset, heavy_max)
            density += minimum * phi_float(petal_mass, offset, heavy_min)
            if residual:
                density += phi_float(petal_mass, offset, residual)
            value = light * density
            checked += 1
            if value > best_value:
                best_value = value
                best = (light, count, full, residual, minimum)

    assert best is not None
    light, count, full, residual, minimum = best
    exact_density = full * phi_exact(petal_mass, offset, heavy_max)
    exact_density += minimum * phi_exact(petal_mass, offset, heavy_min)
    if residual:
        exact_density += phi_exact(petal_mass, offset, residual)
    exact_value = light * exact_density
    clean = exact_value.numerator // exact_value.denominator

    h = total // heavy_min
    cross_floor = petal_mass * petal_mass // 4
    balanced = (
        comb(total, 2) * (cross_floor + offset * petal_mass) // cross_floor
    )
    collision = comb(h, 2) * (comb(petal_mass - 1, 2) + offset * petal_mass)
    return {
        "core": core,
        "petal_mass": petal_mass,
        "total": total,
        "offset": offset,
        "checked_integer_states": checked,
        "maximizer": {
            "light_mass": light,
            "heavy_budget": total - light,
            "owner_count": count,
            "full_max_owners": full,
            "residual_owner_weight": residual,
            "minimum_weight_owners": minimum,
        },
        "clean_cap": clean,
        "balanced_cap": balanced,
        "collision_cap": collision,
        "chart_cap": clean + balanced + collision,
    }


@app.local_entrypoint()
def main() -> None:
    rows = list(scan_core.map(range(9, K_PRIME)))
    chart_row = max(rows, key=lambda item: int(item["chart_cap"]))
    chart = int(chart_row["chart_cap"])

    old_corank_one_term = (
        comb(N, 9) * OLD_CORANK_ONE_CAP * comb(QUOTIENT, 2)
    )
    new_corank_one_term = (
        comb(N, 9) * NEW_CORANK_ONE_CAP * comb(QUOTIENT, 2)
    )
    kernel = OLD_KERNEL - old_corank_one_term + new_corank_one_term
    marks = comb(N, 9) * chart
    full_rank = (marks + RECORD_FLOOR * PREMIUM) // 45
    total_capacity = kernel + full_rank
    demand = (
        DENSITY_NUMERATOR * RECORD_FLOOR * comb(M, 11)
        + DENSITY_DENOMINATOR
        - 1
    ) // DENSITY_DENOMINATOR
    result = {
        "K_prime": K_PRIME,
        "core_rows": rows,
        "maximizing_core": int(chart_row["core"]),
        "uniform_chart_cap": chart,
        "old_kernel_cap": OLD_KERNEL,
        "new_kernel_cap": kernel,
        "kernel_saving": OLD_KERNEL - kernel,
        "full_rank_cap": full_rank,
        "total_capacity": total_capacity,
        "demand": demand,
        "demand_minus_capacity": demand - total_capacity,
        "closed": demand > total_capacity,
    }
    print(json.dumps(result, sort_keys=True))
