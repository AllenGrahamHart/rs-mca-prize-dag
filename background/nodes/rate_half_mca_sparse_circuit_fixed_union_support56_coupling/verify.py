#!/usr/bin/env python3
"""Verify the fixed-union support-5/6 weighted specialization."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


def cap(K: int, m: int, u: int, g: int, w5: int, w6: int) -> int:
    residual, outside = K - u - g, m - u
    assert g >= 6 and residual >= 0 and outside >= residual + 4
    total = 0
    for inside in range(4):
        choices = comb(u, inside)
        low = choices * residual * comb(outside, 4 - inside) // (5 - inside)
        rhs = choices * residual * comb(outside, 5 - inside)
        coefficient = outside - residual - 4 + inside
        slope = (6 - inside) * w5 - coefficient * w6
        total += (w6 * rhs + max(slope, 0) * low) // (6 - inside)
    total += w5 * (comb(u, 4) * residual + comb(u, 5))
    total += w6 * (
        comb(u, 4) * residual * outside // 2
        + comb(u, 5) * residual
        + comb(u, 6)
    )
    return total


data = json.loads(Path(__file__).with_name("source_contract.json").read_text())
assert data["schema"] == "rate-half-mca-fixed-union-support56-coupling-v1"
assert data["hypotheses"] == {
    "minimum_dimension": 6,
    "residual": "R=K-u-g>=0",
    "outside_size": "N=m-u>=R+4",
}
row = data["specialization"]
m = row["m"]
w5 = row["deficit5"] * comb(m - 5, 6)
w6 = row["deficit6"] * comb(m - 6, 5)
value = cap(row["K"], m, row["u"], row["g"], w5, w6)
assert value == int(row["expected_weighted_cap"])
print(json.dumps({"residual": 48, "weighted_cap": str(value)}, sort_keys=True))
