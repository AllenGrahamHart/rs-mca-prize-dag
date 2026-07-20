#!/usr/bin/env python3
"""Verify the HGE4 primitive swap straight-line certificate lift."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_primitive_swap_straight_line_certificate_lift"
DEPENDENCIES = {"f3_hge4_primitive_swap_half_order_square_descent"}
CONSUMERS = {"f3_hge4_norm_gate_count"}


def trim(polynomial: list[int]) -> list[int]:
    while polynomial and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def add(left: list[int], right: list[int], prime: int) -> list[int]:
    output = [0] * max(len(left), len(right))
    for index in range(len(output)):
        output[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % prime
    return trim(output)


def multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    if not left or not right:
        return []
    output = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            output[i + j] = (output[i + j] + a * b) % prime
    return trim(output)


def divide_monic(
    dividend: list[int], divisor: list[int], prime: int
) -> tuple[list[int], list[int]]:
    assert divisor and divisor[-1] == 1
    work = trim(dividend.copy())
    quotient = [0] * max(0, len(work) - len(divisor) + 1)
    while len(work) >= len(divisor):
        shift = len(work) - len(divisor)
        factor = work[-1]
        quotient[shift] = factor
        for index, coefficient in enumerate(divisor):
            work[index + shift] = (work[index + shift] - factor * coefficient) % prime
        trim(work)
    return trim(quotient), work


def divisor_from_t(t: list[int], scalar: int, prime: int) -> list[int]:
    square = multiply(t, t, prime)
    return [(-scalar) % prime, *square]


def recurrence(divisor: list[int], exponent_log: int, prime: int) -> tuple[list[list[int]], list[list[int]]]:
    values = [[0, 1]]
    quotients: list[list[int]] = []
    for _ in range(exponent_log):
        square = multiply(values[-1], values[-1], prime)
        quotient, value = divide_monic(square, divisor, prime)
        quotients.append(quotient)
        values.append(value)
    return values, quotients


def presentation_size(exponent_log: int, width: int) -> tuple[int, int, int, int]:
    assert width >= 5 and width % 2 == 1
    s_0 = (width - 1).bit_length() - 1
    k = exponent_log - s_0
    assert k >= 1
    base = (width + 1) // 2
    variables = base + k * (2 * width - 1) - width
    equations = k * (2 * width - 1)
    return s_0, k, variables, equations


def fixture_check() -> None:
    prime, order, width = 97, 16, 5
    t = [78, 73, 1]
    scalar = 18
    divisor = divisor_from_t(t, scalar, prime)
    assert divisor == [79, 70, 39, 53, 49, 1]
    values, quotients = recurrence(divisor, 4, prime)
    assert values[-1] == [1]
    assert len(values) == 5 and len(quotients) == 4
    for current, quotient, following in zip(values, quotients, values[1:]):
        left = multiply(current, current, prime)
        right = add(following, multiply(divisor, quotient, prime), prime)
        assert left == right
        assert len(following) <= width
        assert len(quotient) <= width - 1


def size_check() -> None:
    assert presentation_size(12, 5) == (2, 10, 88, 90)
    assert presentation_size(12, 7) == (2, 10, 127, 130)
    assert presentation_size(12, 9) == (3, 9, 149, 153)
    assert presentation_size(40, 5) == (2, 38, 340, 342)


def parity_check() -> None:
    for order in (4, 8):
        full_order = 2 * order
        for weight in range(1, full_order + 1, 2):
            for support in combinations(range(full_order), weight):
                coefficients = [int(index in support) for index in range(full_order)]
                divisible = all(
                    coefficients[index] == coefficients[index + order]
                    for index in range(order)
                )
                assert not divisible


def first_moment_route_fence() -> None:
    prime, root = 337, 191
    support = (0, 1, 2, 5, 7, 11, 12)
    assert pow(root, 16, prime) == 1 and pow(root, 8, prime) == -1 % prime
    moments = tuple(
        sum(pow(pow(root, exponent, prime), degree, prime) for exponent in support)
        % prime
        for degree in (1, 3, 5)
    )
    assert moments == (0, 163, 240)
    assert prime >= 16**2 and (prime - 1) % 16 == 0


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
        "variables = b+k(2h-1)-h",
        "maximum total degree = 3",
        "Delta_(N,h)",
        "sharp next boundary",
        "does not bound the number",
    ):
        assert marker in text


def main() -> None:
    fixture_check()
    size_check()
    parity_check()
    first_moment_route_fence()
    packet_check()
    print(
        "F3_HGE4_PRIMITIVE_SWAP_STRAIGHT_LINE_CERTIFICATE_LIFT_PASS "
        "fixture_N=16 h5_vars=88 h7_vars=127 h9_vars=149 parity_orders=2 "
        "first_moment_fence=1"
    )


if __name__ == "__main__":
    main()
