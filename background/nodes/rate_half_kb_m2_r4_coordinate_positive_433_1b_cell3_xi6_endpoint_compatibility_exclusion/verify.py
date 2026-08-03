#!/usr/bin/env python3
"""Verify the cell-3 xi6 source endpoint-compatibility exclusion."""

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
    "rate_half_kb_positive_433_1b_cell3_xi5_xi6_"
    "endpoint_compatibility_modal.py"
)
RESULT = EXPERIMENTS / (
    "rate_half_kb_positive_433_1b_cell3_xi5_xi6_"
    "endpoint_compatibility_census_result.json"
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
    SCRIPT: "3e5ad66722ba7b4890a2c29333a1525ce91a5efe87357e779d472c3ffd2f3f87",
    RESULT: "74aad0cbb33fad989d11f2d412d2f74c4d1e52e47865a0d6106fae4d4b0e05fc",
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


def poly_pow(value, exponent):
    output = {(0, 0): 1}
    for _ in range(exponent):
        output = poly_mul(output, value)
    return output


def formal_identity():
    c_value = {(1, 0): 1}
    g_value = {(0, 1): 1}
    m_value = poly_mul(c_value, g_value)
    sum_value = poly_add(c_value, g_value)
    s_value = poly_pow(sum_value, 2)
    c_square = poly_pow(c_value, 2)
    cleared = poly_add(
        poly_pow(poly_add(c_square, m_value), 2),
        poly_scale(poly_mul(s_value, c_square), -1),
    )
    require(not cleared, "formal cleared endpoint identity")


def b_rows(lift):
    for r_row in lift["rows"]:
        for t_row in r_row.get("t_rows", []):
            for b_row in t_row.get("b_rows", []):
                yield r_row["r"], t_row["t"], b_row


def verify_payload(payload):
    require(
        payload["schema"] ==
        "rate-half-kb-positive-433-1b-cell3-xi5-xi6-"
        "endpoint-compatibility-source-census-v1",
        "schema",
    )
    require("compatible sources are not asserted" in payload["scope"],
            "scope discipline")
    require(payload["source_quotient_sha256"] == digest(QUOTIENT),
            "quotient custody")
    require(payload["source_kernel_sha256"] == digest(KERNEL),
            "kernel custody")
    require(payload["source_product_sha256"] == digest(PRODUCT),
            "product custody")

    expected = {(epsilon, xi) for epsilon in SIGNS for xi in (5, 6)}
    rows = {}
    profiles = collections.Counter()
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["xi_index"])
        require(key in expected and key not in rows, "source/xi row")
        rows[key] = row
        require(
            row["status"] == "COMPLETE" and
            row["pairing_index"] == 0 and
            row["sigma_c_anchor"] == 0 and
            row["sigma_o_anchor"] == 0 and
            row["target_lanes_covered"] == [
                [-1, -1], [-1, 1], [1, -1], [1, 1]
            ] and
            row["basis"] == ["1", "t", "t^2", "b", "b*t", "b*t^2"] and
            (row["base_degree"], row["b_degree"],
             row["algebra_dimension"]) == (3, 2, 6) and
            row["tower_norm_used"] and
            row["field_root_gcd_degree"] == len(row["field_roots"]),
            "complete source-only quotient row",
        )
        require(
            row["endpoint_kind"] == ("b" if key[1] == 5 else "c"),
            "endpoint kind",
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

        points = []
        compatible = []
        statuses = collections.Counter()
        eligible = 0
        for r_value, t_value, b_row in b_rows(lift):
            statuses[b_row["status"]] += 1
            if "source_missing" not in b_row:
                continue
            point = [r_value, t_value, b_row["b"], b_row["c"]]
            points.append(point)
            m_value = b_row["source_missing"]
            if m_value == 0:
                require(b_row["status"] == "MISSING_PRODUCT_BOUNDARY",
                        "zero missing product boundary")
                continue
            eligible += 1
            endpoint = b_row["b"] if key[1] == 5 else b_row["c"]
            endpoint_square = endpoint*endpoint % PRIME
            signed_other = m_value*pow(endpoint, -1, PRIME) % PRIME
            direct = (
                pow(endpoint+signed_other, 2, PRIME)-b_row["source_sum"]
            ) % PRIME
            cleared = (
                pow(endpoint_square+m_value, 2, PRIME)
                - b_row["source_sum"]*endpoint_square
            ) % PRIME
            require(
                b_row["endpoint"] == endpoint and
                b_row["signed_other"] == signed_other and
                b_row["direct_compatibility"] == direct and
                b_row["cleared_compatibility"] == cleared and
                cleared == endpoint_square*direct % PRIME,
                "direct endpoint replay",
            )
            if not cleared:
                require(b_row["status"] == "COMPATIBLE_SOURCE",
                        "compatible status")
                compatible.append((point, endpoint, signed_other, m_value))
            else:
                require(b_row["status"] == "COMPATIBILITY_NONZERO",
                        "nonzero compatibility status")

        require(
            lift["source_point_count"] == len(points) ==
            len(lift["source_points"]) and
            sorted(points) == sorted(lift["source_points"]),
            "source-point ledger",
        )
        listed_compatible = [
            (
                item["point"], item["endpoint"], item["signed_other"],
                item["source_missing"],
            )
            for item in lift["compatible_source_points"]
        ]
        require(
            lift["compatible_source_point_count"] == len(compatible) ==
            len(listed_compatible) and
            sorted(compatible) == sorted(listed_compatible) and
            lift["unresolved_count"] == 0 and lift["unresolved"] == [],
            "compatible and unresolved ledgers",
        )

        if key[1] == 5:
            require(
                (len(row["field_roots"]),
                 lift["live_norm_root_count"],
                 lift["candidate_r_count"], len(points), eligible,
                 len(compatible)) == (7, 3, 10, 14, 12, 6) and
                statuses == collections.Counter({
                    "COMPATIBILITY_NONZERO": 6,
                    "COMPATIBLE_SOURCE": 6,
                    "MISSING_PRODUCT_BOUNDARY": 2,
                    "MISSING_RATIO_INCONSISTENT": 2,
                }) and not lift["case_excluded"],
                "xi5 retained frontier",
            )
        else:
            require(
                (len(row["field_roots"]),
                 lift["live_norm_root_count"],
                 lift["candidate_r_count"], len(points), eligible,
                 len(compatible)) == (5, 1, 8, 8, 6, 0) and
                statuses == collections.Counter({
                    "COMPATIBILITY_NONZERO": 6,
                    "MISSING_PRODUCT_BOUNDARY": 2,
                    "MISSING_RATIO_INCONSISTENT": 2,
                }) and lift["case_excluded"],
                "xi6 complete exclusion",
            )
        profiles[(key[1], len(points), eligible, len(compatible))] += 1

    require(set(rows) == expected and len(rows) == 8, "eight exact rows")
    require(profiles == collections.Counter({
        (5, 14, 12, 6): 4,
        (6, 8, 6, 0): 4,
    }), "exact profile multiset")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    require(PARENT in nodes and nodes[PARENT]["status"] == "PROVED",
            "parent")
    edges = {(row["from"], row["to"], row["kind"])
             for row in dag["edges"]}
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")


def main():
    formal_identity()
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    verify_payload(json.loads(RESULT.read_text()))
    verify_dag()
    print(
        "cell=3 xi=6 source_rows=4 candidate_r=32 source_points=32 "
        "eligible_points=24 compatible=0 raw_cases=240"
    )


if __name__ == "__main__":
    main()
