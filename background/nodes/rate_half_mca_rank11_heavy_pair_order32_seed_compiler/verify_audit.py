#!/usr/bin/env python3
"""Independent audit of the rank-eleven heavy-pair seed compiler."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "378cf4a4c17f7fffc4ba9863d0dabef5fd85f9831dcde0481ed193ba26aa6b6a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def falling_ratio_floor(top: int, bottom: int, order: int) -> int:
    numerator = 1
    denominator = 1
    for offset in range(order):
        numerator *= top - offset
        denominator *= bottom - offset
    return numerator // denominator


def audit(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "object")
    row = data.get("official")
    require(isinstance(row, dict), "official")
    n, dimension, agreement, w, budget = (
        row.get(key) for key in ("n", "K", "m", "w", "B_star")
    )
    require(
        (n, dimension, agreement, w, budget)
        == (2097152, 1048576, 1116048, 67472, 274980728111395087),
        "base constants",
    )
    top = n - dimension + 10
    bottom = w - row.get("low_margin_maximum") + 10
    pair_cap = falling_ratio_floor(top, bottom, 10)
    require(pair_cap == row.get("distinct_pair_cap") == 869784434119, "pair cap")
    require(row.get("singleton_record_cap") == pair_cap, "singleton")
    require(
        row.get("selected_heavy_pair_types_maximum")
        == row.get("component_span_dimension_maximum") + 1
        == 11,
        "basis size",
    )
    require(
        row.get("selected_seed_records_maximum")
        == 2 * row.get("selected_heavy_pair_types_maximum")
        == 22
        < row.get("order32_size")
        == 32,
        "seed size",
    )
    fixed = n - agreement + 1
    heavy = row.get("shortened_heavy_pair_type_cap") * fixed
    low = pair_cap + heavy
    total = row.get("near_charge") + row.get("high_margin_cap") + low
    require(fixed == row.get("pair_record_cap"), "fixed cap")
    require(heavy == row.get("heavy_record_cap"), "heavy cap")
    require(low == row.get("low_margin_cap"), "low cap")
    require(total == row.get("total_cap_if_large_heavy_core") < budget, "total")
    require(budget - total == row.get("budget_slack_if_large_heavy_core"), "slack")
    unsafe_low = budget + 1 - row.get("near_charge") - row.get("high_margin_cap")
    require(unsafe_low == row.get("unsafe_low_record_minimum") > pair_cap, "unsafe low")
    require(
        dimension - row.get("common_core_codimension_maximum")
        == row.get("common_core_size_threshold"),
        "core",
    )
    return {"pair_cap": pair_cap, "total": total, "unsafe_low": unsafe_low}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = audit(data)
    controls = []
    for key, value in (
        ("singleton_record_cap", 869784434118),
        ("selected_seed_records_maximum", 24),
        ("total_cap_if_large_heavy_core", 274791086998147431),
        ("common_core_size_threshold", 1043653),
    ):
        altered = copy.deepcopy(data)
        altered["official"][key] = value
        try:
            audit(altered)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "audit controls")
    print(
        "RATE_HALF_MCA_RANK11_HEAVY_PAIR_ORDER32_SEED_COMPILER_AUDIT_PASS "
        f"Q={result['pair_cap']} total={result['total']} low_min={result['unsafe_low']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
