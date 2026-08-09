#!/usr/bin/env python3
"""Independent scope and combinatorial audit for the cell-9 common node."""

import ast
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
SUBSET = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell9_lex_subset_scout_result.json"
)
EXPECTED = {
    (0, 1, 3, 4, 6),
    (0, 1, 3, 5, 6),
    (0, 1, 4, 5, 6),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        yield ((first, second), (rest[0], rest[1]))


def main():
    ast.parse((NODE / "verify.py").read_text())
    cells = []
    for singleton in range(5):
        rest = tuple(index for index in range(5) if index != singleton)
        cells.extend((singleton, matching) for matching in pairings(rest))
    require(cells[9] == (3, ((0, 1), (2, 4))), "cell-9 role assignment")

    payload = json.loads(SUBSET.read_text())
    signs = set(itertools.product((-1, 1), repeat=2))
    for epsilon in signs:
        rows = [row for row in payload["rows"]
                if tuple(row["epsilon"]) == epsilon]
        exact = {
            tuple(row["indices"]) for row in rows
            if all(item["expression"] == "0" for item in row["remainders"])
        }
        require({item for item in exact if len(item) == 5} == EXPECTED,
                "five-relation pattern")
        require(all({0, 1, 6}.issubset(item) and 2 not in item
                    for item in EXPECTED), "common core and K2 redundancy")

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("singleton is `BC+`" in statement and
            "excludes no outside label" in statement and
            "Cell `10`" in contract and "Genus" in contract,
            "scope markers")
    print("audit=ok cell=9 signs=4 exact_five_sets=3 outside_claims=0")


if __name__ == "__main__":
    main()
