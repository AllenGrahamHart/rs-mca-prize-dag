#!/usr/bin/env python3
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
node = json.loads((HERE / "node.json").read_text())
pin = json.loads((HERE / "source_pin.json").read_text())

assert node["node"]["status"] == "PROVED"
assert pin["commit"] == "93fba1be3f3299b0ba4708d88715377bbb656e45"
assert pin["git_blob"] == "ba51f8ddac7b6fb84669f9d805fb56f5a9ed0df1"
assert pin["source_lines"] == "58-206"

for n in range(3, 18):
    for m in range(2, n + 1):
        for g in range(m):
            lhs = (n - g) // (m - g)
            assert lhs <= n - m + 1
            assert (n - m + 1) * (m - g) - (n - g) >= 0

statement = (HERE / "statement.md").read_text()
for token in ("n-g+B^MCA", "at most one slope", "D\\P", "No claim"):
    assert token in statement

print("PASS pole-tolerant localization harvest endpoint_inequality_n<=17")
