#!/usr/bin/env python3
"""Verify the repeated-BC cell-3 BC+ torus locus."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_monomial_probe_modal.py",
        "7b5650b65801e4a870da9d5ba92f9ff030d3e72bab94aa97cba472eb18b80926",
    ),
    "result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_monomial_probe_result.json",
        "9ad509b330416fc095fcbf6ff2ac75ae82123cc824b4f819e3c6aac0c78279fc",
    ),
}
SOURCE_SHA256 = "713122da1efabb83a8c10598591240e6e7abb1069c1d105f6bea973de6a9d554"
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cells3_6_compact_locus"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
CORES = {
    (-1, -1): "r**2*u + 16711678*r*u**2 + 16711678*r - 16711679*u",
    (-1, 1): "r**2*u + 16711680*r*u**2 + 16711680*r + 16711679*u",
    (1, -1): "r**2*u - 16711678*r*u**2 - 16711678*r - 16711679*u",
    (1, 1): "r**2*u - 16711680*r*u**2 - 16711680*r + 16711679*u",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check_summary(item, label):
    require(item["terms"] > 0 and item["degree"] >= 0, f"{label} shape")
    digest = hashlib.sha256(item["expression"].encode()).hexdigest()
    require(digest == item["sha256"], f"{label} digest")


def validate(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-torus-v1", "schema")
    require(payload["source_sha256"] == SOURCE_SHA256, "source custody")
    expected = set(itertools.product((-1, 1), repeat=2))
    actual = set()
    for row in payload["rows"]:
        epsilon = tuple(row["epsilon"])
        require(epsilon in expected and epsilon not in actual, "case")
        actual.add(epsilon)
        require(row["status"] == "COMPLETE", "completion")
        require(row["substitution"] == {
            "t": f"{epsilon[0] * epsilon[1]}*r^2",
            "b": "-u^-3",
            "c": "u",
        }, "substitution")
        require(row["t_relation_remainder"] == "0" and
                row["monomial_relation_remainder"] == "0", "forced relations")
        require(row["gcd_identity"] is True, "gcd identity")
        require(row["torus_core"]["expression"] == CORES[epsilon], "torus core")
        require(row["torus_core"]["degree"] == 3 and
                row["torus_core"]["degree_r"] == 2 and
                row["torus_core"]["degree_u"] == 2 and
                row["torus_core"]["terms"] == 4, "torus core shape")
        require(row["original_dimension"] == 2, "adjoined-u dimension")
        require(row["parameter_unit"] is False and
                row["parameter_dimension"] == 1, "parameter locus")
        require(row["saturated_unit"] is True and
                row["saturated_dimension"] == -1 and
                row["saturated_basis_size"] == 1 and
                row["saturated_basis"] == "1", "residual unit ideal")
        for index, item in enumerate(row["numerators"]):
            check_summary(item, f"numerator {epsilon} {index}")
        check_summary(row["removed_gcd"], f"gcd {epsilon}")
        check_summary(row["torus_core"], f"core {epsilon}")
        check_summary(row["transformed_guard"], f"guard {epsilon}")
        for index, item in enumerate(row["primitive_equations"]):
            check_summary(item, f"primitive {epsilon} {index}")
        for index, item in enumerate(row["groebner_basis"]):
            check_summary(item, f"basis {epsilon} {index}")
    require(actual == expected and len(payload["rows"]) == 4, "case coverage")


def main():
    for filename, expected in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == expected, f"file custody {filename}")
    payload = json.loads((EXPERIMENTS / FILES["result"][0]).read_text())
    validate(payload)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req")) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED" and
            (PARENT, NODE_ID, "req") in edges, "parent")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL3_BCPLUS_TORUS_VERIFY_PASS rows=4 exact=4 residual_unit=4")


if __name__ == "__main__":
    main()
