#!/usr/bin/env python3
"""Independent endpoint audit for the K'=41 sharp-isolated payment."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
PARENT = (
    Path(__file__).resolve().parents[1]
    / "rate_half_mca_rank11_k24_k40_full_deficit_shadow_payment/source_contract.json"
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    parent = json.loads(PARENT.read_text())
    p = data["parameters"]
    old = parent["parameters"]["K41_method_wall"]
    require(p["total_capacity"] == old["total_capacity"], "unchanged capacity")
    require(p["kernel_capacity"] == old["kernel_capacity"], "unchanged kernel")

    records = p["residual_record_floor"]
    demand = records * comb(p["m"], 11) - comb(p["n"], 11)
    gap = demand - p["total_capacity"]
    coefficient = 55 * comb(p["m"], 11) - p["completion_premium"]
    raw = (
        records * coefficient
        - 55 * comb(p["n"], 11)
        - 55 * p["kernel_capacity"]
        - p["rank_nine_marks"]
    )
    require(demand == p["required_component_incidence"], "demand")
    require(gap == p["gap"] and gap > 0, "gap")
    require(coefficient == p["record_coefficient_cross"] and coefficient > 0, "coefficient")
    require(raw == p["floor_record_raw_cross"] and raw > 0, "raw")
    require(raw // 55 == gap - 1 and raw % 55 == 43, "floor orientation")
    print(
        "RATE_HALF_MCA_RANK11_K41_SHARP_ISOLATED_PAYMENT_AUDIT_PASS "
        f"demand={demand} gap={gap} floor_remainder={raw % 55}"
    )


if __name__ == "__main__":
    main()
