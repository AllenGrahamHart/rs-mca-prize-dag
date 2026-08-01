#!/usr/bin/env python3
"""Verify the exact refutation of the positive three-loop neighbor norm weld."""

import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_positive_three_loop_neighbor_norm_compiler"
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_positive_three_loop_neighbor_norm.py"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    specification = importlib.util.spec_from_file_location("neighbor_norm", SCRIPT)
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    result = module.verify()
    require(result["numerator_u_degree"] == 2, "numerator degree")
    require(result["denominator_u_degree"] == 2, "denominator degree")
    require(result["placements"] == 4 and result["lanes"] == 8, "coverage")
    require(result["resultant_identities_valid"], "true identity")
    require(result["graph_tables_valid"], "true graph tables")
    require(not result["resultant_graph_weld_valid"], "refuted weld")
    require(result["counterexample"] == {
        "prime": 13,
        "placement": "433_root_low",
        "kernel": (4, 7, 6, 1),
        "observed_norm_at_one": 8,
        "claimed_neighbor_product": 6,
    }, "counterexample replay")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "REFUTED", "DAG status")
    statement = (NODE / "statement.md").read_text()
    require("8!=6" in statement, "falsifier")
    require("must not be used" in statement, "scope fence")
    print(
        "RATE_HALF_KB_POSITIVE_THREE_LOOP_NEIGHBOR_NORM_REFUTATION_PASS "
        "prime=13 placement=433_root_low observed=8 claimed=6"
    )


if __name__ == "__main__":
    main()
