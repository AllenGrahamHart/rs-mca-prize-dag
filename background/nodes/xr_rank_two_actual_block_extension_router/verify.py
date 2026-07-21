#!/usr/bin/env python3
"""Verify the XR actual-block extension router."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_rank_two_actual_block_extension_router"
PARENTS = {
    "xr_rank_two_dual_support_extension_factorization",
    "xr_rank_two_received_pair_alternating_router",
}
CONSUMER = "xr_highcore_collision_count"
PRIME = 1009


def trim(poly: list[int]) -> list[int]:
    result = [entry % PRIME for entry in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def multiply(left: list[int], right: list[int]) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            product[i + j] = (product[i + j] + x * y) % PRIME
    return trim(product)


def add(left: list[int], right: list[int]) -> list[int]:
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def locator(points: set[int]) -> list[int]:
    result = [1]
    for point in sorted(points):
        result = multiply(result, [(-point) % PRIME, 1])
    return result


def divide_monic(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    remainder = trim(dividend)
    divisor = trim(divisor)
    assert divisor[-1] == 1
    if len(remainder) < len(divisor):
        return [0], remainder
    quotient = [0] * (len(remainder) - len(divisor) + 1)
    while len(remainder) >= len(divisor) and remainder != [0]:
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1]
        quotient[shift] = coefficient
        for i, value in enumerate(divisor):
            remainder[i + shift] = (remainder[i + shift] - coefficient * value) % PRIME
        remainder = trim(remainder)
    return trim(quotient), trim(remainder)


def evaluate(poly: list[int], point: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % PRIME
    return value


def locator_derivative(domain: set[int], point: int) -> int:
    product = 1
    for other in domain:
        if other != point:
            product = product * (point - other) % PRIME
    return product


def parity(domain: set[int], numerator: list[int], function: dict[int, int]) -> int:
    return sum(
        evaluate(numerator, point)
        * function[point]
        * pow(locator_derivative(domain, point), -1, PRIME)
        for point in domain
    ) % PRIME


def fixture(a: int, d: int, z: int, h: int, offset: int) -> tuple[int, int]:
    support_size = a + d + 1 - z
    tau = h - d - 1 + z
    assert support_size >= a + 1 and tau >= 1
    support = set(range(offset, offset + support_size))
    zeros = set(range(offset + support_size, offset + a + d + 1))
    external = list(range(offset + a + d + 1, offset + a + d + tau + 8))
    omega = support | zeros | set(external)

    external_zero_set = set(sorted(zeros)[: min(2, len(zeros))])
    external_zero_set.update(external[: tau + 2 - len(external_zero_set)])
    assert len(external_zero_set) == tau + 2
    assert support.isdisjoint(external_zero_set)

    correction = [7 + offset, 3, 2]
    assert len(correction) - 1 < a
    residual = {
        point: 0 if point in support or point in external_zero_set else (point + 19) % PRIME
        for point in omega
    }
    direction = {
        point: (residual[point] - evaluate(correction, point)) % PRIME
        for point in omega
    }

    local_dimension = d + 1 - z
    for degree in range(local_dimension):
        assert parity(support, [0] * degree + [1], direction) == 0

    extensions = list(itertools.combinations(sorted(external_zero_set), tau))
    assert len(extensions) == math.comb(len(external_zero_set), tau)
    for extension_tuple in extensions:
        extension = set(extension_tuple)
        block = support | extension
        assert len(block) == a + h
        for degree in range(h):
            assert parity(block, [0] * degree + [1], direction) == 0

        test_polynomial = [degree + 2 for degree in range(h)]
        quotient, remainder = divide_monic(test_polynomial, locator(extension))
        assert len(quotient) - 1 < local_dimension
        assert len(remainder) - 1 < tau
        assert add(multiply(locator(extension), quotient), remainder) == trim(test_polynomial)
        left = parity(block, test_polynomial, direction)
        right = (
            parity(support, quotient, direction)
            + parity(block, remainder, direction)
        ) % PRIME
        assert left == right == 0

        cofactor = [5, 1][: local_dimension]
        selected_numerator = multiply(cofactor, locator(extension))
        assert parity(block, selected_numerator, direction) == 0

    bad_point = next(point for point in omega if point not in support | external_zero_set)
    bad_extension = {bad_point} | set(sorted(external_zero_set)[: tau - 1])
    bad_block = support | bad_extension
    assert len(bad_block) == a + h
    assert any(
        parity(bad_block, [0] * degree + [1], direction)
        for degree in range(h)
    )
    return len(extensions), h - 1


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "J=Lambda_(T_i)U+V",
        "d+1-z_i",
        "extension-sensitivechecks",
        "(d-z_i)+tau_i=h-1",
        "uniquepolynomial`w_i`ofdegreebelow`a`",
        "E_i={xinOmega\\S_i:f_i(x)+w_i(x)=0}",
        "T_isubsetE_i",
        "C(|E_i|,tau_i)",
        "closesper-rowagreement-blockextensioncounting",
    ):
        assert marker in statement


def main() -> None:
    parameters = [
        (4, 2, 1, 5, 0),
        (7, 4, 2, 6, 40),
        (8, 7, 4, 5, 90),
        (9, 5, 5, 8, 140),
    ]
    counts = [fixture(*entry) for entry in parameters]
    packet_check()
    print(
        "XR_RANK_TWO_ACTUAL_BLOCK_EXTENSION_ROUTER_PASS "
        f"fixtures={len(counts)} extensions={sum(count for count, _ in counts)} "
        f"residual_checks={sum(checks for _, checks in counts)}"
    )


if __name__ == "__main__":
    main()
