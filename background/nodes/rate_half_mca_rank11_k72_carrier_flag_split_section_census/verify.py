#!/usr/bin/env python3
"""Verify the exact K'=72 flat-coupled split-section payment."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "25f9b08e71c86c8168a8352b574bbac10395e15c6dee16e0645e7cadb4861f6a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def lower_strata(d: int, union: int, outside: int, maximum: int) -> int:
    total = comb(union, d)
    for j in range(1, d):
        total += comb(union, d - j) * comb(outside, j - 1) * maximum // j
    return total


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract object")
    require(data["schema"] == "rate-half-mca-rank11-k72-carrier-flag-split-section-census-v1", "schema")
    row = data["row"]
    caps = data["flat_caps"]
    weights = data["weights"]
    expected = data["expected"]
    require(row["Kprime"] == 72 and row["m"] == 67472 + row["Kprime"], "row")
    require(row["outside_points"] == row["m"] - row["fixed_union"], "outside")
    require(row["residual_degree_ceiling"] == row["Kprime"] - 1 - row["fixed_union"], "degree")
    require(caps == {"rank3": 34, "rank4": 35, "completion": 31}, "flat caps")
    require(weights == {"support4": 21, "support5": 15, "selected_set_size": 11}, "weights")

    m = row["m"]
    n = row["outside_points"]
    top4 = caps["completion"] * comb(n, 3) // 4
    top5 = (
        caps["completion"] * comb(n, 4)
        - (n - caps["rank3"]) * top4
    ) // 5
    require(top4 == expected["top4"], "top4")
    require(top5 == expected["top5_coupled"], "top5")

    i4 = (lower_strata(4, row["fixed_union"], n, 31) + top4) * comb(m - 4, 7)
    i5 = (lower_strata(5, row["fixed_union"], n, 31) + top5) * comb(m - 5, 6)
    weighted = weights["support4"] * i4 + weights["support5"] * i5
    margin = expected["required"] - weighted
    monotone = (
        weights["support4"] * comb(m - 4, 7)
        - weights["support5"] * ((n - 34 + 4) // 5) * comb(m - 5, 6)
    ) // comb(m - 5, 6)
    require(i4 == expected["I4"] and i5 == expected["I5"], "incidences")
    require(weighted == expected["weighted"], "weighted")
    require(margin == expected["margin"] > 0, "safe margin")
    require(monotone == expected["floor_monotonicity_units"] == 195, "monotonicity")
    return {"top4": top4, "top5": top5, "weighted": weighted, "margin": margin}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["row"].__setitem__("fixed_union", 35),
        lambda item: item["flat_caps"].__setitem__("rank4", 36),
        lambda item: item["flat_caps"].__setitem__("completion", 32),
        lambda item: item["weights"].__setitem__("support4", 20),
        lambda item: item["expected"].__setitem__("top5_coupled", 0),
        lambda item: item["expected"].__setitem__("margin", -1),
    )
    rejected = 0
    for mutate in mutations:
        trial = copy.deepcopy(data)
        mutate(trial)
        try:
            validate(trial)
        except (Reject, KeyError, TypeError, ValueError, ZeroDivisionError):
            rejected += 1
    require(rejected == len(mutations), "tamper rejection")
    return rejected


def main() -> int:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    result["contract_sha256"] = CONTRACT_SHA256
    result["tamper_rejected"] = tamper_selftest(data)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Reject as exc:
        print(f"REJECT: {exc}", file=sys.stderr)
        raise SystemExit(1)
