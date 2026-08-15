#!/usr/bin/env python3
"""Verify the descending-support completion ladder contract."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "b2a9f966a819fbc77724775722e7a35695dadc14daae67c6271e9eec5809ac7b"
SOURCE_ORDER = (5, 4, 3, 2)


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def defects(source: int) -> list[int]:
    return list(range(10 - source))


def fallback_ceiling(source: int) -> str:
    return f"q-{10 - source}"


def carrier_valid(source: int, target: int, defect: int) -> bool:
    return source + (defect + 1) * target - defect - 1 <= 10


def classify(maxima: dict[int, int], q: int) -> str:
    for source in SOURCE_ORDER:
        maximum = maxima[source]
        require(0 <= maximum <= q, "completion maximum range")
        defect = q - maximum
        if defect <= 9 - source:
            return f"c{source}_defect_{defect}"
    return "all_fallback"


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-sparse-circuit-descending-support-completion-ladder-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_sparse_circuit_cross_support_defect_carrier"],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("correction_dimension") == 10, "dimension")
    require(p.get("minimum_quotient_dimension") == 8, "minimum q")
    require(p.get("source_order") == list(SOURCE_ORDER), "source order")
    require(
        p.get("terminal_defects")
        == {str(source): defects(source) for source in SOURCE_ORDER},
        "defects",
    )
    require(
        p.get("fallback_ceilings")
        == {str(source): fallback_ceiling(source) for source in SOURCE_ORDER},
        "fallback ceilings",
    )
    require(p.get("carrier_condition") == "c+(s+1)d-s-1<=10", "condition")
    require(p.get("carrier_size") == "q+c-1+s(d-1)", "carrier")
    terminal_count = sum(len(defects(source)) for source in SOURCE_ORDER)
    require(p.get("terminal_branch_count") == terminal_count == 26, "terminal count")
    require(p.get("all_fallback_branch_count") == 1, "fallback count")
    require(p.get("total_leaf_count") == terminal_count + 1 == 27, "leaf count")

    partition_checks = 0
    seen = set()
    q = 8
    for m5 in range(q + 1):
        for m4 in range(q + 1):
            for m3 in range(q + 1):
                for m2 in range(q + 1):
                    label = classify({5: m5, 4: m4, 3: m3, 2: m2}, q)
                    seen.add(label)
                    partition_checks += 1
    require(len(seen) == 27 and "all_fallback" in seen, "all leaves attained")

    carrier_checks = 0
    for source in SOURCE_ORDER:
        for defect in defects(source):
            for target in range(2, 10):
                q = 8
                carrier = q + source - 1 + defect * (target - 1)
                require(
                    carrier_valid(source, target, defect)
                    == (carrier + target <= q + 10),
                    "carrier union equivalence",
                )
                carrier_checks += 1
    require(
        data.get("logical_pins")
        == [
            "each_completion_maximum_is_an_integer_between_zero_and_q",
            "terminal_defects_and_fallback_partition_each_stage",
            "fallback_ceilings_persist_down_the_ladder",
            "carrier_caps_are_used_only_on_terminal_valid_targets",
        ],
        "logical pins",
    )
    require("No weighted premium" in str(data.get("nonclaim")), "nonclaim")
    return {"partition_checks": partition_checks, "carrier_checks": carrier_checks}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("source_order", [5, 3, 2]),
        lambda item: item["parameters"]["terminal_defects"].__setitem__("4", [0, 1]),
        lambda item: item["parameters"]["fallback_ceilings"].__setitem__("2", "q-7"),
        lambda item: item["parameters"].__setitem__("total_leaf_count", 26),
        lambda item: item.__setitem__("logical_pins", []),
        lambda item: item.__setitem__("nonclaim", "K'=43 paid"),
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
    result = validate(json.loads(raw))
    controls = tamper_selftest(json.loads(raw))
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_DESCENDING_SUPPORT_COMPLETION_LADDER_PASS "
        f"partition_checks={result['partition_checks']} "
        f"carrier_checks={result['carrier_checks']} controls={controls}"
    )


if __name__ == "__main__":
    main()
