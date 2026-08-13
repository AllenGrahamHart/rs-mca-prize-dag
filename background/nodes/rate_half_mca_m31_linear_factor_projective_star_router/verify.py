#!/usr/bin/env python3
"""Verify the M31 linear-factor projective-star router constants."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "f37875f78786e56e17d1baeeaa98078b11341b26145fcfacc03ef0c081cd01a8"
PINS = {
    "background/nodes/rate_half_mca_m31_common_factor_mass_router/statement.md":
        "df2bcaa8c2577970c1e39b867787c0d311b7daa7679f4e0ecce053a6eb0963d8",
    "background/nodes/rate_half_mca_m31_common_factor_mass_router/proof.md":
        "8015bbe6671ef8a68d056a6ebb71c87bcc119844f1ce550b302a3cfd630432d0",
}


class Reject(ValueError):
    pass


def johnson(e: int, agreement: int, degree: int) -> tuple[int, int]:
    denominator = agreement * agreement - e * degree
    if denominator <= 0:
        raise Reject("Johnson denominator")
    return denominator, e * (agreement - degree) // denominator


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "row", "johnson", "conclusion"}:
        raise Reject("schema keys")
    if payload["schema"] != (
            "rate-half-mca-m31-linear-factor-projective-star-router-v1"):
        raise Reject("schema")
    if payload["sources"] != {
            "mass_router_statement_sha256": PINS[
                "background/nodes/rate_half_mca_m31_common_factor_mass_router/statement.md"],
            "mass_router_proof_sha256": PINS[
                "background/nodes/rate_half_mca_m31_common_factor_mass_router/proof.md"]}:
        raise Reject("sources")
    row = payload["row"]
    if row != {
            "e": 130237, "inside_agreement": 807,
            "captured_sections": 4982, "section_degree": 5}:
        raise Reject("row")
    table = payload["johnson"]
    if not isinstance(table, list) or len(table) != 6:
        raise Reject("table")
    checks = 17
    for degree, record in enumerate(table):
        denominator, cap = johnson(
            row["e"], row["inside_agreement"], degree)
        if record != {
                "parameter_degree": degree,
                "denominator": denominator, "cap": cap}:
            raise Reject(f"degree {degree}")
        checks += 7
    if max(record["cap"] for record in table[:5]) >= row["captured_sections"]:
        raise Reject("nonconstant exclusion")
    if table[5]["cap"] <= row["captured_sections"]:
        raise Reject("constant branch must survive this bound")
    if payload["conclusion"] != (
            "linear factor has constant YZ coefficients and an F-rational "
            "projective star center"):
        raise Reject("conclusion")
    return checks + 11


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINS.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"pin {relative}")
    payload = json.loads(CONTRACT.read_text())
    checks = validate(payload)
    mutations = []
    for index, key, delta in (
            (4, "cap", 1), (4, "denominator", -1),
            (5, "cap", -1)):
        mutant = copy.deepcopy(payload)
        mutant["johnson"][index][key] += delta
        try:
            validate(mutant)
        except Reject:
            mutations.append(True)
        else:
            mutations.append(False)
    mutant = copy.deepcopy(payload)
    mutant["row"]["captured_sections"] = 802
    try:
        validate(mutant)
    except Reject:
        mutations.append(True)
    else:
        mutations.append(False)
    if not all(mutations):
        raise Reject("mutations")
    print("m31-linear-factor-projective-star-router: PASS "
          f"({checks} checks; mutations={sum(mutations)}/{len(mutations)}; "
          "nonconstant_cap=802; captured=4982; residual=projective_star)")


if __name__ == "__main__":
    main()
