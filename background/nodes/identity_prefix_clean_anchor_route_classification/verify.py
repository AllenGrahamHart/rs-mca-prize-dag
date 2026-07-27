#!/usr/bin/env python3
"""Verify the exact identity-prefix route classification on clean anchors."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "identity_prefix_clean_anchor_route_classification"
PARENT = "identity_prefix_flexible_budget_unsafe_floor"
TARGET = "unsafe_crossing_family_instantiation"
SOURCE = (
    ROOT
    / "critical/nodes/xr_smallcore_spread_count/notes/"
    "audit_consumption_replay_20260710.py"
)
SOURCE_SHA256 = "c39442d16fcbe86bbfd97f245de970dc729d0e257514c6d4f9f74c9a8c7fac56"
ROWC_BUDGET = 1 << 122
PRIZE_BUDGET = 317494674775468773183020924238786383963
TARGET_BITS = 128
BASE_CAP = 194309137781254382992506402317422272798923813601398339285841609906262


def pair_cost(budget: int, dimension: int) -> int:
    return budget * (budget + 1) // 2 * dimension


def impossible_from_budget_interval(budget: int, dimension: int, bits: int) -> bool:
    return budget * dimension >= 1 << (bits + 1)


def uniformly_passes_budget_interval(
    budget: int, dimension: int, domain_size: int, bits: int
) -> bool:
    return pair_cost(budget, dimension) < (budget << bits) - domain_size


def main() -> None:
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256

    # Exhaust both interval-router implications on small exact fields.
    checked = 0
    for bits in range(2, 9):
        for budget in range(1, 20):
            q_lo = budget << bits
            q_hi = (budget + 1) << bits
            for dimension in range(1, 20):
                cost = pair_cost(budget, dimension)
                if impossible_from_budget_interval(budget, dimension, bits):
                    assert all(cost >= q for q in range(q_lo, q_hi))
                for domain_size in range(2, min(q_lo, 9)):
                    if uniformly_passes_budget_interval(
                        budget, dimension, domain_size, bits
                    ):
                        assert all(cost < q - domain_size for q in range(q_lo, q_hi))
                checked += 1

    rows = (
        ("RowC-1/4", 1024, 256, 261, ROWC_BUDGET, "IMPOSSIBLE"),
        ("RowC-1/8", 1024, 128, 133, ROWC_BUDGET, "IMPOSSIBLE"),
        ("RowC-1/16", 1024, 64, 67, ROWC_BUDGET, "PASS"),
        ("prize-1/4", 1 << 41, 1 << 39, 558345748481, PRIZE_BUDGET, "IMPOSSIBLE"),
        ("prize-1/8", 1 << 41, 1 << 38, 283467841537, PRIZE_BUDGET, "IMPOSSIBLE"),
        ("prize-1/16", 1 << 41, 1 << 37, 141733920769, PRIZE_BUDGET, "IMPOSSIBLE"),
    )
    verdicts = {}
    for name, n, k, a_safe, budget, expected in rows:
        m = a_safe - 1
        assert k + 1 <= m <= n
        w = m - k - 1
        if impossible_from_budget_interval(budget, k, TARGET_BITS):
            verdict = "IMPOSSIBLE"
            assert pair_cost(budget, k) >= (budget + 1) << TARGET_BITS
        elif uniformly_passes_budget_interval(budget, k, n, TARGET_BITS):
            verdict = "PASS"
        else:
            verdict = "Q_DEPENDENT"
        assert verdict == expected, (name, verdict, expected)
        verdicts[name] = (verdict, w)

    assert verdicts["RowC-1/4"] == ("IMPOSSIBLE", 3)
    assert verdicts["RowC-1/8"] == ("IMPOSSIBLE", 3)
    assert verdicts["RowC-1/16"] == ("PASS", 1)

    count = math.comb(1024, 66)
    assert (count - 1) // ROWC_BUDGET == BASE_CAP
    assert count > BASE_CAP * ROWC_BUDGET
    assert count <= (BASE_CAP + 1) * ROWC_BUDGET
    assert BASE_CAP.bit_length() == 227
    assert BASE_CAP < ROWC_BUDGET << TARGET_BITS

    # Boundary mutations catch the equality and base-field off-by-one.
    assert impossible_from_budget_interval(ROWC_BUDGET, 128, TARGET_BITS)
    assert not impossible_from_budget_interval(ROWC_BUDGET, 127, TARGET_BITS)
    assert not (count > (BASE_CAP + 1) * ROWC_BUDGET)

    dag = json.loads((ROOT / "dag.json").read_text())
    status = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert status[NODE] == "PROVED"
    assert status[PARENT] == "PROVED"
    assert status[TARGET] == "TARGET"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, TARGET, "ev") in edges

    print(
        "IDENTITY_PREFIX_CLEAN_ANCHOR_ROUTE_CLASSIFICATION_PASS "
        f"router_checks={checked} impossible=5 conditional_base_cutoff={BASE_CAP}"
    )


if __name__ == "__main__":
    main()
