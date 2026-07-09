#!/usr/bin/env python3
"""Current branch-level frontier ledger for h=3 repeat-boundary."""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_repeat_loose_branch_degree_compiler import branch_degree_budget
from f3_h3_repeat_loose_generic_degree_compiler import generic_rows as loose_generic_rows
from f3_h3_repeat_loose_rank_minor_compiler import minor_degree_row
from f3_h3_repeat_loose_secondary_payment import secondary_payments
from f3_h3_repeat_loose_stepanov_compiler import sample_targets
from f3_h3_repeat_same_lambda_degree_compiler import generic_budget, scale_branch_budget
from f3_h3_repeat_same_lambda_orbit_domain import generic_off_orbit_product, poly_degrees
from f3_h3_repeat_same_lambda_scale_count import scale_collision_pair_bound, scale_orbit_bound
from f3_h3_repeat_lambda_one_scale_h2_cap import (
    combined_scale_orbit_bound,
    combined_scale_pair_bound,
    scale_h2_cap_summary,
)
from f3_h3_repeat_slope_branch_assembly import BRANCHES as SLOPE_BRANCHES
from f3_h3_repeat_slope_equality_factorization import (
    verify_generic_factorization,
    verify_mixed_factorization,
    verify_scale_source_mixed_factorization,
)
from f3_h3_repeat_same_lambda_j_invariant import (
    verify_j_separates_orbits,
    verify_reciprocal_product_formula,
)


@dataclass(frozen=True)
class FrontierGate:
    name: str
    interface: str
    membership_total: int
    extra_total: int


def strict_frontier_gates() -> tuple[FrontierGate, ...]:
    same_generic = generic_budget()
    same_scale = scale_branch_budget()
    off_total = poly_degrees(generic_off_orbit_product())[2]
    slope_gg = SLOPE_BRANCHES["generic-generic"]
    slope_mixed = SLOPE_BRANCHES["mixed"]
    loose_generic_total = sum(row.total_degree for row in loose_generic_rows())
    loose_a = branch_degree_budget("A")
    loose_b = branch_degree_budget("B")
    return (
        FrontierGate(
            "H3-VALUE-GEN-INJECTIVE",
            "generic same-lambda ratio collision",
            same_generic["sum_total"],
            off_total,
        ),
        FrontierGate(
            "H3-VALUE-SCALE-INJECTIVE",
            "lambda=1 primitive-cube scale collision",
            same_scale["sum_total"],
            3,
        ),
        FrontierGate(
            "H3-SLOPE-GG-HIT",
            "generic-generic lambda-distinct slope hit",
            slope_gg.membership_total,
            slope_gg.hit_product_total,
        ),
        FrontierGate(
            "H3-SLOPE-MIXED-HIT",
            "generic/scale lambda-distinct slope hit",
            slope_mixed.membership_total,
            slope_mixed.hit_product_total,
        ),
        FrontierGate(
            "LOOSE-GEN-RANK/NV",
            "generic two-parameter loose nine-slope target",
            loose_generic_total,
            0,
        ),
        FrontierGate(
            "LOOSE-A-RANK/NV",
            "clean branch-A one-parameter loose eight-slope target",
            loose_a.sum_total_degrees,
            0,
        ),
        FrontierGate(
            "LOOSE-B-RANK/NV",
            "clean branch-B one-parameter loose eight-slope target",
            loose_b.sum_total_degrees,
            0,
        ),
    )


def count_route_frontier_gates() -> tuple[FrontierGate, ...]:
    return tuple(
        gate
        for gate in strict_frontier_gates()
        if gate.name != "H3-VALUE-SCALE-INJECTIVE"
    )


def rank_minor_rows() -> dict[str, tuple[int, int, int]]:
    return {
        target.name: (
            minor_degree_row(target).rank_target,
            minor_degree_row(target).entry_parameter_degree,
            minor_degree_row(target).minor_total_degree,
        )
        for target in sample_targets()
    }


def paid_ledgers(n: int) -> dict[str, int]:
    scale_refined = scale_h2_cap_summary()
    return {
        "scale_orbits": combined_scale_orbit_bound(n),
        "scale_collision_pairs": combined_scale_pair_bound(n),
        "scale_trivial_orbits": scale_orbit_bound(n),
        "scale_trivial_collision_pairs": scale_collision_pair_bound(n),
        "scale_h2_first_better_s": scale_refined["first_h2_better_s"],
        "loose_secondary_points": sum(row.point_bound(n) for row in secondary_payments()),
    }


def slope_factorization_summary() -> dict[str, int]:
    generic = verify_generic_factorization()
    mixed = verify_mixed_factorization()
    mixed_reverse = verify_scale_source_mixed_factorization()
    return {
        "generic_product_total": sum(generic.values()),
        "mixed_product_total": sum(mixed.values()),
        "mixed_reverse_product_total": sum(mixed_reverse.values()),
        "generic_rows": len(generic),
        "mixed_rows": len(mixed),
        "mixed_reverse_rows": len(mixed_reverse),
    }


def same_lambda_j_summary() -> dict[str, int]:
    product_degrees = verify_reciprocal_product_formula()
    j_degrees = verify_j_separates_orbits()
    return {
        "r_degree_a": product_degrees[0],
        "r_degree_z": product_degrees[1],
        "r_total": product_degrees[2],
        "j_difference_total": j_degrees[2],
    }


def main() -> None:
    print("h=3 repeat frontier ledger")
    gates = strict_frontier_gates()
    expected = {
        "H3-VALUE-GEN-INJECTIVE": (14, 10),
        "H3-VALUE-SCALE-INJECTIVE": (6, 3),
        "H3-SLOPE-GG-HIT": (14, 41),
        "H3-SLOPE-MIXED-HIT": (10, 27),
        "LOOSE-GEN-RANK/NV": (15, 0),
        "LOOSE-A-RANK/NV": (22, 0),
        "LOOSE-B-RANK/NV": (24, 0),
    }
    actual = {gate.name: (gate.membership_total, gate.extra_total) for gate in gates}
    if actual != expected:
        raise AssertionError(actual)
    print("strict_branch_frontier:")
    for gate in gates:
        print(
            f"  {gate.name}: {gate.interface}; "
            f"membership_S_total={gate.membership_total}; extra_total={gate.extra_total}"
        )
    count_route = count_route_frontier_gates()
    if len(count_route) != 6:
        raise AssertionError(count_route)
    if any(gate.name == "H3-VALUE-SCALE-INJECTIVE" for gate in count_route):
        raise AssertionError(count_route)
    print("count_route_frontier:")
    print("  H3-VALUE-SCALE-INJECTIVE: replaced by paid scale-collision count")
    for gate in count_route:
        print(f"  {gate.name}: still open on the count route")

    same_lambda_j = same_lambda_j_summary()
    if same_lambda_j != {
        "r_degree_a": 3,
        "r_degree_z": 6,
        "r_total": 7,
        "j_difference_total": 10,
    }:
        raise AssertionError(same_lambda_j)
    print(
        "same_lambda_j_invariant: "
        f"R_degrees=({same_lambda_j['r_degree_a']},{same_lambda_j['r_degree_z']},"
        f"{same_lambda_j['r_total']}) "
        f"J_difference_total={same_lambda_j['j_difference_total']}"
    )

    slope_factors = slope_factorization_summary()
    if slope_factors != {
        "generic_product_total": 41,
        "mixed_product_total": 27,
        "mixed_reverse_product_total": 27,
        "generic_rows": 3,
        "mixed_rows": 3,
        "mixed_reverse_rows": 3,
    }:
        raise AssertionError(slope_factors)
    print(
        "slope_equality_factorization: "
        f"generic_rows={slope_factors['generic_rows']} "
        f"generic_product_total={slope_factors['generic_product_total']} "
        f"mixed_rows={slope_factors['mixed_rows']} "
        f"mixed_product_total={slope_factors['mixed_product_total']} "
        f"mixed_reverse_rows={slope_factors['mixed_reverse_rows']} "
        f"mixed_reverse_product_total={slope_factors['mixed_reverse_product_total']}"
    )

    minor_rows = rank_minor_rows()
    expected_minors = {
        "generic": (1061, 1470, 1559670),
        "branch_A": (1057, 2127, 2248239),
        "branch_B": (1057, 2319, 2451183),
    }
    if minor_rows != expected_minors:
        raise AssertionError(minor_rows)
    print("loose_rank_minor_sample_box:")
    for label, (rank_target, entry_degree, minor_degree) in minor_rows.items():
        print(
            f"  {label}: rank_target={rank_target} "
            f"entry_degree={entry_degree} minor_degree<={minor_degree}"
        )

    first_official = 2**13
    ledgers = paid_ledgers(first_official)
    if ledgers["scale_collision_pairs"] >= first_official * first_official:
        raise AssertionError(ledgers)
    if ledgers["loose_secondary_points"] >= first_official * first_official:
        raise AssertionError(ledgers)
    print(
        "paid_ledgers_first_official: "
        f"scale_orbits<={ledgers['scale_orbits']} "
        f"scale_pairs<={ledgers['scale_collision_pairs']} "
        f"scale_h2_first_better=2^{ledgers['scale_h2_first_better_s']} "
        f"loose_secondary<={ledgers['loose_secondary_points']}"
    )
    print("H3_REPEAT_FRONTIER_LEDGER_PASS")


if __name__ == "__main__":
    main()
