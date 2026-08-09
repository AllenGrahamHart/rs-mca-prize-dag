#!/usr/bin/env python3
"""Verify complete all-role exclusion at cell-9 section-base points."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell9_kernel_null_residual_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell9_kernel_null_residual_result.json"
PINNED = {
    SCRIPT: "812198b5149cb90649464144e7b7b8f6e2f9cc3ba5e0fb5b91f7bfaf14b58a0d",
    RESULT: "4197b0413cfae562589351850cf937c5a0aaca9dc021e30d8ff360bebdb64993",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_kernel_section_base_locus_regularization",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"hash drift: {path.name}")
    payload = json.loads(RESULT.read_text())
    expected = {
        (source, point, lane)
        for source in itertools.product((-1, 1), repeat=2)
        for point in range(2)
        for lane in itertools.product((-1, 1), repeat=2)
    }
    seen = set()
    total = 0
    wanted_labels = set(itertools.product(range(7), range(15)))
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["point_index"], tuple(row["sigma"]))
        require(key in expected and key not in seen, "lane coverage")
        seen.add(key)
        labels = {(item["xi_index"], item["pairing_index"])
                  for item in row["rows"]}
        require(row["status"] == "COMPLETE" and row["systems"] == 105
                and row["completed_systems"] == 105
                and row["unit_systems"] == 105
                and not row["nonunit_systems"] and labels == wanted_labels
                and len(row["rows"]) == 105 and row["program_sha256"]
                and not row["stderr"]
                and all(item["unit"] and item["dimension"] == -1
                        and item["basis_size"] == 1
                        and item["nonunit_basis"] is None
                        for item in row["rows"]), "unit ledger")
        total += len(row["rows"])
    require(seen == expected and total == 3360, "Cartesian total")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE.name in nodes and nodes[NODE.name]["status"] == "PROVED",
            "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(all((parent, NODE.name, "req") in edges for parent in PARENTS),
            "DAG parents")
    print("cell=9 base_locus_systems=3360 unit=3360 roles=7")


if __name__ == "__main__":
    main()
