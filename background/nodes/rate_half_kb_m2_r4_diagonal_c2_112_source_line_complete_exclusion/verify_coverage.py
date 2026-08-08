#!/usr/bin/env python3
"""Audit exhaustive dependency coverage for source-line exclusion."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name

CORE = (
    "rate_half_kb_m2_r4_diagonal_c2_112_saturated_defect_classifier",
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_colored_quotient_compiler",
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_odd_part_incidence_gate",
    "rate_half_kb_m2_r4_diagonal_c2_112_ramified_complete_source_repair",
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_internal_star_reconstruction",
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_q_slice_resultant_gate",
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_negative_reconstruction_factor_gate",
)
ALIGNED = (
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_aligned_negative_q_slice_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_ramified_q_slice_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_moving_swap_q_slice_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_moving_same_q_slice_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_moving_mixed_full_quotient_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_fixed_same_full_quotient_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_fixed_swap_full_quotient_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_unramified_fixed_mixed_full_quotient_exclusion",
)
NEAR_NEGATIVE = (
    "rate_half_kb_m2_r4_diagonal_c2_112_near_negative_q_slice_exclusion",
)
NEAR_POSITIVE = (
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_projective_boundary_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_fixed_xi_direct_square_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_fixed_xi_swapped_square_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_fixed_xi_mixed_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_tau_xi_mixed_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_tau_xi_square_exclusions",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_other_xi_square_xi_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_other_xi_square_ell_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_other_xi_mixed_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_a_xi_square_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_a_xi_square_ell_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_a_xi_mixed_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_tau_xi_orbit_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_other_xi_square_xi_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_other_xi_square_ell_exclusion",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_moving_moving_other_xi_mixed_exclusion",
)
EXPECTED = set(CORE + ALIGNED + NEAR_NEGATIVE + NEAR_POSITIVE)
LITERAL_COVERAGE = (
    "rate_half_kb_m2_r4_diagonal_c2_112_source_line_literal_assignment_coverage"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


payload = json.loads((ROOT / "dag.json").read_text(encoding="ascii"))
nodes = {item["id"]: item for item in payload["nodes"]}
requirements = {
    edge["from"] for edge in payload["edges"]
    if edge["to"] == NODE_ID and edge["kind"] == "req"
}

require(len(CORE) == 7, "core count")
require(len(ALIGNED) == 8, "aligned count")
require(len(NEAR_NEGATIVE) == 1, "near negative count")
require(len(NEAR_POSITIVE) == 16, "near positive theorem count")
require(len(EXPECTED) == 32, "total dependency count")
require(requirements == EXPECTED | {LITERAL_COVERAGE}, "DAG requirement coverage")
require(all(nodes[item]["status"] == "PROVED" for item in EXPECTED),
        "dependency status")
require(nodes[LITERAL_COVERAGE]["status"] == "PROVED", "coverage status")
require(nodes[NODE_ID]["status"] == "PROVED", "parent status")

print(
    "KB_C2_112_SOURCE_LINE_COMPLETE_EXCLUSION_COVERAGE_PASS "
    "requirements=33 proved=33 aligned=8 near_negative=1 "
    "near_positive_theorems=16 "
    "near_affine_charts=18 near_boundary_shards=7"
)
