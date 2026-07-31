#!/usr/bin/env python3
"""Verify the negative paired-product involution gate."""

import itertools
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_negative_paired_product_involution_gate"
P = 29
REPRESENTATIVES = (1, 4, 5, 6, 7, 9, 13)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def determinant(rows: list[list[int]]) -> int:
    return (
        rows[0][0] * (rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1])
        - rows[0][1] * (rows[1][0] * rows[2][2] - rows[1][2] * rows[2][0])
        + rows[0][2] * (rows[1][0] * rows[2][1] - rows[1][1] * rows[2][0])
    ) % P


def paired_products(values: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    a, b, c, d, e, f = values
    return (
        (d * e, d * f), (-d * f, e * f), (-e * f, a * b),
        (a * c, -a * c), (b * c, -b * c), (a * d, b * e),
    )


def rows(values: tuple[int, ...]) -> list[list[int]]:
    return [
        [y * z % P, -(y + z) % P, -1 % P]
        for y, z in paired_products(values)
    ]


def rank_at_most_two(matrix: list[list[int]]) -> bool:
    return all(
        determinant([matrix[i], matrix[j], matrix[k]]) == 0
        for i, j, k in itertools.combinations(range(6), 3)
    )


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("(KBNP-1)" in statement and "a^2+bc != 0" in statement, "gate")
    require("(KBNP-3)" in statement and "every odd field" in statement, "symbolic cut")
    require("necessary, not sufficient" in (NODE / "audit.md").read_text(), "scope")
    require("nonclaim" in contract and "No positive-parity packet" in statement, "nonclaim")
    require("conjugating" in (NODE / "source_evidence.md").read_text(), "source")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    parent = "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler"
    require((parent, NODE_ID, "req") in edges, "dependency")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    tested = survivors = 0
    for values in itertools.permutations(REPRESENTATIVES, 6):
        tested += 1
        survivors += int(rank_at_most_two(rows(values)))
    require((tested, survivors) == (5040, 0), "fixture census")

    witness_rows = rows((1, 4, 6, 9, 7, 5))
    require(determinant(witness_rows[:3]) == 12, "printed minor")
    require("determinant is `12`" in proof, "proof minor")
    u, v = 2, 3
    antisymmetric = [[-u * u % P, 0, -1 % P], [-v * v % P, 0, -1 % P]]
    require((antisymmetric[0][0] - antisymmetric[1][0]) % P != 0, "distinct squares")
    require("D(E+F)!=0" in proof, "fixture contradiction")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_PAIRED_PRODUCT_PASS "
        "tested=5040 survivors=0 witness_minor=12 symbolic_fixture=deleted"
    )


if __name__ == "__main__":
    main()
