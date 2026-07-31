#!/usr/bin/env python3
"""Contract check for the fixed-mixed full-quotient exclusion."""

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
require("degree-338" in statement and "four quadratic-field" in statement,
        "degree-five ledger")
require("degree 116" in statement and "twelve remaining" in statement,
        "linear ledger")
require("`5`, `4`, and `1`" in statement and "All 20" in statement,
        "off-common ledger")
require("q-slice is not empty" in contract, "scope correction")
require("packet assembly" in contract and "Prize theorem" in contract,
        "nonclaim")
require(NODE.name in dag, "DAG registration")

print("KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_FIXED_MIXED_CONTRACT_PASS")
