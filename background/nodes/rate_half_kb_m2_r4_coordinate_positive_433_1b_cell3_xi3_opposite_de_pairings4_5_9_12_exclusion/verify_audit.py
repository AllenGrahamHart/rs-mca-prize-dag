#!/usr/bin/env python3
"""Independent source and claim audit for xi3 pairings 4, 5, 9, and 12."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_"
    "opposite_de_parity_missing_f_bezout_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_"
    "opposite_de_parity_missing_f_bezout_census_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def direct_rows(lift):
    for r_row in lift["rows"]:
        for t_row in r_row.get("t_rows", []):
            for b_row in t_row.get("b_rows", []):
                for f_row in b_row.get("f_rows", []):
                    for q_row in f_row.get("q_rows", []):
                        yield f_row, q_row


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "pairing_index not in (4, 5)",
        "opposite_q_cut = paired_polynomial(q_variable, -q_variable)",
        "def q_coefficients_for_scaled_f(scale):",
        "parity_x1 = 2*next_q0*next_q2-next_q1**2",
        "parity_missing_f_resultant = (",
        "(opposite_x2*parity_x0-opposite_x0*parity_x2)**2",
        "missing_f_cut = PairPolynomial(",
        "def monic_remainder(value, divisor):",
        "reduced_parity_cut = monic_remainder(",
        "def bezout_resultant(left, right, degree=4):",
        'raise ValueError("Bezout quotient reconstruction failed")',
        "target_free_norm = target_free_pair_determinant.norm()",
        "candidate_r_values = set(roots or []) | exceptional_r_values",
        "f_roots = field_roots(missing_f_field)",
        "first_q_cut = opposite_q_polynomial_at()",
        "common_q_cut = first_q_cut.gcd(second_q_cut)",
        'f_row["status"] = "FREE_Q"',
        "source_missing*pow(f_value, -1, PRIME)",
        "q_value*f_value*pow(source_missing, -1, PRIME)",
        "tuple(itertools.product((-1, 1), repeat=2))",
        "for selected_sigma_c, selected_sigma_o in lane_signs:",
        "selected_sigma_o*e_value*f_value % PRIME",
        'raise ValueError("direct lift replay failed")',
        "(*epsilon, 0, 0, 3, 4) for epsilon in sign_pairs",
        "(*epsilon, selected_sigma_c, 0, 3, 5)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 12, "12-row source/matching census")
    require(all(
        row["status"] == "COMPLETE" and row["tower_norm_used"] and
        (row["opposite_q_cut_degree"],
         row["parity_missing_f_resultant_degree"],
         row["missing_f_cut_degree"],
         row["reduced_parity_cut_degree"],
         row["bezout_matrix_size"]) == (4, 8, 4, 3, 4) and
        row["direct_lift"]["case_excluded"] and
        row["direct_lift"]["witness_count"] == 0 and
        row["direct_lift"]["boundary_solution_count"] == 0 and
        row["direct_lift"]["unresolved_count"] == 0 and
        row["direct_lift"]["final_pair_solution_count"] == 0
        for row in payload["rows"]
    ), "complete exclusion census")
    pairs = [item for row in payload["rows"]
             for item in direct_rows(row["direct_lift"])]
    lanes = [lane for _, q_row in pairs for lane in q_row["lane_rows"]]
    require(len(pairs) == 184 and all(
        q_row["status"] == "CHECKED" and
        q_row["first_pair_cut"] == 0 and
        q_row["second_pair_cut"] == 0
        for _, q_row in pairs
    ), "defining-pair ledger")
    require(len(lanes) == 480 and all(
        lane["status"] == "THIRD_PAIR_NONZERO" and
        lane["final_pair_cut"] != 0 for lane in lanes
    ), "final-pair ledger")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    lineage = (NODE / "lineage.md").read_text()
    require("all 64 raw" in statement and "matching 4 to 9" in statement and
            "matching 5 to 12" in statement,
            "computed and transported scope")
    require("J(f)" in proof and "M(f)" in proof and "exact gcd" in proof and
            "928" in proof and "480" in proof,
            "elimination and finite ledger")
    require("maps 4 to 9 and 5 to 12" in audit, "transport discipline")
    require("cached-product" in lineage and
            "closes the last two" in lineage,
            "route-selection discipline")
    require("960 raw cases" in frontier and "No `xi=3` pairing remains" in frontier and
            "Do not infer complete cell-3" in frontier,
            "retained frontier")
    print(
        "audit=ok xi=3 pairings=4,5,9,12 computed_rows=12 "
        "raw_cases=64 final_checks=480"
    )


if __name__ == "__main__":
    main()
