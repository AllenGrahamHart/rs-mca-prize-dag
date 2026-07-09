#!/usr/bin/env python3
"""Pin the h=3 rank-avoidance interface needed to close H3-ACT(16)."""

from __future__ import annotations

from f3_h3_nondiagonal_highrow_budget import EXPECTED_ROWS as HIGH_ROWS
from f3_h3_nondiagonal_lowrow_budget import C_RED, H3_ACT_C, EXPECTED_ROWS as LOW_ROWS
from f3_h3_nondiagonal_lowrow_budget import witness_bound
from f3_h3_exact_profile_bridge_budget import exact_profile_budget_summary
from f3_h3_exact_profile_rank_capacity_guard import (
    exact_profile_capacity_guard_summary,
)
from f3_h3_exact_profile_rank_deficit_budget import rank_deficit_budget_summary
from f3_h3_conic_chart_linear_relation_guard import linear_relation_guard_summary
from f3_h3_private_linear_bad_prime_guardrail import EXPECTED_RANKS as BAD_PRIME_RANKS
from f3_h3_private_linear_lowrow_budget import EXPECTED_ROWS as PRIVATE_ROWS
from f3_h3_private_linear_lowrow_budget import feasible_witness as private_feasible_witness
from f3_h3_private_linear_rank_deficit_budget import (
    private_rank_deficit_budget_summary,
)


def main() -> None:
    rows = (*LOW_ROWS, *HIGH_ROWS)
    private_rows = tuple(PRIVATE_ROWS)
    exponents = [row.s for row in rows]
    private_exponents = [row.s for row in private_rows]
    expected_exponents = list(range(13, 42))
    if exponents != expected_exponents:
        raise AssertionError((exponents, expected_exponents))
    if private_exponents != expected_exponents:
        raise AssertionError((private_exponents, expected_exponents))

    print("h=3 rank-avoidance interface")
    print(f"C_red={C_RED} H3_ACT_C={H3_ACT_C}")
    print("non-diagonal degree-2 route")
    print(" s          n       Z_budget       bound          16n      A      B       D")
    min_z = None
    max_z = None
    for row in rows:
        n = 2**row.s
        target = H3_ACT_C * n
        bound, conditions, coeffs, image_cap = witness_bound(
            n, row.z, row.a, row.b, row.d
        )
        if bound != row.bound:
            raise AssertionError((row.s, bound, row.bound))
        if not (bound <= target < row.next_bound):
            raise AssertionError((row.s, bound, target, row.next_bound))
        if not (conditions < coeffs and conditions < image_cap):
            raise AssertionError((row.s, conditions, coeffs, image_cap))
        min_z = row.z if min_z is None else min(min_z, row.z)
        max_z = row.z if max_z is None else max(max_z, row.z)
        print(
            f"{row.s:2d} {n:10d} {row.z:14d} {bound:11d} "
            f"{target:12d} {row.a:6d} {row.b:6d} {row.d:8d}"
        )

    if min_z != 16 or max_z != 10795:
        raise AssertionError((min_z, max_z))

    exact_profile = exact_profile_budget_summary()
    exact_capacity = exact_profile_capacity_guard_summary()
    exact_deficit = rank_deficit_budget_summary()
    conic_relation = linear_relation_guard_summary()
    private_deficit = private_rank_deficit_budget_summary()
    if exact_profile["exact_min"] != 33 or exact_profile["exact_max"] != 21421:
        raise AssertionError(exact_profile)
    if exact_capacity["degree_space_capacity_min"] != 1:
        raise AssertionError(exact_capacity)
    if exact_capacity["degree_space_capacity_max"] != 1:
        raise AssertionError(exact_capacity)
    if exact_capacity["collapsed_capacity_max"] != 0:
        raise AssertionError(exact_capacity)
    if exact_deficit["min_allowed_deficit"] != 1847:
        raise AssertionError(exact_deficit)
    if private_deficit["min_allowed_deficit"] != 25:
        raise AssertionError(private_deficit)
    print("exact-profile degree-2 route")
    print(
        " official rows s=13..41 "
        f"Z_exact={exact_profile['exact_min']}..{exact_profile['exact_max']} "
        f"total_gain={exact_profile['gain_total']} "
        f"one_image_degree_capacity={exact_capacity['degree_space_capacity_min']}.."
        f"{exact_capacity['degree_space_capacity_max']} "
        f"collapsed_capacity_max={exact_capacity['collapsed_capacity_max']} "
        f"allowed_rank_deficit_min={exact_deficit['min_allowed_deficit']}"
    )
    print(
        "conic-chart relation guard: "
        f"pairwise_gcd_checks={conic_relation['pairwise_gcd_checks']} "
        f"max_gcd_degree={conic_relation['max_gcd_degree']} "
        f"degree_guard_failures={conic_relation['degree_guard_failures']} "
        f"pilot_failures={conic_relation['pilot_failures']}"
    )
    print(
        "private-linear bounded-deficit route: "
        f"allowed_rank_deficit_min={private_deficit['min_allowed_deficit']} "
        f"tight_s={private_deficit['tight_s']} "
        f"rank_room_min={private_deficit['min_rank_room']}"
    )

    private_min_z = None
    private_max_z = None
    print("private-linear route")
    print(" s          n     Z_private       bound          16n      A      B       D")
    for row in private_rows:
        n = 2**row.s
        target = H3_ACT_C * n
        witness = private_feasible_witness(n, row.z, row.b, row.d)
        expected_witness = (row.bound, row.a, row.b, row.d)
        if witness != expected_witness:
            raise AssertionError((row.s, witness, expected_witness))
        if not (row.bound <= target < row.next_bound):
            raise AssertionError((row.s, row.bound, target, row.next_bound))
        private_min_z = row.z if private_min_z is None else min(private_min_z, row.z)
        private_max_z = row.z if private_max_z is None else max(private_max_z, row.z)
        print(
            f"{row.s:2d} {n:10d} {row.z:13d} {row.bound:11d} "
            f"{target:12d} {row.a:6d} {row.b:6d} {row.d:8d}"
        )

    if private_min_z != 23 or private_max_z != 15267:
        raise AssertionError((private_min_z, private_max_z))
    if not (BAD_PRIME_RANKS[1009] < BAD_PRIME_RANKS[1013]):
        raise AssertionError(BAD_PRIME_RANKS)

    print("official h=3 rows covered by all three conditional arithmetic routes: s=13..41")
    print("exact-profile degree-2 route is the strongest current conditional route")
    print("rank theorem must be finite-row minor nonvanishing, not only char-zero fullness")
    print(
        "theorem interface: legacy degree-2, exact-profile degree-2, or private-linear "
        "rank-avoidance, plus the matching bridge, implies H3-ACT(16)"
    )
    print("H3_RANK_AVOID_INTERFACE_PASS")


if __name__ == "__main__":
    main()
