#!/usr/bin/env python3
"""Evaluate the cell-12 common kernel on every rational boundary point."""

import ast
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
)
BOUNDARY = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell12_tower_boundary_result.json"
)
PRIME = 2130706433
IOTA = 16711679
t, r, c, b = sp.symbols("t r c b")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def rows(point, signs):
    e1, e2 = signs
    rv, tv, bv, cv = (point[name] for name in ("r", "t", "b", "c"))
    roots = (1, e1*IOTA, rv, e2*IOTA*rv, tv)
    labels = tuple(root*root % PRIME for root in roots)
    products = (-1, bv, cv, bv*cv, -bv*cv)
    sums = (0, 1+bv, 1+cv, bv+cv, bv-cv)
    q_values = tuple(root*edge_sum % PRIME
                     for root, edge_sum in zip(roots, sums))
    product_rows = [
        (-product, -product*label, -product*label*label,
         1, label, label*label, 0, 0)
        for product, label in zip(products, labels)
    ]
    sum_rows = [
        (q_value, q_value*label, q_value*label*label,
         0, 0, 0, label, label*label)
        for q_value, label in zip(q_values, labels)
    ]
    return [*product_rows, *sum_rows]


def main():
    ast.parse((NODE / "verify.py").read_text())
    kernel_payload = json.loads(RESULT.read_text())
    kernel = [sp.sympify(item["expression"])
              for item in kernel_payload["rows"][0]["kernel"]]
    boundary = json.loads(BOUNDARY.read_text())
    points = 0
    pairings = 0
    for boundary_row in boundary["rows"]:
        signs = tuple(boundary_row["epsilon"])
        for point in boundary_row["rational_points"]:
            values = {t: point["t"], r: point["r"],
                      c: point["c"], b: point["b"]}
            coordinates = [int(value.subs(values)) % PRIME for value in kernel]
            require(any(coordinates), "zero kernel at boundary point")
            for row in rows(point, signs):
                require(sum(left*right for left, right in
                            zip(row, coordinates)) % PRIME == 0,
                        "boundary row pairing")
                pairings += 1
            points += 1
    statement = (NODE / "statement.md").read_text()
    require("does not itself impose" in statement and
            "outside row" in statement and "does not close" in statement,
            "kernel scope")
    require(points == 8 and pairings == 80, "boundary audit totals")
    print("audit=ok boundary_points=8 row_pairings=80")


if __name__ == "__main__":
    main()
