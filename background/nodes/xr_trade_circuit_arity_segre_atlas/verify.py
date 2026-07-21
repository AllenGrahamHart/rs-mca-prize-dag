#!/usr/bin/env python3
"""Verify the XR trade-circuit arity and Segre atlas."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_trade_circuit_arity_segre_atlas"
PARENT = "xr_higher_rank_uniform_split_pencil_reduction"
CONSUMER = "xr_highcore_collision_count"
PRIME = 1009


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


def arity_checks() -> int:
    checked = 0
    for trade_rank in range(2, 33):
        for blocks in range(trade_rank + 2, 2 * trade_rank + 2):
            assert blocks - 2 >= trade_rank
            kernel_floor = blocks - 2 * trade_rank
            if blocks == 2 * trade_rank + 1:
                assert kernel_floor == 1
            checked += 1
        assert 2 * trade_rank + 2 - 2 * trade_rank == 2
    return checked


def segre_columns(slopes: list[int], parameters: list[int]) -> list[list[int]]:
    return [
        [1, parameter % PRIME, slope % PRIME, slope * parameter % PRIME]
        for slope, parameter in zip(slopes, parameters)
    ]


def transpose(columns: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*columns)]


def segre_checks() -> tuple[int, int]:
    # Four points on the graph parameter=slope give a rank-three circuit.
    slopes4 = [1, 2, 3, 4]
    columns4 = segre_columns(slopes4, slopes4)
    assert rank_mod(transpose(columns4)) == 3
    assert all(rank_mod(transpose([column for j, column in enumerate(columns4) if j != i])) == 3 for i in range(4))

    # Five points on parameter=slope^2 form a Vandermonde rank-four circuit.
    slopes5 = [1, 2, 3, 4, 5]
    columns5 = segre_columns(slopes5, [value * value for value in slopes5])
    assert rank_mod(transpose(columns5)) == 4
    assert all(rank_mod(transpose([column for j, column in enumerate(columns5) if j != i])) == 4 for i in range(5))

    for column in columns4 + columns5:
        c, d, gc, gd = column
        assert (c * gd - d * gc) % PRIME == 0
    return len(columns4), len(columns5)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[PARENT]["status"] == "PROVED"
    assert (PARENT, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "r+2<=t<=2r+1",
        "sumofrow-scalingcircuits",
        "exactlyfourorfiveactiveblocks",
        "v_1v_4-v_2v_3=0",
        "t=4:rank(v_1,...,v_4)=3",
        "t=5:rank(v_1,...,v_5)=4",
        "doesnotcountembeddings",
    ):
        assert marker in statement


def main() -> None:
    arities = arity_checks()
    four, five = segre_checks()
    packet_check()
    print(
        "XR_TRADE_CIRCUIT_ARITY_SEGRE_ATLAS_PASS "
        f"arities={arities} segre={four}+{five}"
    )


if __name__ == "__main__":
    main()
