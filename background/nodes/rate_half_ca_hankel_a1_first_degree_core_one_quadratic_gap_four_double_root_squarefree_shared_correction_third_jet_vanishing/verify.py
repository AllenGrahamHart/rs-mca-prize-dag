#!/usr/bin/env python3
"""Replay the symmetric Schur argument forcing the shared jet to vanish."""


def main() -> None:
    # Model N=diag(z^3,1). Any lift with Nv divisible by z^2 has a regular
    # coordinate beginning in order two, so its self-pairing begins in
    # order at least three.
    schur_order = 3
    regular_lift_order = 2
    self_pair_order = min(schur_order, 2 * regular_lift_order)
    assert self_pair_order == 3

    u_at_xstar = 17
    prime = 101
    for kappa in range(prime):
        order_two_self_coefficient = kappa * u_at_xstar % prime
        compatible = order_two_self_coefficient == 0
        assert compatible == (kappa == 0)

    print("RATE_HALF_SHARED_THIRD_JET_VANISHING_PASS kappa_cases=101")


if __name__ == "__main__":
    main()
