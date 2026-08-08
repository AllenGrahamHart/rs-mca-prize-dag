#!/usr/bin/env python3
"""Verify the complete source-line literal-assignment aggregate."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
CONSUMER = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_complete_exclusion"
REQUIREMENTS = {
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_36_cell_coverage",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_literal_inversion_transport",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_direct_residual_registry",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_f02_square_orbit_exclusions",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_f02_mixed_collision_exclusions",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_f04_complete_chart_classification",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_f06_complete_chart_classification",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_m01_complete_chart_classification",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_m03_complete_chart_classification",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_positive_projective_boundary_literal_coverage",
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_negative_literal_assignment_coverage",
    "rate_half_kb_m2_r4_diagonal_c2_112_near_negative_literal_assignment_coverage",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


statement = (NODE / "statement.md").read_text(encoding="utf-8")
result = (NODE / "result.md").read_text(encoding="utf-8")
require("**status:** PROVED" in statement, "statement status")
require("aligned-positive residual = empty" in statement, "aligned positive")
require("affine near-positive direct residual = empty" in statement, "affine near positive")
require("positive projective-boundary literal residual = empty" in statement, "boundary")
require("aligned-negative literal residual = empty" in statement, "aligned negative")
require("near-negative literal residual = empty" in statement, "near negative")
require("**PROVED.**" in result and "No literal residual remains" in result, "result")

dag = json.loads((ROOT / "dag.json").read_text())
nodes = {item["id"]: item for item in dag["nodes"]}
requirements = {
    item["from"] for item in dag["edges"]
    if item["to"] == NODE_ID and item["kind"] == "req"
}
require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
require(requirements == REQUIREMENTS, "requirement census")
require(all(nodes[item]["status"] == "PROVED" for item in REQUIREMENTS), "requirement status")
require(any(
    item["from"] == NODE_ID and item["to"] == CONSUMER and item["kind"] == "req"
    for item in dag["edges"]
), "consumer edge")

print(
    "KB_C2_112_SOURCE_LINE_LITERAL_ASSIGNMENT_COVERAGE_PASS "
    "requirements=12 residuals=0 status=PROVED"
)
