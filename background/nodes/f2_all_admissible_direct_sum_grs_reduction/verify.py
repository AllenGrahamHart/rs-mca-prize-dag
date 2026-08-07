#!/usr/bin/env python3
"""Verify the minus-branch counterexample and corrected DAG split."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f2_all_admissible_direct_sum_grs_reduction"
SURVIVOR = "f2_admissible_direct_sum_grs_reduction"
CONSUMER = "f2_conditional_close"


def main() -> None:
    result = json.loads(
        (ROOT / "notes/pilots_20260806/f2_minus_branch/counterexample_result.json").read_text()
    )
    assert result["status"] == "PASS"

    p = (1 << 61) - 1
    n = 1 << 41
    assert p % n == n - 1
    assert pow(p, 2, n) == 1
    assert p % n != 1
    assert (p * p).bit_length() < 256
    assert (p - 1) & -(p - 1) == 2
    assert n // 2 == 1 << 40

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "REFUTED"
    assert nodes[SURVIVOR]["status"] == "PROVED"
    assert "plus branch" in nodes[SURVIVOR]["statement"].lower()
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (NODE, CONSUMER, "ev") in edges
    print("F2_ALL_ADMISSIBLE_DIRECT_SUM_REFUTED_PASS witness=1 survivor=1 dag=1/1")


if __name__ == "__main__":
    main()
