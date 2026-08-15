#!/usr/bin/env python3
"""Independent audit of the K'=22 integral heavy-owner maxima."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")


def main() -> None:
    data = json.loads(CONTRACT.read_text())
    p = data["parameters"]
    checked = 0
    charts = {}
    for core in range(9, 22):
        petal = 67494 - core
        total = 1048598 - core
        offset = core - 9
        light = total - 8 * (petal - 1)
        charge = comb(petal - 1, 2) + offset * petal
        clean = 8 * light * charge
        assert clean == p["clean_caps"][str(core)]

        heavy_min = petal // 2 + 1
        h = total // heavy_min
        cross = petal * petal // 4
        balanced = comb(total, 2) * (cross + offset * petal) // cross
        collision = comb(h, 2) * (comb(petal - 1, 2) + offset * petal)
        charts[str(core)] = clean + balanced + collision
        assert charts[str(core)] == p["chart_caps"][str(core)]
        checked += 4

    assert max(charts.values()) == p["uniform_chart_cap"]
    assert max(charts, key=charts.get) == str(p["maximizing_core"])
    print(
        "RATE_HALF_MCA_WEIGHTED_SPLIT_PENCIL_INTEGRAL_HEAVY_CAP_AUDIT_PASS "
        f"cores=13 checks={checked} uniform={p['uniform_chart_cap']}"
    )


if __name__ == "__main__":
    main()
