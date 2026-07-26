#!/usr/bin/env python3
"""Verify the tangent-floor route classification on six clean anchors."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "tangent_clean_anchor_route_classification"
PARENT = "rs_tangent_flexible_budget_unsafe_floor"
TARGET = "unsafe_crossing_family_instantiation"
SOURCE = (
    ROOT
    / "critical/nodes/xr_smallcore_spread_count/notes/"
    "audit_consumption_replay_20260710.py"
)
SOURCE_SHA256 = "c39442d16fcbe86bbfd97f245de970dc729d0e257514c6d4f9f74c9a8c7fac56"
TARGET_BITS = 128
ROWC_BUDGET = 1 << 122
PRIZE_BUDGET = 317494674775468773183020924238786383963


def tangent_cutoff(error_count: int, bits: int = TARGET_BITS) -> int:
    return (error_count << bits) - 1


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == {
        "candidate_file": str(SOURCE.relative_to(ROOT)),
        "candidate_file_sha256": SOURCE_SHA256,
        "parent_node": PARENT,
        "target_bits": TARGET_BITS,
    }
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256

    rows = (
        ("RowC-1/4", 1024, 260, ROWC_BUDGET, 764,
         259975728327596986086018200077870913552383, 138),
        ("RowC-1/8", 1024, 132, ROWC_BUDGET, 892,
         303531871293477109409330149829137244618751, 138),
        ("RowC-1/16", 1024, 66, ROWC_BUDGET, 958,
         325990507510259047997912873919633946574847, 138),
        ("prize-1/4", 1 << 41, 558345748480, PRIZE_BUDGET, 1640677507072,
         558293625460404914753807606097620113508566231416831, 169),
        ("prize-1/8", 1 << 41, 283467841536, PRIZE_BUDGET, 1915555414016,
         651829730249582701518843435391462226766545914167295, 169),
        ("prize-1/16", 1 << 41, 141733920768, PRIZE_BUDGET, 2057289334784,
         700059284281502497819565034871099566415191688085503, 169),
    )
    for name, n, agreement, budget, expected_e, expected_cutoff, expected_bits in rows:
        error_count = n - agreement
        assert error_count == expected_e, name
        cutoff = tangent_cutoff(error_count)
        assert cutoff == expected_cutoff, name
        assert cutoff.bit_length() == expected_bits, name
        assert error_count > cutoff // (1 << TARGET_BITS)
        assert not error_count > (cutoff + 1) // (1 << TARGET_BITS)
        assert error_count <= budget, name

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[PARENT] == "PROVED"
    assert statuses[TARGET] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, TARGET, "ev") in edges
    assert "q<=e*2^128-1" in statements[NODE]
    assert "pays none of the six named envelope anchors" in statements[NODE]

    print(
        "TANGENT_CLEAN_ANCHOR_ROUTE_CLASSIFICATION_PASS "
        f"rows={len(rows)} low_field_branches={len(rows)} named_anchor_payments=0"
    )


if __name__ == "__main__":
    main()
