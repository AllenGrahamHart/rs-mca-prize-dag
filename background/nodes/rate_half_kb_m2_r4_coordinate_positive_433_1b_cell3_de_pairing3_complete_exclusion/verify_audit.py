#!/usr/bin/env python3
"""Independent source and claim audit for the pairing-3 exclusion."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_de_pairing3_"
    "nested_quadratic_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_de_pairing3_"
    "nested_quadratic_census_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "class RationalFunction:",
        "common = numer.gcd(denom)",
        "return Cubic(*solve(",
        "p_u = paired_polynomial(",
        "p_v = paired_polynomial(",
        "nested_quartic = (",
        "remainder_linear**2*p_v_c",
        "guard_values.append((\"base_cubic_leading\", base_leading))",
        "candidate_r_values = set(roots or []) | exceptional_r_values",
        "de_value*pow(u_value+eta*v_value, 2, PRIME)",
        "u_value*v_value*pow(de_value, -1, PRIME)",
        "colored_cut = paired_value_at(",
        'raise ValueError("direct lift replay failed")',
        "for selected_xi in (0, 2)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 32, "32-row census")
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
    require(len(boundaries) == 32 and all(
        item["f"] == 0 and item["failed_guards"] == ["nonzero_5"]
        for item in boundaries
    ), "f=0 boundary ledger")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("= 48 raw cases" in statement and
            "32 computed and 16 transported" in proof,
            "raw-case discipline")
    require("does not treat vanishing elimination coefficients" in proof and
            "directly solved" in audit,
            "exceptional-stratum discipline")
    require("matching index `14`" in frontier and
            "do not infer complete cell-3" in frontier and
            "from the fourteen paid" in frontier,
            "retained frontier")
    print("audit=ok pairing=3 exceptional_roots=lifted boundary_f_zero=32")


if __name__ == "__main__":
    main()
