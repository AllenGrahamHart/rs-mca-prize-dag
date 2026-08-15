#!/usr/bin/env python3
"""Small-plane falsification audit for the split-pencil offset cap."""

from __future__ import annotations

import hashlib
import itertools
import json
import random
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "c16ddeb5b7e492a6ababe1f558ba7f7b049ac4f1116149191d7065dbed163159"


def affine_lines(prime: int) -> list[tuple[int, ...]]:
    points = [(x, y) for x in range(prime) for y in range(prime)]
    index = {point: i for i, point in enumerate(points)}
    lines = [tuple(index[(a, y)] for y in range(prime)) for a in range(prime)]
    for slope in range(prime):
        for intercept in range(prime):
            lines.append(
                tuple(index[(x, (slope * x + intercept) % prime)] for x in range(prime))
            )
    assert len(lines) == len(set(lines)) == prime * (prime + 1)
    return lines


def exact_charge(capacities: tuple[int, ...], target: int, offset: int) -> int | None:
    best = [0] + [-1] * target
    for ceiling in capacities:
        nxt = [-1] * (target + 1)
        for used, value in enumerate(best):
            if value < 0:
                continue
            for take in range(min(ceiling, target - used) + 1):
                nxt[used + take] = max(nxt[used + take], value + comb(take, 2))
        best = nxt
    return None if best[target] < 0 else best[target] + offset * target


def cap(petal_mass: int, total: int, offset: int) -> int:
    heavy = total // (petal_mass // 2 + 1)
    cross_floor = petal_mass * petal_mass // 4
    balanced = comb(total, 2) * (cross_floor + offset * petal_mass) // cross_floor
    collision = comb(heavy, 2) * (comb(petal_mass - 1, 2) + offset * petal_mass)
    clean = max(
        ell * ((petal_mass - 2) * (total - ell) + 2 * heavy * offset * petal_mass) // 2
        for ell in range(total + 1)
    )
    return clean + balanced + collision


def check(weights: tuple[int, ...], lines: list[tuple[int, ...]], p: int, r: int) -> None:
    observed = 0
    for line in lines:
        charge = exact_charge(tuple(weights[i] for i in line), p, r)
        if charge is not None:
            observed += charge
    assert observed <= cap(p, sum(weights), r), (p, r, weights, observed, cap(p, sum(weights), r))


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["parameters"]["K11_specializations"][1]["total_cap"] == 9275866238180030

    exhaustive = 0
    lines3 = affine_lines(3)
    for p in (3, 4):
        for r in (0, 1, 2):
            for weights in itertools.product(range(p), repeat=9):
                check(weights, lines3, p, r)
                exhaustive += 1

    rng = random.Random(20260815)
    random_checks = 0
    lines5 = affine_lines(5)
    for p in range(3, 10):
        for r in range(4):
            for _ in range(80):
                weights = tuple(rng.randrange(p) for _ in range(25))
                check(weights, lines5, p, r)
                random_checks += 1

    print(
        "PASS split-pencil core-offset audit: "
        f"{exhaustive} exhaustive F3 instances, "
        f"{random_checks} deterministic F5 instances"
    )


if __name__ == "__main__":
    main()
