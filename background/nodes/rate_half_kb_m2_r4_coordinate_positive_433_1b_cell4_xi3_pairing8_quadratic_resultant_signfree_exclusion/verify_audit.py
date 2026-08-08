#!/usr/bin/env python3
"""Audit cell-4 xi3 pairing-8 quadratic-resultant sign-free exclusion."""

import ast
import collections
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing8_"
    "quadratic_resultant_signfree_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi3_pairing8_"
    "quadratic_resultant_signfree_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def lane_rows(row):
    for finite in row["finite_rows"]:
        for z_row in finite.get("z_rows", []):
            for q_row in z_row.get("q_rows", []):
                yield from q_row.get("lanes", [])


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "epsilon_1, epsilon_2, sigma_c = case",
        "def polynomial_remainder(dividend, divisor):",
        "class PairBivariate:",
        "def q_coefficients(polynomial):",
        "p_bf_qz = paired_bivariate(",
        "p_cf_qz = paired_bivariate(",
        "(bf_a*cf_c-bf_c*cf_a)**2",
        "z_bivariate*(sigma_c*c_pair*missing_record)",
        "p_z_even**2-variable_polynomial*p_z_odd**2",
        "remainder_linear**2*p_m_0",
        "target_norm = target_free.norm()",
        "missing_z_roots = univariate_roots([",
        "bf_q_roots = univariate_roots",
        "cf_q_roots = univariate_roots",
        "set(bf_q_roots) & set(cf_q_roots)",
        "d_value = pow(z_value, -1, PRIME)",
        "e_value = q_value*z_value % PRIME",
        "f_value = missing*z_value % PRIME",
        'raise ValueError("direct target replay failed")',
        "for sigma_c in (-1, 1)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 8, "8-row sign/lane census")
    require(all(
        row["status"] == "COMPLETE"
        and row["target_excluded"]
        and row["remainder_degree"] == 1
        and row["witness_count"] == 0
        and row["target_boundary_rows"] == []
        and row["unresolved"] == []
        and row["final_pair_solution_count"] == 0
        and row["q_candidate_count"] in (0, 4)
        for row in payload["rows"]
    ), "complete exclusion census")
    lanes = [item for row in payload["rows"] for item in lane_rows(row)]
    require(len(lanes) == 32 and all(
        item["status"] == "THIRD_PAIR_NONZERO"
        and item["final_pair_cut"] != 0 for item in lanes
    ), "final-pair ledger")
    statuses = collections.Counter(
        item["status"]
        for row in payload["rows"]
        for item in row["finite_rows"]
    )
    require(statuses == {"CHECKED": 32},
            "source terminal partition")
    require(
        sum(row["candidate_root_count"] for row in payload["rows"]) == 64
        and sum(row["source_point_count"] for row in payload["rows"]) == 32
        and sum(row["z_candidate_count"] for row in payload["rows"]) == 16
        and sum(row["q_candidate_count"] for row in payload["rows"]) == 16,
        "aggregate root census",
    )

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("pays 16 raw atlas cases" in " ".join(statement.split()),
            "raw-case discipline")
    require("linear remainder" in proof
            and "All 32 evaluations are nonzero" in " ".join(proof.split()),
            "remainder and finite ledger")
    require("does not trust stored terminal statuses" in audit,
            "independent replay contract")
    require("one matching-exchange pair" in frontier, "retained frontier")
    print(
        "audit=ok cell=4 xi=3 pairing=8 sign_lane_rows=8 "
        "raw_cases=16 z=16 q=16 lane_checks=32"
    )


if __name__ == "__main__":
    main()
