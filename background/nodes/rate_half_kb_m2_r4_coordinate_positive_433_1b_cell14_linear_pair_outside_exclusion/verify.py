#!/usr/bin/env python3
"""Verify the positive 433-1b cell-14 linear-pair outside exclusion."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "rate_half_kb_positive_433_1b_cell14_generic_fiber_modal.py":
        "cbac2c88c6706485cdb6b09241a0cb4781ea5e117c696f4312be6967e9c18fb0",
    "rate_half_kb_positive_433_1b_cell14_linear_pair_census.py":
        "7158a1ee9e4409da5fc106aa11b75f66eba6713c0bc20ae6a42687a796d750a2",
    "rate_half_kb_positive_433_1b_cell14_linear_pair_census_result.json":
        "c0c43e981b05106e3dbb18c7659a59ca2e7ddded7252a07d13c9b4dcc305fdda",
    "rate_half_kb_positive_433_1b_cell14_linear_pair_pairing0_complete_result.json":
        "f6c6b654aecfb2c4052f8bc0bef4886cde5c4e959416b41b408a4b460279eed1",
    "rate_half_kb_positive_433_1b_cell14_linear_pair_pairings1_2_open_result.json":
        "ffcea7b92953804deaec7bb2f5072e214c98181e0827334f4e174ef0a056438c",
    "rate_half_kb_positive_433_1b_cell14_linear_pair_xi0_1_pairings1_2_boundary_result.json":
        "52d6f3aa755fee4d40bb9031d6a3d5d3e212cb9fa01814116ecd575d802be1fe",
    "rate_half_kb_positive_433_1b_cell14_linear_pair_xi2_pairings1_2_boundary_result.json":
        "be71d5fa64b74a2f8557f0b8a4317bd6d805fbe97deb9bdf70c20ada8379bc65",
    "rate_half_kb_positive_433_1b_cell14_linear_pair_xi2_boundary_timeout_replay_result.json":
        "e34ed7a1adaec7d3a7e1c699295b1d67ccfb54de74c206f177781a242bc41b3b",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell14_quadratic_curve_structure",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell14-linear-pair-census-v1",
            "schema")
    require(payload["field"] == 2130706433, "field")
    require(payload["logical_case_count"] == 144 and
            payload["open_ideal_count"] == 144 and
            payload["boundary_ideal_count"] == 1632 and
            payload["unit_ideal_count"] == 1776, "ideal census")
    require(payload["raw_outside_case_count"] == 1680 and
            payload["excluded_outside_case_count"] == 144 and
            payload["retained_outside_case_count"] == 1536, "scope census")
    expected = set(itertools.product(
        itertools.product((-1, 1), repeat=2),
        itertools.product((-1, 1), repeat=2),
        range(3), range(3),
    ))
    rows = {}
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), tuple(row["sigma"]),
               row["xi_index"], row["pairing_index"])
        require(key not in rows, "duplicate logical row")
        rows[key] = row
        count = 12 if row["xi_index"] in (0, 1) else 10
        require(row["boundary_factor_count"] == count and
                len(row["boundary_program_sha256"]) == count,
                f"boundary count: {key}")
        hashes = [row["open_program_sha256"], row["open_cut_sha256"],
                  *row["boundary_program_sha256"]]
        require(all(len(value) == 64 for value in hashes), f"digests: {key}")
    require(set(rows) == expected and len(rows) == 144, "Cartesian coverage")
    for epsilon, sigma, pairing_index in itertools.product(
            itertools.product((-1, 1), repeat=2),
            itertools.product((-1, 1), repeat=2), range(3)):
        left = rows[(epsilon, sigma, 0, pairing_index)]
        right = rows[(epsilon, sigma, 1, pairing_index)]
        require(left["open_program_sha256"] == right["open_program_sha256"] and
                left["boundary_program_sha256"] ==
                right["boundary_program_sha256"], "duplicate de-role identity")
    require(len({row["open_program_sha256"] for row in rows.values()}) == 96,
            "open program census")
    require(len({value for row in rows.values()
                 for value in row["boundary_program_sha256"]}) == 736,
            "boundary program census")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED", "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"parent: {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")


def main():
    for name, expected in FILES.items():
        require(digest(EXPERIMENTS / name) == expected, f"custody: {name}")
    payload = json.loads((EXPERIMENTS /
        "rate_half_kb_positive_433_1b_cell14_linear_pair_census_result.json").read_text())
    verify_payload(payload)
    verify_dag()
    print("cell14 linear-pair outside exclusion: cases=144 unit_ideals=1776")


if __name__ == "__main__":
    main()
