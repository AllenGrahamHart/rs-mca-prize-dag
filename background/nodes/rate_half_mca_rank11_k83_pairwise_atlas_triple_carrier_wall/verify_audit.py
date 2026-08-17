#!/usr/bin/env python3
"""Independent static audit of the narrowed K'=83 cell contract."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
EXPECTED_SHA256 = "06a01a521241157263a72b3d90539bfbbc74c9a367603136efb173165c363187"

raw = CONTRACT.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
data = json.loads(raw)
assert data["scope"] == "single exact cell; not a complete K'=83 frontier maximum"
assert data["parameters"]["q"] == 73
cell = data["active_cell"]
assert cell["completion_maxima"] == [
    73 - defect for defect in cell["defects"]
]
assert cell["pairwise_charges"] == [[29, 6], [29, 6]]
expected_margin = cell["safe_premium_ceiling"] - cell["pairwise_maximum"]
assert cell["pairwise_margin"] == expected_margin < 0

rows = data["forced_intersection_rows"]
assert [row["overlap45"] for row in rows] == [0, 1, 2, 3]
assert [row["triple_union"] for row in rows] == [32, 31, 30, 29]
for row in rows:
    assert row["triple_union"] == 32 - row["overlap45"]
    assert row["triple_dimension"] == 4
    assert row["maximum"] == cell["pairwise_maximum"]
    assert row["margin"] == expected_margin

print(json.dumps({
    "contract_sha256": EXPECTED_SHA256,
    "independent_checks": 7 + 4 * len(rows),
    "scope": "single-cell",
}, sort_keys=True))
