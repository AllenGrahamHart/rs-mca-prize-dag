#!/usr/bin/env python3
"""Check the Newton reformulation of the order-one reciprocal equations."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_order_one_newton_reciprocal_reduction"
DEPENDENCY = "l1_mersenne_hnf_order_one_frobenius_gate"
CONSUMER = "l1_mixed_petal_amplification"


def elementary(values: list[int], p: int) -> list[int]:
    out = [1] + [0] * len(values)
    for value in values:
        for degree in range(len(values), 0, -1):
            out[degree] = (out[degree] + value * out[degree - 1]) % p
    return out


def newton(values: list[int], p: int) -> list[int]:
    size = len(values)
    powers = [0] + [sum(pow(value, degree, p) for value in values) % p for degree in range(1, size + 1)]
    out = [1]
    for degree in range(1, size + 1):
        numerator = sum(
            (-1) ** (power - 1) * out[degree - power] * powers[power]
            for power in range(1, degree + 1)
        )
        out.append(numerator * pow(degree, -1, p) % p)
    return out


def check_case(p: int, h: int, m: int) -> int:
    size = h - 1
    roots = list(range(2, size + 2))
    y = [pow(root, m, p) for root in roots]
    inverse_y = [pow(value, -1, p) for value in y]
    star_y = list(reversed(inverse_y))

    e = elementary(y, p)
    e_inverse = elementary(inverse_y, p)
    e_star = elementary(star_y, p)
    assert e == newton(y, p)
    assert e_inverse == newton(inverse_y, p)
    assert e_star == newton(star_y, p)

    q = [(-1) ** degree * e[degree] % p for degree in range(size + 1)]
    q_star = [(-1) ** degree * e_star[degree] % p for degree in range(size + 1)]
    constant = q[-1]
    for degree in range(1, size + 1):
        assert e_star[degree] == e_inverse[degree]
        assert constant * q_star[degree] % p == q[size - degree]
    assert constant * q_star[-1] % p == 1

    mutated = star_y[:]
    mutated[0] = mutated[0] * 2 % p
    assert elementary(mutated, p) != e_inverse
    return 4 + size + 2


def main() -> None:
    checks = check_case(101, 7, 8) + check_case(127, 15, 16)

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == statuses[DEPENDENCY] == "PROVED"
    assert statuses[CONSUMER] == "TARGET"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(NRR1)", "(NRR2)", "(NRR3)", "(NRR4)", "8,16,24", "16,32,48"):
        assert anchor in statement
    for anchor in ("e_(H-j)(y)", "differ by `2j`", "monic reciprocal polynomial"):
        assert anchor in proof

    print(f"L1_MERSENNE_HNF_ORDER_ONE_NEWTON_RECIPROCAL_REDUCTION_PASS checks={checks}")


if __name__ == "__main__":
    main()
