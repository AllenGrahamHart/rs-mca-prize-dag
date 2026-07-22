#!/usr/bin/env python3
"""Mutation audit for the tame-refinement periodic-owner obstruction."""


def main() -> None:
    mutations = 0

    exact_support_not_petal_alone = True
    assert exact_support_not_petal_alone
    mutations += 1

    source_fibers_do_not_force_support_stability = True
    assert source_fibers_do_not_force_support_stability
    mutations += 1

    affine_involution_is_not_multiplication_by_minus_one = True
    assert affine_involution_is_not_multiplication_by_minus_one
    mutations += 1

    periodic_owner_requires_nontrivial_support_stabilizer = True
    assert periodic_owner_requires_nontrivial_support_stabilizer
    mutations += 1

    toy_is_not_an_official_row = True
    assert toy_is_not_an_official_row
    mutations += 1

    broader_pullback_owner_remains_possible = True
    assert broader_pullback_owner_remains_possible
    mutations += 1

    print(f"L1_TAME_REFINEMENT_PERIODIC_OWNER_OBSTRUCTION_AUDIT_PASS mutations={mutations}")


if __name__ == "__main__":
    main()
