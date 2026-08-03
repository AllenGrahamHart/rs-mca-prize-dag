#!/usr/bin/env python3
"""Independent source and claim audit for the pairing-6 exclusion."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_de_pairing6_"
    "nested_quadratic_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_de_pairing6_"
    "nested_quadratic_census_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "p_u = paired_polynomial(",
        "PairPolynomial(de_record), variable_polynomial*sigma_o",
        "PairPolynomial(second_de), variable_polynomial",
        "nested_quartic = (",
        "remainder = polynomial_remainder(nested_quartic, p_v)",
        "candidate_r_values = set(roots or []) | exceptional_r_values",
        "p_u_field = paired_polynomial_at(de_value, sigma_o)",
        "p_v_field = paired_polynomial_at(second_de_value)",
        "d_value = v_value*pow(f_value, -1, PRIME)",
        "e_value = u_value*pow(f_value, -1, PRIME)",
        "de_value, sigma_o*u_value % PRIME",
        'raise ValueError("direct lift replay failed")',
        "for selected_xi in (0, 2)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 32, "32-row census")
    require(all(
        row["status"] == "COMPLETE" and row["tower_norm_match"] and
        row["direct_lift"]["case_excluded"] and
        row["direct_lift"]["colored_solution_count"] == 0 and
        row["direct_lift"]["witness_count"] == 0 and
        row["direct_lift"]["unresolved_count"] == 0
        for row in payload["rows"]
    ), "complete exclusion census")
    boundaries = [
        item for row in payload["rows"]
        for item in row["direct_lift"]["boundary_solutions"]
    ]
    require(len(boundaries) == 32 and all(
        item["f"] == 0 and item["failed_guards"] == ["nonzero_5"]
        for item in boundaries
    ), "f=0 boundary ledger")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("= 48 raw cases" in statement and
            "32 computed and 16 transported" in audit,
            "raw-case discipline")
    require("No vanishing elimination coefficient" in proof and
            "32 aggregate colored-pair evaluations are nonzero" in proof and
            "zero witnesses or" in proof,
            "exceptional and terminal discipline")
    require("`u=ef`, `v=df`" in audit and
            "`d=v/f`," in audit and "`e=u/f`" in audit,
            "variable-role discipline")
    require("`0,1,2,3,4,5,6,7,8,9,10,11,12,13`" in frontier and
            "complete cell-3 closure" in frontier,
            "retained frontier")
    print("audit=ok pairing=6 rows=32 uv_candidates=48 boundary_f_zero=32")


if __name__ == "__main__":
    main()
