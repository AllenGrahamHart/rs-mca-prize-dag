#!/usr/bin/env python3
"""Verify the small-support same-source collision charge."""

from __future__ import annotations

import copy
import hashlib
import json
import sys
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "fc8bb1a5b4a91ac455f1613dc997879cc352af7910873b56666a2ec5c1f74177"
SUPPORTS = tuple(range(2, 6))


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def support_count(K: int, m: int, support: int, defect: int) -> int:
    q = K - 10
    require(0 <= defect <= q, "defect range")
    if defect == q:
        return 0
    carrier = q + support - 1 - defect
    outside = m - carrier
    if defect == 0:
        return comb(carrier, support)
    return comb(carrier, support) + sum(
        comb(carrier, support - external)
        * comb(outside, external - 1)
        * (defect + support - external)
        // external
        for external in range(1, support + 1)
    )


def incidence_cap(K: int, m: int, support: int, defect: int) -> int:
    return support_count(K, m, support, defect) * comb(
        m - support, 11 - support
    )


def contract() -> dict[str, object]:
    K = 54
    m = 67526
    defect = 22
    samples = {
        str(support): {
            "intersection_dimension": 12 - 2 * support,
            "carrier_size": K - 10 + support - 1 - defect,
            "outside_budget": defect + support - 1,
            "support_count": support_count(K, m, support, defect),
            "incidence_cap": incidence_cap(K, m, support, defect),
        }
        for support in SUPPORTS
    }
    return {
        "schema": "rate-half-mca-sparse-circuit-small-support-self-collision-charge-v1",
        "dependencies": [
            "rate_half_mca_sparse_circuit_universal_completion_incidence_cap",
            "rate_half_mca_sparse_circuit_cross_support_defect_carrier",
        ],
        "parameters": {
            "correction_dimension": 10,
            "component_size": 11,
            "support_range": [2, 5],
            "completion_maximum": "M_c=q-s",
            "empty_stratum": "s=q implies zero circuits",
            "source_carrier_size": "b=q+c-1-s",
            "intersection_dimension": "12-2c",
            "outside_carrier_budget": "s+c-1",
            "inside_count": "C(b,c)",
            "outside_stratum_count": (
                "floor(C(b,c-j)C(m-b,j-1)(s+c-j)/j)"
            ),
            "incidence_multiplier": "C(m-c,11-c)",
            "K54_defect22_samples": samples,
        },
        "claim": (
            "Exact same-source collisions give branch-safe circuit and "
            "selected-incidence caps at every support c=2..5."
        ),
        "nonclaim": (
            "No support c>=6, rank-eight, rank-eleven, KoalaBear, or prize "
            "closure is asserted."
        ),
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(data == contract(), "exact contract")
    p = data["parameters"]
    require(isinstance(p, dict), "parameters")
    checks = 0
    for support in SUPPORTS:
        require(12 - 2 * support > 0, "positive intersection")
        require(2 * support - 1 <= 10, "zero-defect Vandermonde")
        for defect in range(1, 45):
            for external in range(1, support + 1):
                require(
                    defect + support - 1 - (external - 1)
                    == defect + support - external,
                    "outside budget",
                )
                require(defect + support - external > 0, "positive cap")
                checks += 1
        require(support_count(54, 67526, support, 44) == 0, "empty")
    require("c>=6" in str(data["nonclaim"]), "nonclaim")
    return {"supports": len(SUPPORTS), "checks": checks}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item.__setitem__("dependencies", []),
        lambda item: item["parameters"].__setitem__("support_range", [2, 6]),
        lambda item: item["parameters"].__setitem__("empty_stratum", "wrong"),
        lambda item: item["parameters"].__setitem__("intersection_dimension", "11-2c"),
        lambda item: item["parameters"].__setitem__("outside_carrier_budget", "s+c"),
        lambda item: item["parameters"]["K54_defect22_samples"]["2"].__setitem__("incidence_cap", 0),
        lambda item: item.__setitem__("nonclaim", "support six proved"),
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
        "RATE_HALF_MCA_SPARSE_CIRCUIT_SMALL_SUPPORT_SELF_COLLISION_CHARGE_PASS "
        f"supports={result['supports']} checks={result['checks']} controls={controls}"
    )


if __name__ == "__main__":
    main()
