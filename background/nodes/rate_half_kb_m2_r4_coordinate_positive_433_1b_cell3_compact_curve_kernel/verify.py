#!/usr/bin/env python3
"""Verify the positive 433-1b cell-3 compact curve and kernel theorem."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
STRUCTURE_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_compact_structure_modal.py"
STRUCTURE_RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_compact_structure_result.json"
PROFILE_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_projection_profile_modal.py"
PROFILE_RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_projection_profile_result.json"
KERNEL_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_compact_kernel_modal.py"
KERNEL_RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
PRODUCT = EXPERIMENTS / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
PINNED = {
    STRUCTURE_SCRIPT: "a59823c43f5305baa22ea7435084b82a7dfc29cf7a70ffc3eaeec07e2c382998",
    STRUCTURE_RESULT: "2f8712f2a942bb46f153d5204c4f4c8f9bff08336c295db4f31aef10fb5d22b7",
    PROFILE_SCRIPT: "d5cbd41bead5e0db2895c944868101b6acf3a665d87b084063d27fb3409f78a9",
    PROFILE_RESULT: "06b08bc7f10228b4875d53e677414970be7af9d73aec141f5b9a1f8b1a63398b",
    KERNEL_SCRIPT: "bb0a4db8d407e910dd941867b5933c6d1b5d10e3530c805178636172b9da6515",
    KERNEL_RESULT: "e20ccb714b252f00ee3ce877ee68eff032f43deb877e2097919151436ddcf789",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_common_exception_classifier",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_structure(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-compact-structure-v1",
            "structure schema")
    require(payload["field"] == 2130706433 and
            payload["source_product_sha256"] == digest(PRODUCT),
            "structure custody")
    expected = set(itertools.product((-1, 1), (-1, 1), range(6)))
    actual = set()
    signatures = {}
    shapes = {
        "etr": (6, 14), "erb": (16, 58),
        "ebt": (19, 106), "erc": (13, 49),
    }
    for row in payload["rows"]:
        key = (*row["epsilon"], row["chart"])
        require(key not in actual, "duplicate structure row")
        actual.add(key)
        require(row["status"] == "COMPLETE" and row["dimension"] == 1 and
                row["basis_size"] == 21, "common curve")
        require(row["beta_boundary_unit"] and
                row["beta_boundary_dimension"] == -1 and
                row["beta_boundary_size"] == 1, "open beta boundary")
        projection_signature = []
        for name, shape in shapes.items():
            require(row["projection_dimensions"][name] == 3 and
                    row["projection_sizes"][name] == 1,
                    f"{name} projection dimension")
            require(len(row["projections"][name]) == 1, f"{name} relation")
            relation = row["projections"][name][0]
            require((relation["degree"], relation["terms"]) == shape,
                    f"{name} shape")
            projection_signature.append(relation["sha256"])
        signs = tuple(row["epsilon"])
        signature = tuple(projection_signature)
        require(signs not in signatures or signatures[signs] == signature,
                "chart projection mismatch")
        signatures[signs] = signature
        require(not row["stderr"] and row["program_sha256"],
                "structure transcript")
    require(actual == expected and len(signatures) == 4, "24-chart cover")
    return signatures


def verify_profile(payload, signatures):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-projection-profile-v1",
            "profile schema")
    require(payload["source_structure_sha256"] == digest(STRUCTURE_RESULT),
            "profile custody")
    result = payload["result"]
    require(result["status"] == "COMPLETE" and result["field"] == 2130706433,
            "profile status")
    actual = set()
    for row in result["rows"]:
        signs = tuple(row["epsilon"])
        require(signs in signatures and signs not in actual, "profile signs")
        actual.add(signs)
        for name, value in row["projections"].items():
            factors = value["factorization"]["factors"]
            require(len(factors) == 1 and factors[0]["multiplicity"] == 1,
                    f"{name} irreducible")
            if name == "etr":
                require(value["reciprocal"] is None, "etr reciprocal scope")
            else:
                require(value["reciprocal"]["palindromic"] and
                        value["reciprocal"]["exact_reconstruction"],
                        f"{name} reciprocal")
    require(actual == set(signatures), "four profile rows")


def verify_kernel(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-compact-kernel-v1",
            "kernel schema")
    require(payload["field"] == 2130706433 and
            payload["source_product_sha256"] == digest(PRODUCT) and
            payload["source_structure_sha256"] == digest(STRUCTURE_RESULT),
            "kernel custody")
    expected = set(itertools.product((-1, 1), (-1, 1)))
    actual = set()
    kernel_digests = set()
    shapes = ((15, 24), (14, 26), (12, 24), (16, 24),
              (16, 26), (14, 24), (14, 48), (14, 48))
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs not in actual, "duplicate kernel row")
        actual.add(signs)
        require(row["status"] == "COMPLETE" and
                row["all_rows_zero_mod_common"], "kernel completion")
        require(tuple((value["degree"], value["terms"])
                      for value in row["kernel"]) == shapes, "kernel shapes")
        require(row["identically_zero_rows"] == [True] * 7 + [False] * 3,
                "identical row ledger")
        require(row["reduced_remainders"] == ["0"] * 10,
                "ten zero reductions")
        require(row["common_dimension"] == 2 and
                row["common_basis_size"] == 87 and not row["stderr"],
                "kernel reduction transcript")
        require(row["final_kernel_removed_gcd"]["degree"] == 3 and
                row["final_kernel_removed_gcd"]["terms"] == 2,
                "kernel gcd")
        kernel_digests.add(tuple(value["sha256"] for value in row["kernel"]))
    require(actual == expected and len(kernel_digests) == 1,
            "four identical kernels")


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
    signatures = verify_structure(json.loads(STRUCTURE_RESULT.read_text()))
    verify_profile(json.loads(PROFILE_RESULT.read_text()), signatures)
    verify_kernel(json.loads(KERNEL_RESULT.read_text()))
    verify_dag()
    print("cell=3 charts=24 curve_dim=1 beta_boundary=unit kernels=4 rows=40")


if __name__ == "__main__":
    main()
