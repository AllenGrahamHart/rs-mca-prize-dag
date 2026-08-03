#!/usr/bin/env python3
"""Verify the positive 433-1b cell-14 all-mixed exclusion."""

import gzip
import hashlib
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXPERIMENTS = ROOT / "experiments/prize_resolution"
NODE_ID = NODE.name
FILES = {
    "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_modal.py":
        "b5914205877e7d3e8a14cd02a1f57024b521a83f64206b77c18a971baf707d12",
    "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_result.json":
        "ae69b532ebdfa61b84d78b595a4f87636e6bb5515cf8d33391e21f45c8a00d9f",
    "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_root_replay_modal.py":
        "134761bc4395fb0c0f7af6668ea2777d0c85fa088c5ee8226204731a42817cc1",
    "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_root_replay_result.json":
        "ca8d4145e48395d25fe3278d0c4c1ab2fe026429a5cfa013da11f6aaa30f8b89",
    "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_census_modal.py":
        "7f7fa46ee7565c19f718ee7d2a6ed436e9750c6909349d1244f41cb293fae0e1",
    "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_census_result.json":
        "ffb1fa027da69b1226fe0df5d662e354e022238f4dfd3244eb03e52c3821cd2f",
}
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell14_quadratic_curve_structure",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0a_signed_edge_atlas",
    "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell14_rankone_target_projection_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell14_fixed_a_rankone_chain_exclusion",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    # Custody hash of the RAW ledger bytes. Ledgers above GitHub's 100 MB
    # limit are stored gzip-compressed (wave-43 integration, dli_wcl
    # precedent); the pinned sha256 is unchanged — it is taken over the
    # decompressed stream.
    result = hashlib.sha256()
    opener = (lambda: gzip.open(path.with_name(path.name + ".gz"), "rb")) \
        if not path.exists() else (lambda: path.open("rb"))
    with opener() as handle:
        for block in iter(lambda: handle.read(1024*1024), b""):
            result.update(block)
    return result.hexdigest()


def verify_payload(payload):
    require(payload["schema"] ==
            "rate-half-kb-positive-433-1b-cell14-allmixed-census-v1", "schema")
    require(payload["status"] == "PASS", "status")
    require(payload["case_count"] == 144, "case census")
    require(payload["root_count"] == 2992 and
            payload["guard_boundary_count"] == 1808 and
            payload["checked_root_count"] == 1184, "root census")
    require(payload["common_factor_root_count"] == 960 and
            payload["factor_no_weight_root_count"] == 192 and
            payload["factor_excluded_count"] == 768, "factor census")
    require(payload["factor_weight_branch_count"] == 960 and
            payload["factor_f_root_count"] == 0 and
            payload["factor_boundary_solution_count"] == 0, "factor fibers")
    require(payload["residual_outer_root_count"] == 0 and
            payload["direct_fiber_count"] == 0 and
            payload["target_boundary_count"] == 0, "residual fibers")
    require(payload["maximum_eliminant_degree"] == 85536 and
            payload["maximum_eliminant_terms"] == 81489 and
            payload["eliminant_bytes"] == 230008092, "eliminant census")
    for key, name in (
        ("compiler_sha256", "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_modal.py"),
        ("ledger_sha256", "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_result.json"),
        ("replay_script_sha256", "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_root_replay_modal.py"),
        ("replay_sha256", "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_root_replay_result.json"),
        ("source_script_sha256", "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_census_modal.py"),
    ):
        require(payload[key] == FILES[name], f"payload custody: {name}")


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
        "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_allmixed_census_result.json").read_text())
    verify_payload(payload)
    verify_dag()
    print("cell14 all-mixed: cases=144 roots=2992 cell14=1680/1680")


if __name__ == "__main__":
    main()
