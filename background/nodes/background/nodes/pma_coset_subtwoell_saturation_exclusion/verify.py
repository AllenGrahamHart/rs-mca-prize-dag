#!/usr/bin/env python3
"""Verify the constant-shift-pencil rank lemma and its sharp boundaries."""

from __future__ import annotations

import itertools
import json


NODE = "pma_coset_subtwoell_saturation_exclusion"


def inv_mod(a: int, p: int) -> int:
    return pow(a % p, -1, p)


def det3(rows: list[list[int]], cols: tuple[int, int, int], p: int) -> int:
    a, b, c = ([row[j] % p for j in cols] for row in rows)
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    ) % p


def rank_at_most_two(rows: list[list[int]], p: int) -> bool:
    return all(det3(rows, cols, p) == 0 for cols in itertools.combinations(range(4), 3))


def trim(poly: list[int], p: int) -> list[int]:
    out = [x % p for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def sub(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[i] if i < len(left) else 0)
            - (right[i] if i < len(right) else 0)
            for i in range(size)
        ],
        p,
    )


def add(left: list[int], right: list[int], p: int) -> list[int]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[i] if i < len(left) else 0)
            + (right[i] if i < len(right) else 0)
            for i in range(size)
        ],
        p,
    )


def mul(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out, p)


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return trim([scalar * x for x in poly], p)


def divmod_poly(numer: list[int], denom: list[int], p: int) -> tuple[list[int], list[int]]:
    rem = trim(numer, p)
    den = trim(denom, p)
    if den == [0]:
        raise ZeroDivisionError
    quotient = [0] * max(1, len(rem) - len(den) + 1)
    lead_inv = inv_mod(den[-1], p)
    while rem != [0] and len(rem) >= len(den):
        shift = len(rem) - len(den)
        coeff = rem[-1] * lead_inv % p
        quotient[shift] = coeff
        for j, value in enumerate(den):
            rem[shift + j] = (rem[shift + j] - coeff * value) % p
        rem = trim(rem, p)
    return trim(quotient, p), rem


def gcd_poly(left: list[int], right: list[int], p: int) -> list[int]:
    a, b = trim(left, p), trim(right, p)
    while b != [0]:
        _, r = divmod_poly(a, b, p)
        a, b = b, r
    if a == [0]:
        return a
    lead_inv = inv_mod(a[-1], p)
    return scale(a, lead_inv, p)


def locator(ell: int, a: int, p: int) -> list[int]:
    out = [0] * (ell + 1)
    out[0] = -a % p
    out[ell] = 1
    return out


def divisible(poly: list[int], divisor: list[int], p: int) -> bool:
    return divmod_poly(poly, divisor, p)[1] == [0]


def run() -> dict[str, object]:
    triple_checks = 0
    rank_two_cases = 0
    for p in (3, 5, 7, 11, 13):
        for labels in itertools.combinations(range(p), 3):
            for values in itertools.product(range(p), repeat=3):
                rows = [
                    [1, a, c, a * c]
                    for a, c in zip(labels, values, strict=True)
                ]
                low_rank = rank_at_most_two(rows, p)
                constant = values[0] == values[1] == values[2]
                assert low_rank == constant
                triple_checks += 1
                rank_two_cases += int(low_rank)

    strip_checks = 0
    for ell in range(1, 65):
        for d in range(ell + 1, 2 * ell):
            for touched in range(3, 17):
                assert d < touched * ell
                strip_checks += 1

    # The two-block argument works for non-coset common pencils P-a as well.
    pencil_decompositions = 0
    for p in (3, 5, 7):
        for ell in range(2, 7):
            common = [1, 1] + [0] * (ell - 2) + [1]
            for salt in range(1, 8):
                poly = [
                    (i * i + (salt + 2) * i + salt) % p
                    for i in range(2 * ell)
                ]
                quotient, remainder = divmod_poly(poly, common, p)
                assert len(quotient) - 1 < ell
                assert len(remainder) - 1 < ell
                assert add(remainder, mul(common, quotient, p), p) == trim(poly, p)
                pencil_decompositions += 1
            for a, b in itertools.combinations(range(p), 2):
                left = common.copy()
                right = common.copy()
                left[0] = (left[0] - a) % p
                right[0] = (right[0] - b) % p
                assert gcd_poly(left, right, p) == [1]

    # Mutation 1: t=2 is false inside the strict strip.
    p = 7
    ell = 2
    f = [2, -1, -1, 1]
    w = [2, -2, -1, 2]
    assert divisible(sub(w, f, p), locator(ell, 1, p), p)
    assert divisible(sub(w, scale(f, 2, p), p), locator(ell, 2, p), p)
    assert gcd_poly(f, w, p) == [1]
    assert ell < len(trim(f, p)) - 1 < 2 * ell

    # Mutation 2: equality d=2ell is false for three petals.
    ell = 3
    f = [1] + [0] * (2 * ell - 1) + [1]
    w = [0] * ell + [1]
    endpoint_values = (4, 6, 1)
    for a, c in zip((1, 2, 3), endpoint_values, strict=True):
        assert divisible(sub(w, scale(f, c, p), p), locator(ell, a, p), p)
    assert gcd_poly(f, w, p) == [1]
    assert len(trim(f, p)) - 1 == 2 * ell

    # Mutation 3: without saturation, the constant-label branch survives.
    ell = 3
    f = [1, 0, 0, 0, 1]
    w = scale(f, 2, p)
    for a in (1, 2, 3):
        assert divisible(sub(w, scale(f, 2, p), p), locator(ell, a, p), p)
    assert gcd_poly(f, w, p) != [1]
    assert ell < len(trim(f, p)) - 1 < 2 * ell

    return {
        "node": NODE,
        "status": "PASS",
        "rank_triples_checked": triple_checks,
        "rank_two_cases": rank_two_cases,
        "strict_strip_checks": strip_checks,
        "common_pencil_decompositions": pencil_decompositions,
        "mutations_caught": 3,
    }


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True))
