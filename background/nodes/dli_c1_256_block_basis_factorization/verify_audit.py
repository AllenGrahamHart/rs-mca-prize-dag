#!/usr/bin/env python3
"""Audit scope for the DLI C1 256-block factorization."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "dli_c1_256_block_basis_factorization"
CONSUMER = "dli_c1r3_gated_envelope_bound"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    text = "\n".join(
        (NODE / name).read_text()
        for name in ("statement.md", "proof.md", "claim_contract.md", "audit.md")
    ).lower()
    for marker in ("256 blocks", "exact iid", "companion orbit",
                   "not prove joint independence", "not joint independence"):
        require(marker in text, f"missing marker {marker}")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "node status")
    require(any(edge == {"from": NODE_ID, "to": CONSUMER, "kind": "ev"}
                for edge in dag["edges"]), "consumer edge")
    print("DLI C1 256-block factorization audit verified")


if __name__ == "__main__":
    main()
