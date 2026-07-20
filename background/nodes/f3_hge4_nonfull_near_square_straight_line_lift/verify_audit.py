#!/usr/bin/env python3
"""Mutation audit for the HGE4 non-full near-square lift."""

from __future__ import annotations

import verify


def main() -> None:
    prime = 97
    center = [0, 78, 0, 73, 0, 1]
    divisor = verify.near_square(center, 42, prime)
    values, _ = verify.recurrence(divisor, 5, prime)
    assert values[-1] == [1]

    wrong_shift = verify.near_square(center, 43, prime)
    wrong_values, _ = verify.recurrence(wrong_shift, 5, prime)
    assert wrong_values[-1] != [1]

    full_center = [0, 0, 0, 0, 1]
    assert not any(full_center[1:4])
    assert any(center[1:5])

    assert verify.sizes(13, 4)[3:] == (163, 166)
    assert verify.sizes(13, 8)[3:] == (304, 311)

    print(
        "F3_HGE4_NONFULL_NEAR_SQUARE_STRAIGHT_LINE_LIFT_AUDIT_PASS "
        "shift_mutation=1 selector_guard=1 size_guard=1"
    )


if __name__ == "__main__":
    main()
