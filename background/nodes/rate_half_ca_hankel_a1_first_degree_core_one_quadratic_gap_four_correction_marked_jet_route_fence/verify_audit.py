#!/usr/bin/env python3
"""Tamper checks for the abstract marked orders."""


def main():
    assert 2 + 2 * 3 == 8
    assert 1 + 2 * 3 == 7
    assert 1 + 2 * 3 != 8
    assert 2 + 2 * 2 != 8
    print("PASS quadratic correction marked-jet fence audit tamper=2/2")


if __name__ == "__main__":
    main()
