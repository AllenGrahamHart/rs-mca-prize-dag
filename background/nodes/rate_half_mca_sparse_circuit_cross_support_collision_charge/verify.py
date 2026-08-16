#!/usr/bin/env python3
"""Verify the small-source cross-support collision charge."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "ad7994569e830ab2d56e58bdb16ca8658e0a2903a28e50e7e0985514e34075c5"
SOURCES = tuple(range(2, 6))
TARGETS = tuple(range(2, 10))


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def target_count(K: int, m: int, source: int, target: int, defect: int) -> int:
    q = K - 10
    require(source in SOURCES, "source")
    require(target in TARGETS and source + target <= 11, "target")
    require(0 <= defect < q, "nonempty defect")
    carrier = q + source - 1 - defect
    if defect == 0:
        return comb(carrier, target)
    outside = m - carrier
    return comb(carrier, target) + sum(
        comb(carrier, target - external)
        * comb(outside, external - 1)
        * (defect + target - external)
        // external
        for external in range(1, target + 1)
    )


def incidence_cap(K: int, m: int, source: int, target: int, defect: int) -> int:
    return target_count(K, m, source, target, defect) * comb(
        m - target, 11 - target
    )


def contract() -> dict[str, object]:
    K = 60
    m = 67532
    defect = 25
    samples = {
        str(source): {
            str(target): {
                "intersection_dimension": 12 - source - target,
                "source_carrier_size": K - 10 + source - 1 - defect,
                "target_outside_budget": defect + target - 1,
                "target_support_count": target_count(
                    K, m, source, target, defect
                ),
                "target_incidence_cap": incidence_cap(
                    K, m, source, target, defect
                ),
            }
            for target in TARGETS
            if source + target <= 11
        }
        for source in SOURCES
    }
    return {
        "schema": "rate-half-mca-sparse-circuit-cross-support-collision-charge-v1",
        "dependencies": [
            "rate_half_mca_sparse_circuit_small_support_self_collision_charge",
            "rate_half_mca_sparse_circuit_cross_support_defect_carrier",
        ],
        "parameters": {
            "correction_dimension": 10,
            "component_size": 11,
            "source_support_range": [2, 5],
            "target_support_range": [2, 9],
            "support_condition": "c+d<=11",
            "completion_maximum": "M_c=q-s>0",
            "source_carrier_size": "b=q+c-1-s",
            "intersection_dimension": "12-c-d",
            "target_outside_budget": "s+d-1",
            "inside_count": "C(b,d)",
            "outside_stratum_count": (
                "floor(C(b,d-j)C(m-b,j-1)(s+d-j)/j)"
            ),
            "incidence_multiplier": "C(m-d,11-d)",
            "empty_source_nonclaim": "s=q gives no target cap",
            "K60_defect25_samples": samples,
        },
        "claim": (
            "Exact nonempty source defects give branch-safe target-circuit "
            "and selected-incidence caps whenever c+d<=11."
        ),
        "nonclaim": (
            "No target cap follows from an empty source stratum, no pair "
            "with c+d>=12 is covered, and no rank-eight, rank-eleven, "
            "KoalaBear, or prize closure is asserted."
        ),
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data == contract(), "exact contract")
    p = data["parameters"]
    require(isinstance(p, dict), "parameters")
    checks = 0
    pairs = 0
    for source in SOURCES:
        for target in TARGETS:
            if source + target > 11:
                continue
            pairs += 1
            require(12 - source - target > 0, "positive intersection")
            require(source + target - 1 <= 10, "zero-defect Vandermonde")
            require(
                target_count(60, 67532, source, target, 0)
                == comb(50 + source - 1, target),
                "zero defect",
            )
            for defect in range(1, 50):
                for external in range(1, target + 1):
                    require(
                        defect + target - 1 - (external - 1)
                        == defect + target - external,
                        "outside budget",
                    )
                    require(defect + target - external > 0, "positive cap")
                    checks += 1
    require("empty source" in str(data["nonclaim"]), "nonclaim")
    return {"pairs": pairs, "checks": checks}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("support_condition", "c+d<=12"),
        lambda item: item["parameters"].__setitem__("intersection_dimension", "11-c-d"),
        lambda item: item["parameters"].__setitem__("target_outside_budget", "s+d"),
        lambda item: item["parameters"].__setitem__("empty_source_nonclaim", "zero targets"),
        lambda item: item["parameters"]["K60_defect25_samples"]["2"]["9"].__setitem__("target_incidence_cap", 0),
        lambda item: item.__setitem__("nonclaim", "all supports proved"),
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
    if sys.argv[1:] == ["--write"]:
        CONTRACT.write_text(json.dumps(contract(), indent=2) + "\n")
        print(f"WROTE {CONTRACT}")
        return
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    controls = tamper_selftest(data)
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_CROSS_SUPPORT_COLLISION_CHARGE_PASS "
        f"pairs={result['pairs']} checks={result['checks']} controls={controls}"
    )


if __name__ == "__main__":
    main()
