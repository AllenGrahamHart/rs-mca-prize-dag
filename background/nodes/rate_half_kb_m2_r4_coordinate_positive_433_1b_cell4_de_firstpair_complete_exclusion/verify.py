#!/usr/bin/env python3
"""Verify the positive 433-1b cell-4 DE first-pair block."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = NODE.name
PARENTS = (
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi0_pairing0_four_basis_exclusion",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi1_pairing0_parallel_edge_transport",
    "rate_half_kb_m2_r4_coordinate_positive_433_1b_cell4_xi2_pairing0_four_basis_exclusion",
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, second),) + tail


def verify_combinatorics():
    matchings = tuple(pairings(range(6)))
    require(len(matchings) == len(set(matchings)) == 15,
            "fifteen canonical matchings")
    expected_first = (
        ((0, 1), (2, 3), (4, 5)),
        ((0, 1), (2, 4), (3, 5)),
        ((0, 1), (2, 5), (3, 4)),
    )
    require(matchings[:3] == expected_first, "first-pair matching block")
    require(all(matching[0] == (0, 1) for matching in matchings[:3]) and
            all(matching[0] != (0, 1) for matching in matchings[3:]),
            "exact first-pair orbit")
    records = {
        0: ("DE", "-DE", "DF", "soEF", "BF", "scCF"),
        1: ("DE", "-DE", "DF", "soEF", "BF", "scCF"),
        2: ("DE", "DE", "DF", "soEF", "BF", "scCF"),
    }
    require(records[0] == records[1], "parallel positive-copy transport")
    require({tuple(records[xi][index] for index in matching[0])
             for xi in (0, 1) for matching in matchings[:3]} ==
            {("DE", "-DE")}, "opposite-DE first pair")
    require({tuple(records[2][index] for index in matching[0])
             for matching in matchings[:3]} == {("DE", "DE")},
            "equal-DE first pair")
    require(3*3*len(tuple(itertools.product((-1, 1), repeat=2)))*4 == 144,
            "raw Cartesian count")


def verify_parents():
    for parent in PARENTS:
        payload = json.loads((ROOT / "background/nodes" / parent /
                              "node.json").read_text())
        require(payload["node"]["status"] == "PROVED", f"proved {parent}")
    xi0 = (ROOT / "background/nodes" / PARENTS[0] / "proof.md").read_text()
    xi1 = (ROOT / "background/nodes" / PARENTS[1] / "proof.md").read_text()
    xi2 = (ROOT / "background/nodes" / PARENTS[2] / "proof.md").read_text()
    require("P(m,-m)=0" in xi0 and "positions `0` and `1`" in xi1 and
            "P(-m,-m)=0" in xi2, "parent cut custody")


def verify_dag():
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    require(NODE_ID in nodes and nodes[NODE_ID]["status"] == "PROVED",
            "DAG node")
    edges = {(row["from"], row["to"], row["kind"]) for row in dag["edges"]}
    for parent in PARENTS:
        require((parent, NODE_ID, "req") in edges, f"DAG parent {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges,
            "DAG consumer")


def verify_documents():
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    require("3*3*4*4=144" in proof and "leaves\n`96`" in statement,
            "count and frontier")
    require("P(-m,-m)" in proof and "necessary first-pair equation" in audit,
            "sound transport scope")
    require("`xi=3,...,6`" in statement and "`pairing=3,...,14`" in statement,
            "nonclaim fence")


def main():
    verify_combinatorics()
    verify_parents()
    verify_dag()
    verify_documents()
    print("cell=4 de_first_pair slices=9 raw_cases=144 paid=9/105 remaining=96")


if __name__ == "__main__":
    main()
