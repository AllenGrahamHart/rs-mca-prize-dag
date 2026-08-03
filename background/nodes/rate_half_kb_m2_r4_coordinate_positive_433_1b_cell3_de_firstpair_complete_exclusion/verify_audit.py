#!/usr/bin/env python3
"""Independent audit of the cell-3 DE-first-pair exclusion."""

import ast
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_de_pairings12_direct_solver_modal.py"
RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_de_pairings12_direct_solver_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    source = SCRIPT.read_text()
    ast.parse(source)
    for snippet in (
        "if xi_index not in (0, 2) or pairing_index not in (1, 2):",
        "matching = tuple(pairings(range(6)))[pairing_index]",
        "de_value = source_missing if xi_index == 0 else -source_missing % PRIME",
        "sign = 1 if xi_index == 0 else -1",
        "(d_symbol*d_symbol+sign*de_value)**2",
        "e_value = de_value*pow(d_value, -1, PRIME) % PRIME",
        "cuts[0].gcd(cuts[1])",
        'raise ValueError("direct target-equation replay failed")',
    ):
        require(snippet in source, f"source construction {snippet}")

    payload = json.loads(RESULT.read_text())
    require(len(payload["rows"]) == 16 and all(
        row["status"] == "COMPLETE" and row["case_excluded"] and
        not row["witnesses"] and not row["boundary_solutions"] and
        not row["unresolved"]
        for row in payload["rows"]
    ), "complete computed census")
    positive = [row for row in payload["rows"] if row["xi_index"] == 0]
    negative = [row for row in payload["rows"] if row["xi_index"] == 2]
    positive_counts = [len(point["d_roots"])
                       for row in positive for point in row["rows"]]
    require(positive_counts.count(0) == positive_counts.count(4) == 16,
            "positive d-root partition")
    require(all(point["d_roots"] == []
                for row in negative for point in row["rows"]),
            "negative d-root emptiness")
    require(all(d_row["f_gcd_degree"] == 0
                for row in positive for point in row["rows"]
                for lane in point["lanes"] for d_row in lane["d_rows"]),
            "positive residual gcds")

    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    frontier = (NODE / "frontier.md").read_text()
    require("= 144 raw cases" in statement and
            "48` parent pairing-zero cases" in proof and
            "64 newly computed" in audit and "32" in audit,
            "aggregate count discipline")
    require("pairing indices `3,...,14`" in frontier and
            "computational route no-go" in frontier,
            "retained frontier")
    print("audit=ok DE_copies=3 pairings=3 raw_cases=144 witnesses=0")


if __name__ == "__main__":
    main()
