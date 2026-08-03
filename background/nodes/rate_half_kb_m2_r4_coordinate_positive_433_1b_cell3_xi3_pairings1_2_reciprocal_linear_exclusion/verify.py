#!/usr/bin/env python3
"""Verify the cell-3 xi3/pairings1-2 reciprocal-linear exclusion."""

import collections
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_pairings1_2_"
    "reciprocal_linear_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_pairings1_2_"
    "reciprocal_linear_census_result.json"
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
    SCRIPT: "66480d33177930d0376ff10ed1ae971344a247de803a8e8aa015dc4c8d757f21",
    RESULT: "df010f16c1b70213b03527570e7b0a51d07f2604d519f62b290ce212a4349786",
}
SIGNS = set(itertools.product((-1, 1), repeat=2))
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def poly_add(left, right):
    output = dict(left)
    for monomial, coefficient in right.items():
        output[monomial] = output.get(monomial, 0) + coefficient
        if output[monomial] == 0:
            del output[monomial]
    return output


def poly_scale(value, scalar):
    return {
        monomial: scalar*coefficient
        for monomial, coefficient in value.items()
        if scalar*coefficient
    }


def poly_mul(left, right):
    output = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                a+b for a, b in zip(left_monomial, right_monomial)
            )
            output[monomial] = (
                output.get(monomial, 0)
                + left_coefficient*right_coefficient
            )
    return {key: value for key, value in output.items() if value}


def formal_identities():
    # Variables are A0,A1,A2,B0,B1,B2,q.
    variables = []
    for index in range(7):
        monomial = [0]*7
        monomial[index] = 1
        variables.append({tuple(monomial): 1})
    a_values = variables[:3]
    b_values = variables[3:6]
    q = variables[6]
    linear = [
        poly_add(b_values[index], poly_scale(poly_mul(q, a_values[index]), -1))
        for index in range(3)
    ]
    p0, p1, p2 = linear
    q0, q1, q2 = p0, poly_scale(p1, -1), p2
    first = poly_add(poly_mul(p2, q0), poly_scale(poly_mul(p0, q2), -1))
    second = poly_add(poly_mul(p2, q1), poly_scale(poly_mul(p1, q2), -1))
    third = poly_add(poly_mul(p1, q0), poly_scale(poly_mul(p0, q1), -1))
    paired = poly_add(
        poly_mul(first, first),
        poly_scale(poly_mul(second, third), -1),
    )
    expected = poly_scale(
        poly_mul(poly_mul(p0, poly_mul(p1, p1)), p2), 4
    )
    require(paired == expected, "formal paired(q,q) factorization")

    # Variables are p0,p1,p2,r0,r1.  This is r1^2 P(-r0/r1).
    variables = []
    for index in range(5):
        monomial = [0]*5
        monomial[index] = 1
        variables.append({tuple(monomial): 1})
    c0, c1, c2, r0, r1 = variables
    cleared = poly_add(
        poly_add(poly_mul(c0, poly_mul(r1, r1)),
                 poly_scale(poly_mul(c1, poly_mul(r0, r1)), -1)),
        poly_mul(c2, poly_mul(r0, r0)),
    )
    require(cleared == {
        (1, 0, 0, 0, 2): 1,
        (0, 1, 0, 1, 1): -1,
        (0, 0, 1, 2, 0): 1,
    }, "formal linear-remainder cut")


def lane_rows(lift):
    for r_row in lift["rows"]:
        for t_row in r_row.get("t_rows", []):
            for b_row in t_row.get("b_rows", []):
                for z_row in b_row.get("z_rows", []):
                    yield from z_row.get("lanes", [])


def verify_payload(payload):
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-cell3-xi3-pairings1-2-"
        "reciprocal-linear-source-census-v1",
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
        (epsilon, branch, 0, 1)
        for epsilon in SIGNS for branch in (0, 1, 2)
    } | {
        (epsilon, branch, sigma_c, 2)
        for epsilon in SIGNS for branch in (0, 1, 2)
        for sigma_c in (-1, 1)
    }
    rows = {}
    profiles = collections.Counter()
    all_lanes = []
    for row in payload["rows"]:
        key = (
            tuple(row["epsilon"]), row["branch_index"],
            row["sigma_c_anchor"], row["pairing_index"],
        )
        require(key in expected and key not in rows, "branch Cartesian row")
        rows[key] = row
        covered = (
            SIGNS if row["pairing_index"] == 1 else
            {(row["sigma_c_anchor"], sigma_o) for sigma_o in (-1, 1)}
        )
        require(
            row["xi_index"] == 3 and
            {tuple(lane) for lane in row["target_lanes_covered"]} == covered,
            "scope and lane cover",
        )
        require(
            row["status"] == "COMPLETE" and
            row["basis"] == ["1", "t", "t^2", "b", "b*t", "b*t^2"] and
            (row["base_degree"], row["b_degree"],
             row["algebra_dimension"]) == (3, 2, 6),
            "complete six-basis row",
        )
        require(
            (row["p_missing_degree"], row["p_next_degree"],
             row["remainder_degree"]) == (4, 2, 1) and
            row["tower_norm_match"] and
            row["field_root_gcd_degree"] == len(row["field_roots"]),
            "quartic reduction and norm ledger",
        )

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
            lift["case_excluded"] and
            lift["witness_count"] == 0 and lift["witnesses"] == [] and
            lift["boundary_solution_count"] == 0 and
            lift["boundary_solutions"] == [] and
            lift["unresolved_count"] == 0 and lift["unresolved"] == [] and
            lift["final_pair_solution_count"] == 0 and
            lift["final_pair_solutions"] == [],
            "complete exclusion ledger",
        )
        require(
            lift["z_candidate_count"] == len(lift["z_candidates"]),
            "finite candidate ledger",
        )
        for r_row in lift["rows"]:
            for t_row in r_row.get("t_rows", []):
                for b_row in t_row.get("b_rows", []):
                    require(
                        b_row.get("status") != "FREE_Q_BRANCH",
                        "no free q branch",
                    )
                    if "q" not in b_row:
                        continue
                    require(
                        (b_row["a_branch"]*b_row["q"]
                         - b_row["b_branch"]) % PRIME == 0,
                        "q branch replay",
                    )
                    m = b_row["source_missing"]
                    s = b_row["source_sum"]
                    for z_row in b_row.get("z_rows", []):
                        z = z_row["z"]
                        d, e, f = z_row["d"], z_row["e"], z_row["f"]
                        require(
                            z and d*z % PRIME == 1 and
                            d*e % PRIME == b_row["q"] and
                            d*f % PRIME == m and
                            ((d+f)*(d+f)-s) % PRIME == 0 and
                            (1+(2*m-s)*z*z+m*m*pow(z, 4, PRIME)) % PRIME == 0,
                            "reciprocal-linear replay",
                        )

        current_lanes = list(lane_rows(lift))
        require(all(
            tuple(item["sigma"]) in covered and
            item["status"] == "THIRD_PAIR_NONZERO" and
            item["final_pair_cut"] != 0
            for item in current_lanes
        ), "nonzero final-pair rows")
        all_lanes.extend(current_lanes)
        profiles[(
            row["pairing_index"], row["branch_index"],
            row["sigma_c_anchor"], len(row["field_roots"]),
            lift["live_norm_root_count"], lift["candidate_r_count"],
            lift["source_point_count"], lift["z_candidate_count"],
            len(current_lanes),
        )] += 1

    require(set(rows) == expected and len(rows) == 36, "36 branch rows")
    expected_profiles = collections.Counter({
        (1, 0, 0, 4, 0, 10, 12, 0, 0): 2,
        (1, 0, 0, 8, 4, 13, 18, 2, 8): 2,
        (1, 1, 0, 4, 0, 8, 6, 0, 0): 4,
        (1, 2, 0, 4, 0, 10, 12, 0, 0): 2,
        (1, 2, 0, 8, 4, 13, 18, 2, 8): 2,
        (2, 0, -1, 5, 1, 10, 10, 0, 0): 2,
        (2, 0, -1, 7, 3, 13, 22, 6, 12): 2,
        (2, 0, 1, 5, 1, 10, 10, 0, 0): 2,
        (2, 0, 1, 7, 3, 13, 22, 6, 12): 2,
        (2, 1, -1, 4, 0, 8, 6, 0, 0): 4,
        (2, 1, 1, 4, 0, 8, 6, 0, 0): 4,
        (2, 2, -1, 5, 1, 10, 10, 0, 0): 2,
        (2, 2, -1, 7, 3, 13, 22, 6, 12): 2,
        (2, 2, 1, 5, 1, 10, 10, 0, 0): 2,
        (2, 2, 1, 7, 3, 13, 22, 6, 12): 2,
    })
    require(profiles == expected_profiles, "exact branch profile multiset")
    require(len(all_lanes) == 128, "128 nonzero final-pair evaluations")
    require(sum(row["direct_lift"]["candidate_r_count"]
                for row in rows.values()) == 372, "candidate-r aggregate")
    require(sum(row["direct_lift"]["source_point_count"]
                for row in rows.values()) == 448, "source-point aggregate")
    require(sum(row["direct_lift"]["z_candidate_count"]
                for row in rows.values()) == 56, "finite-candidate aggregate")
    return 36, 32


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
    formal_identities()
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    internal_rows, raw_cases = verify_payload(json.loads(RESULT.read_text()))
    require((internal_rows, raw_cases) == (36, 32), "raw-case accounting")
    verify_dag()
    print(
        "cell=3 xi=3 pairings=1,2 raw_cases=32 branch_rows=36 "
        "lane_checks=128 witnesses=0"
    )


if __name__ == "__main__":
    main()
