#!/usr/bin/env python3
"""Tamper audit for all-padding subtraction."""


def main():
    e = 101
    for d_a in (0, 1):
        cap = 2 * e - 5 if d_a == 0 else e - 3
        exceptional = e - 3 if d_a == 0 else 0
        total_padding = e - 6 - d_a
        assert cap - exceptional - total_padding == 4

        # Leaving one positive-excess padding unit uncharged reproduces the
        # old loose bound and must fail the exact-four assertion.
        assert cap - exceptional - (total_padding - 1) == 5
    print("PASS extremal exact four-core audit tamper=1/1")


if __name__ == "__main__":
    main()
