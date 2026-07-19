#!/usr/bin/env python3
"""Verify the deleted-pair parity/univariate reduction and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction"
DEPENDENCY = "rate_half_list_budget_three_antipodal_generic_two_window_square_reduction"
CONSUMER = "rate_half_list_adjacent_crossing"
PACKETS = (
    (257, 128, 9, (0, 20, 64, 84), (0, 31)),
    (641, 128, 243, (0, 6, 64, 70), (0, 381)),
)


def multiply(left: list[int], right: list[int], prime: int, limit: int) -> list[int]:
    answer = [0] * min(limit, len(left) + len(right) - 1)
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            if i + j >= len(answer):
                break
            answer[i + j] = (answer[i + j] + value * other) % prime
    return answer


def fourth_root_inverse(e_poly: list[int], limit: int, prime: int) -> list[int]:
    answer = [1]
    for degree in range(1, limit):
        numerator = sum(
            (4 * degree - 3 * index) * e_poly[index] * answer[degree - index]
            for index in range(1, min(len(e_poly) - 1, degree) + 1)
        )
        answer.append(-numerator * pow(4 * degree, -1, prime) % prime)
    return answer


def reduced_coefficients(t: int, limit: int, prime: int) -> list[int]:
    answer = [1]
    for degree in range(1, limit):
        previous = answer[degree - 1]
        previous_two = answer[degree - 2] if degree >= 2 else 0
        numerator = (
            (4 * degree - 3) * (1 + t) * previous
            - (4 * degree - 6) * t * previous_two
        )
        answer.append(numerator * pow(4 * degree, -1, prime) % prime)
    return answer


def square_root_one(poly: list[int], prime: int) -> list[int]:
    answer = [1]
    inverse_two = pow(2, -1, prime)
    for degree in range(1, len(poly)):
        cross = sum(answer[index] * answer[degree - index] for index in range(1, degree))
        answer.append((poly[degree] - cross) * inverse_two % prime)
    return answer


def packet_check() -> None:
    for prime, order, zeta, exponents, expected_terminal in PACKETS:
        assert pow(zeta, order, prime) == 1
        assert pow(zeta, order // 2, prime) == prime - 1
        assert {
            (exponent + order // 2) % order for exponent in exponents
        } == set(exponents)

        m_value = order // 16
        h = 2 * m_value + 1
        roots = [pow(zeta, exponent, prime) for exponent in exponents]
        e_poly = [1]
        for root in roots:
            e_poly = multiply(e_poly, [1, -root % prime], prime, 5)
        assert e_poly[1] == e_poly[3] == 0

        full = fourth_root_inverse(e_poly, 3 * h, prime)
        assert all(full[index] == 0 for index in range(1, len(full), 2))
        assert full[4 * m_value : 4 * m_value + 3][:2] == [0, 0]
        assert full[4 * m_value + 2] != 0

        u = roots[0] * roots[0] % prime
        v = roots[1] * roots[1] % prime
        assert u != v
        t = v * pow(u, -1, prime) % prime
        assert pow(t, order // 2, prime) == 1 and t != 1
        reduced = reduced_coefficients(t, 3 * m_value + 2, prime)
        assert all(
            full[2 * index] == pow(u, index, prime) * reduced[index] % prime
            for index in range(3 * m_value + 2)
        )
        assert reduced[2 * m_value] == 0
        assert reduced[2 * m_value + 1] != 0

        contact = full[2 * h]
        full_square = multiply(full[:h], full[2 * h : 3 * h], prime, h)
        full_square = [value * pow(contact, -1, prime) % prime for value in full_square]
        full_root = square_root_one(full_square, prime)
        assert all(full_root[index] == 0 for index in range(1, h, 2))
        assert tuple(full_root[h - 2 : h]) == expected_terminal

        reduced_square = multiply(
            reduced[: m_value + 1],
            reduced[2 * m_value + 1 : 3 * m_value + 2],
            prime,
            m_value + 1,
        )
        inverse_reduced_contact = pow(reduced[2 * m_value + 1], -1, prime)
        reduced_square = [
            value * inverse_reduced_contact % prime for value in reduced_square
        ]
        reduced_root = square_root_one(reduced_square, prime)
        assert all(
            full_root[2 * index]
            == pow(u, index, prime) * reduced_root[index] % prime
            for index in range(m_value + 1)
        )
        assert reduced_root[m_value] == expected_terminal[1]

    ordinary = {0, 5, 87, 93}
    assert {(value + 64) % 128 for value in ordinary} != ordinary


def wiring_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "Every odd coefficient",
        "[w^M]C_0=0",
        "t^(8M)=1",
        "F_(2M)(t)=0",
        "neither proves",
    ):
        assert marker in statement


def main() -> None:
    packet_check()
    wiring_check()
    print(
        "RATE_HALF_ANTIPODAL_GENERIC_DELETED_PAIR_PARITY_PASS "
        "packets=2 automatic_primary=1 automatic_secondary=1 variables=1"
    )


if __name__ == "__main__":
    main()
