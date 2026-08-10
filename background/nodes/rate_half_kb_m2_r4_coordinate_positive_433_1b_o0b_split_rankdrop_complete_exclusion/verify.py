#!/usr/bin/env python3
"""Verify complete O0b split-BC rank-drop exclusion."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PREFIX = "rate_half_kb_positive_433_1b_o0b_split_rankdrop_outside"
SCRIPT = EXPERIMENTS / f"{PREFIX}_modal.py"
MASTER = EXPERIMENTS / f"{PREFIX}_result.json"
POINTS = EXPERIMENTS / "rate_half_kb_positive_433_1b_rankdrop_fglm_profile_result.json"
SHARDS = {
    stratum: EXPERIMENTS / f"{PREFIX}_{stratum}_result.json"
    for stratum in ("S0", "SDE", "SDF")
}
HASHES = {
    SCRIPT: "eab64cbfcbefa6e85e56c4d5a0eb2598509819f588ec8842d761aa49a9472313",
    MASTER: "c89eae30f3281990c125b8dccdaf8ec223fd738d752fff6e29600319422bcbb9",
    POINTS: "1ef0469634892459a35ea9b7b2b72d112d0b10a099ddab2c6754cc9c8e184017",
    SHARDS["S0"]: "a4e07c7e26a47eaa5607a594438d92810bfaec1219cc691a7e2473786d70691d",
    SHARDS["SDE"]: "f55ca390b1984bd8177acdda665e10f2eaaa22505337ca6805724d16192d3177",
    SHARDS["SDF"]: "89b23e31564c4ae800046f440da1fdb1581a5cb2de453dcda3b1cd250b8e3c25",
}
POINTS_SHA256 = HASHES[POINTS]
PRIME = 2130706433
IOTA = 16711679
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_product_rankdrop_deployed_rational_classifier",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_vieta_minor_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
)
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, values[index]),) + tail


def matching_cells():
    output = []
    for singleton in range(5):
        rest = tuple(index for index in range(5) if index != singleton)
        output.extend((singleton, matching) for matching in pairings(rest))
    return tuple(output)


def rank_kernel(rows):
    matrix = [[value % PRIME for value in row] for row in rows]
    pivots = []
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(pivot_row, len(matrix))
                      if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, PRIME)
        matrix[pivot_row] = [value * inverse % PRIME
                             for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            scalar = matrix[row][column]
            if scalar:
                matrix[row] = [
                    (left - scalar * right) % PRIME
                    for left, right in zip(matrix[row], matrix[pivot_row])
                ]
        pivots.append(column)
        pivot_row += 1
    require(pivot_row == len(matrix[0]) - 1, "common rank")
    free = next(column for column in range(len(matrix[0]))
                if column not in pivots)
    kernel = [0] * len(matrix[0])
    kernel[free] = 1
    for row, column in enumerate(pivots):
        kernel[column] = -matrix[row][free] % PRIME
    return kernel


def missing_product(record):
    singleton, matching = matching_cells()[record["cell"]]
    point = record["point"]
    epsilon = record["epsilon"]
    roots = [None] * 5
    roots[matching[0][0]] = 1
    roots[matching[0][1]] = epsilon[0] * IOTA
    roots[matching[1][0]] = point["r"]
    roots[matching[1][1]] = epsilon[1] * IOTA * point["r"]
    roots[singleton] = point["t"]
    labels = [root * root % PRIME for root in roots]
    b_value, c_value = point["b"], point["c"]
    products = (-1, b_value, c_value,
                b_value * c_value, -b_value * c_value)
    sums = (0, 1 + b_value, 1 + c_value,
            b_value + c_value, b_value - c_value)
    rows = [
        [-product, -product * label, -product * label * label,
         1, label, label * label, 0, 0]
        for product, label in zip(products, labels)
    ]
    rows.extend(
        [q, q * label, q * label * label, 0, 0, 0, label, label * label]
        for root, label, edge_sum in zip(roots, labels, sums)
        for q in [root * edge_sum]
    )
    kernel = rank_kernel(rows)
    missing_label = -point["t"] * point["t"] % PRIME

    def evaluate(coefficients):
        return (coefficients[0] + coefficients[1] * missing_label
                + coefficients[2] * missing_label * missing_label) % PRIME

    denominator = evaluate(kernel[:3])
    require(denominator != 0, "missing leading support")
    return evaluate(kernel[3:6]) * pow(denominator, -1, PRIME) % PRIME


def validate(master, shard_payloads, points):
    require(master["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-split-rankdrop-outside-v1",
            "master schema")
    require(master["app"] ==
            "rs-mca-positive-433-1b-o0b-split-rankdrop-outside", "app")
    require(master["source_points_sha256"] == POINTS_SHA256, "point source")
    require(master["point_count"] == 16 and master["lane_count"] == 96 and
            master["case_count"] == 10080 and
            master["status_counts"] == {"COMPLETE": 10080},
            "master census")

    source_points = [
        {"cell": row["cell"], "epsilon": row["epsilon"],
         "point_index": index, "point": point}
        for row in points["rows"]
        for index, point in enumerate(row["rational_points"])
    ]
    require(len(source_points) == 16, "source-point census")
    lanes = []
    for stratum, payload in shard_payloads.items():
        require(payload["schema"] ==
                "rate-half-kb-positive-433-1b-o0b-split-rankdrop-outside-shard-v1",
                "shard schema")
        require(payload["stratum"] == stratum and
                payload["source_points_sha256"] == POINTS_SHA256,
                "shard identity")
        require(payload["lane_count"] == 32 and payload["case_count"] == 3360,
                "shard census")
        manifest = master["shard_manifest"][stratum]
        require(manifest == {
            "file": SHARDS[stratum].name,
            "sha256": HASHES[SHARDS[stratum]],
            "lane_count": 32, "case_count": 3360,
        }, "shard manifest")
        lanes.extend(payload["lanes"])

    expected_lanes = set(itertools.product(
        range(16), ("S0", "SDE", "SDF"), (-1, 1)
    ))
    expected_cases = set(itertools.product(range(7), range(15)))
    actual_lanes = set()
    program_hashes = set()
    summaries = {}
    for lane in lanes:
        key = (lane["point_id"], lane["stratum"], lane["sigma_o"])
        require(key not in actual_lanes, "duplicate lane")
        actual_lanes.add(key)
        source = source_points[lane["point_id"]]
        require(lane["cell"] == source["cell"] and
                lane["epsilon"] == source["epsilon"] and
                lane["point_index"] == source["point_index"],
                "source-point metadata")
        require(lane["missing_product"] == missing_product(source),
                "missing product replay")
        require(lane["status"] == "COMPLETE" and lane["case_count"] == 105 and
                lane["unit_count"] == 105 and lane["survivor_count"] == 0 and
                lane["rational_candidate_cases"] == 0,
                "lane closure")
        actual_cases = set()
        for row in lane["rows"]:
            case = (row["xi_index"], row["pairing_index"])
            require(case not in actual_cases, "duplicate case")
            actual_cases.add(case)
            require(row["status"] == "COMPLETE" and row["unit"] and
                    "UNIT=1" in row["stdout"] and not row["stderr"],
                    "unit certificate")
            require("lex_status" not in row, "unexpected fallback")
            require(len(row["program_sha256"]) == 64, "program digest")
            program_hashes.add(row["program_sha256"])
        require(actual_cases == expected_cases, "case coverage")
        summaries[key] = {
            "point_id": lane["point_id"], "cell": lane["cell"],
            "epsilon": lane["epsilon"], "point_index": lane["point_index"],
            "stratum": lane["stratum"], "sigma_o": lane["sigma_o"],
            "status": lane["status"], "unit_count": lane["unit_count"],
            "survivor_count": lane["survivor_count"],
            "rational_candidate_cases": lane["rational_candidate_cases"],
        }
    require(actual_lanes == expected_lanes, "lane coverage")
    require(len(program_hashes) == 3744, "program digest census")
    master_summaries = {
        (row["point_id"], row["stratum"], row["sigma_o"]): row
        for row in master["lane_summaries"]
    }
    require(master_summaries == summaries, "master summaries")


def main():
    for path, digest in HASHES.items():
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                f"file custody {path.name}")
    master = json.loads(MASTER.read_text())
    shards = {key: json.loads(path.read_text()) for key, path in SHARDS.items()}
    points = json.loads(POINTS.read_text())
    validate(master, shards, points)
    source = SCRIPT.read_text()
    require("ideal I=q0,q1,q2,q3,q4,u*guard-1" in source,
            "five-equation localized ideal")
    require('"S0": (' in source and '"SDE": (' in source and
            '"SDF": (' in source and "endpoint_squares" in source,
            "six signed lanes")
    require(len(tuple(pairings(range(6)))) == 15, "matching count")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    for parent in PARENTS:
        require(nodes[parent]["status"] == "PROVED" and
                (parent, NODE_ID, "req") in edges, f"parent {parent}")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer edge")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_SPLIT_RANKDROP_VERIFY_PASS points=16 lanes=96 ledgers=10080 unit=10080")


if __name__ == "__main__":
    main()
