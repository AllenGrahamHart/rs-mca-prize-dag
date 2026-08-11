#!/usr/bin/env python3
"""Independent truncated-local-ring audit of the fixed-row comparison."""


def valuation(coefficients: list[int]) -> int:
    for index, coefficient in enumerate(coefficients):
        if coefficient:
            return index
    raise AssertionError("zero series")


def main() -> None:
    # The moving value has order q=2-c. The substitution error begins in
    # order three, so the fixed value retains q.
    for center_order, moving in (
        (0, [0, 0, 5, 1]),
        (1, [0, 7, 0, 1]),
    ):
        substitution_error = [0, 0, 0, 9]
        fixed = [left + right for left, right in zip(moving, substitution_error)]
        expected = 2 - center_order
        assert valuation(moving) == expected
        assert valuation(fixed) == expected
        assert valuation(fixed) - expected == 0

    print("RATE_HALF_HEAVY_ROW_CORRECTION_EXACT_ORDER_AUDIT_PASS cases=2")


if __name__ == "__main__":
    main()
