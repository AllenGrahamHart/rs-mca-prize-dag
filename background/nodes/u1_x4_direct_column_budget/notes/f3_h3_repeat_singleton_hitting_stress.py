#!/usr/bin/env python3
"""Bounded stress test for singleton h=3 repeat-boundary hitting."""

from __future__ import annotations

from f3_h3_repeat_coordinate_hitting_ledger import (
    active_coordinate_edges_from_triples,
    minimum_hitting_set,
)
from f3_h3_repeat_support_boundary_evidence import is_prime
from f3_h3_repeat_support_forced_point_reduction import active_ordered_triples


CONFIGS = (
    (16, 200),
    (32, 200),
    (64, 200),
    (128, 120),
    (256, 80),
)


def scan_row(n: int, prime_limit: int) -> dict[str, int | str]:
    seen = 0
    nonzero = 0
    max_edges = 0
    max_summary = "-"
    p = n * n + 1
    while seen < prime_limit and p <= n * n + 5_000_000:
        if (p - 1) % n == 0 and is_prime(p):
            triples = active_ordered_triples(p, n)
            edges = active_coordinate_edges_from_triples(p, n, triples)
            if edges:
                nonzero += 1
                tau, hitting = minimum_hitting_set(edges)
                if tau > 1:
                    raise AssertionError((n, p, len(triples), len(edges), tau, hitting))
                if len(edges) > max_edges:
                    max_edges = len(edges)
                    max_summary = (
                        f"p={p},B={len(triples)},edges={len(edges)},"
                        f"tau={tau},hit={','.join(str(a) for a in hitting)}"
                    )
            seen += 1
        p += n
    if seen != prime_limit:
        raise AssertionError((n, seen, prime_limit))
    return {
        "seen": seen,
        "nonzero": nonzero,
        "max_edges": max_edges,
        "max_summary": max_summary,
    }


def main() -> None:
    print("h=3 repeat singleton-hitting stress")
    for n, prime_limit in CONFIGS:
        row = scan_row(n, prime_limit)
        print(
            f"n={n} scanned_primes={row['seen']} nonzero_rows={row['nonzero']} "
            f"max_edges={row['max_edges']} max_row={row['max_summary']}"
        )
    print("No tau_coord > 1 found in the bounded boundary-style scan")
    print("If tau_coord <= 1, repeat_residue <= 90*n^2")
    print("H3_REPEAT_SINGLETON_HITTING_STRESS_PASS")


if __name__ == "__main__":
    main()
