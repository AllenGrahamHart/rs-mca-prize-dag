#!/usr/bin/env python3
"""Audit cell-4 xi3 pairing-3 reciprocal-square exclusion."""

import ast
import collections
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing3_"
    "reciprocal_square_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing3_"
    "reciprocal_square_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def lane_rows(row):
    for finite in row["finite_rows"]:
        for z_row in finite.get("z_rows", []):
            for d_row in z_row.get("d_rows", []):
                yield from d_row.get("lanes", [])


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "epsilon_1, epsilon_2, sigma_c = case",
        "def polynomial_remainder(dividend, divisor):",
        "variable_polynomial * (common_b*missing_record)",
        "variable_polynomial * (sigma_c*c_pair*missing_record)",
        "p_colored_even**2",
        "variable_polynomial*p_colored_odd**2",
        "remainder_linear**2*p_m_0",
        "target_norm = target_free.norm()",
        "missing_z_roots = univariate_roots([",
        "sorted(set(missing_z_roots) & set(colored_z_roots))",
        "antipodal_q_roots = univariate_roots",
        "set(antipodal_q_roots)",
        "d_value = pow(z_value, -1, PRIME)",
        "e_value = q_value*inverse_d % PRIME",
        "f_value = missing*inverse_d % PRIME",
        'raise ValueError("direct target replay failed")',
        "for sigma_c in (-1, 1)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 8, "8-row sign census")
    require(all(
        row["status"] == "COMPLETE"
        and row["target_excluded"]
        and row["remainder_degree"] == 1
        and row["witness_count"] == 0
        and row["target_boundary_rows"] == []
        and row["unresolved"] == []
        and row["final_pair_solution_count"] == 0
        and row["q_candidate_count"] == 0
        for row in payload["rows"]
    ), "complete exclusion census")
    lanes = [item for row in payload["rows"] for item in lane_rows(row)]
    require(len(lanes) == 16 and all(
        item["common_q_roots"] == [] for item in lanes
    ), "q-intersection ledger")
    statuses = collections.Counter(
        item["status"]
        for row in payload["rows"]
        for item in row["finite_rows"]
    )
    require(statuses == {"CHECKED": 16},
            "source terminal partition")
    require(
        sum(row["candidate_root_count"] for row in payload["rows"]) == 60
        and sum(row["source_point_count"] for row in payload["rows"]) == 16
        and sum(row["z_candidate_count"] for row in payload["rows"]) == 8,
        "aggregate root census",
    )

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("pays 16 raw atlas cases" in " ".join(statement.split()),
            "raw-case discipline")
    require("linear remainder" in proof
            and "zero common q roots" in " ".join(proof.split()),
            "remainder and finite ledger")
    require("does not trust stored terminal statuses" in audit,
            "independent replay contract")
    require("five matching-exchange pairs" in frontier, "retained frontier")
    print(
        "audit=ok cell=4 xi=3 pairing=3 sign_rows=8 "
        "raw_cases=16 z=8 q=0"
    )


if __name__ == "__main__":
    main()
