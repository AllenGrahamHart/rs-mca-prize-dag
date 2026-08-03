#!/usr/bin/env python3
"""Independent source and claim audit for xi3/pairings1-2."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_pairings1_2_"
    "reciprocal_linear_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_pairings1_2_"
    "reciprocal_linear_census_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def lane_rows(lift):
    for r_row in lift["rows"]:
        for t_row in r_row.get("t_rows", []):
            for b_row in t_row.get("b_rows", []):
                for z_row in b_row.get("z_rows", []):
                    yield from z_row.get("lanes", [])


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "pairing_index not in (1, 2)",
        "q_record = b_coefficients[branch_index]/a_coefficients[branch_index]",
        "2*missing_record-source_sum_record",
        "missing_record**2",
        "common_b*missing_record if pairing_index == 1 else",
        "sigma_c*c_pair*missing_record",
        "p_next = paired_polynomial(",
        "remainder = polynomial_remainder(p_missing, p_next)",
        "remainder_linear**2*p_next_c",
        "- remainder_linear*remainder_constant*p_next_b",
        "+ p_next_a*remainder_constant**2",
        "candidate_r_values = set(roots or []) | exceptional_r_values",
        '"FREE_Q_BRANCH"',
        "q_value = b_branch*pow(a_branch, -1, PRIME) % PRIME",
        "same_pair_cut = paired_value_at(q_value, q_value)",
        "missing_z_field = polynomial_context([",
        "next_z_field = paired_polynomial_at(",
        "sorted(set(missing_z_roots) & set(next_z_roots))",
        "d_value = pow(z_value, -1, PRIME)",
        "e_value = q_value*z_value % PRIME",
        "f_value = source_missing*z_value % PRIME",
        "itertools.product((-1, 1), (-1, 1))",
        "((sigma_c, lane_o) for lane_o in (-1, 1))",
        'raise ValueError("direct lift replay failed")',
        "for selected_branch in (0, 1, 2)",
        "for selected_sigma_c in (-1, 1)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 36, "36-row branch census")
    require(all(
        row["status"] == "COMPLETE" and row["tower_norm_match"] and
        (row["p_missing_degree"], row["p_next_degree"],
         row["remainder_degree"]) == (4, 2, 1) and
        row["direct_lift"]["case_excluded"] and
        row["direct_lift"]["witness_count"] == 0 and
        row["direct_lift"]["boundary_solution_count"] == 0 and
        row["direct_lift"]["unresolved_count"] == 0 and
        row["direct_lift"]["final_pair_solution_count"] == 0
        for row in payload["rows"]
    ), "complete exclusion census")
    lanes = [
        item for row in payload["rows"]
        for item in lane_rows(row["direct_lift"])
    ]
    require(len(lanes) == 128 and all(
        item["status"] == "THIRD_PAIR_NONZERO" and
        item["final_pair_cut"] != 0
        for item in lanes
    ), "final-pair ledger")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    lineage = (NODE / "lineage.md").read_text()
    require("pay 32 raw target-lane cases, not 96" in statement,
            "raw-case discipline")
    require("r_1^2 p_0 - r_1 r_0 p_1 + p_2 r_0^2" in proof and
            "56 `z` candidates" in proof and "128" in proof,
            "remainder cut and finite ledger")
    require("branches are not counted as separate raw target lanes" in audit,
            "branch multiplicity discipline")
    require("reducing the quartic" in lineage.lower() and
            "exceptional strata" in lineage,
            "route lineage")
    require("800 raw cases" in frontier and
            "Do not infer complete cell-3" in frontier,
            "retained frontier")
    print(
        "audit=ok xi=3 pairings=1,2 branch_rows=36 "
        "raw_cases=32 lane_checks=128"
    )


if __name__ == "__main__":
    main()
