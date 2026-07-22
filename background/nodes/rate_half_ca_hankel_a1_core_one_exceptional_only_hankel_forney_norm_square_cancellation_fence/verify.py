#!/usr/bin/env python3
"""Exact finite control for the Forney norm-square cancellation."""

from __future__ import annotations

from math import prod


def main() -> None:
    prime = 101
    e = 3
    beta = [100, 5, 91, 10, 96, 1]
    q_1 = [2, 12, 30, 56, 90, 31]

    beta_class = pow(-1, e, prime) * prod(beta) % prime
    res_q_1 = prod(q_1) % prime
    xi_reduced = beta_class * res_q_1 * res_q_1 % prime
    if pow(beta_class, (prime - 1) // 2, prime) != 1:
        raise AssertionError("weighted self-dual determinant class is nonsquare")
    if xi_reduced != 25:
        raise AssertionError("Forney cancellation control changed")
    if pow(xi_reduced, (prime - 1) // 2, prime) != 1:
        raise AssertionError("cancelled norm class is nonsquare")

    print(
        "RATE_HALF_FORNEY_NORM_CANCELLATION_PASS "
        f"prime={prime} e={e} xi={xi_reduced}"
    )


if __name__ == "__main__":
    main()
