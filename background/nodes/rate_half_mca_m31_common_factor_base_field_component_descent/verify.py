#!/usr/bin/env python3
"""Verify the M31 base-field component descent constants."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "3548a23429caf5943dc01c5fbc7c4bbedb5dee92322699fe7fa0772ec6020297"
PINS = {
    "background/nodes/rate_half_mca_m31_common_factor_weighted_degree_bound/statement.md":
        "6c014e5f95c42b80daaa41e1939068d1f4af9b632bf9310d385a6b0f63242b75",
    "background/nodes/rate_half_mca_m31_common_factor_weighted_degree_bound/proof.md":
        "f24d70c3359c403d596c01f5e173eecbc2d6a081e4c81f734759821411de8299",
    "background/nodes/deployed_identity_prefix_owner_scope_audit/statement.md":
        "d7ac0f627dc606dc0beee3bf4f4bc2ac63410298f71cf4408722359936923c7c",
    "background/nodes/deployed_identity_prefix_owner_scope_audit/deployed_rows.json":
        "bdef9068a68dccaae0240eb87b0edce6c068497377cb65273d4f8548d36b85d1",
}


class Reject(ValueError):
    pass


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "field", "descent", "conclusion"}:
        raise Reject("schema keys")
    if payload["schema"] != (
            "rate-half-mca-m31-common-factor-base-field-component-descent-v1"):
        raise Reject("schema")
    if payload["sources"] != {
            "weighted_statement_sha256": PINS[
                "background/nodes/rate_half_mca_m31_common_factor_weighted_degree_bound/statement.md"],
            "weighted_proof_sha256": PINS[
                "background/nodes/rate_half_mca_m31_common_factor_weighted_degree_bound/proof.md"],
            "deployed_rows_statement_sha256": PINS[
                "background/nodes/deployed_identity_prefix_owner_scope_audit/statement.md"],
            "deployed_rows_json_sha256": PINS[
                "background/nodes/deployed_identity_prefix_owner_scope_audit/deployed_rows.json"]}:
        raise Reject("sources")

    field = payload["field"]
    if field != {
            "characteristic": 2147483647, "extension_degree": 4,
            "factor_degree_max": 43}:
        raise Reject("field")
    if field["characteristic"] <= field["factor_degree_max"]:
        raise Reject("separability guard")

    row = payload["descent"]
    if set(row) != {
            "factor_degree_min", "forced_lines", "ambient_yz_degree",
            "base_field_pairs_min", "one_component_pairs_min",
            "inside_core_lower", "pairwise_core_intersection",
            "inside_support", "base_field_factor_points_min",
            "exception_points_max"}:
        raise Reject("descent keys")
    if (row["factor_degree_min"], row["forced_lines"],
            row["ambient_yz_degree"]) != (2, 7583, 52):
        raise Reject("descent constants")
    records = []
    for degree in range(
            row["factor_degree_min"], field["factor_degree_max"] + 1):
        captured = row["forced_lines"] - (row["ambient_yz_degree"] - degree) ** 2
        base_field = captured - degree**2
        one_component = ceil_div(base_field, degree)
        records.append((degree, captured, base_field, one_component))
    if min(record[2] for record in records) != row["base_field_pairs_min"]:
        raise Reject("base-field pairs")
    if min(record[3] for record in records) != row["one_component_pairs_min"]:
        raise Reject("component pairs")
    if records[0][2] != 5079 or records[-1][2] != 5653:
        raise Reject("endpoint descent")
    if (row["inside_core_lower"],
            row["pairwise_core_intersection"],
            row["inside_support"]) != (807, 5, 130237):
        raise Reject("incidence constants")
    pairs = row["base_field_pairs_min"]
    points = ceil_div(
        pairs * row["inside_core_lower"] ** 2,
        row["inside_core_lower"]
        + row["pairwise_core_intersection"] * (pairs - 1))
    if row["base_field_factor_points_min"] != points:
        raise Reject("factor points")
    if row["exception_points_max"] != row["inside_support"] - points:
        raise Reject("exceptions")
    if payload["conclusion"] != (
            "at least 5079 selected pairs lie on F(X)-defined components"):
        raise Reject("conclusion")
    return 101


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
            ("field", "factor_degree_max", 1),
            ("descent", "base_field_pairs_min", -1),
            ("descent", "one_component_pairs_min", -1),
            ("descent", "base_field_factor_points_min", -1),
            ("descent", "exception_points_max", 1)):
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
    print("m31-common-factor-base-field-component-descent: PASS "
          f"({checks} checks; mutations={sum(mutations)}/{len(mutations)}; "
          "base_pairs>=5079; component_pairs>=132; exceptions<=3974)")


if __name__ == "__main__":
    main()
