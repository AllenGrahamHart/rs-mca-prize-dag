#!/usr/bin/env python3
"""Verify the cell-11 selected-cofactor deployed boundary exclusion."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_"
    "cell11_selected_rank_fiber_partition",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_"
    "cell11_symmetric_function_field_tower",
}
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
PRIME = 2130706433
RESULT = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_selected_cofactor_boundary_result.json"
)
TOWER = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_symmetric_tower_result.json"
)
INPUT = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_principal_input_result.json"
)
FILES = {
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_selected_cofactor_boundary_modal.py": "2d2449c5f58e25006c40b4eb1a3e199498ba81659baa5e3a42d2c35c9fe656b8",
    RESULT: "8c9a12c38c1cb4f48a9c9fd8b648a297131b6de26479eec42ab786f4dac496e3",
    TOWER: "e80940956518b958dafe74eb34e8ce4f00ce729e78646203bb0724057e6f7899",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_function_field_core.py": "336aace4780acce09d9cb53cc969635d16a038af0a5379338a746e086758aac7",
    INPUT: "a9c3f10fc7e368f88599bce085598d641d0a73352a1f7d54e06abcd9b4aabbf7",
}
EXPECTED = {
    -1: {
        "dimension": 6,
        "guard_count": 9,
        "numerator_degree": 14,
        "denominator_degree": 2,
        "minor_sha256": "565aa4fb6fb918dfd2cad221ba290a17c8e148890f31c52996b2a3759c8bd9ef",
        "numerator_sha256": "7233ece430c01d5dd59b87d5134966570521d3ad9959540d8f02242b7f95c89e",
        "denominator_sha256": "7ead7f2ac1f175e1650b7a7b433f7cbdca3ae29ff06e6ff5c5199d17b731658c",
        "factors": [(2, 2), (1, 10)],
        "factor_hashes": [
            "18d7e1f9ccea7bee00b81ce9d2f71fd37750c7ef152aeffae2ff3e5ec3e975f0",
            "90b200f2835231116b91a70ad14f795df828702cf3c1ba2b6891163594860f1c",
        ],
        "root": 1,
        "multiplicity": 10,
        "zero_guards": [3, 4, 5, 6, 7, 8],
    },
    1: {
        "dimension": 4,
        "guard_count": 6,
        "numerator_degree": 18,
        "denominator_degree": 8,
        "minor_sha256": "e3570ad8e5401672b4212af63f2c30d9b454f178335c51e21289b211a693ee99",
        "numerator_sha256": "85318e9f312f0a4d319bf079c3c4d0628214acfa3394ec4e24084ce0725d3517",
        "denominator_sha256": "da28beab3c89fec92475971d05da5b156b8480e4f0d3ebf3fb260d929c9aafdc",
        "factors": [(3, 2), (2, 4), (1, 4)],
        "factor_hashes": [
            "cee7b82e878b4a24899f4006f2841c83cad720f2afe8a227dc78fd5569357483",
            "51b5dec31aa0ea9afcbef69fde42fc30d0350901d22ab5c9e020421219ae0f22",
            "e61b9f584dbe27741cef6e9ee440831d7d94470c0871b0871541f0308916efea",
        ],
        "root": PRIME - 1,
        "multiplicity": 4,
        "zero_guards": [2, 3, 4, 5],
    },
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(filename):
    return json.loads((EXPERIMENTS / filename).read_text())


def validate_payload(payload, tower, principal):
    require(
        payload["schema"]
        == "kb-positive-433-1b-o0b-cell11-selected-boundary-v1",
        "schema",
    )
    require(payload["case_count"] == len(payload["rows"]) == 8,
            "row census")
    require(
        payload["status_counts"]
        == {"NO_DEPLOYED_FIELD_BOUNDARY_POINT": 8},
        "status census",
    )
    require(payload["deployed_boundary_root_occurrences"] == 0,
            "deployed root census")
    require(payload["distinct_deployed_boundary_root_count"] == 0,
            "distinct deployed root census")
    require(payload["field_boundary_point_count"] == 0,
            "field boundary point census")

    tower_programs = {
        (row["bc_sign"], tuple(row["epsilon"])): row["program_sha256"]
        for row in tower["rows"]
    }
    minor_hashes = {
        row["bc_sign"]: row["rank_minor_sha256"]
        for row in principal["product_rows"]
    }
    expected_keys = set(itertools.product((-1, 1), repeat=3))
    seen = set()
    for row in payload["rows"]:
        key = (row["epsilon"][0], row["epsilon"][1], row["bc_sign"])
        require(key in expected_keys and key not in seen, "row key")
        seen.add(key)
        tower_key = (row["bc_sign"], tuple(row["epsilon"]))
        require(row["tower_program_sha256"] == tower_programs[tower_key],
                "tower custody")
        require(row["tower_valid"], "tower validation")
        expected = EXPECTED[row["bc_sign"]]
        require(row["algebra_dimension"] == expected["dimension"],
                "algebra dimension")
        require(row["pre_cofactor_guard_count"] == expected["guard_count"],
                "guard count")
        require(len(row["pre_cofactor_guard_sha256"])
                == expected["guard_count"], "guard hashes")
        require(row["selected_rank_minor_sha256"]
                == expected["minor_sha256"]
                == minor_hashes[row["bc_sign"]], "cofactor identity")
        require(row["norm_numerator_degree"]
                == expected["numerator_degree"], "numerator degree")
        require(row["norm_denominator_degree"]
                == expected["denominator_degree"], "denominator degree")
        require(row["norm_numerator_sha256"]
                == expected["numerator_sha256"], "numerator identity")
        require(row["norm_denominator_sha256"]
                == expected["denominator_sha256"], "denominator identity")
        factors = row["norm_numerator_factorization"]
        require([(item["degree"], item["multiplicity"])
                 for item in factors] == expected["factors"],
                "factor profile")
        require([item["sha256"] for item in factors]
                == expected["factor_hashes"], "factor identities")
        require(sum(item["degree"] * item["multiplicity"]
                    for item in factors) == row["norm_numerator_degree"],
                "factor degree reconstruction")
        require(row["base_field_roots"] == [{
            "x": expected["root"],
            "multiplicity": expected["multiplicity"],
            "zero_guard_indices": expected["zero_guards"],
            "pre_cofactor_guards_nonzero": False,
        }], "base-field root classification")
        require(row["off_chart_roots"] == row["base_field_roots"],
                "off-chart roots")
        require(row["deployed_boundary_roots"] == [], "deployed roots")
        require(row["root_fiber_census"] == [], "root fibers")
        require(row["boundary_points"] == [], "boundary points")
        require(row["field_boundary_point_count"] == 0,
                "row point census")
        require(row["status"] == "NO_DEPLOYED_FIELD_BOUNDARY_POINT",
                "row status")
    require(seen == expected_keys, "Cartesian coverage")


def main():
    for filename, expected in FILES.items():
        actual = hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
        require(actual == expected, f"file custody: {filename}")
    validate_payload(load(RESULT), load(TOWER), load(INPUT))
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {
        (row["from"], row["to"], row.get("kind", "req"))
        for row in dag["edges"]
    }
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED", "parent status")
        require((parent, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer edge")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_CELL11_SELECTED_BOUNDARY_PASS "
        "rows=8 base_roots=8 deployed_roots=0 field_points=0"
    )


if __name__ == "__main__":
    main()
