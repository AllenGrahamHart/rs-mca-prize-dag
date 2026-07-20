#!/usr/bin/env python3
"""Mutation audit for the two-petal small-support closure."""


def premises(ell: int, a: int, z: int, r: int, d: int) -> bool:
    return (
        1 <= z <= a <= ell
        and 0 <= r < ell
        and a <= d
        and r <= d
        and a + z + r >= ell + d
    )


def conclusion(ell: int, a: int, z: int, r: int, d: int) -> bool:
    return (
        d <= ell + z - 1
        and ell - r <= z
        and ell - a <= z
        and (ell - r) + (ell - a) <= 2 * z
    )


def main() -> None:
    controls = [
        (8, 7, 1, 7, 7),
        (8, 8, 1, 7, 8),
        (8, 6, 2, 6, 6),
        (8, 8, 2, 6, 8),
    ]
    for case in controls:
        assert premises(*case)
        assert conclusion(*case)

    # Dropping a<=d permits the background-deficit conclusion to fail.
    no_petal_cap = (8, 8, 1, 0, 1)
    assert no_petal_cap[0] - no_petal_cap[3] > no_petal_cap[2]

    # Dropping r<=d permits the largest-petal-deficit conclusion to fail.
    no_root_cap = (8, 1, 1, 7, 1)
    assert no_root_cap[0] - no_root_cap[1] > no_root_cap[2]

    # Allowing r=ell loses the sharp ell+z-1 defect ceiling.
    nonmaximal = (8, 8, 1, 8, 9)
    assert nonmaximal[4] > nonmaximal[0] + nonmaximal[2] - 1

    print("L1_TWO_PETAL_SMALL_SUPPORT_AUDIT_PASS mutations=3")


if __name__ == "__main__":
    main()
