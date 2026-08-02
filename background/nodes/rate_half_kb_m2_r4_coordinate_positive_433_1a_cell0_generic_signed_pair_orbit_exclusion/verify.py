#!/usr/bin/env python3
"""Verify the generic cell-0 signed-pair orbit exclusion."""

import hashlib
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell0_generic_signed_pair_orbit_exclusion"
)
EXPERIMENTS = ROOT / "experiments/prize_resolution"
KERNEL = EXPERIMENTS / "rate_half_kb_positive_433_1a_cell0_kernel_reduction_result.json"
PAIR = EXPERIMENTS / "rate_half_kb_positive_433_1a_cell0_generic_signed_pair_result.json"
T2 = EXPERIMENTS / "rate_half_kb_positive_433_1a_cell0_t2_signed_family_result.json"
HASHES = {
    KERNEL: "9b846a05e43b092b2f4b41658424d0ab70bf910e9d79a48be49db6d38f573167",
    PAIR: "70f18a761f952475c43156daeffac5d874c981a790fecc76c40b05ec3b421e69",
    T2: "6e08887afefdeb156d95b53aa7d4fde010c6e3a900925f810f7ec1b52ea23860",
}
BRANCHES = (583634934, 1547071505)
PROGRAMS = {
    583634934: "5e177fdf090a04907eec5bfef116e705b918a8297448dec5cc830e2d6ce8e6e3",
    1547071505: "59261800cf90480bfa2fb3252debf1a38ea2370c64e4185c371e19e679d71c31",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_kernel(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell0-kernel-reduction-v1",
            "kernel schema")
    result = payload["result"]
    require(result["status"] == "COMPLETE", "kernel completion")
    rows = {row["b"]: row for row in result["branch_rational_coefficients"]}
    require(set(rows) == set(BRANCHES), "kernel branches")
    for root, row in rows.items():
        scale = row["common_scale"]
        require(scale["numerator"] == "t**14 - 2*t**10 + t**6",
                "common scale numerator")
        require(scale["numerator_degree"] == 14 and
                scale["denominator_degree"] == 6, "common scale degrees")
        normalized = row["normalized_coefficients"]
        require(set(normalized) ==
                {"a20", "a21", "a22", "a00", "a01", "a02", "b10", "b11"},
                "coefficient names")
        require(max(value["degree"] for value in normalized.values()) <= 8,
                "normalized degree")
        scalar = 759420084 if root == 583634934 else 234633685
        t = sp.symbols("t")
        expected_b10 = sp.Poly(
            scalar * t**2 * (t**2 - 1) * (t**4 + 1), t,
            modulus=2130706433,
        )
        expected_b11 = sp.Poly(
            -scalar * (t**2 - 1) * (t**4 + 1), t,
            modulus=2130706433,
        )
        observed_b10 = sp.Poly(sp.sympify(normalized["b10"]["polynomial"]),
                               t, modulus=2130706433)
        observed_b11 = sp.Poly(sp.sympify(normalized["b11"]["polynomial"]),
                               t, modulus=2130706433)
        require(observed_b10 == expected_b10 and observed_b11 == expected_b11,
                "B1 factor")


def verify_pair(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1a-cell0-generic-signed-pair-v1",
            "pair schema")
    rows = {row["b"]: row for row in payload["rows"]}
    require(set(rows) == set(BRANCHES), "pair branches")
    transcript = (
        "BEGIN_LOCALIZED\n-1\n1\nUNIT=1\nEND_LOCALIZED\n"
        "BEGIN_PROJECTED\n-1\n1\nE[1]=1\nEND_PROJECTED\n"
    )
    for root, row in rows.items():
        require(row["status"] == "COMPLETE" and row["unit"] is True,
                "pair unit")
        require(row["c_gcd_degree"] == 0, "c chart coverage")
        require(row["equation_shape"] == [
            {"degree": 20, "terms": 55},
            {"degree": 40, "terms": 305},
        ], "pair shapes")
        require(row["guard_shape"] == {"degree": 97, "terms": 2072},
                "guard shape")
        require(row["program_sha256"] == PROGRAMS[root], "program hash")
        require(row["stdout"] == transcript and row["stderr"] == "",
                "pair transcript")


def verify_formal_pair_identity():
    d, e, d0, d1 = sp.symbols("d e d0 d1")
    n0 = d * e * d0
    n1 = -d * e * d1
    q0 = -(d + e) * d0
    q1 = -(d - e) * d1
    cuts = (
        n1 * d0 + n0 * d1,
        q0**2 * d1**2 - q1**2 * d0**2 - 4 * n0 * d0 * d1**2,
    )
    require(all(sp.expand(value) == 0 for value in cuts), "formal pair identity")


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("cell-0 root-sign orbit is empty" in statement, "closure")
    require("Six common symmetry" in statement and "40 raw rows" in statement,
            "remaining frontier")
    require("nonclaim" in contract, "scope fence")

    for path, expected_hash in HASHES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected_hash,
                f"artifact hash {path.name}")
    verify_kernel(json.loads(KERNEL.read_text()))
    verify_pair(json.loads(PAIR.read_text()))
    verify_formal_pair_identity()
    t2 = json.loads(T2.read_text())
    require(all(row["unit"] is True and row["status"] == "COMPLETE"
                for row in t2["rows"]), "t2 audit")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    parents = (
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_kernel_uniqueness",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_quadratic_paired_product_resultant_interface",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell0_common_lex_rational_witness",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1a cell-0 generic signed-pair orbit exclusion verified")


if __name__ == "__main__":
    main()
