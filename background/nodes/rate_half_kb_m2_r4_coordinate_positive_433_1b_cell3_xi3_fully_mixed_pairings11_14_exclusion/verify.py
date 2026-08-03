#!/usr/bin/env python3
"""Verify the cell-3 xi3 fully mixed pairings 11 and 14 exclusion."""

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
    "rate_half_kb_positive_433_1b_cell3_xi3_"
    "fully_mixed_pairing11_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_"
    "fully_mixed_pairing11_census_result.json"
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
    SCRIPT: "068326c0d28732e83afa96d4a88163f5c7aaf316bfa043a16e485608d5a6da95",
    RESULT: "a37aaa98b0fb4716d188a765e665aeff3fa7044653db37759e74738c601a5985",
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
        output[monomial] = output.get(monomial, 0)+coefficient
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


def formal_identities():
    # Variables are A0,A1,A2,B0,B1,B2,x,y.
    variables = []
    for index in range(8):
        monomial = [0]*8
        monomial[index] = 1
        variables.append({tuple(monomial): 1})
    a_values, b_values = variables[:3], variables[3:6]
    x, y = variables[6:]

    def paired(left, right):
        p = [poly_add(b_values[i], poly_scale(poly_mul(left, a_values[i]), -1))
             for i in range(3)]
        q = [
            poly_add(b_values[0], poly_scale(poly_mul(right, a_values[0]), -1)),
            poly_add(poly_scale(b_values[1], -1),
                     poly_mul(right, a_values[1])),
            poly_add(b_values[2], poly_scale(poly_mul(right, a_values[2]), -1)),
        ]
        first = poly_add(poly_mul(p[2], q[0]),
                         poly_scale(poly_mul(p[0], q[2]), -1))
        second = poly_add(poly_mul(p[2], q[1]),
                          poly_scale(poly_mul(p[1], q[2]), -1))
        third = poly_add(poly_mul(p[1], q[0]),
                         poly_scale(poly_mul(p[0], q[1]), -1))
        return poly_add(poly_mul(first, first),
                        poly_scale(poly_mul(second, third), -1))

    require(paired(x, y) == paired(y, x), "formal paired symmetry")
    require(max(monomial[6] for monomial in paired(x, y)) == 2 and
            max(monomial[7] for monomial in paired(x, y)) == 2,
            "formal biquadratic degree")

    # For F(q,w)=A w^2+B w+C, subtraction has the printed factor.
    variables = []
    for index in range(6):
        monomial = [0]*6
        monomial[index] = 1
        variables.append({tuple(monomial): 1})
    a, b, c, u, v, z = variables
    f_u = poly_add(poly_add(product(a, u, u, z, z), product(b, u, z)), c)
    f_v = poly_add(poly_add(product(a, v, v, z, z), product(b, v, z)), c)
    expected = product(poly_add(u, poly_scale(v, -1)), z,
                       poly_add(product(a, poly_add(u, v), z), b))
    require(poly_add(f_u, poly_scale(f_v, -1)) == expected,
            "linear-z subtraction identity")


def canonical_matchings(items):
    if not items:
        return ((),)
    first = items[0]
    output = []
    for index in range(1, len(items)):
        for tail in canonical_matchings(items[1:index]+items[index+1:]):
            output.append(((first, items[index]),)+tail)
    return tuple(output)


def normalized_matching(value):
    return tuple(sorted(tuple(sorted(pair)) for pair in value))


def formal_transport():
    matchings = canonical_matchings(tuple(range(6)))
    require(len(matchings) == 15, "15 canonical matchings")
    require(matchings[11] == ((0, 4), (1, 5), (2, 3)), "pairing 11")
    require(matchings[14] == ((0, 5), (1, 4), (2, 3)), "pairing 14")
    swap = {0: 1, 1: 0, 2: 2, 3: 3, 4: 4, 5: 5}
    transported = tuple((swap[left], swap[right])
                        for left, right in matchings[11])
    require(normalized_matching(transported) == normalized_matching(matchings[14]),
            "positive-DE transport")


def q_rows(lift):
    for r_row in lift["rows"]:
        for t_row in r_row.get("t_rows", []):
            for b_row in t_row.get("b_rows", []):
                for q_row in b_row.get("q_rows", []):
                    yield b_row, q_row


def verify_payload(payload):
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-cell3-xi3-fully-mixed-"
        "pairing11-source-census-v1",
        "schema",
    )
    require("no claim beyond the printed cases" in payload["scope"],
            "scope discipline")
    require(payload["source_quotient_sha256"] == digest(QUOTIENT),
            "quotient custody")
    require(payload["source_kernel_sha256"] == digest(KERNEL), "kernel custody")
    require(payload["source_product_sha256"] == digest(PRODUCT), "product custody")

    expected = {(epsilon, sigma_c, sigma_o) for epsilon in SIGNS
                for sigma_c in (-1, 1) for sigma_o in (-1, 1)}
    rows = {}
    profiles = collections.Counter()
    all_q_rows = []
    all_roots = []
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["sigma_c_anchor"],
               row["sigma_o_anchor"])
        require(key in expected and key not in rows, "source/target row")
        rows[key] = row
        require(
            row["xi_index"] == 3 and row["pairing_index"] == 11 and
            row["target_lanes_covered"] == [[key[1], key[2]]],
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
            (row["compatibility_cut_degree"],
             row["missing_substitution_cut_degree_bound"],
             row["reduced_missing_cut_degree"],
             row["bezout_matrix_size"]) == (4, 8, 3, 4) and
            row["tower_norm_used"] and
            row["field_root_gcd_degree"] == len(row["field_roots"]),
            "elimination degree and norm ledger",
        )

        lift = row["direct_lift"]
        exceptional = {root for guard in row["exceptional_root_rows"]
                       for root in (guard["roots"] or [])}
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
        for b_row, q_row in current_q_rows:
            require(q_row["status"] == "CHECKED", "checked q row")
            if q_row["reconstruction_mode"] == "LINEAR_Z":
                require(q_row["linear_denominator"] != 0, "regular denominator")
            elif q_row["reconstruction_mode"] == "DEGENERATE_A_B":
                require(q_row["linear_denominator"] == 0 and q_row["b_q"] == 0,
                        "degenerate branch")
            else:
                require(q_row["reconstruction_mode"] == "INCONSISTENT_LINEAR_Z",
                        "known reconstruction mode")
            for root in q_row["root_rows"]:
                z, d, e, f = (root[name] for name in ("z", "d", "e", "f"))
                q = q_row["q"]
                m, s = b_row["source_missing"], b_row["source_sum"]
                require(
                    z and z*d % PRIME == 1 and d*e % PRIME == q and
                    d*f % PRIME == m and pow(d+f, 2, PRIME) == s and
                    root["first_pair_cut"] == 0 and
                    root["second_pair_cut"] == 0 and
                    root["final_pair_cut"] != 0 and
                    root["status"] == "THIRD_PAIR_NONZERO",
                    "direct target replay",
                )
                current_roots.append(root)
        require(len(current_roots) == lift["z_candidate_count"],
                "reconstructed-target ledger")
        all_q_rows.extend(current_q_rows)
        all_roots.extend(current_roots)
        profiles[(
            row["sigma_c_anchor"], len(row["field_roots"]),
            lift["live_norm_root_count"], lift["candidate_r_count"],
            lift["source_point_count"], lift["z_candidate_count"],
            len(current_q_rows), len(current_roots),
        )] += 1

    require(set(rows) == expected and len(rows) == 16, "16 exact rows")
    require(profiles == collections.Counter({
        (-1, 9, 4, 11, 16, 6, 24, 6): 8,
        (1, 7, 2, 9, 10, 2, 6, 2): 8,
    }), "exact profile multiset")
    require(len(all_q_rows) == 240, "240 compatibility-q rows")
    require(len(all_roots) == 64, "64 final-pair evaluations")
    require(sum(row["direct_lift"]["candidate_r_count"]
                for row in rows.values()) == 160, "candidate-r aggregate")
    require(sum(row["direct_lift"]["source_point_count"]
                for row in rows.values()) == 208, "source-point aggregate")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED", "DAG node")
    require(PARENT in nodes and nodes[PARENT]["status"] == "PROVED", "parent")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")


def main():
    formal_identities()
    formal_transport()
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    verify_payload(json.loads(RESULT.read_text()))
    verify_dag()
    print(
        "cell=3 xi=3 pairings=11,14 raw_cases=32 computed_rows=16 "
        "q_rows=240 final_checks=64 witnesses=0"
    )


if __name__ == "__main__":
    main()
