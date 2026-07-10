#!/usr/bin/env python3
"""Clause (b) confrontation: the fifth branch's canonical-class counts vs the
ACTUAL dyadic_profile_evaluation pricing column.

dyadic_profile_evaluation (QA.22, critical/nodes/dyadic_profile_evaluation/proof.md):
    Q_M = C(n/M - 1, floor(A/M))   for dyadic M | n, M > t
i.e. the fixed-tail quotient-coset count at scale M, weight 1 per coset.

The fifth branch's objects: canonical support-scale classes (bijective with
supports R), counted per scale either raw (admissible at M) or selected
(minimal admissible scale = M).

If the branch's 'declared duplicate subtraction or multiplicity factor' were
any per-scale factor lambda_M with  class_count_M = lambda_M * Q_M, then
raw_M/Q_M (resp. sel_M/Q_M) would have to be that factor.  We tabulate both
ratios on |R| = A slices and test integrality/constancy.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from math import comb

sys.path.insert(0, "/tmp/claude-1000/-home-u2470931-smooth-read-solomin/d53e6c57-2281-4b35-b085-8a669b4db5f5/scratchpad")
from g3_lib import eligible_scales, minimal_scale, tail_size


def run(n: int, t: int, A_values: list[int]) -> None:
    elig = eligible_scales(n, t)
    print(f"n={n} t={t} eligible scales {elig}")
    for A in A_values:
        masks = [mk for mk in range(1 << n) if mk.bit_count() == A]
        raw = {M: 0 for M in elig}
        sel = {M: 0 for M in elig}
        for mk in masks:
            for M in elig:
                if tail_size(n, M, mk) < M:
                    raw[M] += 1
            ms = minimal_scale(n, t, mk)
            if ms is not None:
                sel[ms] += 1
        print(f"  A={A}  (supports of size A: {len(masks)})")
        print(f"    {'M':>4} {'Q_M':>8} {'raw_M':>10} {'sel_M':>10} {'raw/Q':>12} {'sel/Q':>12}")
        for M in elig:
            h = A // M
            N = n // M
            Q = comb(N - 1, h) if N - 1 >= h >= 0 else 0
            rq = Fraction(raw[M], Q) if Q else None
            sq = Fraction(sel[M], Q) if Q else None
            print(f"    {M:>4} {Q:>8} {raw[M]:>10} {sel[M]:>10} {str(rq):>12} {str(sq):>12}")
        print()


def main() -> None:
    run(16, 1, [5, 6, 7, 8])
    run(16, 3, [7, 8, 11])
    run(8, 1, [3, 5])


if __name__ == "__main__":
    main()
