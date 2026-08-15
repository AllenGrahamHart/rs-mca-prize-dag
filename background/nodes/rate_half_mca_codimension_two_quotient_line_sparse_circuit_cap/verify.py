#!/usr/bin/env python3
"""Verify the codimension-two quotient-line sparse-circuit cap."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "2007208c46a197c7d526ea185b9fe9034c860279f02c6d7d815cc0816eb90c82"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def label_cap(m: int, support: int) -> int:
    if support == 1:
        return 2
    candidates = [support + 1]
    for degree in range(1, support + 1):
        for fixed in range(support):
            candidates.append(
                support + degree * (m - fixed) // (support - fixed)
            )
    return max(candidates)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-codimension-two-quotient-line-sparse-circuit-cap-v1",
        "schema",
    )
    require(data.get("dependencies") == [], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(
        (p["ambient_polynomial_dimension"], p["correction_dimension"])
        == (12, 10),
        "dimensions",
    )
    require(p["quotient_dimension"] == 2, "quotient")
    require(p["component_subset_size"] == 11, "component size")
    require(p["support_ceiling"] == 5, "support ceiling")
    m = int(p["official_support_size"])
    require(m == 67484, "official support")

    caps: dict[str, int] = {}
    terms: dict[str, int] = {}
    for support in range(1, 6):
        key = str(support)
        caps[key] = label_cap(m, support)
        terms[key] = caps[key] * comb(m - support, 11 - support)
    require(p["support_one_label_cap"] == 2, "support-one cap")
    require(p["support_label_caps"] == caps, "label caps")
    require(p["support_incidence_terms"] == terms, "incidence terms")
    total = sum(terms.values())
    require(p["per_record_sparse_incidence_cap"] == total, "total")
    require(max(terms, key=terms.get) == "2", "largest stratum")
    require("No quotient plane" in str(data.get("nonclaim")), "nonclaim")
    return {"total": total, "largest": terms["2"]}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("quotient_dimension", 3),
        lambda item: item["parameters"].__setitem__("support_ceiling", 6),
        lambda item: item["parameters"].__setitem__("support_one_label_cap", 3),
        lambda item: item["parameters"]["support_label_caps"].__setitem__("2", 134967),
        lambda item: item["parameters"]["support_incidence_terms"].__setitem__("3", 0),
        lambda item: item["parameters"].__setitem__("per_record_sparse_incidence_cap", result["total"] - 1),
        lambda item: item.__setitem__("nonclaim", "quotient planes included"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (KeyError, Reject, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "hostile mutation rejection")
    print(
        "PASS codimension-two quotient-line sparse circuit cap: "
        f"total {result['total']}, largest {result['largest']}, "
        f"{rejected}/{len(mutations)} hostile mutations"
    )


if __name__ == "__main__":
    main()
