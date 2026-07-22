#!/usr/bin/env python3
"""Verify the XR rank-two Maxwell collision-defect identity."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_rank_two_maxwell_collision_defect_identity"
PARENTS = {
    "xr_higher_rank_rank_two_shell_maxwell_router",
    "xr_rank_two_extension_family_collision_ledger",
}
CONSUMER = "xr_highcore_collision_count"


def profile_check(
    a: int, d: int, h: int, zero_sizes: list[int]
) -> tuple[int, int]:
    t = len(zero_sizes)
    rho = a + d + 1
    active_union = set(range(rho))
    zero_sets = []
    cursor = 0
    for size in zero_sizes:
        zero_sets.append(set(range(cursor, cursor + size)))
        cursor += size
    assert cursor <= rho
    supports = [active_union - zero_set for zero_set in zero_sets]
    outside_domain = set(range(rho, rho + 4))
    taus = [h - d - 1 + size for size in zero_sizes]
    assert all(tau >= 0 for tau in taus)
    choices = [
        [set(choice) for choice in itertools.combinations(sorted(zero_set | outside_domain), tau)]
        for zero_set, tau in zip(zero_sets, taus)
    ]

    checked = 0
    zero_baseline = 0
    for extensions in itertools.product(*choices):
        inside = [extension & zero_set for extension, zero_set in zip(extensions, zero_sets)]
        outer = [extension - active_union for extension in extensions]
        pair_residuals = []
        compatible = True
        for i in range(t):
            for j in range(i + 1, t):
                ell = zero_sizes[i] + zero_sizes[j] - d - 1
                consumed = len(inside[i]) + len(inside[j]) + len(outer[i] & outer[j])
                if consumed > ell:
                    compatible = False
                    break
                pair_residuals.append(ell - consumed)
            if not compatible:
                break
        if not compatible:
            continue

        multiplicities = {
            point: sum(point in outer_set for outer_set in outer)
            for point in outside_domain
        }
        total_inside = sum(map(len, inside))
        sigma = sum(pair_residuals)
        higher = sum(
            (count - 1) * (count - 2) // 2
            for count in multiplicities.values()
            if count >= 1
        )
        z_total = sum(zero_sizes)
        baseline = (
            2 * (d + 1)
            + t * (h - 2 * d - 2)
            + (d + 1) * t * (t - 1)
            - 2 * (t - 2) * z_total
        )
        factored = t * h + (t - 2) * ((t - 1) * (d + 1) - 2 * z_total)
        assert baseline == factored

        blocks = [support | extension for support, extension in zip(supports, extensions)]
        union = set().union(*blocks)
        deficit = 2 * len(union) - 2 * a - h * t
        predicted = baseline + 2 * ((t - 2) * total_inside + sigma + higher)
        assert deficit == predicted
        checked += 1

        if baseline == 0:
            zero_baseline += 1
            if deficit <= 0:
                assert total_inside == sigma == higher == 0
                assert all(count <= 2 for count in multiplicities.values())
    assert checked > 0
    return checked, zero_baseline


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "H=sum_(xoutsideX,m_x>=1)C(m_x-1,2)",
        "sigma=sum_(i<j)(ell_ij-|I_i|-|I_j|-|O_iintersectO_j|)",
        "D_0=2(d+1)+t(h-2d-2)",
        "=th+(t-2)((t-1)(d+1)-2Z)",
        "Delta=D_0+2((t-2)I+sigma+H)",
        "<=floor(-D_0/2)",
        "everypairbudget(EC4)issaturated",
        "m_x<=2foreveryxoutsideX",
        "sharpenseverynonpositive-baselineshell",
    ):
        assert marker in statement


def main() -> None:
    profiles = [
        (4, 3, 2, [2, 2, 2, 2]),
        (4, 2, 3, [1, 2, 2, 2]),
        (4, 3, 3, [2, 2, 2, 2]),
        (6, 4, 3, [2, 3, 3, 3]),
    ]
    results = [profile_check(*profile) for profile in profiles]
    assert sum(zero for _, zero in results) > 0
    packet_check()
    print(
        "XR_RANK_TWO_MAXWELL_COLLISION_DEFECT_IDENTITY_PASS "
        f"profiles={len(results)} compatible={sum(count for count, _ in results)} "
        f"zero_baseline={sum(zero for _, zero in results)}"
    )


if __name__ == "__main__":
    main()
