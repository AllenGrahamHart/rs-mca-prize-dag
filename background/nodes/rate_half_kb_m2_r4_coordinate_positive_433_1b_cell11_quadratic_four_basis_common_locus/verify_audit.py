#!/usr/bin/env python3
"""Independent arithmetic audit of the cell-11 boundary census."""

import ast
import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
BOUNDARY = ROOT / "experiments/prize_resolution" / (
    "rate_half_kb_positive_433_1b_cell11_tower_boundary_result.json"
)
PRIME = 2130706433
b = sp.symbols("b")


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
    require(cells[11] == (3, ((0, 4), (1, 2))),
            "cell-11 role reconstruction")

    payload = json.loads(BOUNDARY.read_text())
    actual = set()
    nonsplit = 0
    for row in payload["rows"]:
        key = (*row["epsilon"], row["boundary"])
        require(key not in actual, "duplicate sign/boundary row")
        actual.add(key)
        require(len(row["t_factors"]) == 1 and
                row["t_factors"][0]["degree"] == 1 and
                len(row["b_factors"]) == 1 and
                row["b_factors"][0]["degree"] == 2 and
                row["rational_points"] == [], "boundary shape")
        eliminant = sp.Poly(
            sp.sympify(row["b_factors"][0]["expression"]),
            b, modulus=PRIME,
        )
        discriminant = int(sp.discriminant(eliminant.as_expr(), b)) % PRIME
        require(discriminant and
                pow(discriminant, (PRIME - 1) // 2, PRIME) == PRIME - 1,
                "quadratic boundary eliminant splits")
        nonsplit += 1

    expected = set(itertools.product(
        (-1, 1), (-1, 1), ("b_leading", "c_leading")
    ))
    require(actual == expected and nonsplit == 8, "boundary totals")
    statement = (NODE / "statement.md").read_text()
    require("BC+" in statement and
            "outside record" in statement and
            "does not close" in statement, "scope and role audit")
    print("audit=ok cell=11 boundary_points=0 nonsplit_fibers=8")


if __name__ == "__main__":
    main()
