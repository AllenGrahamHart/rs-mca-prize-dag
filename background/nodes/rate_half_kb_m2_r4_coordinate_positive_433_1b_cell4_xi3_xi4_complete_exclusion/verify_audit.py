#!/usr/bin/env python3
"""Audit the xi3/xi4 assembly claim discipline."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    manifest = json.loads((NODE / "node.json").read_text())
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    result = (NODE / "result.md").read_text()
    require(manifest["node"]["status"] == "PROVED", "proved manifest")
    require(len(manifest["requires"]) == 10, "ten blocks")
    require("{3,4} x {0,...,14}" in statement, "scope rectangle")
    require("pairwise" in proof and "2*15=30" in proof,
            "disjoint coverage proof")
    require("outside-role labels   30" in result and "raw cases paid       480" in result,
            "printed census")
    print("audit=ok cell=4 xi=3,4 labels=30 raw_cases=480 parents=10")


if __name__ == "__main__":
    main()
