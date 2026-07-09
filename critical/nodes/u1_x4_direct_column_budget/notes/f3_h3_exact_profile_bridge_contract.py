#!/usr/bin/env python3
"""Contract ledger for the h=3 exact-profile bridge route."""

from __future__ import annotations

from f3_h3_bridge_budget_lineage import budget_lineage_summary
from f3_h3_exact_profile_bridge_budget import exact_profile_budget_summary
from f3_h3_exact_profile_rank_capacity_guard import (
    exact_profile_capacity_guard_summary,
)
from f3_h3_exact_profile_rank_deficit_budget import rank_deficit_budget_summary
from f3_h3_l2_levelset_bridge_compiler import check_ledger, synthetic_ledgers
from f3_h3_rich_curve_condition_profile import condition_profile_summary


def l2_contract_summary() -> dict[str, int]:
    rows = [check_ledger(name, n, r_values) for name, n, r_values in synthetic_ledgers()]
    boundary = rows[2]
    if boundary["pairs"] != 1024 or boundary["exact_numer"] != 73728:
        raise AssertionError(boundary)
    return {
        "target_multiplier": 1152,
        "pair_target_multiplier": 16,
        "boundary_pairs": boundary["pairs"],
        "boundary_exact_numer": boundary["exact_numer"],
    }


def exact_profile_bridge_contract_summary() -> dict[str, int]:
    lineage = budget_lineage_summary()
    exact = exact_profile_budget_summary()
    capacity = exact_profile_capacity_guard_summary()
    deficit = rank_deficit_budget_summary()
    l2 = l2_contract_summary()
    profile = condition_profile_summary()

    row_span = (exact["rows"], exact["first_s"], exact["last_s"])
    if row_span != (capacity["rows"], capacity["first_s"], capacity["last_s"]):
        raise AssertionError((row_span, capacity))
    if row_span != (deficit["rows"], deficit["first_s"], deficit["last_s"]):
        raise AssertionError((row_span, deficit))
    if row_span != (29, 13, 41):
        raise AssertionError(row_span)

    exact_range = (exact["exact_min"], exact["exact_max"])
    if exact_range != (capacity["z_min"], capacity["z_max"]):
        raise AssertionError((exact_range, capacity))
    if exact_range != (deficit["min_z"], deficit["max_z"]):
        raise AssertionError((exact_range, deficit))
    if (exact["old_min"], exact["old_max"]) != (
        lineage["nondiagonal_min"],
        lineage["nondiagonal_max"],
    ):
        raise AssertionError((exact, lineage))

    if capacity["degree_space_capacity_min"] != 1:
        raise AssertionError(capacity)
    if capacity["degree_space_capacity_max"] != 1:
        raise AssertionError(capacity)
    if capacity["collapsed_capacity_max"] != 0:
        raise AssertionError(capacity)
    if deficit["min_allowed_deficit"] != 1847:
        raise AssertionError(deficit)
    if exact["gain_total"] != 51451:
        raise AssertionError(exact)
    if profile["legacy_c_red"] != 13:
        raise AssertionError(profile)

    return {
        "rows": row_span[0],
        "first_s": row_span[1],
        "last_s": row_span[2],
        "legacy_z_min": lineage["nondiagonal_min"],
        "legacy_z_max": lineage["nondiagonal_max"],
        "diagonal_z_min": lineage["diagonal_min"],
        "diagonal_z_max": lineage["diagonal_max"],
        "exact_z_min": exact["exact_min"],
        "exact_z_max": exact["exact_max"],
        "exact_gain_total": exact["gain_total"],
        "degree_space_capacity": capacity["degree_space_capacity_min"],
        "collapsed_capacity_max": capacity["collapsed_capacity_max"],
        "min_allowed_deficit": deficit["min_allowed_deficit"],
        "l2_target_multiplier": l2["target_multiplier"],
        "pair_target_multiplier": l2["pair_target_multiplier"],
        "legacy_c_red": profile["legacy_c_red"],
    }


def main() -> None:
    summary = exact_profile_bridge_contract_summary()
    print("h=3 exact-profile bridge contract")
    print(
        f"official_rows=s={summary['first_s']}..{summary['last_s']} "
        f"count={summary['rows']}"
    )
    print(
        "rank-family budget: "
        f"Z_exact={summary['exact_z_min']}..{summary['exact_z_max']} "
        f"(legacy_non_diagonal={summary['legacy_z_min']}.."
        f"{summary['legacy_z_max']}, gain_total={summary['exact_gain_total']})"
    )
    print(
        "one-image capacity guard: "
        f"degree_space_capacity={summary['degree_space_capacity']} "
        f"collapsed_capacity_max={summary['collapsed_capacity_max']} "
        f"min_allowed_deficit={summary['min_allowed_deficit']}"
    )
    print(
        "separate L2 target: "
        f"sum R_z(R_z-6) <= {summary['l2_target_multiplier']} n "
        f"equiv P_total <= {summary['pair_target_multiplier']} n"
    )
    print("contract: spend Z_exact on distinct rank-effective repaired images")
    print("do not treat Z_exact as an L2 pair-count bound")
    print("H3_EXACT_PROFILE_BRIDGE_CONTRACT_PASS")


if __name__ == "__main__":
    main()
