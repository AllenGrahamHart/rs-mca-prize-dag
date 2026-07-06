#!/usr/bin/env python3
"""Run selected existing verifiers relevant to amber stress testing.

Each verifier is capped independently.  Results are checkpointed after every
command so partial evidence survives interruption.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "verifier_results.json"

COMMANDS = [
    {
        "name": "list_corridor_ledger",
        "nodes": ["list_adjacency_closing", "list_grand"],
        "cmd": ["python3", "tools/verify_list_corridor_ledger.py"],
    },
    {
        "name": "list_corridor_widths",
        "nodes": ["list_adjacency_closing", "list_grand"],
        "cmd": ["python3", "tools/verify_list_corridor_widths.py"],
    },
    {
        "name": "f1_minimal_field_descent",
        "nodes": ["f1_classification", "ext_lift"],
        "cmd": ["python3", "nodes/f1_minimal_field_descent/verify.py"],
    },
    {
        "name": "f1_pole_threshold_probe",
        "nodes": ["f1_pole_list_threshold_location", "f1_case_pole", "f1_classification"],
        "cmd": ["python3", "experiments/amber_stress/f1_pole_threshold_probe.py"],
    },
    {
        "name": "xr_radius_arithmetic",
        "nodes": ["r2_clean_rates", "xr_clean_residual_any_gate"],
        "cmd": ["python3", "nodes/xr_radius_arithmetic/verify.py"],
    },
    {
        "name": "xr_ledger_qpower",
        "nodes": ["r2_clean_rates", "xr_clean_residual_any_gate"],
        "cmd": ["python3", "nodes/xr_ledger_qpower/verify.py"],
    },
    {
        "name": "xr_ledger_exponent_reconciliation",
        "nodes": ["r2_clean_rates", "xr_clean_residual_any_gate"],
        "cmd": ["python3", "nodes/xr_ledger_exponent_reconciliation/verify.py"],
    },
    {
        "name": "xr_smallcore_triangle_scan",
        "nodes": ["xr_clean_residual_any_gate", "xr_smallcore_spread_count"],
        "cmd": ["python3", "experiments/amber_stress/xr_smallcore_triangle_scan.py"],
    },
    {
        "name": "xr_smallcore_quad_scan",
        "nodes": ["xr_clean_residual_any_gate", "xr_smallcore_spread_count"],
        "cmd": ["python3", "experiments/amber_stress/xr_smallcore_quad_scan.py"],
    },
    {
        "name": "e22_two_class_exhaustion",
        "nodes": ["worst_word_planted", "list_planted_arithmetic"],
        "cmd": ["python3", "nodes/e22_two_class_exhaustion/verify.py"],
    },
    {
        "name": "e22_fixed_scale_staircase_injectivity",
        "nodes": ["worst_word_planted", "list_planted_arithmetic"],
        "cmd": ["python3", "nodes/e22_fixed_scale_staircase_injectivity/verify.py"],
    },
    {
        "name": "e22_extended_local_census",
        "nodes": [
            "worst_word_challenger_pricing",
            "worst_word_planted",
            "list_planted_arithmetic",
        ],
        "cmd": ["python3", "experiments/amber_stress/e22_extended_local_census.py"],
    },
    {
        "name": "e22_random_layout_census",
        "nodes": [
            "worst_word_challenger_pricing",
            "worst_word_planted",
            "list_planted_arithmetic",
        ],
        "cmd": ["python3", "experiments/amber_stress/e22_random_layout_census.py"],
    },
    {
        "name": "gap2_seam",
        "nodes": ["strip"],
        "cmd": ["python3", "nodes/gap2_seam/verify.py"],
    },
    {
        "name": "petal_fixed_excess",
        "nodes": ["imgfib", "list_safe"],
        "cmd": ["python3", "nodes/petal_fixed_excess/verify.py"],
    },
    {
        "name": "petal_excess_local_scan",
        "nodes": ["imgfib", "petal_growth"],
        "cmd": ["python3", "experiments/amber_stress/petal_excess_local_scan.py"],
    },
    {
        "name": "pma_aux_list_probe",
        "nodes": ["petal_mixed_amplification", "pma_wide_residual"],
        "cmd": ["python3", "experiments/amber_stress/pma_aux_list_probe.py"],
    },
    {
        "name": "pma_correlated_target_search",
        "nodes": ["petal_mixed_amplification", "pma_wide_residual"],
        "cmd": ["python3", "experiments/amber_stress/pma_correlated_target_search.py"],
    },
    {
        "name": "dyadic_profile_evaluation",
        "nodes": ["x4_exactlist_staircase_split", "tr_perleaf_list_ident"],
        "cmd": ["python3", "nodes/dyadic_profile_evaluation/verify.py"],
    },
    {
        "name": "tr_quotient_dictionary_probe",
        "nodes": ["tr_perleaf_list_ident", "gap1_product_model"],
        "cmd": ["python3", "experiments/amber_stress/tr_quotient_dictionary_probe.py"],
    },
    {
        "name": "u2c_tnull_boundary_scan",
        "nodes": ["x4_exactlist_staircase_split", "u2c_giant_tnull_dichotomy"],
        "cmd": ["python3", "experiments/amber_stress/u2c_tnull_boundary_scan.py"],
    },
    {
        "name": "dli_weighted_res_probe",
        "nodes": ["x4_exactlist_staircase_split", "dli_prime_weighted_large_block_support"],
        "cmd": ["python3", "experiments/amber_stress/dli_weighted_res_probe.py"],
    },
    {
        "name": "u1_x4_active_core_budget_probe",
        "nodes": ["x4_exactlist_staircase_split", "u1_x4_direct_column_budget"],
        "cmd": ["python3", "experiments/amber_stress/u1_x4_active_core_budget_probe.py"],
    },
    {
        "name": "gap1_telescope_checks",
        "nodes": ["gap1_product_model", "gap1_noneq_mass", "tr_perleaf_list_ident"],
        "cmd": ["python3", "experiments/amber_stress/gap1_telescope_checks.py"],
    },
    {
        "name": "census_bounded_scales",
        "nodes": ["mca_safe", "safe_assembly_uniformity"],
        "cmd": ["python3", "nodes/census_bounded_scales/verify.py"],
    },
    {
        "name": "conjectural_mca_delta_self_test",
        "nodes": ["mca_grand", "mca_safe", "adjacency_closing"],
        "cmd": ["python3", "tools/conjectural_mca_delta.py", "--self-test"],
    },
    {
        "name": "spi_hankel_writeup_checks",
        "nodes": ["hankel_slope_large_sieve", "spi_point_counting"],
        "cmd": ["python3", "nodes/spi_exceptional_class/notes/verify_writeup.py"],
    },
    {
        "name": "diffuse_shadow_circuit_scan",
        "nodes": ["diffuse_triple_shadow", "hankel_slope_large_sieve"],
        "cmd": ["python3", "experiments/amber_stress/diffuse_shadow_circuit_scan.py"],
    },
    {
        "name": "rate_half_local_floor_and_threshold",
        "nodes": ["adjacency_closing", "list_adjacency_closing"],
        "cmd": ["python3", "experiments/amber_stress/rate_half_local_checks.py"],
    },
    {
        "name": "assembly_orphan_checks",
        "nodes": ["prize", "packaging", "a_regular_collapse", "free_pool_ladder", "m_le3_route"],
        "cmd": ["python3", "experiments/amber_stress/assembly_orphan_checks.py"],
    },
    {
        "name": "subgroup_expsum_probe",
        "nodes": ["free_pool_ladder", "subgroup_expsum_input"],
        "cmd": ["python3", "experiments/amber_stress/subgroup_expsum_probe.py"],
    },
]


def checkpoint(results: dict) -> None:
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")


def main() -> int:
    timeout = 60
    if len(sys.argv) > 1:
        timeout = int(sys.argv[1])
    results = {
        "started_at_unix": time.time(),
        "timeout_per_command_seconds": timeout,
        "commands": [],
    }
    checkpoint(results)
    for spec in COMMANDS:
        t0 = time.monotonic()
        item = {
            "name": spec["name"],
            "nodes": spec["nodes"],
            "cmd": spec["cmd"],
        }
        try:
            proc = subprocess.run(
                spec["cmd"],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=timeout,
                check=False,
            )
            item.update(
                {
                    "returncode": proc.returncode,
                    "status": "PASS" if proc.returncode == 0 else "FAIL",
                    "output_tail": proc.stdout[-4000:],
                }
            )
        except subprocess.TimeoutExpired as exc:
            item.update(
                {
                    "status": "TIMEOUT",
                    "returncode": None,
                    "output_tail": (exc.stdout or "")[-4000:] if isinstance(exc.stdout, str) else "",
                }
            )
        item["wall_seconds"] = round(time.monotonic() - t0, 6)
        results["commands"].append(item)
        checkpoint(results)
    results["finished_at_unix"] = time.time()
    checkpoint(results)
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0 if all(c["status"] == "PASS" for c in results["commands"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
