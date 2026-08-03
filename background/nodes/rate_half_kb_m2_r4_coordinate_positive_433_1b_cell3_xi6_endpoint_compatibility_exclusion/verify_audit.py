#!/usr/bin/env python3
"""Independent source and claim audit for the xi6 endpoint exclusion."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi5_xi6_"
    "endpoint_compatibility_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi5_xi6_"
    "endpoint_compatibility_census_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "xi_index not in (5, 6)",
        "endpoint_record = common_b if xi_index == 5 else c_pair",
        "(endpoint_square+missing_record)**2",
        "endpoint_compatibility_pair_norm",
        "endpoint_compatibility_norm = endpoint_compatibility_pair_norm.norm()",
        "candidate_r_values = set(roots or []) | exceptional_r_values",
        "endpoint_value = b_value if xi_index == 5 else c_value",
        "source_missing*pow(endpoint_value, -1, PRIME)",
        "pow(endpoint_square_value+source_missing, 2, PRIME)",
        "endpoint_square_value*direct_compatibility % PRIME",
        'b_row["status"] = "COMPATIBLE_SOURCE"',
        'b_row["status"] = "COMPATIBILITY_NONZERO"',
        '"case_excluded": not compatible_source_points and not unresolved',
        "for selected_xi in (5, 6)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 8, "eight-row source/xi census")
    xi6 = [row for row in payload["rows"] if row["xi_index"] == 6]
    xi5 = [row for row in payload["rows"] if row["xi_index"] == 5]
    require(len(xi6) == len(xi5) == 4, "four source signs per xi")
    require(all(
        row["status"] == "COMPLETE" and row["tower_norm_used"] and
        row["endpoint_kind"] == "c" and
        row["direct_lift"]["candidate_r_count"] == 8 and
        row["direct_lift"]["source_point_count"] == 8 and
        row["direct_lift"]["compatible_source_point_count"] == 0 and
        row["direct_lift"]["compatible_source_points"] == [] and
        row["direct_lift"]["unresolved_count"] == 0 and
        row["direct_lift"]["case_excluded"]
        for row in xi6
    ), "complete xi6 exclusion census")
    require(all(
        row["endpoint_kind"] == "b" and
        row["direct_lift"]["compatible_source_point_count"] == 6 and
        not row["direct_lift"]["case_excluded"]
        for row in xi5
    ), "xi5 retained frontier")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("15*4*4=240" in statement and
            "not asserted to be target" in statement,
            "scope discipline")
    require("c^2 ((c+m/c)^2-s)" in proof and
            "32 candidate `r`" in proof and "24 points" in proof,
            "identity and finite ledger")
    require("source-only" in audit and "24 compatible `xi=5`" in audit,
            "audit nonclaim")
    require("paid cell-3 ledger is now 1440" in frontier and
            "All 240 cases at `xi=4` remain" in frontier,
            "retained frontier")
    print(
        "audit=ok xi=6 source_rows=4 raw_cases=240 "
        "xi5_compatible_sources=24"
    )


if __name__ == "__main__":
    main()
