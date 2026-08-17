#!/usr/bin/env python3
"""Independent arithmetic audit of the flat-circuit coupling theorem."""

from __future__ import annotations

import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
EXPECTED_SHA256 = "9d93ab795e311ec5789fe77494d9fd26ed8b17d5f5cf88bbbc1e04de112317e5"


raw = CONTRACT.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
data = json.loads(raw)

checks = 0
for row in data["uniform_rank4_rows"]:
    # U_{4,N}: every five-set is a circuit, and the whole ground set is the
    # unique rank-four flat.  These rows attain the theorem exactly.
    assert row["B"] == row["N"] - 1
    assert row["C4"] == 0
    assert row["C5"] == comb(row["N"], 5)
    assert 5 * row["C5"] == (row["B"] - 3) * comb(row["N"], 4)
    checks += 4

row = data["uniform_rank5_row"]
assert row["B"] == 3
assert row["C4"] == row["C5"] == 0
assert (row["B"] - 3) * comb(row["N"], 4) == 0
checks += 3

# Coefficient mutations fail on the sharp U_{4,7} control.
sharp = data["uniform_rank4_rows"][1]
left = 5 * sharp["C5"]
assert left > (sharp["B"] - 4) * comb(sharp["N"], 4)
assert left == (sharp["B"] - 3) * comb(sharp["N"], 4)
checks += 2

print(json.dumps({
    "contract_sha256": EXPECTED_SHA256,
    "independent_checks": checks,
    "sharp_rows": len(data["uniform_rank4_rows"]),
}, sort_keys=True))
