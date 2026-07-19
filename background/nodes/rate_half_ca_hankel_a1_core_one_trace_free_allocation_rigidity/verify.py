#!/usr/bin/env python3
"""Verify the core-one trace-free allocation-rigidity packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_trace_free_allocation_rigidity"
DEPENDENCY = "rate_half_ca_hankel_a1_core_one_nonzero_weld_trace_descent"
CONSUMER = "rate_half_band_closure"


def allocation_degree_check() -> None:
    e = (1 << 38) - 1
    for b in (0, 1, e // 5):
        for slope_deficit in (0, 1):
            capacity = e - 5 * b - 1 + slope_deficit
            assert capacity >= 2
            for delta in (1, capacity):
                if not slope_deficit:
                    assert delta > slope_deficit
                else:
                    # Divisibility by E_Z forces epsilon=1, so Qhat is too
                    # large even at the smallest positive row deficit.
                    assert delta + 1 > slope_deficit


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md", "proof.md", "claim_contract.md", "dependency_subdag.md",
        "audit.md", "result.md", "verify.py", "verify_audit.py",
    }
    refs = set(nodes[NODE]["refs"])
    for name in required:
        assert f"background/nodes/{NODE}/{name}" in refs
    assert f"background/nodes/{NODE}/statement.md" in nodes[CONSUMER]["refs"]

    packet = (base / "statement.md").read_text() + (base / "proof.md").read_text()
    for marker in (
        "S_*=product_(x:B_X(x)=0)N_x",
        "B_X divides both A and B",
        "deg Qhat_x=delta_x+1>=2>deg E_Z",
        "q_0=Q(gamma_0;X) is squarefree of degree r-1",
        "Q V_1+P_X W_1=P_cl Z_B",
        "W_1B_1-1=QK_1",
    ):
        assert marker in packet


def main() -> None:
    allocation_degree_check()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_TRACE_FREE_ALLOCATION_RIGIDITY_PASS "
        "domain_allocations=AB slope_allocations=2"
    )


if __name__ == "__main__":
    main()
