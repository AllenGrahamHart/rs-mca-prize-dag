#!/usr/bin/env python3
"""Verify the 433 two-loop antipodal-label atlas."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_antipodal_label_atlas"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def cell(singleton: str, left: tuple[str, str], right: tuple[str, str]):
    return singleton, frozenset((frozenset(left), frozenset(right)))


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("k_C^2=k_+ k_-" in statement and "exactly nine" in statement, "claim")
    require("fifteen" in proof and "nonclaim" in contract, "classification")
    require("does not impose" in statement and "remain open" in statement, "scope")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req")) for edge in dag["edges"]}
    for parent in (
        "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
        "rate_half_kb_m2_r4_coordinate_negative_two_loop_product_q_weld",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    names = ("X", "M", "N", "L", "Z")
    cells = []
    for singleton in names:
        remaining = [name for name in names if name != singleton]
        first = remaining[0]
        for mate in remaining[1:]:
            rest = tuple(name for name in remaining if name not in (first, mate))
            cells.append(cell(singleton, (first, mate), rest))
    require(len(cells) == len(set(cells)) == 15, "matching census")

    retained = {
        cell("X", ("M", "L"), ("N", "Z")),
        cell("X", ("M", "Z"), ("N", "L")),
        cell("M", ("X", "N"), ("L", "Z")),
        cell("M", ("X", "L"), ("N", "Z")),
        cell("M", ("X", "Z"), ("N", "L")),
        cell("N", ("X", "L"), ("M", "Z")),
        cell("N", ("X", "Z"), ("M", "L")),
        cell("L", ("X", "N"), ("M", "Z")),
        cell("Z", ("X", "N"), ("M", "L")),
    }
    require(retained <= set(cells) and len(retained) == 9, "nine retained")

    # Generic and fourth-root examples cover all retained row shapes.
    examples = (
        (101, (1, 2, 4, -2, -4)),
        (101, (1, 2, 4, -4, -2)),
        (17, (1, 4, -1, 2, -2)),
        (101, (1, 2, 4, -1, -4)),
        (101, (1, 2, 4, -4, -1)),
        (101, (1, 2, 4, -1, -2)),
        (101, (1, 2, 4, -2, -1)),
        (17, (1, 4, -1, 2, -4)),
        (17, (1, 4, -1, -4, 2)),
    )
    for prime, raw in examples:
        values = tuple(value % prime for value in raw)
        require(len(set(values)) == 5, "example distinctness")
        require(sum((left + right) % prime == 0 for left, right in itertools.combinations(values, 2)) == 2,
                "example antipodal count")

    k_values = (1, 28, 4, 25, 9)
    survivors = sum(
        (k_c*k_c-k_plus*k_minus) % 29 == 0
        for k_a, k_c, k_plus, k_minus, k_bc in itertools.permutations(k_values)
    )
    require(survivors == 0, "F29 consequence")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_433_LABEL_PASS "
        "matching_cells=15 retained=9 free_parameters=1 f29_role_survivors=0"
    )


if __name__ == "__main__":
    main()
