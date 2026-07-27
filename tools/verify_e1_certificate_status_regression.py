#!/usr/bin/env python3
"""Fail closed on the E1 quantifier, finite-budget, and exhibit cuts."""

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

    branch_target = "e1_official_prime_exception_control"
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
    offorbit_route = {
        branch_target,
        "e1_clean_anchor_exact_collision_allowance",
        "e1_pair_feasible_ambient_generation",
        "e1_pair_feasible_prime_field_reduction",
        "e1_prime_field_l2_norm_collision_radius",
        "e1_n256_s16_high_variance_collision_exclusion",
        "e1_n256_s16_sparse_l1_variance_exclusion",
        "e1_n256_proper_conductor_collision_exclusion",
        "e1_n256_2adic_cofactor_collision_exclusion",
        "e1_n256_s16_signed_chord_collision_gate",
        "e1_n256_local_norm_cofactor_collapse",
        "e1_n512_four_singleton_collision_exclusion",
        "e1_n512_trinomial_interval_norm_exclusion",
        "e1_fullness",
        "e1_exceptional_set_reduction",
        "are_exceptional_density",
        "zone_b",
    }

    require(nodes[branch_target]["status"] == "TARGET", "direct E1 node is not TARGET")
    target_statement = nodes[branch_target]["statement"].lower()
    require("every admissible clean-anchor row" in target_statement,
            "direct-E1 clean-row quantifier is missing")
    require("class b=f_p(q), |b|>=b_pair_min" in target_statement,
            "independent generated-field candidate class is missing")
    require("quotient orders n in {256,512}" in target_statement,
            "quotient-order scope is missing")
    require("p<=k-b*-1" in target_statement,
            "exact finite collision-pair allowance is missing")
    require("q=p and p=1 mod n" in target_statement,
            "prime-field reduction is missing from the live target")
    require(
        "do not discharge" in target_statement,
        "named exhibits are not explicitly fenced from route-wide discharge",
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
        if target == branch_target and kind == "req"
    }
    require(not req_parents, f"direct E1 TARGET gained req parents: {sorted(req_parents)}")
    evidence_edges = {
        ("official_row_primes_pinning", branch_target, "ev"),
        ("axis8_generating", branch_target, "ev"),
        ("v13_base_field_normalization_guard", branch_target, "ev"),
        ("e1_folded_certificate_soundness", branch_target, "ev"),
        ("e1_open_cell_control_payload", branch_target, "ev"),
        ("e1_official_typicality_or_certificate", branch_target, "ev"),
        ("e1_clean_anchor_exact_collision_allowance", branch_target, "ev"),
        ("e1_pair_feasible_ambient_generation", branch_target, "ev"),
        ("e1_pair_feasible_prime_field_reduction", branch_target, "ev"),
        ("e1_prime_field_l2_norm_collision_radius", branch_target, "ev"),
        ("e1_n256_s16_high_variance_collision_exclusion", branch_target, "ev"),
        ("e1_n256_s16_sparse_l1_variance_exclusion", branch_target, "ev"),
        ("e1_n256_proper_conductor_collision_exclusion", branch_target, "ev"),
        ("e1_n256_2adic_cofactor_collision_exclusion", branch_target, "ev"),
        ("e1_n256_s16_signed_chord_collision_gate", branch_target, "ev"),
        ("e1_n256_local_norm_cofactor_collapse", branch_target, "ev"),
        ("e1_n512_four_singleton_collision_exclusion", branch_target, "ev"),
        ("e1_n512_trinomial_interval_norm_exclusion", branch_target, "ev"),
    }
    require(evidence_edges <= edges, "named-exhibit route is not evidence-only")
    require(
        (branch_target, "e1_fullness", "req") in edges,
        "corrected direct-E1 target no longer gates e1_fullness",
    )
    exact_compiler = "e1_clean_anchor_exact_collision_allowance"
    require(nodes[exact_compiler]["status"] == "PROVED", "finite E1 compiler is not proved")
    compiler_statement = nodes[exact_compiler]["statement"].lower()
    require("k-|image|<=p" in compiler_statement, "collision-loss inequality is missing")
    require("b<=b* rules out direct e1" in compiler_statement,
            "small-generated-field route cut is missing")
    require("p>=p_min(k,b)" in compiler_statement,
            "balanced-fiber pair floor is missing")
    require("b_pair_min=ceil((k+b*+1)/3)" in compiler_statement,
            "pair-feasibility threshold is missing")
    require((exact_compiler, "e1_fullness", "req") in edges,
            "finite compiler no longer gates e1_fullness")
    ambient_generation = "e1_pair_feasible_ambient_generation"
    require(nodes[ambient_generation]["status"] == "PROVED",
            "pair-feasible ambient generation regressed")
    require("f_p(q)=f_q" in nodes[ambient_generation]["statement"].lower(),
            "ambient-generation conclusion is missing")
    require((exact_compiler, ambient_generation, "req") in edges,
            "ambient-generation node lost its threshold parent")
    prime_field = "e1_pair_feasible_prime_field_reduction"
    require(nodes[prime_field]["status"] == "PROVED",
            "pair-feasible prime-field reduction regressed")
    prime_statement = nodes[prime_field]["statement"].lower()
    require("q=p" in prime_statement and "p=1 mod n" in prime_statement,
            "prime-field conclusion is missing")
    require((ambient_generation, prime_field, "req") in edges,
            "prime-field reduction lost its ambient-generation parent")
    l2_radius = "e1_prime_field_l2_norm_collision_radius"
    require(nodes[l2_radius]["status"] == "PROVED",
            "folded L2 collision radius regressed")
    l2_statement = nodes[l2_radius]["statement"].lower()
    require("s<=4" in l2_statement and "s=1" in l2_statement,
            "folded L2 collision bands are missing")
    require((prime_field, l2_radius, "req") in edges,
            "folded L2 radius lost its prime-field parent")
    require(("collision_norm_criterion", l2_radius, "req") in edges,
            "folded L2 radius lost its norm parent")
    n256_s16 = "e1_n256_s16_high_variance_collision_exclusion"
    require(nodes[n256_s16]["status"] == "PROVED",
            "N=256 square-mass-16 variance exclusion regressed")
    n256_s16_statement = nodes[n256_s16]["statement"].lower()
    require("v>=136" in n256_s16_statement and "v<=134" in n256_s16_statement,
            "N=256 low-variance residual is missing")
    require((l2_radius, n256_s16, "req") in edges,
            "N=256 variance exclusion lost its L2 parent")
    require(("collision_norm_criterion", n256_s16, "req") in edges,
            "N=256 variance exclusion lost its norm parent")
    sparse_l1 = "e1_n256_s16_sparse_l1_variance_exclusion"
    require(nodes[sparse_l1]["status"] == "PROVED",
            "N=256 sparse-L1 variance exclusion regressed")
    sparse_l1_statement = nodes[sparse_l1]["statement"].lower()
    require("90<=v<=134" in sparse_l1_statement and "v<=88" in sparse_l1_statement,
            "N=256 sparse-L1 residual is missing")
    require((n256_s16, sparse_l1, "req") in edges,
            "sparse-L1 exclusion lost its variance parent")
    require(("collision_norm_criterion", sparse_l1, "req") in edges,
            "sparse-L1 exclusion lost its norm parent")
    proper_conductor = "e1_n256_proper_conductor_collision_exclusion"
    require(nodes[proper_conductor]["status"] == "PROVED",
            "N=256 proper-conductor exclusion regressed")
    proper_statement = nodes[proper_conductor]["statement"].lower()
    require("full conductor" in proper_statement and "18^32<2^250" in proper_statement,
            "N=256 proper-conductor conclusion is missing")
    require((l2_radius, proper_conductor, "req") in edges,
            "proper-conductor exclusion lost its L2 parent")
    require(("collision_norm_criterion", proper_conductor, "req") in edges,
            "proper-conductor exclusion lost its norm parent")
    two_adic = "e1_n256_2adic_cofactor_collision_exclusion"
    require(nodes[two_adic]["status"] == "PROVED",
            "N=256 2-adic cofactor exclusion regressed")
    two_adic_statement = nodes[two_adic]["statement"].lower()
    require("mu<=5" in two_adic_statement and "not divisible by 32" in two_adic_statement,
            "N=256 2-adic cofactor conclusion is missing")
    require((l2_radius, two_adic, "req") in edges,
            "2-adic cofactor exclusion lost its L2 parent")
    require(("collision_norm_criterion", two_adic, "req") in edges,
            "2-adic cofactor exclusion lost its norm parent")
    signed_chord = "e1_n256_s16_signed_chord_collision_gate"
    require(nodes[signed_chord]["status"] == "PROVED",
            "N=256 signed-chord gate regressed")
    signed_chord_statement = nodes[signed_chord]["statement"].lower()
    require("c<=-19" in signed_chord_statement and "circular sidon" in signed_chord_statement,
            "N=256 signed-chord conclusion is missing")
    require((sparse_l1, signed_chord, "req") in edges,
            "signed-chord gate lost its sparse-L1 parent")
    local_norm = "e1_n256_local_norm_cofactor_collapse"
    require(nodes[local_norm]["status"] == "PROVED",
            "N=256 local-norm cofactor collapse regressed")
    local_norm_statement = nodes[local_norm]["statement"].lower()
    require("r=2^mu p" in local_norm_statement and "419" in local_norm_statement,
            "N=256 local-norm cofactor conclusion is missing")
    require((prime_field, local_norm, "req") in edges,
            "local-norm cofactor collapse lost its prime-field parent")
    require((two_adic, local_norm, "req") in edges,
            "local-norm cofactor collapse lost its 2-adic parent")
    four_singleton = "e1_n512_four_singleton_collision_exclusion"
    require(nodes[four_singleton]["status"] == "PROVED",
            "N=512 four-singleton exclusion regressed")
    four_singleton_statement = nodes[four_singleton]["statement"].lower()
    require("(0,4,0)" in four_singleton_statement and "(1,2,0)" in four_singleton_statement,
            "N=512 first-band profile reduction is missing")
    require((l2_radius, four_singleton, "req") in edges,
            "four-singleton exclusion lost its L2 parent")
    require(("collision_norm_criterion", four_singleton, "req") in edges,
            "four-singleton exclusion lost its norm parent")
    trinomial = "e1_n512_trinomial_interval_norm_exclusion"
    require(nodes[trinomial]["status"] == "PROVED",
            "N=512 trinomial interval exclusion regressed")
    trinomial_statement = nodes[trinomial]["statement"].lower()
    require("129540" in trinomial_statement and "s>=3" in trinomial_statement,
            "N=512 complete first-band close is missing")
    require((l2_radius, trinomial, "req") in edges,
            "trinomial exclusion lost its L2 parent")
    require((four_singleton, trinomial, "req") in edges,
            "trinomial exclusion lost its four-singleton parent")
    require(("collision_norm_criterion", trinomial, "req") in edges,
            "trinomial exclusion lost its norm parent")
    universal = "unsafe_crossing_family_instantiation"
    for source in (
        exact_compiler,
        ambient_generation,
        prime_field,
        l2_radius,
        n256_s16,
        sparse_l1,
        proper_conductor,
        two_adic,
        signed_chord,
        local_norm,
        four_singleton,
        trinomial,
        branch_target,
        "e1_fullness",
    ):
        require((source, universal, "ev") in edges,
                f"{source} lost its evidence edge to the universal target")

    route_folder = ROOT / "background" / "nodes" / branch_target
    require(route_folder.is_dir(), "direct E1 target left the background tree")
    require(
        not (ROOT / "critical" / "nodes" / branch_target).exists(),
        "route-local E1 target leaked onto the critical surface",
    )
    require(
        not (route_folder / "conditional.md").exists(),
        "invalid named-exhibit conditional proof remains live",
    )
    require(
        (route_folder / "status_ruling.md").is_file(),
        "direct E1 status ruling is missing",
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

    for node_id in offorbit_route:
        require(
            (ROOT / "background" / "nodes" / node_id).is_dir(),
            f"off-orbit E1 route node {node_id} is not in background",
        )
        require(
            not (ROOT / "critical" / "nodes" / node_id).exists(),
            f"off-orbit E1 route node {node_id} leaked into critical",
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
        f"route_target={branch_target} background_exhibit_nodes={len(background_branch)} "
        f"offorbit_route_nodes={len(offorbit_route)}"
    )


if __name__ == "__main__":
    main()
