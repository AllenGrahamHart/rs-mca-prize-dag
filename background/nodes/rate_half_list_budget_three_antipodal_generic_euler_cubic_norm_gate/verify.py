#!/usr/bin/env python3
"""Verify the generic Euler cubic-norm gate."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_list_budget_three_antipodal_generic_euler_cubic_norm_gate"
DEPENDENCY = "rate_half_list_budget_three_antipodal_generic_euler_divisor_gate"
CONSUMER = "rate_half_list_adjacent_crossing"


def exact_fixture_check() -> None:
    # V=Y^2+1 divides T U^3+d=Y^4-1 for T=U=Y and d=-1.
    v_degree = 2
    res_v_t = 1
    res_v_u = 1
    d_value = -1
    assert res_v_t * res_v_u**3 == (-d_value) ** v_degree


def character_check() -> None:
    p = 7
    cubes = {pow(value, 3, p) for value in range(1, p)}
    assert cubes == {1, 6}
    # tau=0,t_1=1: V(0)=1 passes and V(0)=2 rejects.
    assert 1 in cubes and 2 not in cubes
    assert pow(1, (p - 1) // 3, p) == 1
    assert pow(2, (p - 1) // 3, p) != 1

    for q in (5, 11, 17):
        assert q % 3 == 2
        assert {pow(value, 3, q) for value in range(1, q)} == set(range(1, q))


def official_arithmetic_check() -> None:
    d_value = 1 << 39
    v_value = (1 << 36) - 2
    assert d_value == (1 << 13) ** 3
    assert v_value % 2 == 0
    assert v_value % 3 == 2


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for marker in (
        "Res(V,T) Res(V,U)^3=(-d)^v", "Res(V,T) is a nonzero cube",
        "t_1^2 V(tau) in (F^*)^3", "q=2 mod 3", "not sufficient",
    ):
        assert marker in statement


def main() -> None:
    exact_fixture_check()
    character_check()
    official_arithmetic_check()
    packet_check()
    print(
        "RATE_HALF_ANTIPODAL_GENERIC_EULER_CUBIC_NORM_PASS "
        "scalar=t1^2*V(tau) nontrivial_when=q_mod_3_is_1"
    )


if __name__ == "__main__":
    main()
