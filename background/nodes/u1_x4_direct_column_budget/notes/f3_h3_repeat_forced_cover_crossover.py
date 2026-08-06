#!/usr/bin/env python3
"""Official-row crossover table for forced-coordinate covers."""

from __future__ import annotations


def ceil_sqrt(n: int) -> int:
    lo = 0
    hi = 1
    while hi * hi < n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid * mid >= n:
            hi = mid
        else:
            lo = mid
    return hi


def ceil_cuberoot(n: int) -> int:
    lo = 0
    hi = 1
    while hi**3 < n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**3 >= n:
            hi = mid
        else:
            lo = mid
    return hi


def residue_bound(n: int, forced_size: int) -> int:
    return (72 * forced_size + 18) * n * n


def first_official(forced_size_fn) -> int | None:
    for s in range(13, 42):
        n = 2**s
        if residue_bound(n, forced_size_fn(n)) < n**3:
            return s
    return None


def main() -> None:
    print("h=3 repeat forced-cover crossover")
    fixed_sizes = (1, 8, 64, 128, 1024, 8192)
    for forced in fixed_sizes:
        first_s = first_official(lambda _n, forced=forced: forced)
        coverage = "none" if first_s is None else f"2^{first_s}..2^41"
        threshold = 72 * forced + 18
        print(
            f"fixed_F={forced:5d} threshold_n>{threshold:8d} "
            f"first_official={first_s} coverage={coverage}"
        )

    profiles = (
        ("ceil_sqrt_n", ceil_sqrt),
        ("ceil_n_2over3", lambda n: ceil_cuberoot(n * n)),
        ("ceil_n_over_128", lambda n: (n + 127) // 128),
        ("ceil_n_over_256", lambda n: (n + 255) // 256),
    )
    for label, fn in profiles:
        first_s = first_official(fn)
        coverage = "none" if first_s is None else f"2^{first_s}..2^41"
        print(f"{label:16s} first_official={first_s} coverage={coverage}")

    # Guard the concrete n=256 evidence row: F=1 gives a tiny quadratic payment.
    n = 256
    forced = 1
    bound = residue_bound(n, forced)
    if bound >= n**3:
        raise AssertionError((n, forced, bound, n**3))
    print(f"n=256 fixed_F=1 residue_bound={bound} n^3={n**3}")
    print("H3_REPEAT_FORCED_COVER_CROSSOVER_PASS")


if __name__ == "__main__":
    main()
