#!/usr/bin/env python3
"""Verify the cell-3 DE-missing pairing-3 48-case exclusion."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_de_pairing3_"
    "nested_quadratic_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_de_pairing3_"
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
    SCRIPT: "9bb70b2cfb1a642dddedaf988d21fdba373e91339eac942f0ec3a1ab8bfc8203",
    RESULT: "b3614f7ecee9b6f0f758aa31e3a89a39c42d792f65fca8c9eb59f8c4c0f56059",
}
PRIME = 2130706433
SIGNS = set(itertools.product((-1, 1), repeat=2))
LANES = set(itertools.product((-1, 1), repeat=2))
EXPECTED_MATCHING = ((0, 2), (1, 3), (4, 5))


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
        "rate-half-kb-positive-433-1b-cell3-de-pairing3-"
        "nested-quadratic-census-v1",
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

    expected = {
        (epsilon, sigma, xi, 3)
        for epsilon in SIGNS for sigma in LANES for xi in (0, 2)
    }
    rows = {}
    candidate_counts = []
    source_counts = []
    uv_counts = []
    boundary_records = []
    for row in payload["rows"]:
        key = (
            tuple(row["epsilon"]), tuple(row["sigma"]),
            row["xi_index"], row["pairing_index"],
        )
        require(key in expected and key not in rows, "computed Cartesian row")
        rows[key] = row
        require(
            row["status"] == "COMPLETE" and
            row["basis"] == ["1", "t", "t^2", "b", "b*t", "b*t^2"] and
            (row["base_degree"], row["b_degree"],
             row["algebra_dimension"]) == (3, 2, 6),
            "complete six-basis row",
        )
        require(
            (row["p_u_degree"], row["p_v_degree"],
             row["nested_quartic_degree"], row["remainder_degree"]) ==
            (2, 2, 4, 1),
            "nested quadratic degrees",
        )
        require(row["tower_norm_match"] and
                row["field_root_gcd_degree"] == len(row["field_roots"]),
                "norm and root ledger")
        require(len(row["exceptional_root_rows"]) == 12,
                "six numerator/denominator guard rows")

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
            lift["colored_solution_count"] == 0 and
            lift["colored_solutions"] == [],
            "complete exclusion ledger",
        )
        require(
            lift["uv_candidate_count"] == len(lift["uv_candidates"]) and
            lift["boundary_solution_count"] ==
            len(lift["boundary_solutions"]),
            "finite candidate counts",
        )
        for boundary in lift["boundary_solutions"]:
            require(
                boundary["f"] == 0 and
                boundary["status"] == "TARGET_BOUNDARY" and
                boundary["failed_guards"] == ["nonzero_5"],
                "f=0 target boundary",
            )
        candidate_counts.append(lift["candidate_r_count"])
        source_counts.append(lift["source_point_count"])
        uv_counts.append(lift["uv_candidate_count"])
        boundary_records.extend(lift["boundary_solutions"])

    require(set(rows) == expected and len(rows) == 32, "32 computed rows")
    require(
        candidate_counts.count(10) == 8 and
        candidate_counts.count(11) == 16 and
        candidate_counts.count(12) == 8,
        "candidate-root census",
    )
    require(source_counts.count(14) == 24 and source_counts.count(18) == 8,
            "source-point census")
    require(uv_counts.count(0) == 8 and uv_counts.count(2) == 24,
            "uv-candidate census")
    require(len(boundary_records) == 32, "32 f=0 boundary records")
    require(residual_signature(0) == residual_signature(1),
            "positive parallel-copy transport")
    return 32, 16


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
        "cell=3 pairing=3 DE_copies=3 raw_cases=48 "
        "computed=32 transported=16 witnesses=0"
    )


if __name__ == "__main__":
    main()
