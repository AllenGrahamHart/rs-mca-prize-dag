#!/usr/bin/env python3
"""Verify the sparse-circuit completion dimension ladder."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "25bbeb3c2124f34399659550c214400bc6afe4ce9d5ee615939241e2e94c298b"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def structured_terms(kprime: int) -> dict[str, int]:
    q = kprime - 10
    m = 67472 + kprime
    return {
        str(support): comb(q + 4, support) * comb(m - support, 11 - support)
        for support in range(2, 6)
    }


def completion_value(m: int, support: int, completions: int) -> int:
    return completions * comb(
        m - support + 1 - completions,
        11 - support,
    )


def unstructured_terms(kprime: int) -> tuple[dict[str, int], dict[str, int]]:
    q = kprime - 10
    m = 67472 + kprime
    terms: dict[str, int] = {}
    maximizers: dict[str, int] = {}
    for support in range(2, 6):
        value, completions = max(
            (completion_value(m, support, b), b)
            for b in range(q)
        )
        terms[str(support)] = comb(m, support - 1) * value // support
        maximizers[str(support)] = completions
    return terms, maximizers


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-sparse-circuit-completion-dimension-ladder-v1",
        "schema",
    )
    require(data.get("dependencies") == [], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["correction_dimension"] == 10, "correction dimension")
    require(p["component_subset_size"] == 11, "component size")
    require((p["support_minimum"], p["support_ceiling"]) == (2, 5), "support")
    require(p["global_common_zero_count"] == 0, "basepoint free")
    require(p["quotient_dimension_formula"] == "q=K_prime-10", "quotient formula")
    require(p["completion_ceiling_formula"] == "q", "completion ceiling")
    require(p["unstructured_completion_ceiling_formula"] == "q-1", "unstructured ceiling")
    require(p["structured_carrier_ceiling_formula"] == "q+4", "carrier ceiling")
    require(p["official_K_prime_interval"] == [14, 21], "official interval")
    require(p["official_unstructured_maximizer_formula"] == "b=q-1", "maximizer formula")

    endpoint_totals: dict[str, dict[str, int]] = {}
    support_checks = 0
    for kprime in range(14, 22):
        q = kprime - 10
        structured = structured_terms(kprime)
        unstructured, maximizers = unstructured_terms(kprime)
        require(set(maximizers.values()) == {q - 1}, f"K'={kprime} maximizers")
        require(sum(unstructured.values()) > sum(structured.values()), f"K'={kprime} active branch")
        support_checks += len(structured) + len(unstructured)
        if kprime in (14, 21):
            endpoint_totals[str(kprime)] = {
                "structured": sum(structured.values()),
                "unstructured": sum(unstructured.values()),
            }
    require(p["endpoint_totals"] == endpoint_totals, "endpoint totals")
    require("No aggregate rank-nine" in str(data.get("nonclaim")), "nonclaim")
    return {
        "support_checks": support_checks,
        "k14_unstructured": endpoint_totals["14"]["unstructured"],
        "k21_unstructured": endpoint_totals["21"]["unstructured"],
    }


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("correction_dimension", 9),
        lambda item: item["parameters"].__setitem__("global_common_zero_count", 1),
        lambda item: item["parameters"].__setitem__("completion_ceiling_formula", "q+1"),
        lambda item: item["parameters"].__setitem__("unstructured_completion_ceiling_formula", "q"),
        lambda item: item["parameters"].__setitem__("structured_carrier_ceiling_formula", "q+5"),
        lambda item: item["parameters"].__setitem__("official_K_prime_interval", [14, 20]),
        lambda item: item["parameters"].__setitem__("official_unstructured_maximizer_formula", "b=q"),
        lambda item: item["parameters"]["endpoint_totals"]["14"].__setitem__("structured", 0),
        lambda item: item["parameters"]["endpoint_totals"]["21"].__setitem__("unstructured", 0),
        lambda item: item.__setitem__("nonclaim", "all rows paid"),
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
        "PASS sparse-circuit completion dimension ladder primary: "
        f"{result['support_checks']} support checks, "
        f"K14 {result['k14_unstructured']}, K21 {result['k21_unstructured']}, "
        f"{rejected}/{len(mutations)} hostile mutations"
    )


if __name__ == "__main__":
    main()
