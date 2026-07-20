#!/usr/bin/env python3
"""Verify the HGE4 primitive swap half-order square descent."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_primitive_swap_half_order_square_descent"
DEPENDENCIES = {"f3_hge4_primitive_swap_odd_moment_router"}
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


def remainder(
    dividend: tuple[int, ...], divisor: tuple[int, ...], prime: int
) -> tuple[int, ...]:
    work = list(dividend)
    while len(work) >= len(divisor):
        factor = work[0] * pow(divisor[0], -1, prime) % prime
        for index, coefficient in enumerate(divisor):
            work[index] = (work[index] - factor * coefficient) % prime
        while work and work[0] == 0:
            work.pop(0)
    return tuple(work)


def monic_square_root(polynomial: tuple[int, ...], prime: int) -> tuple[int, ...] | None:
    degree = len(polynomial) - 1
    if degree % 2 or polynomial[0] != 1:
        return None
    half = degree // 2
    inverse_two = pow(2, -1, prime)
    root = [1]
    for diagonal in range(1, half + 1):
        known = sum(
            root[index] * root[diagonal - index]
            for index in range(1, diagonal)
        )
        root.append((polynomial[diagonal] - known) * inverse_two % prime)
    candidate = tuple(root)
    return candidate if multiply(candidate, candidate, prime) == polynomial else None


def translate(support: frozenset[int], amount: int, order: int) -> frozenset[int]:
    return frozenset((value + amount) % order for value in support)


def stabilizer(support: frozenset[int], order: int) -> tuple[int, ...]:
    return tuple(
        amount for amount in range(order) if translate(support, amount, order) == support
    )


def square_test(
    exponents: frozenset[int], order: int, prime: int
) -> tuple[int, ...] | None:
    generator = primitive_root(prime)
    omega = pow(generator, (prime - 1) // order, prime)
    values = tuple(pow(omega, exponent, prime) for exponent in sorted(exponents))
    polynomial = list(locator(values, prime))
    product_value = 1
    for value in values:
        product_value = product_value * value % prime
    assert polynomial[-1] == -product_value % prime
    polynomial[-1] = (polynomial[-1] + product_value) % prime
    assert polynomial[-1] == 0
    return monic_square_root(tuple(polynomial[:-1]), prime)


def fixture_check() -> None:
    n, prime, width = 32, 97, 5
    half_order = n // 2
    squared = frozenset((0, 1, 2, 4, 6))
    root = square_test(squared, half_order, prime)
    assert root is not None and len(root) == (width + 1) // 2
    assert stabilizer(squared, half_order) == (0,)

    generator = primitive_root(prime)
    omega = pow(generator, (prime - 1) // n, prime)
    half_omega = pow(omega, 2, prime)
    values = tuple(pow(half_omega, exponent, prime) for exponent in sorted(squared))
    product_value = 1
    for value in values:
        product_value = product_value * value % prime
    divisor = (*multiply(root, root, prime), -product_value % prime)
    cyclotomic = (1, *((0,) * (half_order - 1)), -1 % prime)
    assert divisor == locator(values, prime)
    assert remainder(cyclotomic, divisor, prime) == ()
    square_roots = tuple(value for value in (pow(omega, exponent, prime) for exponent in range(n)) if value * value % prime == product_value)
    assert len(square_roots) == 2
    a = square_roots[0]

    def center(value: int) -> int:
        total = 0
        for coefficient in root:
            total = (total * (value * value % prime) + coefficient) % prime
        return value * total % prime

    minus = frozenset(exponent for exponent in range(n) if center(pow(omega, exponent, prime)) == a)
    plus = frozenset(exponent for exponent in range(n) if center(pow(omega, exponent, prime)) == -a % prime)
    assert len(minus) == len(plus) == width
    assert plus == translate(minus, n // 2, n)
    assert not minus & plus
    assert frozenset(exponent % half_order for exponent in minus) == squared


def complete_half_order_check() -> None:
    n, prime, width = 32, 97, 5
    order = n // 2
    valid: set[frozenset[int]] = set()
    anchored: set[frozenset[int]] = set()
    for choice in combinations(range(order), width):
        support = frozenset(choice)
        if stabilizer(support, order) != (0,):
            continue
        if square_test(support, order, prime) is None:
            continue
        valid.add(support)
        if 0 in support:
            anchored.add(support)
    orbit_keys = {
        min(tuple(sorted(translate(support, amount, order))) for amount in range(order))
        for support in valid
    }
    assert len(valid) == 32
    assert len(orbit_keys) == 2
    assert len(anchored) == 10 == width * len(orbit_keys)


def threshold_analogue_check() -> None:
    n, prime, width = 16, 257, 5
    order = n // 2
    retained = 0
    for tail in combinations(range(1, order), width - 1):
        support = frozenset((0, *tail))
        retained += (
            stabilizer(support, order) == (0,)
            and square_test(support, order, prime) is not None
        )
    assert retained == 0


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
        "(L_Y(Z)+c_Y)/Z=T_Y(Z)^2",
        "mu_n/{+/-1}=mu_N",
        "V_h^swap=W_h",
        "divides  Z^N-1",
        "2^(h-1)",
        "does not bound `W_h`",
    ):
        assert marker in text


def main() -> None:
    fixture_check()
    complete_half_order_check()
    threshold_analogue_check()
    packet_check()
    print(
        "F3_HGE4_PRIMITIVE_SWAP_HALF_ORDER_SQUARE_DESCENT_PASS "
        "h5_supports=32 h5_orbits=2 h5_anchored=10 threshold_n16=0"
    )


if __name__ == "__main__":
    main()
