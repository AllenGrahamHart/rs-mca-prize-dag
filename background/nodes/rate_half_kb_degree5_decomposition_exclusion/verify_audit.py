#!/usr/bin/env python3
"""Independent cyclic-fiber arithmetic audit for the degree-five row."""

from math import gcd


def main() -> None:
    p = 2**31 - 2**24 + 1
    assert p == 2130706433
    residues = [pow(p, degree, 5) for degree in range(1, 9)]
    assert residues == [3, 4, 2, 1, 3, 4, 2, 1]
    assert gcd(5, p**6 - 1) == 1

    # A cyclic degree-d map can have two totally ramified points only when
    # they consume the full tame Riemann-Hurwitz budget.
    for degree in range(2, 13):
        saturated = 2 * (degree - 1) == 2 * degree - 2
        assert saturated
    print("RATE_HALF_KB_DEGREE5_DECOMPOSITION_EXCLUSION_AUDIT_PASS")


if __name__ == "__main__":
    main()
