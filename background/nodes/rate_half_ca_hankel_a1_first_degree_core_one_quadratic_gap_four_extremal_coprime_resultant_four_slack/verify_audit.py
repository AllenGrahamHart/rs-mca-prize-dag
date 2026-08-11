#!/usr/bin/env python3
"""Tamper audit for the mandatory-factor subtraction."""


def residual_cap(e, d_a, r_zero):
    cap = 2 * e - 5 if d_a == 0 else e - 3
    exceptional = e - 3 if d_a == 0 else 0
    return cap - exceptional - r_zero


def main():
    e = 101
    for d_a in (0, 1):
        total_r = e - 6 - d_a
        for r_bad in range(total_r + 1):
            r_zero = total_r - r_bad
            assert residual_cap(e, d_a, r_zero) == 4 + r_bad

    # Omitting the exceptional factor in d_A=0 leaves e-3 false degrees.
    total_r = e - 6
    wrong = (2 * e - 5) - total_r
    assert wrong != 4
    assert wrong - 4 == e - 3
    print("PASS extremal resultant four-slack audit tamper=1/1")


if __name__ == "__main__":
    main()
