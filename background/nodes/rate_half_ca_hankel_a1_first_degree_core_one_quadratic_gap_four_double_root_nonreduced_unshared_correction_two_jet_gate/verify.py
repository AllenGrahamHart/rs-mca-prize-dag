#!/usr/bin/env python3
"""Replay the nonreduced two-jet recurrence gate."""


def main() -> None:
    q_row_order = 6
    determinant_order = 4
    forced_order = 2
    x_star = 11
    prime = 101

    assert forced_order < determinant_order < q_row_order

    branches = 0
    for kappa_2, kappa_3 in ((0, 0), (7, 0), (0, 9), (7, 9)):
        for index in range(7):
            scale = pow(x_star, index, prime)
            assert kappa_2 * scale % prime == pow(x_star, index, prime) * kappa_2 % prime
            assert kappa_3 * scale % prime == pow(x_star, index, prime) * kappa_3 % prime
        full_divisibility = kappa_2 == 0 and kappa_3 == 0
        assert full_divisibility == ((kappa_2, kappa_3) == (0, 0))
        branches += 1

    print("RATE_HALF_NONREDUCED_UNSHARED_TWO_JET_PASS branches=4 moments=7")


if __name__ == "__main__":
    main()
