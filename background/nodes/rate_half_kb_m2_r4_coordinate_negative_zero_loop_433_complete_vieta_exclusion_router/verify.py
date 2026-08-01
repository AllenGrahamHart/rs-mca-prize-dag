#!/usr/bin/env python3
"""Exhaustively verify every complete-Vieta lane deletion."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
    "complete_vieta_exclusion_router"
)
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_zero_loop_433_complete_vieta_probe.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("router", SCRIPT)
    router = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(router)
    router.field_audit()

    comparisons = 0
    family_systems = 0
    for packet in range(4):
        for name, expected in (("Z0", 48), ("Z1", 128), ("Z4", 64)):
            result = router.probe(2, packet, name)
            require(len(result["assignments"]) == expected,
                    f"old {packet}/{name} assignment census")
            require(not result["unresolved_families"],
                    f"old {packet}/{name} family")
            require(not result["survivors"], f"old {packet}/{name} survivor")
            comparisons += len(result["records"]) * len(result["assignments"])
            family_systems += len(result["families"])

    expected_z4 = (80, 80, 80, 80, 48, 48, 48, 48)
    for packet, expected in enumerate(expected_z4):
        result = router.probe(12, packet, "Z4")
        require(len(result["assignments"]) == expected,
                f"12/{packet}/Z4 assignment census")
        require(len(result["families"]) == 16,
                f"12/{packet}/Z4 family census")
        require(not result["unresolved_families"], f"12/{packet}/Z4 family")
        require(not result["survivors"], f"12/{packet}/Z4 survivor")
        comparisons += len(result["records"]) * len(result["assignments"])
        family_systems += len(result["families"])

    for cell in (13, 14):
        for packet in range(4):
            for name, expected, expected_families in (
                ("Z1", 96, 0), ("Z3", 128, 32),
            ):
                result = router.probe(cell, packet, name)
                require(len(result["assignments"]) == expected,
                        f"{cell}/{packet}/{name} assignment census")
                require(len(result["families"]) == expected_families,
                        f"{cell}/{packet}/{name} family census")
                require(not result["unresolved_families"],
                        f"{cell}/{packet}/{name} family")
                require(not result["survivors"],
                        f"{cell}/{packet}/{name} survivor")
                comparisons += len(result["records"]) * len(result["assignments"])
                family_systems += len(result["families"])

    require(comparisons == 6528, "comparison total")
    require(family_systems == 384, "family-system total")

    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "statement status")
    require("cell 12: Z2,Z3" in statement, "residual frontier")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
        "product_skeleton_router",
        "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
        "bc_singleton_product_skeleton_router",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_COMPLETE_VIETA_VERIFY_PASS "
        "comparisons=6528 collision_families=384 "
        "deleted=orbit2/5/6/9,12/Z4,13/Z1/Z3,14/Z1/Z3"
    )


if __name__ == "__main__":
    main()
