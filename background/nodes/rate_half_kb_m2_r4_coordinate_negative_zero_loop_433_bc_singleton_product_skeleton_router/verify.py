#!/usr/bin/env python3
"""Verify all BC-singleton product-skeleton exclusions."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
    "bc_singleton_product_skeleton_router"
)
SCRIPT = ROOT / (
    "experiments/prize_resolution/rate_half_kb_zero_loop_433_bc_product_probe.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("router", SCRIPT)
    router = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(router)
    configurations = (
        (12, 8, "Z0", (420, 144, 192, 768, 0, 16)),
        (12, 8, "Z1", (3360, 512, 896, 0, 0, 0)),
        (13, 4, "Z0", (420, 50, 208, 0, 0, 0)),
        (13, 4, "Z4", (1680, 184, 640, 0, 0, 0)),
        (14, 4, "Z0", (420, 50, 208, 0, 0, 0)),
        (14, 4, "Z4", (1680, 184, 640, 0, 0, 0)),
    )
    checked_rows = 0
    for cell, packet_count, name, expected in configurations:
        for packet in range(packet_count):
            result = router.probe(cell, packet, name, verbose=False)
            observed = (
                result["checked"], result["soluble"], result["isolated"],
                result["family_samples"], len(result["guarded"]),
                len(result["families"]),
            )
            require(observed == expected, f"{cell}/{packet}/{name} {observed}")
            require(
                all(family[-1] != "unresolved" for family in result["families"]),
                f"{cell}/{packet}/{name} unresolved family",
            )
            checked_rows += 1

    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("cell 12: Z0 and Z1 are empty" in statement, "claim")
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
        "bc_singleton_finite_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
        "complete_edge_skeleton_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_BC_PRODUCT_ROUTER_VERIFY_PASS "
        f"exclusion_routes={checked_rows} product_rows=16 "
        "deleted=12:Z0,Z1;13:Z0,Z4;14:Z0,Z4"
    )


if __name__ == "__main__":
    main()
