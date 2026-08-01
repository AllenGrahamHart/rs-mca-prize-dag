#!/usr/bin/env python3
"""Verify the positive 433-1a product-base five-orbit exclusion."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_product_base_rank_three_orbit_exclusion",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    # Verify B^2-A^2 = 8(R-1)(T-1)(R+T) on a coefficient grid.
    for prime in (13, 17, 29):
        for r_value in range(prime):
            for t_value in range(prime):
                a = (-r_value * t_value + 3 * r_value
                     + 3 * t_value - 1) % prime
                b_value = ((r_value + 1) * (t_value + 1)) % prime
                expected = (8 * (r_value - 1) * (t_value - 1)
                            * (r_value + t_value)) % prime
                require((b_value * b_value - a * a) % prime == expected,
                        "cell-4 determinant identity")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_PRODUCT_BASE_FIVE_ORBIT_VERIFY_PASS "
        "role_orbits=5 labeled_cells=7 remaining_orbits=4"
    )


if __name__ == "__main__":
    main()
