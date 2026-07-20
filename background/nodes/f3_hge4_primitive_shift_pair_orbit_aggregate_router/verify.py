#!/usr/bin/env python3
"""Verify the HGE4 primitive shift-pair orbit aggregate router."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_primitive_shift_pair_orbit_aggregate_router"
DEPENDENCIES = {
    "x82_square_shift_certifier_keys",
    "f3_shiftpair_weld",
    "f3_hge4_primitive_shift_pair_aggregate_adapter",
}
CONSUMER = "f3_hge4_norm_gate_count"


def polynomial_gap(n: int) -> int:
    return 24 * (n - 1) * (n - 2) * (n - 3) - 7000 * n * n - 4_032_000


def arithmetic_check() -> None:
    assert polynomial_gap(2**13) > 0
    for power in range(13, 42):
        n = 2**power
        assert polynomial_gap(n) > 0
        assert 72 * n * n - 14_216 * n - 6_856 > 0
        assert comb(n, 4) > 7000 * n * (1 + Fraction(n * n, 576))

        for h in (4, 5, 8, 16):
            if h > n // 2:
                continue
            mean_upper = Fraction(1, factorial(h) * n ** (h - 2))
            benchmark_upper = Fraction(n * n, factorial(h) ** 2)
            assert mean_upper < 1
            assert benchmark_upper <= Fraction(n * n, 576)
            assert comb(n, h) >= comb(n, 4)
            assert 7000 * n * (1 + benchmark_upper) < comb(n, h)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "SP_h^prim=n O_h^prim",
        "A_h^left=h O_h^prim",
        "sum_(h=4)^H_max O_h^prim<=14n^2",
        "O_h^prim<=7000 max(1,B_h)",
        "7000n max(1,B_h)<M_h",
        "route separation",
    ):
        assert marker in text


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "F3_HGE4_PRIMITIVE_SHIFT_PAIR_ORBIT_AGGREGATE_ROUTER_PASS "
        "rows=29 orbit_budget=14n^2"
    )


if __name__ == "__main__":
    main()
