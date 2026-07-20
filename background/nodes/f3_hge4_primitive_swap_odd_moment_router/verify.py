#!/usr/bin/env python3
"""Verify the HGE4 primitive swap odd-moment router."""

from __future__ import annotations

import json
from itertools import combinations, product
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_primitive_swap_odd_moment_router"
DEPENDENCIES = {"f3_hge4_primitive_shift_pair_near_square_union_router"}
CONSUMERS = {"f3_hge4_norm_gate_count"}


def primitive_root(prime: int) -> int:
    factors = set()
    value = prime - 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.add(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.add(value)
    for candidate in range(2, prime):
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("primitive root not found")


def multiply(left: tuple[int, ...], right: tuple[int, ...], prime: int) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] = (output[i + j] + a * b) % prime
    return tuple(output)


def locator(values: tuple[int, ...], prime: int) -> tuple[int, ...]:
    polynomial = (1,)
    for value in values:
        polynomial = multiply(polynomial, (1, -value % prime), prime)
    return polynomial


def translate(support: frozenset[int], amount: int, order: int) -> frozenset[int]:
    return frozenset((value + amount) % order for value in support)


def common_stabilizer(left: frozenset[int], right: frozenset[int], order: int) -> tuple[int, ...]:
    return tuple(
        amount
        for amount in range(order)
        if translate(left, amount, order) == left
        and translate(right, amount, order) == right
    )


def swap_fixture() -> dict:
    order, prime, width = 32, 97, 5
    generator = primitive_root(prime)
    omega = pow(generator, (prime - 1) // order, prime)
    points = tuple(pow(omega, exponent, prime) for exponent in range(order))
    left = frozenset((0, 1, 2, 6, 20))
    right = translate(left, order // 2, order)
    assert not left & right
    assert common_stabilizer(left, right, order) == (0,)
    union = left | right
    assert tuple(
        amount for amount in range(order) if translate(union, amount, order) == union
    ) == (0, order // 2)

    left_locator = locator(tuple(points[index] for index in sorted(left)), prime)
    right_locator = locator(tuple(points[index] for index in sorted(right)), prime)
    assert left_locator[:-1] == right_locator[:-1]
    assert left_locator[-1] != right_locator[-1]

    elementary = tuple(
        ((-1) ** index * left_locator[index]) % prime
        for index in range(width + 1)
    )
    odd_elementary = tuple(elementary[index] for index in range(1, width, 2))
    odd_powers = tuple(
        sum(pow(points[index], degree, prime) for index in left) % prime
        for degree in range(1, width, 2)
    )
    assert odd_elementary == (0, 0)
    assert odd_powers == (0, 0)

    inverse_two = pow(2, -1, prime)
    center = tuple(
        (left_value + right_value) * inverse_two % prime
        for left_value, right_value in zip(left_locator, right_locator)
    )
    for index, coefficient in enumerate(center):
        degree = width - index
        if degree % 2 == 0:
            assert coefficient == 0

    return {
        "order": order,
        "prime": prime,
        "width": width,
        "left": left,
        "union": union,
        "points": points,
        "odd_elementary": odd_elementary,
        "odd_powers": odd_powers,
    }


def complete_width_five_check() -> None:
    order, prime, width = 32, 97, 5
    omega = pow(primitive_root(prime), (prime - 1) // order, prime)
    points = tuple(pow(omega, exponent, prime) for exponent in range(order))
    unions: set[frozenset[int]] = set()
    for bases in combinations(range(order // 2), width):
        for tail in product((0, 1), repeat=width - 1):
            bits = (0,) + tail
            left = frozenset(
                base + bit * (order // 2) for base, bit in zip(bases, bits)
            )
            right = translate(left, order // 2, order)
            if common_stabilizer(left, right, order) != (0,):
                continue
            if any(
                sum(pow(points[index], degree, prime) for index in left) % prime
                for degree in range(1, width, 2)
            ):
                continue
            unions.add(left | right)

    orbit_keys = {
        min(tuple(sorted(translate(union, amount, order))) for amount in range(order))
        for union in unions
    }
    anchored = sum(0 in union for union in unions)
    assert len(unions) == 32
    assert len(orbit_keys) == 2
    assert anchored == 10 == width * len(orbit_keys)
    assert len(unions) == (order // 2) * len(orbit_keys)
    assert anchored <= comb(order // 2 - 1, width - 1)


def even_width_constant_check() -> None:
    order, prime, width = 16, 17, 4
    omega = pow(primitive_root(prime), (prime - 1) // order, prime)
    points = tuple(pow(omega, exponent, prime) for exponent in range(order))
    for bases in combinations(range(order // 2), width):
        for bits in product((0, 1), repeat=width):
            left = frozenset(
                base + bit * (order // 2) for base, bit in zip(bases, bits)
            )
            right = translate(left, order // 2, order)
            left_locator = locator(tuple(points[index] for index in sorted(left)), prime)
            right_locator = locator(tuple(points[index] for index in sorted(right)), prime)
            assert not (
                left_locator[:-1] == right_locator[:-1]
                and left_locator[-1] != right_locator[-1]
            )


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "`h` is odd",
        "sum_(x in P)x^j=0",
        "binom(n/2-1,h-1)",
        "odd Vandermonde",
        "does not bound the free",
    ):
        assert marker in text


def main() -> None:
    swap_fixture()
    complete_width_five_check()
    even_width_constant_check()
    packet_check()
    print(
        "F3_HGE4_PRIMITIVE_SWAP_ODD_MOMENT_ROUTER_PASS "
        "even_swap=0 h5_unions=32 h5_orbits=2 h5_anchored=10"
    )


if __name__ == "__main__":
    main()
