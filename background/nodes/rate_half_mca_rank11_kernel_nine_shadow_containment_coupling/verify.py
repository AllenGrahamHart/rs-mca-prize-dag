#!/usr/bin/env python3
"""Verify the full nine-shadow containment coupling contract."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "3ba2ac2f6053c753f3a60e2df8152f4bde8221deb772648699f99c9c5c314056"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-nine-shadow-containment-coupling-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_nine_shadow_coupling"
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["correction_dimension"], p["component_subset_size"], p["shadow_subset_size"]) == (10, 11, 9), "dimensions")
    require(p["shadows_per_component_subset"] == comb(11, 9) == 55, "shadow count")
    require(p["rank9_spanning_shadow_minimum"] == comb(3, 2) == 3, "rank9 minimum")
    require(p["support_extension_formula"] == "C(m_prime-9,2)", "support extension")
    require(p["rank9_extension_formula"] == "C(K_prime-10,2)", "rank9 extension")
    require(p["rank9_coefficient_formula"].startswith("52+3*"), "coefficient")
    require("55*sum_d_ge_2" in p["resource_formula"], "resource")

    checked = 0
    for kprime in (12, 13, 15445, 15670, 1048576):
        mprime = kprime + 67472
        e0 = comb(mprime - 9, 2)
        e1 = comb(kprime - 10, 2)
        require(e0 > e1 > 0, f"extension order {kprime}")
        coefficient = 55 + Fraction(3 * (e0 - e1), e1)
        require(coefficient == 52 + Fraction(3 * e0, e1), f"coefficient identity {kprime}")
        checked += 1

    require("does not by itself pay" in str(data.get("nonclaim")), "nonclaim")
    return {"rows": checked, "shadows": p["shadows_per_component_subset"]}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("shadows_per_component_subset", 54),
        lambda item: item["parameters"].__setitem__("rank9_spanning_shadow_minimum", 2),
        lambda item: item["parameters"].__setitem__("support_extension_formula", "C(m_prime-8,2)"),
        lambda item: item["parameters"].__setitem__("rank9_extension_formula", "C(K_prime-9,2)"),
        lambda item: item["dependencies"].clear(),
        lambda item: item.__setitem__("nonclaim", "complete payment"),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_NINE_SHADOW_CONTAINMENT_COUPLING_PASS "
        f"rows={result['rows']} shadows={result['shadows']} controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
