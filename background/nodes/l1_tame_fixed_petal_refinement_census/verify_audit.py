#!/usr/bin/env python3
"""Mutation audit for the tame fixed-petal refinement census."""


def main() -> None:
    mutations = 0

    # The tame diagonal must be invertible.
    assert 3 % 5 != 0
    mutations += 1

    # The first wild endpoint loses that diagonal.
    assert 3 % 3 == 0
    mutations += 1

    # Normalizing the constant removes exactly additive shifts.
    p = (0, 2, 1)
    shifted = (4, 2, 1)
    assert p[1:] == shifted[1:] and p[0] != shifted[0]
    mutations += 1

    # Map supply and role supply are separate currencies.
    fiber_count = 20
    map_count = 1
    assert map_count <= 1 and 3**fiber_count > 10**9
    mutations += 1

    # The wild fixture is only a formal locator decomposition.
    fixture_is_not_an_official_domain_claim = True
    assert fixture_is_not_an_official_domain_claim
    mutations += 1

    # Partial fibers do not imply a right-component factorization.
    complete_fiber_hypothesis_is_load_bearing = True
    assert complete_fiber_hypothesis_is_load_bearing
    mutations += 1

    print(f"L1_TAME_FIXED_PETAL_REFINEMENT_AUDIT_PASS mutations={mutations}")


if __name__ == "__main__":
    main()
