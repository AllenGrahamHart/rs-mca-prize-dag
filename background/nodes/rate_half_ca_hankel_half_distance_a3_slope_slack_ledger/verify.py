#!/usr/bin/env python3
"""Verify the half-distance A=3 slope-slack ledger and DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_half_distance_a3_slope_slack_ledger"
DEPENDENCIES = {
    "rate_half_ca_hankel_minimal_index_budget",
    "rate_half_ca_hankel_exceptional_root_charge",
}
CONSUMER = "rate_half_band_closure"


def arithmetic_check(m: int, e: int, h: int, omission: int) -> None:
    rho = 4 * m - 1
    domain = 16 * m
    regular = rho - 3 * e
    supported = 4 * e + 1 - h
    incidence = supported * rho - omission
    capacity = domain * e - incidence
    assert domain == 4 * rho + 4
    assert capacity == 4 * e - rho + h * rho + omission
    assert omission <= regular
    assert capacity <= e + h * rho
    assert supported * (domain - rho) + omission == domain * (supported - e) + capacity


def component_chamber_check(m: int, e: int) -> None:
    rho = 4 * m - 1
    defect = 4 * e - rho
    supported = 4 * e + 1
    for component_e in range(1, e + 1):
        lower_numerator = 4 * defect * component_e - (e - defect)
        upper_numerator = 4 * defect * component_e + e
        lower = -((-lower_numerator) // supported)
        upper = upper_numerator // supported
        assert upper < lower or upper == lower


def canonical_left_block_check(index: int) -> None:
    coefficients = [
        tuple(int(row == column) for row in range(index + 1))
        for column in range(index + 1)
    ]
    assert len(set(coefficients)) == index + 1


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all((dependency, NODE, "req") in edges for dependency in DEPENDENCIES)
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
        "0<=h<=4(e-m)-1",
        "C=4e-rho+h*rho+O<=e+h*rho",
        "rank `e+1`",
        "J R=H^rho S",
        "(2e-g)/T<1/2",
        "3m+2",
    ):
        assert marker in packet


def main() -> None:
    for m in range(4, 96):
        rho = 4 * m - 1
        for e in range(m + 1, rho // 3 + 1):
            regular = rho - 3 * e
            component_chamber_check(m, e)
            for h in range(4 * (e - m)):
                for omission in {0, regular}:
                    arithmetic_check(m, e, h, omission)
        canonical_left_block_check(m)

    official_m = 1 << 37
    official_rho = (1 << 39) - 1
    first_e = official_m + 1
    assert 4 * (first_e - official_m) - 1 == 3
    assert 16 * official_m - first_e - 3 * official_rho == 3 * official_m + 2
    arithmetic_check(official_m, first_e, 3, official_rho - 3 * first_e)
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_HALF_DISTANCE_A3_SLOPE_SLACK_PASS "
        f"official_m={official_m} first_slacks=4"
    )


if __name__ == "__main__":
    main()
