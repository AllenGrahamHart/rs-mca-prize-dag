#!/usr/bin/env python3
"""Verify the cell-3 DE-missing pairing-4 48-case exclusion."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_de_pairing4_"
    "nested_quadratic_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_de_pairing4_"
    "nested_quadratic_census_result.json"
)
QUOTIENT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_birational_profile_result.json"
)
KERNEL = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
)
PRODUCT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
)
PARENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell3_global_quadratic_quotient"
)
PINNED = {
    SCRIPT: "0651bae97ca44ed858058299f91d4d3945247b4720a11235333b8865ae7c94cd",
    RESULT: "ca2f5ad99622564786f2bb735aa7c340988b8a411f3a377955ae055cf2a2b42a",
}
SIGNS = set(itertools.product((-1, 1), repeat=2))
LANES = {(-1, -1), (-1, 1), (1, -1), (1, 1)}
EXPECTED_MATCHING = ((0, 2), (1, 4), (3, 5))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def residual_signature(xi):
    products = ("de", "de", "-de", "df", "sigma_o*ef",
                "bf", "sigma_c*cf")
    sums = ("(d+e)^2", "(d+e)^2", "(d-e)^2", "(d+f)^2",
            "(e+sigma_o*f)^2", "(b+f)^2", "(c+sigma_c*f)^2")
    product_residual = products[:xi] + products[xi+1:]
    sum_residual = sums[:xi] + sums[xi+1:]
    return (
        products[xi],
        sums[xi],
        tuple((product_residual[left], product_residual[right])
              for left, right in EXPECTED_MATCHING),
        tuple((sum_residual[left], sum_residual[right])
              for left, right in EXPECTED_MATCHING),
    )


def verify_payload(payload):
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-cell3-de-pairing4-"
        "nested-quadratic-source-census-v1",
        "schema",
    )
    require("no claim beyond the printed cases" in payload["scope"],
            "scope discipline")
    require(payload["source_quotient_sha256"] == digest(QUOTIENT),
            "quotient custody")
    require(payload["source_kernel_sha256"] == digest(KERNEL),
            "kernel custody")
    require(payload["source_product_sha256"] == digest(PRODUCT),
            "product custody")

    expected = {(epsilon, xi) for epsilon in SIGNS for xi in (0, 2)}
    rows = {}
    third_pair_rows = []
    boundary_records = []
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["xi_index"])
        require(key in expected and key not in rows, "source Cartesian row")
        rows[key] = row
        require(row["sigma"] == [-1, -1] and row["pairing_index"] == 4,
                "source-census anchor")
        require({tuple(lane) for lane in row["target_lanes_covered"]} ==
                LANES and len(row["target_lanes_covered"]) == 4,
                "four-lane coverage")
        require(
            row["status"] == "COMPLETE" and
            row["basis"] == ["1", "t", "t^2", "b", "b*t", "b*t^2"] and
            (row["base_degree"], row["b_degree"],
             row["algebra_dimension"]) == (3, 2, 6),
            "complete six-basis row",
        )
        require(
            (row["p_u_degree"], row["p_f_degree"],
             row["uf_eliminant_degree"], row["remainder_degree"]) ==
            (2, 2, 8, 1),
            "nested quadratic degrees",
        )
        require(row["tower_norm_match"] and
                row["field_root_gcd_degree"] == len(row["field_roots"]),
                "norm and root ledger")

        lift = row["direct_lift"]
        exceptional = {
            root
            for guard in row["exceptional_root_rows"]
            for root in (guard["roots"] or [])
        }
        candidates = exceptional | set(row["field_roots"])
        require(
            lift["exceptional_root_count"] == len(exceptional) and
            lift["candidate_r_count"] == len(candidates) and
            {item["r"] for item in lift["rows"]} == candidates,
            "complete exceptional-root lift",
        )
        require(
            lift["source_point_count"] == len(lift["source_points"]) and
            len({tuple(point) for point in lift["source_points"]}) ==
            len(lift["source_points"]),
            "source-point ledger",
        )
        require(
            lift["case_excluded"] and lift["witness_count"] == 0 and
            lift["witnesses"] == [] and lift["unresolved_count"] == 0 and
            lift["unresolved"] == [] and
            lift["third_pair_solution_count"] == 0 and
            lift["third_pair_solutions"] == [],
            "complete exclusion ledger",
        )
        require(lift["uf_candidate_count"] == len(lift["uf_candidates"]) and
                lift["boundary_solution_count"] ==
                len(lift["boundary_solutions"]),
                "finite candidate counts")

        for r_row in lift["rows"]:
            for t_row in r_row.get("t_rows", []):
                for b_row in t_row.get("b_rows", []):
                    for uf_row in b_row.get("uf_rows", []):
                        third_pair_rows.extend(uf_row.get("lanes", []))
        for boundary in lift["boundary_solutions"]:
            require(
                boundary["f"] == 0 and
                boundary["status"] == "TARGET_BOUNDARY" and
                boundary["failed_guards"] == ["nonzero_5"] and
                {tuple(lane) for lane in boundary["target_lanes_covered"]} ==
                LANES,
                "f=0 all-lane boundary",
            )
        boundary_records.extend(lift["boundary_solutions"])

        if row["xi_index"] == 0:
            require(
                (len(row["field_roots"]), lift["live_norm_root_count"],
                 lift["candidate_r_count"], lift["source_point_count"],
                 lift["uf_candidate_count"],
                 lift["boundary_solution_count"]) ==
                (9, 4, 14, 20, 0, 0),
                "positive-DE census",
            )
        else:
            require(
                (len(row["field_roots"]), lift["live_norm_root_count"],
                 lift["candidate_r_count"], lift["source_point_count"],
                 lift["uf_candidate_count"],
                 lift["boundary_solution_count"]) ==
                (11, 6, 15, 36, 6, 2),
                "negative-DE census",
            )

    require(set(rows) == expected and len(rows) == 8, "eight source rows")
    require(len(third_pair_rows) == 64 and all(
        tuple(item["sigma"]) in LANES and
        item["status"] == "THIRD_PAIR_NONZERO" and
        item["third_pair_cut"] != 0
        for item in third_pair_rows
    ), "64 nonzero third-pair lane evaluations")
    require(len(boundary_records) == 8, "eight source-level f=0 boundaries")
    require(residual_signature(0) == residual_signature(1),
            "positive parallel-copy transport")
    return 8*4, 16


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    require(PARENT in nodes and nodes[PARENT]["status"] == "PROVED",
            "proved parent")
    edges = {(row["from"], row["to"], row["kind"])
             for row in dag["edges"]}
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    computed, transported = verify_payload(json.loads(RESULT.read_text()))
    require(computed + transported == 48, "aggregate raw-case count")
    verify_dag()
    print(
        "cell=3 pairing=4 DE_copies=3 raw_cases=48 "
        "source_rows=8 lane_checks=64 witnesses=0"
    )


if __name__ == "__main__":
    main()
