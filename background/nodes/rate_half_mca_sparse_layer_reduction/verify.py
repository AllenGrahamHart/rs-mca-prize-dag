#!/usr/bin/env python3
"""Exhaustive tiny-row replay of the exact MCA sparsification identity."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def evaluate(poly: tuple[int, ...], x: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % prime
    return value


def rs_code(prime: int, domain: tuple[int, ...], k: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(evaluate(poly, x, prime) for x in domain)
        for poly in product(range(prime), repeat=k)
    )


def agreement(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(x == y for x, y in zip(left, right, strict=True))


def line_word(
    first: tuple[int, ...], second: tuple[int, ...], slope: int, prime: int
) -> tuple[int, ...]:
    return tuple((x + slope * y) % prime for x, y in zip(first, second, strict=True))


def common_explanation(
    first: tuple[int, ...],
    second: tuple[int, ...],
    code: tuple[tuple[int, ...], ...],
    a: int,
) -> bool:
    return any(
        sum(
            x == cx and y == cy
            for x, y, cx, cy in zip(first, second, c1, c2, strict=True)
        )
        >= a
        for c1 in code
        for c2 in code
    )


def has_failed_witness(
    first: tuple[int, ...],
    second: tuple[int, ...],
    slope: int,
    prime: int,
    code: tuple[tuple[int, ...], ...],
    a: int,
) -> bool:
    word = line_word(first, second, slope, prime)
    n = len(word)
    for candidate in code:
        matches = tuple(i for i in range(n) if word[i] == candidate[i])
        if len(matches) < a:
            continue
        for support in product((False, True), repeat=len(matches)):
            chosen = tuple(matches[i] for i, keep in enumerate(support) if keep)
            if len(chosen) < a:
                continue
            extends = any(
                all(first[i] == c1[i] and second[i] == c2[i] for i in chosen)
                for c1 in code
                for c2 in code
            )
            if not extends:
                return True
    return False


def replay(prime: int, n: int, k: int) -> int:
    domain = tuple(range(n))
    code = rs_code(prime, domain, k)
    words = tuple(product(range(prime), repeat=n))
    zero = (0,) * n
    checks = 0

    for a in range(1, n + 1):
        r = n - a
        b_mca = 0
        b_far = 0
        b_sparse = 0
        for first in words:
            for second in words:
                bad = sum(
                    has_failed_witness(first, second, slope, prime, code, a)
                    for slope in range(prime)
                )
                b_mca = max(b_mca, bad)

                far = not common_explanation(first, second, code, a)
                if far:
                    close_slopes = sum(
                        max(agreement(line_word(first, second, slope, prime), c) for c in code)
                        >= a
                        for slope in range(prime)
                    )
                    assert close_slopes == bad
                    b_far = max(b_far, close_slopes)

                support = sum(x != z or y != z for x, y, z in zip(first, second, zero, strict=True))
                if support <= r:
                    b_sparse = max(b_sparse, bad)

        assert b_mca == max(b_far, b_sparse), (prime, n, k, a, b_mca, b_far, b_sparse)
        checks += 1
    return checks


def main() -> None:
    checks = replay(3, 3, 1) + replay(3, 3, 2)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_sparse_layer_reduction"]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert (
        "rate_half_mca_sparse_layer_reduction",
        "rate_half_band_closure",
        "ev",
    ) in edges

    print(f"RATE_HALF_MCA_SPARSE_LAYER_REDUCTION_PASS agreements={checks} rows=2")


if __name__ == "__main__":
    main()
