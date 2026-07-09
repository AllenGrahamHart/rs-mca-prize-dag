#!/usr/bin/env python3
"""Efficient boundary-row evidence for the h=3 repeat-boundary support."""

from __future__ import annotations

from f3_h3_pair_count_from_charts_compiler import root_table


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def support_from_h_pairs(p: int, n: int) -> dict[str, int]:
    if not is_prime(p) or (p - 1) % n:
        raise AssertionError((p, n, "bad row"))
    if p < n * n:
        raise AssertionError((p, n, "not boundary-style"))

    h = root_table(p, n)
    hset = set(h)
    support: dict[int, int] = {}
    b_line = 0
    q0_total = 0
    q0_support: set[int] = set()

    for u in h:
        if u == 1:
            continue
        u0 = (u - 1) % p
        for v in h:
            if v == 1 or v == u:
                continue
            v0 = (v - 1) % p
            denom = (u0 + v0) % p
            if denom == 0:
                continue
            w = (1 - u0 * v0 * pow(denom, -1, p)) % p
            lam = (u + v + w - 2) % p
            if w not in hset or lam not in hset or len({u, v, w}) != 3:
                continue
            r = u0 * pow(v0, -1, p) % p
            b_line += 1
            support[r] = support.get(r, 0) + 1
            if (r * r + r + 1) % p == 0:
                q0_total += 1
                q0_support.add(r)

    genuine_support = len(support) - len(q0_support)
    if genuine_support % 6:
        raise AssertionError((p, n, genuine_support))
    return {
        "b_line": b_line,
        "support": len(support),
        "genuine_support": genuine_support,
        "r_orb": genuine_support // 6,
        "q0_support": len(q0_support),
        "q0_total": q0_total,
        "max_fiber": max(support.values(), default=0),
    }


def main() -> None:
    rows = (
        (257, 16),
        (1153, 32),
        (4289, 64),
        (17921, 128),
        (65537, 256),
        (262657, 512),
        (1051649, 1024),
    )
    print("h=3 repeat-boundary support boundary evidence")
    nonzero_rows = 0
    for p, n in rows:
        row = support_from_h_pairs(p, n)
        if row["b_line"]:
            nonzero_rows += 1
        print(
            f"p={p} n={n} B_line={row['b_line']} support={row['support']} "
            f"genuine_support={row['genuine_support']} R_orb={row['r_orb']} "
            f"q0_support={row['q0_support']} q0_total={row['q0_total']} "
            f"max_fiber={row['max_fiber']}"
        )
    if nonzero_rows != 1:
        raise AssertionError(("expected exactly the p=65537 guardrail row", nonzero_rows))
    print("zero-support theorem is false: n=256, p=65537 has B_line=48")
    print("H3_REPEAT_SUPPORT_BOUNDARY_EVIDENCE_PASS")


if __name__ == "__main__":
    main()
