#!/usr/bin/env python3
"""Outcome-neutral checker for the official affine-reflection census."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


P = 2_130_706_433
N = 2**21
INDEX = 1016
GENERATOR = 3
SOURCE = Path(__file__).with_name(
    "rate_half_mca_rank11_affine_reflection_cyclotomic_census.cpp"
)
SOURCE_SHA256 = "a910d1f447cf2f0895a5b050a2de79de57831c7ca22679065c2cdc53b948a00b"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "result")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-affine-reflection-cyclotomic-census-result-v1",
        "schema",
    )
    require(data.get("status") == "COMPLETE" and data.get("failures") == [], "completion")
    require(
        (data.get("p"), data.get("domain_order"), data.get("index"), data.get("primitive_generator"))
        == (P, N, INDEX, GENERATOR),
        "pins",
    )
    require(data.get("source_sha256") == SOURCE_SHA256, "source hash field")
    require(hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256, "source bytes")
    require(data.get("shard_size") == 11 and data.get("shard_count") == 93, "shards")
    require(data.get("completed_shards") == 93, "completed shards")
    rows = data.get("rows")
    require(isinstance(rows, list) and len(rows) == INDEX, "row count")
    counts = []
    c = 1
    for expected_index, row in enumerate(rows):
        require(
            isinstance(row, list)
            and len(row) == 4
            and all(isinstance(value, int) for value in row),
            "row shape",
        )
        index, recorded_c, production, audit = row
        require(index == expected_index and recorded_c == c, "row identity")
        require(production == audit and 0 <= production <= N, "paired count")
        fixed = 1 if pow((recorded_c * pow(2, P - 2, P)) % P, N, P) == 1 else 0
        require(production % 2 == fixed, "involution parity")
        counts.append(production)
        c = c * GENERATOR % P
    require(c == pow(GENERATOR, INDEX, P), "coset traversal")
    require(sum(counts) == N - 1, "cyclotomic first moment")
    maximum = max(counts)
    maximizing = [index for index, count in enumerate(counts) if count == maximum]
    require(data.get("count_sum") == N - 1, "reported sum")
    require(data.get("maximum_reflection_points") == maximum, "reported maximum")
    require(data.get("maximizing_indices") == maximizing, "reported maximizers")
    return {
        "maximum": maximum,
        "maximum_fibers": maximum // 2,
        "maximizers": len(maximizing),
    }


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("status", "INCOMPLETE"),
        lambda item: item.__setitem__("p", P - 2),
        lambda item: item.__setitem__("completed_shards", 92),
        lambda item: item["rows"][0].__setitem__(1, 2),
        lambda item: item["rows"][0].__setitem__(3, item["rows"][0][3] + 1),
        lambda item: item["rows"][1].__setitem__(2, item["rows"][1][2] + 2),
        lambda item: item.__setitem__("count_sum", item["count_sum"] + 1),
        lambda item: item.__setitem__("maximum_reflection_points", item["maximum_reflection_points"] + 1),
        lambda item: item.__setitem__("maximizing_indices", []),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, IndexError, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.result.read_text())
    checked = validate(data)
    if args.tamper_selftest:
        print(f"AFFINE_REFLECTION_CENSUS_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "AFFINE_REFLECTION_CENSUS_PASS "
        f"maximum={checked['maximum']} fibers={checked['maximum_fibers']} "
        f"maximizers={checked['maximizers']}"
    )


if __name__ == "__main__":
    main()
