#!/usr/bin/env python3
"""Independent packet audit for the E31 three-profile exclusion."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e31_three_profile_joint_exclusion"
NOTES = ROOT / "background/nodes/e1_n256_s16_e31_profile_parity_light_reduction/notes"
PRODUCTION = NOTES / "e31_three_profile_joint_census_result.json"
AUDIT = NOTES / "e31_three_profile_joint_census_audit_result.json"
FIELDS = ("count", "full_conductor", "maximum_m3", "maximum_full_conductor_m3")


def aggregate(packet: dict[str, object]) -> dict[str, dict[str, int]]:
    rows = packet["rows"]
    assert isinstance(rows, list)
    answer = {}
    for profile in ("profile_37", "profile_251", "profile_132"):
        profile_rows = [row[profile] for row in rows]
        answer[profile] = {
            "count": sum(item["count"] for item in profile_rows),
            "full_conductor": sum(item["full_conductor"] for item in profile_rows),
            "maximum_m3": max(item["maximum_m3"] for item in profile_rows),
            "maximum_full_conductor_m3": max(
                item["maximum_full_conductor_m3"] for item in profile_rows
            ),
        }
    return answer


def main() -> None:
    production = json.loads(PRODUCTION.read_text())
    audit = json.loads(AUDIT.read_text())
    assert production["completed_templates"] == production["expected_templates"] == 8
    assert audit["completed_templates"] == audit["expected_templates"] == 8
    assert len(production["rows"]) == len(audit["rows"]) == 8
    assert aggregate(production) == production["summary"]
    assert aggregate(audit) == audit["summary"]
    assert production["summary"] == audit["summary"]

    row_pairs = zip(production["rows"], audit["rows"])
    for left, right in row_pairs:
        assert left["template"] == right["template"]
        assert left["light"] == right["light"]
        assert left["supports"] == right["supports"] == math.comb(124, 3)
        assert left["vectors"] == right["vectors"] == math.comb(124, 3) * 64
        for profile in ("profile_37", "profile_251", "profile_132"):
            assert all(left[profile][field] == right[profile][field] for field in FIELDS)

    summary = production["summary"]
    assert summary["profile_251"]["maximum_m3"] == 1068 < 1302
    assert summary["profile_132"]["maximum_m3"] == 1122 < 1302
    assert summary["profile_37"]["maximum_full_conductor_m3"] == 1206 < 1302
    assert summary["profile_37"]["maximum_m3"] == 1380 > 1302
    assert summary["profile_37"]["count"] - summary["profile_37"]["full_conductor"] == 3348

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    incoming = {
        edge["from"]
        for edge in dag["edges"]
        if edge["to"] == NODE and edge.get("kind", "req") == "req"
    }
    assert incoming == {
        "e1_n256_s16_e31_profile_parity_light_reduction",
        "collision_norm_criterion",
        "e1_n256_proper_conductor_collision_exclusion",
    }
    assert all(nodes[source]["status"] == "PROVED" for source in incoming | {NODE})
    statement = (ROOT / nodes[NODE]["refs"][0]).read_text()
    assert "158,783,488" in statement
    assert "proper-conductor theorem excludes its complement" in statement

    print(
        "E1_N256_S16_E31_THREE_PROFILE_JOINT_EXCLUSION_AUDIT_PASS "
        "rows=8 agreement=exact cubic_global=2 cubic_full=1 conductor_complement=3348 mutations=4"
    )


if __name__ == "__main__":
    main()
