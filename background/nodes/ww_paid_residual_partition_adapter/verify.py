#!/usr/bin/env python3
"""Verify the W3 first-match partition and budget adapter."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
NODE_ID = "ww_paid_residual_partition_adapter"
DEPENDENCY = "stratification_partition_thm"
CONSUMER = "ww_row_envelope_clause"


def first_match(bits: tuple[bool, ...]) -> tuple[bool, ...]:
    guards = []
    missed = True
    for bit in bits:
        guards.append(missed and bit)
        missed = missed and not bit
    guards.append(missed)
    return tuple(guards)


def load_inputs() -> tuple[dict[str, Any], dict[str, str]]:
    dag = json.loads((ROOT / "dag.json").read_text())
    here = ROOT / "background/nodes" / NODE_ID
    documents = {
        "statement": (here / "statement.md").read_text(),
        "proof": (here / "proof.md").read_text(),
        "frontier": (
            ROOT
            / "background/nodes/ww_row_envelope_clause/specification_frontier.md"
        ).read_text(),
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

    partition_ok = True
    cases = 0
    for width in range(9):
        for mask in range(1 << width):
            bits = tuple(bool(mask & (1 << index)) for index in range(width))
            guards = first_match(bits)
            partition_ok &= sum(guards) == 1
            expected = next((index for index, bit in enumerate(bits) if bit), width)
            partition_ok &= guards[expected]
            cases += 1

    budget_ok = True
    budget_cases = 0
    for b_star in range(21):
        for paid in range(b_star + 1):
            b_chal = b_star - paid
            for residual in range(b_chal + 1):
                budget_ok &= paid + residual <= b_star
                budget_cases += 1
    overflow_detected = all(
        paid + (b_star - paid + 1) > b_star
        for b_star in range(21)
        for paid in range(b_star + 1)
    )

    statement = documents["statement"]
    proof = documents["proof"]
    return {
        "node_proved": nodes.get(NODE_ID, {}).get("status") == "PROVED",
        "dependency_proved": nodes.get(DEPENDENCY, {}).get("status") == "PROVED",
        "req_wiring_exact": incoming_req == {DEPENDENCY},
        "consumer_evidence_wiring": CONSUMER in outgoing_ev,
        "consumer_retired_target": nodes.get(CONSUMER, {}).get("status") == "TARGET",
        "partition_exhaustive": partition_ok and cases == 511,
        "budget_implication_exhaustive": budget_ok and budget_cases == 1771,
        "budget_overflow_detected": overflow_detected,
        "binding_identity_printed": (
            "B_chal(U) = B* - sum_i u_i(U)" in statement
            and "|X(U)|<=B*" in statement
        ),
        "catch_all_is_fail_closed": (
            "omitted or too-narrow paid" in proof
            and "enlarges the residual" in proof
        ),
        "nonclaims_preserved": (
            "does not define the paid predicates" in statement
            and "prove their bounds" in statement
        ),
    }


def main() -> None:
    checks = evaluate(*load_inputs())
    failures = [name for name, passed in checks.items() if not passed]
    if failures:
        raise SystemExit("W3_PARTITION_ADAPTER_FAIL " + ",".join(failures))
    print(
        "W3_PAID_RESIDUAL_PARTITION_ADAPTER_PASS "
        f"checks={len(checks)} predicate_cases=511 budget_cases=1771"
    )


if __name__ == "__main__":
    main()
