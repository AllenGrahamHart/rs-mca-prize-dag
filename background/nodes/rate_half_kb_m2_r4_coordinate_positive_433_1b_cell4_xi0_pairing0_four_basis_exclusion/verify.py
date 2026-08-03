#!/usr/bin/env python3
"""Verify the cell-4 xi0/pairing0 four-basis exclusion."""

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
    "rate_half_kb_positive_433_1b_cell4_xi0_pairing0_four_basis_norm_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_xi0_pairing0_four_basis_norm_result.json"
)
STRUCTURE = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_result.json"
)
KERNEL = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell4_compact_kernel_result.json"
)
PINNED = {
    SCRIPT: "dbf2a2db03c2f741ca03b91b7ee4d1851f00eef56a84a4b9cc887930560cce05",
    RESULT: "ded7d2b0679c83ddf2dc85b53a1ddcf08e06ae5a3405ac7ef22b9faf0d63baf4",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_four_basis_tower_kernel",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
)
PRIME = 2130706433
IOTA = 16711679
r_symbol = sp.symbols("r")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_profile(profile, shape, label):
    require((profile["degree"], profile["terms"]) == shape,
            f"{label} shape")
    polynomial = sp.Poly(
        sp.sympify(profile["expression"]), r_symbol, modulus=PRIME
    )
    require(polynomial.degree() == shape[0] and
            len(polynomial.terms()) == shape[1] and
            hashlib.sha256(str(polynomial.as_expr()).encode()).hexdigest() ==
            profile["sha256"], f"{label} custody")


def modular_value(expression, point):
    return int(sp.Poly(expression, *expression.free_symbols,
                       modulus=PRIME).eval(point)) % PRIME


def verify_result(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell4-xi0-pairing0-four-basis-v1",
            "schema")
    require(payload["field"] == PRIME and
            payload["source_structure_sha256"] == digest(STRUCTURE) and
            payload["source_kernel_sha256"] == digest(KERNEL), "custody")
    expected = set(itertools.product((-1, 1), (-1, 1)))
    actual = set()
    guard_shapes = (
        ("base_leading_0", 2, 3, 0, 1),
        ("quad_inverse_1", 8, 7, 0, 1),
        ("quad_inverse_2", 10, 11, 4, 4),
        ("quad_inverse_3", 76, 68, 33, 34),
    )
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs not in actual, "duplicate sign row")
        actual.add(signs)
        require(row["status"] == "COMPLETE" and row["excluded"],
                "exclusion status")
        require(row["target_root_count"] == 5 and
                len(row["target_roots"]) == 5 and
                set(row["target_roots"]) <= set(row["candidate_roots"]),
                "target roots")
        require(row["candidate_root_count"] == 7 and
                len(set(row["candidate_roots"])) == 7, "candidate roots")
        require(row["source_point_count"] == 0 and
                row["route_point_count"] == 0 and
                not row["finite_rows"] and not row["witnesses"] and
                not row["unresolved"], "empty direct replay")
        verify_profile(
            row["target_norm"]["numerator"], (298, 265), "norm numerator"
        )
        verify_profile(
            row["target_norm"]["denominator"], (156, 157), "norm denominator"
        )
        require(len(row["inverse_guards"]) == 4, "inverse guard count")
        for guard, shape in zip(row["inverse_guards"], guard_shapes):
            name, nd, nt, dd, dt = shape
            require(guard["name"] == name, f"guard order {name}")
            verify_profile(guard["numerator"], (nd, nt), f"{name} numerator")
            verify_profile(guard["denominator"], (dd, dt), f"{name} denominator")

        boundaries = row["boundary_rows"]
        require(len(boundaries) == 7 and
                {value["r"] for value in boundaries} ==
                set(row["candidate_roots"]), "boundary cover")
        base = sp.sympify(row["base_relation"])
        t_var, r_var = sp.symbols("t r")
        for boundary in boundaries:
            r_value = boundary["r"]
            if boundary["stage"] == "R_GUARD":
                require(
                    r_value * (r_value*r_value - 1) *
                    (r_value*r_value + 1) % PRIME == 0,
                    "r boundary guard",
                )
            elif boundary["stage"] == "T_GUARD":
                t_value = boundary["t"]
                require(int(base.subs({r_var: r_value, t_var: t_value})) %
                        PRIME == 0, "base lift")
                require(
                    t_value * (t_value*t_value - 1) *
                    (t_value*t_value + 1) *
                    (t_value*t_value - r_value*r_value) *
                    (t_value*t_value + r_value*r_value) % PRIME == 0,
                    "t boundary guard",
                )
            else:
                raise RuntimeError("unexpected boundary stage")
        r_boundaries = {
            value["r"] for value in boundaries if value["stage"] == "R_GUARD"
        }
        require(r_boundaries == {0, 1, PRIME - 1, IOTA, PRIME - IOTA},
                "five universal r boundaries")
    require(actual == expected, "four-sign cover")


def verify_source():
    ast.parse(SCRIPT.read_text())
    text = SCRIPT.read_text()
    for snippet in (
        "target_free = paired(missing_record, -missing_record)",
        "target_norm = target_free.norm()",
        "candidate_roots.update(roots)",
        "for r_value in sorted(candidate_roots)",
        "unresolved.append",
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
    print("cell=4 xi=0 pairing=0 signs=4 lanes=4 raw_cases=16 candidates=28")


if __name__ == "__main__":
    main()
