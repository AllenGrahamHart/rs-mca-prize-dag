#!/usr/bin/env python3
"""Verify the W3 two-class minimal-ledger reduction."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
NODE_ID = "ww_two_class_minimal_ledger_reduction"
DEPENDENCY = "ww_paid_residual_partition_adapter"
LEMMA_A = "ww_lemma_a_exhaustion"
CONSUMER = "ww_row_envelope_clause"


def load_inputs() -> tuple[dict[str, Any], dict[str, str]]:
    dag = json.loads((ROOT / "dag.json").read_text())
    here = ROOT / "background/nodes" / NODE_ID
    documents = {
        "statement": (here / "statement.md").read_text(),
        "proof": (here / "proof.md").read_text(),
        "w3": (
            ROOT / "background/nodes/ww_row_envelope_clause/statement.md"
        ).read_text(),
        "frontier": (
            ROOT
            / "background/nodes/ww_row_envelope_clause/specification_frontier.md"
        ).read_text(),
        "roadmap": (ROOT / "notes/PRIZE_RESOLUTION_ROADMAP.md").read_text(),
        "compute": (ROOT / "notes/PRIZE_COMPUTE_REQUESTS.md").read_text(),
    }
    return dag, documents


def evaluate(dag: dict[str, Any], documents: dict[str, str]) -> dict[str, bool]:
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming_req = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge.get("kind") == "req"
    }
    incoming_ev = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE_ID and edge.get("kind") == "ev"
    }
    outgoing_ev = {
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "ev"
    }

    partition_ok = True
    partition_cases = 0
    for width in range(9):
        full = (1 << width) - 1
        for list_mask in range(1 << width):
            for plant_mask in range(1 << width):
                if plant_mask & (full ^ list_mask):
                    continue
                residual_mask = list_mask & (full ^ plant_mask)
                partition_ok &= (plant_mask & residual_mask) == 0
                partition_ok &= (plant_mask | residual_mask) == list_mask
                partition_ok &= (
                    plant_mask.bit_count() + residual_mask.bit_count()
                    == list_mask.bit_count()
                )
                partition_cases += 1

    budget_ok = True
    budget_cases = 0
    for b_star in range(21):
        for planted in range(23):
            for nonplant in range(21):
                safe = planted + nonplant <= b_star
                if planted <= b_star:
                    budget_ok &= safe == (nonplant <= b_star - planted)
                else:
                    budget_ok &= not safe
                budget_cases += 1

    statement = documents["statement"]
    proof = documents["proof"]
    return {
        "node_proved": nodes.get(NODE_ID, {}).get("status") == "PROVED",
        "dependency_proved": nodes.get(DEPENDENCY, {}).get("status") == "PROVED",
        "lemma_a_proved_evidence": (
            nodes.get(LEMMA_A, {}).get("status") == "PROVED" and LEMMA_A in incoming_ev
        ),
        "req_wiring_exact": incoming_req == {DEPENDENCY},
        "consumer_evidence_wiring": CONSUMER in outgoing_ev,
        "consumer_retired_target": nodes.get(CONSUMER, {}).get("status") == "TARGET",
        "partition_exhaustive": partition_ok and partition_cases == 9841,
        "budget_equivalence_exhaustive": budget_ok and budget_cases == 10143,
        "distinct_plant_dedup_printed": (
            "set of distinct printed planted polynomials" in statement
            and "with repeated labels" in statement
        ),
        "minimal_target_printed": (
            "N_nonplant(U) <= B* - p(U)" in statement
            and "optional proof refinement" in statement
        ),
        "lemma_a_not_hidden": (
            "not needed for the two-class identity" in proof
        ),
        "w3_scope_exact": (
            "**status:** TARGET" in documents["w3"]
            and "literal safe-side quantifier" in documents["w3"]
            and "p(U)+N_nonplant(U) >= 7 > 6=B*" in documents["w3"]
        ),
        "frontier_records_scope_counterexample": (
            "Exact scope counterexample" in documents["frontier"]
            and "least seven members" in documents["frontier"]
        ),
        "roadmap_records_rewire": (
            "D0 — RESOLVED BY SCOPE CORRECTION AND REWIRE" in documents["roadmap"]
        ),
        "compute_request_canceled": (
            "Retired request W3: unneeded safe-side non-planted envelope" in documents["compute"]
            and "CANCELED; NO LIVE CONSUMER; DO NOT RUN" in documents["compute"]
        ),
    }


def main() -> None:
    checks = evaluate(*load_inputs())
    failures = [name for name, passed in checks.items() if not passed]
    if failures:
        raise SystemExit("W3_TWO_CLASS_REDUCTION_FAIL " + ",".join(failures))
    print(
        "W3_TWO_CLASS_MINIMAL_LEDGER_REDUCTION_PASS "
        f"checks={len(checks)} partition_cases=9841 budget_cases=10143"
    )


if __name__ == "__main__":
    main()
