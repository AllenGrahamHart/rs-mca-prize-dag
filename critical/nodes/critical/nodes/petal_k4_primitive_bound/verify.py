#!/usr/bin/env python3
"""Contract audit for the K4 b4=1 closure."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


def main() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    node = nodes["petal_k4_primitive_bound"]
    if node["status"] != "PROVED" or "b4=1" not in node["statement"]:
        raise AssertionError(node)

    required = {
        ("petal_retained_zero_effective_degree", "petal_full_touched_set_injection", "req"),
        ("petal_full_touched_set_injection", "petal_top_band_tail_collapse", "req"),
        ("petal_top_band_tail_collapse", "petal_k4_primitive_bound", "req"),
        ("petal_k4_primitive_bound", "petal_growth", "req"),
    }
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    if not required <= edges:
        raise AssertionError(sorted(required - edges))

    g1 = nodes["petal_g1_layer_maps"]["statement"]
    for pin in ("|R0|<ell", "d >= ell(m-2)", "121/128"):
        if pin not in g1:
            raise AssertionError(("missing G1 consumption pin", pin))

    print("PETAL_K4_PRIMITIVE_BOUND_PASS b4=1 open_petals=G1")


if __name__ == "__main__":
    main()
