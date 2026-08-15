#!/usr/bin/env python3
"""Small-plane falsification audit for the weighted split-pencil cap."""

from __future__ import annotations

import hashlib
import itertools
import json
import random
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "414e1f902ec6a53abdb7ea789061c6147af9953c841440b963d71d6dfb7be434"


def affine_lines(prime: int) -> list[tuple[int, ...]]:
    points = [(x, y) for x in range(prime) for y in range(prime)]
    index = {point: i for i, point in enumerate(points)}
    lines: list[tuple[int, ...]] = []
    for intercept in range(prime):
        lines.append(tuple(index[(intercept, y)] for y in range(prime)))
    for slope in range(prime):
        for intercept in range(prime):
            lines.append(
                tuple(index[(x, (slope * x + intercept) % prime)] for x in range(prime))
            )
    assert len(lines) == prime * (prime + 1)
    assert len(set(lines)) == len(lines)
    return lines


def exact_line_charge(capacities: tuple[int, ...], target: int) -> int | None:
    best = [0] + [-1] * target
    for ceiling in capacities:
        nxt = [-1] * (target + 1)
        for used, value in enumerate(best):
            if value < 0:
                continue
            for take in range(min(ceiling, target - used) + 1):
                nxt[used + take] = max(nxt[used + take], value + comb(take, 2))
        best = nxt
    return None if best[target] < 0 else best[target]


def cap(a: int, total: int) -> int:
    heavy_count = total // (a // 2 + 1)
    return (
        (a - 2) * total * total // 8
        + comb(total, 2)
        + comb(heavy_count, 2) * comb(a - 1, 2)
    )


def check_instance(weights: tuple[int, ...], lines: list[tuple[int, ...]], a: int) -> None:
    total_charge = 0
    for line in lines:
        charge = exact_line_charge(tuple(weights[i] for i in line), a)
        if charge is not None:
            total_charge += charge
    assert total_charge <= cap(a, sum(weights)), (a, weights, total_charge, cap(a, sum(weights)))


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["parameters"]["specialization"]["total_cap"] == 9274769506943785

    exhaustive = 0
    lines3 = affine_lines(3)
    for a in (3, 4):
        for weights in itertools.product(range(a), repeat=9):
            check_instance(weights, lines3, a)
            exhaustive += 1

    rng = random.Random(20260815)
    random_checks = 0
    lines5 = affine_lines(5)
    for a in range(3, 10):
        for _ in range(180):
            weights = tuple(rng.randrange(a) for _ in range(25))
            check_instance(weights, lines5, a)
            random_checks += 1

    print(
        "PASS weighted split-pencil audit: "
        f"{exhaustive} exhaustive F3 instances, "
        f"{random_checks} deterministic F5 instances"
    )


if __name__ == "__main__":
    main()
