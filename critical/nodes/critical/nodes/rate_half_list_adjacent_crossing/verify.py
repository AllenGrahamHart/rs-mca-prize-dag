#!/usr/bin/env python3
"""Check the rate-half ordinary-list scope repair and its DAG wiring."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE_ID = "rate_half_list_adjacent_crossing"
CONSUMER = "list_adjacency_closing"
FLOOR = "rate_half_cyclic_rotated_prefix_floor"
SAFE_ANCHOR = "rate_half_list_integer_johnson_safe_anchor"
LOW_BUDGET = "rate_half_list_low_budget_exact_crossing"
BUDGET_THREE = "rate_half_list_budget_three_intersection_reduction"
CYCLE_BIMOBIUS = "rate_half_list_budget_three_cycle_bimobius_transversal"
RESIDUAL_TRANSVERSAL = "rate_half_list_budget_three_residual_transversal_atlas"
K4_GRASSMANN = "rate_half_list_budget_three_k4_grassmann_line"
LINEAR_GRASSMANN = "rate_half_list_budget_three_linear_grassmann_atlas"
MAXIMAL_FIELD = "rate_half_list_budget_three_maximal_field_degree_collapse"
QUADRATIC_SCROLL = "rate_half_list_budget_three_quadratic_scroll_atlas"
QUADRATIC_FULL_RANK = "rate_half_list_budget_three_quadratic_scroll_full_rank"
QUADRATIC_PRIMITIVE = "rate_half_list_budget_three_quadratic_scroll_primitive_module"
SPLIT_PENCIL = "rate_half_list_budget_three_split_pencil_normal_form"
SPLIT_UNIT_SINGLE_FIBER = "rate_half_list_budget_three_split_unit_single_fiber_exclusion"
PLUCKER_GATE = "rate_half_list_budget_three_plucker_edge_gate"
SPLIT_FIBER = "rate_half_list_budget_three_split_fiber_atlas"
PATH_MOBIUS = "rate_half_list_budget_three_path_mobius_transversal"
PATH_WITNESS = "rate_half_list_budget_three_path_power_two_witness"
PATH_CHARACTERISTIC = "rate_half_list_budget_three_path_pattern_characteristic_isolation"
MULTIFIBER = "rate_half_list_budget_three_multifiber_vandermonde_exclusion"
MULTIDELETION = "rate_half_list_budget_three_multideletion_multifiber_exclusion"
FIBER_FOUR_GATE = "rate_half_list_budget_three_fiber_four_rank_gate"
ANTIPODAL_DESCENT = "rate_half_list_budget_three_fiber_four_antipodal_descent"
ANTIPODAL_WELD = "rate_half_list_budget_three_antipodal_mobius_weld"
ANTIPODAL_DEGREE_FLOOR = "rate_half_list_budget_three_antipodal_pencil_degree_floor"
ANTIPODAL_PRIMITIVE = "rate_half_list_budget_three_antipodal_primitive_quotient_gate"
ANTIPODAL_PURE_QUARTIC = "rate_half_list_budget_three_antipodal_pure_quartic_degree_rigidity"
ANTIPODAL_REVERSE_RESIDUAL = "rate_half_list_budget_three_antipodal_reverse_residual_stratification"
ANTIPODAL_FOURTH_ROOT_GAP = "rate_half_list_budget_three_antipodal_fourth_root_gap_reduction"
ANTIPODAL_GENERIC_SECONDARY_GAP = "rate_half_list_budget_three_antipodal_generic_secondary_gap_reduction"
ANTIPODAL_GENERIC_TWO_WINDOW = "rate_half_list_budget_three_antipodal_generic_two_window_square_reduction"
ANTIPODAL_GENERIC_DELETED_PAIR_PARITY = "rate_half_list_budget_three_antipodal_generic_deleted_pair_parity_reduction"
ANTIPODAL_GENERIC_DELETED_PAIR_FACTORIZATION = "rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization"
ANTIPODAL_GENERIC_DELETED_PAIR_BRANCH = "rate_half_list_budget_three_antipodal_generic_deleted_pair_fourier_resultant_branch_collapse"
ANTIPODAL_GENERIC_DELETED_PAIR_ODE = "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_ode"
ANTIPODAL_GENERIC_DELETED_PAIR_MOBIUS = "rate_half_list_budget_three_antipodal_generic_deleted_pair_mobius_ratio_router"
ANTIPODAL_GENERIC_DELETED_PAIR_REMAINDER = "rate_half_list_budget_three_antipodal_generic_deleted_pair_remainder_square_router"
ANTIPODAL_GENERIC_DELETED_PAIR_HARMONIC = "rate_half_list_budget_three_antipodal_generic_deleted_pair_harmonic_exclusion"
ANTIPODAL_GENERIC_DELETED_PAIR_NONHARMONIC = "rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_scalar_router"
ANTIPODAL_GENERIC_DELETED_PAIR_FOURTH_POWER = "rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_fourth_power_router"
ANTIPODAL_GENERIC_DELETED_PAIR_GCD = "rate_half_list_budget_three_antipodal_generic_deleted_pair_fourth_root_gcd_gate"
ANTIPODAL_GENERIC_DELETED_PAIR_CONSTANT = "rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_coefficient_gate"
ANTIPODAL_GENERIC_CANONICAL_SPAN = "rate_half_list_budget_three_antipodal_generic_canonical_span_criterion"
ANTIPODAL_INTERMEDIATE_HENSEL = "rate_half_list_budget_three_antipodal_intermediate_hensel_certifier"
ANTIPODAL_PURE_HARMONIC_FERMAT = "rate_half_list_budget_three_antipodal_pure_harmonic_fermat_router"


def main() -> int:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    packet = ROOT / "critical" / "nodes" / NODE_ID
    statement = (packet / "statement.md").read_text()
    consumer = (
        ROOT / "critical" / "nodes" / CONSUMER / "conditional.md"
    ).read_text()
    floor_statement = (
        ROOT / "critical" / "nodes" / FLOOR / "statement.md"
    ).read_text()

    incoming = sorted(
        (edge["from"], edge.get("kind"))
        for edge in dag["edges"]
        if edge["to"] == NODE_ID
    )
    outgoing_req = sorted(
        edge["to"]
        for edge in dag["edges"]
        if edge["from"] == NODE_ID and edge.get("kind") == "req"
    )
    old_floor_consumer = sorted(
        edge.get("kind")
        for edge in dag["edges"]
        if edge["from"] == FLOOR and edge["to"] == CONSUMER
    )

    checks = [
        ("node_exists", NODE_ID in nodes),
        ("node_is_target", nodes[NODE_ID]["status"] == "TARGET"),
        ("floor_is_proved", nodes[FLOOR]["status"] == "PROVED"),
        ("safe_anchor_is_proved", nodes[SAFE_ANCHOR]["status"] == "PROVED"),
        ("low_budget_is_proved", nodes[LOW_BUDGET]["status"] == "PROVED"),
        ("budget_three_reduction_is_proved", nodes[BUDGET_THREE]["status"] == "PROVED"),
        ("cycle_bimobius_transversal_is_proved", nodes[CYCLE_BIMOBIUS]["status"] == "PROVED"),
        ("residual_transversal_atlas_is_proved", nodes[RESIDUAL_TRANSVERSAL]["status"] == "PROVED"),
        ("k4_grassmann_line_is_proved", nodes[K4_GRASSMANN]["status"] == "PROVED"),
        ("linear_grassmann_atlas_is_proved", nodes[LINEAR_GRASSMANN]["status"] == "PROVED"),
        ("maximal_field_degree_collapse_is_proved", nodes[MAXIMAL_FIELD]["status"] == "PROVED"),
        ("quadratic_scroll_atlas_is_proved", nodes[QUADRATIC_SCROLL]["status"] == "PROVED"),
        ("quadratic_scroll_full_rank_is_proved", nodes[QUADRATIC_FULL_RANK]["status"] == "PROVED"),
        ("quadratic_scroll_primitive_module_is_proved", nodes[QUADRATIC_PRIMITIVE]["status"] == "PROVED"),
        ("split_pencil_normal_form_is_proved", nodes[SPLIT_PENCIL]["status"] == "PROVED"),
        ("split_unit_single_fiber_exclusion_is_proved", nodes[SPLIT_UNIT_SINGLE_FIBER]["status"] == "PROVED"),
        ("plucker_edge_gate_is_proved", nodes[PLUCKER_GATE]["status"] == "PROVED"),
        ("split_fiber_atlas_is_proved", nodes[SPLIT_FIBER]["status"] == "PROVED"),
        ("path_mobius_transversal_is_proved", nodes[PATH_MOBIUS]["status"] == "PROVED"),
        ("path_power_two_witness_is_proved", nodes[PATH_WITNESS]["status"] == "PROVED"),
        ("path_characteristic_isolation_is_proved", nodes[PATH_CHARACTERISTIC]["status"] == "PROVED"),
        ("multifiber_exclusion_is_proved", nodes[MULTIFIBER]["status"] == "PROVED"),
        ("multideletion_exclusion_is_proved", nodes[MULTIDELETION]["status"] == "PROVED"),
        ("fiber_four_gate_is_proved", nodes[FIBER_FOUR_GATE]["status"] == "PROVED"),
        ("antipodal_descent_is_proved", nodes[ANTIPODAL_DESCENT]["status"] == "PROVED"),
        ("antipodal_weld_is_proved", nodes[ANTIPODAL_WELD]["status"] == "PROVED"),
        ("antipodal_degree_floor_is_proved", nodes[ANTIPODAL_DEGREE_FLOOR]["status"] == "PROVED"),
        ("antipodal_primitive_gate_is_proved", nodes[ANTIPODAL_PRIMITIVE]["status"] == "PROVED"),
        ("antipodal_pure_quartic_is_proved", nodes[ANTIPODAL_PURE_QUARTIC]["status"] == "PROVED"),
        ("antipodal_reverse_residual_is_proved", nodes[ANTIPODAL_REVERSE_RESIDUAL]["status"] == "PROVED"),
        ("antipodal_fourth_root_gap_is_proved", nodes[ANTIPODAL_FOURTH_ROOT_GAP]["status"] == "PROVED"),
        ("antipodal_generic_secondary_gap_is_proved", nodes[ANTIPODAL_GENERIC_SECONDARY_GAP]["status"] == "PROVED"),
        ("antipodal_generic_two_window_is_proved", nodes[ANTIPODAL_GENERIC_TWO_WINDOW]["status"] == "PROVED"),
        ("antipodal_generic_deleted_pair_parity_is_proved", nodes[ANTIPODAL_GENERIC_DELETED_PAIR_PARITY]["status"] == "PROVED"),
        ("antipodal_generic_deleted_pair_factorization_is_proved", nodes[ANTIPODAL_GENERIC_DELETED_PAIR_FACTORIZATION]["status"] == "PROVED"),
        ("antipodal_generic_deleted_pair_branch_is_proved", nodes[ANTIPODAL_GENERIC_DELETED_PAIR_BRANCH]["status"] == "PROVED"),
        ("antipodal_generic_deleted_pair_ode_is_proved", nodes[ANTIPODAL_GENERIC_DELETED_PAIR_ODE]["status"] == "PROVED"),
        ("antipodal_generic_deleted_pair_mobius_is_proved", nodes[ANTIPODAL_GENERIC_DELETED_PAIR_MOBIUS]["status"] == "PROVED"),
        ("antipodal_generic_deleted_pair_remainder_is_proved", nodes[ANTIPODAL_GENERIC_DELETED_PAIR_REMAINDER]["status"] == "PROVED"),
        ("antipodal_generic_deleted_pair_harmonic_is_proved", nodes[ANTIPODAL_GENERIC_DELETED_PAIR_HARMONIC]["status"] == "PROVED"),
        ("antipodal_generic_deleted_pair_nonharmonic_is_proved", nodes[ANTIPODAL_GENERIC_DELETED_PAIR_NONHARMONIC]["status"] == "PROVED"),
        ("antipodal_generic_deleted_pair_fourth_power_is_proved", nodes[ANTIPODAL_GENERIC_DELETED_PAIR_FOURTH_POWER]["status"] == "PROVED"),
        ("antipodal_generic_deleted_pair_gcd_is_proved", nodes[ANTIPODAL_GENERIC_DELETED_PAIR_GCD]["status"] == "PROVED"),
        ("antipodal_generic_deleted_pair_constant_is_proved", nodes[ANTIPODAL_GENERIC_DELETED_PAIR_CONSTANT]["status"] == "PROVED"),
        ("antipodal_generic_canonical_span_is_proved", nodes[ANTIPODAL_GENERIC_CANONICAL_SPAN]["status"] == "PROVED"),
        ("antipodal_intermediate_hensel_is_proved", nodes[ANTIPODAL_INTERMEDIATE_HENSEL]["status"] == "PROVED"),
        ("antipodal_pure_harmonic_fermat_is_proved", nodes[ANTIPODAL_PURE_HARMONIC_FERMAT]["status"] == "PROVED"),
        (
            "brackets_are_evidence",
            incoming
            == [
                (FLOOR, "ev"),
                (ANTIPODAL_FOURTH_ROOT_GAP, "ev"),
                (ANTIPODAL_GENERIC_CANONICAL_SPAN, "ev"),
                (ANTIPODAL_GENERIC_DELETED_PAIR_CONSTANT, "ev"),
                (ANTIPODAL_GENERIC_DELETED_PAIR_ODE, "ev"),
                (ANTIPODAL_GENERIC_DELETED_PAIR_FACTORIZATION, "ev"),
                (ANTIPODAL_GENERIC_DELETED_PAIR_BRANCH, "ev"),
                (ANTIPODAL_GENERIC_DELETED_PAIR_GCD, "ev"),
                (ANTIPODAL_GENERIC_DELETED_PAIR_HARMONIC, "ev"),
                (ANTIPODAL_GENERIC_DELETED_PAIR_MOBIUS, "ev"),
                (ANTIPODAL_GENERIC_DELETED_PAIR_FOURTH_POWER, "ev"),
                (ANTIPODAL_GENERIC_DELETED_PAIR_NONHARMONIC, "ev"),
                (ANTIPODAL_GENERIC_DELETED_PAIR_PARITY, "ev"),
                (ANTIPODAL_GENERIC_DELETED_PAIR_REMAINDER, "ev"),
                (ANTIPODAL_GENERIC_SECONDARY_GAP, "ev"),
                (ANTIPODAL_GENERIC_TWO_WINDOW, "ev"),
                (ANTIPODAL_INTERMEDIATE_HENSEL, "ev"),
                (ANTIPODAL_WELD, "ev"),
                (ANTIPODAL_DEGREE_FLOOR, "ev"),
                (ANTIPODAL_PRIMITIVE, "ev"),
                (ANTIPODAL_PURE_HARMONIC_FERMAT, "ev"),
                (ANTIPODAL_PURE_QUARTIC, "ev"),
                (ANTIPODAL_REVERSE_RESIDUAL, "ev"),
                (CYCLE_BIMOBIUS, "ev"),
                (ANTIPODAL_DESCENT, "ev"),
                (FIBER_FOUR_GATE, "ev"),
                (BUDGET_THREE, "ev"),
                (K4_GRASSMANN, "ev"),
                (LINEAR_GRASSMANN, "ev"),
                (MAXIMAL_FIELD, "ev"),
                (MULTIDELETION, "ev"),
                (MULTIFIBER, "ev"),
                (PATH_MOBIUS, "ev"),
                (PATH_CHARACTERISTIC, "ev"),
                (PATH_WITNESS, "ev"),
                (PLUCKER_GATE, "ev"),
                (QUADRATIC_SCROLL, "ev"),
                (QUADRATIC_FULL_RANK, "ev"),
                (QUADRATIC_PRIMITIVE, "ev"),
                (RESIDUAL_TRANSVERSAL, "ev"),
                (SPLIT_FIBER, "ev"),
                (SPLIT_PENCIL, "ev"),
                (SPLIT_UNIT_SINGLE_FIBER, "ev"),
                (SAFE_ANCHOR, "ev"),
                (LOW_BUDGET, "ev"),
            ],
        ),
        ("direct_consumer", outgoing_req == [CONSUMER]),
        ("floor_remains_parent_requirement", old_floor_consumer == ["req"]),
        ("consumer_names_new_leaf", NODE_ID in consumer),
        ("statement_pins_ordinary_object", "L_1(a)" in statement and "m=1" in statement),
        ("statement_pins_threshold", "B*=floor(q/2^128)" in statement),
        (
            "statement_pins_razor_lower_bound",
            "17,179,869,184" in statement and "k+2^34" in statement,
        ),
        (
            "statement_pins_safe_anchor",
            "a_IJ(C)" in statement and "1554944255988" in statement,
        ),
        (
            "statement_pins_exact_low_budgets",
            "B* in {1,2}" in statement and "a_L(C)=3n/4" in statement,
        ),
        (
            "statement_pins_budget_three_reduction",
            "six incidence types" in statement and "4-wise RS" in statement,
        ),
        (
            "statement_pins_split_pencil_normal_form",
            "A_k b_ij+A_i b_jk=A_j b_ik" in statement and "degree at most two" in statement,
        ),
        (
            "statement_pins_plucker_gate",
            "b_01b_23-b_02b_13+b_03b_12=0" in statement and "degree at most four" in statement,
        ),
        (
            "statement_pins_split_fiber_atlas",
            "thirteen necessary" in statement and "three-member constant split pencils" in statement,
        ),
        (
            "statement_pins_path_mobius_transversal",
            "injective Mobius-transversal" in statement
            and "order-eight singular witness" in statement,
        ),
        (
            "statement_pins_path_power_two_witness",
            "RS[F_17,F_17^*,8]" in statement and "power-of-two" in statement,
        ),
        (
            "statement_pins_cycle_bimobius_transversal",
            "two complete" in statement and "constant fibers" in statement
            and "at most six domain roots" in statement,
        ),
        (
            "statement_pins_residual_transversal_atlas",
            "all six incidence types" in statement
            and "Every fourth-member route has been closed" in statement
            and "degree-two graph fibers" in statement,
        ),
        (
            "statement_pins_k4_grassmann_line",
            "projective line on `Gr(2,4)`" in statement
            and "lambda_0lambda_1lambda_2lambda_3!=0" in statement
            and "exactly eight roots" in statement,
        ),
        (
            "statement_pins_linear_grassmann_atlas",
            "nine of the thirteen edge-degree" in statement
            and "exactly four quadratic" in statement
            and "three pendant chambers" in statement
            and "`K_4-e` chamber" in statement,
        ),
        (
            "statement_pins_quadratic_scroll_atlas",
            "four conics are now normalized as balanced Grassmann scrolls" in statement
            and "C^(-1)A=(alpha,X alpha,beta,X beta)^T" in statement
            and "bounded edge geometry is complete" in statement,
        ),
        (
            "statement_pins_quadratic_scroll_full_rank",
            "b_01^2(L_12L_03-L_02L_13)!=0" in statement
            and "rank-deficient quadratic split-unit branch is empty" in statement
            and "full-rank balanced scrolls" in statement
            and "four full-rank scroll chambers" in statement,
        ),
        (
            "statement_pins_quadratic_scroll_primitive_module",
            "automatically coprime" in statement
            and "degrees are exactly `(d-2,d-1)`" in statement
            and "`(d-2,d-2)`" in statement
            and "<alpha,Xalpha> intersect <beta,Xbeta>={0}" in statement
            and "genuinely four-dimensional" in statement,
        ),
        (
            "statement_pins_maximal_field_degree_collapse",
            "At the maximal `n=2^41` row" in statement
            and "e=1 with p=1 mod 2^41" in statement
            and "e=2 with p=+/-1 mod 2^40" in statement
            and "divisible by seven" in statement
            and "This gate is scoped" in statement
            and "to the maximal domain" in statement,
        ),
        (
            "statement_pins_split_unit_single_fiber_exclusion",
            "direct quotient-periodic construction" in statement
            and "at most eight geometric Vandermonde" in statement
            and "independent for `d>=8`" in statement
            and "primitive or use a genuinely multi-fiber" in statement,
        ),
        (
            "statement_pins_path_characteristic_isolation",
            "full cyclotomic" in statement
            and "2^170 17^4" in statement
            and "unchanged-exponent transport" in statement,
        ),
        (
            "statement_pins_multifiber_exclusion",
            "top `m`" in statement
            and "Vandermonde-independent" in statement
            and "survive only at fiber sizes" in statement
            and "`1,2`" in statement,
        ),
        (
            "statement_pins_multideletion_exclusion",
            "reversed top coefficients" in statement
            and "m>sum ell_i-ell_min" in statement
            and "m>=8" in statement,
        ),
        (
            "statement_pins_fiber_four_gate",
            "fiber-four residue gate" in statement
            and "rank three forces" in statement
            and "rank-two reciprocal locus" in statement,
        ),
        (
            "statement_pins_antipodal_descent",
            "descends one exact" in statement
            and "quotient level" in statement
            and "degree-`2^37-1`" in statement
            and "exact quotient split-pencil census" in statement,
        ),
        (
            "statement_pins_antipodal_weld",
            "quartic norm equation" in statement
            and "Möbius image" in statement
            and "deg R,deg S<=2^37-1" in statement,
        ),
        (
            "statement_pins_antipodal_primitive_gate",
            "reduced rational degree is" in statement
            and "cyclic or dihedral quotient" in statement
            and "nonzero Vandermonde matrix" in statement
            and "primitive, nonperiodic pencil census" in statement,
        ),
        (
            "statement_pins_antipodal_degree_floor",
            "unique degree-drop direction" in statement
            and "deg V>=2^36-2" in statement
            and "deg V>=(2^38-4)/3" in statement
            and "reverse-polynomial contact" in statement
            and "two high-degree" in statement,
        ),
        (
            "statement_pins_antipodal_pure_quartic",
            "centered pure-quartic" in statement
            and "e_2=e_3=0" in statement
            and "deg V=r-1=2^37-2" in statement
            and "deg L=1" in statement
            and "Both `U,V` are squarefree" in statement
            and "second-derivative Wronskian" in statement,
        ),
        (
            "statement_pins_antipodal_reverse_residual",
            "T=dDU-Y(D'U+4DU')" in statement
            and "exact degree `r+4-qh`" in statement
            and "lowest official generic boundary `T` is linear" in statement
            and "lowest intermediate boundary it is quadratic" in statement,
        ),
        (
            "statement_pins_antipodal_fourth_root_gap",
            "E(z)^(-1/4)=sum_(m>=0)a_mz^m" in statement
            and "monic direction is unique" in statement
            and "a_(r+1)=a_(r+2)=0" in statement
            and "a_(r+1)=0" in statement
            and "four-term recurrence" in statement,
        ),
        (
            "statement_pins_antipodal_generic_secondary_gap",
            "J=z^(-2h)R/B^2" in statement
            and "P=C/C(0) mod z^h" in statement
            and "[z^(2^36-1)]P=[z^(2^36)]P=0" in statement
            and "nested fourth-root and square-root" in statement,
        ),
        (
            "statement_pins_antipodal_generic_two_window",
            "P^2=L T/a_(2h) mod z^h" in statement
            and "first-order differential equation" in statement
            and "does not exclude" in statement,
        ),
        (
            "statement_pins_antipodal_generic_deleted_pair_parity",
            "F_(2M)(t)=0" in statement
            and "t^(8M)=1" in statement
            and "one torsion variable" in statement,
        ),
        (
            "statement_pins_antipodal_generic_deleted_pair_factorization",
            "beta` to vanish" in statement
            and "B_0^2+lambda w^(2M+1)C_0^2" in statement
            and "degree `4M-1`" in statement
            and "-h(lambda-mu)" in statement,
        ),
        (
            "statement_pins_antipodal_generic_deleted_pair_branch",
            "p<4N^2" in statement
            and "p<2N" in statement
            and "p=1 mod 2^40" in statement
            and "descend to `F_p`" in statement,
        ),
        (
            "statement_pins_antipodal_generic_deleted_pair_ode",
            "U=YU_0(x)" in statement
            and "constant-forcing ODE" in statement
            and "(16M-4)D_0U_0-2xD_0'U_0-8xD_0U_0'=kappa" in statement
            and "at most one monic" in statement
            and "only exceptional root" in statement,
        ),
        (
            "statement_pins_antipodal_generic_deleted_pair_mobius",
            "(1,iota,r,iota r)" in statement
            and "q^N=1" in statement
            and "r^2(1+q)^2=4q(r^2-r+1)^2" in statement
            and "(r-1)^4(1+q)^2=4q(r+1)^4" in statement
            and "(r^2+1)^2(1+q)^2=4q(r^2-4r+1)^2" in statement
            and "at most three unordered" in statement
            and "retain `q=-1`" in statement,
        ),
        (
            "statement_pins_antipodal_generic_deleted_pair_remainder",
            "R=Q-A^2" in statement
            and "divide `R=AS+T`" in statement
            and "T=qS^2/(1+q)^2" in statement
            and "S/(1+q) is a nonzero polynomial square" in statement
            and "`-R` be a fourth power" in statement
            and "no free `V_0`" in statement,
        ),
        (
            "statement_pins_antipodal_generic_deleted_pair_harmonic",
            "r^2-r+1=0" in statement
            and "c_(j+1)=c_j^2-2" in statement
            and "4,495,441" in statement
            and "q!=-1" in statement
            and "only by the Euclidean quotient-square" in statement,
        ),
        (
            "statement_pins_antipodal_generic_deleted_pair_nonharmonic",
            "4b_jT=a_jS^2" in statement
            and "X^2-yX+1" in statement
            and "y_38=2" in statement
            and "reciprocal root choice" in statement
            and "three one-variable certifiers" in statement,
        ),
        (
            "statement_pins_antipodal_generic_deleted_pair_fourth_power",
            "chi=r+r^(-1)" in statement
            and "h_0=1/(2(chi-1))" in statement
            and "T=(h_jS)^2" in statement
            and "T=W^4" in statement
            and "one common" in statement
            and "fourth-power test" in statement,
        ),
        (
            "statement_pins_antipodal_generic_deleted_pair_gcd",
            "P=2N+kappa x^2U_0^3" in statement
            and "2xD_0R'=P+2(ND_0-xD_0')R" in statement
            and "W|P" in statement
            and "S|P^2" in statement
            and "deg gcd(S,P)>=M-1" in statement,
        ),
        (
            "statement_pins_antipodal_generic_deleted_pair_constant",
            "sigma=[z^(2M-2)]" in statement
            and "=S(0)" in statement
            and "t sigma^2+4(chi-1)^2=0" in statement
            and "t(chi-2)^2sigma^2+4(chi+2)^2=0" in statement
            and "t chi^2sigma^2+4(chi-4)^2=0" in statement,
        ),
        (
            "statement_pins_antipodal_generic_canonical_span",
            "S=beta X+gamma Y" in statement
            and "beta=[z^h]S" in statement
            and "fractionally-linearly matched" in statement
            and "four subgroup roots" in statement
            and "checking only a" in statement
            and "prefix of the span identity is insufficient" in statement,
        ),
        (
            "statement_pins_antipodal_intermediate_hensel",
            "H=C_u^3(1+u z^h C_u/B)" in statement
            and "3kappa-uDelta=0" in statement
            and "u=3kappa/Delta" in statement
            and "only `Delta=kappa=0` retains one scalar" in statement
            and "W^4+theta W+theta u" in statement,
        ),
        (
            "statement_pins_antipodal_pure_harmonic_fermat",
            "pure deleted-root lifts to be harmonic" in statement
            and "w=(2x-y(1+x))/(1+x-2y)" in statement
            and "Q=(1-z^d)/E=B^4+Z^4" in statement
            and "Harmonicity alone is not empty" in statement,
        ),
        ("floor_disclaims_safe_side", "no safe-side list claim" in floor_statement),
        (
            "packet_complete",
            all(
                (packet / name).is_file()
                for name in [
                    "statement.md",
                    "attack.md",
                    "frontier.md",
                    "claim_contract.md",
                    "dependency_subdag.md",
                ]
            ),
        ),
    ]

    result = {
        "node": NODE_ID,
        "status": "PASS" if all(ok for _, ok in checks) else "FAIL",
        "checks": [{"name": name, "ok": ok} for name, ok in checks],
        "nonclaim": "Budgets one and two are exact; the adjacent crossing remains open for B*>=3.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
