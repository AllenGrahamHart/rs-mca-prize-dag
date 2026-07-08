#!/usr/bin/env python3
"""Exact checks for the h=3 rich-curve denominator-clearing compiler."""

from __future__ import annotations

import random
from itertools import product


def trim(poly: list[int], p: int) -> list[int]:
    out = [x % p for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(out, p)


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return trim(out, p)


def pow_poly(a: list[int], e: int, p: int) -> list[int]:
    out = [1]
    base = trim(a, p)
    while e:
        if e & 1:
            out = mul(out, base, p)
        base = mul(base, base, p)
        e //= 2
    return out


def monomial_x(a: int) -> list[int]:
    return [0] * a + [1]


def eval_poly(poly: list[int], x: int, p: int) -> int:
    acc = 0
    for coeff in reversed(poly):
        acc = (acc * x + coeff) % p
    return acc


def degree(poly: list[int]) -> int:
    return len(poly) - 1 if poly else -1


def random_quad(rng: random.Random, p: int) -> list[int]:
    poly = [rng.randrange(p) for _ in range(3)]
    if poly == [0, 0, 0]:
        poly[0] = 1
    return trim(poly, p)


def build_cleared(
    terms: dict[tuple[int, int, int, int], int],
    ps: list[list[int]],
    qs: list[list[int]],
    h: int,
    bmax: int,
    p: int,
) -> list[int]:
    cleared = [0]
    for (a, b1, b2, b3), coeff in terms.items():
        term = [(coeff % p)]
        term = mul(term, monomial_x(a), p)
        for poly_p, poly_q, b in zip(ps, qs, (b1, b2, b3)):
            term = mul(term, pow_poly(poly_p, h * b, p), p)
            term = mul(term, pow_poly(poly_q, h * (bmax - 1 - b), p), p)
        cleared = add(cleared, term, p)
    return cleared


def eval_phi_rational(
    terms: dict[tuple[int, int, int, int], int],
    ps: list[list[int]],
    qs: list[list[int]],
    x: int,
    h: int,
    p: int,
) -> tuple[int, int]:
    qs_x = [eval_poly(q, x, p) for q in qs]
    if any(qx == 0 for qx in qs_x):
        raise ZeroDivisionError
    rs = [
        eval_poly(poly_p, x, p) * pow(qx, -1, p) % p
        for poly_p, qx in zip(ps, qs_x)
    ]
    ys = [pow(r, h, p) for r in rs]
    value = 0
    for (a, b1, b2, b3), coeff in terms.items():
        item = coeff * pow(x, a, p)
        for y, b in zip(ys, (b1, b2, b3)):
            item = item * pow(y, b, p) % p
        value = (value + item) % p
    return value, qs_x[0] * qs_x[1] % p * qs_x[2] % p


def run_case(p: int, h: int, amax: int, bmax: int, seed: int) -> None:
    rng = random.Random(seed)
    ps = [random_quad(rng, p) for _ in range(3)]
    qs = [random_quad(rng, p) for _ in range(3)]
    terms = {}
    for key in product(range(amax), range(bmax), range(bmax), range(bmax)):
        coeff = rng.randrange(p)
        if coeff:
            terms[key] = coeff
    if not terms:
        raise AssertionError("empty Phi")

    cleared = build_cleared(terms, ps, qs, h, bmax, p)
    degree_bound = (amax - 1) + 6 * h * (bmax - 1)
    if degree(cleared) > degree_bound:
        raise AssertionError((p, h, amax, bmax, degree(cleared), degree_bound))

    for x in range(p):
        qs_x = [eval_poly(q, x, p) for q in qs]
        if any(qx == 0 for qx in qs_x):
            continue
        rational_value, q_product = eval_phi_rational(terms, ps, qs, x, h, p)
        clearing = pow(q_product, h * (bmax - 1), p)
        lhs = eval_poly(cleared, x, p)
        rhs = rational_value * clearing % p
        if lhs != rhs:
            raise AssertionError((p, h, amax, bmax, x, lhs, rhs))


def main() -> None:
    cases = []
    for p in (101, 257, 769):
        for h in (2, 3, 4, 5, 8):
            for amax, bmax in ((2, 2), (3, 2), (4, 3), (6, 3)):
                cases.append((p, h, amax, bmax))
    for index, case in enumerate(cases):
        run_case(*case, seed=20260708 + index)
    print(f"rich-curve denominator cases checked: {len(cases)}")
    print("degree bound: deg <= (A-1) + 6*h*(B-1)")
    print("H3_RICH_CURVE_DENOMINATOR_COMPILER_PASS")


if __name__ == "__main__":
    main()
