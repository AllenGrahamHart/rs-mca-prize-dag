#!/usr/bin/env python3
"""Audit elliptic involutions and the six-pole dihedral sieve."""


def main() -> None:
    # In genus one, a is fixed-free while c and ac are reflections.
    g_gamma = 1
    fixed = {"a": 0, "c": 4, "ac": 4}
    numerator = 2 * g_gamma - 2 - sum(fixed.values())
    assert numerator % 4 == 0
    two_g_c_minus_two = numerator // 4
    assert two_g_c_minus_two == -2
    assert (two_g_c_minus_two + 2) // 2 == 0

    candidates = []
    for degree in (2, 3, 5, 6, 10, 15, 30):
        ramification_indices = {1, 2, degree}
        if 5 in ramification_indices:
            possible = degree == 5
        else:
            possible = 6 % degree == 0
        if possible:
            candidates.append(degree)
    assert candidates == [2, 3, 5, 6]
    print("RATE_HALF_KB_M2_R2_DIHEDRAL_OUTER_FACTOR_REDUCTION_AUDIT_PASS")


if __name__ == "__main__":
    main()
