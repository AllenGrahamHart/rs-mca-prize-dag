#!/usr/bin/env python3
"""Independent exact-integer and finite-coverage audit for K'=86."""

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
    residual = coverage["best_single_residual"]
    all_offset_units = 5929 * arithmetic_sum(1, 75)
    residual_source_units = 5929 * arithmetic_sum(34, 75)
    assert raw["source_units_per_implementation"] == all_offset_units
    assert residual["source_units_per_implementation"] == residual_source_units
    assert raw["raw_rows_per_implementation"] == 7 * all_offset_units
    assert (
        raw["raw_safe_units_per_implementation"]
        + residual["unsafe_units_per_implementation"]
        == all_offset_units
    )
    assert all(len(item["sha256"]) == 64 for item in data["captures"])
    assert "No K'=87" in data["nonclaim"]
    proof = (HERE / "proof.md").read_text()
    for marker in (
        "ordinary slice",
        "offsets 43 through 75",
        "best-single",
        "does not compose overlapping edges",
        "62,159,220",
    ):
        assert marker in proof
    print(json.dumps({
        "status": "AUDIT_PASS",
        "ceiling_remainder": remainder,
        "gap": row["gap"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
