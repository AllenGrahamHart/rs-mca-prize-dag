#!/usr/bin/env python3
"""Verify the weighted odd-prefix collision identity and DAG contract."""

from __future__ import annotations

import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f2_admissible_weighted_prefix_l2_identity"
PARENT = "f2_admissible_direct_sum_grs_reduction"
CONSUMER = "f2_conditional_close"


def element_of_order(p: int, order: int) -> int:
    for candidate in range(2, p):
        omega = pow(candidate, (p - 1) // order, p)
        if pow(omega, order, p) == 1 and pow(omega, order // 2, p) != 1:
            return omega
    raise AssertionError("no element of requested order")


def check_row(p: int, s: int, r: int) -> tuple[int, int]:
    assert (p - 1) % (2 * s) == 0
    omega = element_of_order(p, 2 * s)
    columns = [
        tuple(pow(omega, exponent * (2 * j - 1), p) for j in range(1, r + 1))
        for exponent in range(s)
    ]

    fibers: Counter[tuple[int, ...]] = Counter()
    for mask in range(1 << s):
        value = tuple(
            sum(columns[index][j] for index in range(s) if mask >> index & 1) % p
            for j in range(r)
        )
        fibers[value] += 1
    collisions = sum(count * count for count in fibers.values())

    mass = Fraction(0)
    kernel_words = 0
    for eps in itertools.product((-1, 0, 1), repeat=s):
        if all(sum(eps[index] * columns[index][j] for index in range(s)) % p == 0 for j in range(r)):
            weight = sum(value != 0 for value in eps)
            mass += Fraction(1, 1 << weight)
            kernel_words += 1
    assert collisions == (1 << s) * mass
    assert mass >= 1
    assert mass >= Fraction(1 << s, p**r)
    return collisions, kernel_words


def main() -> None:
    rows = [
        check_row(17, 8, 1),
        check_row(17, 8, 2),
        check_row(17, 8, 3),
        check_row(97, 8, 2),
    ]

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARENT]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    print(
        "F2_ADMISSIBLE_WEIGHTED_PREFIX_L2_IDENTITY_PASS "
        f"rows={len(rows)} collisions={sum(row[0] for row in rows)} "
        f"kernel_words={sum(row[1] for row in rows)} dag=2/2"
    )


if __name__ == "__main__":
    main()
