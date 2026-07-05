#!/usr/bin/env python3
"""Small checks for the E22 lower-scale dyadic-tail formula."""

from __future__ import annotations

from itertools import combinations


def dyadic_scales(n: int) -> list[int]:
    out: list[int] = []
    m = 1
    while m <= n:
        out.append(m)
        m *= 2
    return out


def canonical_tail_size(mask: int, n: int, size: int) -> int:
    tail = 0
    block_mask = (1 << size) - 1
    for start in range(0, n, size):
        shifted = block_mask << start
        part = mask & shifted
        if part != shifted:
            tail += part.bit_count()
    return tail


def weighted_profile(mask: int, n: int) -> int:
    """A nonconstant toy multiplicity used to test weighted summation."""

    alternating = sum(1 << i for i in range(0, n, 2))
    return 1 + mask.bit_count() + 2 * (mask & alternating).bit_count() + mask % 7


def add_tail(tails: tuple[int, ...], idx: int, value: int) -> tuple[int, ...]:
    out = list(tails)
    out[idx] += value
    return tuple(out)


def dp_block(
    start: int, size: int, constrained: tuple[int, ...], index: dict[int, int]
) -> list[tuple[int, int, tuple[int, ...]]]:
    zero = (0,) * len(constrained)
    if size == 1:
        return [(0, 0, zero), (1 << start, 1, zero)]

    half = size // 2
    left = dp_block(start, half, constrained, index)
    right = dp_block(start + half, half, constrained, index)
    out: list[tuple[int, int, tuple[int, ...]]] = []
    for lm, ls, lt in left:
        for rm, rs, rt in right:
            mask = lm | rm
            support_size = ls + rs
            tails = tuple(a + b for a, b in zip(lt, rt))
            if size in index and support_size < size:
                tails = add_tail(tails, index[size], support_size)
            out.append((mask, support_size, tails))
    return out


def formula_count(n: int, mi: int, mj: int, subset: tuple[int, ...]) -> int:
    constrained = tuple(sorted({mi, mj, *subset}))
    index = {scale: idx for idx, scale in enumerate(constrained)}
    atoms = dp_block(0, n, constrained, index)
    masks = {mask for mask, _, _ in atoms}
    assert len(atoms) == 1 << n
    assert len(masks) == 1 << n
    for mask, _, tails in atoms:
        for scale, idx in index.items():
            assert tails[idx] == canonical_tail_size(mask, n, scale)

    total = 0
    for mask, _, tails in atoms:
        if tails[index[mi]] >= mi or tails[index[mj]] >= mj:
            continue
        if any(tails[index[scale]] >= scale for scale in subset):
            continue
        total += weighted_profile(mask, n)
    return total


def brute_count(n: int, mi: int, mj: int, subset: tuple[int, ...]) -> int:
    total = 0
    for mask in range(1 << n):
        if canonical_tail_size(mask, n, mi) >= mi:
            continue
        if canonical_tail_size(mask, n, mj) >= mj:
            continue
        if any(canonical_tail_size(mask, n, scale) >= scale for scale in subset):
            continue
        total += weighted_profile(mask, n)
    return total


def all_subsets(items: list[int]):
    for r in range(len(items) + 1):
        yield from combinations(items, r)


def main() -> None:
    checked = 0
    for n in (8, 16):
        scales = dyadic_scales(n)
        for mi in scales[:-1]:
            for mj in scales:
                if mi >= mj:
                    continue
                smaller = [scale for scale in scales if scale < mi]
                for subset in all_subsets(smaller):
                    assert formula_count(n, mi, mj, subset) == brute_count(
                        n, mi, mj, subset
                    )
                    checked += 1
    print(f"PASS: dyadic-tail intersection formula matches brute force in {checked} cases")


if __name__ == "__main__":
    main()
