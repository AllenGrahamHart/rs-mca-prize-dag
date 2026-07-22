#!/usr/bin/env python3
"""Verify the XR proper-circuit defect and host router."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_rank_two_proper_circuit_defect_host_router"
PARENTS = {
    "xr_rank_two_maxwell_collision_defect_identity",
    "xr_higher_rank_rank_two_shell_maxwell_router",
    "xr_higher_rank_uniform_split_pencil_reduction",
    "xr_trade_circuit_arity_segre_atlas",
}
CONSUMER = "xr_highcore_collision_count"


def mass_floor(t: int, D: int) -> int:
    return t * D // 2 if D % 2 == 0 else t * (D + 1) // 2 - 1


def baseline(h: int, t: int, D: int, Z: int) -> int:
    return t * h + (t - 2) * ((t - 1) * D - 2 * Z)


def positive_cutoff(h: int, t: int, parity: int) -> int:
    if t == 4:
        return 2 * h - 2 if parity == 0 else 2 * h - 3
    if t == 5:
        numerator = 5 * h - (1 if parity == 0 else 10)
        return numerator // 3
    raise ValueError(t)


def formula_check() -> int:
    checks = 0
    for h in range(1, 200, 2):
        for t, delta in ((4, 2), (5, 1)):
            for D in range(3, 5 * h + 10):
                M = mass_floor(t, D)
                D0_max = baseline(h, t, D, M)
                cutoff = positive_cutoff(h, t, D % 2)
                if D > cutoff:
                    assert D0_max < delta
                elif cutoff >= 3:
                    assert D0_max >= delta

                assert (D0_max - delta) % 2 == 0
                if D0_max < delta:
                    proper_lower = (delta - D0_max) // 2
                    assert proper_lower >= 1
                    if D0_max <= 0:
                        full_upper = (-D0_max) // 2
                        assert proper_lower == full_upper + 1
                checks += 1
    return checks


def host_check() -> int:
    checks = 0
    for h in range(1, 50, 2):
        for t, delta in ((4, 2), (5, 1)):
            for D0 in range(-20, 21):
                if D0 % 2 != t % 2:
                    continue
                charge = max(0, (delta - D0) // 2)
                Delta = D0 + 2 * charge
                assert Delta >= delta
                for e in (0, h - 1):
                    r = (Delta + e + h - 1) // h
                    assert h * r >= Delta + e
                    if r > 0:
                        assert h * (r - 1) < Delta + e
                    checks += 1
    return checks


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "Delta_J=D_0+2C>=delta_t",
        "disjointbyexactlyoneintegercharge",
        "r>=ceil((Delta_J+e)/h)",
        "D<=2h-2ifDiseven",
        "doesnotboundthenumber",
    ):
        assert marker in statement


def main() -> None:
    formula_checks = formula_check()
    host_checks = host_check()
    packet_check()
    print(
        "XR_RANK_TWO_PROPER_CIRCUIT_DEFECT_HOST_ROUTER_PASS "
        f"formula_checks={formula_checks} host_checks={host_checks}"
    )


if __name__ == "__main__":
    main()
