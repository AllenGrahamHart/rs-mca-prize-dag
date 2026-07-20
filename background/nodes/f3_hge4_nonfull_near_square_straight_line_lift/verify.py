#!/usr/bin/env python3
"""Verify the HGE4 non-full near-square straight-line lift."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_nonfull_near_square_straight_line_lift"
DEPENDENCIES = {
    "f3_hge4_primitive_shift_pair_near_square_union_router",
    "x24_char0_dyadic_descent",
}
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


def near_square(center: list[int], shift: int, prime: int) -> list[int]:
    square = multiply(center, center, prime)
    square[0] = (square[0] - shift * shift) % prime
    return trim(square)


def recurrence(divisor: list[int], exponent_log: int, prime: int) -> tuple[list[list[int]], list[list[int]]]:
    values = [[0, 1]]
    quotients: list[list[int]] = []
    for _ in range(exponent_log):
        quotient, value = divide_monic(
            multiply(values[-1], values[-1], prime), divisor, prime
        )
        quotients.append(quotient)
        values.append(value)
    return values, quotients


def sizes(exponent_log: int, width: int) -> tuple[int, int, int, int, int]:
    assert width >= 4
    r_0 = (2 * width - 1).bit_length() - 1
    k = exponent_log - r_0
    assert k >= 1
    global_variables = k * (4 * width - 1)
    chart_variables = global_variables - width + 2
    equations = global_variables + 1
    return r_0, k, global_variables, chart_variables, equations


def finite_nonfull_fixture() -> None:
    prime, width = 97, 5
    center = [0, 78, 0, 73, 0, 1]
    divisor = near_square(center, 42, prime)
    values, quotients = recurrence(divisor, 5, prime)
    assert values[-1] == [1]
    assert any(center[index] for index in range(1, width))
    selectors = [pow(center[1], -1, prime), 0, 0, 0]
    assert sum(selectors[index - 1] * center[index] for index in range(1, width)) % prime == 1
    for current, quotient, following in zip(values, quotients, values[1:]):
        assert multiply(current, current, prime) == add(
            following, multiply(divisor, quotient, prime), prime
        )


def full_fiber_guard() -> None:
    prime, width = 97, 4
    center = [0, 0, 0, 0, 1]
    divisor = near_square(center, 1, prime)
    values, _ = recurrence(divisor, 4, prime)
    assert values[-1] == [1]
    assert not any(center[index] for index in range(1, width))


def size_check() -> None:
    assert sizes(13, 4) == (2, 11, 165, 163, 166)
    assert sizes(13, 5) == (3, 10, 190, 187, 191)
    assert sizes(13, 6) == (3, 10, 230, 226, 231)
    assert sizes(13, 8) == (3, 10, 310, 304, 311)


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
        "sum_(j=1)^(h-1) z_j s_j=1",
        "variables = k(4h-1)",
        "h-1` chart cover",
        "legacy x24 source path is absent",
        "No certificate is computed",
    ):
        assert marker in text


def main() -> None:
    finite_nonfull_fixture()
    full_fiber_guard()
    size_check()
    packet_check()
    print(
        "F3_HGE4_NONFULL_NEAR_SQUARE_STRAIGHT_LINE_LIFT_PASS "
        "nonfull_fixture=1 full_fiber_guard=1 h4_chart=163/166 h5_chart=187/191"
    )


if __name__ == "__main__":
    main()
