#!/usr/bin/env python3
"""Verify the quadratic scroll atlas and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_quadratic_scroll_atlas"
PLUCKER = "rate_half_list_budget_three_plucker_edge_gate"
LINEAR = "rate_half_list_budget_three_linear_grassmann_atlas"
CONSUMER = "rate_half_list_adjacent_crossing"
P = 101


def trim(poly: tuple[int, ...]) -> tuple[int, ...]:
    values = list(poly)
    while len(values) > 1 and values[-1] % P == 0:
        values.pop()
    return tuple(value % P for value in values)


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return trim(tuple((left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0) for i in range(size)))


def scale(poly: tuple[int, ...], scalar: int) -> tuple[int, ...]:
    return trim(tuple(scalar * value for value in poly))


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return trim(tuple(answer))


def degree(poly: tuple[int, ...]) -> int:
    return len(trim(poly)) - 1


def balance(
    b01: tuple[int, ...],
    b02: tuple[int, ...],
    b03: tuple[int, ...],
    b12: tuple[int, ...],
    b13: tuple[int, ...],
) -> tuple[list[tuple[int, ...]], list[tuple[int, ...]], tuple[int, ...]]:
    r0 = [b01, (0,), scale(b12, -1), scale(b13, -1)]
    r1 = [(0,), b01, b02, b03]
    h = (0,)
    if degree(b13) == 2:
        h = (0, b13[-1] * pow(b03[-1], -1, P) % P)
    row = [add(left, multiply(h, right)) for left, right in zip(r0, r1, strict=True)]
    assert max(map(degree, row)) <= 1
    assert max(map(degree, r1)) <= 1
    return row, r1, h


def wedge(rows: tuple[list[tuple[int, ...]], list[tuple[int, ...]]]) -> tuple[tuple[int, ...], ...]:
    left, right = rows
    result = []
    for i in range(4):
        for j in range(i + 1, 4):
            result.append(add(multiply(left[i], right[j]), scale(multiply(left[j], right[i]), -1)))
    return tuple(result)


def check_fixtures() -> None:
    x1 = (1, 1)
    samples = (
        # pendant: b13 linear, b23 quadratic
        ((1,), (2,), (3, 1), (5, 1), (7, 1), (0, 0, 1)),
        # pendant: b13 quadratic, leading cancellation makes b23 linear
        ((1,), (1,), (3, 1), (5, 1), (7, 4, 1), (0, 1)),
        # pendant: b13 and b23 quadratic
        ((1,), (3,), (3, 1), (5, 1), (7, 4, 1), (0, 0, 1)),
        # K4-e: four linear entries and quadratic b23
        ((1,), (2, 2), (3, 1), (5, 1), (7, 1), (0, 0, 1)),
    )
    expected_degrees = ((0, 0, 1, 1, 1, 2), (0, 0, 1, 1, 2, 1), (0, 0, 1, 1, 2, 2), (0, 1, 1, 1, 1, 2))
    for sample, expected in zip(samples, expected_degrees, strict=True):
        b01, b02, b03, b12, b13, _ = sample
        b23 = add(multiply(b02, b13), scale(multiply(b03, b12), -1))
        degrees = tuple(map(degree, (b01, b02, b03, b12, b13, b23)))
        assert degrees == expected
        u, v, _ = balance(b01, b02, b03, b12, b13)
        minors = wedge((u, v))
        target = tuple(scale(poly, b01[0]) for poly in (b01, b02, b03, b12, b13, b23))
        assert minors == target
        leading_u = tuple(poly[1] if len(poly) > 1 else 0 for poly in u)
        leading_v = tuple(poly[1] if len(poly) > 1 else 0 for poly in v)
        assert any((leading_u[i] * leading_v[j] - leading_u[j] * leading_v[i]) % P for i in range(4) for j in range(i + 1, 4))
    assert degree(x1) == 1


def check_sources() -> None:
    packet = ROOT / "background" / "nodes" / NODE
    statement = (packet / "statement.md").read_text()
    proof = (packet / "proof.md").read_text()
    assert "three" in statement and "pendant chambers" in statement and "quadratic `K_4-e` chamber" in statement
    assert "C^(-1)A=(alpha,X alpha,beta,X beta)^T" in statement
    assert "U_1 wedge V_1!=0" in statement
    assert "No rational denominator remains" in proof


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    for parent in (PLUCKER, LINEAR):
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    check_fixtures()
    check_sources()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_QUADRATIC_SCROLL_ATLAS_PASS "
        "quadratic_chambers=4 balanced_rows=4 exceptional_degrees=4,6 dag=3/3"
    )


if __name__ == "__main__":
    main()
