#!/usr/bin/env python3
"""Independent extremal audit of the changed-set Johnson bound."""

from itertools import combinations


def maximum_family(universe: int, block_size: int, intersection_cap: int) -> int:
    blocks = tuple(combinations(range(universe), block_size))
    neighbours = [set() for _ in blocks]
    for i, left in enumerate(blocks):
        left_set = set(left)
        for j in range(i + 1, len(blocks)):
            if len(left_set & set(blocks[j])) <= intersection_cap:
                neighbours[i].add(j)
                neighbours[j].add(i)

    best = 0

    def search(candidates, size):
        nonlocal best
        if size + len(candidates) <= best:
            return
        if not candidates:
            best = max(best, size)
            return
        vertex = candidates[-1]
        search(candidates[:-1], size)
        search([x for x in candidates[:-1] if x in neighbours[vertex]], size + 1)

    search(list(range(len(blocks))), 0)
    return best


def main() -> None:
    # N=8,e=3,d=1: six-sets intersect in at most four. Complements form a
    # matching, and the Johnson bound 8*(3-1)/(36-32)=4 is attained.
    maximum = maximum_family(8, 6, 4)
    assert maximum == 4

    n = 1 << 41
    e0 = n // 4 + 1
    denominator = 4 * e0 * e0 - n * (e0 + 1)
    assert denominator == 4
    assert n * (e0 - 1) // denominator == n * n // 16
    print(
        "X4_LOW_DIFFERENCE_JOHNSON_HIGHWIDTH_AUDIT_PASS "
        f"small_extremal={maximum} official_first_denominator={denominator}"
    )


if __name__ == "__main__":
    main()
