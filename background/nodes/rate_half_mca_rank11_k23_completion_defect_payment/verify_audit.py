#!/usr/bin/env python3
"""Independent factor audit of the K'=23 payment and K'=24 wall."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def compare(p: dict, wall: bool = False) -> int:
    if wall:
        w = p["K24_method_wall"]
        return w["required_incidence"] - w["total_capacity"]
    marks = comb(p["n_prime"], 9) * p["uniform_rank9_chart_cap"]
    assert marks == p["global_rank9_mark_capacity"]
    premium = sum(
        p["premium_weights"][key] * p["refined_sparse_caps"][key]
        for key in ("2", "3", "4", "5")
    )
    assert premium == p["active_refined_premium"]
    full = (marks + p["residual_record_floor"] * premium) // 45
    assert full == p["full_rank_capacity"]
    total = p["kernel_capacity"] + full
    demand = (
        p["component_density_numerator"]
        * p["residual_record_floor"]
        * comb(p["m_prime"], 11)
        + p["component_density_denominator"]
        - 1
    ) // p["component_density_denominator"]
    assert total == p["total_capacity"]
    assert demand == p["required_incidence"]
    return demand - total


def main() -> None:
    p = json.loads(CONTRACT.read_text())["parameters"]
    gap = compare(p)
    wall = compare(p, wall=True)
    assert gap == p["demand_capacity_gap"] > 0
    assert wall == -p["K24_method_wall"]["capacity_excess"] < 0
    assert max(p["core_chart_caps"], key=p["core_chart_caps"].get) == "22"
    print(
        "RATE_HALF_MCA_RANK11_K23_COMPLETION_DEFECT_PAYMENT_AUDIT_PASS "
        f"gap={gap} wall={-wall} checks=10"
    )


if __name__ == "__main__":
    main()
