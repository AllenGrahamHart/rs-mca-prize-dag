#!/usr/bin/env python3
"""Basepoint-free guard for the h=3 conic boxed product series."""

from __future__ import annotations

from f3_h3_conic_chart_linear_relation_guard import linear_relation_guard_summary
from f3_h3_exact_profile_bridge_budget import EXPECTED_ROWS


def conic_box_basepoint_free_summary() -> dict[str, int]:
    relation = linear_relation_guard_summary()
    if relation["max_gcd_degree"] != 0:
        raise AssertionError(relation)
    min_b = min(row.b for row in EXPECTED_ROWS)
    if min_b < 2:
        raise AssertionError(min_b)
    return {
        "pairwise_gcd_checks": relation["pairwise_gcd_checks"],
        "max_gcd_degree": relation["max_gcd_degree"],
        "official_rows": len(EXPECTED_ROWS),
        "official_min_b": min_b,
        "official_max_b": max(row.b for row in EXPECTED_ROWS),
    }


def main() -> None:
    summary = conic_box_basepoint_free_summary()
    print("h=3 conic boxed-product basepoint-free guard")
    print(
        "pairwise-coprime P_U,P_V,P_W,Q imply the boxed products have no "
        "common base point"
    )
    print(
        f"pairwise_gcd_checks={summary['pairwise_gcd_checks']} "
        f"max_gcd_degree={summary['max_gcd_degree']} "
        f"official_B={summary['official_min_b']}.."
        f"{summary['official_max_b']}"
    )
    print("H3_CONIC_BOX_BASEPOINT_FREE_PASS")


if __name__ == "__main__":
    main()
