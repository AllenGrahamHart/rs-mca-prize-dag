#!/usr/bin/env python3
"""Verify the cell-3 exceptional scale-chart exclusion packet."""

import hashlib
import json
from pathlib import Path
import re


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1a_"
    "cell3_exceptional_scale_chart_exclusion"
)
FILES = {
    "factor": "rate_half_kb_positive_433_1a_cell3_exceptional_scale_factor_result.json",
    "charts": "rate_half_kb_positive_433_1a_cell3_exceptional_common_charts_result.json",
    "points": "rate_half_kb_positive_433_1a_cell3_exceptional_point_lift_result.json",
    "outside": "rate_half_kb_positive_433_1a_cell3_exceptional_outside_result.json",
    "kernel": "rate_half_kb_positive_433_1a_cell3_kernel_reduction_result.json",
}
HASHES = {
    "factor": "02cbc9d6cc95d6f8d3ac7782fa2e9fdccbb9b5d035f420a4df3588e57b0b192c",
    "charts": "4c158d2fec9b71a291be4c444e303b0ecd51c9529811b0dc3ebbb8c086b4abc3",
    "points": "22eb1b5514c73edc29c86731514b922740592389a02ac8e4c42cef234b6e5d13",
    "outside": "77b1000da7dddc789a4b328f9d5036fbf37cbda8d5878a6a78c84e1300ca0f91",
    "kernel": "afa3829dec518a9000d65cfcca5ec7632980986086f53ce5de6f2eaf12f06b48",
}
PRIME = 2130706433
ROOTS = [0, 1, 16711679, 1288361599, 2113994754, 2130706432]
POINTS = [
    {"t": 1288361599, "r": 700051530, "b": 1068789879, "c": 393847656},
    {"t": 1288361599, "r": 700051530, "b": 1953359317, "c": 159222518},
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def evaluate_compact(value, point):
    total = 0
    for raw_term in re.findall(r"[+-]?[^+-]+", value):
        sign = 1
        term = raw_term
        if term.startswith("+"):
            term = term[1:]
        elif term.startswith("-"):
            sign = -1
            term = term[1:]
        match = re.match(r"\d+", term)
        coefficient = int(match.group(0)) if match else 1
        term = term[match.end():] if match else term
        monomial = coefficient
        while term:
            match = re.match(r"([crbt])(\d*)", term)
            require(match is not None, "compact coefficient parser")
            variable, exponent = match.groups()
            monomial = monomial * pow(
                point[variable], int(exponent) if exponent else 1, PRIME
            ) % PRIME
            term = term[match.end():]
        total = (total + sign*monomial) % PRIME
    return total


def verify_payloads(payloads):
    factor = payloads["factor"]
    require(factor["schema"] ==
            "rate-half-kb-positive-433-1a-cell3-exceptional-scale-factor-v1",
            "factor schema")
    result = factor["result"]
    require(result["status"] == "COMPLETE" and result["field"] == PRIME,
            "factor completion")
    require([row["t"] for row in result["linear_roots"]] == ROOTS,
            "exceptional root census")
    require({row["name"] for row in result["rows"]} == {
        "r_denominator", "c_denominator", "denominator_scale",
        "common_projective_scale", "plane_leading_coefficient",
        "projected_common_scale",
    }, "scale census")
    for row in result["rows"]:
        require(sum(item["total_degree"]*item["multiplicity"]
                    for item in row["factorization"]) == row["degrees"][1],
                f"factor degree {row['name']}")
        for item in row["factorization"]:
            require(item["total_degree"] in (1, 3), "factor degree class")
            if item["total_degree"] == 3:
                require("root" not in item, "cubic root fence")

    charts = payloads["charts"]
    require(charts["schema"] ==
            "rate-half-kb-positive-433-1a-cell3-exceptional-common-charts-v1",
            "charts schema")
    require(charts["source_factor_sha256"] == HASHES["factor"],
            "factor-to-chart hash chain")
    require([row["t"] for row in charts["rows"]] == ROOTS,
            "chart root coverage")
    nonunits = []
    for row in charts["rows"]:
        require(row["status"] == "COMPLETE" and not row["stderr"],
                "chart completion")
        if row["t"] == 1288361599:
            require(row["unit"] is False and row["guard_trivial"] is False,
                    "sole proper chart")
            require("G[4]=b2-891442763b+1" in row["stdout"],
                    "proper chart quadratic")
            nonunits.append(row)
        else:
            require(row["unit"] is True and row["guard_trivial"] is True,
                    "guard-empty chart")
    require(len(nonunits) == 1, "unique proper exceptional chart")

    points = payloads["points"]
    require(points["schema"] ==
            "rate-half-kb-positive-433-1a-cell3-exceptional-point-lift-v1",
            "point schema")
    lifted = points["result"]
    require(lifted["status"] == "COMPLETE" and lifted["field"] == PRIME,
            "point completion")
    require(lifted["source_charts_sha256"] == HASHES["charts"],
            "chart-to-point hash chain")
    require(lifted["legendre"] == 1 and
            lifted["b_roots"] == [1068789879, 1953359317],
            "split quadratic")
    require(lifted["deployed_points"] == POINTS, "point census")
    for point in POINTS:
        b_value = point["b"]
        require((b_value*b_value - 891442763*b_value + 1) % PRIME == 0,
                "quadratic substitution")
        require(point["c"] ==
                (736842529*b_value + 915102487) % PRIME,
                "linear c substitution")

    outside = payloads["outside"]
    require(outside["schema"] ==
            "rate-half-kb-positive-433-1a-cell3-exceptional-outside-v1",
            "outside schema")
    require(outside["source_points_sha256"] == HASHES["points"],
            "point-to-outside hash chain")
    require([row["point"] for row in outside["rows"]] == POINTS,
            "outside point coverage")
    reduced = payloads["kernel"]["result"]["reduced_coefficients"]
    expected_program_hashes = [
        "416c444ea0e156b6ca1b8ba73b6745b883e20d9157e1aa4f7bfbd6494a4e5ea9",
        "a934dbcff8b1a5180c4dc526372c730b5d6af946d38213c3e5098c5a1b7f6634",
    ]
    for row, program_hash in zip(outside["rows"], expected_program_hashes):
        require(row["status"] == "COMPLETE", "outside completion")
        expected = {name: evaluate_compact(value, row["point"])
                    for name, value in reduced.items()}
        require(row["coefficients"] == expected and any(expected.values()),
                "independent kernel evaluation")
        require((expected["b10"] + expected["b11"]) % PRIME == 0,
                "exceptional B1 opposition")
        common = [
            1, pow(row["point"]["t"], 2, PRIME), PRIME-1,
            pow(row["point"]["r"], 2, PRIME),
            (-pow(row["point"]["r"], 2, PRIME)) % PRIME,
        ]
        require(row["common_labels"] == common and
                len(set(common)) == 5 and all(common), "common-label guards")
        pair = row["pair"]
        require(pair["status"] == "COMPLETE" and pair["unit"] is True and
                pair["program_sha256"] == program_hash and
                "UNIT=1" in pair["stdout"] and not pair["stderr"],
                "signed-pair unit ideal")
        require(row["family"] is None, "pair suffices fence")


def main():
    payloads = {}
    for name, filename in FILES.items():
        path = EXPERIMENTS / filename
        require(hashlib.sha256(path.read_bytes()).hexdigest() == HASHES[name],
                f"artifact hash {name}")
        payloads[name] = json.loads(path.read_text())
    verify_payloads(payloads)

    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "statement status")
    require("does not exclude the main genus-three chart" in statement,
            "main-chart nonclaim")
    require("only `F_2130706433`" in contract and "nonclaim" in contract,
            "contract field and nonclaim fences")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    parents = (
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_cell3_genus3_plane_kernel_reduction",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_root_sign_symmetry_quotient",
        "rate_half_kb_m2_r4_coordinate_positive_433_1a_o0b_signed_edge_atlas",
    )
    for parent in parents:
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")
    print("positive 433-1a cell-3 exceptional scale charts verified")


if __name__ == "__main__":
    main()
