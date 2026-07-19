#!/usr/bin/env python3
"""Verify the A=1 core-one maximal-degree component localization."""

from __future__ import annotations

import json
from math import ceil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_max_component_localization"
DEPENDENCY = "rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger"
CONSUMER = "rate_half_band_closure"


def arithmetic_check(m: int) -> None:
    e = 2 * m - 1
    d = 4 * m - 1
    supported = 4 * e + 1
    residual_domain = 16 * m - 1
    assert d == 2 * e + 1
    assert residual_domain == 8 * e + 7
    regular = d - 2 * e
    total = residual_domain * e + regular
    cap, remainder = divmod(total, d)
    assert (regular, cap, remainder) == (1, supported, e)

    for component_e in range(1, e + 1):
        possible = []
        for defect in range(-2, 4):
            difference = 5 * component_e - supported * defect
            if -1 <= difference <= e:
                possible.append(defect)
        assert len(possible) <= 1
        assert all(defect in (0, 1) for defect in possible)

    residual_e = e // 5
    assert 5 * residual_e <= e
    assert ceil((e + 1) / (residual_e + 1)) >= 5 or m < 12


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    assert f"background/nodes/{NODE}/statement.md" in nodes[CONSUMER]["refs"]

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    packet = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in (
        "r_*=2e_*+1",
        "r_i=2e_i",
        "5b<=C-E<=e",
        "sr(Q_*)>=ceil((e+1)/(b+1))",
        "sr(Q_*)>=5",
        "14m",
    ):
        assert marker in packet


def main() -> None:
    for m in range(3, 512):
        arithmetic_check(m)

    m = 1 << 37
    e = 2 * m - 1
    residual_e = e // 5
    dominant_e = e - residual_e
    assert e % 5 == 3
    assert residual_e == 54_975_581_388
    assert dominant_e == 219_902_325_555
    assert 2 * dominant_e + 1 == 439_804_651_111
    assert ceil((e + 1) / (residual_e + 1)) == 5
    assert (16 * m - 1) - e == 14 * m
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_MAX_COMPONENT_LOCALIZATION_PASS "
        f"official_e={e} dominant_rank=5"
    )


if __name__ == "__main__":
    main()
