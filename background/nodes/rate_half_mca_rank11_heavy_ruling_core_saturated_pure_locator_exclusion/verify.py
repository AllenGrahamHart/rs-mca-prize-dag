#!/usr/bin/env python3
"""Verify the core-saturated pure-locator exclusion."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "1fd80f10d27b398d80c5636f4869ba58b71c18a46b935391af678d891ab2f1ca"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def matrix_rank(matrix: list[list[int]], p: int) -> int:
    rows = [row[:] for row in matrix]
    rank = 0
    width = len(rows[0]) if rows else 0
    for column in range(width):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column] % p), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, p)
        rows[rank] = [(value * inverse) % p for value in rows[rank]]
        for i, row in enumerate(rows):
            if i == rank:
                continue
            factor = row[column] % p
            if factor:
                rows[i] = [
                    (value - factor * pivot_value) % p
                    for value, pivot_value in zip(row, rows[rank])
                ]
        rank += 1
        if rank == len(rows) or rank == width:
            break
    return rank


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-heavy-ruling-core-saturated-pure-locator-exclusion-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank11_heavy_plane_ruling_degree24_order32_seed",
            "rate_half_mca_rank11_heavy_plane_ruling_degree24_partial_relative_router",
        ],
        "dependencies",
    )
    row = data.get("official")
    require(isinstance(row, dict), "official")
    dimension, agreement = row.get("K"), row.get("m")
    require((dimension, agreement) == (1048576, 1116048), "row")
    excess = agreement - dimension
    margin = row.get("pair_core_margin")
    require(excess == row.get("agreement_excess") == 67472, "excess")
    require(margin == 11, "margin")
    require(
        (
            row.get("seed_size"),
            row.get("minimum_anchor_records"),
            row.get("minimum_selected_pair_types"),
            row.get("minimum_records_per_selected_pair"),
        )
        == (32, 24, 2, 2),
        "packet",
    )
    require(row.get("common_support_maximum") == dimension - 3, "common core")
    require(row.get("minimum_residual_dimension") == 3, "residual dimension")
    require(row.get("residual_pair_core_intersection_offset") == 1, "intersection offset")
    surplus = excess - (2 * margin - 1)
    require(surplus == row.get("core_union_surplus_over_locator_degree") == 67451, "surplus")
    require(row.get("denominator_degree_maximum") == excess, "denominator")
    require(row.get("complexity_threshold") == 3 * agreement - dimension + 3 == 2299571, "complexity")

    samples = data.get("residual_samples")
    require(isinstance(samples, list) and len(samples) == 4, "samples")
    for sample in samples:
        require(isinstance(sample, dict), "sample")
        c = sample.get("c")
        require(isinstance(c, int) and 0 <= c <= dimension - 3, "sample core")
        kp, mp = dimension - c, agreement - c
        core = mp - margin
        union = 2 * core - (kp - 1)
        require(
            sample
            == {
                "c": c,
                "K_residual": kp,
                "m_residual": mp,
                "core_minimum": core,
                "two_core_union_minimum": union,
            },
            "sample arithmetic",
        )
        require(union == mp + surplus > mp, "strict root surplus")

    toy = data.get("toy")
    require(isinstance(toy, dict), "toy")
    p = toy.get("field")
    core0, core1 = toy.get("core_0"), toy.get("core_1")
    require((p, toy.get("K_residual"), toy.get("m_residual")) == (17, 4, 7), "toy row")
    require(toy.get("pair_core_margin") == 1, "toy margin")
    require(isinstance(core0, list) and isinstance(core1, list), "toy cores")
    require(len(core0) == len(core1) == 6, "toy core sizes")
    require(len(set(core0) & set(core1)) == 3, "toy intersection")
    union = sorted(set(core0) | set(core1))
    require(len(union) == toy.get("expected_union_size") == 9, "toy union")
    degree = toy.get("locator_degree_maximum")
    vandermonde = [[pow(x, j, p) for j in range(degree + 1)] for x in union]
    rank = matrix_rank(vandermonde, p)
    require(rank == toy.get("expected_vandermonde_rank") == degree + 1 == 8, "toy rank")
    require("remain unpaid" in str(data.get("nonclaim")), "nonclaim")
    return {"surplus": surplus, "rank": rank, "samples": len(samples)}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item["official"].__setitem__("pair_core_margin", 12),
        lambda item: item["official"].__setitem__("minimum_selected_pair_types", 1),
        lambda item: item["official"].__setitem__("minimum_records_per_selected_pair", 1),
        lambda item: item["official"].__setitem__("common_support_maximum", 1048574),
        lambda item: item["official"].__setitem__("minimum_residual_dimension", 2),
        lambda item: item["official"].__setitem__("core_union_surplus_over_locator_degree", 67450),
        lambda item: item["official"].__setitem__("complexity_threshold", 2299570),
        lambda item: item["residual_samples"][3].__setitem__("two_core_union_minimum", 134925),
        lambda item: item["toy"].__setitem__("core_1", [2, 3, 4, 5, 6, 7]),
        lambda item: item["toy"].__setitem__("expected_vandermonde_rank", 7),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    if args.tamper_selftest:
        caught = tamper_selftest(data)
        print(f"RANK11_CORE_SATURATED_PURE_LOCATOR_TAMPER_PASS mutations={caught}/10")
        return
    print(
        "RANK11_CORE_SATURATED_PURE_LOCATOR_PASS "
        f"surplus={result['surplus']} toy_rank={result['rank']} "
        f"stairs={result['samples']}"
    )


if __name__ == "__main__":
    main()
