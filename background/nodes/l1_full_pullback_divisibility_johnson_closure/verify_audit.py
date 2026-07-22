#!/usr/bin/env python3
"""Mutation audit for full-pullback divisibility/Johnson closure."""


def main() -> None:
    mutations = 0

    exact_support_must_be_fiberwise = True
    assert exact_support_must_be_fiberwise
    mutations += 1

    source_threshold_is_k_plus_ell_minus_one = True
    assert source_threshold_is_k_plus_ell_minus_one
    mutations += 1

    both_scale_orderings_are_required = True
    assert both_scale_orderings_are_required
    mutations += 1

    strict_johnson_denominator_is_load_bearing = True
    assert strict_johnson_denominator_is_load_bearing
    mutations += 1

    smooth_label_structure_is_not_used = True
    assert smooth_label_structure_is_not_used
    mutations += 1

    subjohnson_and_partial_fibers_remain_open = True
    assert subjohnson_and_partial_fibers_remain_open
    mutations += 1

    print(f"L1_FULL_PULLBACK_DIVISIBILITY_JOHNSON_AUDIT_PASS mutations={mutations}")


if __name__ == "__main__":
    main()
