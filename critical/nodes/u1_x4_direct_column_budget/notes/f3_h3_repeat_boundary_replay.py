#!/usr/bin/env python3
"""Replay the h=3 repeat-boundary proof chain."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]


COMMANDS = [
    (
        "h2 affine coset-pair Stepanov corollary",
        "f3_h2_affine_coset_pair_stepanov.py",
        "H2_AFFINE_COSET_PAIR_STEPANOV_PASS",
    ),
    (
        "h3 moment bookkeeping identity",
        "f3_h3_moment_bookkeeping_identity.py",
        "H3_MOMENT_BOOKKEEPING_IDENTITY_PASS",
    ),
    (
        "h3 repeat-residue boundary compiler",
        "f3_h3_repeat_residue_boundary_compiler.py",
        "H3_REPEAT_RESIDUE_BOUNDARY_COMPILER_PASS",
    ),
    (
        "h3 repeat-boundary line compiler",
        "f3_h3_repeat_boundary_line_compiler.py",
        "H3_REPEAT_BOUNDARY_LINE_COMPILER_PASS",
    ),
    (
        "h3 repeat edge reciprocal form",
        "f3_h3_repeat_edge_reciprocal_form.py",
        "H3_REPEAT_EDGE_RECIPROCAL_FORM_PASS",
    ),
    (
        "h3 repeat edge cubic gcd form",
        "f3_h3_repeat_edge_cubic_gcd_form.py",
        "H3_REPEAT_EDGE_CUBIC_GCD_FORM_PASS",
    ),
    (
        "h3 repeat pair-intersection compiler",
        "f3_h3_repeat_pair_intersection_compiler.py",
        "H3_REPEAT_PAIR_INTERSECTION_COMPILER_PASS",
    ),
    (
        "h3 repeat lambda-fiber ledger",
        "f3_h3_repeat_lambda_fiber_ledger.py",
        "H3_REPEAT_LAMBDA_FIBER_LEDGER_PASS",
    ),
    (
        "h3 repeat quadratic-rho compiler",
        "f3_h3_repeat_quadratic_rho_compiler.py",
        "H3_REPEAT_QUADRATIC_RHO_COMPILER_PASS",
    ),
    (
        "h3 repeat affine value-slope compiler",
        "f3_h3_repeat_affine_value_slope_compiler.py",
        "H3_REPEAT_AFFINE_VALUE_SLOPE_COMPILER_PASS",
    ),
    (
        "h3 repeat reciprocal-product compiler",
        "f3_h3_repeat_reciprocal_product_compiler.py",
        "H3_REPEAT_RECIPROCAL_PRODUCT_COMPILER_PASS",
    ),
    (
        "h3 repeat lambda-root fiber compiler",
        "f3_h3_repeat_lambda_root_fiber_compiler.py",
        "H3_REPEAT_LAMBDA_ROOT_FIBER_COMPILER_PASS",
    ),
    (
        "h3 repeat lambda-ratio parametrization",
        "f3_h3_repeat_lambda_ratio_parametrization.py",
        "H3_REPEAT_LAMBDA_RATIO_PARAMETRIZATION_PASS",
    ),
    (
        "h3 repeat lambda-ratio membership compiler",
        "f3_h3_repeat_lambda_ratio_membership_compiler.py",
        "H3_REPEAT_LAMBDA_RATIO_MEMBERSHIP_COMPILER_PASS",
    ),
    (
        "h3 repeat lambda-ratio orbit compiler",
        "f3_h3_repeat_lambda_ratio_orbit_compiler.py",
        "H3_REPEAT_LAMBDA_RATIO_ORBIT_COMPILER_PASS",
    ),
    (
        "h3 repeat lambda=1 scale compiler",
        "f3_h3_repeat_lambda_one_scale_compiler.py",
        "H3_REPEAT_LAMBDA_ONE_SCALE_COMPILER_PASS",
    ),
    (
        "h3 repeat same-lambda collision system",
        "f3_h3_repeat_same_lambda_collision_system.py",
        "H3_REPEAT_SAME_LAMBDA_COLLISION_SYSTEM_PASS",
    ),
    (
        "h3 repeat slope-ratio compiler",
        "f3_h3_repeat_slope_ratio_compiler.py",
        "H3_REPEAT_SLOPE_RATIO_COMPILER_PASS",
    ),
    (
        "h3 repeat slope numerator compiler",
        "f3_h3_repeat_slope_numerator_compiler.py",
        "H3_REPEAT_SLOPE_NUMERATOR_COMPILER_PASS",
    ),
    (
        "h3 repeat-boundary LP4 Stepanov compiler",
        "f3_h3_repeat_boundary_lp4_stepanov_compiler.py",
        "H3_REPEAT_BOUNDARY_LP4_STEPANOV_COMPILER_PASS",
    ),
    (
        "h3 repeat-boundary q0 cell",
        "f3_h3_repeat_boundary_q0_cell.py",
        "H3_REPEAT_BOUNDARY_Q0_CELL_PASS",
    ),
    (
        "h3 repeat-boundary fiber cap",
        "f3_h3_repeat_boundary_fiber_cap.py",
        "H3_REPEAT_BOUNDARY_FIBER_CAP_PASS",
    ),
    (
        "h3 repeat-boundary support symmetry",
        "f3_h3_repeat_boundary_support_symmetry.py",
        "H3_REPEAT_BOUNDARY_SUPPORT_SYMMETRY_PASS",
    ),
    (
        "h3 repeat-boundary LP4 rank guardrail",
        "f3_h3_repeat_boundary_lp4_rank_guardrail.py",
        "H3_REPEAT_BOUNDARY_LP4_RANK_GUARDRAIL_PASS",
    ),
    (
        "h3 repeat-boundary support compiler",
        "f3_h3_repeat_boundary_support_compiler.py",
        "H3_REPEAT_BOUNDARY_SUPPORT_COMPILER_PASS",
    ),
    (
        "h3 repeat-support boundary evidence",
        "f3_h3_repeat_support_boundary_evidence.py",
        "H3_REPEAT_SUPPORT_BOUNDARY_EVIDENCE_PASS",
    ),
    (
        "h3 repeat-support forced-point reduction",
        "f3_h3_repeat_support_forced_point_reduction.py",
        "H3_REPEAT_SUPPORT_FORCED_POINT_REDUCTION_PASS",
    ),
    (
        "h3 repeat forced-fiber Stepanov compiler",
        "f3_h3_repeat_forced_fiber_stepanov_compiler.py",
        "H3_REPEAT_FORCED_FIBER_STEPANOV_COMPILER_PASS",
    ),
    (
        "h3 repeat forced-fiber degree bound",
        "f3_h3_repeat_forced_fiber_degree_bound.py",
        "H3_REPEAT_FORCED_FIBER_DEGREE_BOUND_PASS",
    ),
    (
        "h3 repeat forced-cover crossover",
        "f3_h3_repeat_forced_cover_crossover.py",
        "H3_REPEAT_FORCED_COVER_CROSSOVER_PASS",
    ),
    (
        "h3 repeat coordinate-cover ledger",
        "f3_h3_repeat_coordinate_cover_ledger.py",
        "H3_REPEAT_COORDINATE_COVER_LEDGER_PASS",
    ),
    (
        "h3 repeat coordinate-hitting ledger",
        "f3_h3_repeat_coordinate_hitting_ledger.py",
        "H3_REPEAT_COORDINATE_HITTING_LEDGER_PASS",
    ),
    (
        "h3 repeat forced-coordinate-2 normal form",
        "f3_h3_repeat_forced_two_normal_form.py",
        "H3_REPEAT_FORCED_TWO_NORMAL_FORM_PASS",
    ),
    (
        "h3 repeat hitting exception scan",
        "f3_h3_repeat_hitting_exception_scan.py",
        "H3_REPEAT_HITTING_EXCEPTION_SCAN_PASS",
    ),
    (
        "h3 repeat singleton-hitting stress",
        "f3_h3_repeat_singleton_hitting_stress.py",
        "H3_REPEAT_SINGLETON_HITTING_STRESS_PASS",
    ),
    (
        "h3 repeat star-obstruction compiler",
        "f3_h3_repeat_star_obstruction_compiler.py",
        "H3_REPEAT_STAR_OBSTRUCTION_COMPILER_PASS",
    ),
    (
        "h3 repeat star-obstruction taxonomy",
        "f3_h3_repeat_star_obstruction_taxonomy.py",
        "H3_REPEAT_STAR_OBSTRUCTION_TAXONOMY_PASS",
    ),
    (
        "h3 repeat pairwise-coreless compiler",
        "f3_h3_repeat_pairwise_coreless_compiler.py",
        "H3_REPEAT_PAIRWISE_CORELESS_COMPILER_PASS",
    ),
    (
        "h3 repeat coreless-pattern compiler",
        "f3_h3_repeat_coreless_pattern_compiler.py",
        "H3_REPEAT_CORELESS_PATTERN_COMPILER_PASS",
    ),
    (
        "h3 repeat linear-hypergraph compiler",
        "f3_h3_repeat_linear_hypergraph_compiler.py",
        "H3_REPEAT_LINEAR_HYPERGRAPH_COMPILER_PASS",
    ),
    (
        "h3 repeat loose-triangle shadow compiler",
        "f3_h3_repeat_loose_triangle_shadow_compiler.py",
        "H3_REPEAT_LOOSE_TRIANGLE_SHADOW_COMPILER_PASS",
    ),
    (
        "h3 repeat loose reciprocal-closure compiler",
        "f3_h3_repeat_loose_reciprocal_closure_compiler.py",
        "H3_REPEAT_LOOSE_RECIPROCAL_CLOSURE_COMPILER_PASS",
    ),
    (
        "h3 repeat loose pair-membership compiler",
        "f3_h3_repeat_loose_pair_membership_compiler.py",
        "H3_REPEAT_LOOSE_PAIR_MEMBERSHIP_COMPILER_PASS",
    ),
    (
        "h3 repeat loose six-point system",
        "f3_h3_repeat_loose_six_point_system.py",
        "H3_REPEAT_LOOSE_SIX_POINT_SYSTEM_PASS",
    ),
]


def main() -> None:
    notes = "critical/nodes/u1_x4_direct_column_budget/notes"
    print("F3 h=3 repeat-boundary replay")
    for label, script, digest in COMMANDS:
        cmd = [sys.executable, f"{notes}/{script}"]
        result = subprocess.run(
            cmd,
            cwd=ROOT,
            check=False,
            text=True,
            capture_output=True,
        )
        if result.returncode:
            print(result.stdout)
            print(result.stderr, file=sys.stderr)
            raise SystemExit(f"{label} failed with code {result.returncode}")
        if digest not in result.stdout:
            print(result.stdout)
            raise SystemExit(f"{label} missing digest {digest}")
        print(f"{label}: {digest}")
    print("F3_H3_REPEAT_BOUNDARY_REPLAY_PASS")


if __name__ == "__main__":
    main()
