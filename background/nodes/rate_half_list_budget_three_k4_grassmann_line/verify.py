#!/usr/bin/env python3
"""Verify the K4 Grassmann-line compression and DAG wiring."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_k4_grassmann_line"
PLUCKER = "rate_half_list_budget_three_plucker_edge_gate"
ATLAS = "rate_half_list_budget_three_residual_transversal_atlas"
CONSUMER = "rate_half_list_adjacent_crossing"
P = 101


def determinant3(rows: list[tuple[int, int, int]]) -> int:
    (a, b, c), (d, e, f), (g, h, i) = rows
    return (a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)) % P


def edge(w: tuple[int, ...], u: tuple[int, ...], v: tuple[int, ...], i: int, j: int) -> tuple[int, int]:
    return ((w[i] * u[j] - w[j] * u[i]) % P, (w[i] * v[j] - w[j] * v[i]) % P)


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % P
    return tuple(answer)


def add(*polys: tuple[int, ...]) -> tuple[int, ...]:
    size = max(map(len, polys))
    return tuple(sum(poly[i] if i < len(poly) else 0 for poly in polys) % P for i in range(size))


def scale(poly: tuple[int, ...], scalar: int) -> tuple[int, ...]:
    return tuple(scalar * value % P for value in poly)


def check_fixture() -> None:
    w = (1, 1, 1, 1)
    u = (0, 1, 8, 27)
    v = (0, 1, 2, 3)
    edges = {(i, j): edge(w, u, v, i, j) for i, j in combinations(range(4), 2)}
    assert all(linear != 0 for _, linear in edges.values())
    roots = {
        (-constant * pow(linear, -1, P)) % P
        for constant, linear in edges.values()
    }
    assert len(roots) == 6

    b01, b02, b03 = edges[(0, 1)], edges[(0, 2)], edges[(0, 3)]
    b12, b13, b23 = edges[(1, 2)], edges[(1, 3)], edges[(2, 3)]
    plucker = add(multiply(b01, b23), scale(multiply(b02, b13), -1), multiply(b03, b12))
    assert all(value == 0 for value in plucker)

    lambdas = []
    points = list(zip(w, u, v, strict=True))
    for omitted in range(4):
        cofactor = determinant3([points[index] for index in range(4) if index != omitted])
        lambdas.append(((-1) ** omitted * cofactor) % P)
    assert all(lambdas)
    assert sum(lambdas[i] * w[i] for i in range(4)) % P == 0
    assert sum(lambdas[i] * u[i] for i in range(4)) % P == 0
    assert sum(lambdas[i] * v[i] for i in range(4)) % P == 0

    alpha = (1, 2, 1)
    beta = (3, 0, 1)
    locators = []
    for i in range(4):
        moving = (u[i], v[i])
        locators.append(add(scale(alpha, w[i]), multiply(beta, moving)))
    relation = add(*(scale(locator, lambdas[i]) for i, locator in enumerate(locators)))
    assert all(value == 0 for value in relation)


def check_sources() -> None:
    packet = ROOT / "background" / "nodes" / NODE
    statement = (packet / "statement.md").read_text()
    proof = (packet / "proof.md").read_text()
    assert "projective line on `Gr(2,4)`" in statement
    assert "every coordinate of `lambda` is nonzero" in statement
    assert "deg E=2+6=8" in statement
    assert "No proper subsum" in proof


def check_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    for parent in (PLUCKER, ATLAS):
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    check_fixture()
    check_sources()
    check_dag()
    print(
        "RATE_HALF_LIST_BUDGET_THREE_K4_GRASSMANN_LINE_PASS "
        "edge_roots=6 annihilator_nonzero=4 exceptional_degree=8 dag=3/3"
    )


if __name__ == "__main__":
    main()
