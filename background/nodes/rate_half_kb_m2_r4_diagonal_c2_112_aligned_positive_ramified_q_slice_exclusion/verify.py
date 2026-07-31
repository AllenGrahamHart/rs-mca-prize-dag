#!/usr/bin/env python3
"""Contract check for the aligned positive ramified exclusion."""

from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


statement = (NODE / "statement.md").read_text()
proof = (NODE / "proof.md").read_text()
contract = (NODE / "claim_contract.md").read_text()
dag = (ROOT / "dag.json").read_text()

require("**status:** PROVED" in statement, "status")
require("forced source\n  ramification `w=0`" in statement, "ramified scope")
require("fixed-moving" in statement and "moving-moving" in statement, "templates")
require(all(name in statement for name in ("`same`", "`swap`", "`mixed`")),
        "allocations")
require("basis of" in proof and "is `<1>`" in proof, "unit bases")
require("near-aligned homogeneous deletion" in contract, "nonclaim")
require(NODE.name in dag, "DAG registration")

print("KB_C2_112_ALIGNED_POSITIVE_RAMIFIED_CONTRACT_PASS cases=6")
