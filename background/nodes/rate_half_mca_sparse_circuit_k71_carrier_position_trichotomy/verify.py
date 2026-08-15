#!/usr/bin/env python3
"""Verify the support-2/3/4 carrier-position trichotomy metadata."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "45df072823fad4f85ce8ed08bd32b1a1f03202b6b397f9644078593a75071c4e"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def six_cases(completion2: int) -> dict[str, dict[str, int]]:
    b2 = completion2 + 1
    b3 = completion2 + 3
    b4 = completion2 + 4
    return {
        "T23": {"union_size": b2 + b3, "fixed_dimension": 7},
        "A23": {"union_size": b2 + b3 - 1, "fixed_dimension": 8},
        "T24": {"union_size": b2 + b4, "fixed_dimension": 6},
        "A24": {"union_size": b2 + b4 - 1, "fixed_dimension": 7},
        "N34": {"union_size": b2 + 5, "fixed_dimension": 6},
        "N34A": {"union_size": b2 + 4, "fixed_dimension": 7},
    }


def contract() -> dict[str, object]:
    q = 61
    impossible = [
        [s2, s3]
        for s2 in range(q)
        for s3 in range(q)
        if q - s3 <= q - s2 and s2 + s3 < q
    ]
    impossible_digest = hashlib.sha256(
        "".join(f"{s2},{s3}\n" for s2, s3 in impossible).encode()
    ).hexdigest()
    return {
        "schema": "rate-half-mca-sparse-circuit-k71-carrier-position-trichotomy-v1",
        "dependencies": [
            "rate_half_mca_sparse_circuit_cross_support_collision_charge",
            "rate_half_mca_sparse_circuit_multicarrier_collision_charge",
        ],
        "parameters": {
            "correction_dimension": 10,
            "support2_carrier": "full nonzero parallel class of size M2+1",
            "positions": ["transverse", "proper_span", "full_completion"],
            "transverse_fixed_dimension": "10-c",
            "proper_span_fixed_dimension": "11-c",
            "full_completion_necessary_condition": "Mc>=M2+1",
            "support23_pruning_condition": "M3<=M2",
            "support23_impossible_condition": "s2+s3<q",
            "K71_impossible_defect_pair_count": len(impossible),
            "K71_impossible_defect_pair_digest_sha256": impossible_digest,
            "one_step_condition": "M3=M4=M2+1",
            "K71_active_completions": {"M2": 29, "M3": 30, "M4": 30},
            "K71_cases": six_cases(29),
            "nested_anchor_intersection_sizes": [0, 1],
        },
        "claim": (
            "The support-two projective point has an exhaustive position "
            "relative to the support-three and support-four attaining "
            "deletions, yielding the six fixed-union cases."
        ),
        "nonclaim": (
            "A completion carrier is not asserted to equal the full "
            "ground-set intersection with its projective flat."
        ),
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data == contract(), "exact contract")
    p = data["parameters"]
    require(p["positions"] == ["transverse", "proper_span", "full_completion"], "positions")
    require(p["K71_impossible_defect_pair_count"] == 961, "impossible census")
    require(
        p["K71_impossible_defect_pair_digest_sha256"]
        == "07931c53bb2dd546e5a671fa59592ede3f153a422dbb1b033d38ffb00668edab",
        "impossible digest",
    )
    require(p["nested_anchor_intersection_sizes"] == [0, 1], "nested anchors")
    cases = p["K71_cases"]
    expected = {
        "T23": (62, 7),
        "A23": (61, 8),
        "T24": (63, 6),
        "A24": (62, 7),
        "N34": (35, 6),
        "N34A": (34, 7),
    }
    for name, (union, dimension) in expected.items():
        require(cases[name]["union_size"] == union, f"{name} union")
        require(cases[name]["fixed_dimension"] == dimension, f"{name} dimension")
    require("not asserted" in str(data["nonclaim"]), "nonclaim")
    return {"impossible": 961, "cases": len(cases)}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("positions", ["nested"]),
        lambda item: item["parameters"].__setitem__("full_completion_necessary_condition", "Mc>=M2"),
        lambda item: item["parameters"].__setitem__("K71_impossible_defect_pair_count", 0),
        lambda item: item["parameters"]["K71_cases"]["N34"].__setitem__("union_size", 34),
        lambda item: item["parameters"].__setitem__("nested_anchor_intersection_sizes", [0, 1, 2]),
        lambda item: item.__setitem__("nonclaim", "carriers are full flats"),
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
        "RATE_HALF_MCA_SPARSE_CIRCUIT_K71_CARRIER_POSITION_TRICHOTOMY_PASS "
        f"impossible={result['impossible']} cases={result['cases']} controls={controls}"
    )


if __name__ == "__main__":
    main()
