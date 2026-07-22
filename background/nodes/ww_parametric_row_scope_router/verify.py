#!/usr/bin/env python3
"""Verify the W3 parametric row-scope repair and its DAG wiring."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
NODE_ID = "ww_parametric_row_scope_router"
OFFICIAL = "official_row_primes_pinning"
DESCRIPTOR = "descriptor"
CONSUMER = "ww_row_envelope_clause"


def load_inputs() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, str]]:
    sys.path.insert(0, str(ROOT / "tools"))
    from prize_row_descriptor import INPUT_SCHEMA, describe_row

    dag = json.loads((ROOT / "dag.json").read_text())
    official = json.loads(
        (
            ROOT
            / "critical/nodes/official_row_primes_pinning"
            / "official_row_primes_reframe.json"
        ).read_text()
    )
    descriptor = describe_row(
        {
            "schema": INPUT_SCHEMA,
            "p": "17",
            "extension_degree": 32,
            "subgroup_log2": 9,
            "rate": "1/2",
        }
    )
    documents = {
        "statement": (
            ROOT / "background/nodes/ww_row_envelope_clause/statement.md"
        ).read_text(),
        "frontier": (
            ROOT
            / "background/nodes/ww_row_envelope_clause/specification_frontier.md"
        ).read_text(),
        "attack": (
            ROOT / "background/nodes/ww_row_envelope_clause/attack.md"
        ).read_text(),
        "roadmap": (ROOT / "notes/PRIZE_RESOLUTION_ROADMAP.md").read_text(),
        "compute": (ROOT / "notes/PRIZE_COMPUTE_REQUESTS.md").read_text(),
    }
    return dag, official, descriptor, documents


def evaluate(
    dag: dict[str, Any],
    official: dict[str, Any],
    descriptor: dict[str, Any],
    documents: dict[str, str],
) -> dict[str, bool]:
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

    frontier = documents["frontier"]
    return {
        "scope_node_proved": nodes.get(NODE_ID, {}).get("status") == "PROVED",
        "proved_dependencies": (
            nodes.get(OFFICIAL, {}).get("status") == "PROVED"
            and nodes.get(DESCRIPTOR, {}).get("status") == "PROVED"
        ),
        "req_wiring_exact": incoming_req == {OFFICIAL, DESCRIPTOR},
        "consumer_evidence_wiring": CONSUMER in outgoing_ev,
        "consumer_retired_target": nodes.get(CONSUMER, {}).get("status") == "TARGET",
        "official_scope_pin": (
            official.get("verdict") == "no_fixed_official_primes"
            and "for every choice of F, L, and k"
            in official.get("quote_fragments", [])
        ),
        "descriptor_exact_q": (
            descriptor["field"]["order_decimal"] == str(17**32)
            and descriptor["evaluation_domain"]["order_decimal"] == "512"
            and descriptor["code"]["dimension_decimal"] == "256"
        ),
        "descriptor_exact_budget": descriptor["target"]["B_star_decimal"] == "6",
        "exact_scope_counterexample_printed": (
            "q=1705*2^120+1" in documents["statement"]
            and "p(U)+N_nonplant(U) >= 7 > 6=B*" in documents["statement"]
            and "outside W3's" in documents["statement"]
        ),
        "parameterized_scope_check_exercised": (
            "admissible prime" in frontier
            and "no exhaustive" in frontier
        ),
        "envelope_retired": (
            "OPEN BUT RETIRED FROM THE PRIZE REQUIREMENT PATH" in frontier
            and "Do not run the former W3 envelope campaign" in frontier
        ),
        "attack_rejects_raw_sweep": (
            "No further W3 computation is authorized" in documents["attack"]
            and "no longer consumed" in documents["attack"]
        ),
        "roadmap_gate_repaired": (
            "D0 — RESOLVED BY SCOPE CORRECTION AND REWIRE" in documents["roadmap"]
            and "Track-N gate event, W3 scope correction and consumer repair" in documents["roadmap"]
        ),
        "large_run_canceled": (
            "Retired request W3: unneeded safe-side non-planted envelope"
            in documents["compute"]
            and "CANCELED; NO LIVE CONSUMER; DO NOT RUN"
            in documents["compute"]
        ),
    }


def main() -> None:
    checks = evaluate(*load_inputs())
    failures = [name for name, passed in checks.items() if not passed]
    if failures:
        raise SystemExit("W3_SCOPE_ROUTER_FAIL " + ",".join(failures))
    print(
        "W3_PARAMETRIC_ROW_SCOPE_ROUTER_PASS "
        f"checks={len(checks)} dependencies=2 consumer_retired=1 compute_canceled=1"
    )


if __name__ == "__main__":
    main()
