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
from f3_h5_central_chart_graph import central_graph_summary as h5_central_graph_summary
from f3_h5_central_fixedpoint_skeleton import (
    fixedpoint_skeleton_summary as h5_central_fixedpoint_summary,
)
from f3_h5_central_slice_fixedpoint_skeleton import (
    slice_fixedpoint_summary as h5_central_slice_fixedpoint_summary,
)
from f3_h5_central_slice_tangent import (
    slice_tangent_summary as h5_central_slice_tangent_summary,
)
from f3_h5_central_slice_quadratic_normal_form import (
    quadratic_normal_form_summary as h5_central_slice_quadratic_summary,
)
from f3_h5_central_slice_cubic_normal_form import (
    cubic_normal_form_summary as h5_central_slice_cubic_summary,
)
from f3_h5_central_slice_formal_isolation import (
    formal_isolation_summary as h5_central_slice_formal_isolation_summary,
)
from f3_h5_central_finite_scheme_payment import (
    finite_scheme_payment_summary as h5_central_finite_payment_summary,
)
from f3_h5_central_infinity_flag import (
    infinity_flag_summary as h5_central_infinity_flag_summary,
)
from f3_h5_central_projective_infinity_exclusion import (
    projective_infinity_exclusion_summary as h5_central_projective_summary,
)
from f3_h5_central_weighted_slice import (
    central_slice_summary as h5_central_slice_summary,
)
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
from f3_h5_weighted_homogeneity import (
    weighted_homogeneity_summary as h5_weighted_summary,
)
from f3_h5_official_scaling_action import (
    official_scaling_summary as h5_scaling_summary,
)
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
from f3_h8_reciprocal_compatibility_compiler import (
    reciprocal_compatibility_summary as h8_reciprocal_summary,
)
from f3_h8_x83_parity_reduction import parity_reduction_summary as h8_parity_summary
from f3_h8_x83_triangular_obstruction import h8_triangular_summary


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
    central_graph = h5_central_graph_summary()
    central_slice = h5_central_slice_summary()
    central_slice_tangent = h5_central_slice_tangent_summary()
    central_slice_quadratic = h5_central_slice_quadratic_summary()
    central_slice_cubic = h5_central_slice_cubic_summary()
    central_slice_formal_isolation = h5_central_slice_formal_isolation_summary()
    central_finite_payment = h5_central_finite_payment_summary()
    central_infinity_flag = h5_central_infinity_flag_summary()
    central_projective = h5_central_projective_summary()
    central_fixedpoint = h5_central_fixedpoint_summary()
    central_slice_fixedpoint = h5_central_slice_fixedpoint_summary()
    unit_propagation = h5_unit_propagation_summary()
    minor_propagation = h5_minor_propagation_summary()
    weighted = h5_weighted_summary()
    scaling = h5_scaling_summary()
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
        "min_chart_total_terms": chart_recovery["min_chart_total_terms"],
        "max_chart_total_terms": chart_recovery["max_chart_total_terms"],
        "central_chart_total_terms": chart_recovery["central_chart_total_terms"],
        "central_chart_max_degree": chart_recovery["central_chart_max_degree"],
        "central_graph_rows": central_graph["graph_rows"],
        "central_graph_terms": central_graph["total_graph_terms"],
        "central_graph_max_degree": central_graph["max_graph_degree"],
        "central_slice_rows": central_slice["slice_rows"],
        "central_slice_terms": central_slice["total_slice_terms"],
        "central_slice_max_degree": central_slice["max_slice_degree"],
        "central_slice_action_rows": central_slice["action_rows_checked"],
        "central_slice_tangent_nonzero": central_slice_tangent[
            "graph_tangent_nonzero_entries"
        ],
        "central_slice_tangent_denominator": central_slice_tangent[
            "graph_tangent_denominator"
        ],
        "central_slice_fixed_linear_num": central_slice_tangent[
            "fixed_equation_diagonal_numerator"
        ],
        "central_slice_fixed_linear_den": central_slice_tangent[
            "fixed_equation_diagonal_denominator"
        ],
        "central_slice_fixed_det_num": central_slice_tangent[
            "fixed_equation_det_numerator"
        ],
        "central_slice_fixed_det_den": central_slice_tangent[
            "fixed_equation_det_denominator"
        ],
        "central_slice_quadratic_rows": central_slice_quadratic[
            "quadratic_rows"
        ],
        "central_slice_quadratic_triangular_rows": central_slice_quadratic[
            "triangular_rows"
        ],
        "central_slice_quadratic_max_graph_terms": central_slice_quadratic[
            "max_graph_quadratic_terms"
        ],
        "central_slice_quadratic_max_fixed_terms": central_slice_quadratic[
            "max_fixed_quadratic_terms"
        ],
        "central_slice_cubic_rows": central_slice_cubic["cubic_rows"],
        "central_slice_cubic_min_fixed_terms": central_slice_cubic[
            "min_fixed_terms"
        ],
        "central_slice_cubic_max_fixed_terms": central_slice_cubic[
            "max_fixed_terms"
        ],
        "central_slice_formal_isolation_variables": central_slice_formal_isolation[
            "variables"
        ],
        "central_slice_formal_isolation_det_num": central_slice_formal_isolation[
            "det_num"
        ],
        "central_slice_formal_isolation_det_den": central_slice_formal_isolation[
            "det_den"
        ],
        "central_finite_degree_product": central_finite_payment["degree_product"],
        "central_finite_first_margin": central_finite_payment["first_margin"],
        "central_infinity_branch_checks": central_infinity_flag["branch_checks"],
        "central_infinity_split_options": central_infinity_flag["split_options"],
        "central_projective_branches": central_projective["branches"],
        "central_projective_terminal_leaves": central_projective["terminal_leaves"],
        "central_projective_max_coeff_prime": central_projective[
            "max_coefficient_prime"
        ],
        "central_fixedpoint_max_terms": central_fixedpoint[
            "max_pre_cancellation_terms"
        ],
        "central_fixedpoint_max_degree": central_fixedpoint[
            "max_total_degree_bound"
        ],
        "central_slice_fixedpoint_max_terms": central_slice_fixedpoint[
            "max_pre_cancellation_terms"
        ],
        "central_slice_fixedpoint_max_degree": central_slice_fixedpoint[
            "max_slice_degree_bound"
        ],
        "central_slice_fixedpoint_min_drop": central_slice_fixedpoint[
            "min_degree_drop"
        ],
        "central_slice_fixedpoint_max_drop": central_slice_fixedpoint[
            "max_degree_drop"
        ],
        "weighted_pairwise_rows": weighted["pairwise_rows"],
        "weighted_unit_rows": weighted["unit_rows"],
        "central_scaling_stabilizer": scaling["central_stabilizer_size"],
        "central_scaling_first_orbit": scaling["first_central_orbit_size"],
        "central_scaling_last_orbit": scaling["last_central_orbit_size"],
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
    parity = h8_parity_summary()
    triangular = h8_triangular_summary()
    reciprocal = h8_reciprocal_summary()
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
        "parity_high_odd_degrees": parity["high_odd_degrees"],
        "parity_low_odd_degrees": parity["low_odd_degrees"],
        "parity_max_denominator_prime": parity["max_denominator_prime"],
        "triangular_keys": triangular["keys"],
        "triangular_max_terms": triangular["max_terms"],
        "triangular_max_total_degree": triangular["max_total_degree"],
        "triangular_first_key_denominator": triangular["first_key_denominator"],
        "triangular_first_key_terms": triangular["first_key_terms"],
        "triangular_first_key_total_degree": triangular["first_key_total_degree"],
        "reciprocal_delta_free_rows": reciprocal["delta_free_rows"],
        "reciprocal_max_terms": reciprocal["max_compatibility_terms"],
        "reciprocal_max_total_degree": reciprocal["max_compatibility_total_degree"],
        "reciprocal_central_terms": reciprocal["central_terms"],
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
            "REPLAYED/PAID",
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
                f"chart terms={h5['min_chart_total_terms']}.."
                f"{h5['max_chart_total_terms']}; "
                f"central graph rows={h5['central_graph_rows']}; "
                f"central slice max degree={h5['central_slice_max_degree']}; "
                f"slice tangent=1/"
                f"{h5['central_slice_tangent_denominator']} anti-diagonal; "
                f"fixed linear det={h5['central_slice_fixed_det_num']}/"
                f"{h5['central_slice_fixed_det_den']}; "
                f"quadratic normal form rows="
                f"{h5['central_slice_quadratic_triangular_rows']}/"
                f"{h5['central_slice_quadratic_rows']} triangular; "
                f"cubic fixed terms={h5['central_slice_cubic_min_fixed_terms']}.."
                f"{h5['central_slice_cubic_max_fixed_terms']}; "
                f"formal isolated variables={h5['central_slice_formal_isolation_variables']}; "
                f"slice fixed-point max degree={h5['central_slice_fixedpoint_max_degree']}; "
                f"finite-slice payment K={h5['central_finite_degree_product']} "
                f"first margin={h5['central_finite_first_margin']}; "
                f"infinity flag checks={h5['central_infinity_branch_checks']} "
                f"with split options={h5['central_infinity_split_options']}; "
                f"projective-infinity exclusion branches="
                f"{h5['central_projective_branches']} terminal_leaves="
                f"{h5['central_projective_terminal_leaves']} "
                f"max_coeff_prime={h5['central_projective_max_coeff_prime']}; "
                f"fixed-point pre-cancel max={h5['central_fixedpoint_max_terms']}; "
                f"weighted rows={h5['weighted_pairwise_rows']}+"
                f"{h5['weighted_unit_rows']}; "
                f"central scaling stabilizer={h5['central_scaling_stabilizer']}; "
                f"minor propagation syzygies={h5['minor_propagation_syzygies']}; "
                f"unit propagation syzygies={h5['unit_propagation_syzygies']}"
            ),
            "no h=5 residual for the direct n^3 budget; stronger norm-gate emptiness remains optional and is not needed here",
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
                f"{h8['radius3_rows']} radius-three x83 shell certificates; "
                f"x83 parity filter high_odd={h8['parity_high_odd_degrees']} "
                f"low_odd={h8['parity_low_odd_degrees']} "
                f"denom_prime={h8['parity_max_denominator_prime']}; "
                f"x83 triangular keys={h8['triangular_keys']} "
                f"first_key_terms={h8['triangular_first_key_terms']} "
                f"first_key_degree={h8['triangular_first_key_total_degree']}; "
                f"reciprocal delta-free rows={h8['reciprocal_delta_free_rows']} "
                f"max_degree={h8['reciprocal_max_total_degree']}"
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
        f"chart_total_terms={h5['min_chart_total_terms']}.."
        f"{h5['max_chart_total_terms']} "
        f"central_chart_terms={h5['central_chart_total_terms']} "
        f"central_chart_max_degree={h5['central_chart_max_degree']} "
        f"central_graph_rows={h5['central_graph_rows']} "
        f"central_graph_terms={h5['central_graph_terms']} "
        f"central_graph_max_degree={h5['central_graph_max_degree']} "
        f"central_slice_rows={h5['central_slice_rows']} "
        f"central_slice_terms={h5['central_slice_terms']} "
        f"central_slice_max_degree={h5['central_slice_max_degree']} "
        f"central_slice_action_rows={h5['central_slice_action_rows']} "
        f"central_slice_tangent_nonzero={h5['central_slice_tangent_nonzero']} "
        f"central_slice_tangent_denominator={h5['central_slice_tangent_denominator']} "
        f"central_slice_fixed_linear={h5['central_slice_fixed_linear_num']}/"
        f"{h5['central_slice_fixed_linear_den']} "
        f"central_slice_fixed_det={h5['central_slice_fixed_det_num']}/"
        f"{h5['central_slice_fixed_det_den']} "
        f"central_slice_quadratic_rows={h5['central_slice_quadratic_rows']} "
        f"central_slice_quadratic_triangular_rows="
        f"{h5['central_slice_quadratic_triangular_rows']} "
        f"central_slice_quadratic_terms="
        f"{h5['central_slice_quadratic_max_graph_terms']}.."
        f"{h5['central_slice_quadratic_max_fixed_terms']} "
        f"central_slice_cubic_rows={h5['central_slice_cubic_rows']} "
        f"central_slice_cubic_fixed_terms={h5['central_slice_cubic_min_fixed_terms']}.."
        f"{h5['central_slice_cubic_max_fixed_terms']} "
        f"central_slice_formal_isolation_det="
        f"{h5['central_slice_formal_isolation_det_num']}/"
        f"{h5['central_slice_formal_isolation_det_den']} "
        f"central_fixedpoint_precancel_max={h5['central_fixedpoint_max_terms']} "
        f"central_fixedpoint_max_degree={h5['central_fixedpoint_max_degree']} "
        f"central_slice_fixedpoint_precancel_max={h5['central_slice_fixedpoint_max_terms']} "
        f"central_slice_fixedpoint_max_degree={h5['central_slice_fixedpoint_max_degree']} "
        f"central_slice_fixedpoint_degree_drop={h5['central_slice_fixedpoint_min_drop']}.."
        f"{h5['central_slice_fixedpoint_max_drop']} "
        f"central_finite_K={h5['central_finite_degree_product']} "
        f"central_finite_first_margin={h5['central_finite_first_margin']} "
        f"central_infinity_branch_checks={h5['central_infinity_branch_checks']} "
        f"central_projective_branches={h5['central_projective_branches']} "
        f"central_projective_terminal_leaves={h5['central_projective_terminal_leaves']} "
        f"central_projective_max_coeff_prime={h5['central_projective_max_coeff_prime']} "
        f"weighted_pairwise_rows={h5['weighted_pairwise_rows']} "
        f"weighted_unit_rows={h5['weighted_unit_rows']} "
        f"central_scaling_stabilizer={h5['central_scaling_stabilizer']} "
        f"central_scaling_orbit={h5['central_scaling_first_orbit']}.."
        f"{h5['central_scaling_last_orbit']} "
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
    print(
        "h=8 x83 parity filter: "
        f"high_odd_degrees={h8['parity_high_odd_degrees']} "
        f"low_odd_degrees={h8['parity_low_odd_degrees']} "
        f"max_denominator_prime={h8['parity_max_denominator_prime']}"
    )
    print(
        "h=8 x83 triangular obstruction keys: "
        f"keys={h8['triangular_keys']} "
        f"max_terms={h8['triangular_max_terms']} "
        f"max_total_degree={h8['triangular_max_total_degree']} "
        f"first_key_denominator={h8['triangular_first_key_denominator']} "
        f"first_key_terms={h8['triangular_first_key_terms']} "
        f"first_key_total_degree={h8['triangular_first_key_total_degree']}"
    )
    print(
        "h=8 reciprocal compatibility: "
        f"delta_free_rows={h8['reciprocal_delta_free_rows']} "
        f"max_terms={h8['reciprocal_max_terms']} "
        f"max_total_degree={h8['reciprocal_max_total_degree']} "
        f"central_terms={h8['reciprocal_central_terms']}"
    )
    print("F3_T4_RESIDUAL_FRONTIER_LEDGER_PASS")


if __name__ == "__main__":
    main()
