#!/usr/bin/env python3
"""Independent formal-row audit for the cell-9 global kernel."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
PRIME = 2130706433
IOTA = 16711679


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    payload = json.loads(RESULT.read_text())
    b, c, r, t = sp.symbols("b c r t")
    variables = (t, r, c, b)
    for row in payload["rows"]:
        epsilon_1, epsilon_2 = row["epsilon"]
        roots = (1, epsilon_1*IOTA, r, t, epsilon_2*IOTA*r)
        labels = tuple(sp.expand(value**2) for value in roots)
        products = (-1, b, c, b*c, -b*c)
        sums = (0, 1+b, 1+c, b+c, b-c)
        q_values = tuple(sp.expand(root*value)
                         for root, value in zip(roots, sums))
        kernel = [sp.sympify(item["expression"]) for item in row["kernel"]]
        product_rows = [
            [-product, -product*label, -product*label**2,
             1, label, label**2, 0, 0]
            for label, product in zip(labels, products)
        ]
        sum_rows = [
            [q, q*label, q*label**2, 0, 0, 0, label, label**2]
            for label, q in zip(labels, q_values)
        ]
        dots = [
            sp.Poly(sum(a*b for a, b in zip(source, kernel)),
                    *variables, modulus=PRIME)
            for source in [*product_rows, *sum_rows]
        ]
        require(all(value.is_zero for value in dots[:7]),
                "formal row identity")
        require(not any(value.is_zero for value in dots[7:]),
                "nonformal rows mislabeled")

    statement = (NODE / "statement.md").read_text()
    require("excludes no outside record" in statement and
            "final two coordinates" in statement,
            "scope and sign-law markers")
    print("audit=ok cell=9 formal_pairings=28 quotient_pairings=12")


if __name__ == "__main__":
    main()
