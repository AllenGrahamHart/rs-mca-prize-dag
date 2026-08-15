#!/usr/bin/env python3
"""Verify the fixed-union multicarrier collision charge."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "5c635f5606250742ee39155a55eb6cbf33ea3546ce8599bfaf2b2a9d8c642b32"
CASES = {
    "K71_T23": (71, 67543, 62, 7),
    "K71_A23": (71, 67543, 61, 8),
    "K71_T24": (71, 67543, 63, 6),
    "K71_N34": (71, 67543, 35, 6),
    "K71_N34A": (71, 67543, 34, 7),
}


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def target_count(K: int, m: int, union: int, dimension: int, target: int) -> int:
    intersection = dimension + 1 - target
    require(intersection > 0, "positive intersection")
    outside_budget = K - intersection - union
    outside = m - union
    return comb(union, target) + sum(
        comb(union, target - external)
        * comb(outside, external - 1)
        * max(0, outside_budget - external + 1)
        // external
        for external in range(1, target + 1)
    )


def incidence_cap(K: int, m: int, union: int, dimension: int, target: int) -> int:
    return target_count(K, m, union, dimension, target) * comb(
        m - target, 11 - target
    )


def contract() -> dict[str, object]:
    samples = {}
    for name, (K, m, union, dimension) in CASES.items():
        samples[name] = {
            "K": K,
            "m": m,
            "union_size": union,
            "fixed_dimension": dimension,
            "targets": {
                str(target): {
                    "intersection_dimension": dimension + 1 - target,
                    "outside_budget": K - (dimension + 1 - target) - union,
                    "target_support_count": target_count(
                        K, m, union, dimension, target
                    ),
                    "target_incidence_cap": incidence_cap(
                        K, m, union, dimension, target
                    ),
                }
                for target in range(2, min(9, dimension) + 1)
            },
        }
    return {
        "schema": "rate-half-mca-sparse-circuit-multicarrier-collision-charge-v1",
        "dependencies": [
            "rate_half_mca_sparse_circuit_cross_support_collision_charge"
        ],
        "parameters": {
            "correction_dimension": 10,
            "intersection_dimension": "r_d=g+1-d",
            "outside_budget": "R_d=K-r_d-u",
            "inside_count": "C(u,d)",
            "outside_stratum_count": (
                "floor(C(u,d-j)C(m-u,j-1)max(0,R_d-j+1)/j)"
            ),
            "incidence_multiplier": "C(m-d,11-d)",
            "K71_samples": samples,
        },
        "claim": (
            "A fixed g-dimensional vanishing space on a fixed u-point "
            "union gives exact target-circuit and selected-incidence caps "
            "whenever g+1-d>0."
        ),
        "nonclaim": (
            "The theorem does not construct the fixed union or permit "
            "deletion-dependent unions to be combined."
        ),
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data == contract(), "exact contract")
    samples = data["parameters"]["K71_samples"]
    checks = 0
    for name, (K, m, union, dimension) in CASES.items():
        row = samples[name]
        require(row["union_size"] == union, "union")
        require(row["fixed_dimension"] == dimension, "dimension")
        for target in range(2, min(9, dimension) + 1):
            value = row["targets"][str(target)]
            require(value["intersection_dimension"] == dimension + 1 - target > 0, "intersection")
            require(value["outside_budget"] == K - (dimension + 1 - target) - union, "outside")
            require(value["target_support_count"] == target_count(K, m, union, dimension, target), "count")
            require(value["target_incidence_cap"] == incidence_cap(K, m, union, dimension, target), "incidence")
            checks += 1
    require("does not construct" in str(data["nonclaim"]), "nonclaim")
    return {"cases": len(CASES), "checks": checks}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("correction_dimension", 11),
        lambda item: item["parameters"].__setitem__("intersection_dimension", "g-d"),
        lambda item: item["parameters"].__setitem__("outside_budget", "K-u"),
        lambda item: item["parameters"]["K71_samples"]["K71_T23"].__setitem__("union_size", 61),
        lambda item: item["parameters"]["K71_samples"]["K71_N34"]["targets"]["6"].__setitem__("target_incidence_cap", 0),
        lambda item: item.__setitem__("nonclaim", "all unions may be combined"),
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
    result = validate(json.loads(raw))
    controls = tamper_selftest(json.loads(raw))
    print(
        "RATE_HALF_MCA_SPARSE_CIRCUIT_MULTICARRIER_COLLISION_CHARGE_PASS "
        f"cases={result['cases']} checks={result['checks']} controls={controls}"
    )


if __name__ == "__main__":
    main()
