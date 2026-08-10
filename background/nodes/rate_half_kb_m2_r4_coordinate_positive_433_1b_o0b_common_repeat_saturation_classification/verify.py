#!/usr/bin/env python3
"""Verify repeated-BC guarded common saturation classification."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_saturation_modal.py",
        "9a7ebbf327a33ea1bfbd059a7242b14eee6543b99515b9d92a070e57f7768b06",
    ),
    "result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_saturation_result.json",
        "fa6a5332c6eafe14644d497e564b36deb589f0cac5936d2cc4ea5f0acbe64270",
    ),
    "compiler": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler.py",
        "e438d227f5ed7b92c8b787daf075dd56aadb1f6e871f3ffd06e8dd4823b3deea",
    ),
    "compiler_result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_vieta_compiler_result.json",
        "09f23b511fd22195e251aafe45c1a958448be224f2d5e0bd549c9adf69820117",
    ),
}
REPRESENTATIVES = (0, 1, 3, 4, 6, 7, 9, 10, 11)
ORBIT_PARTNER = {0: 0, 1: 2, 3: 3, 4: 5, 6: 6, 7: 8,
                 9: 12, 10: 13, 11: 14}
ALWAYS_UNIT = {0, 4, 7, 9, 10}
ALWAYS_SURVIVE = {3, 6, 11}
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_vieta_minor_atlas",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_vieta_minor_compiler",
}
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def expected_unit(cell, epsilon):
    if cell in ALWAYS_UNIT:
        return True
    if cell in ALWAYS_SURVIVE:
        return False
    require(cell == 1, f"unexpected representative {cell}")
    return epsilon[0] == epsilon[1]


def validate(payload, compiler_payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-repeat-saturation-v1", "schema")
    require(payload["source_sha256"] == FILES["compiler"][1], "source custody")
    require(payload["representative_cells"] == list(REPRESENTATIVES),
            "representatives")
    expected_cases = set(itertools.product(
        REPRESENTATIVES, (-1, 1), (-1, 1), (-1, 1),
    ))
    actual_cases = set()
    representative_units = 0
    representative_survivors = 0
    formal_units = 0
    formal_survivors = 0
    for row in payload["rows"]:
        case = (row["cell"], *row["epsilon"], row["bc_sign"])
        require(case not in actual_cases, "duplicate case")
        actual_cases.add(case)
        require(row["status"] == "COMPLETE" and row["chart_complete"],
                "case completion")
        unit = expected_unit(row["cell"], row["epsilon"])
        require(row["chart_unit"] is unit and row["full_unit"] is unit,
                "unit pattern")
        if unit:
            representative_units += 1
        else:
            representative_survivors += 1
            expected_dimension = 2 if row["cell"] == 1 else 1
            require(f"DIM={expected_dimension}" in row["stdout"],
                    "survivor dimension")
        orbit_size = 1 if ORBIT_PARTNER[row["cell"]] == row["cell"] else 2
        formal_units += orbit_size * int(unit)
        formal_survivors += orbit_size * int(not unit)
    require(actual_cases == expected_cases, "case coverage")
    require((representative_units, representative_survivors) == (44, 28),
            "representative census")
    require((formal_units, formal_survivors) == (80, 40),
            "algebra-row census")

    stripped = [row for row in compiler_payload["rows"]
                if row["mode"] == "stripped"]
    by_case = {
        (row["cell"], *row["epsilon"], row["bc_sign"]):
        tuple(sorted(item["sha256"] for item in row["minor_summaries"]))
        for row in stripped
    }
    require(len(by_case) == 120, "compiler row census")
    for representative, partner in ORBIT_PARTNER.items():
        for epsilon_1, epsilon_2, bc_sign in itertools.product(
                (-1, 1), (-1, 1), (-1, 1)):
            left = by_case[(representative, epsilon_1, epsilon_2, bc_sign)]
            right = by_case[(partner, epsilon_1, epsilon_2, bc_sign)]
            require(left == right, "duplicate-role polynomial transport")
    return {
        "representative_units": representative_units,
        "representative_survivors": representative_survivors,
        "algebra_units": formal_units,
        "algebra_survivors": formal_survivors,
        "formal_lane_units": 2 * formal_units,
        "formal_lane_survivors": 2 * formal_survivors,
    }


def main():
    for filename, expected_hash in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == expected_hash, f"file custody {filename}")
    payload = json.loads((EXPERIMENTS / FILES["result"][0]).read_text())
    compiler = json.loads(
        (EXPERIMENTS / FILES["compiler_result"][0]).read_text()
    )
    counts = validate(payload, compiler)

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED", f"parent {parent}")
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer evidence edge")
    statement = (NODE / "statement.md").read_text()
    require("does not classify the surviving varieties" in statement and
            "or prove either Prize" in statement, "scope fence")
    print(
        "RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_SATURATION_VERIFY_PASS "
        f"representatives=72 unit={counts['representative_units']} "
        f"survive={counts['representative_survivors']} "
        f"algebra=80+40 formal_lanes=160+80"
    )


if __name__ == "__main__":
    main()
