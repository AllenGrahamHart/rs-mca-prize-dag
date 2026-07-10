#!/usr/bin/env python3
"""Top-level residual frontier ledger for the F3 flip attempt.

This is a bookkeeping layer over the current T3, h=3, and T4 ledgers.  It
launches no search and does not promote the F3 flip.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path

from f3_h3_conic_bridge_accounting_ledger import conic_bridge_accounting_summary
from f3_h3_frontier_ledger import (
    activation_summary,
    frontier_gates,
    l2_bridge_summary,
    official_budget_summary,
    rank_capacity_summary,
    repeat_count_route_summary,
    repeat_frontier_summary,
    repeat_loose_geometry_summary,
    repeat_slope_summary,
    repeat_value_summary,
    rich_curve_condition_summary,
)
from f3_t3_constant_campaign_ledger import t3_summary


ROOT = Path(__file__).resolve().parents[4]
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"

H3_GATE_NAMES = (
    "H3-ACT-COMPILER",
    "F3-RANK-AVOID / RC-NV",
    "H3-BRIDGE-RANKCAP",
    "F3-PRIVATE-LINEAR-RANK-AVOID",
    "H3-REPEAT-BOUNDARY-STAR",
)

T4_NODE_NAMES = (
    "T4-H4-STRUCTURAL",
    "T4-H5-NORM-GATE",
    "T4-H6-H7-BUDGET",
    "T4-H8-N64-NONANTIPODAL-X83",
)


@dataclass(frozen=True)
class T4FrontierNode:
    name: str
    status: str
    residual: str


def require_dag_status(node_id: str, status: str = "PROVED") -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    by_id = {node["id"]: node for node in dag["nodes"]}
    node = by_id.get(node_id)
    if node is None:
        raise AssertionError(("missing node", node_id))
    if node.get("status") != status:
        raise AssertionError((node_id, node.get("status"), status))


def h3_gate_rows():
    activation = activation_summary()
    budgets = official_budget_summary()
    capacity = rank_capacity_summary()
    l2 = l2_bridge_summary()
    conic = conic_bridge_accounting_summary()
    repeat = repeat_frontier_summary()
    repeat_count = repeat_count_route_summary()
    repeat_value = repeat_value_summary()
    repeat_slope = repeat_slope_summary()
    repeat_loose = repeat_loose_geometry_summary()
    rich_curve_conditions = rich_curve_condition_summary()
    gates = frontier_gates(
        activation,
        budgets,
        capacity,
        l2,
        conic,
        repeat,
        repeat_count,
        repeat_value,
        repeat_slope,
        repeat_loose,
        rich_curve_conditions,
    )
    names = tuple(gate.name for gate in gates)
    if names != H3_GATE_NAMES:
        raise AssertionError(names)
    return gates, activation, budgets, repeat, repeat_count, repeat_loose


def t4_node_rows():
    """Return the pinned T4 residual state without replaying the heavy audit."""

    for node_id in (
        "h4_terminal_dichotomy",
        "x83_uniform_square_shift_obstruction_gate",
    ):
        require_dag_status(node_id)

    note = (NOTES / "F3_T4_RESIDUAL_FRONTIER_LEDGER.md").read_text()
    required_snippets = (
        "Status: FRONTIER LEDGER — SCOPE RETRACTED 2026-07-10 (see banner); artifacts replayed, official-row T4 frontier = h>=4 band.",
        "T4-H4-STRUCTURAL: PROVED",
        "T4-H5-NORM-GATE: SCOPE-RETRACTED 2026-07-10",
        "T4-H6-H7-BUDGET: SAMPLED-ROW EVIDENCE ONLY",
        "T4-H8-N64-NONANTIPODAL-X83: OPEN",
        "122,131,731,640,320 anchored non-antipodal 16-supports",
        "7,633,233,227,520 aperiodic rotation orbits",
        "F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS",
    )
    missing = tuple(snippet for snippet in required_snippets if snippet not in note)
    if missing:
        raise AssertionError(missing)

    nodes = (
        T4FrontierNode(
            "T4-H4-STRUCTURAL",
            "PROVED",
            "no h=4 classification residual",
        ),
        T4FrontierNode(
            "T4-H5-NORM-GATE",
            "SCOPE-RETRACTED 2026-07-10",
            "h=5 official-row residual OPEN (conjugation guardrail)",
        ),
        T4FrontierNode(
            "T4-H6-H7-BUDGET",
            "SAMPLED-ROW EVIDENCE ONLY",
            "h=6/h=7 official rows OPEN (n=32/64 evidence only)",
        ),
        T4FrontierNode(
            "T4-H8-N64-NONANTIPODAL-X83",
            "OPEN",
            "certify the non-antipodal support universe or replace the blind join",
        ),
    )
    h5 = {"certified_rows": 589}
    h6_h7 = {"n32_h6_h7_full_zero_rows": 11}
    h8 = {
        "anchored_nonantipodal_supports": 122_131_731_640_320,
        "nonantipodal_rotation_orbits": 7_633_233_227_520,
    }
    names = tuple(node.name for node in nodes)
    if names != T4_NODE_NAMES:
        raise AssertionError(names)
    return nodes, h5, h6_h7, h8


def residual_data():
    t3 = t3_summary()
    h3_gates, activation, budgets, repeat, repeat_count, repeat_loose = h3_gate_rows()
    t4_nodes, h5, h6_h7, h8 = t4_node_rows()

    h3_frontier_items = tuple(
        gate for gate in h3_gates if "OPEN" in gate.status or "CONDITIONAL" in gate.status
    )
    t4_open_nodes = tuple(node for node in t4_nodes if "OPEN" in node.status)
    expected_t4_open = ("T4-H8-N64-NONANTIPODAL-X83",)
    if tuple(node.name for node in t4_open_nodes) != expected_t4_open:
        raise AssertionError(t4_open_nodes)

    summary = {
        "official_rows": t3["official_rows"],
        "h2_external_import_rows": t3["h2_external_import_rows"],
        "h2_inhouse_residual_rows": t3["h2_residual_rows"],
        "h3_conditional_rows": t3["h3_conditional_rows"],
        "h3_accident_c": t3["h3_accident_c"],
        "h3_threshold": t3["h3_threshold"],
        "h3_official_max_safe_c": t3["h3_official_max_safe_c"],
        "h3_midpoint_c": t3["h3_midpoint_c"],
        "h3_midpoint_first_ratio_ppm": t3["h3_midpoint_first_ratio_ppm"],
        "h3_frontier_items": len(h3_frontier_items),
        "h3_activation_oriented": activation["oriented_activations"],
        "h3_activation_deduped_orbits": activation["deduped_orbits"],
        "h3_activation_max_deduped_count": activation["max_deduped_count"],
        "h3_exact_z_min": budgets["z_exact_profile_min"],
        "h3_exact_z_max": budgets["z_exact_profile_max"],
        "h3_exact_4096_z_min": budgets["z_exact_4096_min"],
        "h3_exact_4096_z_max": budgets["z_exact_4096_max"],
        "h3_exact_min_allowed_deficit": budgets["exact_profile_min_allowed_deficit"],
        "h3_exact_4096_min_allowed_deficit": budgets[
            "exact_4096_min_allowed_deficit"
        ],
        "h3_conic_4096_balanced_margin": budgets[
            "conic_kernel_4096_balanced_margin"
        ],
        "h3_conic_4096_margin_minus_allowance": budgets[
            "conic_kernel_4096_margin_minus_allowance"
        ],
        "h3_private_min_allowed_deficit": budgets["private_min_allowed_deficit"],
        "h3_repeat_strict_gates": len(repeat),
        "h3_repeat_count_route_open_gates": repeat_count["open_gates"],
        "h3_loose_shared_core_total": repeat_loose["shared_sum_total"],
        "h3_loose_shared_core_rank_target": repeat_loose[
            "shared_core_rank_rank_target"
        ],
        "t4_frontier_nodes": len(t4_nodes),
        "t4_open_nodes": len(t4_open_nodes),
        "h5_certified_rows": h5["certified_rows"],
        "h6_h7_full_zero_rows": h6_h7["n32_h6_h7_full_zero_rows"],
        "h8_anchored_nonantipodal_supports": h8[
            "anchored_nonantipodal_supports"
        ],
        "h8_nonantipodal_rotation_orbits": h8[
            "nonantipodal_rotation_orbits"
        ],
        "f3_flip_ready": 0,
    }
    expected = {
        "official_rows": 29,
        "h2_external_import_rows": 29,
        "h2_inhouse_residual_rows": 4,
        "h3_conditional_rows": 29,
        "h3_accident_c": 16,
        "h3_threshold": 17,
        "h3_official_max_safe_c": 8191,
        "h3_midpoint_c": 4096,
        "h3_midpoint_first_ratio_ppm": 500001,
        "h3_frontier_items": 5,
        "h3_activation_oriented": 720,
        "h3_activation_deduped_orbits": 167,
        "h3_activation_max_deduped_count": 27,
        "h3_exact_z_min": 33,
        "h3_exact_z_max": 21421,
        "h3_exact_4096_z_min": 2112,
        "h3_exact_4096_z_max": 1370944,
        "h3_exact_min_allowed_deficit": 1847,
        "h3_exact_4096_min_allowed_deficit": 2899,
        "h3_conic_4096_balanced_margin": 2951,
        "h3_conic_4096_margin_minus_allowance": 52,
        "h3_private_min_allowed_deficit": 25,
        "h3_repeat_strict_gates": 7,
        "h3_repeat_count_route_open_gates": 6,
        "h3_loose_shared_core_total": 14,
        "h3_loose_shared_core_rank_target": 1049,
        "t4_frontier_nodes": 4,
        "t4_open_nodes": 1,
        "h5_certified_rows": 589,
        "h6_h7_full_zero_rows": 11,
        "h8_anchored_nonantipodal_supports": 122_131_731_640_320,
        "h8_nonantipodal_rotation_orbits": 7_633_233_227_520,
        "f3_flip_ready": 0,
    }
    if summary != expected:
        raise AssertionError(summary)
    return summary, h3_gates, t4_nodes


def main() -> None:
    summary, h3_gates, t4_nodes = residual_data()

    print("F3 residual frontier ledger")
    print("status: OPEN; this is not an F3 flip dossier")
    print(
        "T3: "
        f"h2 external import closes {summary['h2_external_import_rows']} official rows; "
        f"in-house h2 residual rows={summary['h2_inhouse_residual_rows']}; "
        f"H3-ACCIDENT({summary['h3_accident_c']}) would cover "
        f"{summary['h3_conditional_rows']} rows from n>={summary['h3_threshold']}"
    )
    print(
        "T3 official h=3 slack: "
        f"max_safe_C={summary['h3_official_max_safe_c']} "
        f"midpoint_C={summary['h3_midpoint_c']} "
        f"midpoint_first_ratio_ppm={summary['h3_midpoint_first_ratio_ppm']}"
    )
    print("h=3 frontier items:")
    for gate in h3_gates:
        print(f"  {gate.name}: {gate.status}")
        print(f"    residual: {gate.residual}")
    print(
        "h=3 key budgets: "
        f"activation_oriented={summary['h3_activation_oriented']} "
        f"activation_deduped_orbits={summary['h3_activation_deduped_orbits']} "
        f"deduped_max_per_prime={summary['h3_activation_max_deduped_count']} "
        f"Z_exact={summary['h3_exact_z_min']}..{summary['h3_exact_z_max']} "
        f"Z_exact_4096_floor={summary['h3_exact_4096_z_min']}.."
        f"{summary['h3_exact_4096_z_max']} "
        f"exact_deficit_min={summary['h3_exact_min_allowed_deficit']} "
        f"exact_4096_deficit_min="
        f"{summary['h3_exact_4096_min_allowed_deficit']} "
        f"conic_4096_margin={summary['h3_conic_4096_balanced_margin']} "
        f"conic_4096_margin_minus_allowance="
        f"{summary['h3_conic_4096_margin_minus_allowance']} "
        f"private_deficit_min={summary['h3_private_min_allowed_deficit']} "
        f"repeat_strict_gates={summary['h3_repeat_strict_gates']} "
        f"repeat_count_route_open={summary['h3_repeat_count_route_open_gates']} "
        f"loose_shared_core_total={summary['h3_loose_shared_core_total']} "
        f"loose_shared_core_rank_target="
        f"{summary['h3_loose_shared_core_rank_target']}"
    )
    print("T4 frontier nodes:")
    for node in t4_nodes:
        print(f"  {node.name}: {node.status}")
        print(f"    residual: {node.residual}")
    print(
        "T4 key budgets: "
        f"h5_certified_rows={summary['h5_certified_rows']} "
        f"h6_h7_full_zero_rows={summary['h6_h7_full_zero_rows']} "
        f"h8_anchored_nonantipodal_supports="
        f"{summary['h8_anchored_nonantipodal_supports']} "
        f"h8_rotation_orbits={summary['h8_nonantipodal_rotation_orbits']}"
    )
    print("F3 residual blockers: h=3 frontier plus T4 h=8 non-antipodal x83")
    print("F3_FLIP_RESIDUAL_FRONTIER_LEDGER_PASS")


if __name__ == "__main__":
    main()
