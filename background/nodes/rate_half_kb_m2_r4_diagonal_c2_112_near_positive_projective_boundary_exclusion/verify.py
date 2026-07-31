#!/usr/bin/env python3
"""Contract check for the near-positive projective exclusion."""

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
require("q_hom=Y(T-dY)" in statement, "homogeneous locator")
require("All seven exhaustive" in statement, "seven shards")
require("complete near-aligned source-line branch is\nempty" in statement,
        "branch consequence")
require("coeff_(T^4)" in proof, "infinity audit")
require("aligned positive unramified deletion" in contract, "nonclaim")
require(NODE.name in dag, "DAG registration")

print("KB_C2_112_NEAR_POSITIVE_PROJECTIVE_CONTRACT_PASS shards=7")
