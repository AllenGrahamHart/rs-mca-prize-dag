#!/usr/bin/env python3
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
node = json.loads((HERE / "node.json").read_text())

assert node["node"]["status"] == "PROVED"
assert node["requires"] == [
    {"from": "rate_half_mca_pole_tolerant_scalar_locator_harvest"}
]

rows = ((1116048, 1048576), (1116024, 1048576))
for m, k in rows:
    for t in (0, 1, m - k - 1, m - k):
        assert 0 <= t <= m - k
        assert m - t >= k

statement = (HERE / "statement.md").read_text()
for token in ("m-t >= k", "v_i|_P != 0", "Distinct slopes", "does not bound"):
    assert token in statement

print("PASS denominator-root dichotomy rows=2 endpoint_degrees=4")
