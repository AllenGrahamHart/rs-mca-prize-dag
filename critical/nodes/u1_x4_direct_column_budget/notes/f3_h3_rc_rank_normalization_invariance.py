#!/usr/bin/env python3
"""Finite-field replay for h=3 RC-RANK normalization invariance."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


P = 97
H = 4
A = 3
B = 3


@dataclass(frozen=True)
class Curve:
    ps: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]
    qs: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]


def trim(poly: list[int]) -> list[int]:
    out = [x % P for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    n = max(len(a), len(b))
    return tuple(
        trim(
            [
                ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % P
                for i in range(n)
            ]
        )
    )


def scale(a: tuple[int, ...], c: int) -> tuple[int, ...]:
    return tuple(trim([(c * x) % P for x in a]))


def mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P
    return tuple(trim(out))


def pow_poly(a: tuple[int, ...], e: int) -> tuple[int, ...]:
    out = (1,)
    base = tuple(trim(list(a)))
    while e:
        if e & 1:
            out = mul(out, base)
        base = mul(base, base)
        e //= 2
    return out


def monomial_x(a: int) -> tuple[int, ...]:
    return (0,) * a + (1,)


def linear_root(root: int) -> tuple[int, int]:
    return ((-root) % P, 1)


def compose_affine(poly: tuple[int, ...], m: int, t: int) -> tuple[int, ...]:
    base = (t % P, m % P)
    power = (1,)
    out = (0,)
    for coeff in poly:
        out = add(out, scale(power, coeff))
        power = mul(power, base)
    return tuple(trim(list(out)))


def affine_reparametrize(curve: Curve, m: int, t: int) -> Curve:
    if m % P == 0:
        raise ValueError("affine source multiplier must be nonzero")
    return Curve(
        ps=tuple(compose_affine(poly, m, t) for poly in curve.ps),
        qs=tuple(compose_affine(poly, m, t) for poly in curve.qs),
    )


def target_scale(curve: Curve, scalars: tuple[int, int, int]) -> Curve:
    if any(c % P == 0 for c in scalars):
        raise ValueError("target scalars must be nonzero")
    return Curve(
        ps=tuple(scale(poly, c) for poly, c in zip(curve.ps, scalars)),
        qs=curve.qs,
    )


def target_permute(curve: Curve, order: tuple[int, int, int]) -> Curve:
    if sorted(order) != [0, 1, 2]:
        raise ValueError("target order must be a permutation")
    return Curve(
        ps=tuple(curve.ps[i] for i in order),
        qs=tuple(curve.qs[i] for i in order),
    )


def target_invert(curve: Curve, indices: tuple[int, ...]) -> Curve:
    invert = set(indices)
    return Curve(
        ps=tuple(curve.qs[i] if i in invert else curve.ps[i] for i in range(3)),
        qs=tuple(curve.ps[i] if i in invert else curve.qs[i] for i in range(3)),
    )


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


def precompute(curve: Curve) -> tuple[list[tuple[int, ...]], list[tuple[int, ...]]]:
    p_powers = [(1,) for _ in range(3 * B)]
    q_powers = [(1,) for _ in range(3 * B)]
    for i, (poly_p, poly_q) in enumerate(zip(curve.ps, curve.qs)):
        for b in range(B):
            p_powers[i * B + b] = pow_poly(poly_p, H * b)
            q_powers[i * B + b] = pow_poly(poly_q, H * (B - 1 - b))
    return p_powers, q_powers


def substitution_rank(curve: Curve) -> int:
    degree_cap = (A - 1) + 6 * H * (B - 1)
    p_powers, q_powers = precompute(curve)
    columns: list[list[int]] = []
    for a, bs in product(range(A), product(range(B), repeat=3)):
        poly = monomial_x(a)
        for i, b_i in enumerate(bs):
            poly = mul(poly, p_powers[i * B + b_i])
            poly = mul(poly, q_powers[i * B + b_i])
        if len(poly) > degree_cap + 1:
            raise AssertionError(("degree cap exceeded", len(poly) - 1, degree_cap))
        columns.append(list(poly) + [0] * (degree_cap + 1 - len(poly)))
    return rank_columns(columns)


def main() -> None:
    private = Curve(
        ps=(linear_root(2), linear_root(5), linear_root(11)),
        qs=(linear_root(3), linear_root(7), linear_root(13)),
    )
    original_rank = substitution_rank(private)
    if original_rank != 27:
        raise AssertionError(("original rank drift", original_rank))

    cases = [
        ("source affine", affine_reparametrize(private, 2, 17)),
        ("target scaling", target_scale(private, (3, 11, 47))),
        ("target permutation", target_permute(private, (2, 0, 1))),
        ("target inversion", target_invert(private, (0, 2))),
        (
            "combined normalizations",
            target_invert(
                target_permute(
                    target_scale(affine_reparametrize(private, 5, 19), (19, 23, 29)),
                    (1, 2, 0),
                ),
                (1,),
            ),
        ),
    ]
    for name, curve in cases:
        rank = substitution_rank(curve)
        if rank != original_rank:
            raise AssertionError((name, rank, original_rank))
        print(f"{name}: rank={rank}")

    print("source/target normalizations preserve RC-RANK rank")
    print("H3_RC_RANK_NORMALIZATION_INVARIANCE_PASS")


if __name__ == "__main__":
    main()
