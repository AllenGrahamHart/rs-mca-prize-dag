#!/usr/bin/env python3
"""Independent arithmetic audit of the pairwise carrier atlas."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
EXPECTED_SHA256 = "18a8f0af39e118d2d8c4554b03b142c57f6f01ea9db8f1b43d4ea570e85fdab9"
raw = CONTRACT.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
data = json.loads(raw)

checks = 0
for control in data["controls"]:
    M2, M3, Md, d = (control[key] for key in ("M2", "M3", "Md", "d"))
    b2 = M2 + 1
    r3 = M3 - M2 + 1
    rd = Md - M2 + d - 2
    assert len(control["rows"]) == min(r3, Md - M2) + 1
    for t, union, dimension in control["rows"]:
        assert union == b2 + r3 + rd - t
        assert dimension == (10 - d if t == 0 else 11 - d)
        checks += 2

print(json.dumps({
    "contract_sha256": EXPECTED_SHA256,
    "independent_checks": checks,
}, sort_keys=True))
