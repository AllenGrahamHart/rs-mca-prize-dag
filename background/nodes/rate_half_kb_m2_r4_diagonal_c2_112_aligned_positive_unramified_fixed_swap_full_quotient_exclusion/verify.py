#!/usr/bin/env python3
"""Contract check for the fixed-swap full-quotient exclusion."""

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
require("degree-333" in statement and "one quadratic-field" in statement,
        "direct ledger")
require("`2`, `1`, and `1`" in statement and "nine distinct" in statement,
        "off-common ledger")
require("q-slice is not empty" in contract, "scope correction")
require("fixed-mixed" in contract, "nonclaim")
require(NODE.name in dag, "DAG registration")

print("KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_SWAP_CONTRACT_PASS")
