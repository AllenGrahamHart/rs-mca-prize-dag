#!/usr/bin/env python3
"""Independent exact audit of the K'=14..21 payment batch."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
R_BASE = 1048576
W_BASE = 67472


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def independent_record_cap(kprime: int, corank: int) -> int:
    if corank == 9:
        return 61871313426630599
    rank = 10 - corank
    shift = kprime - rank
    zero_num = prod(range(R_BASE + shift - corank, R_BASE + shift + 1))
    zero_den = (W_BASE + shift) * prod(range(W_BASE + 1, W_BASE + corank))
    far_num = prod(range(R_BASE, R_BASE + corank + 1))
    far_den = prod(range(W_BASE + 1, W_BASE + corank + 1))
    return int(max(Fraction(zero_num, zero_den), Fraction(far_num, far_den)))


def independent_offset(petal: int, total: int, offset: int) -> int:
    heavy = total // (petal // 2 + 1)
    cross = petal**2 // 4
    balanced = (cross + offset * petal) * total * (total - 1) // 2 // cross
    collision = (
        heavy * (heavy - 1) // 2
        * ((petal - 1) * (petal - 2) // 2 + offset * petal)
    )
    linear = (petal - 2) * total + 2 * heavy * offset * petal
    quadratic = petal - 2
    vertex = Fraction(linear, 2 * quadratic)
    floor_vertex = vertex.numerator // vertex.denominator
    clean = max(
        light * (linear - quadratic * light) // 2
        for light in {0, total, floor_vertex, floor_vertex + 1}
        if 0 <= light <= total
    )
    return clean + balanced + collision


def analytic_completion_maximum(m: int, support: int, ceiling: int) -> tuple[int, int]:
    exponent = 11 - support
    size = m - support + 1
    threshold = Fraction(size - exponent, exponent + 1)
    pivot = (threshold.numerator + threshold.denominator - 1) // threshold.denominator
    pivot = min(ceiling, max(1, pivot))
    candidates = range(max(1, pivot - 2), min(ceiling, pivot + 2) + 1)
    return max(
        (completion * comb(size - completion, exponent), completion)
        for completion in candidates
    )


def independent_row(kprime: int) -> dict[str, int]:
    n = R_BASE + kprime
    m = W_BASE + kprime
    quotient = kprime - 10
    records = 274980728111260126

    kernel_terms = []
    for corank in range(1, min(9, quotient - 1) + 1):
        kernel_terms.append(
            comb(n, 10 - corank)
            * independent_record_cap(kprime, corank)
            * comb(quotient, corank + 1)
        )
    kernel = sum(kernel_terms)

    core_caps = [
        independent_offset(m - core, n - core, core - 9)
        for core in range(9, kprime)
    ]
    chart = max(core_caps)
    marks = comb(n, 9) * chart

    structured = []
    unstructured = []
    maximizers = []
    for support in range(2, 6):
        structured.append(comb(quotient + 4, support) * comb(m - support, 11 - support))
        completion_value, completion = analytic_completion_maximum(m, support, quotient - 1)
        maximizers.append(completion)
        unstructured.append(comb(m, support - 1) * completion_value // support)
    weights = [26, 18, 11, 5]
    premiums = [
        sum(weight * cap for weight, cap in zip(weights, branch))
        for branch in (structured, unstructured)
    ]
    premium = max(premiums)
    full_rank = (marks + records * premium) // 45
    total = kernel + full_rank
    demand = -(-990810934 * records * comb(m, 11) // 10**9)
    coefficient = 45 * 990810934 * comb(m, 11) - 10**9 * premium
    raw = records * coefficient - 10**9 * (45 * kernel + marks)
    return {
        "kernel": kernel,
        "chart": chart,
        "maximizing_core": 9 + core_caps.index(chart),
        "premium": premium,
        "total": total,
        "demand": demand,
        "gap": demand - total,
        "coefficient": coefficient,
        "raw": raw,
        "completion_min": min(maximizers),
        "completion_max": max(maximizers),
        "core_checks": len(core_caps),
    }


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    rows = {str(kprime): independent_row(kprime) for kprime in range(14, 22)}
    require({key: row["kernel"] for key, row in rows.items()} == p["kernel_caps"], "independent kernels")
    require({key: row["chart"] for key, row in rows.items()} == p["uniform_rank9_chart_caps"], "independent charts")
    require({key: row["premium"] for key, row in rows.items()} == p["active_sparse_premiums"], "independent premiums")
    require({key: row["total"] for key, row in rows.items()} == p["total_capacities_at_record_floor"], "independent totals")
    require({key: row["demand"] for key, row in rows.items()} == p["required_incidences_at_record_floor"], "independent demands")
    require({key: row["gap"] for key, row in rows.items()} == p["demand_capacity_gaps"], "independent gaps")
    require(all(row["maximizing_core"] == int(key) - 1 for key, row in rows.items()), "independent core maxima")
    require(all(row["completion_min"] == row["completion_max"] == int(key) - 11 for key, row in rows.items()), "independent completion maxima")
    require(all(row["coefficient"] > 0 and row["raw"] > 0 for row in rows.values()), "independent persistence")

    wall = independent_row(22)
    require(wall["total"] == p["K22_method_wall"]["total_capacity_at_record_floor"], "wall total")
    require(wall["demand"] == p["K22_method_wall"]["required_incidence_at_record_floor"], "wall demand")
    require(-wall["gap"] == p["K22_method_wall"]["capacity_excess"] > 0, "wall excess")
    print(
        "PASS K14..K21 joint sparse-shadow payment independent: "
        f"{sum(row['core_checks'] for row in rows.values())} core charts, "
        f"minimum gap {rows['21']['gap']}, K22 excess {-wall['gap']}"
    )


if __name__ == "__main__":
    main()
