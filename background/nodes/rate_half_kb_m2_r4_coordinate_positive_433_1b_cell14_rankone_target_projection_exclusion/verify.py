#!/usr/bin/env python3
"""Verify the positive 433-1b cell-14 rank-one exclusion."""

import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "rate_half_kb_positive_433_1b_cell14_target_projection_modal.py":
        "86fb95403d6faead0d7feac65145c0bf17712c25a6e6ec51b70090469dfeab3e",
    "rate_half_kb_positive_433_1b_cell14_rankone_simple_full_result.json":
        "5ac03e6a9725929490ec98ee7be383f0fe914aaa117f3b7c276b4091d33354df",
    "rate_half_kb_positive_433_1b_cell14_rankone_df_chain_full_result.json":
        "d23ec272428bf8d170a4529f345d25eb5b6047b85cae31f31f36127c04cea920",
    "rate_half_kb_positive_433_1b_cell14_rankone_ef_chain_full_result.json":
        "22c1c10a136d34a11202f57d705fa047a54335ac2223e18844b133cf983968cc",
    "rate_half_kb_positive_433_1b_cell14_rankone_bf_targetfree_full_result.json":
        "e231d8722e96525f4b0ad0e57ea4cd0bf15ae41844c442ab4b8d33fa229cd8e0",
    "rate_half_kb_positive_433_1b_cell14_rankone_cf_targetfree_full_result.json":
        "2f69423df5c29d5153d6445f4d9b980ec8a2ea6b2c3e0fb9df747a1016a3cb62",
    "rate_half_kb_positive_433_1b_cell14_missing_ratio_boundary_modal.py":
        "7bc3368a96c2ffd57c9966fd8d03557ee4de29939d16288e32bb51655cc09ea4",
    "rate_half_kb_positive_433_1b_cell14_missing_ratio_boundary_result.json":
        "96ae7f85a9eec06f1704ccc3238beb5e30fdde67f21ce2b367dd0195b545dfa8",
    "rate_half_kb_positive_433_1b_cell14_rankone_census.py":
        "fdcf8b2e92a862dee33b140404bce914798a12c7de11d876bdee31f3f6400fb7",
    "rate_half_kb_positive_433_1b_cell14_rankone_census_result.json":
        "7fa4f47781bc5226ac665fe122393ebac11d124d220888d0ada272b4a0a5a77f",
    "rate_half_kb_positive_433_1b_cell14_rankone_root_replay_modal.py":
        "09c87b00416aa5afee92fc5ae95126d6933a30464e7bfc03ae5fe14de1f54364",
    "rate_half_kb_positive_433_1b_cell14_rankone_root_replay_result.json":
        "231a20d50dc5b9def119ce16c403ed2d69750b7096036ac915203c550f480f27",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell14_quadratic_curve_structure",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    result = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024*1024), b""):
            result.update(block)
    return result.hexdigest()


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell14-rankone-census-v1", "schema")
    require(payload["field"] == 2130706433, "field")
    require(payload["raw_cell_case_count"] == 1680 and
            payload["prior_linear_pair_excluded_count"] == 144 and
            payload["rankone_excluded_count"] == 960 and
            payload["combined_excluded_count"] == 1104 and
            payload["retained_case_count"] == 576, "scope census")
    require(payload["projection_script_sha256"] == FILES[
        "rate_half_kb_positive_433_1b_cell14_target_projection_modal.py"],
        "projection source")
    require(payload["boundary_script_sha256"] == FILES[
        "rate_half_kb_positive_433_1b_cell14_missing_ratio_boundary_modal.py"],
        "boundary source")
    expected = {
        "simple": (32, "rankone_resultant", 544, 192, 8),
        "df_chain": (224, "rankone_chain", 3648, 1088, 64),
        "ef_chain": (224, "rankone_chain", 3648, 1088, 64),
        "bf_targetfree": (240, "rankone_targetfree", 2400, 240, 4),
        "cf_targetfree": (240, "rankone_targetfree", 2640, 240, 4),
    }
    require(len(payload["shards"]) == 5, "shard count")
    for shard in payload["shards"]:
        require(shard["name"] in expected, "shard name")
        count, branch, roots, checked, eliminants = expected[shard["name"]]
        require((shard["case_count"], shard["unit_count"], shard["branch"],
                 shard["total_field_roots"], shard["checked_field_roots"],
                 shard["distinct_eliminant_count"]) ==
                (count, count, branch, roots, checked, eliminants),
                f"shard census: {shard['name']}")
        require(shard["file_sha256"] == FILES[shard["file"]],
                f"shard custody: {shard['name']}")
    boundary = payload["missing_ratio_boundary"]
    require(boundary["case_count"] == boundary["unit_count"] == 4 and
            boundary["field_root_count"] == 24 and
            boundary["curve_leading_field_root_count"] == 8, "boundary census")
    require(boundary["file_sha256"] == FILES[boundary["file"]],
            "boundary custody")
    replay = payload["independent_root_replay"]
    require(replay["case_count"] == replay["pass_count"] == 960 and
            replay["field_root_count"] == 12880, "root replay census")
    require(replay["source_script_sha256"] == FILES[
        "rate_half_kb_positive_433_1b_cell14_rankone_root_replay_modal.py"],
        "root replay source")
    require(replay["file_sha256"] == FILES[replay["file"]],
            "root replay custody")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED", "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent: {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")


def main():
    for name, expected in FILES.items():
        require(digest(EXPERIMENTS / name) == expected, f"custody: {name}")
    payload = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_rankone_census_result.json").read_text())
    verify_payload(payload)
    verify_dag()
    print("cell14 rank-one target projection: cases=960 retained=576")


if __name__ == "__main__":
    main()
