#!/usr/bin/env python3
"""Independent arithmetic and scope audit for weighted root concentration."""

from __future__ import annotations

import json
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "source_contract.json").read_text())
row = data["row"]
pin = data["selection"]
n, k, m, agreement = (row[x] for x in ("n", "k", "anchor_good_universe", "A"))
multiplicity = n - agreement


def affine_slope_cap(d: int) -> int:
    numerator = prod(n - k + i for i in range(1, d + 1))
    denominator = prod(agreement - k + i for i in range(1, d + 1))
    return multiplicity * (numerator // denominator)


r4, r5, r6 = (affine_slope_cap(d) for d in (4, 5, 6))
cutoff = pin["factor_cutoff"]
h = pin["residual_h"]
roots = row["H"] - cutoff + 1
gap = roots - h
factor_classes = m // cutoff
dim2_classes = prod(m - i for i in range(3)) // gap**3
dim3_classes = prod(m - i for i in range(2)) // gap**2
union = factor_classes * r5 + dim2_classes * r4 + dim3_classes * r6
mass = row["budget"] + 1 - row["transverse"] - union
classes = (mass + r6 - 1) // r6
coordinate_mass = ((h + 1) * mass + m - 1) // m

assert (roots, gap, factor_classes, dim2_classes, dim3_classes) == (
    pin["residual_roots"],
    pin["gap"],
    pin["factor_classes"],
    pin["residual_dim2_classes"],
    pin["residual_dim3_classes"],
)
assert union == pin["union_cost"]
assert mass == pin["flag_mass"]
assert classes == pin["minimum_flag_classes"]
assert coordinate_mass == pin["coordinate_mass"]

contract = (HERE / "claim_contract.md").read_text().lower()
assert "base-freeness" in contract
assert "payment of the concentrated" in contract
audit = (HERE / "audit.md").read_text().lower()
assert "weighted by slope mass" in audit
assert "bucket-local" in audit

print(
    "RANK11_WEIGHTED_ROOT_AUDIT_PASS "
    f"T={cutoff} S={h + 1} classes={classes} coordinate_mass={coordinate_mass}"
)
