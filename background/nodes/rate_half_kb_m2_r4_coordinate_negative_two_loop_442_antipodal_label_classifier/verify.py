#!/usr/bin/env python3
"""Verify the 442 two-loop antipodal-label classifier."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_antipodal_label_classifier"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("k_B^2=k_AB k_AC" in statement and "k_A^2=k_AB k_BC" in statement, "label gate")
    require("exactly three" in statement and "fifteen" in proof, "classification")
    require("nonclaim" in contract and "does not delete" in statement, "scope")

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

    # The fifteen singleton/perfect-matching cells are combinatorially exact.
    names = ("X", "L", "M", "Y", "Z")
    cells = []
    for singleton in names:
        remaining = [name for name in names if name != singleton]
        first = remaining[0]
        for mate in remaining[1:]:
            rest = tuple(name for name in remaining if name not in (first, mate))
            cells.append((singleton, frozenset((frozenset((first, mate)), frozenset(rest)))))
    require(len(cells) == len(set(cells)) == 15, "matching census")
    retained = {
        ("X", frozenset((frozenset(("L", "Y")), frozenset(("M", "Z"))))),
        ("L", frozenset((frozenset(("X", "Y")), frozenset(("M", "Z"))))),
        ("M", frozenset((frozenset(("X", "Z")), frozenset(("L", "Y"))))),
    }
    require(retained <= set(cells) and len(retained) == 3, "three retained cells")

    # Exact witnesses show that each retained algebraic cell is nonvacuous.
    examples = (
        (13, 4, 10),  # l^3=-1, m=-l^2
        (17, 2, 13),  # l^4=-1, m=-l^2
        (17, 13, 2),  # m^4=-1, l=-m^2
    )
    for prime, ell, em in examples:
        values = (1, ell, em, em * em % prime, ell * ell % prime)
        require(len(set(values)) == 5, "retained distinctness")
        opposites = sum(
            1 for left, right in itertools.combinations(values, 2)
            if (left + right) % prime == 0
        )
        require(opposites == 2, "retained antipodal count")

    # The banked F_29 K-set has no role assignment satisfying both gates.
    k_values = (1, 28, 4, 25, 9)
    survivors = 0
    for k_a, k_b, k_ab, k_ac, k_bc in itertools.permutations(k_values):
        survivors += int(
            (k_b * k_b - k_ab * k_ac) % 29 == 0
            and (k_a * k_a - k_ab * k_bc) % 29 == 0
        )
    require(survivors == 0, "F29 consequence")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_442_LABEL_PASS "
        "matching_cells=15 retained=3 roots=6,8,8 f29_role_survivors=0"
    )


if __name__ == "__main__":
    main()
