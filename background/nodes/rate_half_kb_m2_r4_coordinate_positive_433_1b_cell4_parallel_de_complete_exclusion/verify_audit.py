#!/usr/bin/env python3
"""Audit the parallel-DE assembly claim discipline."""

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
    require(len(manifest["requires"]) == 7, "seven blocks")
    require("{0,1,2} x {0,...,14}" in statement, "scope rectangle")
    require("pairwise disjoint" in proof and "3*15=45" in proof,
            "disjoint coverage proof")
    require("parallel-DE labels    45" in result and "raw cases paid       720" in result,
            "printed census")
    print("audit=ok cell=4 parallel_DE labels=45 raw_cases=720 parents=7")


if __name__ == "__main__":
    main()
