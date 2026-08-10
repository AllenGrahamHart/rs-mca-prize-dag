#!/usr/bin/env python3
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
node = json.loads((HERE / "node.json").read_text())
pin = json.loads((HERE / "source_pin.json").read_text())

assert node["node"]["status"] == "PROVED"
assert pin["commit"] == "93fba1be3f3299b0ba4708d88715377bbb656e45"
assert pin["git_blob"] == "6b21d6ea937a8a9f85fc7ade6032d73efd4c7222"

n = 2097152
rows = (
    (1116048, 274980728111395087),
    (1116024, 16777215),
)
for m, budget in rows:
    assert n < 2 * m
    assert n <= 2 * (m - 1)
    for c in (2, 3, m // 2, m - 2, m - 1):
        assert 2 <= c < m
        assert c * (m - c + 1) >= n
        assert 2 * (n - c) <= 2 * c * (m - c)
    assert 2 * n < budget

statement = (HERE / "statement.md").read_text()
for token in ("N_C (m-c) <= 2(n-c)", "N_C <= 2c", "4194304", "at most one"):
    assert token in statement

print("PASS coordinate-clone subcritical payment rows=2 test_classes=5 total=4194304")
