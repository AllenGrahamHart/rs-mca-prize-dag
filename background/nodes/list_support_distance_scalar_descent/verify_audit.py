#!/usr/bin/env python3
"""Mutation audit for support-distance scalar descent."""

from __future__ import annotations

import verify


def main() -> None:
    q = 2**31 - 1
    total, killed = verify.projective_counts(q, 4)
    assert q * killed < total
    assert (q**4 // 2**100, q**4 // 2**128) == (2**24 - 1, 0)

    # At the GF(9)/GF(3) fixture, dropping the +1 from g would make the
    # theorem unusable: a-k=0 while a-k+1=1.
    n, k, agreement, size = 3, 2, 2, 3
    total_small, killed_small = verify.projective_counts(3, 2)
    assert size * (n - agreement) * killed_small < (agreement - k + 1) * total_small
    assert not size * (n - agreement) * killed_small < (agreement - k) * total_small

    centers, maximum = verify.tiny_exhaustive_check()
    assert centers > 0 and maximum == 3

    # At the same agreement and the local 2^-128 target, the incidence test
    # is nontrivial through degree five but fails at degree six.
    n, k, agreement = 2**21, 2**20, 1_116_023
    errors, gap = n - agreement, agreement - k + 1
    verdicts = []
    for degree in range(1, 9):
        total_r, killed_r = verify.projective_counts(q, degree)
        threshold = q**degree // 2**128 + 1
        verdicts.append(threshold * errors * killed_r < gap * total_r)
    assert verdicts == [True, True, True, True, True, False, False, False]

    print(
        "LIST_SUPPORT_DISTANCE_SCALAR_DESCENT_AUDIT_PASS "
        "target_guard=1 gap_plus_one_guard=1 degree_boundary=5/6"
    )


if __name__ == "__main__":
    main()
