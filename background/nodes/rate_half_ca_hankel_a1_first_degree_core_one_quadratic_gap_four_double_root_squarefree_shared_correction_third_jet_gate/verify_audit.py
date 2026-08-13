#!/usr/bin/env python3
"""Independent truncated-series audit of the shared recurrence."""


def order(coefficients: list[int]) -> int:
    for index, coefficient in enumerate(coefficients):
        if coefficient:
            return index
    return len(coefficients)


def main() -> None:
    x_star = 5
    q_row_h = [0, 0, 0, 0, 9]

    for kappa, expected_order in ((0, 3), (4, 2)):
        f_i = [0, 0, kappa, 6, 1]
        f_next = [
            x_star * left - right
            for left, right in zip(f_i, q_row_h)
        ]
        assert order(f_i) == expected_order
        assert order(f_next) == expected_order
        assert f_next[2] == x_star * kappa

    print("RATE_HALF_SHARED_CORRECTION_THIRD_JET_AUDIT_PASS branches=2")


if __name__ == "__main__":
    main()
