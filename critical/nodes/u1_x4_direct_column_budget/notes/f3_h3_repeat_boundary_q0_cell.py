#!/usr/bin/env python3
"""Verify the repeat-boundary q(r)=0 cell ledger."""

from __future__ import annotations

from f3_h3_pair_count_from_charts_compiler import root_table


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


def q0_roots(p: int) -> list[int]:
    return [r for r in range(p) if (r * r + r + 1) % p == 0]


def q0_count(p: int, n: int) -> dict[str, int]:
    hset = set(root_table(p, n))
    count = 0
    support = 0
    for r in q0_roots(p):
        if r == p - 1:
            raise AssertionError((p, r))
        inv_r1 = pow((r + 1) % p, -1, p)
        c3 = (-r * inv_r1) % p
        local = 0
        for t in range(1, p):
            v = (1 + t) % p
            u = (1 + r * t) % p
            w = (1 + c3 * t) % p
            if v in hset and u in hset and w in hset and len({u, v, w}) == 3:
                local += 1
        if local:
            support += 1
        count += local

    bound_int = ceil_cuberoot((132**3) * (n**2))
    if count > bound_int:
        raise AssertionError((p, n, count, bound_int))
    return {
        "q0_roots": len(q0_roots(p)),
        "q0_count": count,
        "q0_support": support,
        "bound_int": bound_int,
    }


def main() -> None:
    print("h=3 repeat-boundary q0 cell")
    for p, n in ((97, 16), (97, 32), (193, 64), (257, 128)):
        row = q0_count(p, n)
        print(
            f"p={p} n={n} q0_roots={row['q0_roots']} "
            f"q0_support={row['q0_support']} q0_count={row['q0_count']} "
            f"ceil_132_n_2over3={row['bound_int']}"
        )
    print("q0 cell paid by <= 132*n^(2/3) under the coset-pair h2 bound")
    print("H3_REPEAT_BOUNDARY_Q0_CELL_PASS")


if __name__ == "__main__":
    main()
