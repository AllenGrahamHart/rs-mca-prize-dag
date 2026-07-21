#!/usr/bin/env python3
"""Verify the XR rank-two extension-family collision ledger."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_rank_two_extension_family_collision_ledger"
PARENTS = {
    "xr_higher_rank_rank_two_shell_maxwell_router",
    "xr_rank_two_actual_block_extension_router",
}
CONSUMER = "xr_highcore_collision_count"


def profile_check(
    a: int, d: int, h: int, zero_sizes: list[int]
) -> tuple[int, int, int]:
    rho = a + d + 1
    assert sum(zero_sizes) <= rho
    active_union = set(range(rho))
    zero_sets = []
    cursor = 0
    for size in zero_sizes:
        zero_set = set(range(cursor, cursor + size))
        zero_sets.append(zero_set)
        cursor += size
    supports = [active_union - zero_set for zero_set in zero_sets]
    outside = set(range(rho, rho + 4))
    taus = [h - d - 1 + size for size in zero_sizes]
    assert all(tau >= 0 for tau in taus)

    choices = [
        [set(choice) for choice in itertools.combinations(sorted(zero_set | outside), tau)]
        for zero_set, tau in zip(zero_sets, taus)
    ]
    total = math.prod(len(row_choices) for row_choices in choices)
    compatible = 0
    zero_slack_edges = 0
    for extensions in itertools.product(*choices):
        blocks = [support | extension for support, extension in zip(supports, extensions)]
        inside = [extension & zero_set for extension, zero_set in zip(extensions, zero_sets)]
        outer = [extension - active_union for extension in extensions]
        pair_ledgers = []
        cap_checks = []
        for i in range(len(zero_sizes)):
            for j in range(i + 1, len(zero_sizes)):
                ell = zero_sizes[i] + zero_sizes[j] - d - 1
                assert ell >= 0
                actual = len(blocks[i] & blocks[j])
                formula = (
                    a + d + 1 - zero_sizes[i] - zero_sizes[j]
                    + len(inside[i])
                    + len(inside[j])
                    + len(outer[i] & outer[j])
                )
                assert actual == formula
                ledger = len(inside[i]) + len(inside[j]) + len(outer[i] & outer[j]) <= ell
                cap = actual <= a
                assert ledger == cap
                pair_ledgers.append(ledger)
                cap_checks.append(cap)
                if ell == 0:
                    zero_slack_edges += 1
                    if ledger:
                        assert not inside[i] and not inside[j]
                        assert not (outer[i] & outer[j])

        family_ok = all(pair_ledgers)
        assert family_ok == all(cap_checks)
        if family_ok:
            compatible += 1
            multiplicities = {
                point: sum(point in outer_set for outer_set in outer)
                for point in outside
            }
            left = (len(zero_sizes) - 1) * sum(map(len, inside)) + sum(
                count * (count - 1) // 2 for count in multiplicities.values()
            )
            right = (len(zero_sizes) - 1) * sum(zero_sizes) - math.comb(
                len(zero_sizes), 2
            ) * (d + 1)
            assert left <= right
    assert total > 0 and compatible > 0
    return total, compatible, zero_slack_edges


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
        "I_i=T_iintersectZ_i",
        "O_i=T_i\\X",
        "a+d+1-z_i-z_j+|I_i|+|I_j|+|O_iintersectO_j|",
        "ell_ij=z_i+z_j-d-1",
        "bothinsidereusesetsareempty",
        "(t-1)sum_i|I_i|+sum_(xoutsideX)C(m_x,2)",
        "(t-1)Z-C(t,2)(d+1)",
        "completefiniteextension-familycompatibilityledger",
        "doesnotenumeratecoefficient-compatiblesupports",
    ):
        assert marker in statement


def main() -> None:
    profiles = [
        (4, 2, 3, [1, 2, 2, 2]),
        (4, 3, 3, [2, 2, 2, 2]),
        (6, 4, 3, [2, 3, 3, 3]),
    ]
    results = [profile_check(*profile) for profile in profiles]
    packet_check()
    print(
        "XR_RANK_TWO_EXTENSION_FAMILY_COLLISION_LEDGER_PASS "
        f"profiles={len(results)} families={sum(total for total, _, _ in results)} "
        f"compatible={sum(good for _, good, _ in results)}"
    )


if __name__ == "__main__":
    main()
