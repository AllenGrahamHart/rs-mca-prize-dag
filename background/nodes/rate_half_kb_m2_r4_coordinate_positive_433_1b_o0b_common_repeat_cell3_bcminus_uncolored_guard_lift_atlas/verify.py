#!/usr/bin/env python3
"""Verify the cell-3 BC- uncolored guard-lift atlas."""

from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "roots_launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_uncolored_guard_roots_modal.py",
        "62ffddadc1c919d95dfa5b2d1366de9217f9483a06854ee10e3135bd6af90740",
    ),
    "roots_result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_uncolored_guard_roots_result.json",
        "c0ebc30fd4499318b8a8fc883d418ab6c85db5b04fa49ed7f01c005e1d165705",
    ),
    "lifts_launcher": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_guard_lifts_modal.py",
        "ed2a2eee9d40e5b7466f19a9e2113cb5581d3ec6ac71f1f71cc44fcc05bd464b",
    ),
    "lifts_result": (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_guard_lifts_result.json",
        "0694f171b26fe86db214c27f5ffa0f05f49eaf8370938ae83b936babdf01b1fb",
    ),
}
GENERIC = "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_uncolored_generic_rank_result.json"
GENERIC_SHA256 = "5f0a1569a0bdbf61b5e066874ea9adc4b20d8602153d3804e3a0fcf94e0e50c9"
TOWER_SHA256 = "61b807172ce3e7d11e3ee9462897f62654ba31921b88572460c3d57648d281be"
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcminus_uncolored_generic_rank_atlas"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_remaining_route_payment"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def validate_roots(payload, generic):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-uncolored-guard-roots-v1",
            "root schema")
    require(payload["source_sha256"] == GENERIC_SHA256, "root source")
    require(payload["guard_count"] == 47 and
            payload["status_counts"] == {"COMPLETE": 47}, "root completion")
    rows = {row["sha256"]: row for row in payload["rows"]}
    require(set(rows) == set(generic["guard_atlas"]), "root guard coverage")
    incidence = defaultdict(list)
    for digest, row in rows.items():
        require(row["status"] == "COMPLETE", "root row")
        require(row["degree"] == len(generic["guard_atlas"][digest].split(","))-1,
                "guard degree")
        require(row["field_part_degree"] == len(row["roots"]), "field degree")
        require(row["roots"] == sorted(set(row["roots"])), "root ordering")
        for value in row["roots"]:
            incidence[value].append(digest)
    require(payload["root_union"] == sorted(incidence) and
            len(incidence) == 48, "root union")
    require(sum(len(values) for values in incidence.values()) == 73,
            "root incidences")
    require(payload["root_incidence"] == {
        str(value): sorted(values) for value, values in sorted(incidence.items())
    }, "incidence atlas")


def validate_lifts(payload, roots):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-guard-lifts-v1",
            "lift schema")
    require(payload["source_roots_sha256"] == FILES["roots_result"][1],
            "lift root source")
    require(payload["source_tower_sha256"] == TOWER_SHA256, "lift tower source")
    require(payload["q_count"] == 48 and len(payload["rows"]) == 48,
            "lift coverage")
    require([row["q"] for row in payload["rows"]] == roots["root_union"],
            "lift q values")
    statuses = Counter(row["status"] for row in payload["rows"])
    require(statuses == Counter({
        "LIFTED": 23, "NO_BASE_FIELD_Y": 19,
        "NO_GUARDED_COMMON_POINT": 3,
        "PROJECTION_DENOMINATOR_BOUNDARY": 3,
    }) and payload["status_counts"] == dict(sorted(statuses.items())),
            "lift statuses")
    guarded = 0
    for row in payload["rows"]:
        row_guarded = 0
        for y_row in row.get("sign_rows", []):
            if y_row["status"] != "LIFTED":
                continue
            require(len(y_row["sign_rows"]) == 4, "sign census")
            require({tuple(item["epsilon"]) for item in y_row["sign_rows"]} ==
                    {(-1, -1), (-1, 1), (1, -1), (1, 1)}, "sign labels")
            for sign_row in y_row["sign_rows"]:
                for point in sign_row["points"]:
                    if point["status"] == "GUARDED":
                        row_guarded += 1
        require(row.get("guarded_point_count", 0) == row_guarded,
                "row point count")
        guarded += row_guarded
    require(guarded == payload["guarded_point_count"] == 368,
            "guarded point total")


def main():
    for filename, digest in FILES.values():
        require(hashlib.sha256((EXPERIMENTS / filename).read_bytes()).hexdigest()
                == digest, f"file custody {filename}")
    require(hashlib.sha256((EXPERIMENTS / GENERIC).read_bytes()).hexdigest()
            == GENERIC_SHA256, "generic custody")
    generic = json.loads((EXPERIMENTS / GENERIC).read_text())
    roots = json.loads((EXPERIMENTS / FILES["roots_result"][0]).read_text())
    lifts = json.loads((EXPERIMENTS / FILES["lifts_result"][0]).read_text())
    validate_roots(roots, generic)
    validate_lifts(lifts, roots)
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED" and
            (PARENT, NODE_ID, "req") in edges, "parent")
    require((NODE_ID, CONSUMER, "ev") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_CELL3_BCMINUS_GUARD_LIFT_VERIFY_PASS guards=47 q=48 incidences=73 points=368")


if __name__ == "__main__":
    main()
