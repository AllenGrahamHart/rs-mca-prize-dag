#!/usr/bin/env python3
"""Verify the generic weighted collision floor and DAG contract."""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f2_weighted_kernel_collision_floor"
CONSUMER = "f2_conditional_close"


def rank_mod(rows: list[list[int]], p: int) -> int:
    work = [[value % p for value in row] for row in rows]
    if not work:
        return 0
    rank = 0
    for col in range(len(work[0])):
        pivot = next((i for i in range(rank, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][col], -1, p)
        work[rank] = [(inverse * value) % p for value in work[rank]]
        for i in range(len(work)):
            if i != rank and work[i][col]:
                factor = work[i][col]
                work[i] = [
                    (left - factor * right) % p
                    for left, right in zip(work[i], work[rank])
                ]
        rank += 1
        if rank == len(work):
            break
    return rank


def independent_rows(rows: list[list[int]], p: int) -> list[list[int]]:
    basis = []
    for row in rows:
        if rank_mod(basis + [row], p) > len(basis):
            basis.append(row)
    return basis


def syndrome(rows: list[list[int]], vector: tuple[int, ...], p: int) -> tuple[int, ...]:
    return tuple(sum(a * b for a, b in zip(row, vector)) % p for row in rows)


def check_matrix(p: int, m: int, rows: list[list[int]]) -> tuple[int, int]:
    fibers: Counter[tuple[int, ...]] = Counter()
    for bits in itertools.product((0, 1), repeat=m):
        fibers[syndrome(rows, bits, p)] += 1
    collisions = sum(count * count for count in fibers.values())

    mass = Fraction(0)
    words = 0
    for eps in itertools.product((-1, 0, 1), repeat=m):
        if not any(syndrome(rows, eps, p)):
            mass += Fraction(1, 1 << sum(value != 0 for value in eps))
            words += 1
    d = rank_mod(rows, p)
    assert collisions == (1 << m) * mass
    assert mass >= 1
    assert mass >= Fraction(1 << m, p**d)
    basis = independent_rows(rows, p)
    fourier = 0.0
    for u in itertools.product(range(p), repeat=d):
        term = 1.0
        for col in range(m):
            phase = sum(u[i] * basis[i][col] for i in range(d)) % p
            term *= 1.0 + math.cos(2.0 * math.pi * phase / p)
        fourier += term
    fourier /= p**d
    assert abs(fourier - float(mass)) < 1e-9
    return collisions, words


def main() -> None:
    cases = [
        (3, 4, []),
        (3, 5, [[1, 0, 1, 2, 1], [0, 1, 1, 1, 2]]),
        (5, 6, [[1, 2, 3, 4, 0, 1], [2, 4, 1, 3, 0, 2], [0, 1, 0, 1, 0, 1]]),
        (7, 6, [[1, 1, 1, 1, 1, 1], [0, 1, 2, 3, 4, 5]]),
    ]
    counts = [check_matrix(*case) for case in cases]

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges
    print(
        "F2_WEIGHTED_KERNEL_COLLISION_FLOOR_PASS "
        f"cases={len(cases)} collisions={sum(x for x, _ in counts)} "
        f"kernel_words={sum(y for _, y in counts)} dag=1/1"
    )


if __name__ == "__main__":
    main()
