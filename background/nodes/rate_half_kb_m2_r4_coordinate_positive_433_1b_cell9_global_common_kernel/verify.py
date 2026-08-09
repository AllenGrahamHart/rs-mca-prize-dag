#!/usr/bin/env python3
"""Verify the positive 433-1b cell-9 global coefficient kernel."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXP / "rate_half_kb_positive_433_1b_cell9_compact_kernel_modal.py"
RESULT = EXP / "rate_half_kb_positive_433_1b_cell9_compact_kernel_result.json"
COMMON = EXP / "rate_half_kb_positive_433_1b_common_vieta_compiler.py"
PRODUCT = EXP / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
STRUCTURE = EXP / "rate_half_kb_positive_433_1b_cell9_global_common_result.json"
PINNED = {
    SCRIPT: "34becb0d776f8238e37e953c0fe7c37cce7fdd2140e70fea79ca0de87733492a",
    RESULT: "725b81912d1999314eeef826355b2de35c22d01e956e27bbf4bed5b980d9d0bd",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell9_global_five_relation_common_locus",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
)
PRIME = 2130706433


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell9-compact-kernel-v1" and
            payload["field"] == PRIME and payload["cell"] == 9 and
            payload["pivot"] == 1, "payload identity")
    require(payload["source_common_sha256"] == digest(COMMON) and
            payload["source_product_sha256"] == digest(PRODUCT) and
            payload["source_structure_sha256"] == digest(STRUCTURE),
            "source custody")
    expected = set(itertools.product((-1, 1), repeat=2))
    actual = set()
    kernels = {}
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs in expected and signs not in actual, "sign key")
        actual.add(signs)
        require(row["status"] == "COMPLETE" and
                row["pivot_label"] == PRIME - 1 and
                row["pivot_scale"] == PRIME - 2 and
                row["product_kernel_removed_gcd"]["expression"] == "1" and
                row["final_kernel_removed_gcd"]["expression"] == "1",
                "primitive pivot ledger")
        require(len(row["kernel"]) == 8 and
                [[item["degree"], item["terms"]] for item in row["kernel"]] ==
                [[14, 38], [13, 37], [11, 38], [15, 38],
                 [15, 37], [13, 38], [15, 66], [15, 66]],
                "kernel shape")
        require(row["identically_zero_rows"] ==
                [True] * 7 + [False] * 3 and
                row["remainders"] == ["0"] * 10 and row["all_rows_zero"],
                "row annihilation")
        require(row["common_dimension"] == 1 and
                row["common_basis_size"] == 40 and
                len(row["lex_signature"]) == 7 and
                row["program_sha256"] and not row["stderr"],
                "localized transcript")
        kernels[signs] = tuple(item["sha256"] for item in row["kernel"])
    require(actual == expected, "four sign rows")

    first_six = {signature[:6] for signature in kernels.values()}
    require(len(first_six) == 1, "product coordinates depend on signs")
    for first_sign in (-1, 1):
        require(kernels[(first_sign, -1)] == kernels[(first_sign, 1)],
                "second-sign dependence")
    require(kernels[(-1, -1)][6:] == tuple(reversed(kernels[(1, -1)][6:])),
            "first-sign final-coordinate exchange")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "DAG parents")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG consumer")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    verify_payload(json.loads(RESULT.read_text()))
    verify_dag()
    print("cell=9 signs=4 kernel_coordinates=8 formal_rows=7 reduced_rows=3")


if __name__ == "__main__":
    main()
