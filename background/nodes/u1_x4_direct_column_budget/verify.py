#!/usr/bin/env python3
"""Fail-closed audit of the u1 minimal-record currency split."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def load_node(node_id):
    for partition in ("critical", "background"):
        path = ROOT / partition / "nodes" / node_id / "node.json"
        if path.exists():
            return json.loads(path.read_text())
    raise AssertionError(f"missing node: {node_id}")


def required_ids(node):
    return {edge["from"] for edge in node.get("requires", [])}


def main():
    u1 = load_node("u1_x4_direct_column_budget")
    assert u1["node"]["status"] == "CONDITIONAL"
    statement = u1["node"]["statement"]
    for token in (
        "R_h^min",
        "F-4 minimal condition",
        "R_min",
        "<16n^3",
        "does not assert that every general order-t",
        "x4_primitive_star_u1_coverage",
    ):
        assert token in statement, token

    expected_inputs = {
        "f3_h1_singleton_injectivity",
        "f3_h2_stratum_theorem",
        "f3_h3_direct_floor_conditional_close",
        "f3_hge4_aggregate_budget",
    }
    assert required_ids(u1) == expected_inputs
    assert load_node("f3_h1_singleton_injectivity")["node"]["status"] == "PROVED"
    assert load_node("f3_h2_stratum_theorem")["node"]["status"] == "PROVED"

    h3 = load_node("f3_h3_direct_floor_conditional_close")
    assert h3["node"]["status"] == "CONDITIONAL"
    assert "R_3 <= T_3 < n^3" in h3["node"]["statement"]

    tail = load_node("f3_hge4_aggregate_budget")
    assert tail["node"]["status"] == "CONDITIONAL"
    assert "F-4 MINIMAL-TRADE SCOPE PIN" in tail["node"]["statement"]
    assert "<= 14 n^3" in tail["node"]["statement"]

    coverage = load_node("x4_primitive_star_u1_coverage")
    assert coverage["node"]["status"] == "TARGET"
    coverage_statement = coverage["node"]["statement"]
    assert "general order-t star-PTE record" in coverage_statement
    assert "D_0+sum_{d>=1}D_d" in coverage_statement
    assert "nonconstant residue needs its own bound" in coverage_statement
    assert "16N^3-1" in coverage_statement
    assert {edge["to"] for edge in u1.get("evidence_for", [])} == {
        "x4_primitive_star_u1_coverage"
    }

    consumer = load_node("x4_exactlist_staircase_split")
    assert "x4_primitive_star_u1_coverage" in required_ids(consumer)
    assert "u1_x4_direct_column_budget" not in required_ids(consumer)

    route_cut = load_node("x4_general_star_minimal_trade_route_cut")
    assert route_cut["node"]["status"] == "PROVED"
    assert {edge["to"] for edge in route_cut.get("evidence_for", [])} == {
        "x4_primitive_star_u1_coverage"
    }

    partition = load_node("x4_general_shiftpair_difference_degree_partition")
    assert partition["node"]["status"] == "PROVED"
    assert "d=0 if and only if" in partition["node"]["statement"]
    assert {edge["to"] for edge in partition.get("evidence_for", [])} == {
        "x4_primitive_star_u1_coverage"
    }

    assert 0 + 1 + 1 + 14 == 16
    print(
        "U1_X4_MINIMAL_CURRENCY_CONTRACT_PASS "
        "inputs=4 coverage=separate partition=d0+nonconstant total=16"
    )


if __name__ == "__main__":
    main()
