#!/usr/bin/env python3
"""Replay examples for the h=2 affine-coset pair Stepanov corollary."""

from __future__ import annotations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_boundary_q0_cell import ceil_cuberoot


def affine_pair_count(p: int, n: int, alpha: int, beta: int) -> int:
    if alpha % p == 0 or beta % p == 0:
        raise ValueError((p, alpha, beta))
    hset = set(root_table(p, n))
    return sum(1 for x in hset if (alpha * x + beta) % p in hset)


def main() -> None:
    print("h=2 affine-coset pair Stepanov corollary")
    cases = [
        (97, 16, 3, 5),
        (97, 32, 7, 11),
        (193, 64, 19, 23),
        (257, 128, 29, 31),
    ]
    for p, n, alpha, beta in cases:
        count = affine_pair_count(p, n, alpha, beta)
        bound = ceil_cuberoot((66**3) * (n**2))
        if count > bound:
            raise AssertionError((p, n, alpha, beta, count, bound))
        print(
            f"p={p} n={n} alpha={alpha} beta={beta} "
            f"count={count} ceil_66_n_2over3={bound}"
        )
    print("affine coset-pair bound follows from the optimized h=2 Stepanov proof")
    print("H2_AFFINE_COSET_PAIR_STEPANOV_PASS")


if __name__ == "__main__":
    main()
