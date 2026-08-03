#!/usr/bin/env python3
"""Verify the positive 433-1b cell-3 global quadratic quotient."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_birational_profile_modal.py"
RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_birational_profile_result.json"
PRODUCT = EXPERIMENTS / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_compact_curve_kernel"
PINNED = {
    SCRIPT: "d45a3f7cec511b8544ae08b352af8985008ee5c89583abfa52b37f55377b68c0",
    RESULT: "af991fd4b8c2bae2544a5d656f55fecc734b643da58c6f207db54760dad20c46",
}
BASIS_SHAPES = (
    ((0, 0, 3, 4), 6, 14),
    ((0, 2, 2, 6), 8, 22),
    ((0, 2, 1, 5), 7, 16),
    ((0, 2, 2, 4), 7, 17),
    ((0, 2, 3, 5), 8, 29),
    ((1, 1, 2, 7), 8, 34),
    ((1, 1, 1, 2), 3, 6),
    ((1, 2, 2, 6), 7, 36),
    ((2, 2, 2, 6), 7, 43),
    ((4, 4, 2, 9), 11, 81),
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-birational-profile-v1",
            "schema")
    require(payload["source_product_sha256"] == digest(PRODUCT),
            "source-product custody")
    require("no birationality" in payload["scope"], "scope nonclaim")
    expected = set(itertools.product((-1, 1), (-1, 1), range(6)))
    actual = set()
    bases = {}
    interfaces = {}
    programs = set()
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        key = (*signs, row["chart"])
        require(key not in actual, "duplicate row")
        actual.add(key)
        require(row["status"] == "COMPLETE" and row["dimension"] == 1 and
                row["basis_size"] == 10 and not row["stderr"],
                "complete dimension-one basis")
        shape = tuple((tuple(item["degrees"]), item["total_degree"],
                       item["terms"]) for item in row["basis"])
        require(shape == BASIS_SHAPES, "block-lex basis shapes")
        require(row["c_boundary_unit"] and
                (row["c_boundary_dimension"], row["c_boundary_size"]) ==
                (-1, 1), "c denominator unit")
        require(row["b_boundary_unit"] and
                (row["b_boundary_dimension"], row["b_boundary_size"]) ==
                (-1, 1), "b leading coefficient unit")
        require(row["quotient_dimension"] == 1 and
                row["quotient_basis_size"] == 10 and
                row["quotient_exact"] and
                row["quotient_remainders"] == ["0"] * 10,
                "exact saturated quotient")

        interface = row["quotient_interface"]
        require(interface["base_relation"] == row["basis"][0] and
                interface["b_relation"] == row["basis"][2] and
                interface["c_relation"] == row["basis"][6],
                "selected basis interface")
        require((interface["base_relation"]["total_degree"],
                 interface["base_relation"]["terms"]) == (6, 14) and
                (interface["b_relation"]["total_degree"],
                 interface["b_relation"]["terms"]) == (7, 16) and
                (interface["c_relation"]["total_degree"],
                 interface["c_relation"]["terms"]) == (3, 6),
                "interface shapes")
        require(interface["b_palindromic"] and
                interface["b_leading_expected"] and
                interface["c_denominator_expected"],
                "interface coefficient checks")

        epsilon_1, epsilon_2 = signs
        b_expanded = (
            f"{'' if epsilon_2 == 1 else '-'}16711679*r**3 + r**2*t"
        )
        b_factored = (
            f"r**2*({'16711679' if epsilon_2 == 1 else '-16711679'}*r + t)"
        )
        c_denominator = (
            "-r**2 + t" if epsilon_1 * epsilon_2 == 1 else "r**2 + t"
        )
        require(row["b_leading"] == b_factored and
                interface["b_leading"]["expression"] == b_expanded and
                interface["b_constant"]["expression"] == b_expanded,
                "palindromic leading formula")
        require(row["c_denominator"] == c_denominator and
                interface["c_denominator"]["expression"] == c_denominator,
                "c recovery formula")

        basis_key = canonical(row["basis"])
        interface_key = canonical(interface)
        require(signs not in bases or bases[signs] == basis_key,
                "chart-dependent basis")
        require(signs not in interfaces or interfaces[signs] == interface_key,
                "chart-dependent interface")
        bases[signs] = basis_key
        interfaces[signs] = interface_key
        require(row["program_sha256"], "program transcript")
        programs.add(row["program_sha256"])
    require(actual == expected, "24-chart Cartesian cover")
    require(len(bases) == 4 and len(interfaces) == 4, "four sign rows")
    require(len(programs) == 24, "24 specialized programs")


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
    verify_payload(json.loads(RESULT.read_text()))
    verify_dag()
    print("cell=3 charts=24 quotient=quadratic exact_reductions=240")


if __name__ == "__main__":
    main()
