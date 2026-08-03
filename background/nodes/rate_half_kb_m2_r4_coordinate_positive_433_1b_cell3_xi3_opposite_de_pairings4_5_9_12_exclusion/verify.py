#!/usr/bin/env python3
"""Verify the cell-3 xi3 opposite-DE pairings 4, 5, 9, and 12 exclusion."""

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
    "opposite_de_parity_missing_f_bezout_pilot_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi3_"
    "opposite_de_parity_missing_f_bezout_census_result.json"
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
    SCRIPT: "810032f1be4e1d6ebcdce1bd68a289958989d46148f6d92b35380a7fab8607b3",
    RESULT: "2bd07012540e7536918e10937800019972e14e89e1dc241369a0f32199a2369d",
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


def poly_pow(value, exponent):
    size = len(next(iter(value)))
    output = {(0,)*size: 1}
    for _ in range(exponent):
        output = poly_mul(output, value)
    return output


def product(*values):
    if any(not value for value in values):
        return {}
    output = {(0,)*len(next(iter(values[0]))): 1}
    for value in values:
        output = poly_mul(output, value)
    return output


def variables(count):
    output = []
    for index in range(count):
        monomial = [0]*count
        monomial[index] = 1
        output.append({tuple(monomial): 1})
    return output


def permutation_sign(permutation):
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left+1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def formal_identities():
    # Variables are A0,A1,A2,B0,B1,B2,x,y.
    values = variables(8)
    a_values, b_values = values[:3], values[3:6]
    x, y = values[6:]

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

    # A(q)A(-q) is exactly the printed parity cut at x=q^2.
    a2, a1, a0, q_value = variables(4)
    q_square = poly_mul(q_value, q_value)
    even_part = poly_add(poly_mul(a2, q_square), a0)
    a_plus = poly_add(even_part, poly_mul(a1, q_value))
    a_minus = poly_add(even_part, poly_scale(poly_mul(a1, q_value), -1))
    parity = poly_add(poly_mul(even_part, even_part),
                      poly_scale(product(a1, a1, q_square), -1))
    require(poly_mul(a_plus, a_minus) == parity, "formal parity identity")

    # Check the printed quadratic resultant against the Sylvester determinant.
    u2, u1, u0, v2, v1, v0 = variables(6)
    zero = {}
    matrix = (
        (u2, u1, u0, zero),
        (zero, u2, u1, u0),
        (v2, v1, v0, zero),
        (zero, v2, v1, v0),
    )
    determinant = {}
    for permutation in itertools.permutations(range(4)):
        term = product(*(matrix[row][permutation[row]] for row in range(4)))
        determinant = poly_add(
            determinant, poly_scale(term, permutation_sign(permutation))
        )
    first = poly_add(poly_mul(u2, v0), poly_scale(poly_mul(u0, v2), -1))
    second = poly_add(poly_mul(u2, v1), poly_scale(poly_mul(u1, v2), -1))
    third = poly_add(poly_mul(u1, v0), poly_scale(poly_mul(u0, v1), -1))
    formula = poly_add(poly_mul(first, first),
                       poly_scale(poly_mul(second, third), -1))
    require(determinant == formula, "quadratic resultant identity")

    # M(f)=0 follows identically from m=df and s=(d+f)^2.
    d_value, f_value = variables(2)
    m_value = poly_mul(d_value, f_value)
    sum_value = poly_add(d_value, f_value)
    s_value = poly_mul(sum_value, sum_value)
    coefficient = poly_add(poly_scale(m_value, 2), poly_scale(s_value, -1))
    missing = poly_add(
        poly_add(poly_pow(f_value, 4),
                 poly_mul(coefficient, poly_pow(f_value, 2))),
        poly_pow(m_value, 2),
    )
    require(not missing, "monic missing-f identity")


def canonical_matchings(items):
    if not items:
        return ((),)
    output = []
    for index in range(1, len(items)):
        for tail in canonical_matchings(items[1:index]+items[index+1:]):
            output.append(((items[0], items[index]),)+tail)
    return tuple(output)


def normalized_matching(value):
    return tuple(sorted(tuple(sorted(pair)) for pair in value))


def formal_transport():
    matchings = canonical_matchings(tuple(range(6)))
    require(len(matchings) == 15, "15 canonical matchings")
    require(matchings[4] == ((0, 2), (1, 4), (3, 5)), "pairing 4")
    require(matchings[5] == ((0, 2), (1, 5), (3, 4)), "pairing 5")
    swap = {0: 1, 1: 0, 2: 2, 3: 3, 4: 4, 5: 5}
    for source, target in ((4, 9), (5, 12)):
        transported = tuple((swap[left], swap[right])
                            for left, right in matchings[source])
        require(
            normalized_matching(transported) ==
            normalized_matching(matchings[target]),
            f"positive-DE transport {source}->{target}",
        )


def f_rows(lift):
    for r_row in lift["rows"]:
        for t_row in r_row.get("t_rows", []):
            for b_row in t_row.get("b_rows", []):
                for f_row in b_row.get("f_rows", []):
                    yield b_row, f_row


def verify_payload(payload):
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-cell3-xi3-opposite-de-parity-"
        "missing-f-bezout-source-census-v1",
        "schema",
    )
    require("no claim beyond the printed cases" in payload["scope"],
            "scope discipline")
    require(payload["source_quotient_sha256"] == digest(QUOTIENT),
            "quotient custody")
    require(payload["source_kernel_sha256"] == digest(KERNEL), "kernel custody")
    require(payload["source_product_sha256"] == digest(PRODUCT), "product custody")

    expected = {(epsilon, 4, 0) for epsilon in SIGNS} | {
        (epsilon, 5, sigma_c) for epsilon in SIGNS for sigma_c in (-1, 1)
    }
    rows = {}
    profiles = collections.Counter()
    all_f_rows = []
    all_q_rows = []
    all_lanes = []
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["pairing_index"],
               row["sigma_c_anchor"])
        require(key in expected and key not in rows, "source/matching row")
        rows[key] = row
        expected_lanes = (
            [[-1, -1], [-1, 1], [1, -1], [1, 1]] if key[1] == 4
            else [[key[2], -1], [key[2], 1]]
        )
        require(row["xi_index"] == 3 and row["sigma_o_anchor"] == 0 and
                row["target_lanes_covered"] == expected_lanes,
                "scope and lane cover")
        require(
            row["status"] == "COMPLETE" and
            row["basis"] == ["1", "t", "t^2", "b", "b*t", "b*t^2"] and
            (row["base_degree"], row["b_degree"],
             row["algebra_dimension"]) == (3, 2, 6),
            "complete six-basis row",
        )
        require(
            (row["opposite_q_cut_degree"],
             row["parity_missing_f_resultant_degree"],
             row["missing_f_cut_degree"],
             row["reduced_parity_cut_degree"],
             row["bezout_matrix_size"]) == (4, 8, 4, 3, 4) and
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
            lift["target_candidate_count"] == len(lift["target_candidates"]) and
            lift["case_excluded"] and
            lift["witness_count"] == 0 and lift["witnesses"] == [] and
            lift["boundary_solution_count"] == 0 and
            lift["boundary_solutions"] == [] and
            lift["unresolved_count"] == 0 and lift["unresolved"] == [] and
            lift["final_pair_solution_count"] == 0 and
            lift["final_pair_solutions"] == [],
            "complete exclusion ledger",
        )

        current_f_rows = list(f_rows(lift))
        current_q_rows = []
        current_lanes = []
        for b_row, f_row in current_f_rows:
            require(f_row["status"] == "CHECKED", "checked f row")
            require(f_row["f"] in b_row["missing_f_roots"], "enumerated f root")
            require(f_row["q_roots"] is not None, "no free-q branch")
            require(f_row["first_q_cut_degree"] == 4 and
                    f_row["second_q_cut_degree"] <= 2,
                    "opposite quartic and quadratic q cuts")
            for q_row in f_row["q_rows"]:
                require(q_row["status"] == "CHECKED", "checked q row")
                q, d_value, e_value = (
                    q_row[name] for name in ("q", "d", "e")
                )
                f_value = f_row["f"]
                m_value, s_value = (
                    b_row["source_missing"], b_row["source_sum"]
                )
                require(
                    f_value == f_row["f"] and q in f_row["q_roots"] and
                    d_value*e_value % PRIME == q and
                    d_value*f_value % PRIME == m_value and
                    pow(d_value+f_value, 2, PRIME) == s_value and
                    q_row["first_pair_cut"] == 0 and
                    q_row["second_pair_cut"] == 0,
                    "direct target reconstruction",
                )
                require(
                    {tuple(lane["sigma"]) for lane in q_row["lane_rows"]} ==
                    {tuple(lane) for lane in expected_lanes} and
                    len(q_row["lane_rows"]) == len(expected_lanes),
                    "all final lanes",
                )
                for lane in q_row["lane_rows"]:
                    require(
                        lane["status"] == "THIRD_PAIR_NONZERO" and
                        lane["final_pair_cut"] != 0,
                        "nonzero final pair",
                    )
                    current_lanes.append(lane)
                current_q_rows.append(q_row)
        require(len(current_q_rows) == lift["target_candidate_count"],
                "reconstructed-target ledger")
        all_f_rows.extend(current_f_rows)
        all_q_rows.extend(current_q_rows)
        all_lanes.extend(current_lanes)
        profiles[(
            row["sigma_c_anchor"], len(row["field_roots"]),
            lift["live_norm_root_count"], lift["candidate_r_count"],
            lift["source_point_count"], lift["target_candidate_count"],
        )] += 1

    require(set(rows) == expected and len(rows) == 12, "12 exact rows")
    require(profiles == collections.Counter({
        (0, 16, 11, 18, 30, 14): 4,
        (-1, 14, 9, 16, 22, 16): 4,
        (1, 14, 9, 16, 22, 16): 4,
    }), "exact profile multiset")
    require(len(all_f_rows) == 928, "928 missing-f rows")
    require(len(all_q_rows) == 184, "184 reconstructed targets")
    require(len(all_lanes) == 480, "480 final-pair evaluations")
    require(sum(row["direct_lift"]["candidate_r_count"]
                for row in rows.values()) == 200, "candidate-r aggregate")
    require(sum(row["direct_lift"]["source_point_count"]
                for row in rows.values()) == 296, "source-point aggregate")


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
        "cell=3 xi=3 pairings=4,5,9,12 raw_cases=64 computed_rows=12 "
        "f_rows=928 targets=184 final_checks=480 witnesses=0"
    )


if __name__ == "__main__":
    main()
