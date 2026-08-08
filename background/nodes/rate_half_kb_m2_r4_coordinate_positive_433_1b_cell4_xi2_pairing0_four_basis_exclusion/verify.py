#!/usr/bin/env python3
"""Verify the cell-4 xi2/pairing0 four-basis exclusion."""

import ast
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi2_pairing0_four_basis_norm_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi2_pairing0_four_basis_norm_result.json"
)
STRUCTURE = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json"
)
KERNEL = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json"
)
PINNED = {
    SCRIPT: "ece1e6568b7b96128a5fdad47dbf0e03af79659549271c3d1d2d0cfc13414d2a",
    RESULT: "1e0ac4dc98ee943a756ee8b6af1b731e45aca407a1b3c434861fb08fe9c4d722",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_four_basis_tower_kernel",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
)
PRIME = 2130706433
IOTA = 16711679
t, r, c, b = sp.symbols("t r c b")
VARIABLES = (t, r, c, b)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def value(expression, point):
    return int(sp.sympify(expression).subs({
        t: point.get("t", 0),
        r: point.get("r", 0),
        c: point.get("c", 0),
        b: point.get("b", 0),
    })) % PRIME


def verify_profile(profile, shape, label):
    require((profile["degree"], profile["terms"]) == shape,
            f"{label} shape")
    polynomial = sp.Poly(sp.sympify(profile["expression"]), r, modulus=PRIME)
    require(polynomial.degree() == shape[0] and
            len(polynomial.terms()) == shape[1] and
            hashlib.sha256(str(polynomial.as_expr()).encode()).hexdigest() ==
            profile["sha256"], f"{label} custody")


def paired(a_values, b_values, left, right):
    p0, p1, p2 = (
        (b_value - left*a_value) % PRIME
        for a_value, b_value in zip(a_values, b_values)
    )
    q0 = (b_values[0] - right*a_values[0]) % PRIME
    q1 = (-b_values[1] + right*a_values[1]) % PRIME
    q2 = (b_values[2] - right*a_values[2]) % PRIME
    return (
        pow((p2*q0 - p0*q2) % PRIME, 2, PRIME)
        - ((p2*q1 - p1*q2) % PRIME)
        * ((p1*q0 - p0*q1) % PRIME)
    ) % PRIME


def verify_result(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell4-xi2-pairing0-four-basis-v1",
            "schema")
    require(payload["field"] == PRIME and
            payload["source_structure_sha256"] == digest(STRUCTURE) and
            payload["source_kernel_sha256"] == digest(KERNEL), "custody")
    kernel_payload = json.loads(KERNEL.read_text())
    kernels = {
        tuple(row["epsilon"]): tuple(sp.sympify(item["expression"])
                                     for item in row["kernel"])
        for row in kernel_payload["rows"]
    }
    expected = set(itertools.product((-1, 1), repeat=2))
    actual = set()
    guard_shapes = (
        ("base_leading_0", 2, 3, 0, 1),
        ("quad_inverse_1", 8, 7, 0, 1),
        ("quad_inverse_2", 10, 11, 4, 4),
        ("quad_inverse_3", 76, 68, 33, 34),
    )
    norm_hashes = set()
    finite_total = 0
    no_lift_total = 0
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs in expected and signs not in actual, "source-sign row")
        actual.add(signs)
        require(row["status"] == "COMPLETE" and row["excluded"],
                "exclusion status")
        require(row["target_root_count"] == 8 and
                len(row["target_roots"]) == len(set(row["target_roots"])) == 8 and
                set(row["target_roots"]) <= set(row["candidate_roots"]),
                "target roots")
        require(row["candidate_root_count"] == 10 and
                len(row["candidate_roots"]) ==
                len(set(row["candidate_roots"])) == 10, "candidate roots")
        require(row["source_point_count"] == row["route_point_count"] == 4 and
                len(row["finite_rows"]) == 4 and
                not row["witnesses"] and not row["unresolved"],
                "finite terminal ledger")
        verify_profile(row["target_norm"]["numerator"], (308, 281),
                       "norm numerator")
        verify_profile(row["target_norm"]["denominator"], (160, 161),
                       "norm denominator")
        norm_hashes.add(row["target_norm"]["numerator"]["sha256"])
        require(len(row["inverse_guards"]) == 4, "inverse guard count")
        for guard, shape in zip(row["inverse_guards"], guard_shapes):
            name, nd, nt, dd, dt = shape
            require(guard["name"] == name, f"guard order {name}")
            verify_profile(guard["numerator"], (nd, nt), f"{name} numerator")
            verify_profile(guard["denominator"], (dd, dt), f"{name} denominator")

        base = sp.sympify(row["base_relation"])
        b_relation = sp.sympify(row["b_relation"])
        c_relation = sp.sympify(row["c_relation"])
        boundaries = row["boundary_rows"]
        require(len(boundaries) == 7 and
                sum(item["stage"] == "R_GUARD" for item in boundaries) == 5 and
                sum(item["stage"] == "T_GUARD" for item in boundaries) == 2,
                "boundary partition")
        for item in boundaries:
            if item["stage"] == "R_GUARD":
                r_value = item["r"]
                require(r_value * (r_value*r_value - 1) *
                        (r_value*r_value + 1) % PRIME == 0,
                        "r boundary guard")
            elif item["stage"] == "T_GUARD":
                require(value(base, item) == 0, "boundary base lift")
                r_value, t_value = item["r"], item["t"]
                require(t_value * (t_value*t_value - 1) *
                        (t_value*t_value + 1) *
                        (t_value*t_value - r_value*r_value) *
                        (t_value*t_value + r_value*r_value) % PRIME == 0,
                        "t boundary guard")
            else:
                raise RuntimeError("unexpected boundary stage")
        r_boundaries = {item["r"] for item in boundaries
                        if item["stage"] == "R_GUARD"}
        require(r_boundaries == {0, 1, PRIME - 1, IOTA, PRIME - IOTA},
                "universal r boundaries")

        require(len(row["no_lift_rows"]) == 6 and
                all(item["stage"] == "NO_B_ROOT"
                    for item in row["no_lift_rows"]), "no-b ledger")
        b_poly = sp.Poly(b_relation, b)
        require(b_poly.degree() == 2, "quadratic b relation")
        for item in row["no_lift_rows"]:
            require(value(base, item) == 0, "no-b base lift")
            coefficients = [value(coefficient, item)
                            for coefficient in b_poly.all_coeffs()]
            leading, linear, constant = coefficients
            require(leading != 0, "no-b leading unit")
            discriminant = (linear*linear - 4*leading*constant) % PRIME
            require(pow(discriminant, (PRIME - 1)//2, PRIME) == PRIME - 1,
                    "no-b nonsquare discriminant")

        kernel = kernels[signs]
        for item in row["finite_rows"]:
            require(item["status"] == "NONZERO" and item["cut"] % PRIME,
                    "finite nonzero terminal")
            require(value(base, item) == value(b_relation, item) ==
                    value(c_relation, item) == 0, "finite common relations")
            r_value, t_value = item["r"], item["t"]
            b_value, c_value = item["b"], item["c"]
            guards = (
                b_value, c_value, r_value, t_value,
                b_value - 1, b_value + 1, c_value - 1, c_value + 1,
                b_value - c_value, b_value + c_value,
                r_value*r_value - 1, r_value*r_value + 1,
                t_value*t_value - 1, t_value*t_value + 1,
                t_value*t_value - r_value*r_value,
                t_value*t_value + r_value*r_value,
            )
            require(all(guard % PRIME for guard in guards), "finite route guards")
            kernel_values = [value(expression, item) for expression in kernel]
            a_values, b_values = kernel_values[:3], kernel_values[3:6]
            missing_label = -t_value*t_value % PRIME
            a_missing = sum(coefficient*pow(missing_label, degree, PRIME)
                            for degree, coefficient in enumerate(a_values)) % PRIME
            b_missing = sum(coefficient*pow(missing_label, degree, PRIME)
                            for degree, coefficient in enumerate(b_values)) % PRIME
            require(a_missing != 0, "missing-record denominator")
            missing = b_missing*pow(a_missing, -1, PRIME) % PRIME
            require(missing == item["missing"], "missing-record replay")
            de_value = -missing % PRIME
            require(paired(a_values, b_values, de_value, de_value) ==
                    item["cut"] % PRIME, "negative-DE paired replay")

        touched = ({item["r"] for item in boundaries} |
                   {item["r"] for item in row["no_lift_rows"]} |
                   {item["r"] for item in row["finite_rows"]})
        require(touched == set(row["candidate_roots"]),
                "every candidate reaches a terminal")
        finite_total += len(row["finite_rows"])
        no_lift_total += len(row["no_lift_rows"])
    require(actual == expected and len(norm_hashes) == 4,
            "four specialized source signs")
    require((finite_total, no_lift_total) == (16, 24), "global lift totals")


def verify_source():
    ast.parse(SCRIPT.read_text())
    text = SCRIPT.read_text()
    for snippet in (
        "de_record = -missing_record",
        "target_free = paired(de_record, de_record)",
        "target_norm = target_free.norm()",
        'no_lift_rows.append({**bt_point, "stage": "NO_B_ROOT"})',
        "candidate_roots.update(roots)",
        '"excluded": not witnesses and not unresolved',
    ):
        require(snippet in text, f"source snippet {snippet}")
    require("sigma_c" not in text and "sigma_o" not in text,
            "target-lane independence")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"missing parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG consumer")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    verify_source()
    verify_result(json.loads(RESULT.read_text()))
    verify_dag()
    print("cell=4 xi=2 pairing=0 signs=4 lanes=4 raw_cases=16 "
          "candidates=40 finite_points=16 witnesses=0")


if __name__ == "__main__":
    main()
