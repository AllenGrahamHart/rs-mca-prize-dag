#!/usr/bin/env python3
"""Verify the E1 certificate false-green regression and its dependency cut."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    dag = json.loads((ROOT / "dag.json").read_text(encoding="utf-8"))
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }

    targets = {
        "e1_folded_no_vector_certificate_128_payload",
        "e1_folded_no_vector_certificate_256_payload",
    }
    conditionals = {
        "e1_folded_certificate_cell_128_payload",
        "e1_folded_certificate_cell_256_payload",
        "e1_folded_certificate_manifest_payload",
        "e1_open_cell_control_payload",
        "e1_official_typicality_or_certificate",
        "e1_official_prime_exception_control",
        "e1_fullness",
        "zone_b",
        "mca_unsafe",
    }
    for node_id in targets:
        require(nodes[node_id]["status"] == "TARGET", f"{node_id} is false-green")
    for node_id in conditionals:
        require(
            nodes[node_id]["status"] == "CONDITIONAL",
            f"{node_id} did not regress to CONDITIONAL",
        )

    require(
        "complete machine-checkable folded-kernel certificate"
        in nodes["e1_folded_no_vector_certificate_256_payload"]["statement"],
        "N'=256 statement was silently weakened away from its req contract",
    )
    required_edges = {
        (
            "e1_folded_no_vector_certificate_128_payload",
            "e1_folded_certificate_cell_128_payload",
            "req",
        ),
        (
            "e1_folded_no_vector_certificate_256_payload",
            "e1_folded_certificate_cell_256_payload",
            "req",
        ),
        ("e1_fullness", "zone_b", "req"),
        ("zone_b", "mca_unsafe", "req"),
    }
    require(required_edges <= edges, "E1 regression path changed without audit")

    launcher = (
        ROOT
        / "critical/nodes/e1_folded_no_vector_certificate_128_payload/notes/modal_e1_cert.py"
    ).read_text(encoding="utf-8")
    require("except Exception:" in launcher and "pass" in launcher,
            "historical fallback signature changed; re-audit the ruling")
    require("round(math.sqrt(short_n2), 3)" in launcher,
            "historical rounded-output signature changed; re-audit the ruling")
    require("svp_completed" not in launcher,
            "launcher gained a completion flag; re-audit rather than auto-promote")

    for node_id in targets:
        folder = ROOT / "critical" / "nodes" / node_id
        require((folder / "status_ruling.md").is_file(), f"{node_id} ruling missing")
        require(not (folder / "proof.md").exists(), f"{node_id} retains a proof artifact")

    print(
        "E1_CERTIFICATE_STATUS_REGRESSION_VERIFIED "
        f"targets={len(targets)} conditionals={len(conditionals)}"
    )


if __name__ == "__main__":
    main()
