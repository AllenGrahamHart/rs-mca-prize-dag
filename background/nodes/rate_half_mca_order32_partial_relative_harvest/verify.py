#!/usr/bin/env python3
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
node = json.loads((HERE / "node.json").read_text())
pin = json.loads((HERE / "source_pin.json").read_text())

assert node["node"]["status"] == "PROVED"
assert pin["commit"] == "93fba1be3f3299b0ba4708d88715377bbb656e45"
assert pin["git_blob"] == "6b21d6ea937a8a9f85fc7ade6032d73efd4c7222"
assert pin["label"] == "thm:partial-relative"

rows = {
    "koalabear": (1116048, 1048576, 2299571, 1083345, 67472, 1015873),
    "mersenne31": (1116024, 1048576, 2299499, 1083320, 67448, 1015872),
}
n = 2097152
for name, (m, k, xi, g31, d, residual) in rows.items():
    assert 3 * m - k + 3 == xi, name
    assert (31 * m - n + 29) // 30 == g31, name
    assert m - k == d, name
    assert g31 - d == residual, name

statement = (HERE / "statement.md").read_text()
for token in ("18 <= degree_in_slope(E) <= 31", "2299571", "2299499", "(S)", "(A)", "(E)"):
    assert token in statement

print("PASS upstream order32 harvest rows=2 degree=[18,31] terminals_open=3")
