#!/usr/bin/env python3
"""Exact next-row probe for the integral near-saturation payment."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, prod

import modal


app = modal.App("rs-mca-kb-refined-integral-near-saturation-next-row")
image = modal.Image.debian_slim()

RECORD_FLOOR = 274980728111260126


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def kernel_record_cap(kprime: int, corank: int) -> int:
    if corank == 1:
        return 8147918
    if corank == 9:
        return 61871313426630599
    rank = 10 - corank
    shortened = kprime - rank
    zero = Fraction(
        falling(1048576 + shortened, corank + 1),
        (67472 + shortened) * rising(67473, corank - 1),
    )
    endpoint = Fraction(
        falling(1048576 + corank, corank + 1), rising(67473, corank)
    )
    return int(max(zero, endpoint))


def exact_clean_cap(petal_mass: int, total: int, offset: int) -> int:
    a = petal_mass // 2 + 1
    b = petal_mass - 1
    width = b - a
    c0 = comb(petal_mass, 2) + offset * petal_mass

    def phi(weight: int) -> Fraction:
        return Fraction(c0, petal_mass - weight) - weight

    def value(light: int, count: int, full: int) -> Fraction:
        if full == count:
            return light * count * phi(b)
        minimum = count - full - 1
        residual = total - light - full * b - minimum * a
        return light * (full * phi(b) + minimum * phi(a) + phi(residual))

    def derivative(light: int, count: int, full: int) -> Fraction:
        minimum = count - full - 1
        delta = petal_mass - total + full * b + minimum * a
        constant = full * phi(b) + minimum * phi(a)
        denominator = light + delta
        return (
            2 * light
            + constant
            + delta
            - petal_mass
            + Fraction(c0 * delta, denominator * denominator)
        )

    candidates = []
    for count in range(1, total // a + 1):
        if total - count * b >= 0:
            high = total - count * b
            candidates.extend((value(0, count, count), value(high, count, count)))
        for full in range(count):
            low = max(0, total - count * a - (full + 1) * width + 1)
            high = min(total - count * a, total - count * a - full * width)
            if low > high:
                continue
            points = {low, high}
            minimum = count - full - 1
            delta = petal_mass - total + full * b + minimum * a
            if delta > 0:
                if (low + delta) ** 3 >= c0 * delta:
                    split = low
                elif (high + delta) ** 3 < c0 * delta:
                    split = high + 1
                else:
                    left, right = low, high
                    while left < right:
                        middle = (left + right) // 2
                        if (middle + delta) ** 3 >= c0 * delta:
                            right = middle
                        else:
                            left = middle + 1
                    split = left
                concave_high = min(high, split - 1)
                if (
                    low <= concave_high
                    and derivative(low, count, full) > 0
                    and derivative(concave_high, count, full) < 0
                ):
                    left, right = low, concave_high
                    while left < right:
                        middle = (left + right) // 2
                        if derivative(middle, count, full) <= 0:
                            right = middle
                        else:
                            left = middle + 1
                    points.update(range(max(low, left - 2), min(high, left + 2) + 1))
                points.update(range(max(low, split - 2), min(high, split + 2) + 1))
            candidates.extend(value(light, count, full) for light in points)
    best = max(candidates)
    return best.numerator // best.denominator


def chart(kprime: int, core: int) -> int:
    n = 1048576 + kprime
    m = 67472 + kprime
    petal = m - core
    total = n - core
    offset = core - 9
    clean = exact_clean_cap(petal, total, offset)
    heavy_min = petal // 2 + 1
    h = total // heavy_min
    cross = petal * petal // 4
    balanced = comb(total, 2) * (cross + offset * petal) // cross
    collision = comb(h, 2) * (comb(petal - 1, 2) + offset * petal)
    return clean + balanced + collision


def completion_value(m: int, support: int, completions: int) -> int:
    return completions * comb(m - support + 1 - completions, 11 - support)


@app.function(image=image, cpu=1, memory=512, timeout=60)
def scan_row(kprime: int) -> dict[str, object]:
    n = 1048576 + kprime
    m = 67472 + kprime
    q = kprime - 10
    weights = {2: 26, 3: 18, 4: 11, 5: 5}
    kernel_terms = {
        corank: comb(n, 10 - corank)
        * kernel_record_cap(kprime, corank)
        * comb(q, corank + 1)
        for corank in range(1, min(9, q - 1) + 1)
    }
    core_caps = {core: chart(kprime, core) for core in range(9, kprime)}
    maximizing_core = max(core_caps, key=core_caps.get)
    uniform_chart = core_caps[maximizing_core]
    marks = comb(n, 9) * uniform_chart

    structured = {
        support: comb(q + 4, support) * comb(m - support, 11 - support)
        for support in weights
    }
    refined = {}
    completion_maximizers = {}
    defect_depths = {2: 7, 3: 2, 4: 1, 5: 0}
    for support in weights:
        depth = defect_depths[support]
        ceiling = q - depth - 1
        values = {
            b: completion_value(m, support, b) for b in range(ceiling + 1)
        }
        completion_maximizers[support] = max(values, key=values.get)
        deletion = comb(m, support - 1) * max(values.values()) // support
        carrier = max(
            [0]
            + [
                comb(q + (defect + 1) * (support - 1), support)
                * comb(m - support, 11 - support)
                for defect in range(1, depth + 1)
            ]
        )
        refined[support] = max(carrier, deletion)
    structured_premium = sum(weights[c] * structured[c] for c in weights)
    refined_premium = sum(weights[c] * refined[c] for c in weights)
    premium = max(structured_premium, refined_premium)
    full_rank = (marks + RECORD_FLOOR * premium) // 45
    kernel = sum(kernel_terms.values())
    total_capacity = kernel + full_rank
    demand = (990810934 * RECORD_FLOOR * comb(m, 11) + 10**9 - 1) // 10**9
    coefficient = 45 * 990810934 * comb(m, 11) - 10**9 * premium
    raw = RECORD_FLOOR * coefficient - 10**9 * (45 * kernel + marks)
    return {
        "K_prime": kprime,
        "maximizing_core": maximizing_core,
        "uniform_chart_cap": uniform_chart,
        "kernel_capacity": kernel,
        "kernel_terms": kernel_terms,
        "completion_maximizers": completion_maximizers,
        "defect_depths": defect_depths,
        "structured_premium": structured_premium,
        "refined_premium": refined_premium,
        "full_rank_capacity": full_rank,
        "total_capacity": total_capacity,
        "demand": demand,
        "demand_minus_capacity": demand - total_capacity,
        "record_coefficient_cross": coefficient,
        "floor_record_raw_cross": raw,
        "closed": demand > total_capacity and coefficient > 0 and raw > 0,
    }


@app.local_entrypoint()
def main() -> None:
    rows = list(scan_row.map(range(23, 33)))
    summary = [
        {
            "K_prime": row["K_prime"],
            "closed": row["closed"],
            "gap": row["demand_minus_capacity"],
            "maximizing_core": row["maximizing_core"],
            "chart": row["uniform_chart_cap"],
            "premium": row["refined_premium"],
            "completion_maximizers": row["completion_maximizers"],
        }
        for row in rows
    ]
    print(json.dumps(summary, sort_keys=True))
