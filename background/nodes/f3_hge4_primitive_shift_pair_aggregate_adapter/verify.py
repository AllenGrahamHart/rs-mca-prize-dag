#!/usr/bin/env python3
"""Verify the HGE4 primitive shift-pair aggregate adapter."""

from __future__ import annotations

import json
from fractions import Fraction
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_primitive_shift_pair_aggregate_adapter"
DEPENDENCIES = {
    "x81_minimal_trade_square_shift",
    "x82_square_shift_certifier_keys",
    "x83_uniform_square_shift_obstruction_gate",
    "f3_shiftpair_weld",
    "v13_prefix_collision_ledger",
    "v13_second_moment_shift_pair_identity",
}
CONSUMER = "f3_hge4_norm_gate_count"


def arithmetic_check() -> None:
    tail_majorant = Fraction(1, factorial(4) ** 2) + Fraction(1, 14000)
    assert tail_majorant == Fraction(1, 576) + Fraction(1, 14000)
    assert tail_majorant < Fraction(1, 553)

    for power in range(13, 42):
        n = 2**power
        coefficient = Fraction(3500, n) + Fraction(7000, 553)
        assert coefficient < 14


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
        "C_h=sp_(h-1)(h;H)",
        "N_h^strip<=SP_h^prim<=C_h",
        "SP_h^prim<=7000n max(1,B_h)",
        "sum_(h=4)^H_max N_h^strip <14n^3",
        "creates no new conditional DAG premise",
    ):
        assert marker in text


def main() -> None:
    arithmetic_check()
    packet_check()
    print(
        "F3_HGE4_PRIMITIVE_SHIFT_PAIR_AGGREGATE_ADAPTER_PASS "
        "constant=7000 tail=1/553 rows=29"
    )


if __name__ == "__main__":
    main()

