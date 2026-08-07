#!/usr/bin/env python3
"""Reproduce the critical-orbit harness coverage census.

This checks packaging coverage, not mathematical truth. A theorem proved on
paper need not have a Python verifier; a computation claim does need a pinned
result and checker. The pinned exceptions below force a deliberate census
refresh when the critical surface or its harness coverage changes.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAG = ROOT / "dag.json"
CRITICAL_DAG = ROOT / "orbit" / "critical_dag.json"
MANIFEST = ROOT / "tools" / "verifier_manifest.json"

EXPECTED_COUNTS = {
    # 2026-07-27: 147 -> 146 and 49 -> 50. `corridor_ledger` gained a real local
    # verifier (verify_corridor_literal_prime.py, the E-1 literal corridor prime and
    # six-row replay shipped as upstream PR #1107), so it moved out of the md-only
    # bucket. Widened per hard law 8 -- a legitimate change, recorded, not silenced.
    # WAVE-24 (2026-07-27): the proof_sketch re-grade demoted the e1 chain and the
    # zone_b/mca_unsafe/unsafe_at_crossing cluster, so 19 e1 nodes left the critical
    # orbit entirely. md-only 146 -> 131, local-verifier 50 -> 44. Widened per hard
    # law 8: a legitimate re-pricing, recorded, not silenced.
    # 2026-07-27 (averaged_xr false-green cascade): 131 -> 129, 44 -> 43.
    # WAVE-26 (2026-07-27): averaged_xr gained a real verifier and the cascade
    # returned to PROVED; 129 -> 130 md-only, 43 -> 44 local-verifier.
    # 2026-08-06: the complete WCL (1,5) certificate promotes its target and
    # makes the proved weight-four section census an explicit critical parent.
    # Both have local verifiers, so local-verifier 44 -> 46.
    # 2026-08-06 F2 admissibility repair: the generated-field-guarded F2 route
    # is not a requirement of the official exact-slice consumer. Moving that
    # branch off the strict orbit removes four md-only proofs and one legacy-
    # ref-only proof; local verifier coverage is unchanged.
    # 2026-08-06 exact-slice near-tail repair: b2b_near_tail_bound gained an
    # exact integer verifier while remaining PROVED, so one critical proof
    # moves from md-only to local-verifier.
    # 2026-08-06 direct primitive-SP re-pose: the optional F-4/u1 branch
    # leaves strict ancestry. Five proved nodes detach: two md-only and three
    # legacy-ref-only; local verifier coverage is unchanged.
    # 2026-08-07 Conjecture-F false-green repair: four md-only parent nodes
    # return from PROVED to CONDITIONAL. Three new TARGET leaves add no proved
    # harness obligation.
    # The consumer-scope decomposition adds one proof-only SPI interface.
    # LIST route retirement subsequently detaches the 18 proved general-F
    # ancestors, all of which were folder-md-only. The strict FPC5 partition
    # then adds 15 proved suppliers: one proof-only and 14 with local verifiers.
    "folder-md-only": 103,
    "legacy-ref-only": 1,
    "local-verifier": 63,
}

EXPECTED_NO_PROOF = {
    # Manifest migration made five legacy-ref-only PROVED critical nodes own a
    # folder for the first time. node.json is graph metadata, not a proof.
    "f5_lineray_saturation_instrument",
    "f5_wcollision_pair_moment_identity",
    "floor_budget_slack_scan",
    "petal_column_lemma",
    "petal_small_scale_staircase_census",
    "v13_capf_planted_lower_count",
}

EXPECTED_UNREGISTERED_VERIFIER_NODES = {
    "petal_growth",
    "petal_small_scale_staircase_census",
}

KNOWN_TRUTH_STATUS_REVIEW = {
    "far_pair_separation",
    "generator_economy",
    "integer_code_distance_cert",
    "u2_per_row_certifier",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def is_remote(path: Path) -> bool:
    text = "\n" + path.read_text(errors="replace")
    return "\nimport modal\n" in text or "\nfrom modal import App\n" in text


def verifier_paths(node_id: str) -> tuple[list[Path], list[Path], list[Path]]:
    local: list[Path] = []
    remote: list[Path] = []
    unregistered: list[Path] = []
    for tree in ("critical", "background"):
        directory = ROOT / tree / "nodes" / node_id
        if not directory.is_dir():
            continue
        for path in directory.rglob("*.py"):
            if "__pycache__" in path.parts or path.name.endswith("_modal.py"):
                continue
            if path.name.startswith("verify"):
                (remote if is_remote(path) else local).append(path)
            elif "verify" in path.name:
                unregistered.append(path)
    return local, remote, unregistered


def node_directories(node_id: str) -> list[Path]:
    return [
        directory
        for directory in (
            ROOT / "critical" / "nodes" / node_id,
            ROOT / "background" / "nodes" / node_id,
        )
        if directory.is_dir()
    ]


def main() -> None:
    dag = json.loads(DAG.read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    critical = json.loads(CRITICAL_DAG.read_text())
    manifest = json.loads(MANIFEST.read_text())
    proved = [node["id"] for node in critical["nodes"] if node["label"] == "PROVED"]

    # The direct primitive-SP re-pose leaves the F-4/u1 route as evidence. The
    # The Conjecture-F scope decomposition adds one proved interface and one
    # conditional compiler while preserving 28 mathematical leaves.
    require(len(critical["nodes"]) == 231, "critical orbit size drift")
    require(len(proved) == 167, "critical PROVED count drift")

    categories: Counter[str] = Counter()
    no_artifact: set[str] = set()
    no_proof: set[str] = set()
    unregistered_nodes: set[str] = set()

    for node_id in proved:
        node = nodes[node_id]
        directories = node_directories(node_id)
        local, remote, unregistered = verifier_paths(node_id)
        if local:
            category = "local-verifier"
        elif remote:
            category = "remote-only"
        elif any(any(directory.rglob("*.md")) for directory in directories):
            category = "folder-md-only"
        elif node.get("refs"):
            category = "legacy-ref-only"
        else:
            category = "no-artifact"
            no_artifact.add(node_id)
        categories[category] += 1

        critical_folder = ROOT / "critical" / "nodes" / node_id
        if critical_folder.is_dir() and not (critical_folder / "proof.md").is_file():
            no_proof.add(node_id)
        if unregistered and not local:
            unregistered_nodes.add(node_id)

    require(dict(categories) == EXPECTED_COUNTS, f"coverage drift: {dict(categories)}")
    require(not no_artifact, f"artifact drift: {no_artifact}")
    require(no_proof == EXPECTED_NO_PROOF, f"proof-artifact drift: {sorted(no_proof)}")
    require(
        unregistered_nodes == EXPECTED_UNREGISTERED_VERIFIER_NODES,
        f"unregistered verifier drift: {sorted(unregistered_nodes)}",
    )

    scripts = manifest["scripts"]
    remote_launchers = manifest["remote_launchers"]
    xr_verifier = "critical/nodes/xr_highcore_collision_count/verify.py"
    weight5_verifier = "background/nodes/dli_wcl_weight5_first64_mitm_exclusion/verify.py"
    weight5_remote = (
        "background/nodes/dli_wcl_weight5_first64_mitm_exclusion/"
        "notes/verify_search_remote.py"
    )
    require(xr_verifier in scripts, "N6 XR top-level verifier is not registered")
    require(weight5_verifier in scripts, "KB #107 certificate checker is not registered")
    require(weight5_remote in remote_launchers, "KB #107 exhaustive launcher is not registered")

    require(
        "open problem" in nodes["generator_economy"]["statement"].lower(),
        "generator_economy review marker drift",
    )
    require(
        "open problem" in nodes["far_pair_separation"]["statement"].lower(),
        "far_pair_separation review marker drift",
    )
    integer_report = ROOT / "critical/nodes/integer_code_distance_cert/execution_report.json"
    require(
        json.loads(integer_report.read_text()).get("verdict")
        == "left_red_with_execution_report",
        "integer-code status review marker drift",
    )
    require(
        "honest blocker" in nodes["u2_per_row_certifier"]["statement"].lower(),
        "u2 status review marker drift",
    )

    print(
        "CRITICAL_HARNESS_COVERAGE_PASS "
        f"proved={len(proved)} local={categories['local-verifier']} "
        f"md_only={categories['folder-md-only']} "
        f"legacy_only={categories['legacy-ref-only']} "
        f"no_artifact={categories['no-artifact']} "
        f"no_proof={len(no_proof)} "
        f"unregistered_verifier_nodes={len(unregistered_nodes)} "
        f"truth_status_review={len(KNOWN_TRUTH_STATUS_REVIEW)}"
    )


if __name__ == "__main__":
    main()
