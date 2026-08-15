#!/usr/bin/env python3
"""Verify the exact deep support-four/support-five defect partition."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "53267e8271a57e087c39ce77a696d93729588d57cd108ffdd279c51bf3192c4b"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def row(q: int) -> dict[str, int]:
    pair_count = (q + 1) ** 2
    joint_count = q * (q + 1) // 2
    other_product = 9 * 8 * 5 * 4 * 3 * 2
    return {
        "q": q,
        "exact_pair_count": pair_count,
        "joint_eligible_pair_count": joint_count,
        "nonjoint_pair_count": pair_count - joint_count,
        "other_support_option_product": other_product,
        "raw_leaf_count": pair_count * other_product,
    }


def contract() -> dict[str, object]:
    return {
        "schema": "rate-half-mca-sparse-circuit-support45-deep-defect-partition-v1",
        "dependencies": [
            "rate_half_mca_sparse_circuit_completion_branch_lattice_refinement",
            "rate_half_mca_sparse_circuit_support45_joint_zero_carrier",
            "rate_half_mca_sparse_circuit_support4_external_charge",
        ],
        "parameters": {
            "source_supports": [4, 5],
            "empty_stratum_convention": "M_c=0",
            "completion_maximum_range": "0<=M_c<=q",
            "exact_defect": "s_c=q-M_c",
            "exact_defect_range": "0<=s_c<=q",
            "exact_pair_count": "(q+1)^2",
            "joint_condition": "s_4+s_5<q",
            "joint_pair_count": "q(q+1)/2",
            "source_cap": "floor(C(m,c-1)max_(0<=b<=q-s_c)bC(m-c+1-b,11-c)/c)",
            "pareto_rule": "discard a only if another b satisfies a_c<=b_c for every support",
            "rows": {str(q + 10): row(q) for q in range(36, 45)},
        },
        "claim": (
            "Exact deep defects at supports four and five preserve every inherited cap "
            "and expose the joint charge whenever s_4+s_5<q."
        ),
        "nonclaim": "No row, rank-eight, rank-eleven, KoalaBear, or prize closure is asserted.",
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    expected = contract()
    require(data == expected, "exact contract")
    p = data["parameters"]
    require(isinstance(p, dict), "parameters")
    rows = p["rows"]
    require(isinstance(rows, dict), "rows")
    require(rows["46"]["raw_leaf_count"] == 11828160, "K46 leaves")
    require(rows["54"]["raw_leaf_count"] == 17496000, "K54 leaves")
    return {"rows": len(rows), "first_leaves": rows["46"]["raw_leaf_count"]}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("source_supports", [4]),
        lambda item: item["parameters"].__setitem__("joint_condition", "s_4+s_5<=q"),
        lambda item: item["parameters"]["rows"]["46"].__setitem__("exact_pair_count", 0),
        lambda item: item["parameters"]["rows"]["54"].__setitem__("raw_leaf_count", 0),
        lambda item: item.__setitem__("nonclaim", "K'=54 closed"),
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
        "RATE_HALF_MCA_SPARSE_CIRCUIT_SUPPORT45_DEEP_DEFECT_PARTITION_PASS "
        f"rows={result['rows']} first_leaves={result['first_leaves']} controls={controls}"
    )


if __name__ == "__main__":
    main()
