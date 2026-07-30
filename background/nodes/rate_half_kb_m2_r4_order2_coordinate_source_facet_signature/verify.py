#!/usr/bin/env python3
"""Verify the coordinate-order-two source-facet signature and fixture."""

from collections import Counter
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature"
I = set(range(6))
J = set(range(6, 12))
BAR = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4,
       6: 7, 7: 6, 8: 9, 9: 8, 10: 11, 11: 10}


def edge(a: int, b: int) -> frozenset[int]:
    return frozenset((a, b))


def bar_edge(value: frozenset[int]) -> frozenset[int]:
    return frozenset(BAR[x] for x in value)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("J-J: 10" in statement and "I-I: 10" in statement, "census")
    require("eta=L minus K" in statement and "L=I" in proof, "I/L scope")
    require("abstract route cut" in proof, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (item["from"], item["to"], item.get("kind", "req"))
        for item in dag["edges"]
    }
    require(
        (
            "rate_half_kb_m2_v4_outer_recurrence_router",
            NODE_ID,
            "req",
        ) in edges,
        "router dependency",
    )
    require(
        (
            "rate_half_kb_q6_s6_common_five_outgoing_fiber_pin",
            NODE_ID,
            "req",
        ) in edges,
        "source-facet dependency",
    )
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    k_orbits = [
        (edge(6, 8), edge(7, 9)),
        (edge(6, 10), edge(7, 11)),
        (edge(6, 11), edge(7, 10)),
        (edge(8, 10), edge(9, 11)),
        (edge(8, 11), edge(9, 10)),
    ]
    eta_orbit = (edge(0, 2), edge(1, 3))
    lc_records = [
        {"right": 6, "x": 2, "neighbors": (8, 10),
         "stars": (edge(0, 4), edge(1, 5))},
        {"right": 7, "x": 3, "neighbors": (9, 11),
         "stars": (edge(0, 5), edge(1, 4))},
        {"right": 8, "x": 0, "neighbors": (10, 11),
         "stars": (edge(2, 4), edge(3, 5))},
        {"right": 9, "x": 1, "neighbors": (6, 7),
         "stars": (edge(2, 5), edge(3, 4))},
        {"right": 10, "x": 4, "neighbors": (6, 7),
         "stars": (edge(0, 6), edge(1, 7))},
        {"right": 11, "x": 5, "neighbors": (8, 9),
         "stars": (edge(2, 8), edge(3, 9))},
    ]

    all_orbits = k_orbits + [eta_orbit] + [record["stars"] for record in lc_records]
    for first, second in all_orbits:
        require(bar_edge(first) == second, "bar-equivariant orbit")
    stars = [value for pair in all_orbits for value in pair]
    require(len(stars) == 24 and len(set(stars)) == 24, "simple 24-star graph")

    categories = Counter()
    for value in stars:
        if value <= I:
            categories["II"] += 1
        elif value <= J:
            categories["JJ"] += 1
        else:
            categories["IJ"] += 1
    require(categories == Counter({"II": 10, "JJ": 10, "IJ": 4}), "category census")

    degrees = Counter(vertex for value in stars for vertex in value)
    require([degrees[i] for i in range(12)] == [4] * 12, "source degrees")
    defect = sum(weight * (weight - 1) // 2 for weight in Counter(stars).values())
    require(defect == 0, "defect")

    k_degrees = Counter(vertex for pair in k_orbits for value in pair for vertex in value)
    require(sorted(k_degrees[j] for j in J) == [3, 3, 3, 3, 4, 4],
            "pinned K-degree profile")

    left_degrees = Counter()
    for record in lc_records:
        right = record["right"]
        neighbors = record["neighbors"]
        require(right not in neighbors, "diagonal-free pole graph")
        for neighbor in neighbors:
            left_degrees[neighbor] += 1
        first, second = record["stars"]
        common = I - {record["x"]}
        if first <= I:
            require(first <= common and second <= common, "common-I facet")
        else:
            require(len(first & J) == len(second & J) == 1, "one exchange")
            require(next(iter(first & J)) == neighbors[0], "first exchange")
            require(next(iter(second & J)) == neighbors[1], "second exchange")
            require((first & I) <= common and (second & I) <= common, "exchange facet")
    require([left_degrees[j] for j in J] == [2] * 6, "left pole degrees")
    require({record["x"] for record in lc_records} == I, "facet matching")
    colored_edges = sum(2 for record in lc_records if not record["stars"][0] <= I)
    require(colored_edges == 4, "component color count")

    print(
        "RATE_HALF_KB_M2_R4_ORDER2_COORDINATE_SOURCE_FACET_SIGNATURE_PASS "
        f"categories={dict(categories)} defect={defect} colored={colored_edges}"
    )


if __name__ == "__main__":
    main()
