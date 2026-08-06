#!/usr/bin/env python3
"""Refute a too-strong private-divisor full-rank criterion for h=3."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


P = 769
H = 32
A = 5
B = 4
D = 1
C_RED = 13
CONDITIONS = C_RED * D * (A + D)
COEFFS = A * B**3


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


def eval_poly(poly: tuple[int, ...] | list[int], x: int) -> int:
    acc = 0
    for coeff in reversed(poly):
        acc = (acc * x + coeff) % P
    return acc


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


def linear_root(root: int) -> tuple[int, int]:
    return ((-root) % P, 1)


def private_curve() -> Curve:
    return Curve(
        ps=(linear_root(2), linear_root(5), linear_root(11)),
        qs=(linear_root(3), linear_root(7), linear_root(13)),
    )


def collapsed_curve() -> Curve:
    return Curve(
        ps=((0, 1), (0, 3), (0, 5)),
        qs=((1,), (1,), (1,)),
    )


def is_regular_nonzero(num: tuple[int, ...], den: tuple[int, ...], x: int) -> bool:
    return eval_poly(num, x) != 0 and eval_poly(den, x) != 0


def is_zero_or_pole(num: tuple[int, ...], den: tuple[int, ...], x: int) -> bool:
    num_x = eval_poly(num, x)
    den_x = eval_poly(den, x)
    return (num_x == 0 and den_x != 0) or (num_x != 0 and den_x == 0)


def private_supports(curve: Curve) -> dict[str, int]:
    maps = [((0, 1), (1,)), *zip(curve.ps, curve.qs)]
    names = ["X", "r1", "r2", "r3"]
    supports: dict[str, int] = {}
    for index, name in enumerate(names):
        for x in range(P):
            target_num, target_den = maps[index]
            if not is_zero_or_pole(target_num, target_den, x):
                continue
            if all(
                is_regular_nonzero(num, den, x)
                for j, (num, den) in enumerate(maps)
                if j != index
            ):
                supports[name] = x
                break
    return supports


def substitution_rank(curve: Curve) -> int:
    degree_cap = (A - 1) + 6 * H * (B - 1)
    p_powers = [[1] for _ in range(3 * B)]
    q_powers = [[1] for _ in range(3 * B)]
    for i, (poly_p, poly_q) in enumerate(zip(curve.ps, curve.qs)):
        for b in range(B):
            p_powers[i * B + b] = pow_poly(list(poly_p), H * b)
            q_powers[i * B + b] = pow_poly(list(poly_q), H * (B - 1 - b))

    columns: list[list[int]] = []
    for a, bs in product(range(A), product(range(B), repeat=3)):
        poly = monomial_x(a)
        for i, b_i in enumerate(bs):
            poly = mul(poly, p_powers[i * B + b_i])
            poly = mul(poly, q_powers[i * B + b_i])
        if len(poly) > degree_cap + 1:
            raise AssertionError(("degree cap exceeded", len(poly) - 1, degree_cap))
        columns.append(poly + [0] * (degree_cap + 1 - len(poly)))
    return rank_columns(columns)


def main() -> None:
    good = private_curve()
    bad = collapsed_curve()

    supports = private_supports(good)
    if supports != {"X": 0, "r1": 2, "r2": 5, "r3": 11}:
        raise AssertionError(supports)
    if private_supports(bad):
        raise AssertionError(private_supports(bad))

    rank = substitution_rank(good)
    if rank != 293:
        raise AssertionError(rank)
    if not (CONDITIONS < rank < COEFFS):
        raise AssertionError((CONDITIONS, rank, COEFFS))

    print("h=3 private-divisor full-rank refutation")
    print(f"p={P} h={H} A={A} B={B} D={D}")
    print("private supports:", supports)
    print(f"conditions={CONDITIONS} rank={rank} coeffs={COEFFS}")
    print("private divisors do not imply full coefficient rank")
    print("toy RC-RANK still holds for this curve: conditions < rank")
    print("H3_PRIVATE_DIVISOR_FULL_RANK_REFUTATION_PASS")


if __name__ == "__main__":
    main()
