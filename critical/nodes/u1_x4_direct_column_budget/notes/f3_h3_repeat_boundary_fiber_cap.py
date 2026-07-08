#!/usr/bin/env python3
"""Verify the repeat-boundary line fiber-cap ledger."""

from __future__ import annotations

from collections import Counter

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_boundary_q0_cell import ceil_cuberoot


def line_support(p: int, n: int) -> dict[str, int]:
    hset = set(root_table(p, n))
    support = Counter()
    q0_support = Counter()
    for r in range(p):
        if r in (0, p - 1):
            continue
        inv_r1 = pow((r + 1) % p, -1, p)
        c3 = (-r * inv_r1) % p
        c4 = ((r * r + r + 1) * inv_r1) % p
        for t in range(1, p):
            v = (1 + t) % p
            u = (1 + r * t) % p
            w = (1 + c3 * t) % p
            lam = (1 + c4 * t) % p
            if v not in hset or u not in hset or w not in hset or lam not in hset:
                continue
            if len({u, v, w}) != 3:
                continue
            support[r] += 1
            if (r * r + r + 1) % p == 0:
                q0_support[r] += 1

    cap = ceil_cuberoot((66**3) * (n**2))
    max_fiber = max(support.values(), default=0)
    if max_fiber > cap:
        raise AssertionError((p, n, max_fiber, cap))
    total = sum(support.values())
    q0_total = sum(q0_support.values())
    genuine_support = len(set(support) - set(q0_support))
    support_bound = 66**3 * (n**2) * max(genuine_support, 1) ** 3
    genuine_total = total - q0_total
    if genuine_support and genuine_total**3 > support_bound:
        raise AssertionError((p, n, genuine_total, genuine_support))
    return {
        "b_line": total,
        "support": len(support),
        "genuine_support": genuine_support,
        "q0_support": len(q0_support),
        "q0_total": q0_total,
        "max_fiber": max_fiber,
        "cap_int": cap,
        "genuine_total": genuine_total,
    }


def main() -> None:
    print("h=3 repeat-boundary line fiber cap")
    for p, n in ((97, 16), (97, 32), (193, 64), (257, 128)):
        row = line_support(p, n)
        print(
            f"p={p} n={n} B_line={row['b_line']} support={row['support']} "
            f"genuine_support={row['genuine_support']} q0_support={row['q0_support']} "
            f"q0_total={row['q0_total']} max_fiber={row['max_fiber']} "
            f"ceil_66_n_2over3={row['cap_int']} genuine_total={row['genuine_total']}"
        )
    print("B_line_genuine <= 66*n^(2/3)*R_genuine under the coset-pair h2 bound")
    print("H3_REPEAT_BOUNDARY_FIBER_CAP_PASS")


if __name__ == "__main__":
    main()
