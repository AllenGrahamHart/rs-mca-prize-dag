#!/usr/bin/env python3
"""Coordinate-cover ledger for h=3 repeat-boundary support."""

from __future__ import annotations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_support_boundary_evidence import support_from_h_pairs


def active_triples_and_cover(p: int, n: int) -> dict[str, int]:
    h = root_table(p, n)
    hset = set(h)
    cover: set[int] = set()
    b_line = 0
    support: set[int] = set()
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
            support.add(r)
            cover.update((u, v, w))

    if len(cover) > min(n, 3 * b_line):
        raise AssertionError((p, n, len(cover), b_line))
    support_row = support_from_h_pairs(p, n)
    if support_row["b_line"] != b_line or support_row["support"] != len(support):
        raise AssertionError((p, n, support_row, b_line, len(support)))
    bound = (72 * len(cover) + 18) * n * n
    return {
        "b_line": b_line,
        "support": len(support),
        "coord_cover": len(cover),
        "cover_residue_bound": bound,
        "n3": n**3,
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
    print("h=3 repeat coordinate-cover ledger")
    for p, n in rows:
        row = active_triples_and_cover(p, n)
        print(
            f"p={p} n={n} B_line={row['b_line']} support={row['support']} "
            f"C_coord={row['coord_cover']} residue_bound={row['cover_residue_bound']} "
            f"n^3={row['n3']}"
        )
    print("The actual coordinate cover C_coord is a canonical forced cover")
    print("H3_REPEAT_COORDINATE_COVER_LEDGER_PASS")


if __name__ == "__main__":
    main()
