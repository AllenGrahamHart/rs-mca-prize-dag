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
QUADRATIC_SCROLL = "rate_half_list_budget_three_quadratic_scroll_atlas"
QUADRATIC_FULL_RANK = "rate_half_list_budget_three_quadratic_scroll_full_rank"
SPLIT_PENCIL = "rate_half_list_budget_three_split_pencil_normal_form"
PLUCKER_GATE = "rate_half_list_budget_three_plucker_edge_gate"
SPLIT_FIBER = "rate_half_list_budget_three_split_fiber_atlas"
PATH_MOBIUS = "rate_half_list_budget_three_path_mobius_transversal"
PATH_WITNESS = "rate_half_list_budget_three_path_power_two_witness"


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
        ("quadratic_scroll_atlas_is_proved", nodes[QUADRATIC_SCROLL]["status"] == "PROVED"),
        ("quadratic_scroll_full_rank_is_proved", nodes[QUADRATIC_FULL_RANK]["status"] == "PROVED"),
        ("split_pencil_normal_form_is_proved", nodes[SPLIT_PENCIL]["status"] == "PROVED"),
        ("plucker_edge_gate_is_proved", nodes[PLUCKER_GATE]["status"] == "PROVED"),
        ("split_fiber_atlas_is_proved", nodes[SPLIT_FIBER]["status"] == "PROVED"),
        ("path_mobius_transversal_is_proved", nodes[PATH_MOBIUS]["status"] == "PROVED"),
        ("path_power_two_witness_is_proved", nodes[PATH_WITNESS]["status"] == "PROVED"),
        (
            "brackets_are_evidence",
            incoming
            == [
                (FLOOR, "ev"),
                (CYCLE_BIMOBIUS, "ev"),
                (BUDGET_THREE, "ev"),
                (K4_GRASSMANN, "ev"),
                (LINEAR_GRASSMANN, "ev"),
                (PATH_MOBIUS, "ev"),
                (PATH_WITNESS, "ev"),
                (PLUCKER_GATE, "ev"),
                (QUADRATIC_SCROLL, "ev"),
                (QUADRATIC_FULL_RANK, "ev"),
                (RESIDUAL_TRANSVERSAL, "ev"),
                (SPLIT_FIBER, "ev"),
                (SPLIT_PENCIL, "ev"),
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
