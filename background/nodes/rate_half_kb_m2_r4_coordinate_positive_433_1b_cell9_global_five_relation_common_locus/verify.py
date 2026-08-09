#!/usr/bin/env python3
"""Verify the positive 433-1b cell-9 global common-locus theorem."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "scout_script": "rate_half_kb_positive_433_1b_remaining_compact_pivot_scout_modal.py",
    "structure": "rate_half_kb_positive_433_1b_cell9_sign_structure_result.json",
    "subset_script": "rate_half_kb_positive_433_1b_cell9_lex_subset_scout_modal.py",
    "subset": "rate_half_kb_positive_433_1b_cell9_lex_subset_scout_result.json",
    "global_script": "rate_half_kb_positive_433_1b_cell9_global_common_modal.py",
    "global": "rate_half_kb_positive_433_1b_cell9_global_common_result.json",
}
PATHS = {key: EXP / value for key, value in FILES.items()}
PINNED = {
    "scout_script": "0f77351384d69fc31d212569b94d414fcfd8dc2b4cbd7970db86d4d0fb13095b",
    "structure": "744a857618f985ac6b1ed310a8c86693344ae441367f1be3c4aa1093d5433b14",
    "subset_script": "f3df09c885bd32c1853663b3275265416c9409725bc69d3410d997fc736aeea2",
    "subset": "8516d4134ce194c50605a4d5a2e6f1faacbc7925ebaa6523881a4ceffb965422",
    "global_script": "ea418fc6c238d75168eb627ed86ebfa369c7bc86d4721bf36c14e0bb643b9338",
    "global": "dd5b63d70f0263a11d5b29fcf06486adf6e925e528c16727c85daedc2775e903",
}
COMMON = EXP / "rate_half_kb_positive_433_1b_common_vieta_compiler.py"
PRODUCT = EXP / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_common_exception_classifier",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_complete_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
)
PRIME = 2130706433
SIGNS = set(itertools.product((-1, 1), repeat=2))
MINIMAL = {
    (0, 1, 3, 4, 6),
    (0, 1, 3, 5, 6),
    (0, 1, 4, 5, 6),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_structure(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-compact-pivot-scout-v3",
            "structure schema")
    require(payload["field"] == PRIME and payload["complete"] and
            payload["expected_rows"] == 4 and
            payload["source_common_sha256"] == digest(COMMON) and
            payload["source_product_sha256"] == digest(PRODUCT),
            "structure custody")
    signatures = {}
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs in SIGNS and signs not in signatures, "structure key")
        require(row["cell"] == 9 and row["chart"] == 1 and row["pivot"] == 1
                and row["status"] == "COMPLETE" and row["dimension"] == 1
                and row["basis_size"] == 17 and row["lex_basis_size"] == 7,
                "structure dimensions")
        require(row["pivot_boundary_unit"] and
                row["pivot_boundary_dimension"] == -1 and
                row["pivot_boundary_size"] == 1, "structure pivot")
        require(len(row["lex_basis"]) == 7 and not row["stderr"],
                "structure transcript")
        signatures[signs] = tuple(item["sha256"] for item in row["lex_basis"])
    require(set(signatures) == SIGNS, "four structure rows")
    return signatures


def verify_subsets(payload, signatures):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell9-lex-subset-scout-v1" and
            payload["field"] == PRIME and
            payload["source_sha256"] == digest(PATHS["structure"]),
            "subset custody")
    expected_subsets = {
        (0, 1, *tail)
        for size in range(1, 5)
        for tail in itertools.combinations(range(2, 7), size)
    }
    actual = set()
    exact = {signs: set() for signs in SIGNS}
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        indices = tuple(row["indices"])
        key = (signs, indices)
        require(signs in SIGNS and indices in expected_subsets and
                key not in actual, "subset key")
        actual.add(key)
        remainders = row["remainders"]
        require(row["status"] == "COMPLETE" and len(remainders) == 7 and
                [item["index"] for item in remainders] == list(range(7)) and
                not row["stderr"], "subset transcript")
        replay_exact = all(item["expression"] == "0" for item in remainders)
        require(row["exact"] == replay_exact, "subset exactness flag")
        if replay_exact:
            exact[signs].add(indices)
    require(len(actual) == 120, "120 subset rows")
    for signs in SIGNS:
        require({row for row in exact[signs] if len(row) == 5} == MINIMAL,
                "five-relation presentations")
        require(not any(len(row) < 5 for row in exact[signs]),
                "smaller tested presentation")
        expected_digest = hashlib.sha256(
            "\n".join(
                item["expression"] for item in next(
                    row for row in json.loads(PATHS["structure"].read_text())["rows"]
                    if tuple(row["epsilon"]) == signs
                )["lex_basis"]
            ).encode()
        ).hexdigest()
        require(payload["basis_sha256"][str(signs)] == expected_digest and
                len(signatures[signs]) == 7, "subset basis custody")


def verify_global(payload, signatures):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell9-global-common-v1" and
            payload["field"] == PRIME and payload["cell"] == 9 and
            payload["pivot"] == 1 and
            payload["source_common_sha256"] == digest(COMMON) and
            payload["source_product_sha256"] == digest(PRODUCT) and
            payload["source_structure_sha256"] == digest(PATHS["structure"]),
            "global custody")
    actual = set()
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs in SIGNS and signs not in actual, "global key")
        actual.add(signs)
        require(row["status"] == "COMPLETE" and row["dimension"] == 1 and
                row["basis_size"] == 17 and row["lex_basis_size"] == 7 and
                row["pivot_boundary_unit"] and row["ideals_equal"],
                "global common ledger")
        require(row["global_in_chart_remainders"] == ["0"] * 7 and
                row["chart_in_global_remainders"] == ["0"] * 7 and
                not row["stderr"], "mutual containment")
        require(tuple(item["sha256"] for item in row["lex_basis"]) ==
                signatures[signs], "global/chart lex equality")
    require(actual == SIGNS, "four global rows")


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
    for key, expected in PINNED.items():
        require(digest(PATHS[key]) == expected, f"digest {FILES[key]}")
    structure = json.loads(PATHS["structure"].read_text())
    signatures = verify_structure(structure)
    verify_subsets(json.loads(PATHS["subset"].read_text()), signatures)
    verify_global(json.loads(PATHS["global"].read_text()), signatures)
    verify_dag()
    print("cell=9 signs=4 global_chart_equal=4 five_relation_presentations=12")


if __name__ == "__main__":
    main()
