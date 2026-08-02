#!/usr/bin/env python3
"""Verify the positive 433-1b product-rank-drop common classifier."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler"
FILES = {
    "product_compiler": (
        "rate_half_kb_positive_433_1b_product_base_rank_compiler.py",
        "254a30a9b65d939190e1b85340131f7749f4c8fe65eff8ac180904a78f28eddc",
    ),
    "product_launcher": (
        "rate_half_kb_positive_433_1b_product_base_rank_compiler_modal.py",
        "2f372a5e9c4c2e674c218871d4e51581bc9c7cbab37a16fc2f4e483289b091bb",
    ),
    "product_result": (
        "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json",
        "ee4dcb25877e9101a544ee5896b9bf6890059d6398c78d7562127b0d1c53c293",
    ),
    "common_launcher": (
        "rate_half_kb_positive_433_1b_product_rankdrop_common_exact_modal.py",
        "f6c3f269f789011111b68f683557a9529a89a5ed3abdc003dbf50a942e1268d7",
    ),
    "common_result": (
        "rate_half_kb_positive_433_1b_product_rankdrop_common_exact_result.json",
        "8a9f2a4998b91c683b6ab19076fca72a36edc21696b2caa40f918680cb8525a8",
    ),
}
EMPTY_CELLS = {0, 1, 2, 3, 6}
SURVIVOR_SIZES = {
    4: 11, 5: 11, 7: 11, 8: 11,
    9: 21, 10: 21, 11: 21,
    12: 18, 13: 18, 14: 15,
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-rankdrop-common-exact-v2",
            "schema")
    require(payload["source_common_sha256"] ==
            "a956656cba6c884bae665a2439666964ed468dcf9d0466e80cb825e811a6f845",
            "common source custody")
    require(payload["source_product_sha256"] == FILES["product_result"][1],
            "product source custody")
    expected = set(itertools.product(range(15), (-1, 1), (-1, 1)))
    actual = set()
    for row in payload["rows"]:
        require(row["status"] == "COMPLETE", "incomplete row")
        case = (row["cell"], *row["epsilon"])
        require(case not in actual, "duplicate row")
        actual.add(case)
        require(row["minor_count"] == 45, "full minor count")
        require(len(row["program_sha256"]) == 64, "program custody")
        require("END_COMMON" in row["stdout"] and not row["stderr"],
                "clean terminal output")
        if row["cell"] in EMPTY_CELLS:
            require(row["unit"] and row["dimension"] == -1 and
                    row["basis_size"] == 1, "unit cell ledger")
        else:
            require(not row["unit"] and row["dimension"] == 0 and
                    row["basis_size"] == SURVIVOR_SIZES[row["cell"]],
                    "finite cell ledger")
    require(actual == expected, "case coverage")


def main():
    for filename, expected in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == expected, f"file custody {filename}")
    product = json.loads(
        (EXPERIMENTS / FILES["product_result"][0]).read_text()
    )
    require(product["schema"] ==
            "rate-half-kb-positive-433-1b-product-base-rank-compiler-v1" and
            product["status_counts"] == {"COMPLETE": 15} and
            len(product["rows"]) == 15, "product compiler coverage")
    verify_payload(json.loads(
        (EXPERIMENTS / FILES["common_result"][0]).read_text()
    ))

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_RANKDROP_COMMON_VERIFY_PASS "
        "rows=60 unit=20 zero_dimensional=40 minors_per_row=45"
    )


if __name__ == "__main__":
    main()
