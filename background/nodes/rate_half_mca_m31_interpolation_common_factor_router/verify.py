#!/usr/bin/env python3
"""Verify the M31 interpolation common-factor router constants."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "a57810d16c6b0422b5d702abe84da49aef8da783c1cafad88b3e5eab36c37cd3"
PINS = {
    "background/nodes/rate_half_mca_m31_exact_layer_slot_core_packing_payment/statement.md":
        "49726ff8bffe0799bf9ed6899bc7b93922edc30a015a119352a778f55a17d29b",
    "background/nodes/rate_half_mca_m31_exact_layer_slot_core_packing_payment/proof.md":
        "352bfe7fa4576e32c19181ab9abce30f6133bb6c144a820a08f3216d026d1e4c",
    "background/nodes/rate_half_mca_m31_core_dichotomy_capped_charge_payment/statement.md":
        "2b3f5b24ad800aac4dba4896181b832ea43c1376791b1310eec9fbdeacf2647e",
    "background/nodes/rate_half_mca_m31_core_dichotomy_capped_charge_payment/proof.md":
        "ebfb312ad8d7b97df1af97169560f42f4b24e990b6b3d81a2816cec2347dca5a",
}

N, M, C, BUDGET = 1048582, 67454, 5, 16777215


class Reject(ValueError):
    pass


def monomial_count(degree: int, value_weight: int) -> int:
    return sum((level + 1) * (degree - value_weight * level + 1)
               for level in range(degree // value_weight + 1))


def charge_record(e: int, lines: int, lower: int,
                  cap: int) -> dict[str, int]:
    budget = min(lines * cap, e + lines * (lines + 1) * C // 2)
    lower_sum = lines * lower
    excess = budget - lower_sum
    if excess < 0:
        raise Reject("infeasible lower bounds")
    full, remainder = divmod(excess, cap - lower)
    if full >= lines:
        raise Reject("allocation shape")
    value = full * Fraction(N - cap, M - cap)
    if remainder:
        value += Fraction(N - lower - remainder, M - lower - remainder)
        residual = lines - full - 1
    else:
        residual = lines - full
    value += residual * Fraction(N - lower, M - lower)
    return {
        "core_budget": budget,
        "lower_sum": lower_sum,
        "full_caps": full,
        "remainder": remainder,
        "charge": value.numerator // value.denominator,
    }


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "row", "interpolation", "conclusion"}:
        raise Reject("schema keys")
    if payload["schema"] != (
            "rate-half-mca-m31-interpolation-common-factor-router-v1"):
        raise Reject("schema")
    expected_sources = {
        "exact_layer_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_exact_layer_slot_core_packing_payment/statement.md"],
        "exact_layer_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_exact_layer_slot_core_packing_payment/proof.md"],
        "dichotomy_statement_sha256": PINS[
            "background/nodes/rate_half_mca_m31_core_dichotomy_capped_charge_payment/statement.md"],
        "dichotomy_proof_sha256": PINS[
            "background/nodes/rate_half_mca_m31_core_dichotomy_capped_charge_payment/proof.md"],
    }
    if payload["sources"] != expected_sources:
        raise Reject("sources")

    row = payload["row"]
    if set(row) != {
            "e", "cutoff", "minimum_layer", "minimum_line_size",
            "inside_core_lower", "actual_core_cap", "base", "groups",
            "removed_before_forcing", "forced_distinct_lines",
            "core_budget", "lower_sum", "full_caps", "remainder",
            "charge", "target", "next_threshold"}:
        raise Reject("row keys")
    if (row["e"], row["cutoff"], row["minimum_layer"],
            row["minimum_line_size"]) != (130237, 65521, 65522, 2):
        raise Reject("row constants")
    expected_lower = (row["minimum_line_size"] * row["minimum_layer"]
                      - row["e"])
    if row["inside_core_lower"] != expected_lower:
        raise Reject("core lower")
    if row["actual_core_cap"] != row["e"] + 9 - 65450:
        raise Reject("core cap")
    if (row["base"], row["groups"]) != (13961576, 1933560):
        raise Reject("bank")

    interpolation = payload["interpolation"]
    if set(interpolation) != {
            "weights", "weighted_degree", "monomials",
            "kernel_dimension_lower", "value_total_degree", "bezout_cap",
            "root_count"}:
        raise Reject("interpolation keys")
    if interpolation["weights"] != [1, 5, 5]:
        raise Reject("weights")
    degree = interpolation["weighted_degree"]
    if degree != 264:
        raise Reject("degree")
    monomials = monomial_count(degree, 5)
    if interpolation["monomials"] != monomials:
        raise Reject("monomials")
    if interpolation["kernel_dimension_lower"] != monomials - row["e"]:
        raise Reject("kernel dimension")
    value_degree = degree // 5
    if interpolation["value_total_degree"] != value_degree:
        raise Reject("value degree")
    if interpolation["bezout_cap"] != value_degree * value_degree:
        raise Reject("bezout")
    if interpolation["root_count"] != row["inside_core_lower"]:
        raise Reject("root count")
    if interpolation["root_count"] <= degree:
        raise Reject("root-degree gap")

    if row["removed_before_forcing"] != interpolation["bezout_cap"]:
        raise Reject("removed line count")
    if row["forced_distinct_lines"] != row["removed_before_forcing"] + 1:
        raise Reject("forced line count")
    record = charge_record(
        row["e"], row["removed_before_forcing"],
        row["inside_core_lower"], row["actual_core_cap"])
    for key, value in record.items():
        if row[key] != value:
            raise Reject(f"charge {key}")
    if row["target"] != BUDGET - row["charge"]:
        raise Reject("target")
    threshold = ((row["target"] - row["base"] + 1
                  + row["groups"] - 1) // row["groups"])
    if row["next_threshold"] != threshold or threshold != 2:
        raise Reject("threshold")
    if payload["conclusion"] != (
            "unsafe implies a common factor of positive YZ degree over "
            "algebraic closure of F(X)"):
        raise Reject("conclusion")
    return 83


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
            ("row", "inside_core_lower", -1),
            ("row", "charge", 1),
            ("row", "removed_before_forcing", -1),
            ("interpolation", "monomials", -1),
            ("interpolation", "bezout_cap", 1)):
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
    print("m31-interpolation-common-factor-router: PASS "
          f"({checks} checks; mutations={sum(mutations)}/{len(mutations)}; "
          "kernel>=938; coprime_cap=2704; forced=2705)")


if __name__ == "__main__":
    main()
