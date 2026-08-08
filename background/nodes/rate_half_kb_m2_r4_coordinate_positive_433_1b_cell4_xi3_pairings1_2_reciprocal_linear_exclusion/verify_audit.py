#!/usr/bin/env python3
"""Audit cell-4 xi3 pairings 1-2 reciprocal-linear exclusion."""

import ast
import collections
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairings1_2_"
    "reciprocal_linear_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairings1_2_"
    "reciprocal_linear_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def lane_rows(row):
    for finite in row["finite_rows"]:
        for z_row in finite.get("z_rows", []):
            yield from z_row.get("lanes", [])


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "epsilon_1, epsilon_2, branch_index, sigma_c_anchor, pairing_index = case",
        "q_record = b_coefficients[branch_index] / a_coefficients[branch_index]",
        "1, 0,",
        "2*missing_record - source_sum_record, 0,",
        "missing_record**2",
        "def polynomial_remainder(dividend, divisor):",
        "common_b*missing_record if pairing_index == 1",
        "sigma_c_anchor*c_pair*missing_record",
        "remainder_linear**2*p_next_0",
        "target_norm = target_free.norm()",
        '"FREE_Q_BRANCH"',
        "missing_z_roots = univariate_roots([",
        "sorted(set(missing_z_roots) & set(next_z_roots))",
        "d_value = pow(z_value, -1, PRIME)",
        "e_value = q_value*z_value % PRIME",
        "f_value = missing*z_value % PRIME",
        "if pairing_index == 1 else",
        'raise ValueError("direct target replay failed")',
        "pairing_one = tuple(",
        "pairing_two = tuple(",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 36, "36-row branch census")
    require(all(
        row["status"] == "COMPLETE"
        and row["target_excluded"]
        and row["remainder_degree"] == 1
        and row["witness_count"] == 0
        and row["target_boundary_rows"] == []
        and row["unresolved"] == []
        and row["final_pair_solution_count"] == 0
        for row in payload["rows"]
    ), "complete exclusion census")
    lanes = [item for row in payload["rows"] for item in lane_rows(row)]
    require(len(lanes) == 64 and all(
        item["status"] == "THIRD_PAIR_NONZERO"
        and item["final_pair_cut"] != 0
        for item in lanes
    ), "final-pair ledger")
    statuses = collections.Counter(
        item["status"]
        for row in payload["rows"]
        for item in row["finite_rows"]
    )
    require(statuses == {"CHECKED": 180, "EMPTY_Q_BRANCH": 36},
            "source terminal partition")
    pairing_rows = collections.Counter(
        row["pairing_index"] for row in payload["rows"]
    )
    require(pairing_rows == {1: 12, 2: 24}, "matching row partition")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("pay 32 raw atlas cases, not 96" in " ".join(statement.split()),
            "raw-case discipline")
    require("linear remainder" in proof
            and "64 final-lane evaluations" in " ".join(proof.split()),
            "remainder and finite ledger")
    require("does not trust stored terminal statuses" in audit,
            "independent replay contract")
    require("six matching-exchange pairs" in frontier, "retained frontier")
    print(
        "audit=ok cell=4 xi=3 pairings=1,2 branch_rows=36 "
        "raw_cases=32 lane_checks=64"
    )


if __name__ == "__main__":
    main()
