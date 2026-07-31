#!/usr/bin/env python3
"""Contract check for the aligned unramified moving-mixed exclusion."""

from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


statement = (NODE / "statement.md").read_text(encoding="ascii")
proof = (NODE / "proof.md").read_text(encoding="ascii")
contract = (NODE / "claim_contract.md").read_text(encoding="ascii")
dag = (ROOT / "dag.json").read_text(encoding="ascii")

require("**status:** PROVED" in statement, "status")
require("degree 1224" in statement and "degrees `3,3,7,7`" in statement,
        "direct ledger")
require("q-slice itself is not empty" in statement, "scope correction")
require("`3`, `4`," in proof and "six `(p,t)`" in proof,
        "off-common ledger")
require("full colored quotient identities" in contract, "claim")
require("fixed-moving" in contract, "nonclaim")
require(NODE.name in dag, "DAG registration")

print("KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_MIXED_CONTRACT_PASS")
