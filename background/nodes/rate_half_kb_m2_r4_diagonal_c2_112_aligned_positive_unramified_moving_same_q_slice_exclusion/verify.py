#!/usr/bin/env python3
"""Contract check for the aligned unramified moving-same exclusion."""

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
require("same-side" in statement and "degree-272" in statement, "scope")
require("five remaining `w`" in statement, "finite component ledger")
require("degree 86" in proof and "seven distinct `p`" in proof,
        "off-common ledger")
require("other four" in contract, "nonclaim")
require(NODE.name in dag, "DAG registration")

print("KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_SAME_CONTRACT_PASS")
