#!/usr/bin/env python3
"""Verify the cubic source-facet independence contradiction."""

from itertools import combinations
from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("independent five-set" in statement, "contradiction")
    require("D_3(y)-D_3(z)" in proof, "cubic incidence")

    components = [
        [{0, 1}, {2, 3}, {4, 5}],
        [{6, 7}, {8, 9}, {10, 11}],
    ]
    edges = set()
    for parts in components:
        for left_index in range(3):
            for right_index in range(left_index + 1, 3):
                for left in parts[left_index]:
                    for right in parts[right_index]:
                        edges.add(frozenset((left, right)))
    require(len(edges) == 24, "two K222 edge count")

    maximum = 0
    for size in range(13):
        for subset in combinations(range(12), size):
            chosen = set(subset)
            if all(not edge <= chosen for edge in edges):
                maximum = max(maximum, size)
    require(maximum == 4, "independence number")
    require(all(any(edge <= set(subset) for edge in edges)
                for subset in combinations(range(12), 5)),
            "no independent five-set")
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_DEGREE3_SOURCE_FACET_EXCLUSION_PASS")


if __name__ == "__main__":
    main()
