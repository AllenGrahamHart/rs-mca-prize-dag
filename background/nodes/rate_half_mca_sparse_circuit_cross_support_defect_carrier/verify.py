#!/usr/bin/env python3
"""Verify the cross-support completion-defect carrier contract."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "f51f62b2198f3477091f4966b76473aa21f49607535b189b75e87c28ecf2ab9c"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def carrier_size(q: int, source: int, target: int, defect: int) -> int:
    return q + source - 1 + defect * (target - 1)


def valid(source: int, target: int, defect: int) -> bool:
    return source + (defect + 1) * target - defect - 1 <= 10


def incidence_cap(q: int, m: int, source: int, target: int, defect: int) -> int:
    return comb(carrier_size(q, source, target, defect), target) * comb(
        m - target, 11 - target
    )


def support5_targets() -> dict[str, list[int]]:
    return {
        str(defect): [target for target in range(2, 10) if valid(5, target, defect)]
        for defect in range(5)
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-sparse-circuit-cross-support-defect-carrier-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_sparse_circuit_universal_completion_incidence_cap"],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("correction_dimension") == 10, "dimension")
    require(p.get("component_size") == 11, "component size")
    require(p.get("support_range") == [2, 9], "support range")
    require(p.get("defect_range") == "0<=s<=q", "defect range")
    require(p.get("completion_count") == "q-s", "completion count")
    require(p.get("carrier_size") == "q+c-1+s(d-1)", "carrier formula")
    require(
        p.get("vandermonde_condition") == "c+(s+1)d-s-1<=10",
        "Vandermonde condition",
    )
    require(
        p.get("incidence_cap") == "C(q+c-1+s(d-1),d)C(m-d,11-d)",
        "incidence formula",
    )
    special = p.get("support5_specialization")
    require(isinstance(special, dict), "specialization")
    require(special.get("maximum_defect") == 4, "maximum defect")
    require(special.get("target_supports") == support5_targets(), "target sets")
    require(special.get("fallback_completion_ceiling") == "q-5", "fallback")

    cases = 0
    for source in range(2, 10):
        for target in range(2, 10):
            for defect in range(10):
                q = defect + 1
                carrier = carrier_size(q, source, target, defect)
                union = carrier + target
                require(
                    valid(source, target, defect) == (union <= q + 10),
                    "condition equivalence",
                )
                if valid(source, target, defect):
                    cap = incidence_cap(q, 100, source, target, defect)
                    require(cap >= 0, "cap")
                    require(
                        (cap > 0) == (carrier >= target),
                        "zero cap exactly when the carrier is too small",
                    )
                cases += 1
    require(
        data.get("logical_pins")
        == [
            "private_completion_coordinates_give_rank_q_minus_s",
            "target_span_needs_at_most_s_additional_labels",
            "carrier_and_target_union_stays_within_K",
            "vandermonde_uniqueness_forces_target_support_into_carrier",
        ],
        "logical pins",
    )
    require("No component payment" in str(data.get("nonclaim")), "nonclaim")
    return {"cases": cases, "special_cases": sum(map(len, support5_targets().values()))}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("correction_dimension", 9),
        lambda item: item["parameters"].__setitem__("support_range", [2, 8]),
        lambda item: item["parameters"].__setitem__("carrier_size", "q+c+s*d"),
        lambda item: item["parameters"].__setitem__("vandermonde_condition", "always"),
        lambda item: item["parameters"]["support5_specialization"]["target_supports"].__setitem__("1", [2, 3, 4]),
        lambda item: item["parameters"]["support5_specialization"].__setitem__("fallback_completion_ceiling", "q-4"),
        lambda item: item.__setitem__("logical_pins", []),
        lambda item: item.__setitem__("nonclaim", "K'=42 paid"),
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
        "RATE_HALF_MCA_SPARSE_CIRCUIT_CROSS_SUPPORT_DEFECT_CARRIER_PASS "
        f"cases={result['cases']} special_cases={result['special_cases']} "
        f"controls={controls}"
    )


if __name__ == "__main__":
    main()
