#!/usr/bin/env python3
"""Verify the exact K'=22 integral near-saturation payment."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from math import comb, prod
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "4d2031a5d96149bc5cf2d1c20e9b997200f3baf4a98c14b87ab5e7836435f77d"
RECORD_FLOOR = 274980728111260126
DENSITY_NUMERATOR = 990810934
DENSITY_DENOMINATOR = 10**9


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def falling(value: int, length: int) -> int:
    return prod(range(value - length + 1, value + 1))


def rising(value: int, length: int) -> int:
    return prod(range(value, value + length))


def kernel_record_cap(kprime: int, corank: int) -> int:
    if corank == 1:
        return 8147918
    if corank == 9:
        return 61871313426630599
    rank = 10 - corank
    shortened = kprime - rank
    zero_endpoint = Fraction(
        falling(1048576 + shortened, corank + 1),
        (67472 + shortened) * rising(67473, corank - 1),
    )
    maximum_endpoint = Fraction(
        falling(1048576 + corank, corank + 1),
        rising(67473, corank),
    )
    return int(max(zero_endpoint, maximum_endpoint))


def row() -> dict[str, object]:
    kprime = 22
    n = 1048576 + kprime
    m = 67472 + kprime
    q = kprime - 10
    weights = {2: 26, 3: 18, 4: 11, 5: 5}

    kernel = sum(
        comb(n, 10 - corank)
        * kernel_record_cap(kprime, corank)
        * comb(q, corank + 1)
        for corank in range(1, 10)
    )
    chart = 9269974099565290
    marks = comb(n, 9) * chart

    structured = {
        support: comb(q + 4, support) * comb(m - support, 11 - support)
        for support in weights
    }
    refined = {}
    for support in weights:
        completions = q - 2 if support <= 4 else q - 1
        deletion = (
            comb(m, support - 1)
            * completions
            * comb(m - support + 1 - completions, 11 - support)
            // support
        )
        carrier = (
            comb(q + 2 * support - 2, support) * comb(m - support, 11 - support)
            if support <= 4
            else 0
        )
        refined[support] = max(deletion, carrier)
    structured_premium = sum(weights[c] * structured[c] for c in weights)
    refined_premium = sum(weights[c] * refined[c] for c in weights)
    premium = max(structured_premium, refined_premium)

    full_rank = (marks + RECORD_FLOOR * premium) // 45
    total = kernel + full_rank
    demand = (
        DENSITY_NUMERATOR * RECORD_FLOOR * comb(m, 11)
        + DENSITY_DENOMINATOR
        - 1
    ) // DENSITY_DENOMINATOR
    coefficient = (
        45 * DENSITY_NUMERATOR * comb(m, 11)
        - DENSITY_DENOMINATOR * premium
    )
    raw = RECORD_FLOOR * coefficient - DENSITY_DENOMINATOR * (
        45 * kernel + marks
    )
    return {
        "kernel": kernel,
        "chart": chart,
        "marks": marks,
        "structured": {str(key): value for key, value in structured.items()},
        "refined": {str(key): value for key, value in refined.items()},
        "structured_premium": structured_premium,
        "premium": premium,
        "full_rank": full_rank,
        "total": total,
        "demand": demand,
        "gap": demand - total,
        "coefficient": coefficient,
        "raw": raw,
    }


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-k22-integral-near-saturation-payment-v1",
        "schema",
    )
    require(len(data.get("dependencies", [])) == 5, "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p.get("K_prime") == 22, "row")
    require(p.get("uniform_corank_one_record_cap") == 8147918, "corank one")
    require(p.get("maximizing_core") == 21, "core")
    expected = row()
    require(p.get("kernel_capacity") == expected["kernel"], "kernel")
    require(p.get("uniform_rank9_chart_cap") == expected["chart"], "chart")
    require(p.get("global_rank9_mark_capacity") == expected["marks"], "marks")
    require(p.get("structured_sparse_caps") == expected["structured"], "structured")
    require(p.get("refined_unstructured_sparse_caps") == expected["refined"], "refined")
    require(p.get("structured_premium") == expected["structured_premium"], "structured premium")
    require(p.get("active_refined_premium") == expected["premium"], "premium")
    require(expected["premium"] > expected["structured_premium"], "active branch")
    require(p.get("full_rank_capacity") == expected["full_rank"], "full rank")
    require(p.get("total_capacity") == expected["total"], "total")
    require(p.get("required_incidence") == expected["demand"], "demand")
    require(p.get("demand_capacity_gap") == expected["gap"], "gap")
    require(p.get("record_coefficient_cross") == expected["coefficient"], "coefficient")
    require(p.get("floor_record_raw_cross") == expected["raw"], "raw")
    require(expected["gap"] > 0 and expected["coefficient"] > 0 and expected["raw"] > 0, "strict")
    require(p.get("new_closed_prefix") == [10, 22], "prefix")
    require(p.get("remaining_rank9_interval") == [23, 15528], "remaining")
    require("No K'>=23 row" in str(data.get("nonclaim")), "nonclaim")
    return {"gap": int(expected["gap"]), "premium": int(expected["premium"])}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("K_prime", 23),
        lambda item: item["parameters"].__setitem__("uniform_corank_one_record_cap", 8147919),
        lambda item: item["parameters"].__setitem__("kernel_capacity", 0),
        lambda item: item["parameters"].__setitem__("uniform_rank9_chart_cap", 0),
        lambda item: item["parameters"]["refined_unstructured_sparse_caps"].__setitem__("4", 0),
        lambda item: item["parameters"].__setitem__("active_refined_premium", 0),
        lambda item: item["parameters"].__setitem__("full_rank_capacity", 0),
        lambda item: item["parameters"].__setitem__("demand_capacity_gap", 0),
        lambda item: item["parameters"].__setitem__("record_coefficient_cross", 0),
        lambda item: item["parameters"].__setitem__("floor_record_raw_cross", 0),
        lambda item: item["parameters"].__setitem__("remaining_rank9_interval", [22, 15528]),
        lambda item: item.__setitem__("nonclaim", "K'=23 closed"),
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
        "RATE_HALF_MCA_RANK11_K22_INTEGRAL_NEAR_SATURATION_PAYMENT_PASS "
        f"gap={result['gap']} premium={result['premium']} controls={controls}"
    )


if __name__ == "__main__":
    main()
