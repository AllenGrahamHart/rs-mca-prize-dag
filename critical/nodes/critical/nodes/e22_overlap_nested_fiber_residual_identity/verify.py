#!/usr/bin/env python3
"""Tiny brute-force check for the nested-fiber residual identity."""

from __future__ import annotations


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


def parent_index(block: frozenset[int], coarse_size: int) -> int:
    return min(block) // coarse_size


def check_pair(n: int, fine_size: int, coarse_size: int) -> None:
    fine_blocks = blocks(n, fine_size)
    coarse_blocks = blocks(n, coarse_size)
    fine_children = {
        c_idx: [block for block in fine_blocks if block <= coarse]
        for c_idx, coarse in enumerate(coarse_blocks)
    }

    for R in all_subsets(n):
        selected_fine = [block for block in fine_blocks if block <= R]
        selected_set = set(selected_fine)
        fine_tail = canonical_tail(R, n, fine_size)

        coarse_full_from_R = {
            c_idx for c_idx, coarse in enumerate(coarse_blocks) if coarse <= R
        }
        coarse_full_from_children = {
            c_idx
            for c_idx, children in fine_children.items()
            if all(child in selected_set for child in children)
        }
        assert coarse_full_from_R == coarse_full_from_children

        residual_fine = [
            block
            for block in selected_fine
            if parent_index(block, coarse_size) not in coarse_full_from_children
        ]
        coarse_tail = canonical_tail(R, n, coarse_size)
        residual_size = len(fine_tail) + fine_size * len(residual_fine)

        assert len(coarse_tail) == residual_size
        assert (len(coarse_tail) < coarse_size) == (residual_size < coarse_size)


def main() -> None:
    n = 8
    for fine_size in (1, 2, 4):
        for coarse_size in (2, 4, 8):
            if fine_size < coarse_size and coarse_size % fine_size == 0:
                check_pair(n, fine_size, coarse_size)
    print("PASS: nested dyadic fiber residual identity")


if __name__ == "__main__":
    main()
