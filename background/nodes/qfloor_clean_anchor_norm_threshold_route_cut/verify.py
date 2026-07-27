#!/usr/bin/env python3
"""Verify the qfloor norm-threshold route cut at all clean anchors."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "qfloor_clean_anchor_norm_threshold_route_cut"
PARENT = "qfloor_exact"
TARGET = "unsafe_crossing_family_instantiation"
SOURCE = (
    ROOT
    / "critical/nodes/xr_smallcore_spread_count/notes/"
    "audit_consumption_replay_20260710.py"
)
SOURCE_SHA256 = "c39442d16fcbe86bbfd97f245de970dc729d0e257514c6d4f9f74c9a8c7fac56"
FIELD_CAP = 1 << 256
ROWC_BUDGET = 1 << 122
PRIZE_BUDGET = 317494674775468773183020924238786383963


def main() -> None:
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256

    rows = (
        ("RowC-1/4", 1024, 256, 260, ROWC_BUDGET, 256, 65, 899),
        ("RowC-1/8", 1024, 128, 132, ROWC_BUDGET, 256, 33, 774),
        ("RowC-1/16", 1024, 64, 66, ROWC_BUDGET, 512, 33, 1548),
        ("prize-1/4", 1 << 41, 1 << 39, 558345748480, PRIZE_BUDGET, 256, 65, 899),
        ("prize-1/8", 1 << 41, 1 << 38, 283467841536, PRIZE_BUDGET, 256, 33, 774),
        ("prize-1/16", 1 << 41, 1 << 37, 141733920768, PRIZE_BUDGET, 512, 33, 1548),
    )
    raw_ratios = {}
    for name, n, k, m, budget, expected_order, expected_ell, expected_bits in rows:
        gap = m - k
        assert gap > 0 and n % gap == 0
        order = n // gap
        assert order == expected_order
        assert k * order % n == 0
        ell = k * order // n + 1
        assert ell == expected_ell
        support_complement = (n - m) * order // n
        assert support_complement == order - ell
        threshold = (2 * ell) ** (order // 2)
        assert threshold.bit_length() == expected_bits
        assert threshold > FIELD_CAP
        count = math.comb(order, ell)
        assert count == math.comb(order, support_complement)
        assert count > budget
        raw_ratios[name] = count // budget

    assert min(raw_ratios.values()) >= 1245

    # Negative control: the cap alone does not kill every smaller qfloor order.
    assert (2 * 17) ** 32 < FIELD_CAP

    dag = json.loads((ROOT / "dag.json").read_text())
    status = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert status[NODE] == "PROVED"
    assert status[PARENT] == "PROVED"
    assert status[TARGET] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, TARGET, "ev") in edges
    assert "p>(2ell')^(N'/2)" in status_statement(dag, PARENT)

    print(
        "QFLOOR_CLEAN_ANCHOR_NORM_THRESHOLD_ROUTE_CUT_PASS "
        "rows=6 impossible=6 min_raw_ratio=1245"
    )


def status_statement(dag: dict, node_id: str) -> str:
    return next(entry["statement"] for entry in dag["nodes"] if entry["id"] == node_id)


if __name__ == "__main__":
    main()
