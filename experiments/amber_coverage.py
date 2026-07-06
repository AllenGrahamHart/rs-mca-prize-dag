#!/usr/bin/env python3
"""Generate a coverage snapshot for amber-node stress testing."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "coverage.md"


SELECTED_VERIFIER_COVERAGE = {
    "list_adjacency_closing": "selected verifiers: list corridor + rate-half local",
    "list_grand": "selected verifiers: list corridor",
    "f1_classification": "selected verifiers: f1_minimal_field_descent + pole-threshold probe; F1 weakening audit",
    "ext_lift": "selected verifier: f1_minimal_field_descent; F1 weakening audit",
    "r2_clean_rates": "selected verifiers: XR arithmetic/qpower/exponent + smallcore triangle + quadrilateral scans",
    "xr_clean_residual_any_gate": "selected verifiers: XR arithmetic/qpower/exponent + smallcore triangle + quadrilateral scans",
    "worst_word_planted": "selected verifiers: E22 two-class + fixed-scale staircase + extended + shuffled-layout censuses",
    "list_planted_arithmetic": "selected verifiers: E22 two-class + fixed-scale staircase + extended + shuffled-layout censuses",
    "strip": "selected verifier: gap2 seam; statement repair",
    "x4_exactlist_staircase_split": "selected verifier: dyadic profile; moment witness harness; U2-C t-null boundary scan; DLI weighted/RES probe; U1-for-X4 direct-column active-core probe",
    "tr_perleaf_list_ident": "selected verifiers: dyadic profile; exact TR quotient dictionary probe",
    "mca_safe": "selected verifiers: bounded scales + MCA delta self-test",
    "safe_assembly_uniformity": "selected verifier: bounded scales",
    "adjacency_closing": "selected verifiers: MCA delta self-test + rate-half local",
    "gap1_product_model": "selected verifiers: GAP-1 telescope algebra; exact TR quotient dictionary probe",
    "gap1_noneq_mass": "selected verifier: GAP-1 telescope algebra; strip repair",
}


MANUAL_COVERAGE = {
    "prize": "selected verifier: assembly/orphan logical surface check",
    "mca_grand": "MCA delta self-test + explicit predicate-packet rewrite",
    "list_grand": "premise weakening audit + selected list corridor checks",
    "packaging": "selected verifier: assembly/orphan logical surface check",
    "mca_safe": "explicit predicate-packet rewrite + selected arithmetic checks",
    "list_safe": "petal fixed-excess verifier exercises imgfib/list-safe surface",
    "imgfib": "petal fixed-excess verifier + petal excess local scan; petal_growth remains red",
    "a_regular_collapse": "selected verifier: assembly/orphan logical surface check",
    "petal_mixed_amplification": "selected verifiers: PMA auxiliary-list probe + correlated-target search",
    "f1_case_pole": "selected verifier: F1 pole-threshold probe; threshold still rides list adjacency",
    "free_pool_ladder": "selected verifiers: assembly/orphan logical surface check + subgroup expsum probe",
    "m_le3_route": "selected verifier: assembly/orphan logical surface check",
    "spi_point_counting": "selected verifiers: SPI/Hankel write-up checks + diffuse-shadow circuit scan",
    "f1_pole_list_threshold_location": "selected verifier: F1 pole-threshold exact arithmetic probe",
    "hankel_slope_large_sieve": "selected verifiers: SPI/Hankel write-up checks + diffuse-shadow circuit scan",
    "aperiodic_zero_at_crossing": "rate-scope repair + XR selected verifiers",
}


def main() -> int:
    dag = json.loads((ROOT / "dag.json").read_text())
    by_id = {node["id"]: node for node in dag["nodes"]}
    reqs: dict[str, list[str]] = {node["id"]: [] for node in dag["nodes"]}
    for edge in dag["edges"]:
        if edge.get("kind") == "req":
            reqs[edge["to"]].append(edge["from"])

    lines = [
        "# Amber Stress Coverage Snapshot",
        "",
        "Generated from the current DAG and the `experiments/amber_stress` harness.",
        "This is a progress ledger, not a completion certificate.",
        "",
        "| amber node | live non-proved reqs | current stress coverage |",
        "| --- | --- | --- |",
    ]
    unlisted: list[str] = []
    no_direct_harness: list[str] = []
    for node in sorted((n for n in dag["nodes"] if n.get("status") == "CONDITIONAL"), key=lambda n: n["id"]):
        nid = node["id"]
        nonproved = [
            rid
            for rid in reqs[nid]
            if by_id.get(rid, {}).get("status") not in {"PROVED", "REFUTED", "TEST"}
        ]
        coverage = SELECTED_VERIFIER_COVERAGE.get(nid) or MANUAL_COVERAGE.get(nid)
        if not coverage:
            coverage = "not directly stressed yet"
            unlisted.append(nid)
        if any(
            marker in coverage
            for marker in [
                "no direct stress harness",
                "not directly stressed yet",
                "inspection only",
                "auditability repair only",
                "retraction cleanup only",
            ]
        ):
            no_direct_harness.append(nid)
        lines.append(
            f"| `{nid}` | {', '.join(f'`{r}`' for r in nonproved) or '-'} | {coverage} |"
        )

    lines.extend(
        [
            "",
            "## Unlisted Amber Nodes",
            "",
        ]
    )
    if unlisted:
        lines.extend(f"- `{nid}`" for nid in unlisted)
    else:
        lines.append("- none by this coarse coverage map")
    lines.extend(
        [
            "",
            "## Nodes Still Lacking A Direct Falsification Harness",
            "",
        ]
    )
    if no_direct_harness:
        lines.extend(f"- `{nid}`" for nid in no_direct_harness)
    else:
        lines.append("- none")
    lines.append("")
    OUT.write_text("\n".join(lines))
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
