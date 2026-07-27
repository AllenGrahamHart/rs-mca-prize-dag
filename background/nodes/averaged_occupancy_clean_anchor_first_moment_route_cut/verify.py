#!/usr/bin/env python3
"""Verify the complete-support first-moment route cut at six clean anchors."""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "averaged_occupancy_clean_anchor_first_moment_route_cut"
FM1 = "fm1"
CONVERSION = "averaged_slope_conversion"
TARGET = "unsafe_crossing_family_instantiation"
TARGET_BITS = 128
ROWC_BUDGET = 1 << 122
PRIZE_BUDGET = 317494674775468773183020924238786383963

EXPECTED_PIN = {
    "candidate_file": "critical/nodes/xr_smallcore_spread_count/notes/audit_consumption_replay_20260710.py",
    "candidate_file_sha256": "c39442d16fcbe86bbfd97f245de970dc729d0e257514c6d4f9f74c9a8c7fac56",
    "fm1_file": "critical/nodes/fm1/statement.md",
    "fm1_file_sha256": "2055c48edc29644e03813fc28e9dc62cebde52b4ce6663683d20c3e6ad880961",
    "occupancy_file": "critical/nodes/averaged_slope_conversion/statement.md",
    "occupancy_file_sha256": "11de5fba7bfb7704866a91e3822d7749d41406e430fac4f3d705ff20b4ec65e5",
}


def sha256(relative: str) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def complete_support_upper(n: int, k: int, agreement: int, q: int) -> Fraction:
    return sum(
        Fraction(math.comb(n, size), q ** (size - k - 1))
        for size in range(agreement, n + 1)
    )


def main() -> None:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    assert pin == EXPECTED_PIN
    for file_key, hash_key in (
        ("candidate_file", "candidate_file_sha256"),
        ("fm1_file", "fm1_file_sha256"),
        ("occupancy_file", "occupancy_file_sha256"),
    ):
        assert sha256(pin[file_key]) == pin[hash_key]

    # Exact small-parameter replay of the mixed-size geometric domination.
    tail_checks = 0
    for n in range(4, 13):
        q = 2 * n + 1
        for k in range(1, n - 1):
            for agreement in range(k + 1, n + 1):
                first = Fraction(math.comb(n, agreement), q ** (agreement - k - 1))
                assert complete_support_upper(n, k, agreement, q) < 2 * first
                tail_checks += 1

    rows = (
        ("RowC-1/4", 1024, 256, 260, ROWC_BUDGET, None),
        ("RowC-1/8", 1024, 128, 132, ROWC_BUDGET, None),
        ("RowC-1/16", 1024, 64, 66, ROWC_BUDGET, None),
        ("prize-1/4", 1 << 41, 1 << 39, 558345748480, PRIZE_BUDGET, 18),
        ("prize-1/8", 1 << 41, 1 << 38, 283467841536, PRIZE_BUDGET, 23),
        ("prize-1/16", 1 << 41, 1 << 37, 141733920768, PRIZE_BUDGET, 28),
    )
    rowc_slack_bits = []
    prize_exponent_slack = []
    for name, n, k, agreement, budget, rational_exponent in rows:
        t = agreement - k
        q_lower = budget << TARGET_BITS
        assert t >= 2
        assert q_lower > 2 * n
        if rational_exponent is None:
            lhs = 2 * math.comb(n, agreement)
            rhs = budget * q_lower ** (t - 1)
            assert lhs < rhs, name
            rowc_slack_bits.append(rhs.bit_length() - lhs.bit_length())
        else:
            c = rational_exponent
            assert (3 * n) ** 5 < (1 << c) * agreement**5, name
            lhs_exponent = 5 + c * agreement
            rhs_exponent = 5 * (255 * t - 128)
            assert lhs_exponent < rhs_exponent, name
            assert budget.bit_length() == 128
            prize_exponent_slack.append(rhs_exponent - lhs_exponent)

    assert rowc_slack_bits == [40, 309, 23]
    assert prize_exponent_slack == [901943131515, 4432406248827, 1507533520251]

    dag = json.loads((ROOT / "dag.json").read_text())
    statuses = {entry["id"]: entry["status"] for entry in dag["nodes"]}
    statements = {entry["id"]: entry.get("statement", "") for entry in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert statuses[NODE] == "PROVED"
    assert statuses[FM1] == "PROVED"
    assert statuses[CONVERSION] == "PROVED"
    assert statuses[TARGET] == "TARGET"
    assert (FM1, NODE, "req") in edges
    assert (CONVERSION, NODE, "req") in edges
    assert (NODE, TARGET, "ev") in edges
    assert "E[N(A)]<B*" in statements[NODE]
    assert "any support family with |S|>=a" in statements[NODE]

    print(
        "AVERAGED_OCCUPANCY_CLEAN_ANCHOR_FIRST_MOMENT_ROUTE_CUT_PASS "
        f"rows={len(rows)} tail_checks={tail_checks} "
        f"rowc_slack_bits={rowc_slack_bits}"
    )


if __name__ == "__main__":
    main()
