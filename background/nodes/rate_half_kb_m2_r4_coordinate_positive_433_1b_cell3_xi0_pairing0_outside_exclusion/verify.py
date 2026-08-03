#!/usr/bin/env python3
"""Verify the cell-3 xi0/pairing0 outside exclusion."""

import collections
import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_global_quadratic_quotient"

PILOT_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_pilot_modal.py"
PILOT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_census_result.json"
REPLAY_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_root_replay_modal.py"
REPLAY = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_root_replay_census_result.json"
SOLVER_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi0_pairing0_outside_solver_modal.py"
SOLVER = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi0_pairing0_outside_solver_result.json"

QUOTIENT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_birational_profile_result.json"
KERNEL = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
PRODUCT = EXPERIMENTS / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"

PINNED = {
    PILOT_SCRIPT: "0692770c755348318d410f40249f16cbcadc3fabd86a4a913ed7eae3b1663875",
    PILOT: "b52d89b101b12a7003529e6708788e8e8e6625681afe8823ac90cfd8401863f7",
    REPLAY_SCRIPT: "e3087c31cec06ad4b6e3bbd7d7b691db3daecc3d876ab6b790fc3c3e99f1098f",
    REPLAY: "c68888d502250a1addcf6af19d1b63ef94c960dabc0f7d07637b73433a159be0",
    SOLVER_SCRIPT: "ac7590ceeea2843b80943a783cdccf814484df2b9036ad387eb02c0c5febbb6f",
    SOLVER: "8a06a7a073473f5aa8ea1515a20c93be5db53acae7935004aa5109ed6a5df0da",
}

SIGNS = set(itertools.product((-1, 1), repeat=2))
LANES = set(itertools.product((-1, 1), repeat=2))
BASIS = ["1", "t", "t^2", "b", "b*t", "b*t^2"]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def rows_by_sign(payload, label):
    rows = {}
    for row in payload["rows"]:
        signs = tuple(row["epsilon"])
        require(signs in SIGNS and signs not in rows, f"{label} sign row")
        rows[signs] = row
    require(set(rows) == SIGNS, f"{label} four-sign cover")
    return rows


def verify_pilot(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-six-basis-cut-census-v1",
            "pilot schema")
    require(payload["source_quotient_sha256"] == digest(QUOTIENT),
            "pilot quotient custody")
    require(payload["source_kernel_sha256"] == digest(KERNEL),
            "pilot kernel custody")
    rows = rows_by_sign(payload, "pilot")
    numerator_hashes = set()
    denominator_hashes = set()
    for signs, row in rows.items():
        require(row["status"] == "COMPLETE" and row["epsilon"] == list(signs),
                "pilot completion")
        require(row["sigma"] == [-1, -1] and row["xi_index"] == 0 and
                row["pairing_index"] == 0, "pilot scope")
        require(row["basis"] == BASIS and row["base_degree"] == 3 and
                row["b_degree"] == 2 and row["algebra_dimension"] == 6,
                "six-dimensional algebra")
        require(row["tower_norm_match"], "independent norm equality")
        norm = row["target_free_norm"]
        require((norm["numerator"]["degree"],
                 norm["numerator"]["terms"]) == (422, 401),
                "norm numerator shape")
        require((norm["denominator"]["degree"],
                 norm["denominator"]["terms"]) == (156, 157),
                "norm denominator shape")
        numerator_hashes.add(norm["numerator"]["sha256"])
        denominator_hashes.add(norm["denominator"]["sha256"])
        roots = row["field_roots"]
        require(len(roots) == len(set(roots)) == 11 and
                row["field_root_gcd_degree"] == 11 and
                row["field_root_factor_degrees"] == [1] * 11,
                "complete linear field-root ledger")
        root_rows = row["field_root_rows"]
        require([item["r"] for item in root_rows] == roots,
                "pilot root-row custody")
        statuses = collections.Counter(item["status"] for item in root_rows)
        require(statuses == {"DENOMINATOR_BOUNDARY": 5,
                             "LIVE_NORM_ROOT": 6},
                "pilot root partition")
        require(all(not item["zero_guard_denominators"] for item in root_rows),
                "unexpected rational denominator zero")
    require(len(numerator_hashes) == len(denominator_hashes) == 4,
            "sign-specialized norm transcripts")
    return rows


def verify_replay(payload, pilot_rows):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-six-basis-cut-root-replay-census-v1",
            "replay schema")
    require(payload["source_quotient_sha256"] == digest(QUOTIENT),
            "replay quotient custody")
    require(payload["source_kernel_sha256"] == digest(KERNEL),
            "replay kernel custody")
    require(payload["source_product_sha256"] == digest(PRODUCT),
            "replay product custody")
    require(payload["source_pilot_sha256"] == digest(PILOT),
            "replay pilot custody")
    rows = rows_by_sign(payload, "replay")
    missing_records = {}
    for signs, row in rows.items():
        require(row["status"] == "COMPLETE" and row["xi_index"] == 0 and
                row["pairing_index"] == 0, "replay completion and scope")
        require({tuple(value) for value in row["target_lanes_covered"]} == LANES,
                "replay target lanes")
        require(row["norm_root_count"] == 11 and
                [item["r"] for item in row["root_rows"]] ==
                pilot_rows[signs]["field_roots"], "replay all norm roots")
        root_statuses = collections.Counter(
            item["status"] for item in row["root_rows"]
        )
        require(root_statuses == {"ROUTE_BOUNDARY": 5, "CHECKED": 6},
                "replay root partition")

        guarded = []
        zero_points = []
        for root_row in row["root_rows"]:
            if root_row["status"] == "ROUTE_BOUNDARY":
                require(root_row["r_zero_guards"] and not root_row["t_rows"],
                        "route-boundary record")
                continue
            require(not root_row["r_zero_guards"], "live r guard")
            for t_row in root_row["t_rows"]:
                require(t_row["status"] == "CHECKED" and
                        not t_row["tr_zero_guards"], "live t row")
                for b_row in t_row["b_rows"]:
                    require(not b_row["bc_zero_guards"] and
                            b_row["nonzero_cofactor_indices"] == list(range(6)),
                            "guarded b,c point")
                    require(b_row["c_denominator"] % 2130706433 and
                            b_row["a_missing"] % 2130706433,
                            "recovery and missing-ratio units")
                    point = (root_row["r"], t_row["t"],
                             b_row["b"], b_row["c"])
                    guarded.append(point)
                    missing_records[(signs, point)] = b_row["missing_record"]
                    if b_row["status"] == "TARGET_FREE_ZERO":
                        require(b_row["target_free_value"] == 0,
                                "target-free zero transcript")
                        zero_points.append(point)
                    else:
                        require(b_row["status"] == "TARGET_FREE_NONZERO" and
                                b_row["target_free_value"] != 0,
                                "target-free nonzero transcript")
        require(len(guarded) == len(set(guarded)) == 12,
                "twelve guarded common points")
        require(len(zero_points) == len(set(zero_points)) == 4,
                "four target-free points")
        require(set(guarded) == {tuple(value)
                                for value in row["guarded_common_points"]},
                "guarded point summary")
        require(set(zero_points) == {tuple(value)
                                    for value in row["target_free_zero_points"]},
                "target-free point summary")
        require(not row["case_excluded"],
                "target-free cut alone must not claim exclusion")
    return rows, missing_records


def verify_solver(payload, replay_rows, missing_records):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-xi0-pairing0-outside-census-v1",
            "solver schema")
    require(payload["source_kernel_sha256"] == digest(KERNEL),
            "solver kernel custody")
    require(payload["source_replay_sha256"] == digest(REPLAY),
            "solver replay custody")
    rows = rows_by_sign(payload, "solver")
    total_fibers = 0
    total_f_candidates = 0
    for signs, row in rows.items():
        require(row["status"] == "COMPLETE" and row["xi_index"] == 0 and
                row["pairing_index"] == 0 and row["case_excluded"],
                "solver completion and exclusion")
        require(row["case_count"] == len(row["rows"]) == 16,
                "sixteen point/lane rows per sign")
        require(not row["witnesses"] and not row["boundary_solutions"] and
                not row["unresolved"], "empty final ledgers")
        points = {tuple(value)
                  for value in replay_rows[signs]["target_free_zero_points"]}
        expected = set(itertools.product(points, LANES))
        actual = {(tuple(item["point"]), tuple(item["sigma"]))
                  for item in row["rows"]}
        require(actual == expected and len(actual) == 16,
                "point/lane Cartesian cover")
        root_counts = collections.Counter()
        for item in row["rows"]:
            point = tuple(item["point"])
            require(item["status"] == "CHECKED" and
                    item["colored_degree"] == 4,
                    "checked colored quartic")
            require(item["de"] == missing_records[(signs, point)],
                    "missing-record custody")
            roots = item["f_roots"]
            require(roots is not None and len(roots) == len(set(roots)),
                    "finite colored root list")
            root_counts[len(roots)] += 1
            require({entry["f"] for entry in item["f_rows"]} == set(roots) and
                    len(item["f_rows"]) == len(roots),
                    "colored-root replay")
            for entry in item["f_rows"]:
                require(entry["f"] != 0 and entry["status"] == "CHECKED" and
                        entry["u_gcd_degree"] == 0 and
                        entry["u_roots"] == [] and entry["u_rows"] == [],
                        "degree-zero u-cut gcd")
            total_f_candidates += len(roots)
        require(root_counts == {0: 12, 4: 4},
                "per-sign finite-fiber partition")
        total_fibers += len(row["rows"])
    require(total_fibers == 64 and total_f_candidates == 64,
            "global finite census")


def verify_dag():
    dag = load(ROOT / "dag.json")
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    require(PARENT in nodes and nodes[PARENT]["status"] == "PROVED",
            "proved parent")
    edges = {(row["from"], row["to"], row["kind"])
             for row in dag["edges"]}
    require((PARENT, NODE_ID, "req") in edges, "parent edge")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    pilot_rows = verify_pilot(load(PILOT))
    replay_rows, missing_records = verify_replay(load(REPLAY), pilot_rows)
    verify_solver(load(SOLVER), replay_rows, missing_records)
    verify_dag()
    print("cell=3 xi=0 pairing=0 raw_cases=16 fibers=64 f_candidates=64 witnesses=0")


if __name__ == "__main__":
    main()
