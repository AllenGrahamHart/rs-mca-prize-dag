#!/usr/bin/env python3
"""Verify the XR dual support-extension factorization."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_rank_two_dual_support_extension_factorization"
PARENT = "xr_higher_rank_uniform_split_pencil_reduction"
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


def locator(points: set[int]) -> list[int]:
    result = [1]
    for point in sorted(points):
        result = multiply(result, [(-point) % PRIME, 1])
    return result


def evaluate(poly: list[int], point: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * point + coefficient) % PRIME
    return value


def locator_derivative(points: set[int], point: int) -> int:
    product = 1
    for other in points:
        if other != point:
            product = product * (point - other) % PRIME
    return product


def normalized_word(domain: set[int], numerator: list[int], universe: set[int]) -> dict[int, int]:
    return {
        point: (
            evaluate(numerator, point)
            * pow(locator_derivative(domain, point), -1, PRIME)
            % PRIME
            if point in domain
            else 0
        )
        for point in universe
    }


def fixture(a: int, d: int, z: int, h: int, offset: int) -> int:
    x_size = a + d + 1
    s_size = x_size - z
    t_size = h - d - 1 + z
    assert s_size >= a + 1 and t_size >= 0

    support = set(range(offset, offset + s_size))
    zeros = set(range(offset + s_size, offset + x_size))
    outside = list(range(offset + x_size, offset + x_size + max(t_size, 1) + 3))
    overlap = min(len(zeros), t_size // 2)
    extension = set(sorted(zeros)[:overlap])
    extension.update(outside[: t_size - overlap])
    active_union = support | zeros
    block = support | extension
    assert len(active_union) == a + d + 1
    assert len(block) == a + h
    assert support.isdisjoint(zeros) and support.isdisjoint(extension)

    max_degree = d - z
    cofactor = [17 + offset]
    for degree in range(1, max_degree + 1):
        cofactor.append(degree + 2)
    while any(evaluate(cofactor, point) == 0 for point in support):
        cofactor[0] = (cofactor[0] + 1) % PRIME

    active_numerator = multiply(cofactor, locator(zeros))
    block_numerator = multiply(cofactor, locator(extension))
    assert len(active_numerator) - 1 <= d
    assert len(block_numerator) - 1 < h
    assert len(extension) == h - d - 1 + z

    universe = active_union | block
    active_word = normalized_word(active_union, active_numerator, universe)
    block_word = normalized_word(block, block_numerator, universe)
    assert active_word == block_word
    assert {point for point, value in active_word.items() if value} == support
    for point in support:
        expected = evaluate(cofactor, point) * pow(
            locator_derivative(support, point), -1, PRIME
        ) % PRIME
        assert active_word[point] == expected

    for moment in range(a):
        assert sum(active_word[point] * pow(point, moment, PRIME) for point in active_union) % PRIME == 0
        assert sum(block_word[point] * pow(point, moment, PRIME) for point in block) % PRIME == 0
    return len(universe)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARENT]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "|T_i|=h-d-1+z_i",
        "F_i=R_iLambda_(Z_i)",
        "P_i=R_iLambda_(T_i)",
        "degR_i<=d-z_i",
        "lambda_i(x)=R_i(x)/Lambda'_(S_i)(x)",
        "cofactor`R_i`isunique",
        "exactdual-codewordsupport-extensioncertificate",
        "doesnotassertthatanabstractextension`T_i`isanactualagreementblock",
    ):
        assert marker in statement


def main() -> None:
    parameters = [
        (4, 2, 1, 5, 0),
        (7, 4, 2, 6, 30),
        (8, 7, 4, 5, 70),
        (9, 5, 5, 8, 120),
    ]
    points = sum(fixture(*entry) for entry in parameters)
    packet_check()
    print(
        "XR_RANK_TWO_DUAL_SUPPORT_EXTENSION_FACTORIZATION_PASS "
        f"fixtures={len(parameters)} points={points}"
    )


if __name__ == "__main__":
    main()
