#!/usr/bin/env python3
"""Verify complete exclusion of the cell-12 rational leading boundary."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PRIMARY_SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell12_boundary_outside_census_modal.py"
)
PRIMARY = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell12_boundary_outside_census_result.json"
)
AUDIT_SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell12_boundary_outside_census_audit_modal.py"
)
AUDIT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell12_boundary_outside_census_audit_result.json"
)
KERNEL = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"
)
BOUNDARY = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell12_tower_boundary_result.json"
)
PINNED = {
    PRIMARY_SCRIPT: "92e68da6966c2ea8c8f6837aa021f3e9f7e32b7d224f87f88757621bc7d9aa1b",
    PRIMARY: "48182653180d65eb46c1ed23e853a5fed38c8e01e76b55ab90d59406d0dab621",
    AUDIT_SCRIPT: "cab0c4819223730706aa8c1e333069abb603bbb260779c63d713f1da6ba3a6cb",
    AUDIT: "aaad99b314dd56f40373215343e00d6bebc80bb10f6b6316ba15d28e6c9d6a10",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_elliptic_four_basis_common_locus",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_global_common_kernel",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
)
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def expected_cases():
    return set(itertools.product(range(8), (-1, 1), (-1, 1)))


def verify_primary(payload, boundary_points):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell12-boundary-outside-census-v1"
            and payload["field"] == PRIME and payload["expected_cases"] == 32
            and payload["source_kernel_sha256"] == digest(KERNEL)
            and payload["source_boundary_sha256"] == digest(BOUNDARY),
            "primary custody")
    cases = set()
    labels = 0
    candidate_roots = 0
    for row in payload["rows"]:
        key = (row["point_index"], *row["sigma"])
        require(key not in cases, "duplicate primary case")
        cases.add(key)
        signs, point = boundary_points[row["point_index"]]
        require(row["epsilon"] == signs and row["point"] == point,
                "primary point custody")
        require(row["status"] == "COMPLETE" and row["witnesses"] == []
                and row["unresolved"] == [] and len(row["rows"]) == 105
                and row["square_root_count"] == 2
                and row["discriminant_root_count"] == 2,
                "primary complete case")
        label_keys = set()
        for item in row["rows"]:
            label = (item["xi_index"], item["pairing_index"])
            require(label not in label_keys, "duplicate primary label")
            label_keys.add(label)
            require(not item["unresolved"] and item["witnesses"] == 0 and
                    item["target_boundaries"] == 0 and
                    item["missing_lifts"] ==
                    (4 if item["xi_index"] < 5 else 0),
                    "primary label result")
            candidate_roots += item["free_root_candidates"]
        require(label_keys == set(itertools.product(range(7), range(15))),
                "primary 105-label cover")
        labels += len(label_keys)
    require(cases == expected_cases() and labels == 3360 and
            candidate_roots == 14976, "primary Cartesian totals")
    return {(
        row["point_index"], *row["sigma"]
    ): (row["missing"], row["source_sum"]) for row in payload["rows"]}


def verify_audit(payload, primary_values):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell12-boundary-outside-audit-v1"
            and payload["field"] == PRIME and payload["expected_cases"] == 32
            and payload["coverage_agrees"]
            and payload["source_kernel_sha256"] == digest(KERNEL)
            and payload["source_boundary_sha256"] == digest(BOUNDARY)
            and payload["source_primary_sha256"] == digest(PRIMARY),
            "audit custody")
    cases = set()
    labels = 0
    for row in payload["rows"]:
        key = (row["point_index"], *row["sigma"])
        require(key not in cases and key in primary_values,
                "duplicate or foreign audit case")
        cases.add(key)
        require(row["status"] == "COMPLETE" and row["free_branches"] == []
                and len(row["rows"]) == 105
                and (row["missing"], row["source_sum"]) == primary_values[key]
                and len(row["sum_roots"]) == 2
                and len(row["delta_roots"]) == 2,
                "audit complete case")
        label_keys = {
            (item["xi_index"], item["pairing_index"])
            for item in row["rows"]
        }
        require(label_keys == set(itertools.product(range(7), range(15)))
                and all(item["guarded_root_degree"] == 0
                        for item in row["rows"]),
                "audit zero-root label cover")
        labels += len(row["rows"])
    require(cases == expected_cases() and labels == 3360,
            "audit Cartesian totals")


def boundary_points():
    payload = json.loads(BOUNDARY.read_text())
    points = []
    for row in payload["rows"]:
        for point in row["rational_points"]:
            points.append((row["epsilon"], {
                key: point[key] for key in ("r", "t", "b", "c")
            }))
    require(len(points) == 8, "eight parent boundary points")
    return points


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges,
                f"missing parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG consumer")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    points = boundary_points()
    primary_values = verify_primary(json.loads(PRIMARY.read_text()), points)
    verify_audit(json.loads(AUDIT.read_text()), primary_values)
    verify_dag()
    print("cell=12 boundary_points=8 lanes=4 labels=3360 witnesses=0 roots=0")


if __name__ == "__main__":
    main()
