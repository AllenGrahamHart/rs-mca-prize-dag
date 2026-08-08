#!/usr/bin/env python3
"""Audit the cell-4 positive-DE pairing-6 claim boundary."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_positive_de_pairing6_"
    "nested_quadratic_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_positive_de_pairing6_"
    "nested_quadratic_result.json"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "p_u = paired_polynomial(PairPolynomial(second_de)",
        "PairPolynomial(de_record), variable_polynomial * sigma_o",
        "matching = ((0, 3), (1, 2), (4, 5))",
        "for xi_index in (0,)",
    ):
        require(snippet in source, f"source construction {snippet}")
    rows = json.loads(RESULT.read_text())["rows"]
    require(len(rows) == 16 and all(
        row["status"] == "COMPLETE" and row["excluded"] and
        not row["witnesses"] and not row["unresolved"] and
        not row["target_boundary_rows"]
        for row in rows
    ), "complete 16-row exclusion")
    require(sum(row["candidate_root_count"] for row in rows) == 160 and
            sum(row["source_point_count"] for row in rows) == 176 and
            sum(row["uv_candidate_count"] for row in rows) == 48,
            "terminal census")
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    require("= 32 raw cases" in statement and
            "16 further cases transport" in proof,
            "raw-case discipline")
    print("audit=ok pairing=6 computed=16 transported=16 boundaries=0")


if __name__ == "__main__":
    main()
