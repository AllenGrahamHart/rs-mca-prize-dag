#!/usr/bin/env python3
"""Independent source and claim audit for cell-4 xi3/pairing0."""

import ast
import collections
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing0_"
    "reciprocal_square_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing0_"
    "reciprocal_square_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def lane_rows(row):
    for finite in row["finite_rows"]:
        for y_row in finite.get("yd_rows", []):
            for d_row in y_row.get("d_rows", []):
                yield from d_row.get("lanes", [])


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "epsilon_1, epsilon_2, branch_index, sigma_o = case",
        "q_record = b_coefficients[branch_index] / a_coefficients[branch_index]",
        "2*missing_record - source_sum_record",
        "missing_record**2",
        "PairPolynomial(-q_record)",
        "sigma_o*q_record*missing_record",
        "target_free = (",
        "target_norm = target_free.norm()",
        "if a_branch == 0:",
        '"FREE_Q_BRANCH"',
        "q_value = b_branch*pow(a_branch, -1, PRIME) % PRIME",
        "same_pair_cut = paired_scalar(",
        "sorted(set(missing_y_roots) & set(outside_y_roots))",
        "d_squared = pow(y_value, -1, PRIME)",
        "e_value = q_value*inverse_d % PRIME",
        "f_value = missing*inverse_d % PRIME",
        "for sigma_c in (-1, 1):",
        "b_value*f_value % PRIME",
        "sigma_c*c_value*f_value % PRIME",
        'raise ValueError("direct target replay failed")',
        "for branch_index in (0, 1, 2)",
        "for sigma_o in (-1, 1)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 24, "24-row branch census")
    require(all(
        row["status"] == "COMPLETE"
        and row["target_excluded"]
        and row["witness_count"] == 0
        and row["target_boundary_rows"] == []
        and row["unresolved"] == []
        and row["final_pair_solution_count"] == 0
        for row in payload["rows"]
    ), "complete exclusion census")
    lanes = [item for row in payload["rows"] for item in lane_rows(row)]
    require(len(lanes) == 128 and all(
        item["status"] == "THIRD_PAIR_NONZERO"
        and item["final_pair_cut"] != 0
        for item in lanes
    ), "final-pair ledger")
    statuses = collections.Counter(
        item["status"]
        for row in payload["rows"]
        for item in row["finite_rows"]
    )
    require(statuses == {"CHECKED": 48, "EMPTY_Q_BRANCH": 24},
            "source terminal partition")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    lineage = (NODE / "lineage.md").read_text()
    require("pay 16 raw target-lane cases, not 48" in statement,
            "raw-case discipline")
    require("4 L_0(q) L_1(q)^2 L_2(q)" in proof
            and "128 final-pair evaluations" in proof,
            "factorization and finite ledger")
    require("does not trust the stored terminal labels" in audit,
            "independent replay contract")
    require("28 live labels" in frontier, "retained frontier")
    require("separate nodes" in lineage, "transport separation")
    print(
        "audit=ok cell=4 xi=3 pairing=0 branch_rows=24 "
        "raw_cases=16 lane_checks=128"
    )


if __name__ == "__main__":
    main()
