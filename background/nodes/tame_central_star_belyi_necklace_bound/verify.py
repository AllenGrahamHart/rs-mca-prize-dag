#!/usr/bin/env python3
"""Verify the central-star passport and binary-necklace count."""

from __future__ import annotations

import json
from itertools import combinations
from math import comb, gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "tame_central_star_belyi_necklace_bound"
CONSUMER = "f3_hge4_near_third_belyi_necklace_bound"


def divisors(value: int) -> list[int]:
    return [candidate for candidate in range(1, value + 1) if value % candidate == 0]


def totient(value: int) -> int:
    return sum(1 for candidate in range(1, value + 1) if gcd(candidate, value) == 1)


def necklace_formula(length: int, weight: int) -> int:
    numerator = sum(
        totient(divisor) * comb(length // divisor, weight // divisor)
        for divisor in divisors(gcd(length, weight))
    )
    assert numerator % length == 0
    return numerator // length


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[index:] + word[:index] for index in range(len(word)))


def brute_necklaces(length: int, weight: int) -> int:
    words: set[tuple[int, ...]] = set()
    for positions in combinations(range(length), weight):
        word = [0] * length
        for position in positions:
            word[position] = 1
        words.add(canonical_rotation(tuple(word)))
    return len(words)


def passport_check(h_value: int, e_value: int) -> None:
    center = h_value + e_value
    degree = 3 * h_value + e_value
    finite_ramification = 2 * h_value + center - 1
    infinity_ramification = degree - 1
    assert finite_ramification + infinity_ramification == 2 * degree - 2
    vertices = (h_value + e_value) + (1 + 2 * h_value)
    assert vertices == degree + 1
    assert center == h_value + e_value


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (NODE, CONSUMER, "req") in edges
    base = ROOT / "background/nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "A=ZS^3", "A-1=y^cT", "binary necklaces", "(CSN1)",
        "p>m", "not every necklace",
    ):
        assert marker in text


def main() -> None:
    checked = 0
    for length in range(2, 13):
        for weight in range(1, length):
            assert necklace_formula(length, weight) == brute_necklaces(length, weight)
            checked += 1
    for h_value, e_value in ((5, 1), (10, 2), (20, 4), (41, 5)):
        passport_check(h_value, e_value)
    packet_check()
    print(
        "TAME_CENTRAL_STAR_BELYI_NECKLACE_BOUND_PASS "
        f"necklace_cells={checked} passports=4"
    )


if __name__ == "__main__":
    main()
