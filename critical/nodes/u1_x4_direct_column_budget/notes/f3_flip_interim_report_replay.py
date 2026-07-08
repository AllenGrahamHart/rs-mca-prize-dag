#!/usr/bin/env python3
"""Replay the lightweight local evidence behind the F3 flip interim report."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]


COMMANDS = [
    (
        "h2 optimized rich-coset constants",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_rich_coset_optimized.py",
        ],
        "H2_RICH_COSET_OPTIMIZED_PASS",
    ),
    (
        "h2 finite-midrange cost table",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_midrange_certificate_costs.py",
        ],
        "H2_MIDRANGE_CERTIFICATE_COSTS_PASS",
    ),
    (
        "h3 hyperbola identity",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_hyperbola_identity.py",
        ],
        "H3_HYPERBOLA_IDENTITY_PASS",
    ),
    (
        "h3 rich-curve denominator compiler",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_denominator_compiler.py",
        ],
        "H3_RICH_CURVE_DENOMINATOR_COMPILER_PASS",
    ),
    (
        "h3 rich-curve degeneracy audit",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_degeneracy_audit.py",
        ],
        "H3_RICH_CURVE_DEGENERACY_AUDIT_PASS",
    ),
    (
        "h3 rich-curve degeneracy filter",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_degeneracy_filter.py",
        ],
        "H3_RICH_CURVE_DEGENERACY_FILTER_PASS",
    ),
    (
        "h3 reduced-condition compiler",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_reduced_condition_compiler.py",
        ],
        "H3_RICH_CURVE_REDUCED_CONDITION_COMPILER_PASS",
    ),
    (
        "h3 rich-curve log-jet reduction",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_logjet_reduction.py",
        ],
        "H3_RICH_CURVE_LOGJET_REDUCTION_PASS",
    ),
    (
        "h3 rich-curve nonvanishing rank audit",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_nv_rank_audit.py",
        ],
        "H3_RICH_CURVE_NV_RANK_AUDIT_PASS",
    ),
    (
        "h3 rich-curve rank sample",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_rank_sample.py",
        ],
        "H3_RICH_CURVE_RANK_SAMPLE_PASS",
    ),
    (
        "h3 rank-form parameter compiler",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rank_parameter_compiler.py",
        ],
        "H3_RANK_PARAMETER_COMPILER_PASS",
    ),
    (
        "h3 bridge-budget compiler",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_bridge_budget_compiler.py",
        ],
        "H3_BRIDGE_BUDGET_COMPILER_PASS",
    ),
    (
        "h3 non-diagonal low-row budget",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_nondiagonal_lowrow_budget.py",
        ],
        "H3_NONDIAGONAL_LOWROW_BUDGET_PASS",
    ),
    (
        "h3 non-diagonal high-row budget",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_nondiagonal_highrow_budget.py",
        ],
        "H3_NONDIAGONAL_HIGHROW_BUDGET_PASS",
    ),
    (
        "h3 private-divisor full-rank refutation",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_private_divisor_full_rank_refutation.py",
        ],
        "H3_PRIVATE_DIVISOR_FULL_RANK_REFUTATION_PASS",
    ),
    (
        "h3 activation-bound compiler",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_bound_compiler.py",
        ],
        "H3_ACTIVATION_BOUND_COMPILER_PASS",
    ),
    (
        "h3 pair-coprimality pilot",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_coprimality_pilot.py",
        ],
        "H3_PAIR_COPRIMALITY_PILOT_PASS",
    ),
    (
        "h3 activation orbit dedup",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_activation_orbit_dedup.py",
        ],
        "H3_ACTIVATION_ORBIT_DEDUP_PASS",
    ),
    (
        "h5 structural reduction",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_structural_reduction.py",
        ],
        "H5_STRUCTURAL_REDUCTION_PASS",
    ),
    (
        "h5 certificate coverage audit",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h5_certificate_coverage_audit.py",
        ],
        "H5_CERTIFICATE_COVERAGE_AUDIT_PASS",
    ),
    (
        "h4/h5 bonus replay",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h4_h5_bonus_replay.py",
        ],
        "H4_H5_BONUS_REDUCTION_PASS",
    ),
    (
        "h6/h8 bonus replay",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h6_h8_bonus_sweep_replay.py",
        ],
        "H6_H8_BONUS_SWEEP_PASS",
    ),
    (
        "h8 residual frontier audit",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_residual_frontier_audit.py",
        ],
        "H8_RESIDUAL_FRONTIER_AUDIT_PASS",
    ),
    (
        "h8 x83 obstruction interface",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_obstruction_interface.py",
        ],
        "H8_N64_X83_INTERFACE_PASS",
    ),
    (
        "h8 x83 one-exchange shell",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_n64_x83_nearlift_shell.py",
        ],
        "H8_N64_X83_NEARLIFT_SHELL_PASS",
    ),
    (
        "h8 support universe compiler",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_support_universe_compiler.py",
        ],
        "H8_SUPPORT_UNIVERSE_COMPILER_PASS",
    ),
    (
        "h8 rotation-orbit compiler",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_rotation_orbit_compiler.py",
        ],
        "H8_ROTATION_ORBIT_COMPILER_PASS",
    ),
    (
        "h8 exponent-unit falsifier",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_exponent_unit_falsifier.py",
        ],
        "H8_EXPONENT_UNIT_FALSIFIER_PASS",
    ),
    (
        "h8 support-certifier reduction",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h8_x83_support_certifier_reduction.py",
        ],
        "H8_X83_SUPPORT_CERTIFIER_REDUCTION_PASS",
    ),
]


def run_command(label: str, cmd: list[str], digest: str) -> None:
    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        raise AssertionError((label, "nonzero exit", proc.returncode))
    if digest not in proc.stdout:
        print(proc.stdout)
        raise AssertionError((label, "missing digest", digest))
    print(f"{label}: {digest}")


def main() -> None:
    for label, cmd, digest in COMMANDS:
        run_command(label, cmd, digest)
    print("F3_FLIP_INTERIM_REPORT_REPLAY_PASS")


if __name__ == "__main__":
    main()
