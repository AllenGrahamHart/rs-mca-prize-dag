#!/usr/bin/env python3
"""Verify the near-negative q-slice node contract and branch algebra."""

import json
from pathlib import Path

import sympy as sp

from verify_runner import check_hashes


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_negative_reconstruction_factor_gate",
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


statement = (NODE / "statement.md").read_text()
require("- **status:** PROVED" in statement, "status")
require("including the forced-ramified `w=0` branch" in statement, "ramification")
require("(xi*d)^2=1" in statement, "constant gate")

dag = json.loads((ROOT / "dag.json").read_text())
nodes = {node["id"]: node for node in dag["nodes"]}
require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
         for edge in dag["edges"]}
require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
        "dependencies")
require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

c, d = sp.symbols("c d")
p = c * d - 2 * c - 2 * d + 1
q = 2 * c * d - c - d + 2
b = -q / p
require(sp.factor(d * q + p) == (2 * c - 1) * (d - 1) * (d + 1),
        "other-xi plus branch")
minus = 2 * c * d**2 - 2 * c * d + 2 * c - d**2 + 4 * d - 1
require(sp.expand(d * q - p - minus) == 0, "other-xi minus branch")
c_value = (d**2 - 4 * d + 1) / (2 * (d**2 - d + 1))
require(sp.cancel(minus.subs(c, c_value)) == 0, "minus parametrization")
require(sp.cancel(b.subs(c, c_value) + 1 / d) == 0, "bd=-1")

# The only potentially unproved minor factor, cd+1, becomes a collision.
require(sp.cancel((c * d + 1).subs(d, -sp.Rational(1, 2)).subs(c, 2)) == 0,
        "xi=a minor collision")
require(sp.cancel((c * d + 1).subs(d, -2).subs(c, sp.Rational(1, 2))) == 0,
        "xi=tau-a minor collision")
require(sp.cancel(c_value + 1 / d) != 0, "nonidentity sanity")

check_hashes()
print("KB_C2_112_NEAR_NEGATIVE_CONTRACT_PASS branches=3 templates=2")
