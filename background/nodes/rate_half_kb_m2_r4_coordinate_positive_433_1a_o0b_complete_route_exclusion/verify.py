#!/usr/bin/env python3
"""Verify exhaustive closure of the positive 433-1a to O0b route."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "o0b_complete_route_exclusion"
)
ATLAS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "o0b_signed_edge_atlas"
)
QUOTIENT = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "common_root_sign_symmetry_quotient"
)
COVERAGE = (
    ("rate_half_kb_m2_r4_coordinate_positive_433_1a_cell0_generic_signed_pair_orbit_exclusion", (0,), 4, 1),
    ("rate_half_kb_m2_r4_coordinate_positive_433_1a_cell1_2_common_root_sign_orbit_exclusion", (1, 2), 8, 2),
    ("rate_half_kb_m2_r4_coordinate_positive_433_1a_cell3_signed_pair_guard_factorization_exclusion", (3, 6), 8, 1),
    ("rate_half_kb_m2_r4_coordinate_positive_433_1a_cell4_main_projection_guard_factorization_exclusion", (4, 7), 8, 1),
    ("rate_half_kb_m2_r4_coordinate_positive_433_1a_cell58_complete_root_sign_orbit_exclusion", (5, 8), 8, 1),
    ("rate_half_kb_m2_r4_coordinate_positive_433_1a_cell9_signed_pair_guard_factorization_exclusion", (9, 10), 8, 1),
    ("rate_half_kb_m2_r4_coordinate_positive_433_1a_cell11_signed_pair_guard_factorization_exclusion", (11,), 4, 1),
    ("rate_half_kb_m2_r4_coordinate_positive_433_1a_cell12_signed_pair_guard_factorization_exclusion", (12, 13), 8, 1),
    ("rate_half_kb_m2_r4_coordinate_positive_433_1a_cell14_signed_pair_guard_factorization_exclusion", (14,), 4, 1),
)
CLOSURE_MARKERS = {
    COVERAGE[0][0]: "cell-0 root-sign orbit is empty",
    COVERAGE[1][0]: "all eight common rows in those cells are empty",
    COVERAGE[2][0]: "orbit `[3,6]` is PROVED excluded",
    COVERAGE[3][0]: "orbit `[4,7]` is PROVED excluded",
    COVERAGE[4][0]: "proves all eight rows",
    COVERAGE[5][0]: "orbit `[9,10]` is PROVED excluded",
    COVERAGE[6][0]: "orbit `[11]` is PROVED excluded",
    COVERAGE[7][0]: "orbit `[12,13]` is PROVED excluded",
    COVERAGE[8][0]: "orbit\n`[14]` is PROVED excluded",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_coverage(coverage):
    cells = [cell for _, orbit, _, _ in coverage for cell in orbit]
    require(sorted(cells) == list(range(15)) and len(cells) == len(set(cells)),
            "cell coverage")
    require(sum(rows for _, _, rows, _ in coverage) == 60,
            "raw-row coverage")
    require(sum(reps for _, _, _, reps in coverage) == 10,
            "representative coverage")
    expected_rows = {1 if len(orbit) == 1 else 2: 4 if len(orbit) == 1 else 8
                     for _, orbit, _, _ in coverage}
    require(expected_rows == {1: 4, 2: 8}, "orbit row arity")
    for _, orbit, rows, reps in coverage:
        require(rows == 4 * len(orbit), "orbit raw-row count")
        require(reps == (2 if orbit == (1, 2) else 1),
                "orbit representative count")


def main():
    verify_coverage(COVERAGE)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "aggregate DAG status")
    parents = (ATLAS, QUOTIENT) + tuple(row[0] for row in COVERAGE)
    for parent in parents:
        require(parent in nodes and nodes[parent]["status"] == "PROVED",
                f"PROVED dependency {parent}")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency edge {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")

    atlas = ROOT / "background/nodes" / ATLAS / "statement.md"
    quotient = ROOT / "background/nodes" / QUOTIENT / "statement.md"
    atlas_text = atlas.read_text()
    quotient_text = quotient.read_text()
    require("exactly two signed lanes" in atlas_text and
            "- **status:** PROVED" in atlas_text, "signed-lane atlas")
    require("all 60 common matching/root-sign rows" in quotient_text and
            "exactly ten algebraically distinct" in quotient_text and
            "- **status:** PROVED" in quotient_text, "common-row quotient")

    for node_id, _, _, _ in COVERAGE:
        statement = (ROOT / "background/nodes" / node_id / "statement.md")
        text = statement.read_text()
        require("- **status:** PROVED" in text, f"statement status {node_id}")
        require(CLOSURE_MARKERS[node_id] in text,
                f"statement closure marker {node_id}")

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement and
            "route `433-1a -> O0b` is empty" in statement,
            "aggregate statement")
    require("60 raw rows" in contract and "ten algebraic representatives"
            in contract and "No other coordinate route" in contract,
            "aggregate contract")
    print("positive 433-1a to O0b complete route exclusion verified")


if __name__ == "__main__":
    main()
