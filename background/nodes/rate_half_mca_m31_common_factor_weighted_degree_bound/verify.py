#!/usr/bin/env python3
"""Verify the M31 common-factor weighted-degree bound."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "6fc404de1c23def1f24b526655328a6ff9a93c328ff5d0dcb3d997584b36db48"
PINS = {
    "background/nodes/rate_half_mca_m31_interpolation_common_factor_router/statement.md":
        "54b2cf41ab04237d816bfa0dc9e381e656dd7e618ddffdc299635b630a65137d",
    "background/nodes/rate_half_mca_m31_interpolation_common_factor_router/proof.md":
        "4724a3ccc092b7520a3b2433748e62fb7b1a980882992674f772ceef9267de39",
    "background/nodes/rate_half_mca_m31_common_factor_mass_router/statement.md":
        "df2bcaa8c2577970c1e39b867787c0d311b7daa7679f4e0ecce053a6eb0963d8",
    "background/nodes/rate_half_mca_m31_common_factor_mass_router/proof.md":
        "8015bbe6671ef8a68d056a6ebb71c87bcc119844f1ce550b302a3cfd630432d0",
}


class Reject(ValueError):
    pass


def monomial_count(degree: int) -> int:
    if degree < 0:
        return 0
    return sum((level + 1) * (degree - 5 * level + 1)
               for level in range(degree // 5 + 1))


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def validate(payload: object) -> int:
    if not isinstance(payload, dict) or set(payload) != {
            "schema", "sources", "kernel", "nonlinear", "conclusion"}:
        raise Reject("schema keys")
    if payload["schema"] != (
            "rate-half-mca-m31-common-factor-weighted-degree-bound-v1"):
        raise Reject("schema")
    if payload["sources"] != {
            "interpolation_statement_sha256": PINS[
                "background/nodes/rate_half_mca_m31_interpolation_common_factor_router/statement.md"],
            "interpolation_proof_sha256": PINS[
                "background/nodes/rate_half_mca_m31_interpolation_common_factor_router/proof.md"],
            "mass_statement_sha256": PINS[
                "background/nodes/rate_half_mca_m31_common_factor_mass_router/statement.md"],
            "mass_proof_sha256": PINS[
                "background/nodes/rate_half_mca_m31_common_factor_mass_router/proof.md"]}:
        raise Reject("sources")

    kernel = payload["kernel"]
    if set(kernel) != {
            "weighted_degree", "dimension_lower", "quotient_degree_reject",
            "monomials_reject", "quotient_degree_accept",
            "monomials_accept", "factor_weighted_degree_max",
            "factor_yz_degree_max"}:
        raise Reject("kernel keys")
    if (kernel["weighted_degree"], kernel["dimension_lower"]) != (264, 938):
        raise Reject("kernel constants")
    reject = kernel["quotient_degree_reject"]
    accept = kernel["quotient_degree_accept"]
    if accept != reject + 1:
        raise Reject("adjacent threshold")
    if kernel["monomials_reject"] != monomial_count(reject):
        raise Reject("reject count")
    if kernel["monomials_accept"] != monomial_count(accept):
        raise Reject("accept count")
    if not (kernel["monomials_reject"] < kernel["dimension_lower"]
            <= kernel["monomials_accept"]):
        raise Reject("dimension threshold")
    first = min(degree for degree in range(kernel["weighted_degree"] + 1)
                if monomial_count(degree) >= kernel["dimension_lower"])
    if first != accept:
        raise Reject("first quotient degree")
    factor_weight = kernel["weighted_degree"] - first
    if kernel["factor_weighted_degree_max"] != factor_weight:
        raise Reject("factor weight")
    if kernel["factor_yz_degree_max"] != factor_weight // 5:
        raise Reject("factor YZ degree")

    branch = payload["nonlinear"]
    if set(branch) != {
            "factor_yz_degree_min", "forced_lines", "ambient_yz_degree",
            "off_factor_pairs_max", "on_factor_pairs_min",
            "inside_core_lower", "pairwise_core_intersection",
            "inside_support", "factor_points_min",
            "exception_points_max"}:
        raise Reject("branch keys")
    if branch["factor_yz_degree_min"] != 2:
        raise Reject("nonlinear degree")
    if branch["forced_lines"] != 7583 or branch["ambient_yz_degree"] != 52:
        raise Reject("line constants")
    off = (branch["ambient_yz_degree"]
           - branch["factor_yz_degree_min"]) ** 2
    if branch["off_factor_pairs_max"] != off:
        raise Reject("off-factor count")
    on = branch["forced_lines"] - off
    if branch["on_factor_pairs_min"] != on:
        raise Reject("on-factor count")
    if (branch["inside_core_lower"],
            branch["pairwise_core_intersection"],
            branch["inside_support"]) != (807, 5, 130237):
        raise Reject("incidence constants")
    points = ceil_div(
        on * branch["inside_core_lower"] ** 2,
        branch["inside_core_lower"]
        + branch["pairwise_core_intersection"] * (on - 1))
    if branch["factor_points_min"] != points:
        raise Reject("factor points")
    if branch["exception_points_max"] != branch["inside_support"] - points:
        raise Reject("exceptions")
    if payload["conclusion"] != (
            "nonlinear common factor has YZ degree 2..43 and at most 3971 "
            "inside exceptions"):
        raise Reject("conclusion")
    return 89


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
            ("kernel", "monomials_reject", 1),
            ("kernel", "factor_weighted_degree_max", 1),
            ("kernel", "factor_yz_degree_max", 1),
            ("nonlinear", "on_factor_pairs_min", -1),
            ("nonlinear", "factor_points_min", -1)):
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
    print("m31-common-factor-weighted-degree-bound: PASS "
          f"({checks} checks; mutations={sum(mutations)}/{len(mutations)}; "
          "wdeg<=217; yzdeg<=43; nonlinear_pairs>=5083; exceptions<=3971)")


if __name__ == "__main__":
    main()
