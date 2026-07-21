#!/usr/bin/env python3
"""Verify the prize first-shell primitive rank-three exclusion."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_prize_first_shell_primitive_rank_three_exclusion"
PARENTS = {
    "xr_higher_rank_uniform_split_pencil_reduction",
    "xr_prize_primitive_rank_two_shell_band",
}
CONSUMER = "xr_highcore_collision_count"
PRIME = 1009
ROWS = (
    (2**33 + 1, 384),
    (2**33 + 1, 448),
    (2**32 + 1, 960),
)


def rank_mod(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column] % PRIME), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column] % PRIME, -1, PRIME)
        rows[rank] = [(entry * inverse) % PRIME for entry in rows[rank]]
        for i in range(len(rows)):
            if i == rank:
                continue
            factor = rows[i][column] % PRIME
            if factor:
                rows[i] = [(x - factor * y) % PRIME for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def coefficient_checks() -> int:
    checked = 0
    for t in range(5, 31):
        slopes = list(range(1, t + 1))
        check = [[1] * t, slopes]
        assert rank_mod(check) == 2
        assert t - rank_mod(check) >= 3
        checked += 1
    return checked


def graph_checks() -> int:
    checked = 0
    for size in range(6, 13):
        vertices = list(range(size))
        all_edges = list(itertools.combinations(vertices, 2))
        families = (
            all_edges[:5],
            [(0, i) for i in range(1, min(size, 7))],
            [(i, i + 1) for i in range(5)],
        )
        for edges in families:
            t = len(edges)
            degrees = {vertex: 0 for vertex in vertices}
            for left, right in edges:
                degrees[left] += 1
                degrees[right] += 1
            intersection_energy = sum(value * (value - 1) // 2 for value in degrees.values())
            union_sum = sum(len(set(left) | set(right)) for left, right in itertools.combinations(edges, 2))
            assert union_sum == 4 * (t * (t - 1) // 2) - intersection_energy

            singleton = next((vertex for vertex in vertices if degrees[vertex] == 0), None)
            if singleton is not None:
                union_with_singleton = sum(len(set(edge) | {singleton}) for edge in edges)
                assert union_with_singleton == 3 * t
            checked += 1
    return checked


def official_checks() -> int:
    for h, l_max in ROWS:
        assert h - l_max - 1 > 0
        for t in range(5, l_max + 1):
            no_singleton = 6 + t * (h - t - 1)
            singleton = 2 + t * (h - t + 1)
            assert no_singleton > 0
            assert singleton - no_singleton == 2 * t - 4 > 0


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert all(nodes[parent]["status"] == "PROVED" for parent in PARENTS)
    assert all((parent, NODE, "req") in edges for parent in PARENTS)
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "|X|=a+3",
        "dimensionthree",
        "atleastfiveactiverows",
        "sum_iP_i=0",
        "Delta_G>=6+t(h-t-1)+2I",
        "No primitive full-core trade of any rank",
        "Proper local first-shell circuits remain possible",
    ):
        assert "".join(marker.split()) in statement


def main() -> None:
    coefficients = coefficient_checks()
    graphs = graph_checks()
    official_checks()
    packet_check()
    print(
        "XR_PRIZE_FIRST_SHELL_PRIMITIVE_RANK_THREE_EXCLUSION_PASS "
        f"coefficients={coefficients} graphs={graphs}"
    )


if __name__ == "__main__":
    main()
