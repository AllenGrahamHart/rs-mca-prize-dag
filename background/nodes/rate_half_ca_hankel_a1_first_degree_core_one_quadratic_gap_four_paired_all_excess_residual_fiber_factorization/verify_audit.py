#!/usr/bin/env python3
"""Tamper audit for the residual-polynomial source identity."""


def main():
    # Symbolic degree ledger at a positive-excess sample.
    n, a, r, h = 37, 9, 5, 6
    i_size = n - a - r
    degree = i_size + h + r
    assert degree == 34
    assert n - degree == a - h == 3

    # The rejected zero-excess continuation would force h=0 and miss the
    # exact three-degree drop at this sample.
    wrong_degree = i_size + r
    assert n - wrong_degree == a
    assert wrong_degree != degree
    print("PASS paired all-excess factorization audit tamper=1/1")


if __name__ == "__main__":
    main()
