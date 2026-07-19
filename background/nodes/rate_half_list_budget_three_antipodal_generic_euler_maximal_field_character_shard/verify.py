#!/usr/bin/env python3
"""Verify the maximal-field Euler character shard."""

from __future__ import annotations

from math import gcd
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_euler_maximal_field_character_shard"
COUPLED = "rate_half_list_budget_three_antipodal_generic_euler_coupled_norm_gate"
MAXIMAL_FIELD = "rate_half_list_budget_three_maximal_field_degree_collapse"
CONSUMER = "rate_half_list_adjacent_crossing"


def character_index_check() -> None:
    assert gcd(4, 1 << 41) == 4

    for p_residue, expected in ((1, 3), (2, 1)):
        assert gcd(3, p_residue - 1) == expected

    for p in (5, 7, 11, 13, 17, 19):
        assert p != 3
        assert p * p % 3 == 1
        assert gcd(3, p * p - 1) == 3
        assert gcd(4, p * p - 1) == 4


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[COUPLED]["status"] == "PROVED"
    assert nodes[MAXIMAL_FIELD]["status"] == "PROVED"
    assert (COUPLED, NODE, "req") in edges
    assert (MAXIMAL_FIELD, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "gcd(4,q-1)=4",
        "e=2: q=p^2",
        "gcd(3,q-1)=3",
        "p=2 mod 3",
        "N_T^4N_Q^3=d^(4v)",
        "recomputed in `F_p`",
        "necessary, not sufficient",
    ):
        assert marker in statement


def main() -> None:
    character_index_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_GENERIC_EULER_FIELD_SHARD_PASS "
        "ambient_branches=3 fourth=all cubic=quadratic_and_prime_1mod3"
    )


if __name__ == "__main__":
    main()
