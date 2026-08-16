#!/usr/bin/env python3
"""Verify the pairwise full-completion carrier-atlas contract."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "18a8f0af39e118d2d8c4554b03b142c57f6f01ea9db8f1b43d4ea570e85fdab9"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def rows(M2: int, M3: int, Md: int, d: int):
    b2 = M2 + 1
    r3 = M3 - M2 + 1
    rd = Md - M2 + d - 2
    return [
        [t, b2 + r3 + rd - t, 10 - d if t == 0 else 11 - d]
        for t in range(min(r3, Md - M2) + 1)
    ]


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract object")
    require(data["schema"].endswith("pairwise-carrier-atlas-v1"), "schema")
    require(data["ambient_dimension"] == 10, "dimension")
    require(data["supports"] == [3, 4, 5], "supports")
    require(data["position_cases"]["full_completion_condition"] == "Mc>=M2+1", "full condition")
    overlap = data["overlap"]
    require(overlap["maximum_t"] == "min(r3,Md-M2)", "overlap maximum")
    require(overlap["dimension_t0"] == "10-d", "zero dimension")
    require(overlap["dimension_t_positive"] == "11-d", "positive dimension")
    for control in data["controls"]:
        actual = rows(control["M2"], control["M3"], control["Md"], control["d"])
        require(actual == control["rows"], "control atlas")
        require(all(row[1] > 0 and row[2] > 0 for row in actual), "positive row")
    return {"controls": len(data["controls"])}


def tamper_selftest(data: dict) -> int:
    mutations = (
        lambda item: item.__setitem__("ambient_dimension", 11),
        lambda item: item["supports"].append(6),
        lambda item: item["overlap"].__setitem__("maximum_t", "r3"),
        lambda item: item["controls"][0]["rows"][0].__setitem__(1, 35),
    )
    rejected = 0
    for mutate in mutations:
        trial = copy.deepcopy(data)
        mutate(trial)
        try:
            validate(trial)
        except (Reject, KeyError, TypeError, ValueError):
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
