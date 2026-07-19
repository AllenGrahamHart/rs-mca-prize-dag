#!/usr/bin/env python3
"""Verify the half-distance A=1 core-stratified slope-slack ledger."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger"
DEPENDENCIES = {
    "rate_half_ca_hankel_minimal_index_budget",
    "rate_half_ca_hankel_exceptional_root_charge",
}
CONSUMER = "rate_half_band_closure"


def profile(m: int, core: int, degree: int) -> tuple[int, int, int, int]:
    rho = 4 * m
    domain = 4 * rho
    residual_degree = rho - core
    regular = residual_degree - (1 + core) * degree
    total = (domain - core) * degree + regular
    cap, remainder = divmod(total, residual_degree)
    return residual_degree, regular, cap, remainder


def chamber_check(m: int, core: int, degree: int) -> None:
    residual_degree, regular, cap, remainder = profile(m, core, degree)
    beta = cap - 4 * degree
    defect = 4 * degree - residual_degree
    coefficient = 4 * defect + 4 * beta - 3 * core
    for component_degree in range(1, degree + 1):
        lower_num = coefficient * component_degree - regular
        upper_num = coefficient * component_degree + remainder
        lower = -((-lower_num) // cap)
        upper = upper_num // cap
        choices = max(0, upper - lower + 1)
        assert choices <= 2
        if core in (1, 2) or (core == 0 and 3 * degree > residual_degree):
            assert choices <= 1


def arithmetic_check(m: int, core: int, degree: int, slack: int, omission: int) -> None:
    rho = 4 * m
    domain = 4 * rho
    residual_degree, regular, cap, remainder = profile(m, core, degree)
    supported = cap - slack
    incidence = supported * residual_degree - omission
    capacity = (domain - core) * degree - incidence
    assert capacity == slack * residual_degree + remainder - regular + omission
    assert omission <= regular
    if capacity >= 0:
        assert capacity <= slack * residual_degree + remainder
        assert (
            supported * ((domain - core) - residual_degree) + omission
            == (domain - core) * (supported - degree) + capacity
        )


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
        "T_max=floor(L/d)",
        "C=ell*d+eta-Delta+O",
        "rank `e+1`",
        "J Rbar=P^d Sbar",
        "lambda*e_i-Delta<=T_max*a_i<=lambda*e_i+eta",
        "#saturated>=m+1",
    ):
        assert marker in packet


def main() -> None:
    profiles = 0
    for m in range(6, 96):
        rho = 4 * m
        for core in range(3):
            residual_degree = rho - core
            for degree in range(m + 1, residual_degree // (core + 1) + 1):
                residual_degree, regular, cap, remainder = profile(m, core, degree)
                if core == 0:
                    assert (cap, remainder) == (4 * degree, residual_degree - degree)
                elif core == 1:
                    assert (cap, remainder) == (4 * degree + 1, degree)
                elif 3 * degree < residual_degree:
                    assert (cap, remainder) == (4 * degree + 1, 3 * degree)
                else:
                    assert 3 * degree == residual_degree
                    assert (cap, remainder) == (4 * degree + 2, 0)
                chamber_check(m, core, degree)
                for slack in {0, cap - rho - 2}:
                    for omission in {0, regular}:
                        arithmetic_check(m, core, degree, slack, omission)
                profiles += 1

    official_m = 1 << 37
    expected = {
        0: (2, 5 * official_m + 1, official_m + 3),
        1: (3, 3 * official_m + 1, 2 * official_m + 5),
        2: (3, official_m + 1, 3 * official_m + 7),
    }
    rho = 4 * official_m
    for core, (slack_max, saturation, clean) in expected.items():
        degree = official_m + 1
        residual_degree, regular, cap, remainder = profile(official_m, core, degree)
        assert cap - rho - 2 == slack_max
        assert (4 * rho - core) - slack_max * residual_degree - remainder == saturation
        assert rho + 2 - regular == clean
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_HALF_DISTANCE_A1_CORE_SLOPE_SLACK_PASS "
        f"profiles={profiles} first_slacks=3+4+4"
    )


if __name__ == "__main__":
    main()
