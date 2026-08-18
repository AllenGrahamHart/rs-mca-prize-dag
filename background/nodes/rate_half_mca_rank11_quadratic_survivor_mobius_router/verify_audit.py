#!/usr/bin/env python3
"""Independent audit of the quadratic survivor Mobius router."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "9f3f2ec95488d364e8961e1a468c09f907d24f11caa75974d526c5ef82dde175"


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    assert data["minimum_synchronized_fibers"] == 4370
    assert data["minimum_nonfixed_graph_points"] == 2 * 4370 == 8740
    assert data["allowed_exception_degrees"] == list(range(1, 12))
    assert data["retained_nonquadratic_degrees"] == [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert data["quadratic_classes"] == [
        "antipodal",
        "constant-product",
        "shifted-inversion",
    ]

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_nonzero_affine_reflection_mass_router"]["status"] == "PROVED"
    assert nodes[
        "rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_pair_locator_mobius_dichotomy"
    ]["status"] == "PROVED"

    proof = " ".join((HERE / "proof.md").read_text().lower().split())
    frontier = " ".join((HERE / "frontier.md").read_text().lower().split())
    assert "no closure-field descent is required" in proof
    assert "the `r` pairs are disjoint" in proof
    assert "does not control this two-parameter family" in frontier
    assert "does not pay" in data["nonclaim"].lower()
    checker = ROOT / "experiments/prize_resolution/verify_rate_half_mca_rank11_shifted_inversion_probe.py"
    completed = subprocess.run(
        [sys.executable, str(checker)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=15,
    )
    assert completed.returncode == 0, completed.stderr
    assert "SHIFTED_INVERSION_PROBE_PASS" in completed.stdout
    print("RANK11_QUADRATIC_MOBIUS_ROUTER_AUDIT_PASS graph_points=8740")


if __name__ == "__main__":
    main()
