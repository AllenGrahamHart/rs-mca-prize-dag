#!/usr/bin/env python3
"""Independent source and claim audit for the xi5 finite-source exclusion."""

import ast
import collections
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
PRIMARY_SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi5_"
    "finite_source_pairing_solver_modal.py"
)
PRIMARY_RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi5_"
    "finite_source_pairing_solver_census_result.json"
)
AUDIT_SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi5_"
    "finite_source_pairing_audit_modal.py"
)
AUDIT_RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi5_"
    "finite_source_pairing_audit_census_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    primary_source = PRIMARY_SCRIPT.read_text()
    audit_source = AUDIT_SCRIPT.read_text()
    ast.parse(primary_source)
    ast.parse(audit_source)
    for snippet in (
        "q_record = (inverse_f*inverse_f % PRIME)*u_variable*v_variable",
        "equations[left].resultant(",
        'equations[right], "v"',
        "candidates.append((",
        "selected_univariate = univariate(selected, 0)",
        "pow(univariate_variable, PRIME, polynomial)-univariate_variable",
        "specialized = [",
        "common = common.gcd(value)",
        'fiber_row["status"] = "FREE_V"',
        '"source_excluded": not witnesses and not unresolved',
        "for selected_point in range(6)",
    ):
        require(snippet in primary_source, f"primary construction {snippet}")
    for snippet in (
        "q_record = inverse_f*inverse_f % PRIME*u_variable*v_variable",
        'equations[right], "u"',
        "selected_univariate = specialize(selected, 1)",
        "specialize(value, 0, {1: v_value})",
        'fiber["status"] = "FREE_U"',
        '"source_excluded": not solutions and not unresolved',
    ):
        require(snippet in audit_source, f"audit construction {snippet}")

    primary = json.loads(PRIMARY_RESULT.read_text())
    audit = json.loads(AUDIT_RESULT.read_text())
    require(len(primary["rows"]) == len(audit["rows"]) == 24,
            "24 rows in both directions")
    primary_counts = {
        (tuple(row["epsilon"]), row["point_index"]): row["u_root_count"]
        for row in primary["rows"]
    }
    audit_counts = {
        (tuple(row["epsilon"]), row["point_index"]): row["v_root_count"]
        for row in audit["rows"]
    }
    require(primary_counts == audit_counts, "per-source dual root agreement")
    require(
        sum(primary_counts.values()) == 2208 and
        collections.Counter(primary_counts.values()) ==
        collections.Counter({44: 8, 108: 8, 124: 8}),
        "dual root profile",
    )
    require(all(
        row["status"] == "COMPLETE" and row["source_excluded"] and
        row["v_root_count"] == 0 and row["boundary_count"] == 0 and
        row["witness_count"] == 0 and row["unresolved_count"] == 0
        for row in primary["rows"]
    ), "primary empty fibers")
    require(all(
        row["status"] == "COMPLETE" and row["source_excluded"] and
        row["u_root_count"] == 0 and row["solution_count"] == 0 and
        row["unresolved_count"] == 0
        for row in audit["rows"]
    ), "audit empty fibers")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit_md = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("24*15*4=1440" in statement and "4*15*4=240" in statement,
            "subcase/raw scope")
    require("resultants in `v`" in proof and "variables\nreversed" in proof and
            "constant one" in proof,
            "dual elimination proof")
    require("all 4320 primary" in audit_md and
            "eight each of 44, 108, and 124" in audit_md,
            "audit ledger")
    require("paid cell-3 ledger is now 1440" in frontier and
            "Only the 240 cases at `xi=4` remain" in frontier,
            "retained frontier")
    print(
        "audit=ok xi=5 sources=24 subcases=1440 "
        "dual_outer_roots=2208/2208 inner_roots=0"
    )


if __name__ == "__main__":
    main()
