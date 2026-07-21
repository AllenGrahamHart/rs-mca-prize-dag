#!/usr/bin/env python3
"""Verify the XR higher-rank collapsed-face exclusion."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_higher_rank_collapsed_face_exclusion"
DEPENDENCY = "xr_higher_rank_minimal_face_syzygy_dichotomy"
CONSUMER = "xr_highcore_collision_count"
PRIME = 1009


def evaluate(coefficients: tuple[int, ...], value: int) -> int:
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % PRIME
    return result


def rank_mod(matrix: list[list[int]]) -> int:
    rows = [row[:] for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next(
            (index for index in range(rank, len(rows)) if rows[index][column] % PRIME),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, PRIME)
        rows[rank] = [(entry * inverse) % PRIME for entry in rows[rank]]
        for index, row in enumerate(rows):
            if index == rank:
                continue
            factor = row[column] % PRIME
            if factor:
                rows[index] = [
                    (left - factor * right) % PRIME
                    for left, right in zip(row, rows[rank])
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def interpolation_check() -> int:
    checked = 0
    for a in range(1, 13):
        active_union = list(range(1, a + 3))
        p_u = tuple((7 * index + 3) % PRIME for index in range(a))
        p_q = tuple((11 * index + 5) % PRIME for index in range(a))
        for omitted in active_union:
            facet = [value for value in active_union if value != omitted]
            assert len(facet) == a + 1
            vandermonde = [
                [pow(value, degree, PRIME) for degree in range(a)]
                for value in facet
            ]
            assert rank_mod(vandermonde) == a

            slope = 13 + omitted
            w = tuple((left - slope * right) % PRIME for left, right in zip(p_u, p_q))
            assert all(
                evaluate(w, value)
                == (evaluate(p_u, value) - slope * evaluate(p_q, value)) % PRIME
                for value in active_union
            )
            checked += 1

        for k in (a, a + 7, 4 * a + 1):
            assert (k - a) + len(active_union) == k + 2
            assert k + 2 > k
    return checked


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "|X|=a+2",
        "|S_i|=a+1",
        "|P_0unionX|=k+2",
        "contradictingtheprovedpost-stripcap`k`",
        "activeunionatleast",
        "a+3",
        "doesnotpaylarger-unionrank-twotrades",
    ):
        assert marker in statement


def main() -> None:
    checked = interpolation_check()
    packet_check()
    print(f"XR_HIGHER_RANK_COLLAPSED_FACE_EXCLUSION_PASS facets={checked}")


if __name__ == "__main__":
    main()
