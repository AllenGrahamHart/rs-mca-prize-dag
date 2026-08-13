#!/usr/bin/env python3
"""Verify finite controls for the full-explanation lifted-rank dichotomy."""

from __future__ import annotations

import copy
import hashlib
import json
from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "7783651affbb6846c5258b6b1b3f1b9f59627a936afafce71cdb62667750c718"


class Reject(ValueError):
    pass


def matrix_rank(rows: list[tuple[int, ...]], p: int) -> int:
    work = [[value % p for value in row] for row in rows]
    rank = 0
    for column in range(len(work[0]) if work else 0):
        pivot = next(
            (index for index in range(rank, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][column], -1, p)
        work[rank] = [(value * inverse) % p for value in work[rank]]
        for index, row in enumerate(work):
            if index == rank or not row[column]:
                continue
            scale = row[column]
            work[index] = [
                (value - scale * basis) % p
                for value, basis in zip(row, work[rank])
            ]
        rank += 1
    return rank


def inspect_case(
    points: list[tuple[int, tuple[int, ...]]], p: int, dimension: int
) -> dict[str, int]:
    explanation_rank = matrix_rank([word for _, word in points], p)
    lifted_rank = matrix_rank([(slope, *word) for slope, word in points], p)
    gauge_counts: dict[int, int] = {}
    for gauge in product(range(p), repeat=dimension):
        transformed = [
            tuple((word[index] - slope * gauge[index]) % p
                  for index in range(dimension))
            for slope, word in points
        ]
        rank = matrix_rank(transformed, p)
        gauge_counts[rank] = gauge_counts.get(rank, 0) + 1
    errors = [
        tuple((-word[index]) % p for index in range(dimension)) + (slope,)
        for slope, word in points
    ]
    return {
        "explanation_rank": explanation_rank,
        "lifted_rank": lifted_rank,
        "rank_drop_gauges": gauge_counts.get(dimension - 1, 0),
        "other_gauges": gauge_counts.get(dimension, 0),
        "error_rank": matrix_rank(errors, p),
    }


def validate(contract: object) -> int:
    if not isinstance(contract, dict) or contract.get("schema") != (
        "rate-half-mca-full-explanation-lifted-rank-gauge-dichotomy-v1"
    ):
        raise Reject("schema")
    control = contract["finite_control"]
    p, dimension = control["field"], control["K"]
    drop = [(1, (1, 0, 0)), (2, (2, 1, 0)), (3, (3, 0, 1))]
    full = [
        (1, (1, 0, 0)),
        (2, (0, 1, 0)),
        (3, (0, 0, 1)),
        (4, (0, 0, 0)),
    ]
    observed_drop = inspect_case(drop, p, dimension)
    observed_full = inspect_case(full, p, dimension)
    expected_drop = {"explanation_rank": dimension, **control["rank_K"]}
    expected_full = {"explanation_rank": dimension, **control["rank_K_plus_1"]}
    if observed_drop != expected_drop or observed_full != expected_full:
        raise Reject("finite dichotomy")
    expected_rows = {
        "KoalaBear MCA": (14, 5, 992852, 1044239),
        "Mersenne-31 MCA": (6, 1, 1037876, 1044242),
    }
    for row in contract["deployed"]:
        values = tuple(row[key] for key in (
            "K", "low_e", "drop_branch_high_e", "full_lift_high_e"
        ))
        if values != expected_rows.get(row["row"]):
            raise Reject("deployed wall")
        if not row["low_e"] < row["drop_branch_high_e"] < row["full_lift_high_e"]:
            raise Reject("wall order")
    return (
        observed_drop["rank_drop_gauges"] + observed_drop["other_gauges"]
        + observed_full["rank_drop_gauges"] + observed_full["other_gauges"]
    )


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    gauges = validate(contract)
    mutations = 0
    edits = (
        lambda value: value["finite_control"]["rank_K"].__setitem__("rank_drop_gauges", 48),
        lambda value: value["finite_control"]["rank_K_plus_1"].__setitem__("error_rank", 3),
        lambda value: value["deployed"][0].__setitem__("drop_branch_high_e", 1044239),
    )
    for edit in edits:
        changed = copy.deepcopy(contract)
        edit(changed)
        try:
            validate(changed)
        except Reject:
            mutations += 1
    if mutations != len(edits):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_FULL_EXPLANATION_LIFTED_RANK_GAUGE_DICHOTOMY_PASS "
        f"gauges={gauges} mutations={mutations}/{len(edits)}"
    )


if __name__ == "__main__":
    main()
