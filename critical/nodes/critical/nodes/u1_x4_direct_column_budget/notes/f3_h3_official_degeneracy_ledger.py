#!/usr/bin/env python3
"""Official-row h=3 degeneracy ledger checks."""

from __future__ import annotations

from fractions import Fraction


OFFICIAL_EXPONENTS = tuple(range(13, 42))


def toral_bound(n: int) -> int:
    if n % 3:
        return 0
    m = n // 3
    return m * (m - 1) // 2


def compiled_t3_bound_official(n: int, activation_constant: int) -> Fraction:
    if toral_bound(n) != 0:
        raise AssertionError(("official row has toral branch", n))
    return Fraction(n * n, 72) + activation_constant * n * n


def main() -> None:
    rows = [1 << s for s in OFFICIAL_EXPONENTS]
    if any(toral_bound(n) for n in rows):
        raise AssertionError("toral branch present on an official h=3 row")

    # The h=3 activation compiler uses C=16.  With the toral term absent, every
    # official row is far beyond the n>=17 threshold.
    for n in rows:
        bound = compiled_t3_bound_official(n, 16)
        if not bound < n**3:
            raise AssertionError((n, bound, n**3))

    first = rows[0]
    last = rows[-1]
    print("official h=3 rows: n=2^s, s=13..41")
    print(f"first={first} last={last} row_count={len(rows)}")
    print("toral_bound(2^s)=0 for every official row")
    print("remaining official degeneracy cells: constant-ratio, hyperbola-line b=a^2/3")
    print("H3_OFFICIAL_DEGENERACY_LEDGER_PASS")


if __name__ == "__main__":
    main()
