#!/usr/bin/env python3
"""Verify the E25 nine-profile exclusion packet."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_n256_s16_e25_nine_profile_exclusion"
ENDPOINT = "e1_n256_s16_e25_endpoint_exclusion"
REDUCTION = "e1_n256_s16_e25_profile_parity_light_reduction"
CONDUCTOR = "e1_n256_proper_conductor_collision_exclusion"
NORM = "collision_norm_criterion"
TARGETS = ("e1_official_prime_exception_control", "unsafe_crossing_family_instantiation")
MAXIMUM_NORM = 689346143769176281255733260656192958605975198224651023251426809106119000068
EXPECTED = {
    "vectors": 2_203_120_896,
    "profile_counts": [12_156, 11_884, 5_526, 416, 632, 238, 812, 16, 6],
    "above_cutoff": [12_156, 11_628, 5_526, 352, 632, 238, 748, 0, 0],
    "full_above_cutoff": [6_944, 6_888, 2_868, 32, 116, 56, 80, 0, 0],
    "minimum_m3": [60, 0, 120, 0, 120, 96, 0, 0, 0],
    "minimum_full_m3": [60, 0, 120, 0, 120, 96, 0, -1, -1],
    "maximum_m3": [912, 1_068, 696, 660, 690, 636, 396, 0, 0],
    "maximum_full_m3": [900, 720, 696, 276, 480, 384, 240, -1, -1],
}


def load_pin() -> dict[str, str]:
    pin = json.loads(Path(__file__).with_name("source_pin.json").read_text())
    for key, path in pin.items():
        if key.endswith("_file"):
            assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == pin[key + "_sha256"]
    return pin


def without_runtime(summary: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in summary.items() if key != "worker_seconds"}


def run_checker(path: Path, marker: str) -> None:
    completed = subprocess.run(
        [sys.executable, str(path)], cwd=ROOT, capture_output=True, text=True, check=True
    )
    assert marker in completed.stdout


def main() -> None:
    pin = load_pin()
    census = json.loads((ROOT / pin["census_result_file"]).read_text())
    assert census["schema"] == "e1-e25-nine-profile-census-v1"
    assert census["complete"] is census["agreement"] is True
    assert census["completed_production"] == census["completed_audit"] == census["expected_each"] == 111
    assert census["source_sha256"] == pin["production_source_file_sha256"]
    assert census["audit_source_sha256"] == pin["audit_source_file_sha256"]
    assert census["driver_sha256"] == pin["census_driver_file_sha256"]
    assert without_runtime(census["production_summary"]) == EXPECTED
    assert without_runtime(census["audit_summary"]) == EXPECTED
    assert sum(EXPECTED["profile_counts"]) == 31_686
    assert sum(EXPECTED["above_cutoff"]) == 31_280
    assert sum(EXPECTED["full_above_cutoff"]) == 16_984
    assert 31_280 - 16_984 == 14_296

    norms = json.loads((ROOT / pin["norm_result_file"]).read_text())
    assert norms["schema"] == "e1-e25-nine-profile-norm-v1"
    assert norms["complete"] is norms["agreement"] is True
    assert norms["source_sha256"] == pin["norm_driver_file_sha256"]
    assert norms["census_sha256"] == pin["census_result_file_sha256"]
    summary = norms["summary"]
    assert summary["vectors"] == 16_984
    assert summary["distinct_norms"] == 3_727
    assert summary["maximum_norm"] == MAXIMUM_NORM
    assert summary["maximum_norm_bits"] == 249
    assert summary["norms_at_or_above_2_250"] == 0
    assert summary["eligible_distinct_odd_parts"] == 0
    assert summary["candidate_vectors"] == 0 and norms["candidate_records"] == []
    assert 2 * MAXIMUM_NORM < 2**250 < 3 * MAXIMUM_NORM

    run_checker(ROOT / pin["census_checker_file"], "E25_NINE_PROFILE_CENSUS_CHECK_PASS")
    run_checker(ROOT / pin["norm_checker_file"], "E25_NINE_PROFILE_NORM_CHECK_PASS")
    production_source = (ROOT / pin["production_source_file"]).read_text()
    audit_source = (ROOT / pin["audit_source_file"]).read_text()
    norm_source = (ROOT / pin["norm_driver_file"]).read_text()
    assert "folded_class" in production_source and "reverse_exponent" not in production_source
    assert "reverse_exponent" in audit_source and "folded_class" not in audit_source
    assert "python-flint" in norm_source and "polresultant" in norm_source

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in (REDUCTION, CONDUCTOR, NORM):
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    assert (NODE, ENDPOINT, "req") in edges
    for target in TARGETS:
        assert (NODE, target, "ev") in edges
    assert "2,203,120,896" in nodes[NODE]["statement"]
    assert "2*N_max<2^250<3*N_max" in nodes[NODE]["statement"]
    print("E1_N256_S16_E25_NINE_PROFILE_EXCLUSION_PASS templates=111 vectors=2203120896 profile=31686 exceptions=31280 full=16984 max_bits=249 engines=4")


if __name__ == "__main__":
    main()
