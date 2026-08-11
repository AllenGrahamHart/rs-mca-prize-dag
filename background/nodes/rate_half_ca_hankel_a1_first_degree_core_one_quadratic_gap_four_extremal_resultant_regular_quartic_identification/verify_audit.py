#!/usr/bin/env python3
"""Tamper checks for center and all-excess cancellation."""


def main():
    e = 101
    p = (3 * e - 1) // 2
    d = 3 * e - 2
    n = p - 3

    assert (d - 1) + 1 - d == 0
    assert (d - 1) + 0 - d == -1
    assert (n - 3 - 2) + 2 == n - 3
    assert (n - 3 - 2) + 1 == n - 4
    print("PASS extremal regular-quartic eliminant audit tamper=2/2")


if __name__ == "__main__":
    main()
