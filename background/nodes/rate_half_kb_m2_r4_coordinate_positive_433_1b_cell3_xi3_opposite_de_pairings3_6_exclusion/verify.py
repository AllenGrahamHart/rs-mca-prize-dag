#!/usr/bin/env python3
"""Verify the cell-3 xi3 opposite-DE pairings 3 and 6 exclusion."""

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
    "rate_half_kb_positive_433_1b_cell3_xi3_opposite_de_orbit_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_opposite_de_"
    "pairing3_census_result.json"
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
    SCRIPT: "fce2ee32837f802fea4d28735a61c8cbccef1130681267cdf10968a94d159c33",
    RESULT: "e603cedb11de9ed4ed75c2cc2094a6dd60682841bc4e137bc108a87302de3f6f",
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
    return {key: scalar*coefficient for key, coefficient in value.items()
            if scalar*coefficient}


def poly_mul(left, right):
    output = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(a+b for a, b in zip(left_monomial, right_monomial))
            output[monomial] = (
                output.get(monomial, 0)+left_coefficient*right_coefficient
            )
    return {key: value for key, value in output.items() if value}


def product(*values):
    output = {(0,)*len(next(iter(values[0]))): 1}
    for value in values:
        output = poly_mul(output, value)
    return output


def formal_paired_identities():
    # Variables are A0,A1,A2,B0,B1,B2,x,y.
    variables = []
    for index in range(8):
        monomial = [0]*8
        monomial[index] = 1
        variables.append({tuple(monomial): 1})
    a_values, b_values = variables[:3], variables[3:6]
    x, y = variables[6:]

    def paired(left, right):
        p_values = [
            poly_add(b_values[index],
                     poly_scale(poly_mul(left, a_values[index]), -1))
            for index in range(3)
        ]
        q_values = [
            poly_add(b_values[0], poly_scale(poly_mul(right, a_values[0]), -1)),
            poly_add(poly_scale(b_values[1], -1),
                     poly_mul(right, a_values[1])),
            poly_add(b_values[2], poly_scale(poly_mul(right, a_values[2]), -1)),
        ]
        p0, p1, p2 = p_values
        q0, q1, q2 = q_values
        first = poly_add(poly_mul(p2, q0), poly_scale(poly_mul(p0, q2), -1))
        second = poly_add(poly_mul(p2, q1), poly_scale(poly_mul(p1, q2), -1))
        third = poly_add(poly_mul(p1, q0), poly_scale(poly_mul(p0, q1), -1))
        return poly_add(poly_mul(first, first),
                        poly_scale(poly_mul(second, third), -1))

    require(paired(x, y) == paired(y, x), "formal paired symmetry")
    opposite = paired(x, poly_scale(x, -1))
    c4 = product(a_values[0], a_values[1], a_values[1], a_values[2])
    c2 = poly_add(
        poly_add(
            poly_add(product(a_values[0], a_values[0], b_values[2], b_values[2]),
                     poly_scale(product(a_values[0], a_values[1],
                                        b_values[1], b_values[2]), -1)),
            poly_scale(product(a_values[0], a_values[2],
                               b_values[0], b_values[2]), -2)),
        poly_add(poly_scale(product(a_values[1], a_values[2],
                                    b_values[0], b_values[1]), -1),
                 product(a_values[2], a_values[2], b_values[0], b_values[0])),
    )
    c0 = product(b_values[0], b_values[1], b_values[1], b_values[2])
    expected = poly_scale(poly_add(
        poly_add(poly_mul(c4, poly_mul(poly_mul(x, x), poly_mul(x, x))),
                 poly_mul(c2, poly_mul(x, x))),
        c0,
    ), 4)
    require(opposite == expected, "formal opposite-DE even quartic")

    # (E+qO)(E-qO)=E^2-q^2 O^2.
    e, o, q = 3, 5, 7
    require((e+q*o)*(e-q*o) == e*e-q*q*o*o, "parity descent")


def canonical_matchings(items):
    if not items:
        return ((),)
    first = items[0]
    output = []
    for index in range(1, len(items)):
        partner = items[index]
        rest = items[1:index]+items[index+1:]
        for tail in canonical_matchings(rest):
            output.append(((first, partner),)+tail)
    return tuple(output)


def normalized_matching(value):
    return tuple(sorted(tuple(sorted(pair)) for pair in value))


def formal_transport():
    matchings = canonical_matchings(tuple(range(6)))
    require(len(matchings) == 15, "15 canonical matchings")
    require(matchings[3] == ((0, 2), (1, 3), (4, 5)), "pairing 3")
    require(matchings[6] == ((0, 3), (1, 2), (4, 5)), "pairing 6")
    swap = {0: 1, 1: 0, 2: 2, 3: 3, 4: 4, 5: 5}
    transported = tuple((swap[left], swap[right]) for left, right in matchings[3])
    require(normalized_matching(transported) == normalized_matching(matchings[6]),
            "positive-DE transport")


def lane_rows(lift):
    for r_row in lift["rows"]:
        for t_row in r_row.get("t_rows", []):
            for b_row in t_row.get("b_rows", []):
                for q_row in b_row.get("q_rows", []):
                    for root_row in q_row.get("root_rows", []):
                        yield from root_row.get("lanes", [])


def q_rows(lift):
    for r_row in lift["rows"]:
        for t_row in r_row.get("t_rows", []):
            for b_row in t_row.get("b_rows", []):
                yield from b_row.get("q_rows", [])


def verify_payload(payload):
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-cell3-xi3-opposite-de-"
        "pairing3-source-census-v1",
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

    expected = {(epsilon, sigma_o) for epsilon in SIGNS for sigma_o in (-1, 1)}
    rows = {}
    profiles = collections.Counter()
    all_lanes = []
    all_q_rows = []
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["sigma_o_anchor"])
        require(key in expected and key not in rows, "source-sign row")
        rows[key] = row
        covered = {(sigma_c, row["sigma_o_anchor"]) for sigma_c in (-1, 1)}
        require(
            row["xi_index"] == 3 and row["pairing_index"] == 3 and
            row["sigma_c_anchor"] == 0 and
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
            (row["q_cut_degree"], row["p_missing_degree"],
             row["p_next_degree"], row["inner_q_degree"],
             row["q_remainder_degree"], row["parity_condition_degree"],
             row["x_remainder_degree"]) == (4, 2, 2, 3, 3, 3, 1) and
            row["tower_norm_match"] and
            row["field_root_gcd_degree"] == len(row["field_roots"]),
            "nested degree and norm ledger",
        )

        lift = row["direct_lift"]
        exceptional = {
            root for guard in row["exceptional_root_rows"]
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
            lift["z_candidate_count"] == len(lift["z_candidates"]) and
            lift["case_excluded"] and
            lift["witness_count"] == 0 and lift["witnesses"] == [] and
            lift["boundary_solution_count"] == 0 and
            lift["boundary_solutions"] == [] and
            lift["unresolved_count"] == 0 and lift["unresolved"] == [] and
            lift["final_pair_solution_count"] == 0 and
            lift["final_pair_solutions"] == [],
            "complete exclusion ledger",
        )
        current_q_rows = list(q_rows(lift))
        current_roots = []
        for q_row in current_q_rows:
            require(q_row["opposite_pair_cut"] == 0, "opposite pair replay")
            for root_row in q_row["root_rows"]:
                z, d = root_row["z"], root_row["d"]
                e, f = root_row["e"], root_row["f"]
                source = next(
                    item for item in lift["z_candidates"]
                    if item["q"] == q_row["q"] and item["z"] == z and
                    item["d"] == d and item["e"] == e and item["f"] == f
                )
                m = (d*f) % PRIME
                require(
                    z and z*d % PRIME == 1 and
                    d*e % PRIME == q_row["q"] and
                    m and source["root"] == z*z % PRIME,
                    "square/product replay",
                )
                current_roots.append(root_row)
        require(len(current_roots) == lift["z_candidate_count"],
                "root-row ledger")

        current_lanes = list(lane_rows(lift))
        require(all(
            tuple(item["sigma"]) in covered and
            item["status"] == "THIRD_PAIR_NONZERO" and
            item["final_pair_cut"] != 0
            for item in current_lanes
        ), "nonzero final-pair rows")
        all_lanes.extend(current_lanes)
        all_q_rows.extend(current_q_rows)
        profiles[(
            row["sigma_o_anchor"], len(row["field_roots"]),
            lift["live_norm_root_count"], lift["candidate_r_count"],
            lift["source_point_count"], lift["z_candidate_count"],
            len(current_lanes),
        )] += 1

    require(set(rows) == expected and len(rows) == 8, "8 source rows")
    require(profiles == collections.Counter({
        (-1, 10, 5, 14, 26, 32, 64): 4,
        (1, 9, 4, 13, 20, 16, 32): 4,
    }), "exact source profile multiset")
    require(len(all_q_rows) == 480, "480 opposite-q rows")
    require(len(all_lanes) == 384, "384 final-pair evaluations")
    require(sum(row["direct_lift"]["candidate_r_count"]
                for row in rows.values()) == 108, "candidate-r aggregate")
    require(sum(row["direct_lift"]["source_point_count"]
                for row in rows.values()) == 184, "source-point aggregate")
    require(sum(row["direct_lift"]["z_candidate_count"]
                for row in rows.values()) == 192, "target aggregate")


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
    formal_paired_identities()
    formal_transport()
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    verify_payload(json.loads(RESULT.read_text()))
    verify_dag()
    print(
        "cell=3 xi=3 pairings=3,6 raw_cases=32 computed_rows=8 "
        "q_rows=480 lane_checks=384 witnesses=0"
    )


if __name__ == "__main__":
    main()
