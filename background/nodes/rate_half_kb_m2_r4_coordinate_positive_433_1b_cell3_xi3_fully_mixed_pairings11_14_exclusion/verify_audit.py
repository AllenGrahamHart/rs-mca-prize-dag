#!/usr/bin/env python3
"""Independent source and claim audit for xi3 pairings 11 and 14."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_"
    "fully_mixed_pairing11_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_"
    "fully_mixed_pairing11_census_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def root_rows(lift):
    for r_row in lift["rows"]:
        for t_row in r_row.get("t_rows", []):
            for b_row in t_row.get("b_rows", []):
                for q_row in b_row.get("q_rows", []):
                    yield from q_row.get("root_rows", [])


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "pairing_index != 11 or xi_index != 3",
        "paired_plus+paired_minus-2*paired_zero",
        "source_u = common_b*missing_record",
        "source_v = sigma_c*c_pair*missing_record",
        "paired_constant*paired_quadratic*(source_uv_sum**2)",
        "paired_linear**2*source_uv_product",
        "denominator_fourth = compatibility_multiply(",
        "compatibility_multiply(linear_square, denominator_square)",
        "reduced_missing_cut = cached_remainder(",
        "def bezout_resultant(left, right, degree=4):",
        'raise ValueError("Bezout quotient reconstruction failed")',
        "bottom_minors[left_column, right_column]",
        "target_free_pair_determinant = (",
        "target_free_norm = target_free_pair_determinant.norm()",
        "candidate_r_values = set(roots or []) | exceptional_r_values",
        '"DEGENERATE_A_B"',
        "possible_z = missing_roots",
        "first_pair_cut = paired_value_at(",
        "second_pair_cut = paired_value_at(",
        "-q_value % PRIME",
        "sigma_o*e_value*f_value % PRIME",
        'raise ValueError("direct lift replay failed")',
        "for selected_sigma_c in (-1, 1)",
        "for selected_sigma_o in (-1, 1)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 16, "16-row source/target census")
    require(all(
        row["status"] == "COMPLETE" and row["tower_norm_used"] and
        (row["compatibility_cut_degree"],
         row["missing_substitution_cut_degree_bound"],
         row["reduced_missing_cut_degree"],
         row["bezout_matrix_size"]) == (4, 8, 3, 4) and
        row["direct_lift"]["case_excluded"] and
        row["direct_lift"]["witness_count"] == 0 and
        row["direct_lift"]["boundary_solution_count"] == 0 and
        row["direct_lift"]["unresolved_count"] == 0 and
        row["direct_lift"]["final_pair_solution_count"] == 0
        for row in payload["rows"]
    ), "complete exclusion census")
    roots = [item for row in payload["rows"]
             for item in root_rows(row["direct_lift"])]
    require(len(roots) == 64 and all(
        item["status"] == "THIRD_PAIR_NONZERO" and
        item["first_pair_cut"] == 0 and
        item["second_pair_cut"] == 0 and
        item["final_pair_cut"] != 0 for item in roots
    ), "final-pair ledger")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    lineage = (NODE / "lineage.md").read_text()
    require("all 32 raw" in statement and "matching 14" in statement,
            "computed and transported scope")
    require("G(q)" in proof and "K(q)" in proof and "D(q)=B(q)=0" in proof and
            "240" in proof and "64" in proof,
            "elimination and finite ledger")
    require("maps pairing 11 to pairing 14" in audit,
            "transport discipline")
    require("timed out at 300 seconds" in lineage and
            "later monic missing-`f` theorem" in lineage,
            "failed-route discipline")
    require("960 raw cases" in frontier and
            "Do not infer complete cell-3" in frontier,
            "retained frontier")
    print(
        "audit=ok xi=3 pairings=11,14 computed_rows=16 "
        "raw_cases=32 final_checks=64"
    )


if __name__ == "__main__":
    main()
