#!/usr/bin/env python3
"""Small-H guardrail for the h=3 rich-curve RC-RANK statement."""

from __future__ import annotations

from itertools import product


P = 769
A = 5
B = 4
D = 1
C_RED = 13
CONDITIONS = C_RED * D * (A + D)
COEFFS = A * B**3
H_VALUES = (4, 8, 16, 32, 64)
EXPECTED_RANKS = {
    4: 41,
    8: 77,
    16: 149,
    32: 293,
    64: 320,
}


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


def linear_root(root: int) -> list[int]:
    return [(-root) % P, 1]


def substitution_rank(h_order: int) -> int:
    ps = (linear_root(2), linear_root(5), linear_root(11))
    qs = (linear_root(3), linear_root(7), linear_root(13))
    degree_cap = (A - 1) + 6 * h_order * (B - 1)

    p_powers = [[1] for _ in range(3 * B)]
    q_powers = [[1] for _ in range(3 * B)]
    for i, (poly_p, poly_q) in enumerate(zip(ps, qs)):
        for b in range(B):
            p_powers[i * B + b] = pow_poly(poly_p, h_order * b)
            q_powers[i * B + b] = pow_poly(poly_q, h_order * (B - 1 - b))

    columns: list[list[int]] = []
    for a, bs in product(range(A), product(range(B), repeat=3)):
        poly = [0] * a + [1]
        for i, b_i in enumerate(bs):
            poly = mul(poly, p_powers[i * B + b_i])
            poly = mul(poly, q_powers[i * B + b_i])
        if len(poly) > degree_cap + 1:
            raise AssertionError(("degree cap exceeded", h_order, len(poly) - 1, degree_cap))
        columns.append(poly + [0] * (degree_cap + 1 - len(poly)))
    return rank_columns(columns)


def rank_capacity(rank: int) -> int:
    if rank <= CONDITIONS:
        return 0
    return (rank - 1) // CONDITIONS


def private_linear_degree_dim(h_order: int) -> int:
    return A + 3 * h_order * (B - 1)


def main() -> None:
    print("h=3 RC-RANK small-H guardrail")
    print(f"p={P} A={A} B={B} D={D} coeffs={COEFFS} conditions={CONDITIONS}")
    print("curve=(X-2)/(X-3), (X-5)/(X-7), (X-11)/(X-13)")
    print(" H_order    rank    degree_dim    rank_deficit    rc_rank    capacity")
    seen_failure = False
    seen_pass = False
    seen_full = False
    for h_order in H_VALUES:
        rank = substitution_rank(h_order)
        if rank != EXPECTED_RANKS[h_order]:
            raise AssertionError((h_order, rank, EXPECTED_RANKS[h_order]))
        degree_dim = private_linear_degree_dim(h_order)
        if rank != min(COEFFS, degree_dim):
            raise AssertionError((h_order, rank, COEFFS, degree_dim))
        rc_rank = rank > CONDITIONS
        capacity = rank_capacity(rank)
        seen_failure |= not rc_rank
        seen_pass |= rc_rank
        seen_full |= rank == COEFFS
        print(
            f"{h_order:8d} {rank:7d} {degree_dim:13d} {COEFFS - rank:15d}"
            f" {str(rc_rank):>10s} {capacity:11d}"
        )

    if not (seen_failure and seen_pass and seen_full):
        raise AssertionError("guardrail profile drift")

    print("RC-RANK is false for tiny H in this non-collapsed toy family")
    print("RC-RANK becomes true, then full-rank, as H grows in the same family")
    print("private-linear rank equals min(coefficients, A + 3H(B-1)) in this control")
    print("future RC-RANK theorem must print an H-floor or route tiny rows to certificates")
    print("H3_RC_RANK_HFLOOR_GUARD_PASS")


if __name__ == "__main__":
    main()
