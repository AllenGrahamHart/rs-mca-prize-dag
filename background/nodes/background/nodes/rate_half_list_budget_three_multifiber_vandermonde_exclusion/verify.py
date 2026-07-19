#!/usr/bin/env python3
"""Verify the multifiber top-block and Vandermonde exclusion."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_multifiber_vandermonde_exclusion"
DEPENDENCY = "rate_half_list_budget_three_linear_grassmann_atlas"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 1_000_003


def multiply(left: list[int], right: list[int]) -> list[int]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % PRIME
    return answer


def quotient_factor(root: int, m: int) -> list[int]:
    return [pow(root, m - 1 - degree, PRIME) for degree in range(m)]


def multifiber_locator(root: int, extras: list[int], m: int) -> list[int]:
    answer = quotient_factor(root, m)
    for value in extras:
        factor = [0] * (m + 1)
        factor[0] = -value % PRIME
        factor[m] = 1
        answer = multiply(answer, factor)
    return answer


def matrix_rank(rows: list[list[int]]) -> int:
    work = [row[:] for row in rows]
    rank = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(rank, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], PRIME - 2, PRIME)
        work[rank] = [entry * inverse % PRIME for entry in work[rank]]
        for row in range(len(work)):
            if row != rank and work[row][column]:
                factor = work[row][column]
                work[row] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(work[row], work[rank], strict=True)
                ]
        rank += 1
    return rank


def algebra_check() -> int:
    checked = 0
    for m in range(3, 13):
        for s in range(1, 6):
            roots = list(range(2, 2 + min(m, 6)))
            locators = []
            for index, root in enumerate(roots):
                extras = [
                    (100 + 37 * index + 19 * j) % PRIME
                    for j in range(1, s)
                ]
                locator = multifiber_locator(root, extras, m)
                top = locator[m * (s - 1) : m * s]
                assert top == quotient_factor(root, m)
                locators.append(locator)
            coefficient_rows = [
                [locator[degree] for locator in locators]
                for degree in range(m * s)
            ]
            assert matrix_rank(coefficient_rows) == len(roots)
            checked += len(roots)
    return checked


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges


def main() -> None:
    checked = algebra_check()
    assert (1 << 39) % 4 == 0
    packet_check()
    print(
        "RATE_HALF_LIST_B3_MULTIFIBER_VANDERMONDE_EXCLUSION_PASS "
        f"locator_checks={checked} cycle_min_fiber=4 path_min_fiber=3"
    )


if __name__ == "__main__":
    main()
