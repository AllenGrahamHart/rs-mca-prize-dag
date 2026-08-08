#!/usr/bin/env python3
"""Independent source and claim audit for the cell-4 pairing-3 exclusion."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_de_pairing3_"
    "nested_quadratic_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_de_pairing3_"
    "nested_quadratic_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "class RationalFunction:",
        "def polynomial_pseudo_remainder(",
        "target_free = p_v_a * (",
        "target_norm = target_free.norm()",
        "candidate_roots.update(roots)",
        "for xi_index in (0, 2)",
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 32 and all(
        row["status"] == "COMPLETE" and row["excluded"] and
        not row["witnesses"] and not row["unresolved"] and
        row["colored_solution_count"] == 0
        for row in payload["rows"]
    ), "complete exclusion census")
    require(sum(row["candidate_root_count"] for row in payload["rows"]) == 312 and
            sum(row["source_point_count"] for row in payload["rows"]) == 272 and
            sum(row["uv_candidate_count"] for row in payload["rows"]) == 64 and
            sum(len(row["target_boundary_rows"]) for row in payload["rows"]) == 16,
            "printed terminal census")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("= 48 raw cases" in statement and
            "32 computed and 16" in proof, "raw-case discipline")
    require("division-free" in proof and "directly lifted" in audit,
            "exceptional-stratum discipline")
    require("12 of 105" in frontier and
            "No other live matching orbit" in frontier,
            "retained frontier")
    print("audit=ok cell=4 pairing=3 exceptional_roots=lifted")


if __name__ == "__main__":
    main()
