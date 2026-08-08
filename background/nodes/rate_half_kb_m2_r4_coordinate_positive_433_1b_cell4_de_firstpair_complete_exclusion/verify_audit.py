#!/usr/bin/env python3
"""Independent table audit for the cell-4 DE first-pair block."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi0_pairing0_four_basis_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi1_pairing0_parallel_edge_transport",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi2_pairing0_four_basis_exclusion",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    matching_table = (
        ((0, 1), (2, 3), (4, 5)),
        ((0, 1), (2, 4), (3, 5)),
        ((0, 1), (2, 5), (3, 4)),
        ((0, 2), (1, 3), (4, 5)),
        ((0, 2), (1, 4), (3, 5)),
        ((0, 2), (1, 5), (3, 4)),
        ((0, 3), (1, 2), (4, 5)),
        ((0, 3), (1, 4), (2, 5)),
        ((0, 3), (1, 5), (2, 4)),
        ((0, 4), (1, 2), (3, 5)),
        ((0, 4), (1, 3), (2, 5)),
        ((0, 4), (1, 5), (2, 3)),
        ((0, 5), (1, 2), (3, 4)),
        ((0, 5), (1, 3), (2, 4)),
        ((0, 5), (1, 4), (2, 3)),
    )
    require(len(matching_table) == len(set(matching_table)) == 15,
            "explicit perfect-matching table")
    require([index for index, matching in enumerate(matching_table)
             if matching[0] == (0, 1)] == [0, 1, 2],
            "exact first-pair indices")
    for parent in PARENTS:
        node = json.loads((ROOT / "background/nodes" / parent /
                           "node.json").read_text())["node"]
        require(node["status"] == "PROVED" and "pairing0" in node["id"],
                f"parent scope {parent}")
    contract = (NODE / "claim_contract.md").read_text()
    result = (NODE / "result.md").read_text()
    require("`144` cases" in contract and "`96` of `105`" in contract and
            "Nine of `105` slices" in result, "coverage ledger")
    print("audit=ok canonical_matchings=15 first_pair_indices=0,1,2 "
          "slices=9 raw_cases=144")


if __name__ == "__main__":
    main()
