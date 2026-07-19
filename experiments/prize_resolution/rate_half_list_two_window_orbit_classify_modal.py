#!/usr/bin/env python3
"""Classify primary-gap packets modulo common subgroup scaling."""

from __future__ import annotations

from itertools import combinations
import json
import time

import modal


app = modal.App("rate-half-list-two-window-orbits")
image = modal.Image.debian_slim(python_version="3.12")


def primitive_root(prime: int) -> int:
    factors: list[int] = []
    value = prime - 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return next(
        candidate
        for candidate in range(2, prime)
        if all(pow(candidate, (prime - 1) // factor, prime) != 1 for factor in factors)
    )


def coefficients(
    roots: list[int], exponents: tuple[int, int, int, int], limit: int, prime: int
) -> list[int]:
    selected = [roots[index] for index in exponents]
    b0, b1, b2, b3 = selected
    eta = [
        1,
        -(b0 + b1 + b2 + b3) % prime,
        (
            b0 * b1 + b0 * b2 + b0 * b3
            + b1 * b2 + b1 * b3 + b2 * b3
        )
        % prime,
        -(
            b0 * b1 * b2 + b0 * b1 * b3
            + b0 * b2 * b3 + b1 * b2 * b3
        )
        % prime,
        b0 * b1 * b2 * b3 % prime,
    ]
    answer = [1]
    for degree in range(1, limit):
        numerator = sum(
            (4 * degree - 3 * index) * eta[index] * answer[degree - index]
            for index in range(1, min(4, degree) + 1)
        )
        answer.append(-numerator * pow(4 * degree, -1, prime) % prime)
    return answer


def canonical(exponents: tuple[int, int, int, int], order: int) -> tuple[int, int, int, int]:
    return min(
        tuple(sorted((exponent + shift) % order for exponent in exponents))
        for shift in range(order)
    )


def orbit_size(exponents: tuple[int, int, int, int], order: int) -> int:
    return len(
        {
            tuple(sorted((exponent + shift) % order for exponent in exponents))
            for shift in range(order)
        }
    )


def terminal_pair(
    roots: list[int], exponents: tuple[int, int, int, int], order: int, prime: int
) -> tuple[int, int]:
    h = order // 8 + 1
    contact = 2 * h
    values = coefficients(roots, exponents, 3 * h, prime)
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


@app.function(image=image, cpu=1, memory=512, timeout=60)
def classify(task: tuple[int, int]) -> dict[str, object]:
    order, prime = task
    generator = primitive_root(prime)
    zeta = pow(generator, (prime - 1) // order, prime)
    roots = [pow(zeta, exponent, prime) for exponent in range(order)]
    h = order // 8 + 1
    first = 2 * h - 2
    representatives: set[tuple[int, int, int, int]] = set()
    anchored_primary = 0
    processed = 0
    started = time.monotonic()
    for tail in combinations(range(1, order), 3):
        exponents = (0, *tail)
        values = coefficients(roots, exponents, 2 * h + 1, prime)
        processed += 1
        if values[first] == values[first + 1] == 0 and values[first + 2] != 0:
            anchored_primary += 1
            representatives.add(canonical(exponents, order))

    rows = []
    for representative in sorted(representatives):
        rows.append(
            {
                "representative": list(representative),
                "orbit_size": orbit_size(representative, order),
                "terminal": list(terminal_pair(roots, representative, order, prime)),
            }
        )
    return {
        "order": order,
        "prime": prime,
        "zeta": zeta,
        "processed": processed,
        "anchored_primary": anchored_primary,
        "full_primary": sum(row["orbit_size"] for row in rows),
        "orbits": rows,
        "seconds": time.monotonic() - started,
    }


@app.local_entrypoint()
def main() -> None:
    results = list(classify.map([(64, 193), (128, 257), (128, 641)]))
    results.sort(key=lambda row: (int(row["order"]), int(row["prime"])))
    assert results[0]["full_primary"] == 64
    assert results[0]["orbits"] == [
        {"representative": [0, 1, 3, 62], "orbit_size": 64, "terminal": [102, 24]}
    ]
    assert all(int(row["full_primary"]) == 192 for row in results[1:])
    assert all(
        all(orbit["terminal"] != [0, 0] for orbit in row["orbits"])
        for row in results
    )
    print(json.dumps({"results": results}, indent=2, sort_keys=True))
    print(
        "RATE_HALF_LIST_TWO_WINDOW_ORBIT_CLASSIFY "
        f"orbits={sum(len(row['orbits']) for row in results)} "
        "simultaneous=0"
    )
