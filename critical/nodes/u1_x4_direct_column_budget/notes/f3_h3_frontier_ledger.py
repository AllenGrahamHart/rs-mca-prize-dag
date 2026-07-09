#!/usr/bin/env python3
"""Compile the current h=3 frontier for the F3 flip attempt.

This ledger imports existing compilers and records the current proof surface.
It proves no new rank theorem and no new geometric batching theorem.
"""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_activation_bound_compiler import (
    first_n_below_floor,
    load_summary,
    prime_activation_counts,
)
from f3_h3_activation_orbit_dedup import activation_orbit_dedup_summary
from f3_h3_official_accident_slack import official_accident_slack_summary
from f3_h3_conic_bridge_accounting_ledger import conic_bridge_accounting_summary
from f3_h3_bridge_budget_lineage import budget_lineage_summary
from f3_h3_exact_profile_bridge_contract import exact_profile_bridge_contract_summary
from f3_h3_l2_levelset_bridge_compiler import (
    check_ledger,
    synthetic_ledgers,
)
from f3_h3_nondiagonal_highrow_budget import EXPECTED_ROWS as HIGH_ROWS
from f3_h3_nondiagonal_lowrow_budget import EXPECTED_ROWS as LOW_ROWS
from f3_h3_private_linear_lowrow_budget import EXPECTED_ROWS as PRIVATE_ROWS
from f3_h3_private_linear_official_separation_guard import (
    separation_summary as private_separation_summary,
)
from f3_h3_private_linear_rank_deficit_budget import (
    private_rank_deficit_budget_summary,
)
from f3_h3_rank_effective_bridge import EXPECTED_CAPACITIES, PINNED_RANKS, rank_capacity
from f3_h3_exact_profile_bridge_budget import exact_profile_budget_summary
from f3_h3_exact_profile_4096_budget_floor import retarget_summary as exact_4096_summary
from f3_h3_exact_profile_4096_rank_deficit_budget import (
    retarget_deficit_summary as exact_4096_deficit_summary,
)
from f3_h3_conic_chart_linear_relation_guard import linear_relation_guard_summary
from f3_h3_conic_chart_largegap_pilot import largegap_pilot_summary
from f3_h3_conic_binary_form_target import conic_binary_form_summary
from f3_h3_conic_sixa_threshold_target import official_sixa_summary
from f3_h3_conic_rational_curve_interface import conic_rational_curve_summary
from f3_h3_conic_dual_annihilator_target import conic_dual_annihilator_summary
from f3_h3_conic_box_basepoint_free import conic_box_basepoint_free_summary
from f3_h3_conic_kernel_bundle_reduction import conic_kernel_bundle_summary
from f3_h3_conic_kernel_bundle_4096_reduction import conic_kernel_4096_summary
from f3_h3_exact_profile_rank_capacity_guard import exact_profile_capacity_guard_summary
from f3_h3_exact_profile_rank_deficit_budget import rank_deficit_budget_summary
from f3_h3_conic_chart_rank_minor_certificate import EXPECTED_DETERMINANT as TOY_CONIC_MINOR_DET
from f3_h3_rc_rank_generic_open import (
    PINNED_DEGREE2_CONIC_CHART_RANK,
)
from f3_h3_rich_curve_condition_profile import condition_profile_summary
from f3_h3_repeat_frontier_ledger import (
    count_route_frontier_gates,
    paid_ledgers,
    same_lambda_j_summary,
    slope_factorization_summary,
    strict_frontier_gates,
)
from f3_h3_repeat_loose_branch_geometry import branch_geometry_summary
from f3_h3_repeat_loose_shared_core_degree import loose_shared_core_summary
from f3_h3_repeat_loose_shared_core_rank_target import shared_core_rank_summary


@dataclass(frozen=True)
class H3FrontierGate:
    name: str
    status: str
    evidence: str
    residual: str


def activation_summary() -> dict[str, int]:
    data = load_summary()
    counts = prime_activation_counts(data)
    dedup = activation_orbit_dedup_summary()
    slack = official_accident_slack_summary()
    max_prime, max_count = max(counts.items(), key=lambda item: (item[1], -item[0]))
    if data["activation_exception_count"] != 720:
        raise AssertionError(data["activation_exception_count"])
    if max_count != 92 or max_prime != 37633:
        raise AssertionError((max_prime, max_count))
    if dedup["max_prime"] != max_prime:
        raise AssertionError((dedup, max_prime))
    if dedup["max_deduped_per_prime"] != 27 or dedup["unique_orbits"] != 167:
        raise AssertionError(dedup)
    if first_n_below_floor(16) != 17:
        raise AssertionError(first_n_below_floor(16))
    if slack["midpoint_c"] != 4096 or slack["min_max_safe_c"] != 8191:
        raise AssertionError(slack)
    return {
        "n": data["n"],
        "oriented_activations": data["activation_exception_count"],
        "activation_primes": len(counts),
        "max_prime": max_prime,
        "max_count": max_count,
        "deduped_orbits": dedup["unique_orbits"],
        "max_deduped_count": dedup["max_deduped_per_prime"],
        "repeated_deduped_orbits": dedup["repeated_orbits"],
        "c16_threshold": 17,
        "official_midpoint_c": slack["midpoint_c"],
        "official_max_safe_c": slack["min_max_safe_c"],
        "official_midpoint_first_ratio_ppm": slack["first_midpoint_ratio_ppm"],
    }


def official_budget_summary() -> dict[str, int]:
    rows = (*LOW_ROWS, *HIGH_ROWS)
    private = tuple(PRIVATE_ROWS)
    lineage = budget_lineage_summary()
    exact_contract = exact_profile_bridge_contract_summary()
    exact_profile = exact_profile_budget_summary()
    exact_4096 = exact_4096_summary()
    exact_4096_deficit = exact_4096_deficit_summary()
    conic_relation = linear_relation_guard_summary()
    conic_largegap = largegap_pilot_summary()
    conic_binary = conic_binary_form_summary()
    conic_sixa = official_sixa_summary()
    conic_curve = conic_rational_curve_summary()
    conic_dual = conic_dual_annihilator_summary()
    conic_basepoint = conic_box_basepoint_free_summary()
    conic_kernel = conic_kernel_bundle_summary()
    conic_kernel_4096 = conic_kernel_4096_summary()
    exact_capacity = exact_profile_capacity_guard_summary()
    exact_deficit = rank_deficit_budget_summary()
    private_deficit = private_rank_deficit_budget_summary()
    exponents = [row.s for row in rows]
    private_exponents = [row.s for row in private]
    expected = list(range(13, 42))
    if exponents != expected:
        raise AssertionError(exponents)
    if private_exponents != expected:
        raise AssertionError(private_exponents)
    if exact_4096["budget_multiplier"] != 64 or exact_4096["target_c"] != 4096:
        raise AssertionError(exact_4096)
    if exact_4096_deficit["min_allowed_deficit"] != 2899:
        raise AssertionError(exact_4096_deficit)
    if conic_kernel_4096["allowance"] != 2899:
        raise AssertionError(conic_kernel_4096)
    return {
        "first_s": 13,
        "last_s": 41,
        "z_budget_min": min(row.z for row in rows),
        "z_budget_max": max(row.z for row in rows),
        "diagonal_z_budget_min": lineage["diagonal_min"],
        "diagonal_z_budget_max": lineage["diagonal_max"],
        "z_private_min": min(row.z for row in private),
        "z_private_max": max(row.z for row in private),
        "z_exact_profile_min": exact_profile["exact_min"],
        "z_exact_profile_max": exact_profile["exact_max"],
        "z_exact_profile_gain_total": exact_profile["gain_total"],
        "z_exact_4096_min": exact_4096["min_z"],
        "z_exact_4096_max": exact_4096["max_z"],
        "z_exact_4096_multiplier": exact_4096["budget_multiplier"],
        "z_exact_4096_max_ratio_ppm": exact_4096["max_ratio_ppm"],
        "exact_4096_min_allowed_deficit": exact_4096_deficit[
            "min_allowed_deficit"
        ],
        "exact_profile_contract_rows": exact_contract["rows"],
        "exact_profile_contract_l2_target": exact_contract["l2_target_multiplier"],
        "exact_profile_degree_capacity_min": exact_capacity["degree_space_capacity_min"],
        "exact_profile_degree_capacity_max": exact_capacity["degree_space_capacity_max"],
        "exact_profile_collapsed_capacity_max": exact_capacity["collapsed_capacity_max"],
        "exact_profile_min_allowed_deficit": exact_deficit["min_allowed_deficit"],
        "private_min_allowed_deficit": private_deficit["min_allowed_deficit"],
        "private_deficit_tight_s": private_deficit["tight_s"],
        "conic_relation_gcd_checks": conic_relation["pairwise_gcd_checks"],
        "conic_relation_max_gcd_degree": conic_relation["max_gcd_degree"],
        "conic_largegap_cases": conic_largegap["cases"],
        "conic_largegap_max_deficit": conic_largegap["max_pilot_deficit"],
        "conic_largegap_full_cases": conic_largegap["full_cases"],
        "conic_largegap_official_min_gap_ppm": conic_largegap[
            "official_min_gap_ppm"
        ],
        "conic_binary_span_rank": conic_binary["quadratic_span_rank"],
        "conic_binary_allowed_codimension": conic_binary["allowed_codimension"],
        "conic_sixa_official_margin": conic_sixa["min_margin"],
        "conic_curve_box_margin": conic_curve["min_box_column_margin"],
        "conic_curve_linear_defect": conic_curve["min_linear_normality_defect"],
        "conic_dual_allowance": conic_dual["allowance"],
        "conic_dual_min_base_products": conic_dual["min_base_products"],
        "conic_basepoint_min_b": conic_basepoint["official_min_b"],
        "conic_kernel_balanced_margin": conic_kernel["min_balanced_margin"],
        "conic_kernel_max_slope": conic_kernel["max_balanced_slope"],
        "conic_kernel_4096_allowance": conic_kernel_4096["allowance"],
        "conic_kernel_4096_balanced_margin": conic_kernel_4096[
            "min_balanced_margin"
        ],
        "conic_kernel_4096_max_slope": conic_kernel_4096["max_balanced_slope"],
        "conic_kernel_4096_margin_minus_allowance": conic_kernel_4096[
            "min_margin_minus_allowance"
        ],
        "toy_conic_chart_rank": PINNED_DEGREE2_CONIC_CHART_RANK,
        "toy_conic_chart_minor_det": TOY_CONIC_MINOR_DET,
        "private_separation_margin": private_separation_summary()["min_pass_margin"],
    }


def rank_capacity_summary() -> dict[str, int]:
    actual = {name: rank_capacity(rank) for name, rank in PINNED_RANKS.items()}
    if actual != EXPECTED_CAPACITIES:
        raise AssertionError(actual)
    return {
        "collapsed_capacity": actual["constant-ratio collapsed"],
        "private_capacity": actual["private-divisor rational"],
        "random_capacity": actual["repaired random full-rank"],
    }


def l2_bridge_summary() -> dict[str, int]:
    rows = [check_ledger(name, n, r_values) for name, n, r_values in synthetic_ledgers()]
    boundary = rows[2]
    if boundary["pairs"] != 1024 or boundary["exact_numer"] != 73728:
        raise AssertionError(boundary)
    return {
        "target_multiplier": 1152,
        "pair_target_multiplier": 16,
        "synthetic_ledgers": len(rows),
        "boundary_pairs": boundary["pairs"],
    }


def repeat_frontier_summary() -> dict[str, tuple[int, int]]:
    expected = {
        "H3-VALUE-GEN-INJECTIVE": (14, 10),
        "H3-VALUE-SCALE-INJECTIVE": (6, 3),
        "H3-SLOPE-GG-HIT": (14, 41),
        "H3-SLOPE-MIXED-HIT": (10, 27),
        "LOOSE-GEN-RANK/NV": (15, 0),
        "LOOSE-A-RANK/NV": (22, 0),
        "LOOSE-B-RANK/NV": (24, 0),
    }
    actual = {
        gate.name: (gate.membership_total, gate.extra_total)
        for gate in strict_frontier_gates()
    }
    if actual != expected:
        raise AssertionError(actual)
    return actual


def repeat_count_route_summary() -> dict[str, int]:
    count_route = count_route_frontier_gates()
    ledgers = paid_ledgers(2**13)
    if len(count_route) != 6:
        raise AssertionError(count_route)
    if ledgers["scale_collision_pairs"] != 3725085:
        raise AssertionError(ledgers)
    return {
        "open_gates": len(count_route),
        "scale_pairs_first_official": ledgers["scale_collision_pairs"],
        "scale_h2_first_better_s": ledgers["scale_h2_first_better_s"],
    }


def repeat_slope_summary() -> dict[str, int]:
    summary = slope_factorization_summary()
    expected = {
        "generic_product_total": 41,
        "mixed_product_total": 27,
        "mixed_reverse_product_total": 27,
        "generic_rows": 3,
        "mixed_rows": 3,
        "mixed_reverse_rows": 3,
    }
    if summary != expected:
        raise AssertionError(summary)
    return summary


def repeat_loose_geometry_summary() -> dict[str, int]:
    geometry = branch_geometry_summary()
    expected_geometry = {
        "shared_slope_maps": 6,
        "branch_a_private_slope_maps": 2,
        "branch_b_private_slope_maps": 2,
        "active_finite_ramification_points": 0,
        "finite_checks": 186,
    }
    if geometry != expected_geometry:
        raise AssertionError(geometry)
    shared = loose_shared_core_summary()
    expected_shared = {
        "shared_maps": 6,
        "shared_sum_a": 10,
        "shared_sum_total": 14,
        "shared_max_total": 5,
        "branch_a_private_maps": 2,
        "branch_a_private_sum_a": 7,
        "branch_a_private_sum_total": 8,
        "branch_a_private_max_total": 5,
        "branch_b_private_maps": 2,
        "branch_b_private_sum_a": 9,
        "branch_b_private_sum_total": 10,
        "branch_b_private_max_total": 7,
        "branch_a_full_total": 22,
        "branch_b_full_total": 24,
    }
    if shared != expected_shared:
        raise AssertionError(shared)
    rank = shared_core_rank_summary()
    expected_rank = {
        "maps": 6,
        "parameter_blocks": 1,
        "parameter_sum_total": 14,
        "coefficients": 33_554_432,
        "conditions": 1048,
        "x_degree": 1087,
        "point_bound_num": 1087,
        "point_bound_den": 2,
        "rank_capacity_slack": 40,
        "cleared_total_degree": 1870,
        "rank_target": 1049,
        "entry_parameter_degree": 1359,
        "minor_total_degree": 1_425_591,
    }
    if rank != expected_rank:
        raise AssertionError(rank)
    return {**geometry, **shared, **{f"shared_core_rank_{k}": v for k, v in rank.items()}}


def rich_curve_condition_summary() -> dict[str, int]:
    summary = condition_profile_summary()
    if summary["legacy_c_red"] != 13:
        raise AssertionError(summary)
    if summary["sample_rows"] != 5:
        raise AssertionError(summary)
    return summary


def repeat_value_summary() -> dict[str, int]:
    summary = same_lambda_j_summary()
    expected = {
        "r_degree_a": 3,
        "r_degree_z": 6,
        "r_total": 7,
        "j_difference_total": 10,
        "j_critical_points": 3,
        "j_active_critical_points": 0,
        "j_critical_value_num": 27,
        "j_critical_value_den": 4,
        "product_active_critical_points": 0,
        "product_finite_generic_checks": 174,
    }
    if summary != expected:
        raise AssertionError(summary)
    return summary


def frontier_gates(
    activation: dict[str, int],
    budgets: dict[str, int],
    capacity: dict[str, int],
    l2: dict[str, int],
    conic: dict[str, int],
    repeat: dict[str, tuple[int, int]],
    repeat_count: dict[str, int],
    repeat_value: dict[str, int],
    repeat_slope: dict[str, int],
    repeat_loose: dict[str, int],
    rich_curve_conditions: dict[str, int],
) -> tuple[H3FrontierGate, ...]:
    return (
        H3FrontierGate(
            "H3-ACT-COMPILER",
            "REPLAYED/CONDITIONAL",
            (
                f"C=16 gives T3<n^3 from n>={activation['c16_threshold']}; "
                f"official rows only need C<={activation['official_max_safe_c']} "
                f"and C={activation['official_midpoint_c']} uses "
                f"{activation['official_midpoint_first_ratio_ppm']} ppm "
                "of the first-row budget; "
                f"n=96 evidence has max {activation['max_count']} oriented "
                f"activations and max {activation['max_deduped_count']} "
                "deduped affine/Galois pair-orbits at one prime"
            ),
            "prove official-row H3-ACT(4096), the stronger H3-ACT(16), or replace with certificates",
        ),
        H3FrontierGate(
            "F3-RANK-AVOID / RC-NV",
            "OPEN",
            (
                f"non-diagonal official budgets cover s={budgets['first_s']}..{budgets['last_s']} "
                f"with Z={budgets['z_budget_min']}..{budgets['z_budget_max']}; "
                f"exact-profile arithmetic raises this to "
                f"Z={budgets['z_exact_profile_min']}.."
                f"{budgets['z_exact_profile_max']} "
                f"(total gain {budgets['z_exact_profile_gain_total']}); "
                f"official H3-ACT(4096) has a constructive exact-profile "
                f"floor Z={budgets['z_exact_4096_min']}.."
                f"{budgets['z_exact_4096_max']} "
                f"({budgets['z_exact_4096_multiplier']}x, "
                f"max ratio {budgets['z_exact_4096_max_ratio_ppm']} ppm, "
                f"rank-deficit tolerance "
                f"{budgets['exact_4096_min_allowed_deficit']}); "
                f"official exact-profile boxes have one-image degree-space "
                f"capacity {budgets['exact_profile_degree_capacity_min']}.."
                f"{budgets['exact_profile_degree_capacity_max']} and "
                f"constant-ratio collapsed capacity "
                f"{budgets['exact_profile_collapsed_capacity_max']}; "
                f"bounded rank-deficit tolerance is at least "
                f"{budgets['exact_profile_min_allowed_deficit']}; "
                f"conic chart has affine relation with "
                f"{budgets['conic_relation_gcd_checks']} pairwise gcd checks "
                f"and max gcd degree {budgets['conic_relation_max_gcd_degree']}; "
                f"large-gap conic pilot has max deficit "
                f"{budgets['conic_largegap_max_deficit']} across "
                f"{budgets['conic_largegap_cases']} cases "
                f"(official min H/A ppm "
                f"{budgets['conic_largegap_official_min_gap_ppm']}); "
                f"conic binary-form target has quadratic span rank "
                f"{budgets['conic_binary_span_rank']} and allowed codimension "
                f"{budgets['conic_binary_allowed_codimension']}; "
                f"six-A conic guardrail has official min H-6A margin "
                f"{budgets['conic_sixa_official_margin']} "
                f"but six-A alone is not sufficient outside dense boxes; "
                f"conic rational-curve interface has box column margin "
                f"{budgets['conic_curve_box_margin']} and linear-normality "
                f"defect {budgets['conic_curve_linear_defect']}; "
                f"conic dual-annihilator target allows dimension "
                f"{budgets['conic_dual_allowance']} against at least "
                f"{budgets['conic_dual_min_base_products']} product windows; "
                f"boxed conic products are basepoint-free under pairwise gcd "
                f"with official min B {budgets['conic_basepoint_min_b']}; "
                f"kernel-bundle reduction has balanced full-window slope at "
                f"most {budgets['conic_kernel_max_slope']} and min A-slope "
                f"margin {budgets['conic_kernel_balanced_margin']}; "
                f"the H3-ACT(4096) boxes retune this to allowance "
                f"{budgets['conic_kernel_4096_allowance']}, max slope "
                f"{budgets['conic_kernel_4096_max_slope']}, min margin "
                f"{budgets['conic_kernel_4096_balanced_margin']} "
                f"(margin minus allowance "
                f"{budgets['conic_kernel_4096_margin_minus_allowance']}); "
                f"toy same-fiber conic chart has full rank "
                f"{budgets['toy_conic_chart_rank']}=A B^3 "
                f"with minor det {budgets['toy_conic_chart_minor_det']} mod 769; "
                f"exact RC-RED profile uses "
                f"{rich_curve_conditions['min_exact_to_legacy_percent'] / 100:.2f}.."
                f"{rich_curve_conditions['max_exact_to_legacy_percent'] / 100:.2f}% "
                "of the legacy condition count on sample boxes"
            ),
            "prove finite-row rank-good minor nonvanishing on repaired degree-2 signature-curve images",
        ),
        H3FrontierGate(
            "H3-BRIDGE-RANKCAP",
            "OPEN",
            (
                f"rank-effective capacities are pinned: collapsed={capacity['collapsed_capacity']}, "
                f"private={capacity['private_capacity']}, random={capacity['random_capacity']}; "
                f"conic keys are charged once for {conic['sample_fibers']} replayed fibers; "
                f"L2 target is sum R_z(R_z-6)<={l2['target_multiplier']}n; "
                f"exact-profile contract keeps Z_exact distinct from the L2 target "
                f"on {budgets['exact_profile_contract_rows']} official rows"
            ),
            "assign activated non-toral shape pairs to repaired chart images with total rank capacity within the official budget",
        ),
        H3FrontierGate(
            "F3-PRIVATE-LINEAR-RANK-AVOID",
            "OPEN/ALTERNATE",
            (
                f"private-linear budgets cover s={budgets['first_s']}..{budgets['last_s']} "
                f"with Z={budgets['z_private_min']}..{budgets['z_private_max']}; "
                f"official separation margin={budgets['private_separation_margin']}; "
                f"bounded rank-deficit tolerance is "
                f"{budgets['private_min_allowed_deficit']} "
                f"(tight at s={budgets['private_deficit_tight_s']})"
            ),
            "prove finite-row minor nonvanishing on the three-parameter private-linear normal-form image, plus the matching bridge",
        ),
        H3FrontierGate(
            "H3-REPEAT-BOUNDARY-STAR",
            "OPEN FRONTIER",
            (
                f"{len(repeat)} strict branch gates replayed; count route leaves "
                f"{repeat_count['open_gates']} gates after paying scale pairs; "
                f"h2 scale cap improves from 2^{repeat_count['scale_h2_first_better_s']}; "
                f"same-lambda J quotient total={repeat_value['j_difference_total']}; "
                f"J critical value={repeat_value['j_critical_value_num']}/"
                f"{repeat_value['j_critical_value_den']} "
                f"(active critical points={repeat_value['j_active_critical_points']}); "
                f"product active critical points={repeat_value['product_active_critical_points']}; "
                f"slope factorization totals are generic={repeat_slope['generic_product_total']} "
                f"and mixed={repeat_slope['mixed_product_total']} "
                f"(reverse={repeat_slope['mixed_reverse_product_total']}); "
                f"loose branches share {repeat_loose['shared_slope_maps']} slope maps "
                f"with active finite ramification={repeat_loose['active_finite_ramification_points']}; "
                f"shared-core S_total={repeat_loose['shared_sum_total']} and private "
                f"S_totals A/B={repeat_loose['branch_a_private_sum_total']}/"
                f"{repeat_loose['branch_b_private_sum_total']}; "
                f"shared-core sample rank target="
                f"{repeat_loose['shared_core_rank_rank_target']} "
                f"with slack={repeat_loose['shared_core_rank_rank_capacity_slack']}"
            ),
            "prove or replace the strict same-lambda, slope, and loose-triangle branch gates needed by the star route",
        ),
    )


def main() -> None:
    activation = activation_summary()
    budgets = official_budget_summary()
    capacity = rank_capacity_summary()
    l2 = l2_bridge_summary()
    conic = conic_bridge_accounting_summary()
    repeat = repeat_frontier_summary()
    repeat_count = repeat_count_route_summary()
    repeat_value = repeat_value_summary()
    repeat_slope = repeat_slope_summary()
    repeat_loose = repeat_loose_geometry_summary()
    rich_curve_conditions = rich_curve_condition_summary()
    gates = frontier_gates(
        activation,
        budgets,
        capacity,
        l2,
        conic,
        repeat,
        repeat_count,
        repeat_value,
        repeat_slope,
        repeat_loose,
        rich_curve_conditions,
    )

    print("F3 h=3 frontier ledger")
    print(
        f"activation evidence: n={activation['n']} "
        f"oriented={activation['oriented_activations']} "
        f"primes={activation['activation_primes']} "
        f"max={activation['max_count']} at p={activation['max_prime']} "
        f"dedup_orbits={activation['deduped_orbits']} "
        f"dedup_max={activation['max_deduped_count']} "
        f"dedup_repeats={activation['repeated_deduped_orbits']} "
        f"official_midpoint_C={activation['official_midpoint_c']} "
        f"official_max_safe_C={activation['official_max_safe_c']}"
    )
    print(
        "official rank-capacity budgets: "
        f"Z_budget={budgets['z_budget_min']}..{budgets['z_budget_max']} "
        f"Z_exact_profile={budgets['z_exact_profile_min']}.."
        f"{budgets['z_exact_profile_max']} "
        f"Z_exact_4096_floor={budgets['z_exact_4096_min']}.."
        f"{budgets['z_exact_4096_max']} "
        f"(legacy_diag={budgets['diagonal_z_budget_min']}..{budgets['diagonal_z_budget_max']}) "
        f"Z_private={budgets['z_private_min']}..{budgets['z_private_max']} "
        f"private_sep_margin={budgets['private_separation_margin']} "
        f"exact_4096_deficit_min={budgets['exact_4096_min_allowed_deficit']} "
        f"conic_4096_margin={budgets['conic_kernel_4096_balanced_margin']} "
        f"private_deficit_min={budgets['private_min_allowed_deficit']}"
    )
    print(
        "rank-effective capacities: "
        f"collapsed={capacity['collapsed_capacity']} "
        f"private={capacity['private_capacity']} random={capacity['random_capacity']}"
    )
    print(
        "L2 bridge target: "
        f"sum R_z(R_z-6) <= {l2['target_multiplier']} n "
        f"equiv P_total <= {l2['pair_target_multiplier']} n"
    )
    print(
        "conic bridge accounting: "
        f"degree_bound={conic['degree_bound']} "
        f"sample_fibers={conic['sample_fibers']} "
        f"ordered={conic['sample_ordered_triples']} "
        f"chart={conic['sample_chart_points']} "
        f"vertical_losses={conic['sample_vertical_losses']} "
        "basepoint_multiplier=not_charged"
    )
    print("repeat-boundary strict gates:")
    for name, (membership, extra) in repeat.items():
        print(f"  {name}: membership_total={membership} extra_total={extra}")
    print(
        "repeat-boundary count route: "
        f"open_gates={repeat_count['open_gates']} "
        f"scale_pairs_first_official<={repeat_count['scale_pairs_first_official']} "
        f"h2_scale_cap_first_better=2^{repeat_count['scale_h2_first_better_s']}"
    )
    print(
        "repeat-boundary loose branch geometry: "
        f"shared_slope_maps={repeat_loose['shared_slope_maps']} "
        f"branch_A_private={repeat_loose['branch_a_private_slope_maps']} "
        f"branch_B_private={repeat_loose['branch_b_private_slope_maps']} "
        f"active_finite_ramification_points="
        f"{repeat_loose['active_finite_ramification_points']} "
        f"shared_core_total={repeat_loose['shared_sum_total']} "
        f"private_totals=({repeat_loose['branch_a_private_sum_total']},"
        f"{repeat_loose['branch_b_private_sum_total']}) "
        f"shared_core_rank_target={repeat_loose['shared_core_rank_rank_target']} "
        f"rank_slack={repeat_loose['shared_core_rank_rank_capacity_slack']}"
    )
    print(
        "rich-curve condition profile: "
        f"exact_to_legacy_percent="
        f"{rich_curve_conditions['min_exact_to_legacy_percent'] / 100:.2f}.."
        f"{rich_curve_conditions['max_exact_to_legacy_percent'] / 100:.2f} "
        f"total_saved_conditions={rich_curve_conditions['total_saved_conditions']}"
    )
    print("frontier gates:")
    for gate in gates:
        print(f"{gate.name}: {gate.status}")
        print(f"  evidence: {gate.evidence}")
        print(f"  residual: {gate.residual}")
    print("H3_FRONTIER_LEDGER_PASS")


if __name__ == "__main__":
    main()
