#!/usr/bin/env python3
"""Independent finite audit of the intersection-to-codegree argument."""

from itertools import combinations


def compatible(left, right):
    return len(set(left) & set(right)) <= 1


def maximum_family(universe: int, width: int) -> int:
    blocks = tuple(combinations(range(universe), width))
    neighbours = [set() for _ in blocks]
    for i, left in enumerate(blocks):
        for j in range(i + 1, len(blocks)):
            if compatible(left, blocks[j]):
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
        kept = [item for item in candidates[:-1] if item in neighbours[vertex]]
        search(kept, size + 1)

    search(list(range(len(blocks))), 0)
    return best


def main() -> None:
    # The Fano lines attain the Johnson bound v(e-1)/(e^2-v)=7.
    maximum = maximum_family(7, 3)
    assert maximum == 7

    n = 1 << 41
    e = (1 << 31) + 2
    assert n * (e - 1) // (e * e - n) == 1024
    print(
        "X4_LINEAR_DIFFERENCE_PROJECTION_CODEGREE_AUDIT_PASS "
        f"fano_max={maximum} official_codegree=1024"
    )


if __name__ == "__main__":
    main()
