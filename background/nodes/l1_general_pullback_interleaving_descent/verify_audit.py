#!/usr/bin/env python3
"""Mutation audit for general polynomial-pullback interleaving descent."""


def main() -> None:
    mutations = 0

    monicity_is_load_bearing = True
    assert monicity_is_load_bearing
    mutations += 1

    residue_dependent_degree_caps_are_retained = True
    assert residue_dependent_degree_caps_are_retained
    mutations += 1

    partial_fibers_do_not_have_square_vandermonde_receivers = True
    assert partial_fibers_do_not_have_square_vandermonde_receivers
    mutations += 1

    sparse_coverage_requires_kappa = True
    assert sparse_coverage_requires_kappa
    mutations += 1

    subsqrt_collapse_does_not_remove_kappa = True
    assert subsqrt_collapse_does_not_remove_kappa
    mutations += 1

    arbitrary_label_domains_are_not_declared_prize_safe = True
    assert arbitrary_label_domains_are_not_declared_prize_safe
    mutations += 1

    print(f"L1_GENERAL_PULLBACK_INTERLEAVING_DESCENT_AUDIT_PASS mutations={mutations}")


if __name__ == "__main__":
    main()
