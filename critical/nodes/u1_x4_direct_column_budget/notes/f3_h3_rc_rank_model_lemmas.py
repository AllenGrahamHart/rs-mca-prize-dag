#!/usr/bin/env python3
"""Arithmetic model lemmas for the h=3 RC-RANK theorem statement."""

from __future__ import annotations


A = 5
B = 4
D = 1
C_RED = 13
CONDITIONS = C_RED * D * (A + D)
COEFFS = A * B**3
PINNED_PRIVATE_RANKS = {
    4: 41,
    8: 77,
    16: 149,
    32: 293,
    64: 320,
}


def interval_union_size(a_count: int, step: int, s_max: int) -> int:
    values = {
        a + step * s
        for a in range(a_count)
        for s in range(s_max + 1)
    }
    return len(values)


def collapsed_rank(a_count: int, b_count: int, h_order: int) -> int:
    return interval_union_size(a_count, h_order, 3 * (b_count - 1))


def private_linear_degree_dim(a_count: int, b_count: int, h_order: int) -> int:
    return a_count + 3 * h_order * (b_count - 1)


def rank_capacity(rank: int) -> int:
    if rank <= CONDITIONS:
        return 0
    return (rank - 1) // CONDITIONS


def one_curve_h_floor(a_count: int, b_count: int, condition_count: int) -> int:
    h_order = 1
    while private_linear_degree_dim(a_count, b_count, h_order) <= condition_count:
        h_order += 1
    return h_order


def main() -> None:
    print("h=3 RC-RANK model lemmas")
    print(f"A={A} B={B} D={D} coeffs={COEFFS} conditions={CONDITIONS}")

    collapsed = collapsed_rank(A, B, 32)
    if collapsed != 50:
        raise AssertionError(("collapsed rank formula drift", collapsed))
    if rank_capacity(collapsed) != 0:
        raise AssertionError(("collapsed capacity drift", collapsed, rank_capacity(collapsed)))
    print(f"constant-ratio H=32 model rank={collapsed} capacity=0")

    h_floor = one_curve_h_floor(A, B, CONDITIONS)
    if h_floor != 9:
        raise AssertionError(("private-linear H-floor drift", h_floor))
    print(f"private-linear one-curve degree-space H-floor={h_floor}")

    for h_order, pinned_rank in PINNED_PRIVATE_RANKS.items():
        degree_dim = private_linear_degree_dim(A, B, h_order)
        model_rank = min(COEFFS, degree_dim)
        if pinned_rank != model_rank:
            raise AssertionError((h_order, pinned_rank, model_rank, degree_dim))
        print(
            f"H={h_order}: pinned_private_rank={pinned_rank} "
            f"degree_dim={degree_dim} capacity={rank_capacity(pinned_rank)}"
        )

    print("constant-ratio collapse has zero RC-RANK capacity in the toy box")
    print("private-linear RC-RANK needs an explicit H-floor even before lower bounds")
    print("H3_RC_RANK_MODEL_LEMMAS_PASS")


if __name__ == "__main__":
    main()
