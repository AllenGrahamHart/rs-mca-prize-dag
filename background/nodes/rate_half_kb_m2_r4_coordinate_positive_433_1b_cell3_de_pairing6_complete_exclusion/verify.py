#!/usr/bin/env python3
"""Verify the cell-3 DE-missing pairing-6 48-case exclusion."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_de_pairing6_"
    "nested_quadratic_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_de_pairing6_"
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
    SCRIPT: "d5d83fedec998524dd440a6751073ee2aa04ed44742b1b23d05dd8003acbd7c2",
    RESULT: "1c83f249b067e0cb0d71a4d5dc90017a99e9797657038b1b48b2e14aefcc6735",
}
SIGNS = set(itertools.product((-1, 1), repeat=2))
LANES = set(itertools.product((-1, 1), repeat=2))
EXPECTED_MATCHING = ((0, 3), (1, 2), (4, 5))
PROFILES = {
    (0, -1): (7, 2, 11, 14, 0, 0),
    (0, 1): (8, 3, 12, 14, 2, 0),
    (2, -1): (9, 2, 11, 18, 2, 2),
    (2, 1): (8, 1, 10, 14, 2, 2),
}


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


def finite_f_rows(lift):
    for r_row in lift["rows"]:
        for t_row in r_row.get("t_rows", []):
            for b_row in t_row.get("b_rows", []):
                for uv_row in b_row.get("uv_rows", []):
                    yield from uv_row.get("f_rows", [])


def verify_payload(payload):
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-cell3-de-pairing6-"
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

    expected = set(itertools.product(SIGNS, LANES, (0, 2)))
    rows = {}
    boundaries = []
    colored_nonzero_rows = []
    norm_classes = {}
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), tuple(row["sigma"]), row["xi_index"])
        require(key in expected and key not in rows, "Cartesian census row")
        rows[key] = row
        sigma_c, sigma_o = row["sigma"]
        require(row["pairing_index"] == 6, "matching index")
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
        norm_key = (tuple(row["epsilon"]), row["xi_index"], sigma_o)
        norm_text = json.dumps(row["target_free_norm"], sort_keys=True)
        require(norm_key not in norm_classes or
                norm_classes[norm_key] == norm_text,
                "sigma-c-independent norm")
        norm_classes[norm_key] = norm_text

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
            lift["case_excluded"] and lift["colored_solution_count"] == 0 and
            lift["colored_solutions"] == [] and
            lift["witness_count"] == 0 and lift["witnesses"] == [] and
            lift["unresolved_count"] == 0 and lift["unresolved"] == [],
            "complete exclusion ledger",
        )
        require(lift["uv_candidate_count"] == len(lift["uv_candidates"]) and
                lift["boundary_solution_count"] ==
                len(lift["boundary_solutions"]),
                "finite candidate counts")
        observed = (
            len(row["field_roots"]), lift["live_norm_root_count"],
            lift["candidate_r_count"], lift["source_point_count"],
            lift["uv_candidate_count"], lift["boundary_solution_count"],
        )
        require(observed == PROFILES[(row["xi_index"], sigma_o)],
                "profile census")

        f_rows = list(finite_f_rows(lift))
        current_boundaries = [
            item for item in f_rows if item["status"] == "TARGET_BOUNDARY"
        ]
        current_colored_nonzero = [
            item for item in f_rows
            if item["status"] == "COLORED_PAIR_NONZERO"
        ]
        require(len(current_boundaries) == lift["boundary_solution_count"] and
                all(
            item["f"] == 0 and item["status"] == "TARGET_BOUNDARY" and
            item["failed_guards"] == ["nonzero_5"]
            for item in current_boundaries
        ), "finite f ledger")
        expected_colored_nonzero = 4 if (
            row["xi_index"], sigma_o
        ) == (0, 1) else 0
        require(len(current_colored_nonzero) == expected_colored_nonzero and
                all(item["f"] != 0 and item["colored_cut"] != 0
                    for item in current_colored_nonzero) and
                len(f_rows) ==
                len(current_boundaries)+len(current_colored_nonzero),
                "nonzero colored-pair ledger")
        colored_nonzero_rows.extend(current_colored_nonzero)
        for boundary in lift["boundary_solutions"]:
            require(boundary["f"] == 0 and
                    boundary["failed_guards"] == ["nonzero_5"],
                    "f=0 target boundary")
        boundaries.extend(lift["boundary_solutions"])

    require(set(rows) == expected and len(rows) == 32,
            "32-row Cartesian census")
    require(len(norm_classes) == 16, "16 sigma-c-independent norm classes")
    require(sum(row["direct_lift"]["candidate_r_count"]
                for row in rows.values()) == 352,
            "candidate-r aggregate")
    require(sum(row["direct_lift"]["source_point_count"]
                for row in rows.values()) == 480,
            "source-point aggregate")
    require(sum(row["direct_lift"]["uv_candidate_count"]
                for row in rows.values()) == 48,
            "uv aggregate")
    require(len(colored_nonzero_rows) == 32,
            "32 nonzero colored-pair evaluations")
    require(len(boundaries) == 32, "32 source-level f=0 boundaries")
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
        "cell=3 pairing=6 DE_copies=3 raw_cases=48 "
        "computed_rows=32 uv_candidates=48 witnesses=0"
    )


if __name__ == "__main__":
    main()
