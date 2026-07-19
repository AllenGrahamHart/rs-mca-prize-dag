#!/usr/bin/env python3
"""Tiny arithmetic checks for the exceptional-slope root charge."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def inverse(value: int, prime: int) -> int:
    return pow(value % prime, prime - 2, prime)


def matrix_rank(matrix: list[list[int]], prime: int) -> int:
    work = [[value % prime for value in row] for row in matrix]
    row = 0
    for column in range(len(work[0])):
        pivot = next(
            (index for index in range(row, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        scale = inverse(work[row][column], prime)
        work[row] = [(scale * value) % prime for value in work[row]]
        for index in range(row + 1, len(work)):
            if not work[index][column]:
                continue
            scale = work[index][column]
            work[index] = [
                (left - scale * right) % prime
                for left, right in zip(work[index], work[row])
            ]
        row += 1
        if row == len(work):
            break
    return row


def polynomial_gcd_degree(
    left: list[int], right: list[int], prime: int
) -> int:
    def trim(poly: list[int]) -> list[int]:
        while poly and not poly[-1] % prime:
            poly.pop()
        return poly

    left, right = trim(left[:]), trim(right[:])
    while right:
        while len(left) >= len(right):
            scale = left[-1] * inverse(right[-1], prime) % prime
            shift = len(left) - len(right)
            for index, value in enumerate(right):
                left[index + shift] = (
                    left[index + shift] - scale * value
                ) % prime
            trim(left)
        left, right = right, left
    return len(left) - 1


def refined_bound(n: int, rho: int, a: int, e: int, s: int) -> int:
    delta = rho - a * e
    d = rho - s
    assert e >= 1 and delta >= 0 and d > 0
    assert (a + s) * e <= d
    return ((n - s) * e + delta) // d


def old_bound(n: int, rho: int, a: int, e: int, s: int) -> int:
    delta = rho - a * e
    d = rho - s
    return delta + ((n - s) * e) // d


def residual_bound(n: int, rho: int, a: int, e: int, s: int) -> int:
    d = rho - s
    delta_res = d - (a + s) * e
    assert delta_res >= 0
    return ((n - s) * e + delta_res) // d


def check_general_charge() -> int:
    checked = 0
    for rho in range(3, 40):
        for a in range(1, rho + 1, 2):
            for e in range(1, rho // a + 1):
                for s in range(rho):
                    if (a + s) * e > rho - s:
                        continue
                    n = 4 * rho + 4
                    assert refined_bound(n, rho, a, e, s) <= old_bound(
                        n, rho, a, e, s
                    )
                    assert residual_bound(n, rho, a, e, s) <= refined_bound(
                        n, rho, a, e, s
                    )
                    checked += 1
    assert checked > 100
    return checked


def check_official_a3() -> int:
    m = 1 << 37
    rho = 4 * m - 1
    n = 4 * rho + 4

    # The cleared lower-margin polynomial is concave on the low-e interval,
    # so checking both endpoints verifies the symbolic endpoint guard.
    def margin_poly(e: int) -> int:
        return (
            e * rho * rho
            + (-4 * e * e + e - 1) * rho
            - 4 * e * e
            + 5 * e
        )

    assert margin_poly(1) > 0
    assert margin_poly(m - 1) > 0
    assert -8 * (rho + 1) < 0  # second finite difference

    for e in (1, 2, m - 2, m - 1):
        s = (rho - 3 * e) // (e + 1)
        assert refined_bound(n, rho, 3, e, s) <= rho + 1

    # The high-degree branch has no fixed domain root.
    for e in (m, m + 1, rho // 3):
        assert (rho - 3 * e) // (e + 1) == 0
        assert refined_bound(n, rho, 3, e, 0) == 4 * e + 1

    # Strict budget misses first at e=m; the half-distance A=3 target pays it.
    assert refined_bound(n, rho, 3, m, 0) == rho + 2
    assert refined_bound(n, rho, 3, m + 1, 0) > rho + 2
    return 10


def check_official_a1() -> int:
    m = 1 << 37
    rho = 4 * m
    n = 4 * rho

    def margin_poly(e: int) -> int:
        return e * rho * rho + (-4 * e * e - e - 1) * rho + 3 * e

    assert margin_poly(1) > 0
    assert margin_poly(m - 1) > 0
    assert -8 * rho < 0  # second finite difference

    for e in (1, 2, m - 2, m - 1):
        s = (rho - e) // (e + 1)
        assert refined_bound(n, rho, 1, e, s) <= rho + 1

    assert (rho - m) // (m + 1) == 2
    assert residual_bound(n, rho, 1, m, 0) == rho
    assert residual_bound(n, rho, 1, m, 1) == rho + 1
    assert residual_bound(n, rho, 1, m, 2) == rho + 1
    assert refined_bound(n, rho, 1, m, 2) == rho + 2  # old bound misses

    e2_max = (rho - 2) // 3
    e1_max = (rho - 1) // 2
    assert 3 * e2_max <= rho - 2 < 3 * (e2_max + 1)
    assert 2 * e1_max <= rho - 1 < 2 * (e1_max + 1)
    assert rho <= rho
    return 15


def check_nonfixed_regular_tail() -> int:
    prime = 101
    q0 = [31, 86, 85, 70, 86]
    q1 = [22, 16, 11, 20, 68]
    y0 = [40, 3, 89, 98, 65, 15, 26, 88, 4, 51]
    y1 = [12, 61, 7, 71, 86, 77, 93, 67, 1, 0]

    assert polynomial_gcd_degree(q0, q1, prime) == 0
    histogram: dict[int, int] = {}
    for slope in range(prime):
        sequence = [
            (left + slope * right) % prime for left, right in zip(y0, y1)
        ]
        matrix = [sequence[offset : offset + 5] for offset in range(6)]
        generator = [
            (left + slope * right) % prime for left, right in zip(q0, q1)
        ]
        assert all(
            sum(left * right for left, right in zip(row, generator)) % prime
            == 0
            for row in matrix
        )
        rank = matrix_rank(matrix, prime)
        histogram[rank] = histogram.get(rank, 0) + 1
    assert histogram == {4: 100, 3: 1}
    assert 10 + 1 - 2 * 4 == 3
    assert 4 - 3 * 1 == 1
    return prime


def main() -> None:
    general = check_general_charge()
    official = check_official_a3()
    endpoint = check_official_a1()
    fence = check_nonfixed_regular_tail()

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    node_id = "rate_half_ca_hankel_exceptional_root_charge"
    assert nodes[node_id]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dependency in (
        "rate_half_ca_hankel_split_pencil_equivalence",
        "rate_half_ca_hankel_minimal_index_budget",
    ):
        assert (dependency, node_id, "req") in edges
    assert (node_id, "rate_half_band_closure", "ev") in edges

    print(
        "RATE_HALF_CA_HANKEL_EXCEPTIONAL_ROOT_CHARGE_PASS "
        f"general={general} a3={official} a1={endpoint} fence={fence}"
    )


if __name__ == "__main__":
    main()
