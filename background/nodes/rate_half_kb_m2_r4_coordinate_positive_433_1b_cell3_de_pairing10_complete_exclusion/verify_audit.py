#!/usr/bin/env python3
"""Independent source and claim audit for the pairing-10 exclusion."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_de_pairing10_"
    "nested_quadratic_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_de_pairing10_"
    "nested_quadratic_census_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "pairing_index != 10",
        "PairPolynomial(second_de), variable_polynomial*sigma_o",
        "PairPolynomial(de_record),",
        "variable_polynomial*common_b",
        "u_linear = -p_u_b/p_u_a",
        "u_constant = -p_u_c/p_u_a",
        "uf_eliminant = (",
        "PairPolynomial(p_u_a)*relation_constant**2",
        "remainder = polynomial_remainder(uf_eliminant, p_f)",
        "candidate_r_values = set(roots or []) | exceptional_r_values",
        "+ eta*de_value*f_value*f_value,",
        "p_u_field = paired_polynomial_at(second_de_value, sigma_o)",
        "p_f_field = paired_polynomial_at(",
        "de_value, b_value",
        "e_value = u_value*pow(f_value, -1, PRIME) % PRIME",
        "d_value = de_value*pow(e_value, -1, PRIME) % PRIME",
        "for lane_c in (-1, 1):",
        "for lane_o in (sigma_o,):",
        "lane_c*c_value*f_value % PRIME",
        'raise ValueError("direct lift replay failed")',
        "for sigma_o in (-1, 1)",
        "for selected_xi in (0, 2)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 16, "sixteen-row source census")
    require(all(
        row["status"] == "COMPLETE" and row["tower_norm_match"] and
        row["direct_lift"]["case_excluded"] and
        row["direct_lift"]["witness_count"] == 0 and
        row["direct_lift"]["unresolved_count"] == 0
        for row in payload["rows"]
    ), "complete exclusion census")
    boundaries = [
        item for row in payload["rows"]
        for item in row["direct_lift"]["boundary_solutions"]
    ]
    require(len(boundaries) == 16 and all(
        item["f"] == 0 and item["failed_guards"] == ["nonzero_5"] and
        len(item["target_lanes_covered"]) == 2
        for item in boundaries
    ), "f=0 boundary ledger")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    lineage = (NODE / "lineage.md").read_text()
    require("= 48 raw cases" in statement and
            "32 computed and 16 transported" in audit,
            "raw-case discipline")
    require("No vanishing elimination coefficient" in proof and
            "128 nonboundary final-pair evaluations" in audit,
            "exceptional and lane discipline")
    require("sends source role cell 3 to" in lineage and
            "duplicate cell 6" in lineage,
            "failed symmetry shortcut recorded")
    require("`0,1,2,3,4,5,6,7,8,9,10,11,12,13,14`" in frontier and
            "Complete cell-3 exclusion remains open" in frontier,
            "retained frontier")
    print(
        "audit=ok pairing=10 source_rows=16 "
        "lanes_per_row=2 boundary_f_zero=16"
    )


if __name__ == "__main__":
    main()
