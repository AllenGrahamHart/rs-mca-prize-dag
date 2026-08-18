#!/usr/bin/env python3
"""Independent audit for the rank-two residual base/plane dichotomy."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
d = json.loads((HERE / "source_contract.json").read_text())

u, b, cutoff = d["universe"], d["residual_roots"], d["base_cutoff"]
assert u > b > cutoff >= 0

# The rational ratio is strictly increasing: its derivative has numerator
# u-b. Check the exact endpoint floor and neighboring endpoint independently.
endpoint = Fraction(u - cutoff, b - cutoff)
previous = Fraction(u - cutoff + 1, b - cutoff + 1)
assert endpoint > previous
maximum = endpoint.numerator // endpoint.denominator
assert maximum == d["maximum_planes"] == 39
assert (u - cutoff) == 1106045
assert (b - cutoff) == d["minimum_nonbase_roots"] == 27733

q, r = divmod(d["bucket_mass"], maximum)
heavy = q + (r != 0)
assert heavy == d["heavy_plane_mass"] == 9965407986
assert d["rank_three_cap"] == 3977322801 < heavy

proof = (HERE / "proof.md").read_text().lower()
assert "nonzero functional" in proof
assert "first-match" in proof
audit = (HERE / "audit.md").read_text().lower()
assert "zero evaluation columns" in audit
assert "not be the same bound" in audit

print(
    "RANK11_BASE_PLANE_AUDIT_PASS "
    f"endpoint={maximum} heavy_mass={heavy} rank={d['forced_correction_rank']}"
)
