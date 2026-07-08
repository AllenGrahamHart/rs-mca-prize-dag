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
