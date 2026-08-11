#!/usr/bin/env python3
"""Finite-field audit of the incident first-jet mismatch and sign."""


def inv(x, q):
    return pow(x % q, q - 2, q)


def main():
    q = 101
    x_minus_core = 7
    v_x = 11
    lprime = 13
    lambda_value = 17
    b_out = 19
    g_error = 23
    actual_error = 29

    kappa = x_minus_core * v_x * g_error * b_out * lprime % q
    omega = x_minus_core * v_x * (g_error + actual_error) % q

    row_ratio = lprime * omega * inv(lambda_value, q) % q
    fiber_ratio = kappa * inv(lambda_value * b_out, q) % q
    mismatch = (row_ratio - fiber_ratio) % q
    expected = x_minus_core * v_x * lprime * actual_error * inv(lambda_value, q) % q

    assert mismatch == expected
    assert mismatch != 0

    # The rejected substitution omega*B*L'=kappa erases the actual error.
    tampered_omega = kappa * inv(b_out * lprime, q) % q
    assert (lprime * tampered_omega * inv(lambda_value, q) - fiber_ratio) % q == 0
    print("PASS paired first-jet transversality audit tamper=1/1")


if __name__ == "__main__":
    main()
