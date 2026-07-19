# PARKED PENDING ADOPTION DECISION (wave-8 import, 2026-07-16):
# this is v4's WHOLE-CONTRACT checker — it pins v4's imgfib wiring
# (petal_mixed_amplification + pma_exact_periodic_owner as req
# children) and v4's in-place rewrite of petal_growth/proof.md.
# Master's deliberate wiring keeps l1_mixed_petal_amplification as
# the critical slot (audit guard (c) + crosswalk). Becomes live if
# the maintainer adopts v4's decomposition shape; until then the
# scoping content is carried by the imgfib statement addendum +
# notes/mixed_petal_scope_audit_20260714.md.
#!/usr/bin/env python3
"""Verify the post-top-band scope repair for universal imgfib."""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DAG = ROOT / "dag.json"


def load() -> dict[str, object]:
    return json.loads(DAG.read_text())


def edge_set(doc: dict[str, object]) -> set[tuple[str, str, str]]:
    return {
        (str(edge["from"]), str(edge["to"]), str(edge["kind"]))
        for edge in doc["edges"]
    }


def scope_contract(doc: dict[str, object]) -> bool:
    nodes = {str(node["id"]): node for node in doc["nodes"]}
    edges = edge_set(doc)
    imgfib_reqs = {
        source
        for source, target, kind in edges
        if target == "imgfib" and kind == "req"
    }
    mixed_reqs = {
        source
        for source, target, kind in edges
        if target == "petal_mixed_amplification" and kind == "req"
    }
    mixed_evidence = {
        source
        for source, target, kind in edges
        if target == "petal_mixed_amplification" and kind == "ev"
    }
    return (
        nodes["imgfib"]["status"] == "CONDITIONAL"
        and nodes["petal_growth"]["status"] == "PROVED"
        and nodes["petal_mixed_amplification"]["status"] == "TARGET"
        and nodes["pma_quotient_closure_scope"]["status"] == "PROVED"
        and nodes["pma_sigma_one_b11_scope"]["status"] == "PROVED"
        and nodes["pma_sigma_one_low_defect_payment"]["status"] == "PROVED"
        and nodes["pma_sigma_one_d3_background_payment"]["status"] == "PROVED"
        and nodes["pma_sigma_one_d3_full_petal_payment"]["status"] == "PROVED"
        and nodes["pma_sigma_one_d3_diffuse_hyperplane_reduction"]["status"] == "PROVED"
        and nodes["pma_sigma_one_d3_reciprocal_quadratic_obstruction"]["status"] == "PROVED"
        and nodes["pma_sigma_one_index_two_core_owner"]["status"] == "PROVED"
        and nodes["pma_sigma_one_dyadic_near_coset_owner"]["status"] == "PROVED"
        and nodes["pma_sigma_one_odd_lift_boundary_owner"]["status"] == "PROVED"
        and nodes["pma_sigma_one_paired_core_normalization"]["status"] == "PROVED"
        and nodes["pma_sigma_one_paired_core_abundance"]["status"] == "PROVED"
        and nodes["pma_sigma_one_post_top_allowance"]["status"] == "PROVED"
        and nodes["pma_sigma_one_first_layout_domination"]["status"] == "PROVED"
        and nodes["pma_sigma_one_d4_generic_source_obstruction"]["status"] == "PROVED"
        and nodes["petal_reserve_rich_fiber_reduction"]["status"] == "PROVED"
        and nodes["pma_saturated_mixed_support_kernel"]["status"] == "PROVED"
        and nodes["pma_petal_pattern_root_pinning_ledger"]["status"] == "PROVED"
        and nodes["pma_full_petal_band_composition"]["status"] == "PROVED"
        and nodes["pma_coset_subtwoell_saturation_exclusion"]["status"] == "PROVED"
        and nodes["pma_arbitrary_petal_source_realizability"]["status"] == "PROVED"
        and nodes["pma_three_petal_mu_basis_reduction"]["status"] == "PROVED"
        and nodes["pma_official_rate_small_source_degree_sieve"]["status"] == "PROVED"
        and nodes["pma_three_petal_projective_johnson_bound"]["status"] == "PROVED"
        and nodes["pma_wide_residual"]["status"] == "REFUTED"
        and imgfib_reqs
        == {
            "petal_growth",
            "petal_mixed_amplification",
            "pma_exact_periodic_owner",
            "conj_f",
            "l1_program_frontier",
            "dyadic_profile_evaluation",
            "payment_completeness",
        }
        and not mixed_reqs
        and {
            "pma_aux_list_reduction",
            "pma_johnson_regime",
            "pma_source_paving_bridge",
            "pma_b11_first_match_router",
            "pma_exact_periodic_owner",
            "pma_quotient_closure_scope",
            "pma_sigma_one_b11_scope",
            "pma_sigma_one_low_defect_payment",
            "pma_sigma_one_d3_background_payment",
            "pma_sigma_one_d3_full_petal_payment",
            "pma_sigma_one_d3_diffuse_hyperplane_reduction",
            "pma_sigma_one_d3_reciprocal_quadratic_obstruction",
            "pma_sigma_one_index_two_core_owner",
            "pma_sigma_one_dyadic_near_coset_owner",
            "pma_sigma_one_odd_lift_boundary_owner",
            "pma_sigma_one_paired_core_normalization",
            "pma_sigma_one_paired_core_abundance",
            "pma_sigma_one_post_top_allowance",
            "pma_sigma_one_first_layout_domination",
            "pma_sigma_one_d4_generic_source_obstruction",
            "petal_reserve_rich_fiber_reduction",
            "pma_saturated_mixed_support_kernel",
            "pma_petal_pattern_root_pinning_ledger",
            "pma_full_petal_band_composition",
            "pma_coset_subtwoell_saturation_exclusion",
            "pma_arbitrary_petal_source_realizability",
            "pma_three_petal_mu_basis_reduction",
            "pma_official_rate_small_source_degree_sieve",
            "pma_three_petal_projective_johnson_bound",
            "pma_wide_residual",
        }
        <= mixed_evidence
        and ("l1_core_defect_reduction", "pma_aux_list_reduction", "req")
        in edges
        and ("e22_two_class_exhaustion", "pma_full_petal_band_composition", "req")
        in edges
        and ("petal_growth", "pma_full_petal_band_composition", "req") in edges
        and (
            "pma_petal_pattern_root_pinning_ledger",
            "pma_full_petal_band_composition",
            "req",
        )
        in edges
        and (
            "pma_full_petal_band_composition",
            "petal_mixed_amplification",
            "ev",
        )
        in edges
        and (
            "l1_coset_chart_residue_bridge",
            "pma_coset_subtwoell_saturation_exclusion",
            "req",
        )
        in edges
        and (
            "pma_saturated_mixed_support_kernel",
            "pma_coset_subtwoell_saturation_exclusion",
            "req",
        )
        in edges
        and (
            "pma_coset_subtwoell_saturation_exclusion",
            "petal_mixed_amplification",
            "ev",
        )
        in edges
        and (
            "pma_coset_subtwoell_saturation_exclusion",
            "imgfib",
            "req",
        )
        not in edges
        and (
            "pma_arbitrary_petal_source_realizability",
            "petal_mixed_amplification",
            "ev",
        )
        in edges
        and (
            "pma_arbitrary_petal_source_realizability",
            "imgfib",
            "req",
        )
        not in edges
        and (
            "pma_saturated_mixed_support_kernel",
            "pma_three_petal_mu_basis_reduction",
            "req",
        )
        in edges
        and (
            "pma_full_petal_band_composition",
            "pma_three_petal_mu_basis_reduction",
            "req",
        )
        in edges
        and (
            "pma_three_petal_mu_basis_reduction",
            "petal_mixed_amplification",
            "ev",
        )
        in edges
        and (
            "pma_three_petal_mu_basis_reduction",
            "imgfib",
            "req",
        )
        not in edges
        and (
            "pma_full_petal_band_composition",
            "pma_official_rate_small_source_degree_sieve",
            "req",
        )
        in edges
        and (
            "pma_three_petal_mu_basis_reduction",
            "pma_official_rate_small_source_degree_sieve",
            "req",
        )
        in edges
        and (
            "pma_official_rate_small_source_degree_sieve",
            "petal_mixed_amplification",
            "ev",
        )
        in edges
        and (
            "pma_official_rate_small_source_degree_sieve",
            "imgfib",
            "req",
        )
        not in edges
        and (
            "pma_three_petal_mu_basis_reduction",
            "pma_three_petal_projective_johnson_bound",
            "req",
        )
        in edges
        and (
            "pma_official_rate_small_source_degree_sieve",
            "pma_three_petal_projective_johnson_bound",
            "req",
        )
        in edges
        and (
            "pma_three_petal_projective_johnson_bound",
            "petal_mixed_amplification",
            "ev",
        )
        in edges
        and (
            "pma_three_petal_projective_johnson_bound",
            "imgfib",
            "req",
        )
        not in edges
        and ("petal_mixed_amplification", "petal_growth", "ev") not in edges
        and not any(
            target == "pma_wide_residual" and kind == "req"
            for _, target, kind in edges
        )
    )


def main() -> None:
    doc = load()
    nodes = {str(node["id"]): node for node in doc["nodes"]}
    checks: list[tuple[str, bool]] = []

    checks.append(("scope contract", scope_contract(doc)))
    checks.append(("list_safe reopened", nodes["list_safe"]["status"] == "CONDITIONAL"))
    checks.append(("m_le3 reopened", nodes["m_le3_route"]["status"] == "CONDITIONAL"))

    required_files = [
        "critical/nodes/petal_mixed_amplification/statement.md",
        "critical/nodes/petal_mixed_amplification/conditional.md",
        "critical/nodes/petal_mixed_amplification/attack.md",
        "critical/nodes/petal_mixed_amplification/claim_contract.md",
        "critical/nodes/petal_mixed_amplification/dependency_subdag.md",
        "background/nodes/pma_aux_list_reduction/proof.md",
        "background/nodes/pma_johnson_regime/proof.md",
        "background/nodes/pma_source_paving_bridge/proof.md",
        "background/nodes/pma_b11_first_match_router/proof.md",
        "critical/nodes/pma_exact_periodic_owner/proof.md",
        "critical/nodes/pma_exact_periodic_owner/verify.py",
        "background/nodes/pma_quotient_closure_scope/statement.md",
        "background/nodes/pma_quotient_closure_scope/proof.md",
        "background/nodes/pma_quotient_closure_scope/verify.py",
        "background/nodes/pma_sigma_one_b11_scope/statement.md",
        "background/nodes/pma_sigma_one_b11_scope/proof.md",
        "background/nodes/pma_sigma_one_b11_scope/verify.py",
        "background/nodes/pma_sigma_one_low_defect_payment/statement.md",
        "background/nodes/pma_sigma_one_low_defect_payment/proof.md",
        "background/nodes/pma_sigma_one_low_defect_payment/verify.py",
        "background/nodes/pma_sigma_one_d3_background_payment/statement.md",
        "background/nodes/pma_sigma_one_d3_background_payment/proof.md",
        "background/nodes/pma_sigma_one_d3_background_payment/verify.py",
        "background/nodes/pma_sigma_one_d3_full_petal_payment/statement.md",
        "background/nodes/pma_sigma_one_d3_full_petal_payment/proof.md",
        "background/nodes/pma_sigma_one_d3_full_petal_payment/verify.py",
        "background/nodes/pma_sigma_one_d3_diffuse_hyperplane_reduction/statement.md",
        "background/nodes/pma_sigma_one_d3_diffuse_hyperplane_reduction/proof.md",
        "background/nodes/pma_sigma_one_d3_diffuse_hyperplane_reduction/verify.py",
        "background/nodes/pma_sigma_one_d3_reciprocal_quadratic_obstruction/statement.md",
        "background/nodes/pma_sigma_one_d3_reciprocal_quadratic_obstruction/proof.md",
        "background/nodes/pma_sigma_one_d3_reciprocal_quadratic_obstruction/verify.py",
        "background/nodes/pma_sigma_one_index_two_core_owner/statement.md",
        "background/nodes/pma_sigma_one_index_two_core_owner/proof.md",
        "background/nodes/pma_sigma_one_index_two_core_owner/verify.py",
        "background/nodes/pma_sigma_one_dyadic_near_coset_owner/statement.md",
        "background/nodes/pma_sigma_one_dyadic_near_coset_owner/proof.md",
        "background/nodes/pma_sigma_one_dyadic_near_coset_owner/verify.py",
        "background/nodes/pma_sigma_one_odd_lift_boundary_owner/statement.md",
        "background/nodes/pma_sigma_one_odd_lift_boundary_owner/proof.md",
        "background/nodes/pma_sigma_one_odd_lift_boundary_owner/verify.py",
        "background/nodes/pma_sigma_one_paired_core_normalization/statement.md",
        "background/nodes/pma_sigma_one_paired_core_normalization/proof.md",
        "background/nodes/pma_sigma_one_paired_core_normalization/verify.py",
        "background/nodes/pma_sigma_one_paired_core_abundance/statement.md",
        "background/nodes/pma_sigma_one_paired_core_abundance/proof.md",
        "background/nodes/pma_sigma_one_paired_core_abundance/audit.md",
        "background/nodes/pma_sigma_one_paired_core_abundance/claim_contract.md",
        "background/nodes/pma_sigma_one_paired_core_abundance/dependency_subdag.md",
        "background/nodes/pma_sigma_one_paired_core_abundance/verify.py",
        "background/nodes/pma_sigma_one_post_top_allowance/statement.md",
        "background/nodes/pma_sigma_one_post_top_allowance/proof.md",
        "background/nodes/pma_sigma_one_post_top_allowance/verify.py",
        "background/nodes/pma_sigma_one_first_layout_domination/statement.md",
        "background/nodes/pma_sigma_one_first_layout_domination/proof.md",
        "background/nodes/pma_sigma_one_first_layout_domination/audit.md",
        "background/nodes/pma_sigma_one_first_layout_domination/claim_contract.md",
        "background/nodes/pma_sigma_one_first_layout_domination/dependency_subdag.md",
        "background/nodes/pma_sigma_one_first_layout_domination/verify.py",
        "background/nodes/pma_sigma_one_d4_generic_source_obstruction/statement.md",
        "background/nodes/pma_sigma_one_d4_generic_source_obstruction/proof.md",
        "background/nodes/pma_sigma_one_d4_generic_source_obstruction/audit.md",
        "background/nodes/pma_sigma_one_d4_generic_source_obstruction/claim_contract.md",
        "background/nodes/pma_sigma_one_d4_generic_source_obstruction/dependency_subdag.md",
        "background/nodes/pma_sigma_one_d4_generic_source_obstruction/verify.py",
        "background/nodes/petal_reserve_rich_fiber_reduction/statement.md",
        "background/nodes/petal_reserve_rich_fiber_reduction/proof.md",
        "background/nodes/petal_reserve_rich_fiber_reduction/verify.py",
        "background/nodes/pma_saturated_mixed_support_kernel/statement.md",
        "background/nodes/pma_saturated_mixed_support_kernel/proof.md",
        "background/nodes/pma_saturated_mixed_support_kernel/verify.py",
        "background/nodes/pma_petal_pattern_root_pinning_ledger/statement.md",
        "background/nodes/pma_petal_pattern_root_pinning_ledger/proof.md",
        "background/nodes/pma_petal_pattern_root_pinning_ledger/verify.py",
        "background/nodes/pma_full_petal_band_composition/statement.md",
        "background/nodes/pma_full_petal_band_composition/proof.md",
        "background/nodes/pma_full_petal_band_composition/audit.md",
        "background/nodes/pma_full_petal_band_composition/claim_contract.md",
        "background/nodes/pma_full_petal_band_composition/dependency_subdag.md",
        "background/nodes/pma_full_petal_band_composition/verify.py",
        "background/nodes/pma_coset_subtwoell_saturation_exclusion/statement.md",
        "background/nodes/pma_coset_subtwoell_saturation_exclusion/proof.md",
        "background/nodes/pma_coset_subtwoell_saturation_exclusion/audit.md",
        "background/nodes/pma_coset_subtwoell_saturation_exclusion/claim_contract.md",
        "background/nodes/pma_coset_subtwoell_saturation_exclusion/dependency_subdag.md",
        "background/nodes/pma_coset_subtwoell_saturation_exclusion/verify.py",
        "background/nodes/pma_arbitrary_petal_source_realizability/statement.md",
        "background/nodes/pma_arbitrary_petal_source_realizability/proof.md",
        "background/nodes/pma_arbitrary_petal_source_realizability/audit.md",
        "background/nodes/pma_arbitrary_petal_source_realizability/claim_contract.md",
        "background/nodes/pma_arbitrary_petal_source_realizability/dependency_subdag.md",
        "background/nodes/pma_arbitrary_petal_source_realizability/verify.py",
        "background/nodes/pma_three_petal_mu_basis_reduction/statement.md",
        "background/nodes/pma_three_petal_mu_basis_reduction/proof.md",
        "background/nodes/pma_three_petal_mu_basis_reduction/audit.md",
        "background/nodes/pma_three_petal_mu_basis_reduction/claim_contract.md",
        "background/nodes/pma_three_petal_mu_basis_reduction/dependency_subdag.md",
        "background/nodes/pma_three_petal_mu_basis_reduction/verify.py",
        "background/nodes/pma_official_rate_small_source_degree_sieve/statement.md",
        "background/nodes/pma_official_rate_small_source_degree_sieve/proof.md",
        "background/nodes/pma_official_rate_small_source_degree_sieve/audit.md",
        "background/nodes/pma_official_rate_small_source_degree_sieve/claim_contract.md",
        "background/nodes/pma_official_rate_small_source_degree_sieve/dependency_subdag.md",
        "background/nodes/pma_official_rate_small_source_degree_sieve/verify.py",
        "background/nodes/pma_three_petal_projective_johnson_bound/statement.md",
        "background/nodes/pma_three_petal_projective_johnson_bound/proof.md",
        "background/nodes/pma_three_petal_projective_johnson_bound/audit.md",
        "background/nodes/pma_three_petal_projective_johnson_bound/claim_contract.md",
        "background/nodes/pma_three_petal_projective_johnson_bound/dependency_subdag.md",
        "background/nodes/pma_three_petal_projective_johnson_bound/verify.py",
        "background/nodes/pma_wide_residual/statement.md",
        "background/nodes/pma_wide_residual/attack.md",
        "background/nodes/pma_wide_residual/frontier.md",
        "background/nodes/pma_wide_residual/claim_contract.md",
        "background/nodes/pma_wide_residual/dependency_subdag.md",
        "background/nodes/pma_wide_residual/refutation.md",
    ]
    for rel in required_files:
        checks.append((f"artifact {rel}", (ROOT / rel).is_file()))

    growth_proof = (ROOT / "critical/nodes/petal_growth/proof.md").read_text()
    payment_proof = (ROOT / "critical/nodes/payment_completeness/proof.md").read_text()
    audit = (
        ROOT / "critical/nodes/imgfib/notes/mixed_petal_scope_audit_20260714.md"
    ).read_text()
    checks.extend(
        [
            (
                "growth scope pin",
                "layout-anchored top-band" in growth_proof
                and "No off-band induction" in growth_proof
                and "below-floor" in growth_proof,
            ),
            ("taxonomy nonpayment pin", "not \"everything is paid\"" in payment_proof),
            ("toy scope witness pin", "`43` mixed-petal" in audit),
            ("no counterexample overclaim", "No counterexample to `imgfib`" in audit),
        ]
    )

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "petal_mixed_amplification",
            "to": "imgfib",
            "kind": "req",
        }:
            edge["kind"] = "ev"
            break
    checks.append(("mutation: missing mixed req is rejected", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_sigma_one_d3_reciprocal_quadratic_obstruction",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: route-guard logical edge is rejected", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_sigma_one_index_two_core_owner",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: near-core logical edge is rejected", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_sigma_one_dyadic_near_coset_owner",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: all-dyadic logical edge is rejected", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_sigma_one_odd_lift_boundary_owner",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: odd-lift logical edge is rejected", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_sigma_one_paired_core_normalization",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: paired-core logical edge is rejected", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_sigma_one_paired_core_abundance",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: abundance logical edge is rejected", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_sigma_one_post_top_allowance",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: Post-allowance logical edge is rejected", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_sigma_one_first_layout_domination",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: first-layout logical edge is rejected", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_sigma_one_d4_generic_source_obstruction",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: defect-four logical edge is rejected", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_full_petal_band_composition",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: band composition stays evidence", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_coset_subtwoell_saturation_exclusion",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: scoped common-pencil exclusion stays evidence", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_arbitrary_petal_source_realizability",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: arbitrary-source route cut stays evidence", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_three_petal_mu_basis_reduction",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: mu-basis reduction stays evidence", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_official_rate_small_source_degree_sieve",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: official-rate sieve stays evidence", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    for edge in mutant["edges"]:
        if edge == {
            "from": "pma_three_petal_projective_johnson_bound",
            "to": "petal_mixed_amplification",
            "kind": "ev",
        }:
            edge["kind"] = "req"
            break
    checks.append(("mutation: projective Johnson bound stays evidence", not scope_contract(mutant)))

    mutant = copy.deepcopy(doc)
    mutant["edges"].append(
        {
            "from": "petal_mixed_amplification",
            "to": "petal_growth",
            "kind": "ev",
        }
    )
    checks.append(("mutation: backward petal edge is rejected", not scope_contract(mutant)))

    failures = [name for name, passed in checks if not passed]
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    if failures:
        raise SystemExit(f"scope repair verifier failed: {', '.join(failures)}")
    print(f"PASS: {len(checks)}/{len(checks)} post-top-band scope-repair checks")


if __name__ == "__main__":
    main()
