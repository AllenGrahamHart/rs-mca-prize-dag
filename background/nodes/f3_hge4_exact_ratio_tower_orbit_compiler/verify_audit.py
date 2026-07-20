#!/usr/bin/env python3
"""Mutation audit for the HGE4 exact-ratio tower compiler."""

from __future__ import annotations

from fractions import Fraction

import verify


def main() -> None:
    pairs = verify.primitive_pairs(16, 17, 2)
    inherited = [
        pair for pair in pairs if verify.exact_level(*pair, 16)[0] == 8
    ]
    assert inherited

    # Omitting V_(r-1)!=1 would count level-8 pairs again at level 16.
    left, right = inherited[0]
    assert len({exponent % 2 for exponent in left | right}) == 1
    assert verify.exact_level(left, right, 16)[0] != 16

    order = 2**13
    square_sum = sum((2**level) ** 2 for level in range(14))
    assert Fraction(21, 2) * square_sum < 14 * order * order
    assert 11 * square_sum > 14 * order * order

    orbits, _ = verify.census_check(4)
    assert orbits == 14
    print(
        "F3_HGE4_EXACT_RATIO_TOWER_ORBIT_COMPILER_AUDIT_PASS "
        "inherited_level_guard=1 constant_guard=1 anchor_guard=1"
    )


if __name__ == "__main__":
    main()
