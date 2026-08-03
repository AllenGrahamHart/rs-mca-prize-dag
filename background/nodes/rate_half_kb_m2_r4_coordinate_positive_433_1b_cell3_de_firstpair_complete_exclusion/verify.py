#!/usr/bin/env python3
"""Verify the cell-3 DE-first-pair 144-case exclusion."""

import hashlib
import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
SCRIPT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_de_pairings12_direct_solver_modal.py"
RESULT = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_de_pairings12_direct_solver_result.json"
KERNEL = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_compact_kernel_result.json"
REPLAY0 = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_six_basis_cut_root_replay_census_result.json"
REPLAY2 = EXPERIMENTS / "rate_half_kb_positive_433_1b_cell3_xi2_pairing0_six_basis_root_replay_census_result.json"
PARENTS = {
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi0_pairing0_outside_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi1_pairing0_parallel_edge_transport",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell3_xi2_pairing0_outside_exclusion",
}
PINNED = {
    SCRIPT: "b11d23fd9811a3e8a8022aa51812fea638b1d2aa4840482ab4a85325b576b993",
    RESULT: "d5891adf5ba5c3f86c92638c8e72f04d12c4c45fbad8c5ed668416dbee8e3c53",
}
SIGNS = set(itertools.product((-1, 1), repeat=2))
LANES = set(itertools.product((-1, 1), repeat=2))
EXPECTED_MATCHINGS = {
    1: [[0, 1], [2, 4], [3, 5]],
    2: [[0, 1], [2, 5], [3, 4]],
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def residual_signature(xi, pairing_index):
    products = ("de", "de", "-de", "df", "sigma_o*ef",
                "bf", "sigma_c*cf")
    sums = ("(d+e)^2", "(d+e)^2", "(d-e)^2", "(d+f)^2",
            "(e+sigma_o*f)^2", "(b+f)^2", "(c+sigma_c*f)^2")
    product_residual = products[:xi]+products[xi+1:]
    sum_residual = sums[:xi]+sums[xi+1:]
    matching = EXPECTED_MATCHINGS[pairing_index]
    return (
        products[xi], sums[xi],
        tuple((product_residual[left], product_residual[right])
              for left, right in matching),
        tuple((sum_residual[left], sum_residual[right])
              for left, right in matching),
    )


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell3-de-pairings12-direct-solver-v1",
            "schema")
    require(payload["source_kernel_sha256"] == digest(KERNEL),
            "kernel custody")
    require(payload["source_replay0_sha256"] == digest(REPLAY0),
            "positive replay custody")
    require(payload["source_replay2_sha256"] == digest(REPLAY2),
            "negative replay custody")
    expected = set(itertools.product(SIGNS, (0, 2), (1, 2)))
    rows = {}
    degree_zero_gcds = 0
    negative_rootless_points = 0
    positive_root_counts = []
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["xi_index"], row["pairing_index"])
        require(key in expected and key not in rows, "computed Cartesian row")
        rows[key] = row
        xi_index = row["xi_index"]
        pairing_index = row["pairing_index"]
        require(row["matching"] == EXPECTED_MATCHINGS[pairing_index],
                "canonical matching")
        require(row["status"] == "COMPLETE" and row["case_excluded"] and
                not row["witnesses"] and not row["boundary_solutions"] and
                not row["unresolved"], "complete exclusion row")
        expected_points = 4 if xi_index == 0 else 2
        require(row["point_count"] == len(row["rows"]) == expected_points,
                "proved common-point custody")
        for point_row in row["rows"]:
            require(point_row["status"] == "CHECKED" and
                    point_row["d_degree"] == 4,
                    "checked missing-sum quartic")
            require({tuple(lane["sigma"]) for lane in point_row["lanes"]} == LANES and
                    len(point_row["lanes"]) == 4,
                    "four target lanes")
            if xi_index == 2:
                require(point_row["de"] ==
                        (-point_row["source_missing"]) % 2130706433,
                        "negative-DE sign")
                require(point_row["d_roots"] == [] and
                        all(lane["d_rows"] == []
                            for lane in point_row["lanes"]),
                        "negative-DE quartic rootless")
                negative_rootless_points += 1
                continue
            require(point_row["de"] == point_row["source_missing"],
                    "positive-DE sign")
            require(len(point_row["d_roots"]) ==
                    len(set(point_row["d_roots"])) and
                    len(point_row["d_roots"]) in (0, 4),
                    "positive-DE d-root partition")
            positive_root_counts.append(len(point_row["d_roots"]))
            for lane in point_row["lanes"]:
                require({item["d"] for item in lane["d_rows"]} ==
                        set(point_row["d_roots"]) and
                        len(lane["d_rows"]) == len(point_row["d_roots"]),
                        "d-root replay by lane")
                for d_row in lane["d_rows"]:
                    require(d_row["status"] == "CHECKED" and
                            d_row["f_gcd_degree"] == 0 and
                            d_row["f_roots"] == [] and
                            d_row["f_rows"] == [],
                            "degree-zero f gcd")
                    degree_zero_gcds += 1
    require(set(rows) == expected and len(rows) == 16,
            "16 computed rows")
    require(degree_zero_gcds == 256, "256 positive-DE gcd decisions")
    require(positive_root_counts.count(0) == 16 and
            positive_root_counts.count(4) == 16,
            "positive-DE quartic root census")
    require(negative_rootless_points == 16,
            "16 negative-DE rootless point rows")

    for pairing_index in (1, 2):
        require(residual_signature(0, pairing_index) ==
                residual_signature(1, pairing_index),
                "positive parallel-copy transport")
    return 64, 32


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    require(all(parent in nodes and nodes[parent]["status"] == "PROVED"
                for parent in PARENTS), "proved parents")
    edges = {(row["from"], row["to"], row["kind"])
             for row in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "parent edges")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "consumer edge")


def main():
    for path, expected in PINNED.items():
        require(digest(path) == expected, f"digest {path.name}")
    computed, transported = verify_payload(json.loads(RESULT.read_text()))
    require(48+computed+transported == 144, "aggregate raw-case count")
    verify_dag()
    print("cell=3 xi=0,1,2 pairings=0,1,2 raw_cases=144 computed=64 transported=32")


if __name__ == "__main__":
    main()
