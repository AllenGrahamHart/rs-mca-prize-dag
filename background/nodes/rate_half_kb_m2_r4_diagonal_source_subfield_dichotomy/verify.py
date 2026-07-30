#!/usr/bin/env python3
"""Verify the diagonal source-subfield dichotomy packet."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_source_subfield_dichotomy"
PARENT = "rate_half_kb_m2_r4_diagonal_fiber_resultant_interpolation_compiler"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("Source-line lift" in statement, "lifting branch")
    require("Biquadratic source cover" in statement, "cover branch")
    require("need not fix `F=K(W)` pointwise" in proof, "semilinear catch")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    require((PARENT, NODE_ID, "req") in edges, "dependency")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    positions = [(i, j) for i in range(3) for j in range(5)]
    seen = set()
    pairs = 0
    fixed = 0
    for position in positions:
        if position in seen:
            continue
        mate = (2 - position[0], 4 - position[1])
        orbit = {position, mate}
        seen.update(orbit)
        if len(orbit) == 1:
            fixed += 1
        else:
            pairs += 1
    require((pairs, fixed) == (7, 1), "reciprocal coefficient orbits")
    require((pairs + fixed, pairs) == (8, 7), "eigenspace dimensions")

    passports = []
    for genus in range(4):
        n_eta = 2 * genus + 2
        n_mu = 2 * genus + 6 - 2 * n_eta
        if n_mu >= 0:
            passports.append((genus, n_eta, n_eta, n_mu))
    require(passports == [(0, 2, 2, 2), (1, 4, 4, 0)], "V4 passports")
    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_SOURCE_SUBFIELD_DICHOTOMY_PASS "
        "reciprocal_dims=8,7 passports=2"
    )


if __name__ == "__main__":
    main()
