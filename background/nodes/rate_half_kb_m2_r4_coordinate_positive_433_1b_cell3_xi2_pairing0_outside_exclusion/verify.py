#!/usr/bin/env python3
"""Verify the cell-3 xi2/pairing0 outside exclusion."""

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

CUT_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_cut_modal.py"
CUT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_cut_census_result.json"
REPLAY_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_root_replay_modal.py"
REPLAY = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_root_replay_census_result.json"
SOLVER_SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_outside_solver_modal.py"
SOLVER = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_outside_solver_result.json"
QUOTIENT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_birational_profile_result.json"
KERNEL = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
PRODUCT = EXPERIMENTS / "rate_half_kb_positive_433_1b_product_base_rank_compiler_result.json"

PINNED = {
    CUT_SCRIPT: "1f9b877b0c03ebd96c6042a88a8688d88e7b065ff04b59894c6ee75f24af0227",
    CUT: "50330a5695e05ff284124b15e8d0db127e058b5879f2468ead6d97a52eddb1f6",
    REPLAY_SCRIPT: "9b3ad92a52a6756ad9245ee4b69cf966bb150c2846416e2dbdc75b63fe1c03ad",
    REPLAY: "6bf8d58a8af1fc37d153ed71ad506d27974d06249d4165983bc8bc264e893b57",
    SOLVER_SCRIPT: "c88059ff1cc2d0845cde6c44434678b254c2e0ad9b1231cc79510d7e41842185",
    SOLVER: "e1344a96ba48ddf6ca73360749dd7eb20e924bf153b42dab13599be6a09d8fbe",
}

SIGNS = set(itertools.product((-1, 1), repeat=2))
LANES = set(itertools.product((-1, 1), repeat=2))
BASIS = ["1", "t", "t^2", "b", "b*t", "b*t^2"]
PRIME = 2130706433


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


def verify_cut(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-xi2-pairing0-six-basis-cut-census-v1",
            "cut schema")
    require(payload["source_quotient_sha256"] == digest(QUOTIENT),
            "cut quotient custody")
    require(payload["source_kernel_sha256"] == digest(KERNEL),
            "cut kernel custody")
    rows = rows_by_sign(payload, "cut")
    numerator_hashes = set()
    denominator_hashes = set()
    for signs, row in rows.items():
        require(row["status"] == "COMPLETE" and row["epsilon"] == list(signs),
                "cut completion")
        require(row["sigma"] == [-1, -1] and row["xi_index"] == 2 and
                row["pairing_index"] == 0, "cut scope")
        require(row["basis"] == BASIS and row["base_degree"] == 3 and
                row["b_degree"] == 2 and row["algebra_dimension"] == 6,
                "six-dimensional algebra")
        require(row["tower_norm_match"], "tower norm equality")
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
        require(len(roots) == len(set(roots)) == 8 and
                row["field_root_gcd_degree"] == 8 and
                row["field_root_factor_degrees"] == [1] * 8,
                "eight linear field roots")
        root_rows = row["field_root_rows"]
        require([item["r"] for item in root_rows] == roots,
                "cut root-row custody")
        require(collections.Counter(item["status"] for item in root_rows) ==
                {"DENOMINATOR_BOUNDARY": 5, "LIVE_NORM_ROOT": 3},
                "cut root partition")
    require(len(numerator_hashes) == len(denominator_hashes) == 4,
            "sign-specialized norms")
    return rows


def verify_replay(payload, cut_rows):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-xi2-pairing0-six-basis-root-replay-census-v1",
            "replay schema")
    require(payload["source_quotient_sha256"] == digest(QUOTIENT),
            "replay quotient custody")
    require(payload["source_kernel_sha256"] == digest(KERNEL),
            "replay kernel custody")
    require(payload["source_product_sha256"] == digest(PRODUCT),
            "replay product custody")
    require(payload["source_pilot_sha256"] == digest(CUT),
            "replay cut custody")
    rows = rows_by_sign(payload, "replay")
    de_values = {}
    for signs, row in rows.items():
        require(row["status"] == "COMPLETE" and row["xi_index"] == 2 and
                row["pairing_index"] == 0, "replay scope")
        require({tuple(value) for value in row["target_lanes_covered"]} == LANES,
                "four target lanes")
        require(row["norm_root_count"] == 8 and
                [item["r"] for item in row["root_rows"]] ==
                cut_rows[signs]["field_roots"], "all norm roots replayed")
        require(collections.Counter(item["status"] for item in row["root_rows"]) ==
                {"ROUTE_BOUNDARY": 5, "CHECKED": 3},
                "replay root partition")
        guarded = []
        zero_points = []
        for root_row in row["root_rows"]:
            if root_row["status"] == "ROUTE_BOUNDARY":
                require(root_row["r_zero_guards"] and not root_row["t_rows"],
                        "route-boundary row")
                continue
            require(not root_row["r_zero_guards"], "live r guard")
            for t_row in root_row["t_rows"]:
                require(t_row["status"] == "CHECKED" and
                        not t_row["tr_zero_guards"], "live t row")
                for b_row in t_row["b_rows"]:
                    require(not b_row["bc_zero_guards"] and
                            b_row["nonzero_cofactor_indices"] == list(range(6)),
                            "guarded common point")
                    require(b_row["a_missing"] % PRIME and
                            b_row["c_denominator"] % PRIME,
                            "recovery units")
                    require(b_row["de_value"] ==
                            (-b_row["source_missing_record"]) % PRIME,
                            "negative-DE sign")
                    point = (root_row["r"], t_row["t"],
                             b_row["b"], b_row["c"])
                    guarded.append(point)
                    de_values[(signs, point)] = b_row["de_value"]
                    if b_row["status"] == "TARGET_FREE_ZERO":
                        require(b_row["target_free_value"] == 0,
                                "target-free zero")
                        zero_points.append(point)
                    else:
                        require(b_row["status"] == "TARGET_FREE_NONZERO" and
                                b_row["target_free_value"] != 0,
                                "target-free nonzero")
        require(len(guarded) == len(set(guarded)) == 4,
                "four guarded common points")
        require(len(zero_points) == len(set(zero_points)) == 2,
                "two target-free points")
        require(set(guarded) == {tuple(value)
                                for value in row["guarded_common_points"]},
                "guarded point summary")
        require(set(zero_points) == {tuple(value)
                                    for value in row["target_free_zero_points"]},
                "zero point summary")
        require(not row["case_excluded"],
                "target-free cut alone does not exclude")
    return rows, de_values


def verify_solver(payload, replay_rows, de_values):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-xi2-pairing0-outside-census-v1",
            "solver schema")
    require(payload["source_kernel_sha256"] == digest(KERNEL),
            "solver kernel custody")
    require(payload["source_replay_sha256"] == digest(REPLAY),
            "solver replay custody")
    rows = rows_by_sign(payload, "solver")
    total_fibers = 0
    total_f_candidates = 0
    for signs, row in rows.items():
        require(row["status"] == "COMPLETE" and row["xi_index"] == 2 and
                row["pairing_index"] == 0 and row["case_excluded"],
                "solver completion")
        require(row["case_count"] == len(row["rows"]) == 8,
                "eight point/lane rows")
        require(not row["witnesses"] and not row["boundary_solutions"] and
                not row["unresolved"], "empty final ledgers")
        points = {tuple(value)
                  for value in replay_rows[signs]["target_free_zero_points"]}
        require({(tuple(item["point"]), tuple(item["sigma"]))
                 for item in row["rows"]} == set(itertools.product(points, LANES)),
                "point/lane Cartesian cover")
        root_counts = collections.Counter()
        for item in row["rows"]:
            point = tuple(item["point"])
            require(item["status"] == "CHECKED" and
                    item["colored_degree"] == 4 and
                    item["de"] == de_values[(signs, point)],
                    "checked negative-DE colored fiber")
            roots = item["f_roots"]
            require(roots is not None and len(roots) == len(set(roots)),
                    "finite f-root list")
            root_counts[len(roots)] += 1
            require({entry["f"] for entry in item["f_rows"]} == set(roots) and
                    len(item["f_rows"]) == len(roots), "f-root replay")
            for entry in item["f_rows"]:
                require(entry["f"] != 0 and entry["status"] == "CHECKED" and
                        entry["u_gcd_degree"] == 0 and
                        entry["u_roots"] == [] and entry["u_rows"] == [],
                        "degree-zero residual gcd")
            total_f_candidates += len(roots)
        require(root_counts == {0: 4, 2: 4},
                "per-sign colored-root partition")
        total_fibers += len(row["rows"])
    require((total_fibers, total_f_candidates) == (32, 32),
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
    cut_rows = verify_cut(load(CUT))
    replay_rows, de_values = verify_replay(load(REPLAY), cut_rows)
    verify_solver(load(SOLVER), replay_rows, de_values)
    verify_dag()
    print("cell=3 xi=2 pairing=0 raw_cases=16 fibers=32 f_candidates=32 witnesses=0")


if __name__ == "__main__":
    main()
