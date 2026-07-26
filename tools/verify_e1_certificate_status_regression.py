#!/usr/bin/env python3
"""Fail closed on the E1 false-green and named-exhibit quantifier cuts."""

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

    universal = "e1_official_prime_exception_control"
    exhibit_targets = {
        "e1_folded_no_vector_certificate_128_payload",
        "e1_folded_no_vector_certificate_256_payload",
    }
    background_branch = {
        "official_row_primes_pinning",
        "e1_folded_certificate_cell_128_payload",
        "e1_folded_certificate_cell_256_payload",
        "e1_folded_certificate_manifest_payload",
        "e1_folded_certificate_manifest_soundness",
        "e1_folded_certificate_soundness",
        *exhibit_targets,
        "e1_named_field_folded_cell_certificate_soundness",
        "e1_official_typicality_or_certificate",
        "e1_open_cell_control_payload",
        "e1_open_cell_route_soundness",
        "e1_pocklington_250bit_exhibit_field",
        "e1_two_cell_folded_manifest_assembly_soundness",
    }

    require(nodes[universal]["status"] == "TARGET", "universal E1 node is not TARGET")
    universal_statement = nodes[universal]["statement"].lower()
    require("every admissible" in universal_statement, "universal quantifier is missing")
    require(
        "do not discharge" in universal_statement,
        "named exhibits are not explicitly fenced from universal discharge",
    )
    require(
        nodes["official_row_primes_pinning"]["status"] == "PROVED",
        "official quantifier pin is not proved",
    )
    pin_statement = nodes["official_row_primes_pinning"]["statement"].lower()
    require("every admissible" in pin_statement, "official pin lost its family scope")
    require("hidden finite list" in pin_statement, "official pin lost the no-list ruling")

    req_parents = {
        source
        for source, target, kind in edges
        if target == universal and kind == "req"
    }
    require(not req_parents, f"universal E1 TARGET gained req parents: {sorted(req_parents)}")
    evidence_edges = {
        ("official_row_primes_pinning", universal, "ev"),
        ("e1_folded_certificate_soundness", universal, "ev"),
        ("e1_open_cell_control_payload", universal, "ev"),
        ("e1_official_typicality_or_certificate", universal, "ev"),
    }
    require(evidence_edges <= edges, "named-exhibit route is not evidence-only")
    require(
        (universal, "e1_fullness", "req") in edges,
        "corrected universal target no longer gates e1_fullness",
    )

    universal_folder = ROOT / "critical" / "nodes" / universal
    require(universal_folder.is_dir(), "universal E1 target left the critical tree")
    require(
        not (universal_folder / "conditional.md").exists(),
        "invalid named-exhibit conditional proof remains live",
    )
    require(
        (universal_folder / "status_ruling.md").is_file(),
        "universal E1 status ruling is missing",
    )

    for node_id in background_branch:
        require(
            (ROOT / "background" / "nodes" / node_id).is_dir(),
            f"{node_id} is not retained in the background tree",
        )
        require(
            not (ROOT / "critical" / "nodes" / node_id).exists(),
            f"{node_id} leaked back into the critical tree",
        )

    for node_id in exhibit_targets:
        require(nodes[node_id]["status"] == "TARGET", f"{node_id} is false-green")
        folder = ROOT / "background" / "nodes" / node_id
        require((folder / "status_ruling.md").is_file(), f"{node_id} ruling missing")
        require(not (folder / "proof.md").exists(), f"{node_id} retains a proof artifact")

    require(
        "complete machine-checkable folded-kernel certificate"
        in nodes["e1_folded_no_vector_certificate_256_payload"]["statement"],
        "N'=256 exhibit statement was weakened away from its exact contract",
    )
    launcher = (
        ROOT
        / "background/nodes/e1_folded_no_vector_certificate_128_payload/notes/modal_e1_cert.py"
    ).read_text(encoding="utf-8")
    require(
        "except Exception:" in launcher and "pass" in launcher,
        "historical fallback signature changed; re-audit the false-green ruling",
    )
    require(
        "round(math.sqrt(short_n2), 3)" in launcher,
        "historical rounded-output signature changed; re-audit the ruling",
    )
    require(
        "svp_completed" not in launcher,
        "launcher gained a completion flag; re-audit rather than auto-promote",
    )

    require(
        (ROOT / "notes/E1_NAMED_EXHIBIT_QUANTIFIER_AUDIT_20260726.md").is_file(),
        "quantifier audit is missing",
    )
    for node_id in ("e1_fullness", "zone_b", "mca_unsafe"):
        require(nodes[node_id]["status"] == "CONDITIONAL", f"{node_id} status drift")

    print(
        "E1_CERTIFICATE_STATUS_REGRESSION_VERIFIED "
        f"universal_target={universal} background_exhibit_nodes={len(background_branch)}"
    )


if __name__ == "__main__":
    main()
