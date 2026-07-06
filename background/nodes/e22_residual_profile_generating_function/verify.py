#!/usr/bin/env python3
"""Compare the residual-profile generating function with brute force."""

from __future__ import annotations

from math import comb


def blocks(n: int, size: int) -> list[frozenset[int]]:
    return [frozenset(range(start, start + size)) for start in range(0, n, size)]


def all_subsets(n: int):
    for mask in range(1 << n):
        yield frozenset(i for i in range(n) if (mask >> i) & 1)


def union(sets):
    out: set[int] = set()
    for s in sets:
        out.update(s)
    return frozenset(out)


def canonical_tail(R: frozenset[int], n: int, size: int) -> frozenset[int]:
    full = [block for block in blocks(n, size) if block <= R]
    return R - union(full)


def convolve(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i + j] += av * bv
    return out


def tail_coeff(unselected_fibers: int, fine_size: int, tail_size: int) -> int:
    base = [comb(fine_size, a) for a in range(fine_size)]
    poly = [1]
    for _ in range(unselected_fibers):
        poly = convolve(poly, base)
    return poly[tail_size] if tail_size < len(poly) else 0


def parent_profile_counts(parent_count: int, q: int) -> dict[tuple[int, int], int]:
    # (complete parents, residual selected fine fibers) -> count
    poly: dict[tuple[int, int], int] = {(0, 0): 1}
    options = [(1, 0, 1)] + [(0, s, comb(q, s)) for s in range(q)]
    for _ in range(parent_count):
        nxt: dict[tuple[int, int], int] = {}
        for (c0, r0), count0 in poly.items():
            for dc, dr, ways in options:
                key = (c0 + dc, r0 + dr)
                nxt[key] = nxt.get(key, 0) + count0 * ways
        poly = nxt
    return poly


def formula_count(n: int, fine_size: int, coarse_size: int) -> int:
    parent_count = n // coarse_size
    q = coarse_size // fine_size
    fine_count = n // fine_size
    total = 0
    for (complete, residual), selected_ways in parent_profile_counts(
        parent_count, q
    ).items():
        selected_fine = complete * q + residual
        unselected = fine_count - selected_fine
        tail_limit = min(fine_size, coarse_size - fine_size * residual)
        for tail_size in range(max(0, tail_limit)):
            total += selected_ways * tail_coeff(unselected, fine_size, tail_size)
    return total


def brute_count(n: int, fine_size: int, coarse_size: int) -> int:
    total = 0
    for R in all_subsets(n):
        fine_tail = canonical_tail(R, n, fine_size)
        if len(fine_tail) >= fine_size:
            continue
        coarse_tail = canonical_tail(R, n, coarse_size)
        if len(coarse_tail) < coarse_size:
            total += 1
    return total


def main() -> None:
    n = 8
    for fine_size in (1, 2, 4):
        for coarse_size in (2, 4, 8):
            if fine_size < coarse_size and coarse_size % fine_size == 0:
                assert formula_count(n, fine_size, coarse_size) == brute_count(
                    n, fine_size, coarse_size
                )
    print("PASS: residual-profile generating function matches brute force")


if __name__ == "__main__":
    main()
