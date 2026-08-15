#!/usr/bin/env python3
"""Verify the near-saturated sparse-circuit caps."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "03da7712fdd01435cb12f7d0c2afc96d3fadd39f9270152980cc44c79075f38b"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def caps(q: int, m: int, support: int) -> dict[str, int]:
    carrier = comb(q + 2 * support - 2, support) * comb(
        m - support, 11 - support
    )
    values = {
        completions: completions
        * comb(m - support + 1 - completions, 11 - support)
        for completions in range(q - 1)
    }
    maximizing_completions = max(values, key=values.get)
    fallback = comb(m, support - 1) * values[maximizing_completions] // support
    old = (
        comb(m, support - 1)
        * (q - 1)
        * comb(m - support + 2 - q, 11 - support)
        // support
    )
    return {
        "carrier": carrier,
        "fallback": fallback,
        "active": max(carrier, fallback),
        "old": old,
        "maximizing_completions": maximizing_completions,
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-sparse-circuit-near-saturation-carrier-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_sparse_circuit_completion_dimension_ladder"],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("support_interval") == [2, 4], "support interval")
    require(p.get("carrier_size_formula") == "q+2c-2", "carrier formula")
    require(p.get("vandermonde_union_formula") == "q+3c-2", "union formula")
    require(all(3 * support - 2 <= 10 for support in range(2, 5)), "Vandermonde range")
    require(3 * 5 - 2 > 10, "support-five boundary")

    k22 = p.get("K22")
    require(isinstance(k22, dict), "K22")
    q = k22.get("q")
    m = k22.get("m")
    require(q == 12 and m == 67494, "K22 parameters")
    rows = {str(c): caps(q, m, c) for c in range(2, 5)}
    require(
        k22.get("active_caps") == {key: value["active"] for key, value in rows.items()},
        "active caps",
    )
    require(
        k22.get("old_q_minus_1_caps") == {key: value["old"] for key, value in rows.items()},
        "old caps",
    )
    require(all(value["fallback"] > value["carrier"] for value in rows.values()), "active branch")
    require(
        all(value["maximizing_completions"] == q - 2 for value in rows.values()),
        "completion maximizer",
    )
    weights = {"2": 26, "3": 18, "4": 11}
    require(k22.get("premium_weights") == weights, "weights")
    saving = sum(
        weights[key] * (value["old"] - value["active"])
        for key, value in rows.items()
    )
    require(k22.get("weighted_premium_saving") == saving, "saving")
    require("No support-five improvement" in str(data.get("nonclaim")), "nonclaim")
    return {"supports": len(rows), "saving": saving}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("support_interval", [2, 5]),
        lambda item: item["parameters"].__setitem__("carrier_size_formula", "q+2c-3"),
        lambda item: item["parameters"]["K22"].__setitem__("q", 11),
        lambda item: item["parameters"]["K22"]["active_caps"].__setitem__("4", 0),
        lambda item: item["parameters"]["K22"]["old_q_minus_1_caps"].__setitem__("2", 0),
        lambda item: item["parameters"]["K22"].__setitem__("weighted_premium_saving", 0),
        lambda item: item.__setitem__("nonclaim", "support five closed"),
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
        "RATE_HALF_MCA_SPARSE_CIRCUIT_NEAR_SATURATION_CARRIER_PASS "
        f"supports={result['supports']} saving={result['saving']} controls={controls}"
    )


if __name__ == "__main__":
    main()
