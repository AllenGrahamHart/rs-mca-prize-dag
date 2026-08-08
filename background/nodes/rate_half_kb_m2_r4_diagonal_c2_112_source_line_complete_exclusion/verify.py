#!/usr/bin/env python3
"""Contract check for complete c2(1,1,2) source-line exclusion."""

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
require("96 labeled" in statement and "12 matching-preserving" in statement,
        "census")
require("12 x 3 = 36" in statement, "literal aligned coverage")
require("F00/M00" in statement, "canonical cell scope")
require("literal-assignment coverage theorem is now PROVED" in statement, "literal premise")
require("Coordinate/source-cover" in statement, "scope")
require("both Prize theorems remain open" in contract, "nonclaim")
require(NODE.name in dag, "DAG registration")

print("KB_C2_112_SOURCE_LINE_COMPLETE_EXCLUSION_CONTRACT_PASS")
