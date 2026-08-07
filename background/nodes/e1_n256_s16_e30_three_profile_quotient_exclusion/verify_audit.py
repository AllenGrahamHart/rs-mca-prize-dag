#!/usr/bin/env python3
"""Independent packet audit of the E30 quotient exclusions."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e30_three_profile_quotient_exclusion"
RESULT = ROOT / "background/nodes/e1_n256_s16_e30_three_profile_quotient_exclusion/notes/e30_eight_profile_quotient_probe_result.json"
EXPECTED = {
    "6,6": {128: (8_089_426, 1712), 64: (3_316_117, 1694)},
    "2,7": {128: (271_115, 1600), 64: (164_143, 1600)},
    "5,4,1": {128: (5_421_301, 1430), 64: (3_086_861, 1376)},
    "1,5,1": {128: (99_689, 1344), 64: (75_961, 1344)},
    "4,2,2": {128: (970_010, 1230), 64: (690_477, 1230)},
    "0,3,2": {128: (6_892, 936), 64: (6_084, 936)},
    "6,2,0,1": {128: (1_154_703, 1058), 64: (724_659, 1048)},
    "3,0,3": {128: (25_884, 1002), 64: (21_368, 940)},
}


def main() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet["complete"] is True
    assert len(packet["rows"]) == 128
    total = 0
    for profile, orders in EXPECTED.items():
        for order, (tested, maximum) in orders.items():
            rows = [
                row for row in packet["rows"]
                if packet["profiles"][row["profile"]] == profile and row["order"] == order
            ]
            assert len(rows) == 8
            assert {row["shard"] for row in rows} == set(range(8))
            assert sum(row["tested"] for row in rows) == tested
            assert max(row["best"] for row in rows) == maximum
            total += tested
    assert total == 24_124_690

    closed = {
        profile for profile, orders in EXPECTED.items()
        if max(maximum for _, maximum in orders.values()) <= 1087
    }
    assert closed == {"0,3,2", "6,2,0,1", "3,0,3"}
    assert sum(sum(EXPECTED[profile][order][0] for order in (128, 64)) for profile in closed) == 1_939_590
    assert 44**32 < 2**250

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE and edge.get("kind", "req") == "req"
    }
    assert incoming == {
        "e1_n256_s16_e30_profile_parity_light_reduction",
        "collision_norm_criterion",
    }
    assert all(nodes[source]["status"] == "PROVED" for source in incoming | {NODE})
    contract = (ROOT / nodes[NODE]["refs"][2]).read_text()
    assert all(profile in contract for profile in ("(6,6)", "(2,7)", "(5,4,1)", "(1,5,1)", "(4,2,2)"))

    print(
        "E1_N256_S16_E30_THREE_PROFILE_QUOTIENT_EXCLUSION_AUDIT_PASS "
        "profiles=8 closed=3 residual=5 allocations=24124690 mutations=4"
    )


if __name__ == "__main__":
    main()
