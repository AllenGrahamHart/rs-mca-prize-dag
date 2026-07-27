#!/usr/bin/env python3
"""Verify the source-pinned E1 first-band variance route cut."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
NODE = "e1_first_band_variance_route_boundary"
DEPENDENCY = "collision_norm_criterion"
TARGETS = {"e1_official_prime_exception_control", "unsafe_crossing_family_instantiation"}
UPSTREAM_ROOT = HERE / "upstream" / "rs-mca"
EXPECTED_PASS = (
    "E1_FIRST_BAND_VARIANCE_ROUTE_BOUNDARY_PASS "
    "fitted=[1947, 1732, 1517] out_of_sample=[1302, 1087] "
    "slope_in=(107,108) last_live_even_V=50 threshold_at_50=13 "
    "dead_even_V=2..48 mutations=2"
)


def main() -> None:
    pin = json.loads((HERE / "source_pin.json").read_text())
    assert pin["upstream_head_commit"] == "52775686c8f181c08d36de66d3ce0d3b556f8d74"
    expected_files = {
        "upstream_certificate_file",
        "upstream_note_file",
        "upstream_verifier_file",
        "collision_norm_statement_file",
        "collision_norm_proof_file",
    }
    assert {key for key in pin if key.endswith("_file")} == expected_files
    for key in expected_files:
        path = ROOT / pin[key]
        assert path.is_file(), path
        assert hashlib.sha256(path.read_bytes()).hexdigest() == pin[key + "_sha256"]

    certificate = json.loads((ROOT / pin["upstream_certificate_file"]).read_text())
    assert certificate["schema"] == "rs-mca-e1-first-band-variance-route-boundary-v1"
    assert certificate["status"].startswith("PROVED_ROUTE_CUT_TOOL_RELATIVE")
    assert certificate["band"] == {
        "N": 256, "folded_profile": [3, 4, 0], "square_mass": 16
    }
    assert certificate["boundary"] == {
        "affine_in_V": True,
        "slope_bracket": [107, 108],
        "last_live_even_V": 50,
        "threshold_at_V_50": 13,
        "dead_even_V_range": [2, 48],
        "zero_crossing_approx": 49.9,
    }
    bound_hashes = {item["path"]: item["sha256"] for item in certificate["source_bindings"]}
    assert bound_hashes["experimental/notes/e1/e1_first_band_variance_route_boundary_v1.md"] == pin["upstream_note_file_sha256"]
    assert bound_hashes["experimental/scripts/verify_e1_first_band_variance_route_boundary_v1.py"] == pin["upstream_verifier_file_sha256"]

    run = subprocess.run(
        [sys.executable, "experimental/scripts/verify_e1_first_band_variance_route_boundary_v1.py"],
        cwd=UPSTREAM_ROOT,
        text=True,
        capture_output=True,
        timeout=30,
        check=False,
    )
    assert run.returncode == 0, run.stderr
    assert run.stdout.strip() == EXPECTED_PASS

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[NODE]["closure"] == "proof"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    incoming = {source for source, target, kind in edges if target == NODE and kind == "req"}
    assert incoming == {DEPENDENCY}
    assert all((NODE, target, "ev") in edges for target in TARGETS)
    assert "decides no variance level" in nodes[NODE]["statement"]

    ledger = (ROOT / "notes/correspondence/UPSTREAM_IMPORT_LEDGER.md").read_text()
    crosswalk = json.loads((ROOT / "notes/correspondence/JOINT_CROSSWALK.json").read_text())
    assert "first-band cubic-Hermite route boundary" in ledger
    rows = {row["our_node"]: row for row in crosswalk["rows"] if row["our_node"]}
    assert rows[NODE]["status_ours"] == "PROVED"
    assert rows[NODE]["relation"] == "IDENTICAL"

    print("E1_FIRST_BAND_VARIANCE_ROUTE_BOUNDARY_LOCAL_PASS pins=5 thresholds=6 dead_levels=24 edges=3 upstream_mutations=2")


if __name__ == "__main__":
    main()
