#!/usr/bin/env python3
"""Verify the one-loop 442 complete-edge skeleton classifier."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_edge_skeleton_classifier"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def permute(solution, permutation):
    colored, loops, internal = solution
    colored_new = tuple(colored[permutation[index]] for index in range(3))
    loops_new = tuple(loops[permutation[index]] for index in range(3))
    edge = {(0, 1): internal[0], (0, 2): internal[1],
            (1, 2): internal[2]}

    def old_edge(left, right):
        return edge[tuple(sorted((left, right)))]

    internal_new = (
        old_edge(permutation[0], permutation[1]),
        old_edge(permutation[0], permutation[2]),
        old_edge(permutation[1], permutation[2]),
    )
    return colored_new, loops_new, internal_new


def main():
    statement = (NODE / "statement.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("S0:" in statement and "S1:" in statement and "S2:" in statement,
            "claim")
    require("does not choose" in statement and "nonclaim" in contract, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
        "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
        "rate_half_kb_m2_r4_coordinate_negative_loop_budget_gate",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    solutions = []
    for colored in itertools.product(range(3), repeat=3):
        if sum(colored) != 2:
            continue
        for loops in itertools.product(range(2), repeat=3):
            if sum(loops) > 1:
                continue
            for internal in itertools.product(range(3), repeat=3):
                if sum(loops)+sum(internal) != 5:
                    continue
                m_de, m_df, m_ef = internal
                degrees = (
                    2*loops[0]+m_de+m_df,
                    2*loops[1]+m_de+m_ef,
                    2*loops[2]+m_df+m_ef,
                )
                if all(degrees[index] == 4-colored[index]
                       for index in range(3)):
                    solutions.append((colored, loops, internal))
    require(len(solutions) == 12, "ordered census")

    remaining = set(solutions)
    orbits = []
    while remaining:
        representative = next(iter(remaining))
        orbit = {
            permute(representative, permutation)
            for permutation in itertools.permutations(range(3))
        } & set(solutions)
        orbits.append(orbit)
        remaining -= orbit
    require(sorted(len(orbit) for orbit in orbits) == [3, 3, 6], "orbit sizes")
    canonical = {
        ((0, 1, 1), (0, 0, 0), (2, 2, 1)),
        ((0, 1, 1), (1, 0, 0), (1, 1, 2)),
        ((2, 0, 0), (0, 1, 0), (0, 2, 2)),
    }
    require(all(any(representative in orbit for representative in canonical)
                for orbit in orbits), "canonical representatives")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_SKELETON_PASS "
        "ordered=12 orbit_types=3 loops=0,1"
    )


if __name__ == "__main__":
    main()
