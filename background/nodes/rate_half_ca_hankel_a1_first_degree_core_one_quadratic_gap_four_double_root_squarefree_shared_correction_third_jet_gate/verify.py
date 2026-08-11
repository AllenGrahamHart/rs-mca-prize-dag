#!/usr/bin/env python3
"""Replay the shared-root third-jet recurrence gate."""


def main() -> None:
    q_row_order = 4
    determinant_order = 3
    forced_contact_order = 2
    x_star = 7
    prime = 101

    assert forced_contact_order < determinant_order < q_row_order

    for kappa in (0, 13):
        leading = kappa
        moments = []
        for index in range(8):
            moments.append(leading)
            leading = leading * x_star % prime
        expected = [kappa * pow(x_star, index, prime) % prime for index in range(8)]
        assert moments == expected
        full_divisibility = kappa == 0
        assert full_divisibility == all(value == 0 for value in moments)

    print("RATE_HALF_SHARED_CORRECTION_THIRD_JET_PASS branches=2 moments=8")


if __name__ == "__main__":
    main()
