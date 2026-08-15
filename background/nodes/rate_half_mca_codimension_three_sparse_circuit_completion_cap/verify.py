#!/usr/bin/env python3
"""Verify the codimension-three sparse-circuit completion cap."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "87d1bd00338c62a01640e593eec40d0cec20c8e8cbde2c138b482958a458c7e5"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def structured_cap(m: int) -> int:
    return sum(comb(7, support) * comb(m - support, 11 - support)
               for support in range(2, 6))


def unstructured_terms(m: int) -> dict[str, int]:
    return {
        str(support): (
            2 * comb(m, support - 1) * comb(m - support - 1, 11 - support)
            // support
        )
        for support in range(2, 6)
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-codimension-three-sparse-circuit-completion-cap-v1",
        "schema",
    )
    require(data.get("dependencies") == [], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(
        (p["ambient_polynomial_dimension"], p["correction_dimension"],
         p["quotient_dimension"]) == (13, 10, 3),
        "dimensions",
    )
    require(p["component_subset_size"] == 11, "component size")
    require((p["support_minimum"], p["support_ceiling"]) == (2, 5), "support range")
    require(p["global_common_zero_count"] == 0, "basepoint free")
    require(p["completion_ceiling"] == 3, "completion ceiling")
    require(p["unstructured_completion_ceiling"] == 2, "unstructured ceiling")
    require(p["structured_carrier_ceiling"] == 7, "carrier ceiling")
    m = int(p["official_support_size"])
    require(m == 67485, "official support")

    structured = structured_cap(m)
    terms = unstructured_terms(m)
    unstructured = sum(terms.values())
    require(p["structured_carrier_cap"] == structured, "structured cap")
    require(p["unstructured_support_terms"] == terms, "unstructured terms")
    require(p["unstructured_completion_cap"] == unstructured, "unstructured cap")
    require(unstructured > structured, "active branch")
    require(p["per_record_sparse_incidence_cap"] == unstructured, "official cap")
    require(all(
        2 * comb(m - support - 1, 11 - support)
        >= comb(m - support, 11 - support)
        for support in range(2, 6)
    ), "two-completion maximizer")
    require("No support above five" in str(data.get("nonclaim")), "nonclaim")
    return {"structured": structured, "unstructured": unstructured}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("quotient_dimension", 2),
        lambda item: item["parameters"].__setitem__("global_common_zero_count", 1),
        lambda item: item["parameters"].__setitem__("completion_ceiling", 4),
        lambda item: item["parameters"].__setitem__("unstructured_completion_ceiling", 3),
        lambda item: item["parameters"].__setitem__("structured_carrier_ceiling", 8),
        lambda item: item["parameters"].__setitem__("structured_carrier_cap", result["structured"] - 1),
        lambda item: item["parameters"]["unstructured_support_terms"].__setitem__("4", 0),
        lambda item: item["parameters"].__setitem__("unstructured_completion_cap", result["unstructured"] - 1),
        lambda item: item["parameters"].__setitem__("per_record_sparse_incidence_cap", result["unstructured"] - 1),
        lambda item: item.__setitem__("nonclaim", "all quotient dimensions included"),
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
        "PASS codimension-three sparse circuit completion cap: "
        f"structured {result['structured']}, unstructured {result['unstructured']}, "
        f"{rejected}/{len(mutations)} hostile mutations"
    )


if __name__ == "__main__":
    main()
