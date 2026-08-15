#!/usr/bin/env python3
"""Independent factor replay of the K'=22 payment."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    n = p["n_prime"]
    m = p["m_prime"]
    records = p["residual_record_floor"]
    marks = comb(n, 9) * p["uniform_rank9_chart_cap"]
    assert marks == p["global_rank9_mark_capacity"]

    premium = sum(
        p["premium_weights"][key]
        * p["refined_unstructured_sparse_caps"][key]
        for key in ("2", "3", "4", "5")
    )
    assert premium == p["active_refined_premium"]
    full_rank = (marks + records * premium) // 45
    assert full_rank == p["full_rank_capacity"]
    total = p["kernel_capacity"] + full_rank
    demand = (
        p["component_density_numerator"] * records * comb(m, 11)
        + p["component_density_denominator"]
        - 1
    ) // p["component_density_denominator"]
    assert total == p["total_capacity"]
    assert demand == p["required_incidence"]
    assert demand - total == p["demand_capacity_gap"] > 0
    print(
        "RATE_HALF_MCA_RANK11_K22_INTEGRAL_NEAR_SATURATION_PAYMENT_AUDIT_PASS "
        f"gap={demand - total} checks=8"
    )


if __name__ == "__main__":
    main()
