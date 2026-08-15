#!/usr/bin/env python3
"""Verify the completion-branch lattice refinement contract."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "af8bfd54a653a1fe0c0d4bb05a5dde740d6a365924f4240de79fb59616b605be"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def classify(maximum: int, q: int, source: int) -> str:
    require(0 <= maximum <= q, "maximum range")
    defect = q - maximum
    if defect <= 9 - source:
        return f"defect_{defect}"
    return "fallback"


def carrier_valid(source: int, target: int, defect: int) -> bool:
    return source + (defect + 1) * target - defect - 1 <= 10


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-sparse-circuit-completion-branch-lattice-refinement-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_sparse_circuit_cross_support_defect_carrier",
            "rate_half_mca_sparse_circuit_descending_support_completion_ladder",
        ],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("correction_dimension") == 10, "dimension")
    require(p.get("minimum_quotient_dimension") == 8, "minimum q")
    require(p.get("source_support_range") == [2, 9], "source range")
    require(p.get("terminal_defects") == "0<=s<=9-c", "defects")
    require(p.get("fallback_ceiling") == "q-(10-c)", "fallback")
    require(p.get("carrier_condition") == "c+(s+1)d-s-1<=10", "condition")
    require(p.get("carrier_size") == "q+c-1+s(d-1)", "carrier")
    require(p.get("replacement_leaf_count") == "11-c", "leaf formula")
    require(
        p.get("support6_specialization")
        == {
            "terminal_defects": [0, 1, 2, 3],
            "fallback_ceiling": "q-4",
            "replacement_leaf_count": 5,
        },
        "support-six specialization",
    )

    partition_checks = 0
    carrier_checks = 0
    for q in (8, 11, 34):
        for source in range(2, 10):
            labels = {classify(maximum, q, source) for maximum in range(q + 1)}
            require(len(labels) == 11 - source, "leaf count")
            require("fallback" in labels, "fallback attained")
            for defect in range(10 - source):
                require(f"defect_{defect}" in labels, "terminal attained")
                for target in range(2, 10):
                    carrier_without_q = source - 1 + defect * (target - 1)
                    require(
                        carrier_valid(source, target, defect)
                        == (carrier_without_q + target <= 10),
                        "carrier union equivalence",
                    )
                    carrier_checks += 1
            partition_checks += q + 1
    require(
        data.get("logical_pins")
        == [
            "terminal_defects_and_fallback_partition_the_parent_leaf",
            "all_parent_caps_are_inherited_by_every_child",
            "new_caps_are_intersections_with_inherited_caps",
            "refinement_can_be_repeated_on_selected_leaves",
        ],
        "logical pins",
    )
    require("No weighted maximum" in str(data.get("nonclaim")), "nonclaim")
    return {"partition_checks": partition_checks, "carrier_checks": carrier_checks}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("source_support_range", [2, 8]),
        lambda item: item["parameters"].__setitem__("fallback_ceiling", "q-(9-c)"),
        lambda item: item["parameters"].__setitem__("replacement_leaf_count", "10-c"),
        lambda item: item["parameters"]["support6_specialization"].__setitem__("replacement_leaf_count", 4),
        lambda item: item.__setitem__("logical_pins", []),
        lambda item: item.__setitem__("nonclaim", "K'=44 paid"),
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
        "RATE_HALF_MCA_SPARSE_CIRCUIT_COMPLETION_BRANCH_LATTICE_REFINEMENT_PASS "
        f"partition_checks={result['partition_checks']} "
        f"carrier_checks={result['carrier_checks']} controls={controls}"
    )


if __name__ == "__main__":
    main()
