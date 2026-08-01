#!/usr/bin/env python3
"""Verify the deployed cell-5 reciprocal trace quadratic node."""

import json
from pathlib import Path
import subprocess
import sys


NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell5_reciprocal_trace_quadratic"
)
ROOT = Path(__file__).resolve().parents[3]
NODE = Path(__file__).resolve().parent
CHECKER = ROOT / "experiments/prize_resolution/check_rate_half_kb_positive_433_1a_cell5_signed_family_decomposition.py"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    process = subprocess.run(
        [sys.executable, str(CHECKER)], capture_output=True, text=True,
        timeout=30,
    )
    require(process.returncode == 0, process.stderr or process.stdout)
    require("deployed_trace=quadratic" in process.stdout, "checker output")

    for filename in (
        "statement.md", "proof.md", "claim_contract.md", "source_evidence.md",
        "dependency_subdag.md", "audit.md", "result.md", "frontier.md",
        "lineage.md", "verify_audit.py",
    ):
        require((NODE / filename).is_file(), filename)
    statement = (NODE / "statement.md").read_text()
    for token in ("(KBRT-1)", "(KBRT-3)", "(KBRT-4)", "does not"):
        require(token in statement, token)

    dag = json.loads((ROOT / "dag.json").read_text())
    node = next(value for value in dag["nodes"] if value["id"] == NODE_ID)
    require(node["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    require((
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
        "cell5_ratio_exceptional_branch_exclusion",
        NODE_ID,
        "req",
    ) in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "evidence edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_RECIPROCAL_TRACE_VERIFY_PASS "
        "generator=1 terms=19 trace_degree=2 route=open"
    )


if __name__ == "__main__":
    main()
