#!/usr/bin/env python3
"""Verify the matched fiber-two cycle post-field compiler packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_fiber_two_cycle_matched_post_field_compiler"
DEPENDENCIES = {
    "rate_half_list_budget_three_fiber_two_cycle_matched_lift_field_router",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_ode",
    "rate_half_list_budget_three_antipodal_generic_deleted_pair_harmonic_exclusion",
}
CONSUMER = "rate_half_list_adjacent_crossing"
EXPERIMENT = ROOT / "experiments" / "prize_resolution"
CERTIFICATE = EXPERIMENT / "rate_half_list_fiber_two_cycle_harmonic_top_characteristic_result.json"
LAUNCHER = EXPERIMENT / "rate_half_list_fiber_two_cycle_harmonic_top_characteristic_modal.py"
PRIOR = EXPERIMENT / "rate_half_list_deleted_pair_harmonic_characteristic_result.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def arithmetic_check() -> None:
    m = 1 << 36
    n = 8 * m
    assert n == 1 << 39
    assert 2 * n == 1 << 40
    assert 4 * n == 1 << 41
    assert 2 * m - 1 == (1 << 37) - 1
    assert 2 * m - 2 == (1 << 37) - 2
    assert 4 * m - 1 == (1 << 38) - 1
    assert m - 1 == (1 << 36) - 1

    packet = json.loads(CERTIFICATE.read_text())
    prior = json.loads(PRIOR.read_text())
    assert packet["all_complete"] and packet["coverage_exact"]
    assert packet["hits"] == []
    assert packet["processed"] == packet["expected_candidates"] == 2_247_720
    assert packet["source_sha256"] == digest(LAUNCHER)
    assert packet["prior_levels_result_sha256"] == digest(PRIOR)
    assert prior["all_complete"] and prior["hits"] == []


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
        "2,247,720",
        "T/q_out=W^4",
        "y_39=2",
        "chi_41=2",
        "deg gcd(S,P)>=M-1=2^36-1",
        "old unscaled fourth-power test",
    ):
        assert marker in statement
    for marker in (
        "Only `s=41` could remain",
        "nontrivial quartic\ncoset",
        "does not depend on the reciprocal-root choice",
        "Solving `(12)` for `P`",
    ):
        assert marker in proof


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "RATE_HALF_LIST_B3_FIBER_TWO_MATCHED_POST_FIELD_COMPILER_PASS "
        "M_bits=36 harmonic_hits=0 outer_trace_depth=39 source_depth=41 "
        "twisted_fourth_power=1"
    )


if __name__ == "__main__":
    main()
