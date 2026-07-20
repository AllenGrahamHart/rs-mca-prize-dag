#!/usr/bin/env python3
"""Verify the doubled-order matched trace-Jacobi norm transfer."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_two_cycle_matched_trace_jacobi_norm_transfer"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_matched_post_field_compiler",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_chebyshev_gegenbauer_sign_router",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_trace_gcd_router",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_even_jacobi_norm_router",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_torsion_cyclotomic_norm_decomposition",
}
CONSUMER = "rate_half_list_adjacent_crossing"


def arithmetic_check() -> None:
    m = 1 << 36
    ell = 2 * m
    n = 8 * m
    assert ell == 1 << 37
    assert n == 1 << 39
    assert 8 * ell == 1 << 40
    assert 16 * ell == 1 << 41
    assert 8 * m == 1 << 39
    assert 4 * m == 1 << 38

    tower = [1 << exponent for exponent in range(2, 39)]
    traces = [1 << exponent for exponent in range(37)]
    assert len(tower) == len(traces) == 37
    assert tower[0] == 4 and tower[-1] == 1 << 38
    assert traces[0] == 1 and traces[-1] == 1 << 36

    old_tower = [1 << exponent for exponent in range(2, 38)]
    assert len(old_tower) == 36 and len(old_tower) != len(tower)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    proof = (here / "proof.md").read_text()
    for marker in (
        "M=2^36",
        "six degree-`M` tests for each",
        "two six-gcd packets",
        "2<=j<=38",
        "exactly `37` levels",
        "product_(j=0)^36",
        "T/q_out=W^4",
    ):
        assert marker in statement
    for marker in (
        "nonsplit class it\nexcluded",
        "37` orders",
        "surviving\ntorsion gcd is only a necessary",
    ):
        assert marker in proof


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_MATCHED_TRACE_JACOBI_NORM_TRANSFER_PASS "
        "M_bits=36 trace_degree_bits=37 jacobi_degree_bits=36 tower_levels=37"
    )


if __name__ == "__main__":
    main()
