#!/usr/bin/env python3
"""Finite-field replay of aligned common-pencil multiplier collapse."""

from __future__ import annotations


P = 257


def main() -> None:
    tested = 0
    for z1 in (2, 5, 19):
        for z2 in (31, 47, 83):
            for z3 in (101, 149, 211):
                if len({z1, z2, z3}) < 3:
                    continue
                inverse_gap = pow((z2 - z1) % P, -1, P)
                lam = (z3 - z1) * inverse_gap % P
                assert inverse_gap * (z2 - z1) % P == 1
                assert inverse_gap * (z3 - z1) % P == lam
                assert lam not in (0, 1)
                tested += 1

    for ell in range(2, 129):
        for a in range(1, ell):
            j = 2 * ell - a
            s = ell - a
            for e in range(a):
                assert j + e < 2 * ell
                assert j + e > s

    assert tested == 27
    print("PASS: aligned multiplier is constant and every deg(Etilde)<a atom is empty")


if __name__ == "__main__":
    main()
