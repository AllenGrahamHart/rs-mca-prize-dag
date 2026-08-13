#!/usr/bin/env python3
"""Verify the corrected proper-subspace occupancy compiler walls."""

from __future__ import annotations

import copy
import hashlib
import json
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "69a89b3e0d2f4aaf3c5c0dd0d0bf72e47366b0c588209646a9a0f13bbbe22446"


class Reject(ValueError):
    pass


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length)) if length else 1


def endpoint_data(R: int, d: int, K: int, q: int) -> tuple[tuple[int, int], ...]:
    N = R + K
    m = d + K
    common = rising(d + 1, q - 1)
    return (
        (falling(N, q + 1), m * common),
        (falling(R + q, q + 1), (d + q) * common),
    )


def bound(R: int, d: int, K: int, q: int, L: int) -> int:
    return max(numerator // (denominator * L)
               for numerator, denominator in endpoint_data(R, d, K, q))


def minimum_factor(R: int, d: int, K: int, q: int, budget: int) -> int:
    return max(
        numerator // ((budget + 1) * denominator) + 1
        for numerator, denominator in endpoint_data(R, d, K, q)
    )


def validate(contract: object) -> int:
    if not isinstance(contract, dict) or contract.get("schema") != (
        "rate-half-mca-proper-subspace-occupancy-compiler-v1"
    ):
        raise Reject("schema")
    regression = contract.get("regression")
    if not isinstance(regression, dict):
        raise Reject("regression")
    corrected = bound(
        regression["N"] - regression["K"],
        regression["m"] - regression["K"],
        regression["K"],
        regression["q"],
        max(1, regression["e"] - (regression["N"] - regression["m"])),
    )
    if corrected != regression["corrected_bound"] or not (
        regression["observed_slopes"] <= corrected
    ):
        raise Reject("counterexample regression")

    checks = 1
    for row in contract.get("rows", []):
        R, d, K, budget = (row[key] for key in ("R", "d", "K", "budget"))
        factors = [minimum_factor(R, d, K, q, budget) for q in range(1, K + 1)]
        unconditional = max(q for q, factor in enumerate(factors, 1) if factor == 1)
        if unconditional != row["unconditional_through_q"]:
            raise Reject("unconditional wall")
        for wall in row["walls"]:
            q = wall["q"]
            L = factors[q - 1]
            if L != wall["minimum_L"]:
                raise Reject("minimum factor")
            if wall["minimum_e"] != R - d + L:
                raise Reject("support wall")
            if wall["maximum_j"] != R - wall["minimum_e"]:
                raise Reject("defect wall")
            if bound(R, d, K, q, L) != wall["bound"]:
                raise Reject("bound")
            if bound(R, d, K, q, L - 1) != wall["previous_bound"]:
                raise Reject("adjacent bound")
            if not wall["bound"] <= budget < wall["previous_bound"]:
                raise Reject("budget crossing")
            checks += 1
        unpaid = row["unpaid"]
        q = unpaid["q"]
        if factors[q - 1] != unpaid["required_L"] or unpaid["maximum_L"] != d:
            raise Reject("unpaid factor")
        if bound(R, d, K, q, d) != unpaid["maximum_L_bound"]:
            raise Reject("maximum support bound")
        if not unpaid["required_L"] > d or not unpaid["maximum_L_bound"] > budget:
            raise Reject("unpaid wall")
        checks += 1
    return checks


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    checks = validate(contract)
    mutations = 0
    edits = (
        lambda value: value["regression"].__setitem__("corrected_bound", 23),
        lambda value: value["rows"][0]["walls"][0].__setitem__("minimum_L", 3),
        lambda value: value["rows"][0]["walls"][2].__setitem__("bound", 1),
        lambda value: value["rows"][1]["unpaid"].__setitem__("required_L", 67448),
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
        "RATE_HALF_MCA_PROPER_SUBSPACE_OCCUPANCY_COMPILER_PASS "
        f"checks={checks} mutations={mutations}/{len(edits)}"
    )


if __name__ == "__main__":
    main()
