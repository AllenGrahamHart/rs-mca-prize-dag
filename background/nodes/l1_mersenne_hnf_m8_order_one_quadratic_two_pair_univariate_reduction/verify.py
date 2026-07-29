#!/usr/bin/env python3
"""Check the exact degree-eight two-pair eliminant."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_mersenne_hnf_m8_order_one_quadratic_two_pair_univariate_reduction"
DEPENDENCIES = {
    "l1_mersenne_hnf_m8_order_one_conic_reduction",
    "l1_mersenne_hnf_m8_order_one_quadratic_collision_router",
}
CONSUMER = "l1_mixed_petal_amplification"


def add(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return out


def scale(poly: list[int], scalar: int) -> list[int]:
    return [scalar * value for value in poly]


def mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def main() -> None:
    d_poly = [18, 1, -1]
    conic_b = [3, 6, 7, 4, 1]
    conic_a = [27, 27, 11]
    d_times_d_poly = [0, 18, 1, -1]
    expanded = add(
        add(scale(mul(conic_b, mul(d_poly, d_poly)), 5), scale(mul(conic_a, d_times_d_poly), -112)),
        [0, 0, 53760],
    )
    expected = [4860, -44172, 8199, -15516, 2862, 672, -180, 10, 5]
    assert expanded == expected

    atlas = ROOT / "background/nodes/l1_official_checkpoint_characteristic_atlas/checkpoint_atlas.tsv"
    primes = []
    for line in atlas.read_text().splitlines()[1:]:
        _, _, p, _, m, remainder = map(int, line.split("\t"))
        if m == 8 and remainder == 8:
            primes.append(p)
    assert sorted(primes) == [8191, 131071, 524287, 2147483647]
    assert len(primes) * 8 == 32

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {node["id"]: node["status"] for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    for dependency in DEPENDENCIES:
        assert statuses[dependency] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert statuses[CONSUMER] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / f"background/nodes/{NODE}/statement.md").read_text()
    proof = (ROOT / f"background/nodes/{NODE}/proof.md").read_text()
    for anchor in ("(QUR2)", "(QUR3)", "32 degree-eight gcd packets"):
        assert anchor in statement
    for anchor in ("D^2/24", "53760d^2", "no sufficiency"):
        assert anchor in proof

    print("L1_MERSENNE_HNF_M8_ORDER_ONE_QUADRATIC_TWO_PAIR_UNIVARIATE_REDUCTION_PASS degree=8 packets=32")


if __name__ == "__main__":
    main()
