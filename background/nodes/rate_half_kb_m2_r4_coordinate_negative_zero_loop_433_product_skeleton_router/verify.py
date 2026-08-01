#!/usr/bin/env python3
"""Verify the zero-loop 433 Z2/Z3 product exclusions."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
    "product_skeleton_router"
)
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_zero_loop_433_cell2_product_probe.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("router", SCRIPT)
    router = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(router)
    expected = {
        "Z2": (1680, 312, 736, 512, 0, 16),
        "Z3": (3360, 432, 864, 0, 0, 0),
    }
    for packet in range(4):
        for name, counts in expected.items():
            checked, soluble, isolated, samples, guarded, families = (
                router.group_probe(packet, name, print_limit=0, verbose=False)
            )
            observed = (
                checked, soluble, isolated, samples,
                len(guarded), len(families),
            )
            require(observed == counts, f"{packet}/{name} census {observed}")
            require(
                all(family[-1].startswith(("target-square:", "product:"))
                    for family in families),
                f"{packet}/{name} family collision",
            )

    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("`Z2` and `Z3` are empty" in statement, "claim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
        "aligned_doubled_pair_finite_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_"
        "complete_edge_skeleton_classifier",
        "rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_PRODUCT_ROUTER_VERIFY_PASS "
        "packets=4 Z2=empty Z3=empty family_collisions=64"
    )


if __name__ == "__main__":
    main()
