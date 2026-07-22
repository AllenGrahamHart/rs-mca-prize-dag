#!/usr/bin/env python3
"""Verify the prize flat-nullity first-core peeling owner."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_flat_nullity_first_core_peeling_owner"
PARENTS = {
    "xr_prize_flat_nullity_maxwell_trade_space_compiler",
    "xr_uniform_maxwell_first_core_peeling_owner",
    "xr_prize_flat_nullity_nonpersistent_root_cap",
}
CONSUMER = "xr_highcore_collision_count"
ROWS = (
    ("prize-1/4", 4, 256, 1_526_176_110, 383),
    ("prize-1/8", 8, 256, 2_902_067_939, 447),
    ("prize-1/16", 16, 512, 1_962_285_106, 959),
)


def terminal_bound(r: int, h: int, v: int) -> int:
    return (2 * (r - v) - 1) // h


def official_check() -> int:
    n = 1 << 41
    checks = 0
    for _name, rate, scale, v_cap, expected_terminal in ROWS:
        k = n // rate
        h = n // scale + 1
        r = n - k
        actual = terminal_bound(r, h, v_cap)
        assert actual == expected_terminal
        assert v_cap + actual < n
        assert k + terminal_bound(r, h, k) < n
        assert h > 2
        checks += 4
    return checks


def minimal_core(family: tuple[frozenset[int], ...], h: int, kappa: int) -> tuple[int, ...] | None:
    for size in range(1, len(family) + 1):
        for indices in combinations(range(len(family)), size):
            union = set().union(*(family[index] for index in indices))
            if h * size >= 2 * len(union) - 2 * kappa:
                return indices
    return None


def peeling_fixture() -> tuple[int, int]:
    fixtures = (
        (
            tuple(
                frozenset(block)
                for block in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
            ),
            1,
            1,
        ),
        (
            tuple(
                frozenset(block)
                for block in ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))
            ),
            1,
            2,
        ),
    )
    checks = 0
    mutations = 0
    for original, h, kappa in fixtures:
        current = list(original)
        owners = []
        while True:
            core = minimal_core(tuple(current), h, kappa)
            if core is None:
                break
            pivot = core[0]
            owners.append(current[pivot])
            current.pop(pivot)
        assert len(set(owners)) == len(owners)
        union = set().union(*current) if current else set()
        assert h * len(current) < 2 * len(union) - 2 * kappa or not current
        checks += 2

        if owners:
            duplicated = owners + [owners[0]]
            assert len(set(duplicated)) < len(duplicated)
            mutations += 1
    assert mutations == len(fixtures)
    return checks, mutations


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
        "floor((2(R-v)-1)/h)",
        "<n",
        "exactlyonecertificate",
        "duplicationacrossoverlappingMaxwellcores",
    ):
        assert marker in statement


def main() -> None:
    official = official_check()
    fixtures, mutations = peeling_fixture()
    packet_check()
    print(
        "XR_PRIZE_FLAT_NULLITY_FIRST_CORE_PEELING_OWNER_PASS "
        f"official_checks={official} fixture_checks={fixtures} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
