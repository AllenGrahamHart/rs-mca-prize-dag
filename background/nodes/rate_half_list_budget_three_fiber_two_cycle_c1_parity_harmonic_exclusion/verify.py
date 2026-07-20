#!/usr/bin/env python3
"""Verify the c=1 parity harmonic exclusion certificate and wiring."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_two_cycle_c1_parity_harmonic_exclusion"
DEPENDENCY = (
    "rate_half_list_budget_three_fiber_two_cycle_c1_parity_harmonic_field_router"
)
CONSUMER = "rate_half_list_adjacent_crossing"
EXPERIMENT = ROOT / "experiments" / "prize_resolution"
CHECKER = (
    EXPERIMENT
    / "rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_check.py"
)
SOURCE = (
    EXPERIMENT
    / "rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_modal.py"
)
RESULT = (
    EXPERIMENT
    / "rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_result.json"
)


def main() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet["all_complete"] and packet["coverage_exact"]
    assert packet["processed"] == packet["expected_candidates"] == 4_495_441
    assert packet["hits"] == []
    assert packet["source_sha256"] == hashlib.sha256(SOURCE.read_bytes()).hexdigest()

    completed = subprocess.run(
        ["python3", str(CHECKER)],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert "candidates=4495441 shards=32 hits=0 traces=2" in completed.stdout

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "q_out!=-1",
        "4,495,441",
        "899,088",
        "longest\nshard took 3.121 seconds",
        "six nonharmonic",
    ):
        assert marker in statement

    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_C1_PARITY_HARMONIC_EXCLUSION_PASS "
        "candidates=4495441 shards=32 traces=2 hits=0"
    )


if __name__ == "__main__":
    main()

