#!/usr/bin/env python3
"""Exact replay for the fixed-syndrome multiprefix route cut."""

from __future__ import annotations

import itertools
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_fixed_syndrome_multiprefix_route_cut"
CONSUMER = "l1_mixed_petal_amplification"


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for i in range(len(out)):
        out[i] = (
            (left[i] if i < len(left) else 0)
            + (right[i] if i < len(right) else 0)
        ) % p
    return trim(out)


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([(scalar * coefficient) % p for coefficient in poly])


def mul(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out)


def evaluate(poly: list[int], x: int, p: int) -> int:
    out = 0
    for coefficient in reversed(poly):
        out = (out * x + coefficient) % p
    return out


def locator(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for point in points:
        out = mul(out, [(-point) % p, 1], p)
    return out


def prefix(points: tuple[int, ...], depth: int, p: int) -> tuple[int, ...]:
    poly = locator(points, p)
    return tuple(poly[-2 - i] for i in range(depth))


def fixed_template_control() -> int:
    p = 17
    domain = tuple(range(1, p))
    partial = (1, 2, 3)
    labels = {pow(x, 2, p) for x in domain}
    partial_labels = {pow(x, 2, p) for x in partial}
    available = tuple(sorted(labels - partial_labels))
    assert available == (2, 8, 13, 15, 16)

    partial_locator = locator(partial, p)
    center = mul(partial_locator, [0] * 6 + [1], p)
    assert len(center) - 1 == 9

    codewords: set[tuple[int, ...]] = set()
    for selected in itertools.combinations(available, 3):
        full_locator = [1]
        for label in selected:
            full_locator = mul(full_locator, [(-label) % p, 0, 1], p)
        agreement_locator = mul(partial_locator, full_locator, p)
        codeword = add(center, scale(agreement_locator, -1, p), p)
        assert len(codeword) - 1 < 8
        agreement = tuple(
            x for x in domain if evaluate(center, x, p) == evaluate(codeword, x, p)
        )
        expected = tuple(
            x
            for x in domain
            if x in partial or pow(x, 2, p) in selected
        )
        assert agreement == expected
        assert len(agreement) == 9
        codewords.add(tuple(codeword))
    assert len(codewords) == comb(5, 3) == 10
    return len(codewords)


def deployed_floor() -> int:
    p = 2**31 - 1
    k = 1_048_576
    degree = 3_959 + 2_048 * (543 - 32 - 1)
    assert degree == 1_048_439 == k - 137
    numerator = comb(1_021, 543)
    denominator = p**32
    floor = (numerator + denominator - 1) // denominator
    assert floor == 1_693_898
    assert (floor - 1) * denominator < numerator <= floor * denominator
    return floor


def multiprefix_control() -> dict[str, object]:
    p = 17
    domain = tuple(range(1, p))
    support_zero = (1, 2, 3, 4, 9, 13, 14, 15, 16)
    support_bridge = (1, 5, 6, 7, 9, 10, 11, 12, 16)
    bridge = [9, 16, 8, 1]
    received = (0, 0, 0, 0, 6, 14, 6, 1, 0, 14, 2, 4, 0, 0, 0, 0)

    exact_zero = tuple(x for x, y in zip(domain, received) if y == 0)
    exact_bridge = tuple(
        x
        for x, y in zip(domain, received)
        if y == evaluate(bridge, x, p)
    )
    assert exact_zero == support_zero
    assert exact_bridge == support_bridge
    assert len(bridge) - 1 < 7

    error_zero = tuple(x for x in domain if x not in support_zero)
    error_bridge = tuple(x for x in domain if x not in support_bridge)
    agreement_prefixes = (
        prefix(support_zero, 2, p),
        prefix(support_bridge, 2, p),
    )
    error_prefixes = (prefix(error_zero, 2, p), prefix(error_bridge, 2, p))
    assert agreement_prefixes == ((8, 4), (8, 8))
    assert error_prefixes == ((9, 9), (9, 5))
    assert set(support_zero) & set(support_bridge) == {1, 9, 16}
    assert set(error_zero) & set(error_bridge) == {8}
    return {
        "agreement_prefixes": agreement_prefixes,
        "error_prefixes": error_prefixes,
    }


def main() -> None:
    controls = fixed_template_control()
    floor = deployed_floor()
    prefixes = multiprefix_control()

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (NODE, CONSUMER, "ev") in edges

    print(
        "L1_FIXED_SYNDROME_MULTIPREFIX_ROUTE_CUT_PASS "
        f"fixed_template={controls} deployed_floor={floor} "
        f"agreement_prefixes={prefixes['agreement_prefixes']} "
        f"error_prefixes={prefixes['error_prefixes']}"
    )


if __name__ == "__main__":
    main()
