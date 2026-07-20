#!/usr/bin/env python3
"""Replay the split squarefree gap-only parity counterexample."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NODE_ID = "rate_half_list_budget_three_fiber_two_cycle_c2_gap_only_parity_counterexample"
DEPENDENCY = "rate_half_list_budget_three_antipodal_generic_two_window_square_reduction"
CONSUMER = "rate_half_list_adjacent_crossing"
PRIME = 53
HEIGHT = 8
E = (1, 1, 11, 34, 43)
EXPECTED_ROOTS = (2, 24, 46, 48)
EXPECTED_C = (1, 22, 49, 3, 16, 0, 0, 0)


def coefficients(poly: tuple[int, ...] = E) -> list[int]:
    out = [1]
    for n in range(1, 3 * HEIGHT):
        value = sum(
            (4 * n - 3 * j) * poly[j] * out[n - j]
            for j in range(1, min(4, n) + 1)
        )
        out.append(-value * pow(4 * n, -1, PRIME) % PRIME)
    return out


def multiply_truncated(left: list[int], right: list[int]) -> list[int]:
    out = [0] * HEIGHT
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j >= HEIGHT:
                break
            out[i + j] = (out[i + j] + a * b) % PRIME
    return out


def evaluate(poly: tuple[int, ...], value: int) -> int:
    return sum(coefficient * pow(value, index, PRIME) for index, coefficient in enumerate(poly)) % PRIME


def order(value: int) -> int:
    for exponent in range(1, PRIME):
        if pow(value, exponent, PRIME) == 1:
            return exponent
    raise AssertionError("nonzero field element has no order")


def check_wiring() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge.get("kind") == "req"
    }
    outgoing = {
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "ev"
    }
    assert nodes[NODE_ID]["status"] == "PROVED"
    assert incoming == {DEPENDENCY}
    assert CONSUMER in outgoing


def main() -> None:
    check_wiring()
    a = coefficients()
    assert a == [
        1, 13, 9, 6, 14, 27, 50, 39, 27, 20, 16, 11,
        19, 0, 0, 0, 2, 9, 22, 23, 46, 31, 11, 11,
    ]
    assert (a[14], a[15], a[16]) == (0, 0, 2)

    low = a[:HEIGHT]
    high = a[2 * HEIGHT : 3 * HEIGHT]
    normalized = [
        value * pow(a[2 * HEIGHT], -1, PRIME) % PRIME
        for value in multiply_truncated(low, high)
    ]
    square = multiply_truncated(list(EXPECTED_C), list(EXPECTED_C))
    assert normalized == [1, 44, 52, 42, 21, 44, 40, 43]
    assert normalized == square
    assert EXPECTED_C[HEIGHT - 2 :] == (0, 0)

    roots = tuple(value for value in range(PRIME) if evaluate(E, value) == 0)
    assert roots == EXPECTED_ROOTS
    assert all(
        sum(index * E[index] * pow(root, index - 1, PRIME) for index in range(1, 5)) % PRIME
        for root in roots
    )
    assert all((-root) % PRIME not in roots for root in roots)
    assert E[1] and E[3]
    assert tuple(order(root) for root in roots) == (52, 13, 13, 52)
    assert tuple(pow(root, (PRIME - 1) // 2, PRIME) for root in roots) == (52, 1, 1, 52)
    assert all(pow(root, 8 * HEIGHT - 8, PRIME) != 1 for root in (2, 48))

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C2_GAP_ONLY_PARITY_COUNTEREXAMPLE_PASS "
        "primary=(0,0,2) square_degree=4 roots=4 official_torsion=false wiring=2"
    )


if __name__ == "__main__":
    main()
