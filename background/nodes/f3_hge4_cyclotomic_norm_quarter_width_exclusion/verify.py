#!/usr/bin/env python3
"""Verify the HGE4 cyclotomic-norm quarter-width exclusion packet."""

from __future__ import annotations

import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_cyclotomic_norm_quarter_width_exclusion"
DEPENDENCIES = {
    "f3_hge4_exact_ratio_tower_orbit_compiler",
    "f3_hge4_near_third_belyi_necklace_bound",
}
CONSUMER = "f3_hge4_norm_gate_count"


def prime_factors(value: int) -> set[int]:
    factors: set[int] = set()
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.add(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.add(value)
    return factors


def primitive_root(prime: int) -> int:
    factors = prime_factors(prime - 1)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("primitive root not found")


def locator(indices: tuple[int, ...], roots: list[int], prime: int) -> tuple[int, ...]:
    coefficients = [1]
    for index in indices:
        inverse = pow(roots[index], -1, prime)
        following = [0] * (len(coefficients) + 1)
        for degree, coefficient in enumerate(coefficients):
            following[degree] = (following[degree] + coefficient) % prime
            following[degree + 1] = (
                following[degree + 1] - coefficient * inverse
            ) % prime
        coefficients = following
    return tuple(coefficients)


def common_stabilizer(left: set[int], right: set[int], order: int) -> list[int]:
    return [
        shift
        for shift in range(order)
        if {(value + shift) % order for value in left} == left
        and {(value + shift) % order for value in right} == right
    ]


def exhaustive_first_level() -> tuple[tuple[int, int], tuple[int, int]]:
    prime, order = 257, 16
    generator = pow(primitive_root(prime), (prime - 1) // order, prime)
    roots = [pow(generator, exponent, prime) for exponent in range(order)]
    output: list[tuple[int, int]] = []
    for width in (4, 5):
        prefixes: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
        for indices in combinations(range(order), width):
            coefficients = locator(indices, roots, prime)
            prefixes[coefficients[:-1]].append(indices)
        ordered = primitive = 0
        for members in prefixes.values():
            for left in members:
                for right in members:
                    if left == right:
                        continue
                    ordered += 1
                    if common_stabilizer(set(left), set(right), order) == [0]:
                        primitive += 1
        output.append((ordered, primitive))
    assert output == [(12, 0), (0, 0)]
    return output[0], output[1]


def inequality_check() -> int:
    checks = 0
    for exponent in range(4, 14):
        order = 1 << exponent
        quarter = order // 4
        for width in range(quarter, (order - 1) // 3 + 1):
            rank = width // 2
            energy = order if width == quarter + 1 else 4 * width
            lower = (order * order + 1) ** rank
            upper = energy ** quarter
            assert lower > upper, (order, width, lower.bit_length(), upper.bit_length())
            checks += 1
    return checks


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join((base / name).read_text() for name in required if name.endswith(".md"))
    for marker in (
        "p^r_h divides",
        "Odd-frequency Parseval",
        "h=m/4+1",
        "sum_t g_t^2<=4h-4=m",
        "4<=h<=m/4-1",
        "does not estimate any width in the lower-quarter",
    ):
        assert marker in text


def main() -> None:
    first_level = exhaustive_first_level()
    inequalities = inequality_check()
    packet_check()
    print(
        "F3_HGE4_CYCLOTOMIC_NORM_QUARTER_WIDTH_EXCLUSION_PASS "
        f"inequalities={inequalities} first_level={first_level}"
    )


if __name__ == "__main__":
    main()
