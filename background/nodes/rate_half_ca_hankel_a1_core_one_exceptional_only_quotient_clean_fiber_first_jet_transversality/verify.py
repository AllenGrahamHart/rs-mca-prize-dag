#!/usr/bin/env python3
"""Finite-field fixture for clean-fiber first-jet transversality."""

from __future__ import annotations


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    prime = 101
    gamma = 3
    y = 3
    exponent = 2

    # R=(Y-3)(Y-5), F=Y-t, U=Y-5, P=t-3, L=Y-5,
    # E=t-5, W=t^2, S=(5-t)Y+5t.
    f_t = -1
    f_y = 1
    u = y - 5
    p_derivative = 1
    ell = y - 5
    exceptional = gamma - 5
    w = gamma**2
    s = (5 - gamma) * y + 5 * gamma
    r_derivative = 2 * y - 8

    first = (f_t * u + p_derivative * ell) % prime
    second = (ell * w - exceptional * pow(y, exponent, prime)) % prime
    unit = (ell * w - (y - gamma) * s) % prime
    need(first == 0, "differentiated complement identity failed")
    need(second == 0, "selected-root unit identity failed")
    need(unit == exceptional * pow(y, exponent, prime) % prime,
         "global unit fixture failed")

    left = f_t * u * w % prime
    right = -p_derivative * exceptional * pow(y, exponent, prime) % prime
    need(left == right and left != 0, "first-jet product identity failed")
    velocity = (
        p_derivative
        * exceptional
        * pow(y, exponent, prime)
        * pow(r_derivative * w, -1, prime)
    ) % prime
    need(velocity == 1 == (-f_t * pow(f_y, -1, prime)) % prime,
         "root velocity mismatch")

    # Independent smooth-domain exponent check. Over F_17, 2 has order
    # M=8. Remove s=1 and x_0=-1; for r=M/4-1, N_sq=M+r-3.
    smooth_prime = 17
    domain_order = 8
    locator_degree = domain_order - 2
    r = domain_order // 4 - 1
    square_exponent = locator_degree + r - 1
    smooth_y = 2
    core = 1
    zero_trace = -1 % smooth_prime
    denominator = (
        (1 - core * smooth_y) * (1 - zero_trace * smooth_y)
    ) % smooth_prime
    locator_derivative = (
        -domain_order
        * pow(smooth_y, -1, smooth_prime)
        * pow(denominator, -1, smooth_prime)
    ) % smooth_prime
    abstract_weight = (
        pow(smooth_y, square_exponent, smooth_prime)
        * pow(locator_derivative, -1, smooth_prime)
    ) % smooth_prime
    reduced_weight = (
        -pow(domain_order, -1, smooth_prime)
        * pow(smooth_y, r - 2, smooth_prime)
        * denominator
    ) % smooth_prime
    need(square_exponent == domain_order + r - 3,
         "corrected-square exponent was confused with domain order")
    need(abstract_weight == reduced_weight,
         "smooth-domain exponent reduction failed")
    print(
        "RATE_HALF_QUOTIENT_CLEAN_FIBER_FIRST_JET_PASS "
        f"prime={prime} incidence=({gamma},{y}) velocity={velocity} "
        f"smooth_weight={reduced_weight}"
    )


if __name__ == "__main__":
    main()
