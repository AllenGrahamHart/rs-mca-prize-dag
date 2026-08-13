#!/usr/bin/env python3
"""Verify the M31 common-factor mass router constants."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "3426a0567353948b231ba9ce9d9165c2639be4d695a1aaec50c3e1cf133b66c5"
PINS = {
    "background/nodes/rate_half_mca_m31_interpolation_common_factor_router/statement.md":
        "54b2cf41ab04237d816bfa0dc9e381e656dd7e618ddffdc299635b630a65137d",
    "background/nodes/rate_half_mca_m31_interpolation_common_factor_router/proof.md":
        "4724a3ccc092b7520a3b2433748e62fb7b1a980882992674f772ceef9267de39",
    "background/nodes/rate_half_mca_m31_exact_layer_slot_core_packing_payment/statement.md":
        "49726ff8bffe0799bf9ed6899bc7b93922edc30a015a119352a778f55a17d29b",
    "background/nodes/rate_half_mca_m31_exact_layer_slot_core_packing_payment/proof.md":
        "352bfe7fa4576e32c19181ab9abce30f6133bb6c144a820a08f3216d026d1e4c",
}

N, M, C, BUDGET = 1048582, 67454, 5, 16777215


class Reject(ValueError):
    pass


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def line_charge(e: int, lines: int, lower: int,
                cap: int) -> dict[str, int]:
    core_budget = min(lines * cap, e + lines * (lines + 1) * C // 2)
    lower_sum = lines * lower
    full, remainder = divmod(core_budget - lower_sum, cap - lower)
    value = full * Fraction(N - cap, M - cap)
    if remainder:
        value += Fraction(N - lower - remainder, M - lower - remainder)
        residual = lines - full - 1
    else:
        residual = lines - full
    value += residual * Fraction(N - lower, M - lower)
    return {
        "core_budget": core_budget, "lower_sum": lower_sum,
        "full_caps": full, "remainder": remainder,
        "charge": value.numerator // value.denominator,
    }


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "line_supply", "factor", "conclusion"}:
        raise Reject("schema keys")
    if payload["schema"] != "rate-half-mca-m31-common-factor-mass-router-v1":
        raise Reject("schema")
    expected_sources = {
        "factor_router_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_interpolation_common_factor_router/statement.md"],
        "factor_router_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_interpolation_common_factor_router/proof.md"],
        "exact_layer_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_exact_layer_slot_core_packing_payment/statement.md"],
        "exact_layer_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_exact_layer_slot_core_packing_payment/proof.md"],
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")

    line = payload["line_supply"]
    if set(line) != {
            "e", "removed_before_forcing", "forced_distinct_lines",
            "inside_core_lower", "actual_core_cap", "core_budget",
            "lower_sum", "full_caps", "remainder", "charge", "target",
            "next_threshold"}:
        raise Reject("line keys")
    if (line["e"], line["removed_before_forcing"],
            line["forced_distinct_lines"], line["inside_core_lower"],
            line["actual_core_cap"]) != (130237, 7582, 7583, 807, 64796):
        raise Reject("line constants")
    record = line_charge(
        line["e"], line["removed_before_forcing"],
        line["inside_core_lower"], line["actual_core_cap"])
    for key, value in record.items():
        if line[key] != value:
            raise Reject(f"charge {key}")
    if line["target"] != BUDGET - line["charge"]:
        raise Reject("target")
    threshold = ((line["target"] - 13961576 + 1 + 1933560 - 1)
                 // 1933560)
    if line["next_threshold"] != threshold or threshold != 2:
        raise Reject("threshold")

    factor = payload["factor"]
    if set(factor) != {
            "ambient_value_degree", "minimum_factor_degree",
            "maximum_factor_degree", "maximum_off_factor_pairs",
            "minimum_on_factor_pairs", "minimum_factor_points",
            "maximum_exception_points", "pairwise_core_intersection"}:
        raise Reject("factor keys")
    degree = factor["ambient_value_degree"]
    if (degree, factor["minimum_factor_degree"],
            factor["maximum_factor_degree"]) != (52, 1, 52):
        raise Reject("degree range")
    off = (degree - factor["minimum_factor_degree"]) ** 2
    if factor["maximum_off_factor_pairs"] != off:
        raise Reject("off factor")
    on = line["forced_distinct_lines"] - off
    if factor["minimum_on_factor_pairs"] != on:
        raise Reject("on factor")
    c = factor["pairwise_core_intersection"]
    if c != C:
        raise Reject("intersection")
    u = line["inside_core_lower"]
    points = ceil_div(on * u * u, u + c * (on - 1))
    if factor["minimum_factor_points"] != points:
        raise Reject("factor points")
    if factor["maximum_exception_points"] != line["e"] - points:
        raise Reject("exceptions")
    if payload["conclusion"] != (
            "unsafe common factor contains at least 4982 pairs and 126188 "
            "inside received points"):
        raise Reject("conclusion")
    return 97


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINS.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {relative}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    mutations = []
    for section, key, delta in (
            ("line_supply", "charge", 1),
            ("line_supply", "removed_before_forcing", -1),
            ("factor", "maximum_off_factor_pairs", 1),
            ("factor", "minimum_on_factor_pairs", -1),
            ("factor", "minimum_factor_points", -1)):
        mutant = copy.deepcopy(payload)
        mutant[section][key] += delta
        try:
            validate(mutant)
        except Reject:
            mutations.append(True)
        else:
            mutations.append(False)
    if not all(mutations):
        raise Reject("mutations")
    print("m31-common-factor-mass-router: PASS "
          f"({checks} checks; mutations={sum(mutations)}/{len(mutations)}; "
          "pairs>=4982; factor_points>=126188; exceptions<=4049)")


if __name__ == "__main__":
    main()
