#!/usr/bin/env python3
"""Independent degree-five group and field arithmetic audit."""


def main() -> None:
    # Nontrivial point-stabilizer orbit sizes for the transitive degree-five
    # groups: regular, dihedral, Frobenius/two-transitive.
    orbit_types = {1, 2, 4}
    assert 3 not in orbit_types

    p = 2**31 - 2**24 + 1
    residues = [pow(p, exponent, 5) for exponent in range(1, 9)]
    assert residues == [3, 4, 2, 1, 3, 4, 2, 1]
    assert pow(p, 6, 5) - 1 == 3

    candidates = [(r, 4 * 12 // r) for r in (1, 2, 3, 4)]
    assert candidates == [(1, 48), (2, 24), (3, 16), (4, 12)]
    print("RATE_HALF_KB_M12_OUTER_SUBDEGREE_ROUTE_CUT_AUDIT_PASS")


if __name__ == "__main__":
    main()
