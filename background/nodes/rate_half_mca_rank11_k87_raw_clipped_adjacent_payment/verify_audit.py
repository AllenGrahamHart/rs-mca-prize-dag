#!/usr/bin/env python3
"""Independent exact-integer and finite-coverage audit for K'=87."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent


def arithmetic_sum(first: int, last: int) -> int:
    terms = last - first + 1
    return terms * (first + last) // 2


def main() -> None:
    data = json.loads((HERE / "source_contract.json").read_text())
    p, row, frontier = data["parameters"], data["row"], data["frontier"]
    floor = row["record_floor"]
    numerator = (
        floor * 55 * comb(p["m"], 11)
        - 55 * comb(p["n"], 11)
        - 55 * row["kernel_capacity"]
        - row["rank_nine_marks"]
        - 1
    )
    ceiling, remainder = divmod(numerator, floor)
    assert (ceiling, remainder) == (
        frontier["safe_premium_ceiling"],
        row["ceiling_remainder"],
    )
    assert (
        frontier["premium_ceiling_margin"]
        == ceiling - frontier["completion_premium"]
        > 0
    )

    full = (row["rank_nine_marks"] + floor * frontier["completion_premium"]) // 55
    total = full + row["kernel_capacity"]
    demand = floor * comb(p["m"], 11) - comb(p["n"], 11)
    assert (full, total, demand, demand - total) == (
        row["full_rank_capacity"],
        row["total_capacity"],
        row["required_component_incidence"],
        row["gap"],
    )
    assert row["gap"] > 0

    coverage = data["coverage"]
    raw = coverage["raw_offsets"]
    clipped = coverage["clipped_residual"]
    all_offset_units = 6084 * arithmetic_sum(1, 76)
    clipped_source_units = 6084 * arithmetic_sum(34, 76)
    assert raw["source_units_per_implementation"] == all_offset_units
    assert clipped["source_units_per_implementation"] == clipped_source_units
    assert raw["raw_rows_per_implementation"] == 7 * all_offset_units
    assert (
        raw["raw_safe_units_per_implementation"]
        + clipped["unsafe_units_per_implementation"]
        == all_offset_units
    )

    ranges = data["clipped_ranges"]
    expected_start = 1
    for item in ranges:
        start, end = item["offsets"]
        assert start == expected_start and start <= end
        expected_start = end + 1
        assert len(item["sha256"]) == 64
    assert expected_start == 44
    assert all(len(item["sha256"]) == 64 for item in data["captures"])
    assert "No K'=88" in data["nonclaim"]

    proof = (HERE / "proof.md").read_text()
    for marker in (
        "Fresh primary",
        "offsets 44 through 76",
        "extension factors",
        "support-disjoint",
        "77,179,660",
    ):
        assert marker in proof
    print(json.dumps({
        "status": "AUDIT_PASS",
        "ceiling_remainder": remainder,
        "gap": row["gap"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
