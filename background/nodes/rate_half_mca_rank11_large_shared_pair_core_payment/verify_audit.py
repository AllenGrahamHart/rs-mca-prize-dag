#!/usr/bin/env python3
"""Independent arithmetic audit of the shared-pair-core payment."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "a4caa99b66e097953729776ad9b140b929c01761f1fafbd0de842dac7ab0ba8e"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "object")
    row = data.get("official")
    require(isinstance(row, dict), "official")
    n = row.get("n")
    dimension = row.get("K")
    agreement = row.get("m")
    budget = row.get("B_star")
    d_max = row.get("common_core_codimension_maximum")
    low_max = row.get("low_margin_maximum")
    require(
        (n, dimension, agreement, budget, d_max, low_max)
        == (2097152, 1048576, 1116048, 274980728111395087, 4922, 387),
        "official base",
    )

    redundancy = n - dimension
    offset = agreement - dimension - low_max
    fractions: list[Fraction] = []
    denominators: list[int] = []
    for d in range(1, d_max + 2):
        length = redundancy + d
        threshold = offset + d
        denominator = threshold * threshold - length * (d - 1)
        denominators.append(denominator)
        if denominator > 0:
            fractions.append(Fraction(length * (threshold - d + 1), denominator))
    require(all(left < right for left, right in zip(fractions, fractions[1:])), "strict monotonicity")
    require(
        denominators[-2:]
        == [
            row.get("johnson_denominator_at_endpoint"),
            row.get("johnson_denominator_after_endpoint"),
        ]
        == [744391, -170014],
        "sign boundary",
    )
    endpoint = fractions[-1]
    list_bound = endpoint.numerator // endpoint.denominator
    require(list_bound == row.get("ordinary_list_bound") == 94943, "list endpoint")
    require(list_bound**2 < row.get("p") ** row.get("extension_degree"), "field gate")

    pair_cap = n - agreement + 1
    low = list_bound * pair_cap
    total = row.get("near_charge") + row.get("high_margin_cap") + low
    require(pair_cap == row.get("pair_record_cap"), "pair cap")
    require(low == row.get("low_margin_cap"), "low cap")
    require(total == row.get("total_cap") < budget, "total cap")
    require(budget - total == row.get("budget_slack"), "slack")
    require(dimension - d_max == row.get("common_core_size_minimum"), "common core")
    return {"list_bound": list_bound, "total": total, "slack": budget - total}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = audit(data)
    controls = []
    for key, value in (
        ("johnson_denominator_at_endpoint", 744390),
        ("low_margin_cap", 93149052014),
        ("budget_slack", 190510897681773),
        ("common_core_size_minimum", 1043653),
    ):
        altered = copy.deepcopy(data)
        altered["official"][key] = value
        try:
            audit(altered)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "audit controls")
    print(
        "RATE_HALF_MCA_RANK11_LARGE_SHARED_PAIR_CORE_PAYMENT_AUDIT_PASS "
        f"list={result['list_bound']} total={result['total']} slack={result['slack']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
