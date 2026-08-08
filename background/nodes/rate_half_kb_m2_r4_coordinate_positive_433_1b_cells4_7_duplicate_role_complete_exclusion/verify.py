#!/usr/bin/env python3
"""Verify complete duplicate-role transport from cell 4 to cell 7."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
SCRIPT = ROOT / "experiments/prize_resolution/rate_half_kb_positive_433_1b_cells4_7_duplicate_role_transport.py"
SCRIPT_SHA256 = "c14bbe23f7a6580a38ae2bfdc3464e02de83b19524aa0ab381d023d51768b26a"
DEPENDENCIES = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_compiler():
    specification = importlib.util.spec_from_file_location("cells47_transport", SCRIPT)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def main():
    require(digest(SCRIPT) == SCRIPT_SHA256, "compiler custody")
    census = load_compiler().verify_transport()
    require(census == {
        "source_signs": 4,
        "target_lanes": 4,
        "missing_matching_cases": 105,
        "raw_cases": 1680,
    }, "complete transport census")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "proved node")
    for dependency in DEPENDENCIES:
        require(nodes[dependency]["status"] == "PROVED", f"proved {dependency}")
        require((dependency, NODE_ID, "req") in edges, f"required {dependency}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer evidence edge")

    rank_statement = (
        ROOT / "background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion/statement.md"
    ).read_text()
    require("rank-at-most-four branch" in rank_statement
            and "= 6720" in rank_statement,
            "global rank-drop exclusion")
    statement = (NODE / "statement.md").read_text()
    require("= 1680" in statement and "not a valid shortcut" in statement,
            "scope and symmetry discipline")
    print("cells=4,7 duplicate_role_transport=exact cell7_raw_cases=1680 complete=yes")


if __name__ == "__main__":
    main()
