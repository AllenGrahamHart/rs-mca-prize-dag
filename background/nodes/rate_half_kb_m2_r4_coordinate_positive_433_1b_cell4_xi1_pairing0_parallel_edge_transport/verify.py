#!/usr/bin/env python3
"""Verify the cell-4 parallel-positive-DE transport."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell4_xi0_pairing0_four_basis_exclusion"
)
ATLAS_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas"
)
ATLAS = ROOT / f"background/nodes/{ATLAS_ID}/statement.md"
PARENT_RESULT = ROOT / f"background/nodes/{PARENT}/result.md"
PINNED = {
    ATLAS: "62ea6520db4f1a0144e343ff80efe1adf85121738b163ac20a2be805a87fe204",
    PARENT_RESULT: "cef9a90368334035afc3296c24aebaf60177d143e838ac28780af3ee9bb1bd58",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pairing_zero(values):
    return tuple((values[left], values[right])
                 for left, right in ((0, 1), (2, 3), (4, 5)))


def system_signature(xi):
    products = ("de", "de", "-de", "df", "sigma_o*ef",
                "bf", "sigma_c*cf")
    sums = ("(d+e)^2", "(d+e)^2", "(d-e)^2", "(d+f)^2",
            "(e+sigma_o*f)^2", "(b+f)^2", "(c+sigma_c*f)^2")
    residual_products = products[:xi] + products[xi + 1:]
    residual_sums = sums[:xi] + sums[xi + 1:]
    return {
        "missing_product": products[xi],
        "missing_sum": sums[xi],
        "paired_products": pairing_zero(residual_products),
        "paired_sums": pairing_zero(residual_sums),
        "target_representatives": ("1", "b", "c", "d", "e", "f"),
        "source_cell": 4,
    }


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    for parent in (PARENT, ATLAS_ID):
        require(parent in nodes and nodes[parent]["status"] == "PROVED",
                f"proved parent {parent}")
    edges = {(row["from"], row["to"], row["kind"])
             for row in dag["edges"]}
    for parent in (PARENT, ATLAS_ID):
        require((parent, NODE_ID, "req") in edges,
                f"parent edge {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    left = system_signature(0)
    right = system_signature(1)
    require(left == right, "parallel-edge systems differ")
    require(left["paired_products"] == (
        ("de", "-de"), ("df", "sigma_o*ef"), ("bf", "sigma_c*cf")
    ), "canonical residual product matching")
    require(left["paired_sums"] == (
        ("(d+e)^2", "(d-e)^2"),
        ("(d+f)^2", "(e+sigma_o*f)^2"),
        ("(b+f)^2", "(c+sigma_c*f)^2"),
    ), "canonical residual squared-sum matching")
    require(left["missing_sum"] == "(d+e)^2",
            "missing squared-sum row")
    verify_dag()
    print("cell=4 transport=xi0_to_xi1 pairing=0 raw_cases=16")


if __name__ == "__main__":
    main()
