#!/usr/bin/env python3
"""Verify the exact 105-label cell-12 assembly."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PREFIX = "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell12_"
RATIONAL = PREFIX + "rational_boundary_complete_exclusion"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def block(xis, pairings):
    return {(xi, pairing) for xi in xis for pairing in pairings}


def main():
    groups = {
        PREFIX + "endpoint_roles_complete_exclusion": block((5, 6), range(15)),
        PREFIX + "parallel_de_first_pair_complete_exclusion": block((0, 1, 2), range(3)),
        PREFIX + "parallel_de_pairing3_6_nested_quadratic_exclusion": block((0, 1, 2), (3, 6)),
        PREFIX + "parallel_de_pairing4_7_9_10_nested_quadratic_exclusion": (
            block((0, 1), (4, 7)) | block((2,), (4, 7, 9, 10))
        ),
        PREFIX + "parallel_de_pairing5_8_12_13_nested_quadratic_exclusion": (
            block((0, 1), (5, 8)) | block((2,), (5, 8, 12, 13))
        ),
        PREFIX + "positive_de_pairing9_10_nested_quadratic_exclusion": block((0, 1), (9, 10)),
        PREFIX + "positive_de_pairing12_13_nested_quadratic_exclusion": block((0, 1), (12, 13)),
        PREFIX + "parallel_de_pairing11_14_common_f_resultant_exclusion": (
            block((0, 1), (11,)) | block((2,), (11, 14))
        ),
        PREFIX + "positive_de_pairing14_common_f_resultant_exclusion": block((0, 1), (14,)),
        PREFIX + "xi3_pairing0_reciprocal_square_exclusion": block((3, 4), (0,)),
        PREFIX + "xi3_pairings1_2_reciprocal_linear_exclusion": block((3, 4), (1, 2)),
        PREFIX + "xi3_xi4_pairing3_6_reciprocal_square_exclusion": block((3, 4), (3, 6)),
        PREFIX + "xi3_xi4_pairing4_9_nested_signfree_exclusion": block((3, 4), (4, 9)),
        PREFIX + "xi3_xi4_pairing5_12_nested_signfree_exclusion": block((3, 4), (5, 12)),
        PREFIX + "xi3_xi4_pairing7_10_quadratic_resultant_exclusion": block((3, 4), (7, 10)),
        PREFIX + "xi3_xi4_pairing8_13_quadratic_resultant_exclusion": block((3, 4), (8, 13)),
        PREFIX + "xi3_xi4_pairing11_14_quadratic_resultant_exclusion": block((3, 4), (11, 14)),
    }
    require(len(groups) == 17, "17 label suppliers")
    seen = set()
    for node_id, labels in groups.items():
        require(not seen & labels, f"disjoint supplier {node_id}")
        seen |= labels
        manifest = json.loads((ROOT / "background/nodes" / node_id / "node.json").read_text())["node"]
        require(manifest["id"] == node_id and manifest["status"] == "PROVED",
                f"proved supplier {node_id}")
    require(seen == block(range(7), range(15)) and len(seen) == 105,
            "complete 105-label union")
    require(sum(len(labels) for labels in groups.values()) == 105,
            "disjoint label census")
    rational = json.loads((ROOT / "background/nodes" / RATIONAL / "node.json").read_text())["node"]
    require(rational["status"] == "PROVED" and "all 105 outside labels" in rational["closure"],
            "rational-boundary parent")
    own = json.loads((NODE / "node.json").read_text())
    required = {item["from"] for item in own["requires"]}
    require(required == set(groups) | {RATIONAL}, "manifest parent cover")
    require(own["node"]["status"] == "PROVED", "assembly status")
    print("PASS cell-12 assembly: suppliers=17 labels=105 boundary=PROVED")


if __name__ == "__main__":
    main()
