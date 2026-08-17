#!/usr/bin/env python3
"""Verify the fixed-union flat-coupled support-4/5 charge."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "295d82f01e6a8cb9f9ef1d9dd4a0966e14d729cfde5a8259bb0df07ca9a66cd4"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def compute(K: int, m: int, u: int, g: int):
    N = m - u
    R = K - u - g
    B = R + 3

    def lower(d: int) -> int:
        return comb(u, d) + sum(
            comb(u, d - j) * comb(N, j - 1) * R // j
            for j in range(1, d)
        )

    x4 = min(R * comb(N, 3) // 4, R * comb(N, 4) // (N - B))
    x5 = (R * comb(N, 4) - (N - B) * x4) // 5
    i4 = (lower(4) + x4) * comb(m - 4, 7)
    i5 = (lower(5) + x5) * comb(m - 5, 6)
    decrement = (N - B + 4) // 5
    require(21 * comb(m - 4, 7) >= 15 * decrement * comb(m - 5, 6), "slope")
    return {"N": N, "R": R, "B": B, "X4": x4, "X5": x5,
            "I4": i4, "I5": i5, "weighted": 21 * i4 + 15 * i5}


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract object")
    require(data["schema"].endswith("flat-coupled-45-charge-v1"), "schema")
    require(data["hypotheses"]["minimum_dimension"] == 5, "dimension")
    require(data["hypotheses"]["minimum_K_minus_g"] == 5, "monotonicity")
    require(data["weights"] == {"4": 21, "5": 15}, "weights")
    row = data["k72_control"]
    actual = compute(row["K"], row["m"], row["u"], row["g"])
    for key, value in actual.items():
        require(row[key] == value, f"control {key}")
    require(5 * row["X5"] <= row["R"] * comb(row["N"], 4) - (row["N"] - row["B"]) * row["X4"], "FC envelope")
    return {"control_fields": len(actual)}


def tamper_selftest(data: dict) -> int:
    mutations = (
        lambda item: item["weights"].__setitem__("4", 20),
        lambda item: item["hypotheses"].__setitem__("minimum_dimension", 4),
        lambda item: item["k72_control"].__setitem__("B", 35),
        lambda item: item["k72_control"].__setitem__("weighted", 0),
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
