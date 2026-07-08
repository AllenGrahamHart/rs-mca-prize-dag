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
        "h3 reduced-condition compiler",
        [
            sys.executable,
            "critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_rich_curve_reduced_condition_compiler.py",
        ],
        "H3_RICH_CURVE_REDUCED_CONDITION_COMPILER_PASS",
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
