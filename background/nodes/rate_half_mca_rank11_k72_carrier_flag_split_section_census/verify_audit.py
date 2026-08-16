#!/usr/bin/env python3
"""Independent replay of the K'=72 flat-coupled payment."""

from __future__ import annotations

import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
EXPECTED_SHA256 = "25f9b08e71c86c8168a8352b574bbac10395e15c6dee16e0645e7cadb4861f6a"


raw = CONTRACT.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
data = json.loads(raw)
row = data["row"]
want = data["expected"]
m = row["m"]
n = row["outside_points"]


def lower(d: int) -> int:
    terms = [comb(36, d)]
    terms.extend(comb(36, d - j) * comb(n, j - 1) * 31 // j for j in range(1, d))
    return sum(terms)


c4 = 31 * comb(n, 3) // 4
assert c4 == want["top4"]
c5 = (31 * comb(n, 4) - (n - 34) * c4) // 5
assert c5 == want["top5_coupled"]

s4 = comb(m - 4, 7)
s5 = comb(m - 5, 6)
assert 7 * s4 == (m - 4) * s5
assert 21 * s4 - 15 * ((n - 34 + 4) // 5) * s5 == 195 * s5

i4 = (lower(4) + c4) * s4
i5 = (lower(5) + c5) * s5
assert (i4, i5) == (want["I4"], want["I5"])
weighted = 21 * i4 + 15 * i5
assert weighted == want["weighted"]
assert want["required"] - weighted == want["margin"] > 0

# The independent support caps miss the target, while the coupling clears it.
plain5 = 31 * comb(n, 4) // 5
uncoupled = 21 * i4 + 15 * (lower(5) + plain5) * s5
assert uncoupled > want["required"] > weighted

print(json.dumps({
    "contract_sha256": EXPECTED_SHA256,
    "independent_checks": 10,
    "uncoupled": uncoupled,
    "coupled": weighted,
    "margin": want["margin"],
}, sort_keys=True))
