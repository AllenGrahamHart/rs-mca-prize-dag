#!/usr/bin/env python3
"""Contract check for the aligned unramified moving-swap exclusion."""

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
require("moving-moving" in statement and "swapped" in statement, "scope")
require("degree-26" in statement and "eight distinct `p`" in statement,
        "finite ledgers")
require("rank(M)<=2" in proof and "K_2 K_0-K_1^2" in proof,
        "determinant-conic implication")
require("other five" in contract, "nonclaim")
require(NODE.name in dag, "DAG registration")

print("KB_C2_112_ALIGNED_POSITIVE_UNRAMIFIED_MOVING_SWAP_CONTRACT_PASS")
