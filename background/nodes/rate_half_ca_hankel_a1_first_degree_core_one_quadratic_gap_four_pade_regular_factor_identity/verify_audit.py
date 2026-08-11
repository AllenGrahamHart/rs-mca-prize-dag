#!/usr/bin/env python3
"""Tamper checks for the regular-factor normalization."""


def main():
    e = 101
    p = (3 * e - 1) // 2
    d = 2 * p - 1
    n0 = 3 * p - 2
    n = p - 3

    exponent = n0 + d - 1 - n
    assert exponent == 2 * d + 1
    assert exponent != 2 * d
    assert (e - 6) + 4 == e - 2
    assert (e - 6) + 3 != e - 2
    print("PASS quadratic gap-four Pade regular factor audit tamper=2/2")


if __name__ == "__main__":
    main()
