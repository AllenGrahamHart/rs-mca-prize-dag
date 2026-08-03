#!/usr/bin/env python3
"""Independent source and claim audit for xi3 pairings 3 and 6."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_opposite_de_orbit_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_opposite_de_"
    "pairing3_census_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def lane_rows(lift):
    for r_row in lift["rows"]:
        for t_row in r_row.get("t_rows", []):
            for b_row in t_row.get("b_rows", []):
                for q_row in b_row.get("q_rows", []):
                    for root_row in q_row.get("root_rows", []):
                        yield from root_row.get("lanes", [])


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "pairing_index not in (3, 4, 5)",
        "q_cut = paired_polynomial(q_variable, -q_variable)",
        'raise ValueError("opposite-DE cut is not even")',
        "q_leading_inverse = Pair(1)/q_cut.coefficients[4]",
        "factor = work[degree]*q_leading_inverse",
        "paired_plus+paired_minus-2*paired_zero",
        "next_scale = q_variable*(sigma_o*missing_record)",
        "q_multiply(a_left, c_right)-q_multiply(c_left, a_right)",
        "even_part**2-x_variable*odd_part**2",
        "x_remainder = cached_remainder(parity_condition, x_cut)",
        "candidate_r_values = set(roots or []) | exceptional_r_values",
        '"FREE_OPPOSITE_Q"',
        "opposite_q_field = opposite_q_polynomial_at()",
        "q_roots = field_roots(opposite_q_field)",
        "sigma_o*q_value*source_missing % PRIME",
        "sorted(set(missing_roots) & set(next_roots))",
        "d_roots = field_roots(polynomial_context([",
        "e_value = q_value*z_value % PRIME",
        "f_value = source_missing*z_value % PRIME",
        "((lane_c, sigma_o) for lane_c in (-1, 1))",
        "b_value*f_value % PRIME",
        "lane_c*c_value*f_value % PRIME",
        'raise ValueError("direct lift replay failed")',
        "for selected_sigma_o in (-1, 1)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 8, "8-row source census")
    require(all(
        row["status"] == "COMPLETE" and row["tower_norm_match"] and
        (row["q_cut_degree"], row["p_missing_degree"],
         row["p_next_degree"], row["q_remainder_degree"],
         row["x_remainder_degree"]) == (4, 2, 2, 3, 1) and
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
    require(len(lanes) == 384 and all(
        item["status"] == "THIRD_PAIR_NONZERO" and
        item["final_pair_cut"] != 0 for item in lanes
    ), "final-pair ledger")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    lineage = (NODE / "lineage.md").read_text()
    require("all 32 raw" in statement and "matching 6" in statement,
            "computed and transported scope")
    require("E(x)^2 - x O(x)^2" in proof and "480" in proof and
            "384" in proof, "parity cut and finite ledger")
    require("maps pairing 3 to pairing 6" in audit,
            "transport discipline")
    require("timed out" in lineage and "300 seconds" in lineage and
            "pairings 4 and 5 are not claimed" in lineage,
            "failed-route discipline")
    require("896 raw cases" in frontier and
            "Do not infer complete cell-3" in frontier,
            "retained frontier")
    print(
        "audit=ok xi=3 pairings=3,6 computed_rows=8 "
        "raw_cases=32 lane_checks=384"
    )


if __name__ == "__main__":
    main()
