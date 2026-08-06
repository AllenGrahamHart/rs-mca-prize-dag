#!/usr/bin/env python3
"""Compile the h=3 conic-side bridge accounting facts already proved."""

from __future__ import annotations

from f3_h3_conic_basepoint_equivalence import verify_h_fiber_row
from f3_h3_conic_chart_hpoint_coverage import verify_row as verify_coverage_row
from f3_h3_conic_degree2_chart import verify_chart_identities
from f3_h3_l2_levelset_bridge_compiler import check_ledger
from f3_h3_pair_count_from_charts_compiler import verify_row as verify_pair_row


EXPECTED_DEGREE = {"b": 1, "checked_t": 17, "skipped_poles": 0}
EXPECTED_COVERAGE = {
    "fibers": 8,
    "ordered": 96,
    "chart": 88,
    "epsilon": 8,
    "skipped_poles": 16,
    "skipped_degenerate": 0,
}
EXPECTED_BASEPOINTS = {
    "fibers": 8,
    "basepoint_checks": 24,
    "skipped_degenerate": 0,
}
EXPECTED_PAIRS = {
    "fibers": 8,
    "total_t": 88,
    "total_r": 96,
    "max_t": 11,
    "max_r": 12,
    "pairs": 8,
    "exact_bound": 16,
    "chart_bound": 16,
    "exact_numer": 1152,
    "chart_numer": 1152,
    "skipped_degenerate": 0,
}
EXPECTED_L2 = {
    "charts": 1024,
    "pairs": 1024,
    "exact_numer": 73728,
    "square_numer": 147456,
    "safe": 1,
    "exact_safe": 1,
    "square_safe": 0,
    "tail_levels": 1,
    "max_tail": 1024,
}


def conic_bridge_accounting_summary() -> dict[str, int]:
    degree = verify_chart_identities(17, 4, 2, 5)
    if degree != EXPECTED_DEGREE:
        raise AssertionError(("degree chart drift", degree))

    coverage = verify_coverage_row(97, 16, max_fibers=8)
    if coverage != EXPECTED_COVERAGE:
        raise AssertionError(("coverage drift", coverage))
    if coverage["ordered"] != coverage["chart"] + coverage["epsilon"]:
        raise AssertionError(("coverage identity drift", coverage))

    basepoints = verify_h_fiber_row(97, 16, max_fibers=8)
    if basepoints != EXPECTED_BASEPOINTS:
        raise AssertionError(("basepoint drift", basepoints))
    if basepoints["basepoint_checks"] != 3 * basepoints["fibers"]:
        raise AssertionError(("basepoint multiplier drift", basepoints))

    pairs = verify_pair_row(97, 16, max_fibers=8)
    if pairs != EXPECTED_PAIRS:
        raise AssertionError(("pair-count drift", pairs))
    pair_l2_numer = 72 * pairs["pairs"]
    if pair_l2_numer > pairs["exact_numer"]:
        raise AssertionError(("pair numerator drift", pairs))

    l2 = check_ledger("boundary_exact", 64, [12] * 1024)
    if l2 != EXPECTED_L2:
        raise AssertionError(("L2 target drift", l2))

    return {
        "degree_bound": 2,
        "sample_fibers": coverage["fibers"],
        "sample_ordered_triples": coverage["ordered"],
        "sample_chart_points": coverage["chart"],
        "sample_vertical_losses": coverage["epsilon"],
        "basepoint_checks": basepoints["basepoint_checks"],
        "sample_pair_count": pairs["pairs"],
        "sample_pair_l2_numer": pair_l2_numer,
        "sample_bound_numer": pairs["exact_numer"],
        "target_l2_multiplier": 1152,
        "target_pair_multiplier": 16,
        "boundary_pairs": l2["pairs"],
    }


def main() -> None:
    row = conic_bridge_accounting_summary()
    print("h=3 conic bridge accounting ledger")
    print(
        f"degree_bound={row['degree_bound']} "
        f"sample_fibers={row['sample_fibers']} "
        f"ordered={row['sample_ordered_triples']} "
        f"chart={row['sample_chart_points']} "
        f"vertical_losses={row['sample_vertical_losses']}"
    )
    print(
        f"basepoint_checks={row['basepoint_checks']} "
        "basepoint_multiplier=not_charged"
    )
    print(
        f"sample_pairs={row['sample_pair_count']} "
        f"sample_pair_l2_numer={row['sample_pair_l2_numer']} "
        f"sample_bound_numer={row['sample_bound_numer']} "
        f"target=sum R_z(R_z-6)<={row['target_l2_multiplier']} n "
        f"equiv P_total<={row['target_pair_multiplier']} n"
    )
    print(f"boundary_exact_pairs={row['boundary_pairs']}")
    print("residual: global assignment of activated non-toral pairs to repaired conic images")
    print("H3_CONIC_BRIDGE_ACCOUNTING_LEDGER_PASS")


if __name__ == "__main__":
    main()
