#!/usr/bin/env python3
"""Verify the universal sparse-circuit completion incidence cap."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "0f60be130825abd28548760bada38246758588fbf19da9c627e168bda5894d2b"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def completion_cap(q: int, m: int, support: int) -> tuple[int, int]:
    values = {
        b: b * comb(m - support + 1 - b, 11 - support)
        for b in range(q + 1)
    }
    maximizing = max(values, key=values.get)
    cap = comb(m, support - 1) * values[maximizing] // support
    return cap, maximizing


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-sparse-circuit-universal-completion-incidence-cap-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_sparse_circuit_completion_dimension_ladder"],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("correction_dimension") == 10, "dimension")
    require(p.get("component_subset_size") == 11, "component size")
    require(p.get("supported_circuit_sizes") == list(range(2, 10)), "supports")
    require(p.get("quotient_dimension_formula") == "q=K-10", "quotient")
    require(p.get("completion_ceiling") == "b<=q", "ceiling")
    require(
        p.get("incidence_formula")
        == "floor(C(m,c-1)*max_(0<=b<=q)(b*C(m-c+1-b,11-c))/c)",
        "formula",
    )
    example = p.get("K24_example")
    require(isinstance(example, dict), "example")
    require(example.get("q") == 14 and example.get("m") == 67496, "row")
    rows = {
        str(c): completion_cap(example["q"], example["m"], c)
        for c in range(6, 10)
    }
    require(
        example.get("completion_maximizers")
        == {key: value[1] for key, value in rows.items()},
        "maximizers",
    )
    require(
        example.get("incidence_caps")
        == {key: value[0] for key, value in rows.items()},
        "caps",
    )
    require("No carrier improvement" in str(data.get("nonclaim")), "nonclaim")
    return {"supports": len(p["supported_circuit_sizes"]), "example_total": sum(v[0] for v in rows.values())}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("correction_dimension", 9),
        lambda item: item["parameters"].__setitem__("supported_circuit_sizes", [2, 3]),
        lambda item: item["parameters"].__setitem__("completion_ceiling", "b<q"),
        lambda item: item["parameters"]["K24_example"].__setitem__("q", 13),
        lambda item: item["parameters"]["K24_example"]["completion_maximizers"].__setitem__("6", 13),
        lambda item: item["parameters"]["K24_example"]["incidence_caps"].__setitem__("9", 0),
        lambda item: item.__setitem__("nonclaim", "carrier improvement claimed"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (Reject, KeyError, TypeError, ValueError):
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
        "RATE_HALF_MCA_SPARSE_CIRCUIT_UNIVERSAL_COMPLETION_INCIDENCE_CAP_PASS "
        f"supports={result['supports']} example_total={result['example_total']} "
        f"controls={controls}"
    )


if __name__ == "__main__":
    main()
