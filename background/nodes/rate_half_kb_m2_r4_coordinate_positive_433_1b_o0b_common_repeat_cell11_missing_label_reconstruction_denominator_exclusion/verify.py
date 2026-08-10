#!/usr/bin/env python3
"""Verify the cell-11 missing-label reconstruction denominator exclusion."""

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
    "cell11_common_kernel_reconstruction",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_"
    "cell11_symmetric_function_field_tower",
}
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"
PRIME = 2130706433
RESULT = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_reconstruction_denominator_boundary_result.json"
)
TOWER = (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell11_symmetric_tower_result.json"
)
FILES = {
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_reconstruction_denominator_boundary_modal.py": "503e7f066376206f0c090c92d43ee4f8e027210f86962053f32d4fc6c30b9d0a",
    RESULT: "2228e7ece1b6b74d34f15fdc2a6f82e6fd33ba675a6b19f18537fc3756547b05",
    TOWER: "e80940956518b958dafe74eb34e8ce4f00ce729e78646203bb0724057e6f7899",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_function_field_core.py": "336aace4780acce09d9cb53cc969635d16a038af0a5379338a746e086758aac7",
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell11_principal_input_result.json": "a9c3f10fc7e368f88599bce085598d641d0a73352a1f7d54e06abcd9b4aabbf7",
}
EXPECTED = {
    -1: {
        "dimension": 6,
        "guards": 9,
        "degrees": (32, 10),
        "hashes": (
            "c15ecafd0a8d186df424e77942c7756b112e379081f2343e92d21ad7a383b0b6",
            "2aaf7d186b55273c338f410081e57b7f6942c2c55d33968e71b1da06df3862e2",
        ),
        "factors": [(3, 2), (3, 2), (1, 8), (1, 12)],
        "factor_hashes": [
            "32bd5ed9f2265b3886c5375225710a89aeb95b1bd166bbd62160e652798504e1",
            "4f45970c8d843996b434f76d5eea7969177015a56edec908c96166d9983b671f",
            "e61b9f584dbe27741cef6e9ee440831d7d94470c0871b0871541f0308916efea",
            "90b200f2835231116b91a70ad14f795df828702cf3c1ba2b6891163594860f1c",
        ],
        "roots": [
            (PRIME - 1, 8, [0, 1, 2], False),
            (1, 12, [3, 4, 5, 6, 7, 8], False),
        ],
    },
    1: {
        "dimension": 4,
        "guards": 6,
        "degrees": (36, 14),
        "hashes": (
            "6b2157ff66ca6f7a052419bf46a40344abc7256c71cfc1613bd828a744e4b951",
            "999aed1703c1512fb1845d418306013fc5d1f4be412bddf760f3fb4718c5c781",
        ),
        "factors": [(3, 2), (1, 2), (1, 2), (1, 2), (2, 2), (1, 4), (2, 8)],
        "factor_hashes": [
            "5fb7eda44b4f37a36161d1a49ab0bc2872ee7cce136ce08ba9f1589803bdf8af",
            "9db35f33266f42aaae6b1575e5e647fb7294fd0729437f0f3c4296cfa658e45c",
            "06e40a33c7ca79f7b5aa982dd0f89faa0eeac782b712d7f7e8e8af66252fe7b0",
            "8b56a7b87a654707d9278eb7547d2dd54365b099970f667b67252271f42311b7",
            "c1251d58628e01c622193c278fe1fa8da64e51ab61e9e0f63f5ef667af1d8aca",
            "e61b9f584dbe27741cef6e9ee440831d7d94470c0871b0871541f0308916efea",
            "51b5dec31aa0ea9afcbef69fde42fc30d0350901d22ab5c9e020421219ae0f22",
        ],
        "roots": [
            (153731577, 2, [], True),
            (583634934, 2, [], True),
            (1547071505, 2, [], True),
            (PRIME - 1, 4, [2, 3, 4, 5], False),
        ],
    },
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(filename):
    return json.loads((EXPERIMENTS / filename).read_text())


def root_tuple(root):
    return (
        root["x"], root["multiplicity"], root["zero_guard_indices"],
        root["tower_chart_guards_nonzero"],
    )


def validate_payload(payload, tower):
    require(
        payload["schema"]
        == "kb-positive-433-1b-o0b-cell11-reconstruction-denominator-boundary-v1",
        "schema",
    )
    require(payload["case_count"] == len(payload["rows"]) == 8,
            "row census")
    require(
        payload["status_counts"]
        == {"NO_GUARDED_RECONSTRUCTION_BOUNDARY_POINT": 8},
        "status census",
    )
    require(payload["chart_boundary_root_occurrences"] == 12,
            "chart root census")
    require(payload["distinct_chart_boundary_root_count"] == 3,
            "distinct chart roots")
    require(payload["field_boundary_point_count"] == 16,
            "field point census")
    require(payload["guarded_boundary_point_count"] == 0,
            "guarded point census")

    programs = {
        (row["bc_sign"], tuple(row["epsilon"])): row["program_sha256"]
        for row in tower["rows"]
    }
    expected_keys = set(itertools.product((-1, 1), repeat=3))
    seen = set()
    for row in payload["rows"]:
        key = (*row["epsilon"], row["bc_sign"])
        require(key in expected_keys and key not in seen, "row key")
        seen.add(key)
        require(row["tower_valid"], "tower validity")
        require(row["tower_program_sha256"]
                == programs[(row["bc_sign"], tuple(row["epsilon"]))],
                "tower custody")
        expected = EXPECTED[row["bc_sign"]]
        require(row["algebra_dimension"] == expected["dimension"],
                "dimension")
        require(row["tower_chart_guard_count"] == expected["guards"],
                "guard count")
        require(len(row["tower_chart_guard_sha256"])
                == expected["guards"], "guard hashes")
        require((row["norm_numerator_degree"], row["norm_denominator_degree"])
                == expected["degrees"], "norm degrees")
        require((row["norm_numerator_sha256"], row["norm_denominator_sha256"])
                == expected["hashes"], "norm identities")
        factors = row["norm_numerator_factorization"]
        require([(item["degree"], item["multiplicity"])
                 for item in factors] == expected["factors"],
                "factor profile")
        require([item["sha256"] for item in factors]
                == expected["factor_hashes"], "factor identities")
        require(sum(item["degree"] * item["multiplicity"]
                    for item in factors) == row["norm_numerator_degree"],
                "factor degree reconstruction")
        require([root_tuple(root) for root in row["base_field_roots"]]
                == expected["roots"], "base-field roots")
        if row["bc_sign"] == -1:
            require(row["chart_boundary_roots"] == [], "BC- chart roots")
            require(row["root_fiber_census"] == [], "BC- fibers")
            require(row["boundary_points"] == [], "BC- points")
            require(row["field_boundary_point_count"] == 0, "BC- point count")
        else:
            require([root["x"] for root in row["chart_boundary_roots"]]
                    == [153731577, 583634934, 1547071505],
                    "BC+ chart roots")
            require(row["root_fiber_census"] == [
                {"x": 153731577, "y_root_count": 2,
                 "source_candidate_count": 0, "boundary_candidate_count": 0},
                {"x": 583634934, "y_root_count": 2,
                 "source_candidate_count": 2, "boundary_candidate_count": 2},
                {"x": 1547071505, "y_root_count": 2,
                 "source_candidate_count": 2, "boundary_candidate_count": 2},
            ], "BC+ fiber census")
            require(row["field_boundary_point_count"] == 4,
                    "BC+ point count")
            require(sorted(point["x"] for point in row["boundary_points"])
                    == [583634934, 583634934, 1547071505, 1547071505],
                    "BC+ point roots")
            for point in row["boundary_points"]:
                require(point["b_equals_c"] and point["bc_matches_x"],
                        "point coordinates")
                require(point["common_equations_zero"], "common equations")
                require(not point["common_guard_nonzero"], "common guard")
                require(not point["guarded"], "guarded classification")
        require(row["guarded_boundary_point_count"] == 0,
                "row guarded point count")
        require(row["status"]
                == "NO_GUARDED_RECONSTRUCTION_BOUNDARY_POINT", "row status")
    require(seen == expected_keys, "Cartesian coverage")


def main():
    for filename, expected in FILES.items():
        actual = hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
        require(actual == expected, f"file custody: {filename}")
    validate_payload(load(RESULT), load(TOWER))
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
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_CELL11_RECONSTRUCTION_BOUNDARY_PASS "
        "rows=8 chart_roots=12 field_points=16 guarded_points=0"
    )


if __name__ == "__main__":
    main()
