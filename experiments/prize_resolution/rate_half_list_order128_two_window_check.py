#!/usr/bin/env python3
"""Check the pinned order-128 simultaneous two-window pilot."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


RESULT = Path(__file__).with_name("rate_half_list_order128_two_window_result.json")
EXPECTED_SHA256 = "d26d03529e890157653cd69b85396dcb3984f98e130ab29985fe99af1b5548a1"
EXPECTED_COUNTS = {
    (64, 193): 64,
    (128, 257): 192,
    (128, 641): 192,
    (128, 769): 0,
    (128, 1153): 0,
    (128, 1409): 0,
    (128, 2689): 0,
    (128, 3329): 0,
    (128, 3457): 0,
}


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    return all(value % divisor for divisor in range(2, math.isqrt(value) + 1))


def coefficients(
    roots: list[int], exponents: tuple[int, ...], limit: int, prime: int
) -> list[int]:
    selected = [roots[index] for index in exponents]
    eta = [1]
    for root in selected:
        updated = eta + [0]
        for index in range(len(eta)):
            updated[index + 1] = (updated[index + 1] - root * eta[index]) % prime
        eta = updated
    answer = [1]
    for degree in range(1, limit):
        numerator = sum(
            (4 * degree - 3 * index) * eta[index] * answer[degree - index]
            for index in range(1, min(4, degree) + 1)
        )
        answer.append(-numerator * pow(4 * degree, -1, prime) % prime)
    return answer


def terminal_pair(values: list[int], order: int, prime: int) -> tuple[int, int]:
    h = order // 8 + 1
    contact = 2 * h
    square = [0] * h
    for left in range(h):
        for right in range(h - left):
            square[left + right] = (
                square[left + right] + values[left] * values[contact + right]
            ) % prime
    inverse_contact = pow(values[contact], -1, prime)
    square = [value * inverse_contact % prime for value in square]
    root = [1]
    inverse_two = pow(2, -1, prime)
    for degree in range(1, h):
        cross = sum(root[index] * root[degree - index] for index in range(1, degree))
        root.append((square[degree] - cross) * inverse_two % prime)
    return root[h - 2], root[h - 1]


def orbit_size(exponents: tuple[int, ...], order: int) -> int:
    return len(
        {
            tuple(sorted((exponent + shift) % order for exponent in exponents))
            for shift in range(order)
        }
    )


def main() -> None:
    raw = RESULT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
    payload = json.loads(raw)
    rows = payload["exhaustive"]
    assert [(row["order"], row["prime"]) for row in rows] == list(EXPECTED_COUNTS)
    for row in rows:
        order, prime = row["order"], row["prime"]
        assert is_prime(prime) and (prime - 1) % order == 0
        assert row["complete"] is True
        assert row["processed"] == math.comb(order, 4)
        assert pow(row["zeta"], order, prime) == 1
        assert pow(row["zeta"], order // 2, prime) != 1
        assert row["primary"] == EXPECTED_COUNTS[(order, prime)]
        assert row["simultaneous"] == 0
        assert row["first_simultaneous"] == [-1, -1, -1, -1]

    for row in payload["orbits"]:
        order, prime, zeta = row["order"], row["prime"], row["zeta"]
        roots = [pow(zeta, exponent, prime) for exponent in range(order)]
        total = 0
        for representative in row["representatives"]:
            exponents = tuple(representative["exponents"])
            values = coefficients(roots, exponents, 3 * (order // 8 + 1), prime)
            h = order // 8 + 1
            assert values[2 * h - 2 : 2 * h] == [0, 0]
            assert values[2 * h] != 0
            terminal = terminal_pair(values, order, prime)
            assert terminal == tuple(representative["terminal"])
            assert terminal != (0, 0)
            assert orbit_size(exponents, order) == representative["orbit_size"]
            total += representative["orbit_size"]
        assert total == row["full_primary"]

    paired = [
        tuple(item["exponents"])
        for row in payload["orbits"]
        for item in row["representatives"]
        if item["orbit_size"] == 64 and row["order"] == 128
    ]
    assert paired == [(0, 20, 64, 84), (0, 6, 64, 70)]
    print(
        "RATE_HALF_LIST_ORDER128_TWO_WINDOW_CHECK_PASS "
        f"fields={len(rows) - 1} primary_orbits=5 simultaneous=0 "
        f"sha256={EXPECTED_SHA256}"
    )


if __name__ == "__main__":
    main()
