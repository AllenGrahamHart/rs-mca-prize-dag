#!/usr/bin/env python3
"""Audit complete role-cell-4 claim discipline."""

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
    frontier = (NODE / "frontier.md").read_text()
    require(manifest["node"]["status"] == "PROVED", "proved manifest")
    require(len(manifest["requires"]) == 4, "rank split plus three suppliers")
    require("rank-at-most-four" in statement and "1680" in statement,
            "complete rank/census statement")
    require("pairwise disjoint" in proof and "105*4*4=1680" in proof,
            "coverage arithmetic")
    require("Source role cell 4 is closed" in frontier
            and "role cell 7" in frontier,
            "bounded frontier")
    print("audit=ok cell=4 complete labels=105 raw_systems=1680 parents=4")


if __name__ == "__main__":
    main()
