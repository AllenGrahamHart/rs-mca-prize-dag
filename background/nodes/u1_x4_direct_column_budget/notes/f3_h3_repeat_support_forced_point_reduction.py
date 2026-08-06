#!/usr/bin/env python3
"""Verify the h=3 repeat-support forced-point reduction ledger."""

from __future__ import annotations

from f3_h3_pair_count_from_charts_compiler import root_table
from f3_h3_repeat_support_boundary_evidence import support_from_h_pairs


def active_ordered_triples(p: int, n: int) -> list[tuple[int, int, int, int]]:
    h = root_table(p, n)
    hset = set(h)
    triples: list[tuple[int, int, int, int]] = []
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
            if w in hset and lam in hset and len({u, v, w}) == 3:
                triples.append((u, v, w, lam))
    return triples


def fixed_first_count(p: int, n: int, a: int) -> int:
    h = root_table(p, n)
    hset = set(h)
    if a not in hset or a == 1:
        raise AssertionError((p, n, a))
    count = 0
    a0 = (a - 1) % p
    for v in h:
        if v == 1 or v == a:
            continue
        v0 = (v - 1) % p
        denom = (a0 + v0) % p
        if denom == 0:
            continue
        w = (1 - a0 * v0 * pow(denom, -1, p)) % p
        lam = (a + v + w - 2) % p
        if w in hset and lam in hset and len({a, v, w}) == 3:
            count += 1
    return count


def verify_row(p: int, n: int) -> dict[str, int | str]:
    triples = active_ordered_triples(p, n)
    support = support_from_h_pairs(p, n)
    if len(triples) != support["b_line"]:
        raise AssertionError((p, n, len(triples), support))
    if not triples:
        return {
            "b_line": 0,
            "common": "-",
            "first_count_sum": 0,
            "three_first_sum": 0,
        }

    common = set(triples[0][:3])
    for u, v, w, _ in triples[1:]:
        common &= {u, v, w}
    first_sum = sum(fixed_first_count(p, n, a) for a in common)
    three_first_sum = 3 * first_sum
    if three_first_sum < len(triples):
        raise AssertionError((p, n, common, first_sum, len(triples)))
    return {
        "b_line": len(triples),
        "common": ",".join(str(x) for x in sorted(common)) if common else "-",
        "first_count_sum": first_sum,
        "three_first_sum": three_first_sum,
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
    print("h=3 repeat-support forced-point reduction")
    for p, n in rows:
        row = verify_row(p, n)
        print(
            f"p={p} n={n} B_line={row['b_line']} common={row['common']} "
            f"sum_Na={row['first_count_sum']} three_sum_Na={row['three_first_sum']}"
        )
    print("If a forced set A covers all triples, B_line <= 3*sum_{a in A} N_a")
    print("H3_REPEAT_SUPPORT_FORCED_POINT_REDUCTION_PASS")


if __name__ == "__main__":
    main()
