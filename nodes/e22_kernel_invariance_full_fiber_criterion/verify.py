#!/usr/bin/env python3
"""Brute-force cyclic-group check of the kernel-invariance criterion."""

from __future__ import annotations


def all_subsets(n: int):
    for mask in range(1 << n):
        yield {i for i in range(n) if (mask >> i) & 1}


def kernel(n: int, M: int) -> set[int]:
    step = n // M
    return {(k * step) % n for k in range(M)}


def fiber(n: int, M: int, x: int) -> set[int]:
    k = kernel(n, M)
    return {(x + eta) % n for eta in k}


def is_kernel_invariant(S: set[int], n: int, M: int) -> bool:
    k = kernel(n, M)
    return all(((x + eta) % n) in S for x in S for eta in k)


def is_union_of_fibers(S: set[int], n: int, M: int) -> bool:
    return all(fiber(n, M, x) <= S for x in S)


def main() -> None:
    n = 8
    for M in (1, 2, 4, 8):
        for S in all_subsets(n):
            assert is_kernel_invariant(S, n, M) == is_union_of_fibers(S, n, M)
    print("PASS: kernel invariance is equivalent to full-fiber union")


if __name__ == "__main__":
    main()
