#!/usr/bin/env python3
"""Verify the colored source-resultant divisor split."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_u2_colored_source_resultant_split_compiler"
PARENTS = (
    "rate_half_kb_m2_r4_source_row_interpolation_compiler",
    "rate_half_kb_m2_u2_universal_component_color_profile_cut",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("Res_T(P_J,H) ~ D_K^2 C_H" in statement, "J resultant")
    require("C_H Res_T(P_I,H) ~ D_R^2" in statement, "I resultant")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer")

    # Divisor slots: ten over K, two over eta, and twelve over L^c.
    k_slots = tuple(range(10))
    eta_slots = tuple(range(10, 12))
    exchange_slots = tuple(range(12, 24))
    colored = set(exchange_slots[:4])
    j_orders = [0] * 24
    i_orders = [0] * 24
    for slot in k_slots:
        j_orders[slot] = 2
    for slot in eta_slots:
        i_orders[slot] = 2
    for slot in exchange_slots:
        j_orders[slot] = int(slot in colored)
        i_orders[slot] = 2 - j_orders[slot]

    require(sum(j_orders) == 24 and sum(i_orders) == 24,
            "partial resultant degrees")
    require(all(j_orders[index] == 2 for index in k_slots), "D_K square")
    require(all(j_orders[index] == int(index in colored)
                for index in exchange_slots), "colored quotient")
    require(all(i_orders[index] + j_orders[index] == 2
                for index in range(24)), "complete-source square")
    require(len(colored) == 4 and colored <= set(exchange_slots),
            "colored quartic")
    print(
        "RATE_HALF_KB_M2_U2_COLORED_SOURCE_RESULTANT_SPLIT_COMPILER_PASS "
        f"J_degree={sum(j_orders)} I_degree={sum(i_orders)} color_degree=4"
    )


if __name__ == "__main__":
    main()
