#!/usr/bin/env python3
"""Compile the current T4 residual frontier for the F3 flip attempt.

This is a ledger over existing proved nodes and certificate audits.  It launches
no new search and does not enumerate h=8 supports.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path

from f3_h5_certificate_coverage_audit import audit as h5_audit
from f3_h5_basefree_reciprocal_system import basefree_summary as h5_basefree_summary
from f3_h5_chart_recovery_compiler import (
    chart_recovery_summary as h5_chart_recovery_summary,
)
from f3_h5_rank_one_unit_propagation import (
    unit_propagation_summary as h5_unit_propagation_summary,
)
from f3_h5_rank_one_minor_propagation import (
    minor_propagation_summary as h5_minor_propagation_summary,
)
from f3_h5_reciprocal_compatibility_compiler import (
    compatibility_summary as h5_reciprocal_summary,
)
from f3_h5_reciprocal_open_cover import open_cover_summary as h5_open_cover_summary
from f3_h5_unit_norm_reciprocal_gate import unit_norm_summary as h5_unit_norm_summary
from f3_h5_x83_triangular_norm_gate import key_bounds as h5_x83_key_bounds
from f3_h6_h8_bonus_sweep_replay import (
    FULL_ZERO_ROWS,
    load_rows,
    require_h6_n64_certificate,
    require_h6_n64_extra_certificate,
    require_h7_n64_certificate,
    require_zero_full,
)
from f3_h8_residual_frontier_audit import (
    PARTIAL_H8_N64,
    require_h8_n32_rows,
    require_partial_h8_n64_rows,
    require_q3_profile,
    require_radius3_certificate,
)
from f3_h8_nonantipodal_aperiodic import count_summary as h8_aperiodic_summary
from f3_h8_rotation_orbit_compiler import EXPECTED as H8_ROTATION_EXPECTED
from f3_h8_support_universe_compiler import EXPECTED as H8_SUPPORT_EXPECTED


ROOT = Path(__file__).resolve().parents[4]
NOTES = ROOT / "critical/nodes/u1_x4_direct_column_budget/notes"


@dataclass(frozen=True)
class FrontierNode:
    name: str
    status: str
    evidence: str
    residual: str


def load_json(name: str):
    return json.loads((NOTES / name).read_text())


def require_dag_status(node_id: str, status: str = "PROVED") -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    by_id = {node["id"]: node for node in dag["nodes"]}
    node = by_id.get(node_id)
    if node is None:
        raise AssertionError(("missing node", node_id))
    if node.get("status") != status:
        raise AssertionError((node_id, node.get("status"), status))


def h5_summary() -> dict[str, int]:
    rows = h5_audit()
    reciprocal = h5_reciprocal_summary()
    basefree = h5_basefree_summary()
    open_cover = h5_open_cover_summary()
    unit_norm = h5_unit_norm_summary()
    chart_recovery = h5_chart_recovery_summary()
    unit_propagation = h5_unit_propagation_summary()
    minor_propagation = h5_minor_propagation_summary()
    by_n = {row["n"]: row for row in rows}
    expected_by_n = {
        32: (402, 65537, 0, 68304222),
        64: (179, 262337, 515, 1258163613),
        96: (1, 9601, 0, 57940519),
        128: (7, 20353, 0, 1779622425),
    }
    actual_by_n = {
        n: (
            row["certified_primes"],
            row["max_certified_prime"],
            row["missing_admissible_primes_to_max"],
            row["total_right_probes"],
        )
        for n, row in by_n.items()
    }
    if actual_by_n != expected_by_n:
        raise AssertionError(actual_by_n)
    return {
        "certified_rows": sum(row["certified_primes"] for row in rows),
        "total_right_probes": sum(row["total_right_probes"] for row in rows),
        "n32_certified_primes": by_n[32]["certified_primes"],
        "n64_certified_primes": by_n[64]["certified_primes"],
        "n64_missing_to_max": by_n[64]["missing_admissible_primes_to_max"],
        "max_x83_low_key_bound": max(
            row.conjugate_bound for row in h5_x83_key_bounds()
        ),
        "reciprocal_compatibility_equations": reciprocal["compatibility_equations"],
        "reciprocal_delta_free_equations": reciprocal["delta_free_equations"],
        "basefree_reciprocal_equations": basefree["pairwise_equations"],
        "reciprocal_charts": open_cover["charts"],
        "official_max_x10_fiber": open_cover["official_max_x10_fiber"],
        "unit_norm_equations": unit_norm["equations"],
        "chart_local_charts": chart_recovery["charts"],
        "chart_incident_minors_per_chart": chart_recovery[
            "incident_minors_per_chart"
        ],
        "chart_nontrivial_unit_charts": chart_recovery["nontrivial_unit_charts"],
        "chart_tautological_unit_charts": chart_recovery[
            "tautological_unit_charts"
        ],
        "central_unit_syzygies": chart_recovery["central_unit_syzygies"],
        "minor_propagation_syzygies": minor_propagation["ordered_chart_syzygies"],
        "nonincident_minors_per_chart": minor_propagation[
            "nonincident_minors_per_chart"
        ],
        "unit_propagation_syzygies": unit_propagation["ordered_syzygies"],
        "max_unit_norm_degree": unit_norm["max_total_degree"],
        "max_reciprocal_compatibility_degree": reciprocal[
            "max_compatibility_total_degree"
        ],
        "max_basefree_reciprocal_degree": basefree["max_total_degree"],
    }


def h6_h7_summary() -> dict[str, int]:
    loaded = {filename: load_rows(filename) for filename in FULL_ZERO_ROWS}
    full_zero_rows = 0
    for filename, names in FULL_ZERO_ROWS.items():
        for name in names:
            require_zero_full(loaded[filename][name])
            full_zero_rows += 1

    h6_n64 = load_json("f3_h6_n64_boundary_certificate.json")
    require_h6_n64_certificate(h6_n64)
    h6_extra = load_json("f3_h6_n64_extra_primes_certificate.json")
    require_h6_n64_extra_certificate(h6_extra)
    h7_n64 = load_json("f3_h7_n64_boundary_certificate.json")
    require_h7_n64_certificate(h7_n64)

    p4993 = next(row for row in h6_extra if row["p"] == 4993)
    if p4993["anchored_nontoral_trades"] != 6:
        raise AssertionError(p4993)
    if p4993["anchored_nontoral_trades"] >= 64**3:
        raise AssertionError(p4993)

    return {
        "n32_h6_h7_full_zero_rows": full_zero_rows,
        "h6_n64_complete_rows": 1 + len(h6_extra),
        "h7_n64_complete_rows": 1,
        "h6_p4993_nontoral": p4993["anchored_nontoral_trades"],
    }


def h8_summary() -> dict[str, int]:
    n32_probes = require_h8_n32_rows()
    require_partial_h8_n64_rows()
    p4289_processed = require_radius3_certificate(
        "f3_h8_n64_x83_radius3_shell_certificate_p4289.json", 4289, 16048
    )
    q3_processed = require_radius3_certificate(
        "f3_h8_n64_x83_radius3_shell_certificate.json", 262337, 320
    )
    require_q3_profile()
    expected_support = {
        "anchored_nonantipodal_supports": 122131731640320,
        "blind_left_records": 553270671,
        "blind_right_records": 3872894697,
        "shell_le_3_workload": 68753223,
        "nonantipodal_rotation_orbits": 7633233227520,
    }
    actual_support = {
        key: H8_SUPPORT_EXPECTED[key]
        for key in (
            "anchored_nonantipodal_supports",
            "blind_left_records",
            "blind_right_records",
            "shell_le_3_workload",
        )
    }
    actual_rotation = {
        "nonantipodal_rotation_orbits": H8_ROTATION_EXPECTED[
            "nonantipodal_rotation_orbits"
        ]
    }
    aperiodic = h8_aperiodic_summary()
    if (
        aperiodic["nonantipodal_rotation_orbits"]
        != actual_rotation["nonantipodal_rotation_orbits"]
    ):
        raise AssertionError((aperiodic, actual_rotation))
    if {**actual_support, **actual_rotation} != expected_support:
        raise AssertionError((actual_support, actual_rotation))
    return {
        "n32_complete_rows": 6,
        "n32_right_probes": n32_probes,
        "n64_partial_rows": len(PARTIAL_H8_N64),
        "radius3_rows": 2,
        "radius3_processed_each": min(p4289_processed, q3_processed),
        "anchored_per_nonantipodal_orbit": aperiodic[
            "anchored_per_nonantipodal_orbit"
        ],
        **actual_support,
        **actual_rotation,
    }


def frontier_nodes(h5: dict[str, int], h6_h7: dict[str, int], h8: dict[str, int]) -> tuple[FrontierNode, ...]:
    return (
        FrontierNode(
            "T4-H4-STRUCTURAL",
            "PROVED",
            "h4_terminal_dichotomy and x83_uniform_square_shift_obstruction_gate are PROVED",
            "no h=4 classification residual; only the downstream sparse norm-gate/certificate column remains",
        ),
        FrontierNode(
            "T4-H5-NORM-GATE",
            "OPEN",
            (
                f"{h5['certified_rows']} complete zero rows; "
                f"n32={h5['n32_certified_primes']} contiguous-through-65537, "
                f"n64={h5['n64_certified_primes']} selected/contiguous rows; "
                f"x83 low-key bound={h5['max_x83_low_key_bound']}; "
                f"base-free reciprocal equations={h5['basefree_reciprocal_equations']}; "
                f"unit-norm equations={h5['unit_norm_equations']}; "
                f"chart-local unit obligations="
                f"{h5['chart_nontrivial_unit_charts']}+"
                f"{h5['chart_tautological_unit_charts']} tautological; "
                f"minor propagation syzygies={h5['minor_propagation_syzygies']}; "
                f"unit propagation syzygies={h5['unit_propagation_syzygies']}"
            ),
            "prove symbolic p-specific x83 norm-gate incompatibility or replace selected rows by a scalable certificate family",
        ),
        FrontierNode(
            "T4-H6-H7-BUDGET",
            "REPLAYED/PAID",
            (
                f"{h6_h7['n32_h6_h7_full_zero_rows']} n32 h6/h7 full zero rows; "
                f"{h6_h7['h6_n64_complete_rows']} h6 n64 complete rows; "
                f"{h6_h7['h7_n64_complete_rows']} h7 n64 complete row"
            ),
            "p4993 has six h=6 nontoral witnesses, below n^3 and routed to the square-lift h=3 packet",
        ),
        FrontierNode(
            "T4-H8-N64-NONANTIPODAL-X83",
            "OPEN",
            (
                f"{h8['n32_complete_rows']} complete n32 rows; "
                f"{h8['n64_partial_rows']} partial n64 rows; "
                f"{h8['radius3_rows']} radius-three x83 shell certificates"
            ),
            (
                "certify "
                f"{h8['anchored_nonantipodal_supports']} non-antipodal supports "
                f"({h8['nonantipodal_rotation_orbits']} aperiodic rotation orbits) "
                "or build a sharded signature join avoiding the blind left table"
            ),
        ),
    )


def main() -> None:
    for node_id in (
        "h4_terminal_dichotomy",
        "x83_uniform_square_shift_obstruction_gate",
    ):
        require_dag_status(node_id)

    h5 = h5_summary()
    h6_h7 = h6_h7_summary()
    h8 = h8_summary()
    nodes = frontier_nodes(h5, h6_h7, h8)

    print("F3/T4 residual frontier ledger")
    for node in nodes:
        print(f"{node.name}: {node.status}")
        print(f"  evidence: {node.evidence}")
        print(f"  residual: {node.residual}")
    print(f"h=5 total right-side probes audited: {h5['total_right_probes']}")
    print(f"h=5 n64 missing admissible primes to max certified prime: {h5['n64_missing_to_max']}")
    print(f"h=5 max x83 low-key conjugate bound: {h5['max_x83_low_key_bound']}")
    print(
        "h=5 reciprocal compatibility: "
        f"pairwise_equations={h5['reciprocal_compatibility_equations']} "
        f"delta_free_equations={h5['reciprocal_delta_free_equations']} "
        f"basefree_equations={h5['basefree_reciprocal_equations']} "
        f"charts={h5['reciprocal_charts']} "
        f"max_x10_fiber={h5['official_max_x10_fiber']} "
        f"unit_norm_equations={h5['unit_norm_equations']} "
        f"chart_local_charts={h5['chart_local_charts']} "
        f"incident_minors_per_chart={h5['chart_incident_minors_per_chart']} "
        f"chart_unit_obligations={h5['chart_nontrivial_unit_charts']}+"
        f"{h5['chart_tautological_unit_charts']} tautological "
        f"nonincident_minors_per_chart={h5['nonincident_minors_per_chart']} "
        f"minor_propagation_syzygies={h5['minor_propagation_syzygies']} "
        f"central_unit_syzygies={h5['central_unit_syzygies']} "
        f"unit_propagation_syzygies={h5['unit_propagation_syzygies']} "
        f"unit_norm_max_degree={h5['max_unit_norm_degree']} "
        f"max_total_degree={h5['max_basefree_reciprocal_degree']}"
    )
    print(f"h=8 n32 right-side probes audited: {h8['n32_right_probes']}")
    print(
        "h=8 blind join scale: "
        f"left={h8['blind_left_records']} right={h8['blind_right_records']}"
    )
    print(f"h=8 aperiodic non-antipodal rotation orbits: {h8['nonantipodal_rotation_orbits']}")
    print(
        "h=8 anchored supports per non-antipodal orbit: "
        f"{h8['anchored_per_nonantipodal_orbit']}"
    )
    print(f"h=8 paid shell radius<=3 workload: {h8['shell_le_3_workload']}")
    print("F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS")


if __name__ == "__main__":
    main()
