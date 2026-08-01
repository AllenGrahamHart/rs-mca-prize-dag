#!/usr/bin/env python3
"""Exact arithmetic checks for the proposed XR P-B proof-program dossier.

This script does not prove xr_lowcore_spread_heart.  It checks the finite
parameter identities and budget fractions used to decide whether a proposed
energy/ownership composition can possibly close all six official rows.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb, floor, log2


@dataclass(frozen=True)
class Row:
    name: str
    n: int
    K: int
    H: int
    C0: int
    R_C0: int
    R_next: int

    @property
    def h(self) -> int:
        return self.H - 1

    @property
    def A(self) -> int:
        return self.K + self.h

    @property
    def radius(self) -> int:
        return self.n - self.A

    @property
    def d(self) -> int:
        return self.n - 2 * self.K

    @property
    def recursion_depth(self) -> int:
        # Each repeated-difference descent has t >= H, hence K' = K-t <= K-H.
        return (self.K - 1) // self.H

    @property
    def budget(self) -> int:
        return 8 * self.n**3

    @property
    def paid_fraction(self) -> Fraction:
        # Under the candidate producer E_nonzero >= M^2(M-1)/n^2 and M>8n^3,
        # the near-K band costs at most R_C0/(8n), and the multiplicity-one
        # t>=K band costs at most 1/(8n).
        return Fraction(self.R_C0 + 1, 8 * self.n)

    @property
    def remaining_fraction(self) -> Fraction:
        return 1 - self.paid_fraction


ROWS = (
    Row("RowC 1/4", 2**10, 2**8, 6, 2, 6_327, 411_273),
    Row("RowC 1/8", 2**10, 2**7, 6, 1, 128, 14_171),
    Row("RowC 1/16", 2**10, 2**6, 4, 1, 224, 40_455),
    Row("Prize 1/4", 2**41, 2**39, 2**33 + 2, 6, 4_398_046_497_508, 562_949_951_166_976),
    Row("Prize 1/8", 2**41, 2**38, 2**33 + 2, 5, 260_919_262_630, 50_096_498_384_811),
    Row("Prize 1/16", 2**41, 2**37, 2**32 + 2, 4, 40_282_095_485, 18_046_378_752_308),
)


def packing_cap(row: Row, c: int) -> int:
    numerator = comb(row.n - 2 * row.K + 2 * c, c)
    denominator = comb(row.H + c - 1, c)
    return numerator // denominator


def gv_greedy_log2_lower(row: Row) -> float:
    """Greedy constant-weight-code lower bound for the RowC support-only fence."""
    numerator = comb(row.n, row.A)
    ball = sum(comb(row.A, i) * comb(row.n - row.A, i) for i in range(row.H))
    return log2(numerator) - log2(ball)


def main() -> None:
    print("XR_LOWCORE_PROOF_PROGRAM_ARITHMETIC")
    print("name|n|K|H|A|r|d|depth|C0|R_C0|R_next|paid_fraction|remaining_fraction")
    for row in ROWS:
        assert row.A == row.K + row.H - 1
        assert row.radius == row.n - row.K - row.H + 1
        assert packing_cap(row, row.C0) == row.R_C0
        assert packing_cap(row, row.C0 + 1) == row.R_next
        assert row.R_C0 <= 8 * row.n < row.R_next
        assert row.paid_fraction < 1
        print(
            f"{row.name}|{row.n}|{row.K}|{row.H}|{row.A}|{row.radius}|{row.d}|"
            f"{row.recursion_depth}|{row.C0}|{row.R_C0}|{row.R_next}|"
            f"{row.paid_fraction}|{row.remaining_fraction}"
        )

    # Exact fractions singled out in the dossier.
    assert ROWS[0].paid_fraction == Fraction(791, 1024)
    assert ROWS[0].remaining_fraction == Fraction(233, 1024)
    assert ROWS[1].paid_fraction == Fraction(129, 8192)
    assert ROWS[2].paid_fraction == Fraction(225, 8192)

    # A multiplicity-two difference owner would yield only half of the baseline
    # Cauchy energy.  RowC 1/4 already spends more than half before the open
    # middle widths are charged, so that route cannot compose unchanged.
    assert ROWS[0].paid_fraction > Fraction(1, 2)

    print("\nPRODUCER_MULTIPLICITY_HEADROOM")
    for row in ROWS:
        # Largest integer mu for which the already-paid debit is strictly
        # below the Cauchy coefficient 1/mu.  The open middle widths still
        # require additional room, so these are upper compatibility ceilings.
        mu = 1
        while row.paid_fraction < Fraction(1, mu + 1):
            mu += 1
        print(f"{row.name}: max_mu_before_middle={mu}")

    print("\nSUPPORT_ONLY_GREEDY_FENCE")
    for row in ROWS[:3]:
        lower = gv_greedy_log2_lower(row)
        budget_bits = log2(row.budget)
        print(
            f"{row.name}: log2_greedy_lower={lower:.9f}; "
            f"log2_budget={budget_bits:.9f}; margin={lower-budget_bits:.9f}"
        )
        assert lower > budget_bits + 200

    # Descent closure class: (n,K,A) -> (n-2t,K-t,A-t) preserves d=n-2K and h=A-K.
    for row in ROWS:
        for t in (row.H, min(row.K - 1, row.H + 1), row.K - 1):
            if not (row.H <= t <= row.K - 1):
                continue
            n2, k2, a2 = row.n - 2 * t, row.K - t, row.A - t
            assert n2 - 2 * k2 == row.d
            assert a2 - k2 == row.h
            assert k2 >= 1

    print("\nPASS: exact row, packing, budget, support-fence, and descent checks")


if __name__ == "__main__":
    main()
