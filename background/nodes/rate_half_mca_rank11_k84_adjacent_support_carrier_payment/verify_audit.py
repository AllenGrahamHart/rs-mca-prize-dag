#!/usr/bin/env python3
"""Independent exact-integer audit for the K'=84 payment."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent


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
    assert 0 <= remainder < floor
    assert ceiling == frontier["safe_premium_ceiling"]
    assert (
        frontier["premium_ceiling_margin"]
        == ceiling - frontier["completion_premium"]
        > 0
    )

    full = (
        row["rank_nine_marks"]
        + floor * frontier["completion_premium"]
    ) // 55
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
    assert coverage["source_units"] == (
        coverage["ordinary_units"]
        + sum((74 - offset) * 5625 for offset in range(1, 74))
    )
    assert coverage["raw_rows"] == 7 * coverage["source_units"]
    assert coverage["audit_geometry_rows"] >= coverage["primary_geometry_rows"]
    assert all(len(item["sha256"]) == 64 for item in data["captures"])
    proof = (HERE / "proof.md").read_text()
    for marker in (
        "ordinary lane",
        "offset",
        "support sets are disjoint",
        "148",
        "nearest",
    ):
        assert marker in proof
    print(json.dumps({
        "status": "AUDIT_PASS",
        "ceiling_remainder": remainder,
        "gap": row["gap"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
