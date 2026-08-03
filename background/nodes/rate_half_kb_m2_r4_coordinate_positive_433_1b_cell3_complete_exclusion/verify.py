#!/usr/bin/env python3
"""Verify the complete deployed positive 433-1b role-cell-3 aggregation."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
CONSUMER = "rate_half_band_closure"
RANK_DROP = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "product_rankdrop_common_exception_classifier"
)
DE_FIRST = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell3_de_firstpair_complete_exclusion"
)
DE_PAIRINGS = {
    matching: (
        "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
        f"cell3_de_pairing{matching}_complete_exclusion"
    )
    for matching in range(3, 15)
}
XI3_BLOCKS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi3_pairing0_reciprocal_square_exclusion": {0},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi3_pairings1_2_reciprocal_linear_exclusion": {1, 2},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi3_opposite_de_pairings3_6_exclusion": {3, 6},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi3_fully_mixed_pairings11_14_exclusion": {11, 14},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi3_fully_mixed_pairings7_8_10_13_exclusion": {7, 8, 10, 13},
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi3_opposite_de_pairings4_5_9_12_exclusion": {4, 5, 9, 12},
}
XI4 = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell3_xi4_xi3_outside_role_transport_exclusion"
)
XI5 = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell3_xi5_finite_source_pairing_exclusion"
)
XI6 = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_"
    "cell3_xi6_endpoint_compatibility_exclusion"
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def cases(xi_values, matching_values):
    return {
        (xi, matching, epsilon_1, epsilon_2, sigma_c, sigma_o)
        for xi in xi_values
        for matching in matching_values
        for epsilon_1, epsilon_2 in itertools.product((-1, 1), repeat=2)
        for sigma_c, sigma_o in itertools.product((-1, 1), repeat=2)
    }


def main():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}

    dependency_cover = {
        DE_FIRST: cases(range(3), range(3)),
        **{
            dependency: cases(range(3), {matching})
            for matching, dependency in DE_PAIRINGS.items()
        },
        **{
            dependency: cases({3}, matchings)
            for dependency, matchings in XI3_BLOCKS.items()
        },
        XI4: cases({4}, range(15)),
        XI5: cases({5}, range(15)),
        XI6: cases({6}, range(15)),
    }
    dependencies = {RANK_DROP, *dependency_cover}
    require(nodes[NODE_ID]["status"] == "PROVED", "proved aggregate")
    for dependency in dependencies:
        require(nodes[dependency]["status"] == "PROVED", f"proved {dependency}")
        require((dependency, NODE_ID, "req") in edges, f"required {dependency}")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer evidence edge")

    union = set()
    for dependency, supplied in dependency_cover.items():
        require(not (union & supplied), f"overlap at {dependency}")
        union |= supplied
    expected = cases(range(7), range(15))
    require(union == expected, "complete principal Cartesian cover")
    require(len(expected) == 1680, "principal case count")
    require(sum(len(value) for value in dependency_cover.values()) == 1680,
            "disjoint payment count")
    require(len(cases(range(3), range(15))) == 720, "parallel DE payment")
    require(all(len(cases({xi}, range(15))) == 240 for xi in range(3, 7)),
            "single-xi payments")

    rank_statement = (
        ROOT / f"background/nodes/{RANK_DROP}/statement.md"
    ).read_text()
    require("0, 1, 2, 3, 6" in rank_statement and "unit ideal" in rank_statement,
            "cell-3 rank-drop exclusion")
    statement = (NODE / "statement.md").read_text()
    require("principal total" in statement and "= 1680 cases" in statement,
            "printed aggregate ledger")
    print(
        "cell=3 rank_drop=empty principal_cases=1680 "
        "parallel_de=720 xi3=240 xi4=240 xi5=240 xi6=240 complete=yes"
    )


if __name__ == "__main__":
    main()
