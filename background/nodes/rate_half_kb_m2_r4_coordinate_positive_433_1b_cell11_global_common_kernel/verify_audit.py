#!/usr/bin/env python3
"""Independent algebra audit for the cell-11 common kernel."""

import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell11_compact_kernel_result.json"
P = 2130706433
IOTA = 16711679
t, r, c, b = sp.symbols("t r c b")
VARIABLES = (t, r, c, b)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    payload = json.loads(RESULT.read_text())
    signatures = set()
    mutated_failure = False
    formal_rows = 0
    for row in payload["rows"]:
        epsilon_1, epsilon_2 = row["epsilon"]
        roots = (1, r, epsilon_2 * IOTA * r, t, epsilon_1 * IOTA)
        labels = tuple(sp.expand(value**2) for value in roots)
        products = (-1, b, c, b*c, -b*c)
        sums = (0, 1+b, 1+c, b+c, b-c)
        q_values = tuple(
            sp.expand(root * edge_sum)
            for root, edge_sum in zip(roots, sums)
        )
        values = [sp.sympify(item["expression"]) for item in row["kernel"]]
        signatures.add(tuple(item["sha256"] for item in row["kernel"]))
        product_rows = [
            [-product, -product * label, -product * label**2,
             1, label, label**2, 0, 0]
            for label, product in zip(labels, products)
        ]
        sum_rows = [
            [q_value, q_value * label, q_value * label**2,
             0, 0, 0, label, label**2]
            for label, q_value in zip(labels, q_values)
        ]
        identities = []
        for source_row in [*product_rows, *sum_rows]:
            dot = sum(left * right for left, right in zip(source_row, values))
            identities.append(sp.Poly(dot, *VARIABLES, modulus=P).is_zero)
        require(identities == [True] * 7 + [False] * 3,
                "formal identity reconstruction")
        formal_rows += sum(identities)
        if (epsilon_1, epsilon_2) == (-1, -1):
            changed = list(values)
            changed[0] += 1
            dot = sum(left * right
                      for left, right in zip(product_rows[0], changed))
            mutated_failure = not sp.Poly(
                dot, *VARIABLES, modulus=P
            ).is_zero

    statement = (NODE / "statement.md").read_text()
    require(len(signatures) == 1 and formal_rows == 28,
            "sign-independent formal ledger")
    require(mutated_failure, "kernel mutation test")
    require("outside row" in statement and "does not close" in statement,
            "kernel scope")
    print("audit=ok cell=11 formal_rows=28 mutation=1/1")


if __name__ == "__main__":
    main()
