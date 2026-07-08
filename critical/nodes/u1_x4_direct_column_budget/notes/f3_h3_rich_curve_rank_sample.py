#!/usr/bin/env python3
"""Finite-field rank samples for the h=3 rich-curve RC-RANK target."""

from __future__ import annotations

import random
from dataclasses import dataclass
from itertools import product


P = 769
H = 32
A = 5
B = 4
D = 1
C_RED = 13
CONDITIONS_PER_CURVE = C_RED * D * (A + D)


def trim(poly: list[int]) -> list[int]:
    out = [x % P for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P
    return trim(out)


def pow_poly(a: list[int], e: int) -> list[int]:
    out = [1]
    base = trim(a)
    while e:
        if e & 1:
            out = mul(out, base)
        base = mul(base, base)
        e //= 2
    return out


def monomial_x(a: int) -> list[int]:
    return [0] * a + [1]


def rank_columns(columns: list[list[int]]) -> int:
    basis: dict[int, list[int]] = {}
    for column in columns:
        vector = [x % P for x in column]
        while True:
            pivot = None
            for index in range(len(vector) - 1, -1, -1):
                if vector[index]:
                    pivot = index
                    break
            if pivot is None:
                break
            if pivot not in basis:
                inv = pow(vector[pivot], -1, P)
                basis[pivot] = [(x * inv) % P for x in vector]
                break
            factor = vector[pivot]
            pivot_row = basis[pivot]
            vector = [(x - factor * y) % P for x, y in zip(vector, pivot_row)]
    return len(basis)


@dataclass(frozen=True)
class Curve:
    ps: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]
    qs: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]


@dataclass(frozen=True)
class Case:
    name: str
    curves: tuple[Curve, ...]
    expected_rank: int
    expect_rank_target: bool


def random_quad(rng: random.Random) -> tuple[int, ...]:
    return tuple(trim([rng.randrange(1, P), rng.randrange(P), rng.randrange(P)]))


def random_curve(seed: int) -> Curve:
    rng = random.Random(seed)
    return Curve(
        ps=(random_quad(rng), random_quad(rng), random_quad(rng)),
        qs=(random_quad(rng), random_quad(rng), random_quad(rng)),
    )


def precompute(curve: Curve) -> tuple[list[list[int]], list[list[int]]]:
    p_powers = [[1] for _ in range(3 * B)]
    q_powers = [[1] for _ in range(3 * B)]
    for i, (poly_p, poly_q) in enumerate(zip(curve.ps, curve.qs)):
        for b in range(B):
            p_powers[i * B + b] = pow_poly(list(poly_p), H * b)
            q_powers[i * B + b] = pow_poly(list(poly_q), H * (B - 1 - b))
    return p_powers, q_powers


def column_for_curve(
    p_powers: list[list[int]],
    q_powers: list[list[int]],
    a: int,
    bs: tuple[int, int, int],
    degree_cap: int,
) -> list[int]:
    poly = monomial_x(a)
    for i, b_i in enumerate(bs):
        poly = mul(poly, p_powers[i * B + b_i])
        poly = mul(poly, q_powers[i * B + b_i])
    if len(poly) > degree_cap + 1:
        raise AssertionError(("degree cap exceeded", len(poly) - 1, degree_cap))
    return poly + [0] * (degree_cap + 1 - len(poly))


def substitution_rank(curves: tuple[Curve, ...]) -> int:
    degree_cap = (A - 1) + 6 * H * (B - 1)
    cached = [precompute(curve) for curve in curves]
    columns: list[list[int]] = []
    for a, bs in product(range(A), product(range(B), repeat=3)):
        family_column: list[int] = []
        for p_powers, q_powers in cached:
            family_column.extend(column_for_curve(p_powers, q_powers, a, bs, degree_cap))
        columns.append(family_column)
    return rank_columns(columns)


def main() -> None:
    collapsed = Curve(
        ps=((0, 1), (0, 3), (0, 5)),
        qs=((1,), (1,), (1,)),
    )
    cases = [
        Case(
            name="constant-ratio collapsed control",
            curves=(collapsed,),
            expected_rank=50,
            expect_rank_target=False,
        ),
        Case(
            name="deterministic repaired random curve",
            curves=(random_curve(20260708),),
            expected_rank=320,
            expect_rank_target=True,
        ),
    ]

    coeffs = A * B**3
    print("h=3 rich-curve rank sample")
    print(f"p={P} h={H} A={A} B={B} D={D} coeffs={coeffs}")
    print(f"conditions per curve: {CONDITIONS_PER_CURVE}")
    for case in cases:
        rank = substitution_rank(case.curves)
        conditions = CONDITIONS_PER_CURVE * len(case.curves)
        passes = rank > conditions
        if rank != case.expected_rank or passes != case.expect_rank_target:
            raise AssertionError((case, rank, conditions, passes))
        print(
            f"{case.name}: curves={len(case.curves)} rank={rank} "
            f"conditions={conditions} rc_rank={passes}"
        )

    print("collapsed constant-ratio family fails the rank target")
    print("repaired random curve has full coefficient rank in this toy row")
    print("H3_RICH_CURVE_RANK_SAMPLE_PASS")


if __name__ == "__main__":
    main()
