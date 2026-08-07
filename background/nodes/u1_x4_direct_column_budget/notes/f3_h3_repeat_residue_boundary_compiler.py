#!/usr/bin/env python3
"""Verify the h=3 repeat-residue boundary compiler."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations_with_replacement

from f3_h3_pair_count_from_charts_compiler import root_table


def signature(values: tuple[int, int, int], p: int) -> tuple[int, int]:
    return sum(values) % p, sum((x * x) % p for x in values) % p


def perm_count(multiset: tuple[int, int, int]) -> int:
    distinct = len(set(multiset))
    if distinct == 3:
        return 6
    if distinct == 2:
        return 3
    return 1


def double_repeat_signature(a: int, b: int, p: int) -> tuple[int, int]:
    return (2 * a + b) % p, (2 * a * a + b * b) % p


def double_involution(a: int, b: int, p: int) -> tuple[int, int]:
    inv3 = pow(3, -1, p)
    return ((a + 2 * b) * inv3) % p, ((4 * a - b) * inv3) % p


def verify_double_repeat_algebra(p: int) -> dict[str, int]:
    """Check the repeated-multiset classification over F_p, char not 2,3."""
    if p in (2, 3):
        raise AssertionError("characteristic 2 or 3 is excluded")

    buckets: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
    for a in range(p):
        for b in range(p):
            if a == b:
                continue
            c, d = double_involution(a, b, p)
            if double_repeat_signature(a, b, p) != double_repeat_signature(c, d, p):
                raise AssertionError((p, a, b, c, d, "signature"))
            if double_involution(c, d, p) != (a, b):
                raise AssertionError((p, a, b, c, d, "involution"))
            if c == d:
                raise AssertionError((p, a, b, c, d, "collapsed"))
            buckets[double_repeat_signature(a, b, p)].append((a, b))

    sizes = Counter(len(v) for v in buckets.values())
    if set(sizes) - {2}:
        raise AssertionError((p, sizes))
    for pairs in buckets.values():
        left, right = pairs
        if double_involution(*left, p) != right:
            raise AssertionError((p, left, right))

    for a in range(p):
        triple_sig = signature((a, a, a), p)
        for t in range(1, p):
            double_sig = signature((a + t, a + t, a - 2 * t), p)
            if triple_sig == double_sig:
                raise AssertionError((p, a, t))

    return {
        "double_signatures": len(buckets),
        "double_bucket_size": next(iter(sizes)),
        "triple_double_collisions": 0,
    }


def verify_row(p: int, n: int) -> dict[str, int]:
    vals = root_table(p, n)
    multiset_buckets: dict[tuple[int, int], list[tuple[tuple[int, int, int], int]]] = (
        defaultdict(list)
    )

    for idxs in combinations_with_replacement(range(n), 3):
        key = signature(tuple(vals[i] for i in idxs), p)
        multiset_buckets[key].append((idxs, perm_count(idxs)))

    repeat_residue = 0
    formula_residue = 0
    d_boundary = 0
    z_repeat = 0
    bound = 0
    max_r = 0
    max_q = 0
    r_hist = Counter()

    for entries in multiset_buckets.values():
        d_sigma = 0
        r_sigma = 0
        q_sigma = 0
        direct_bucket_residue = 0

        for idxs, weight in entries:
            if len(set(idxs)) == 3:
                d_sigma += weight
            else:
                r_sigma += weight
                q_sigma += weight * weight

        for i, (left, left_weight) in enumerate(entries):
            left_repeated = len(set(left)) < 3
            for j, (right, right_weight) in enumerate(entries):
                if i == j:
                    continue
                if left_repeated or len(set(right)) < 3:
                    direct_bucket_residue += left_weight * right_weight

        bucket_formula = 2 * d_sigma * r_sigma + r_sigma * r_sigma - q_sigma
        if direct_bucket_residue != bucket_formula:
            raise AssertionError((p, n, direct_bucket_residue, bucket_formula))

        repeat_residue += direct_bucket_residue
        formula_residue += bucket_formula
        if r_sigma:
            if r_sigma > 6:
                raise AssertionError((p, n, r_sigma, entries))
            if q_sigma > 18:
                raise AssertionError((p, n, q_sigma, entries))
            d_boundary += d_sigma
            z_repeat += 1
            bound += 12 * d_sigma + 18
            max_r = max(max_r, r_sigma)
            max_q = max(max_q, q_sigma)
            r_hist[r_sigma] += 1

    if repeat_residue != formula_residue:
        raise AssertionError((p, n, repeat_residue, formula_residue))
    if repeat_residue > 12 * d_boundary + 18 * z_repeat:
        raise AssertionError((p, n, repeat_residue, d_boundary, z_repeat))
    if bound != 12 * d_boundary + 18 * z_repeat:
        raise AssertionError((p, n, bound, d_boundary, z_repeat))

    return {
        "buckets": len(multiset_buckets),
        "repeat_residue": repeat_residue,
        "d_boundary": d_boundary,
        "z_repeat": z_repeat,
        "bound": bound,
        "max_r": max_r,
        "max_q": max_q,
        "r1": r_hist[1],
        "r3": r_hist[3],
        "r6": r_hist[6],
    }


def main() -> None:
    print("h=3 repeat-residue boundary compiler")
    for p in (17, 97):
        row = verify_double_repeat_algebra(p)
        print(
            f"p={p} double_signatures={row['double_signatures']} "
            f"bucket_size={row['double_bucket_size']} "
            f"triple_double_collisions={row['triple_double_collisions']}"
        )

    for p, n in ((97, 16), (97, 32), (193, 64)):
        row = verify_row(p, n)
        print(
            f"p={p} n={n} buckets={row['buckets']} "
            f"repeat_residue={row['repeat_residue']} "
            f"D_boundary={row['d_boundary']} Z_repeat={row['z_repeat']} "
            f"bound={row['bound']} max_R={row['max_r']} max_Q={row['max_q']} "
            f"R_hist=(1:{row['r1']},3:{row['r3']},6:{row['r6']})"
        )
    print("repeat_residue <= 12*D_boundary + 18*Z_repeat")
    print("H3_REPEAT_RESIDUE_BOUNDARY_COMPILER_PASS")


if __name__ == "__main__":
    main()
