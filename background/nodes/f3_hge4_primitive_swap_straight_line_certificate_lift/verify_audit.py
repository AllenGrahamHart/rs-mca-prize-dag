#!/usr/bin/env python3
"""Mutation audit for the HGE4 swap straight-line certificate lift."""

from __future__ import annotations

import verify


def main() -> None:
    divisor = verify.divisor_from_t([78, 73, 1], 18, 97)
    values, _ = verify.recurrence(divisor, 4, 97)
    assert values[-1] == [1]

    wrong_scalar = verify.divisor_from_t([78, 73, 1], 19, 97)
    wrong_values, _ = verify.recurrence(wrong_scalar, 4, 97)
    assert wrong_values[-1] != [1]

    wrong_t = verify.divisor_from_t([78, 74, 1], 18, 97)
    wrong_t_values, _ = verify.recurrence(wrong_t, 4, 97)
    assert wrong_t_values[-1] != [1]

    assert verify.presentation_size(12, 5)[2:] == (88, 90)
    assert verify.presentation_size(40, 5)[2:] == (340, 342)

    print(
        "F3_HGE4_PRIMITIVE_SWAP_STRAIGHT_LINE_CERTIFICATE_LIFT_AUDIT_PASS "
        "scalar_mutation=1 coefficient_mutation=1 size_guard=1"
    )


if __name__ == "__main__":
    main()
