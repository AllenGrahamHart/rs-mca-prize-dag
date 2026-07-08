#!/usr/bin/env python3
"""Compiler for the h=3 activation-bound route to the per-row accident bound.

This is an arithmetic and evidence audit.  It does not prove the missing
prime-ideal/common-root sparsity theorem.
"""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SUMMARY_PATH = HERE / "f3_h3_all_core_census_summary.json"


def toral_bound(n: int) -> int:
    if n % 3:
        return 0
    m = n // 3
    return m * (m - 1) // 2


def compiled_t3_bound(n: int, activation_constant: int) -> Fraction:
    """Bound from toral + Poisson boundary + n*A_3 with A_3 <= C*n."""

    return (
        Fraction(toral_bound(n), 1)
        + Fraction(n * n, 72)
        + Fraction(activation_constant * n * n, 1)
    )


def first_n_below_floor(activation_constant: int, limit: int = 10000) -> int:
    for n in range(2, limit + 1):
        if compiled_t3_bound(n, activation_constant) < n**3:
            return n
    raise AssertionError(f"no threshold <= {limit} for C={activation_constant}")


def load_summary() -> dict:
    data = json.loads(SUMMARY_PATH.read_text())
    if data["n"] != 96:
        raise AssertionError(data["n"])
    if data["activation_exception_count"] != len(data["activation_exceptions"]):
        raise AssertionError(
            (data["activation_exception_count"], len(data["activation_exceptions"]))
        )
    if data["activation_exception_count"] != 720:
        raise AssertionError(data["activation_exception_count"])
    return data


def prime_activation_counts(data: dict) -> Counter[int]:
    counts: Counter[int] = Counter()
    for rec in data["activation_exceptions"]:
        for p in rec["activation_primes"]:
            counts[int(p)] += 1
    return counts


def main() -> None:
    data = load_summary()
    n = data["n"]
    counts = prime_activation_counts(data)
    max_prime, max_count = max(counts.items(), key=lambda item: (item[1], -item[0]))
    top = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:8]

    print("h=3 activation-bound compiler")
    print(
        f"n={n} oriented_activations={data['activation_exception_count']} "
        f"activation_primes={len(counts)}"
    )
    print(f"max oriented per-prime activation count: p={max_prime} count={max_count}")
    print("top activation primes:")
    for p, count in top:
        print(f"  p={p}: {count}")

    # The all-core census is not Burnside-deduplicated.  Therefore these are
    # evidence upper counts, not a formal orbit count.  Still, the per-prime
    # maximum is below the C=1 target at n=96.
    if not max_count < n:
        raise AssertionError((max_prime, max_count, n))

    for c in (1, 2, 4, 8, 16):
        threshold = first_n_below_floor(c)
        bound96 = compiled_t3_bound(n, c)
        print(
            f"C={c:2d}: threshold n>={threshold:3d}; "
            f"n=96 bound={float(bound96):.2f}; "
            f"ratio={float(bound96 / n**3):.6f}"
        )

    if first_n_below_floor(16) != 17:
        raise AssertionError("C=16 threshold drift")
    print("H3_ACTIVATION_BOUND_COMPILER_PASS")


if __name__ == "__main__":
    main()
