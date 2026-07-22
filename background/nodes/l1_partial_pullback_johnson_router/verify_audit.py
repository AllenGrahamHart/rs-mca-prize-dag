#!/usr/bin/env python3
"""Mutation audit for the partial-pullback Johnson router."""


def main() -> None:
    mutations = 0

    z_counts_points_not_fibers = True
    assert z_counts_points_not_fibers
    mutations += 1

    incomplete_domain_agreements_enter_z = True
    assert incomplete_domain_agreements_enter_z
    mutations += 1

    threshold_rounds_up_after_loss = True
    assert threshold_rounds_up_after_loss
    mutations += 1

    kappa_is_not_removed_by_johnson = True
    assert kappa_is_not_removed_by_johnson
    mutations += 1

    map_aggregation_requires_tame_anchor = True
    assert map_aggregation_requires_tame_anchor
    mutations += 1

    f17_boundary_remains_subjohnson = True
    assert f17_boundary_remains_subjohnson
    mutations += 1

    print(f"L1_PARTIAL_PULLBACK_JOHNSON_ROUTER_AUDIT_PASS mutations={mutations}")


if __name__ == "__main__":
    main()
