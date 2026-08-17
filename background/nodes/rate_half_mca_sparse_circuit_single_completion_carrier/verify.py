#!/usr/bin/env python3
"""Verify the single-completion carrier arithmetic contract."""

import json
from pathlib import Path


data = json.loads(Path(__file__).with_name("source_contract.json").read_text())
assert data["schema"] == "rate-half-mca-single-completion-carrier-v1"
assert data["formula"] == {"union": "M+c-1", "dimension": "11-c"}
for row in data["controls"]:
    assert row["union"] == row["M"] + row["c"] - 1
    assert row["dimension"] == 11 - row["c"]
print(json.dumps({"controls": len(data["controls"]), "status": "PASS"}, sort_keys=True))
