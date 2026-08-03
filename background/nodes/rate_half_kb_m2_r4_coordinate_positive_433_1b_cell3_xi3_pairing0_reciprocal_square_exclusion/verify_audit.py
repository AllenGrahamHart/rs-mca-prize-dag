#!/usr/bin/env python3
"""Independent source and claim audit for xi3/pairing0."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_pairing0_"
    "reciprocal_square_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_pairing0_"
    "reciprocal_square_census_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def lane_rows(lift):
    for r_row in lift["rows"]:
        for t_row in r_row.get("t_rows", []):
            for b_row in t_row.get("b_rows", []):
                for y_row in b_row.get("yd_rows", []):
                    for d_row in y_row.get("d_rows", []):
                        yield from d_row.get("lanes", [])


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "xi_index != 3 or pairing_index != 0",
        "q_record = b_coefficients[branch_index]/a_coefficients[branch_index]",
        "2*missing_record-source_sum_record",
        "missing_record**2",
        "PairPolynomial(-q_record)",
        "sigma_o*q_record*missing_record",
        "(p_b_a*p_c_c-p_b_c*p_c_a)**2",
        "candidate_r_values = set(roots or []) | exceptional_r_values",
        "if a_branch == 0:",
        '"FREE_Q_BRANCH"',
        "q_value = b_branch*pow(a_branch, -1, PRIME) % PRIME",
        "same_pair_cut = paired_value_at(q_value, q_value)",
        "missing_y_field = polynomial_context([",
        "outside_y_field = paired_polynomial_at(",
        "sorted(set(missing_y_roots) & set(outside_y_roots))",
        "x_value = pow(y_value, -1, PRIME)",
        "-x_value % PRIME, 0, 1",
        "e_value = q_value*inverse_d % PRIME",
        "f_value = source_missing*inverse_d % PRIME",
        "for lane_c in (-1, 1):",
        "b_value*f_value % PRIME",
        "lane_c*c_value*f_value % PRIME",
        'raise ValueError("direct lift replay failed")',
        "for selected_branch in (0, 1, 2)",
        "for selected_sigma_o in (-1, 1)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 24, "24-row branch census")
    require(all(
        row["status"] == "COMPLETE" and row["tower_norm_match"] and
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
    require(len(lanes) == 224 and all(
        item["status"] == "THIRD_PAIR_NONZERO" and
        item["final_pair_cut"] != 0
        for item in lanes
    ), "final-pair ledger")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    lineage = (NODE / "lineage.md").read_text()
    require("pay 16 raw target-lane cases, not 48" in statement,
            "raw-case discipline")
    require("4 L_0(q) L_1(q)^2 L_2(q)" in proof and
            "112" in proof and "(y,d)" in proof,
            "factorization and finite ledger")
    require("branches are not counted as separate raw target lanes" in audit,
            "branch multiplicity discipline")
    require("timed out" in lineage and "lowers the source elimination" in lineage,
            "failed-route replacement recorded")
    require("960 raw cases" in frontier and
            "Do not infer complete cell-3" in frontier,
            "retained frontier")
    print(
        "audit=ok xi=3 pairing=0 branch_rows=24 "
        "raw_cases=16 lane_checks=224"
    )


if __name__ == "__main__":
    main()
