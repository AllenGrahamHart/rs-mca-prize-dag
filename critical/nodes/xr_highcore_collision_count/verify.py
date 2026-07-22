#!/usr/bin/env python3
"""Top-level contract replay for the still-open XR P-A target."""

from __future__ import annotations

import json
from fractions import Fraction
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_highcore_collision_count"

ROWS = (
    ("rowc-r1_4", 1024, 4, 256, 261, 3, 4, 5, 5),
    ("rowc-r1_8", 1024, 8, 256, 133, 3, 4, 5, 4),
    ("rowc-r1_16", 1024, 16, 512, 67, 3, 4, 5, 4),
    ("prize-r1_4", 1 << 41, 4, 256, 558_345_748_481, 11, 16, 17, 4),
    ("prize-r1_8", 1 << 41, 8, 256, 283_467_841_537, 10, 16, 17, 4),
    ("prize-r1_16", 1 << 41, 16, 512, 141_733_920_769, 9, 14, 15, 4),
)

PAID_INPUTS = (
    "xr_highcore_component_union_atlas",
    "xr_direction_distance_ray_bound",
    "xr_all_lineray_affine_core_bound",
    "xr_highcore_collision_line_basis_ledger",
    "xr_affine_core_cogirth_ray_bound",
    "xr_affine_core_all_zero_charge",
    "xr_poststrip_affine_pencil_charge",
    "xr_rs_common_root_basis_charge",
    "xr_higher_rank_uniform_split_pencil_reduction",
    "xr_higher_rank_collapsed_face_exclusion",
    "xr_higher_rank_first_residual_quadratic_involution",
    "xr_higher_rank_rank_two_shell_maxwell_router",
    "xr_prize_primitive_rank_two_shell_band",
    "xr_prize_first_shell_primitive_rank_three_exclusion",
    "xr_trade_circuit_arity_segre_atlas",
    "xr_rank_two_fundamental_circuit_owner",
    "xr_rank_two_three_anchor_grs3_factorization",
    "xr_rank_two_four_anchor_quadric_centroid_atlas",
    "xr_rank_two_dual_support_extension_factorization",
    "xr_rank_two_received_pair_alternating_router",
    "xr_rank_two_actual_block_extension_router",
    "xr_rank_two_extension_family_collision_ledger",
    "xr_tangent_support_mismatch_bridge",
    "xr_supportwise_transverse_lineray_rank_charge",
    "xr_tangent_mismatch_full_external_zero_canonicalization",
    "xr_mismatch_nongeneric_invariant_excess_descent",
    "xr_mismatch_descent_dimension_area_law",
    "xr_nongeneric_explanation_plotkin_width",
)


def require(condition: bool, detail: object) -> None:
    if not condition:
        raise AssertionError(detail)


def grk_depth(n: int, k: int, reserve: int) -> int:
    radius = n - k
    budget = 8 * n**3
    excess = 0
    while Fraction(
        comb(radius + excess, excess) * radius,
        comb(excess + reserve, excess),
    ) <= budget:
        excess += 1
    return excess - 1


def rational_max(values: tuple[tuple[int, int], ...]) -> tuple[int, int]:
    maximum = values[0]
    for candidate in values[1:]:
        if candidate[0] * maximum[1] > maximum[0] * candidate[1]:
            maximum = candidate
    return maximum


def common_root_paid_rank(n: int, k: int, reserve: int) -> tuple[int, int]:
    radius = n - k
    budget = 8 * n**3
    caps = (radius // reserve, (radius + 1) // (reserve + 1))
    paid = []
    for pencil_cap in caps:
        paid_ranks = []
        for affine_dimension in range(2, 80):
            kernel_rank = affine_dimension - 1
            quotient = comb(
                kernel_rank + reserve - 1,
                kernel_rank - 1,
            )
            chart_bases = comb(radius + kernel_rank, kernel_rank)
            common_roots = k - kernel_rank
            numerator, denominator = rational_max(
                (
                    (
                        kernel_rank * pencil_cap * chart_bases,
                        quotient * (kernel_rank + reserve),
                    ),
                    (
                        kernel_rank * pencil_cap * comb(n, kernel_rank),
                        quotient * (k + reserve),
                    ),
                    (
                        kernel_rank * pencil_cap * chart_bases
                        + quotient * common_roots,
                        quotient * (k + reserve),
                    ),
                )
            )
            if numerator <= budget * denominator:
                paid_ranks.append(affine_dimension)
        require(paid_ranks, (n, k, reserve, pencil_cap, "no paid rank"))
        paid.append(max(paid_ranks))
    return paid[0], paid[1]


def replay_rows() -> list[dict[str, int | str]]:
    output = []
    for (
        name,
        n,
        rate_denominator,
        scale_denominator,
        expected_agreement,
        expected_grk,
        expected_common_root,
        expected_a1_open,
        expected_a2_open,
    ) in ROWS:
        k = n // rate_denominator
        reserve = n // scale_denominator + 1
        agreement = k + reserve
        radius = n - agreement
        require(agreement == expected_agreement, (name, agreement))

        a1_budget = 8 * n**3
        a2_budget = 16 * n**3
        require(comb(radius + 3, 3) <= a1_budget, (name, "A1 rank three"))
        require(comb(radius + 4, 4) > a1_budget, (name, "A1 bare rank four"))

        rank_four_a2 = comb(radius + 4, 4) <= a2_budget
        a2_open = 5 if rank_four_a2 else 4
        require(a2_open == expected_a2_open, (name, a2_open))

        paid_grk = grk_depth(n, k, reserve)
        require(paid_grk == expected_grk, (name, paid_grk, expected_grk))

        common_root = common_root_paid_rank(n, k, reserve)
        require(
            common_root == (expected_common_root, expected_common_root),
            (name, common_root, expected_common_root),
        )
        a1_open = expected_common_root + 1
        require(a1_open == expected_a1_open, (name, a1_open))

        output.append(
            {
                "name": name,
                "agreement": agreement,
                "reserve": reserve,
                "radius": radius,
                "grk_excess": paid_grk,
                "a1_first_open_rank": a1_open,
                "a2_first_open_rank": a2_open,
            }
        )
    return output


def replay_dag() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    outgoing: dict[str, set[str]] = {}
    for source, target, _ in edges:
        outgoing.setdefault(source, set()).add(target)

    def has_proved_path(source: str) -> bool:
        pending = [source]
        seen = {source}
        while pending:
            current = pending.pop()
            for target in outgoing.get(current, set()):
                if target == NODE:
                    return True
                if target in seen or nodes[target]["status"] != "PROVED":
                    continue
                seen.add(target)
                pending.append(target)
        return False

    require(nodes[NODE]["status"] == "TARGET", nodes[NODE]["status"])
    for parent in PAID_INPUTS:
        require(nodes[parent]["status"] == "PROVED", (parent, nodes[parent]["status"]))
        require(has_proved_path(parent), (parent, NODE, "missing proved path"))

    refs = set(nodes[NODE]["refs"])
    require(
        "critical/nodes/xr_highcore_collision_count/verify.py" in refs,
        "verify.py missing from refs",
    )
    require(
        "critical/nodes/xr_highcore_collision_count/verify_audit.py" in refs,
        "verify_audit.py missing from refs",
    )


def replay_contract() -> None:
    contract = (
        ROOT / "critical/nodes/xr_highcore_collision_count/claim_contract.md"
    ).read_text()
    for marker in (
        "distinct post-strip live slopes",
        "budget A1:** `8n^3`",
        "budget A2:** `16n^3` combined",
        "first open ranks on P-A1 are `5,5,5,17,17,15`",
        "first open P-A2 ranks are `5,4,4,4,4,4`",
        "next theorem A1",
        "next theorem A2",
    ):
        require(marker in contract, marker)


def main() -> None:
    rows = replay_rows()
    replay_dag()
    replay_contract()
    print(
        "XR_HIGHCORE_COLLISION_COUNT_CONTRACT_PASS "
        + " ".join(
            f"{row['name']}:d<={row['grk_excess']},"
            f"A1open={row['a1_first_open_rank']},"
            f"A2open={row['a2_first_open_rank']}"
            for row in rows
        )
        + f" dependencies={len(PAID_INPUTS)} status=TARGET"
    )


if __name__ == "__main__":
    main()
