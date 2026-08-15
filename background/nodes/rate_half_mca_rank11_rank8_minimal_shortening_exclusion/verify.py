#!/usr/bin/env python3
"""Verify the K'=10 rank-eight minimal-shortening exclusion."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "d03271ea09234ab73dad72b6509a136b07427a479bba822c7db55adf8c4c868e"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    rows = [row[:] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column] % prime), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        for i, row in enumerate(rows):
            if i == rank:
                continue
            factor = row[column] % prime
            if factor:
                rows[i] = [
                    (left - factor * right) % prime
                    for left, right in zip(row, rows[rank])
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-rank8-minimal-shortening-exclusion-v1",
        "schema",
    )
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_dense_root_highspan_saturation",
        "rate_half_mca_rank11_component_ninesubset_target_router",
        "rate_half_mca_rank11_rank8_fixed_chart_local_cap_fence",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(
        p["residual_dimension"]
        == p["ambient_rs_dimension"]
        == p["correction_space_dimension"]
        == 10,
        "dimension equality",
    )
    require(p["selector_size"] == p["selector_rank"] == 9, "selector rank")
    require(p["excluded_selector_rank"] == 8, "excluded rank")
    require(p["interpolation_degree_ceiling"] + 1 == p["selector_size"], "interpolation")
    require(
        p["first_uncovered_residual_dimension"] == p["residual_dimension"] + 1 == 11,
        "adjacent row",
    )
    require(
        p["adjacent_row_fixed_chart_fence"]
        == "rate_half_mca_rank11_rank8_fixed_chart_local_cap_fence",
        "adjacent fence",
    )
    require("impossible at K'=10" in str(data.get("claim")), "claim")
    require("K'>=11" in str(data.get("nonclaim")), "nonclaim")

    prime = 101
    points = list(range(1, 10))
    vandermonde = [[pow(point, degree, prime) for degree in range(9)] for point in points]
    toy_rank = rank_mod(vandermonde, prime)
    require(toy_rank == 9, "finite-field Vandermonde rank")
    return {"toy_prime": prime, "toy_rank": toy_rank}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("residual_dimension", 11),
        lambda item: item["parameters"].__setitem__("correction_space_dimension", 9),
        lambda item: item["parameters"].__setitem__("selector_rank", 8),
        lambda item: item["parameters"].__setitem__("interpolation_degree_ceiling", 9),
        lambda item: item["parameters"].__setitem__("first_uncovered_residual_dimension", 12),
        lambda item: item["parameters"].__setitem__("adjacent_row_fixed_chart_fence", "unassigned"),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_RANK8_MINIMAL_SHORTENING_EXCLUSION_PASS "
        f"toy=GF({result['toy_prime']}) rank={result['toy_rank']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
