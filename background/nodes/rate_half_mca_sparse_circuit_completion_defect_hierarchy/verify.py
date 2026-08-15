#!/usr/bin/env python3
"""Verify the sparse-circuit completion-defect hierarchy."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "c09209dd879b2845e237915ebc9282fb8218e452833b5d810cf52b6813a0b4fa"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def row(q: int, m: int, support: int, depth: int) -> dict[str, object]:
    carrier_caps = {
        defect: comb(q + (defect + 1) * (support - 1), support)
        * comb(m - support, 11 - support)
        for defect in range(1, depth + 1)
    }
    ceiling = q - depth - 1
    values = {
        completions: completions
        * comb(m - support + 1 - completions, 11 - support)
        for completions in range(ceiling + 1)
    }
    maximizing = max(values, key=values.get)
    deletion = comb(m, support - 1) * values[maximizing] // support
    carrier = max(carrier_caps.values(), default=0)
    return {
        "carrier_caps": carrier_caps,
        "deletion": deletion,
        "maximizing": maximizing,
        "active": max(carrier, deletion),
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-sparse-circuit-completion-defect-hierarchy-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_sparse_circuit_near_saturation_carrier"],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    depths = {2: 7, 3: 2, 4: 1, 5: 0}
    require(p.get("depths") == {str(key): value for key, value in depths.items()}, "depths")
    require(
        p.get("carrier_size_formula") == "q+(s+1)(c-1)",
        "carrier formula",
    )
    require(
        p.get("vandermonde_condition") == "(s+2)c-s-1<=10",
        "Vandermonde condition",
    )
    require(
        all(
            (depth + 2) * support - depth - 1 <= 10
            for support, depth in depths.items()
            if depth > 0
        ),
        "valid terminal depths",
    )
    require(
        all(
            (depth + 3) * support - depth - 2 > 10
            for support, depth in depths.items()
        ),
        "maximal depths",
    )

    k23 = p.get("K23")
    require(isinstance(k23, dict), "K23")
    q = k23.get("q")
    m = k23.get("m")
    require(q == 13 and m == 67495, "row parameters")
    rows = {
        str(support): row(q, m, support, depth)
        for support, depth in depths.items()
    }
    require(
        k23.get("completion_maximizers")
        == {key: value["maximizing"] for key, value in rows.items()},
        "completion maximizers",
    )
    require(
        k23.get("active_caps") == {key: value["active"] for key, value in rows.items()},
        "active caps",
    )
    require(all(value["deletion"] == value["active"] for value in rows.values()), "active branch")
    weights = {"2": 26, "3": 18, "4": 11, "5": 5}
    require(k23.get("premium_weights") == weights, "weights")
    premium = sum(weights[key] * value["active"] for key, value in rows.items())
    require(k23.get("weighted_premium") == premium, "premium")
    require("No stronger support-five cap" in str(data.get("nonclaim")), "nonclaim")
    return {"supports": len(rows), "branches": sum(len(value["carrier_caps"]) for value in rows.values()), "premium": premium}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"]["depths"].__setitem__("2", 8),
        lambda item: item["parameters"].__setitem__("carrier_size_formula", "q+s(c-1)"),
        lambda item: item["parameters"]["K23"].__setitem__("q", 12),
        lambda item: item["parameters"]["K23"]["completion_maximizers"].__setitem__("3", 11),
        lambda item: item["parameters"]["K23"]["active_caps"].__setitem__("2", 0),
        lambda item: item["parameters"]["K23"].__setitem__("weighted_premium", 0),
        lambda item: item.__setitem__("nonclaim", "support five improved"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (Reject, KeyError, TypeError):
            rejected += 1
    require(rejected == len(mutations), "tamper controls")
    return rejected


def main() -> None:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    controls = tamper_selftest(data)
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_COMPLETION_DEFECT_HIERARCHY_PASS "
        f"supports={result['supports']} branches={result['branches']} "
        f"premium={result['premium']} controls={controls}"
    )


if __name__ == "__main__":
    main()
