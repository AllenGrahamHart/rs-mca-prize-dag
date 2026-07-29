#!/usr/bin/env python3
"""Shard the profile-(2,10), m=1028, energy-four norm screen on Modal."""

from __future__ import annotations

from hashlib import sha256
from itertools import combinations, product
import json
from math import comb
from pathlib import Path

import modal


app = modal.App("e1-profile210-m1028-e4-norm")
image = modal.Image.debian_slim()
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
P_MAX = (B_PRIZE + 1) * 2**128 - 1
COFACTOR = 1028


def polynomial_add(
    first: list[int], second: list[int], multiplier: int = 1
) -> list[int]:
    result = [0] * max(len(first), len(second))
    for index in range(len(result)):
        result[index] = (
            (first[index] if index < len(first) else 0)
            + multiplier * (second[index] if index < len(second) else 0)
        )
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def chebyshev_polynomials(limit: int) -> list[list[int]]:
    polynomials = [[2], [0, 1]]
    for _ in range(2, limit + 1):
        polynomials.append(
            polynomial_add([0] + polynomials[-1], polynomials[-2], -1)
        )
    return polynomials


def multiplication_norm(modulus: list[int], value: list[int]) -> int:
    degree = len(modulus) - 1
    matrix = [[0] * degree for _ in range(degree)]
    for column in range(degree):
        reduced = [0] * column + value[:]
        for top in range(len(reduced) - 1, degree - 1, -1):
            coefficient = reduced[top]
            if coefficient:
                shift = top - degree
                for index, entry in enumerate(modulus):
                    reduced[index + shift] -= coefficient * entry
        for row in range(degree):
            matrix[row][column] = reduced[row] if row < len(reduced) else 0

    previous = 1
    determinant_sign = 1
    for pivot_index in range(degree - 1):
        if matrix[pivot_index][pivot_index] == 0:
            swap = next(
                row
                for row in range(pivot_index + 1, degree)
                if matrix[row][pivot_index]
            )
            matrix[pivot_index], matrix[swap] = matrix[swap], matrix[pivot_index]
            determinant_sign *= -1
        pivot = matrix[pivot_index][pivot_index]
        for row in range(pivot_index + 1, degree):
            for column in range(pivot_index + 1, degree):
                numerator = (
                    matrix[row][column] * pivot
                    - matrix[row][pivot_index] * matrix[pivot_index][column]
                )
                if numerator % previous:
                    raise RuntimeError("non-exact Bareiss division")
                matrix[row][column] = numerator // previous
            matrix[row][pivot_index] = 0
        previous = pivot
    return determinant_sign * matrix[-1][-1]


def autocorrelation_multiplicity(lags: tuple[int, ...]) -> int:
    exponents = []
    for lag in lags:
        exponents.extend((lag, 128 - lag))
    return next(
        (
            derivative
            for derivative in range(16)
            if sum(comb(exponent, derivative) for exponent in exponents) % 2
        ),
        16,
    )


@app.function(image=image, cpu=1.0, memory=1024, timeout=60, max_containers=60)
def certify_first_lag(first: int) -> dict[str, object]:
    chebyshev = chebyshev_polynomials(64)
    root = 3
    rational_prime = 257
    traces = [0] + [
        (
            pow(root, lag, rational_prime)
            + pow(pow(root, lag, rational_prime), -1, rational_prime)
        )
        % rational_prime
        for lag in range(1, 64)
    ]
    rows = []
    below = inside = above = 0
    minimum = None
    maximum = None
    supports = 0
    for tail in combinations(range(first + 1, 64), 3):
        lags = (first,) + tail
        if autocorrelation_multiplicity(lags) != 4:
            continue
        supports += 1
        for signs in product((-1, 1), repeat=4):
            if (
                18 + sum(sign * traces[lag] for sign, lag in zip(signs, lags))
            ) % rational_prime:
                continue
            value = [18]
            for sign, lag in zip(signs, lags):
                value = polynomial_add(value, chebyshev[lag], sign)
            norm = abs(multiplication_norm(chebyshev[64], value))
            if norm % COFACTOR:
                raise RuntimeError(f"cofactor divisibility failed: {lags}, {signs}")
            quotient = norm // COFACTOR
            if quotient < P_MIN:
                below += 1
            elif quotient <= P_MAX:
                inside += 1
            else:
                above += 1
            minimum = quotient if minimum is None else min(minimum, quotient)
            maximum = quotient if maximum is None else max(maximum, quotient)
            rows.append(
                ",".join(map(str, lags + signs)) + f":{quotient}"
            )

    return {
        "first": first,
        "supports": supports,
        "hits": len(rows),
        "below": below,
        "inside": inside,
        "above": above,
        "minimum": minimum,
        "maximum": maximum,
        "digest": sha256("\n".join(rows).encode("ascii")).hexdigest(),
    }


@app.local_entrypoint()
def main(
    output: str = "experiments/prize_resolution/e1_profile210_m1028_e4_norm_result.json",
) -> None:
    output_path = Path(output)
    rows = []
    for row in certify_first_lag.map(range(1, 61), order_outputs=False):
        rows.append(row)
        rows.sort(key=lambda item: int(item["first"]))
        checkpoint = {
            "schema": "e1-profile210-m1028-e4-norm-result-v1",
            "complete": len(rows) == 60,
            "completed_shards": len(rows),
            "expected_shards": 60,
            "rows": rows,
        }
        output_path.write_text(json.dumps(checkpoint, indent=2, sort_keys=True) + "\n")
        print(
            f"first={row['first']} hits={row['hits']} below={row['below']} "
            f"inside={row['inside']} above={row['above']}"
        )

    totals = {
        key: sum(int(row[key]) for row in rows)
        for key in ("supports", "hits", "below", "inside", "above")
    }
    if totals["hits"] != 8385:
        raise RuntimeError(f"target census drift: {totals}")
    if totals["inside"] or totals["above"]:
        raise RuntimeError(f"energy-four branch not excluded: {totals}")
    print(
        "E1_PROFILE210_M1028_E4_NORM_MODAL_PASS "
        f"shards={len(rows)} hits={totals['hits']} below={totals['below']}"
    )
