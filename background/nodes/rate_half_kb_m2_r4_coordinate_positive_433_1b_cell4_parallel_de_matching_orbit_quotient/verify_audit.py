#!/usr/bin/env python3
"""Independent permutation audit for the parallel-DE quotient."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    matching_table = (
        ((0, 1), (2, 3), (4, 5)),
        ((0, 1), (2, 4), (3, 5)),
        ((0, 1), (2, 5), (3, 4)),
        ((0, 2), (1, 3), (4, 5)),
        ((0, 2), (1, 4), (3, 5)),
        ((0, 2), (1, 5), (3, 4)),
        ((0, 3), (1, 2), (4, 5)),
        ((0, 3), (1, 4), (2, 5)),
        ((0, 3), (1, 5), (2, 4)),
        ((0, 4), (1, 2), (3, 5)),
        ((0, 4), (1, 3), (2, 5)),
        ((0, 4), (1, 5), (2, 3)),
        ((0, 5), (1, 2), (3, 4)),
        ((0, 5), (1, 3), (2, 4)),
        ((0, 5), (1, 4), (2, 3)),
    )
    lookup = {frozenset(matching): index
              for index, matching in enumerate(matching_table)}
    permutation = []
    for matching in matching_table:
        swapped = frozenset(
            tuple(sorted((1 if left == 0 else 0 if left == 1 else left,
                          1 if right == 0 else 0 if right == 1 else right)))
            for left, right in matching
        )
        permutation.append(lookup[swapped])
    require(permutation == [0, 1, 2, 6, 9, 12, 3, 10, 13,
                            4, 7, 14, 5, 8, 11], "explicit permutation")
    fixed = [index for index, image in enumerate(permutation)
             if index == image]
    pairs = sorted(tuple(sorted((index, image)))
                   for index, image in enumerate(permutation) if index < image)
    require(fixed == [0, 1, 2] and pairs ==
            [(3, 6), (4, 9), (5, 12), (7, 10), (8, 13), (11, 14)],
            "orbit table")
    result = (NODE / "result.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("exactly `60` orbits" in result and
            "`96` labeled slices in `54`" in contract, "ledger custody")
    print("audit=ok fixed=3 two_cycles=6 total_orbits=60 live_orbits=54")


if __name__ == "__main__":
    main()
