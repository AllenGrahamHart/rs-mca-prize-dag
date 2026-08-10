#!/usr/bin/env python3
"""Verify the complete 433-1b/O0b common compiler atlas."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_433_1b_o0b_common_compiler_assembly.py"
)
SCRIPT_HASH = "c0bd133188e0e734595210d7f9a305a18d69706d43c038f6af7eccbe3912d914"
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_vieta_minor_compiler",
}
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
EXPECTED = {
    "lanes": 10,
    "split_lanes": 6,
    "repeat_lanes": 4,
    "source_rows_per_lane": 60,
    "formal_common_systems": 600,
    "distinct_split_algebra_rows": 60,
    "distinct_repeat_algebra_rows": 120,
    "distinct_algebra_rows": 180,
    "formal_minors_per_mode": 3600,
    "compiled_minors_per_mode": 1080,
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_assembly():
    require(hashlib.sha256(SCRIPT.read_bytes()).hexdigest() == SCRIPT_HASH,
            "script custody")
    spec = importlib.util.spec_from_file_location("o0b_assembly", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate(rows, counts):
    require(counts == EXPECTED, "exact census")
    require(len(rows) == 10 and len({tuple(row["key"]) for row in rows}) == 10,
            "lane coverage")
    require(sum(row["compiler"] == "split" for row in rows) == 6,
            "split coverage")
    require(sum(row["compiler"] == "repeat" for row in rows) == 4,
            "repeat coverage")
    require({row["bc_sign"] for row in rows if row["compiler"] == "repeat"}
            == {-1, 1}, "repeat signs")
    require(all(row["source_rows"] == 60 for row in rows), "source rows")


def main():
    assembly = load_assembly()
    rows, counts = assembly.assemble()
    validate(rows, counts)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED", f"parent {parent}")
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer evidence edge")
    statement = (NODE / "statement.md").read_text()
    require("600 formal lane/source systems" in statement and
            "neither solves the minor systems" in statement, "scope text")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_COMMON_ATLAS_VERIFY_PASS "
        "lanes=10 split=6 repeat=4 formal=600 distinct=180 minors=3600"
    )


if __name__ == "__main__":
    main()
