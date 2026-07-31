#!/usr/bin/env python3
"""Verify the coordinate complete-fiber Vieta compiler."""

import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler"
CERT = ROOT / "background/nodes/rate_half_kb_m2_r4_coordinate_vieta_profile_only_f29_route_cut/certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def rank_mod(rows: list[list[int]], prime: int) -> int:
    matrix = [[value % prime for value in row] for row in rows]
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, prime)
        matrix[pivot_row] = [value * inverse % prime for value in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row:
                continue
            scale = matrix[row][column]
            if scale:
                matrix[row] = [
                    (left - scale * right) % prime
                    for left, right in zip(matrix[row], matrix[pivot_row])
                ]
        pivot_row += 1
    return pivot_row


def determinant_mod(rows: list[list[int]], prime: int) -> int:
    matrix = [[value % prime for value in row] for row in rows]
    determinant = 1
    for column in range(len(matrix)):
        pivot = next(
            (row for row in range(column, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            return 0
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            determinant = -determinant
        value = matrix[column][column]
        determinant = determinant * value % prime
        inverse = pow(value, -1, prime)
        for row in range(column + 1, len(matrix)):
            scale = matrix[row][column] * inverse % prime
            matrix[row] = [
                (left - scale * right) % prime
                for left, right in zip(matrix[row], matrix[column])
            ]
    return determinant % prime


def product_row(kappa: int, edge: list[int], prime: int) -> list[int]:
    product = edge[0] * edge[1] % prime
    return [
        -product % prime,
        -product * kappa % prime,
        -product * kappa * kappa % prime,
        1,
        kappa % prime,
        kappa * kappa % prime,
    ]


def skeleton_census(degrees: tuple[int, int, int]) -> set[tuple[int, ...]]:
    rows = set()
    for l0 in range(3):
        for l1 in range(3):
            for l2 in range(3):
                for m01 in range(5):
                    for m02 in range(5):
                        for m12 in range(5):
                            value = (l0, l1, l2, m01, m02, m12)
                            if sum(value) != 5:
                                continue
                            actual = (
                                2 * l0 + m01 + m02,
                                2 * l1 + m01 + m12,
                                2 * l2 + m02 + m12,
                            )
                            if actual != degrees:
                                continue
                            if degrees == (4, 4, 2):
                                swapped = (l1, l0, l2, m01, m12, m02)
                            else:
                                swapped = (l0, l2, l1, m02, m01, m12)
                            rows.add(min(value, swapped))
    return rows


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("24 x 8" in statement and "24 x 7" in statement, "complete systems")
    require("det M_+(K union {eta})=0" in statement, "separator")
    require("(KBCV-6)" in statement and "exactly seven" in statement, "negative cut")
    require("Leading support" in (NODE / "audit.md").read_text(), "support audit")
    require("does not prove" in statement and "nonclaim" in contract, "scope")
    require("direct Vieta calculation" in (NODE / "source_evidence.md").read_text(), "source")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {
        (edge["from"], edge["to"], edge.get("kind", "req"))
        for edge in dag["edges"]
    }
    for parent in (
        "rate_half_kb_m2_v4_outer_recurrence_router",
        "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
        "rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler",
    ):
        require((parent, NODE_ID, "req") in edges, f"dependency {parent}")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    expected = {
        (0, 1, 0, 2, 2, 0),
        (1, 1, 0, 1, 1, 1),
        (1, 1, 1, 2, 0, 0),
        (0, 0, 0, 2, 2, 1),
        (1, 0, 0, 1, 1, 2),
        (1, 0, 1, 2, 0, 1),
        (1, 1, 1, 1, 1, 0),
    }
    profile_442 = skeleton_census((4, 4, 2))
    profile_433 = skeleton_census((4, 3, 3))
    require(len(profile_442) == len(profile_433) == 7, "raw skeleton census")
    injective = {
        value
        for value in profile_442 | profile_433
        if max(value[:3]) <= 1 and max(value[3:]) <= 2
    }
    require(injective == expected, "injective skeleton census")

    certificate = json.loads(CERT.read_text())
    prime = certificate["field"]
    records = list(zip(
        certificate["K"],
        [orbit[0] for orbit in certificate["k_orbits"]],
    ))
    records.append((certificate["xi"], certificate["eta_orbit"][0]))
    records.extend(
        (record["right"], record["stars"][0])
        for record in certificate["right_records"]
    )
    rows = [product_row(kappa, edge, prime) for kappa, edge in records]
    require(len(rows) == 12, "complete fiber count")
    require(rank_mod(rows[:5], prime) == 5, "K rank")
    require(rank_mod(rows[:6], prime) == 6, "K+eta rank")
    require(determinant_mod(rows[:6], prime) == 10, "separator determinant")
    require("products on `K union {eta}`" in proof, "regression proof")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_COMPLETE_FIBER_VIETA_PASS "
        "fibers=12 k_rank=5 k_eta_rank=6 determinant=10 negative_skeletons=7"
    )


if __name__ == "__main__":
    main()
