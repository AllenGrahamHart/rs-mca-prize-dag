#!/usr/bin/env python3
"""Verify the QA.22/W3 currency boundary and repaired wiring."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
NODE_ID = "ww_qa22_currency_separation"
XR_BUDGET = "xr_target_budget_audit"
TWO_CLASS = "ww_two_class_minimal_ledger_reduction"
SAME_SLOPE = "xr_sameslope_list_crossover"
W3 = "ww_row_envelope_clause"
WORST = "worst_word_challenger_pricing"


def load_inputs() -> tuple[dict[str, Any], dict[str, str]]:
    dag = json.loads((ROOT / "dag.json").read_text())
    documents = {
        "xr": (
            ROOT / "critical/nodes/xr_clean_residual_any_gate/statement.md"
        ).read_text(),
        "xr_split": (
            ROOT / "critical/nodes/xr_smallcore_spread_count/conditional.md"
        ).read_text(),
        "w3": (
            ROOT / "background/nodes/ww_row_envelope_clause/statement.md"
        ).read_text(),
        "worst": (
            ROOT / "background/nodes/worst_word_challenger_pricing/conditional.md"
        ).read_text(),
        "frontier": (
            ROOT
            / "background/nodes/ww_row_envelope_clause/specification_frontier.md"
        ).read_text(),
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
    outgoing_ev = {
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "ev"
    }
    old_cross_kinds = [
        edge.get("kind")
        for edge in dag["edges"]
        if edge["from"] == XR_BUDGET and edge["to"] == WORST
    ]
    return {
        "currency_node_proved": nodes.get(NODE_ID, {}).get("status") == "PROVED",
        "dependencies_proved": (
            nodes.get(XR_BUDGET, {}).get("status") == "PROVED"
            and nodes.get(TWO_CLASS, {}).get("status") == "PROVED"
            and nodes.get(SAME_SLOPE, {}).get("status") == "PROVED"
        ),
        "req_wiring_exact": incoming_req == {XR_BUDGET, TWO_CLASS},
        "evidence_consumers": {W3, WORST}.issubset(outgoing_ev),
        "cross_edge_demoted": old_cross_kinds == ["ev"],
        "consumer_statuses_preserved": (
            nodes.get(W3, {}).get("status") == "TARGET"
            and nodes.get(WORST, {}).get("status") == "CONDITIONAL"
        ),
        "mca_currency_printed": (
            "for every pair (u,v)" in documents["xr"]
            and "bad-slope count" in documents["xr"]
            and "R_post(u,v; A) <= 16 n^3 per pair" in documents["xr"]
        ),
        "conversion_gap_printed": (
            "same-slope population = the LIST lane's debt" in documents["xr_split"]
        ),
        "w3_currency_printed": (
            "receiver `U`" in documents["w3"]
            and "p(U) + N_nonplant(U) <= B*" in documents["w3"]
        ),
        "qa22_removed_from_w3_budget": (
            "prevent reusing" in documents["w3"]
            and "MCA `16n^3`" in documents["w3"]
        ),
        "direct_assembly_repaired": (
            "List(U)=p(U)+N_nonplant(U)" in documents["worst"]
            and "QA.22 remains evidence only" in documents["worst"]
        ),
        "frontier_keeps_type_boundary": (
            "MCA bad slopes per ordered pair" in documents["frontier"]
            and "list codewords per word" in documents["frontier"]
        ),
        "compute_rerun_rejected": (
            "Do not spend contributor or Modal compute extending the old W3/QA.22 sweep"
            in documents["compute"]
            and "Literal safe-side W3 remains open" in documents["compute"]
        ),
    }


def main() -> None:
    checks = evaluate(*load_inputs())
    failures = [name for name, passed in checks.items() if not passed]
    if failures:
        raise SystemExit("WW_QA22_CURRENCY_FAIL " + ",".join(failures))
    print(
        "WW_QA22_CURRENCY_SEPARATION_PASS "
        f"checks={len(checks)} currencies=2 cross_edge=ev consumers=2"
    )


if __name__ == "__main__":
    main()
