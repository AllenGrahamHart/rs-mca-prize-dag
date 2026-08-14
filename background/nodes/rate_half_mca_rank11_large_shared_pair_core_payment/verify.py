#!/usr/bin/env python3
"""Verify the exact shared-pair-core rank-eleven payment."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "a4caa99b66e097953729776ad9b140b929c01761f1fafbd0de842dac7ab0ba8e"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract object")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-large-shared-pair-core-payment-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == {
            "support_local_router": "rate_half_mca_support_local_error_rank_router",
            "pair_core_route_cut": "rate_half_mca_rank11_pair_core_route_cut_import",
            "upstream_pr1168_head": "6a5dcdae1591fc7f044eda6a942bfe178521a48c",
        },
        "dependencies",
    )
    row = data.get("official")
    require(isinstance(row, dict), "official record")
    fixed = (
        2130706433,
        6,
        2097152,
        1048576,
        1116048,
        67472,
        274980728111395087,
        11,
        10,
        388,
        387,
        274790124064526354,
        4922,
    )
    keys = (
        "p",
        "extension_degree",
        "n",
        "K",
        "m",
        "w",
        "B_star",
        "error_rank",
        "explanation_affine_rank",
        "theta_cutoff",
        "low_margin_maximum",
        "high_margin_cap",
        "common_core_codimension_maximum",
    )
    require(tuple(row.get(key) for key in keys) == fixed, "official constants")
    p, extension, n, dimension, agreement, w, budget, _, _, cutoff, low_max, high, d_max = fixed
    require(cutoff == low_max + 1, "margin partition")
    require(row.get("near_charge") == 2 * w, "near charge")
    require(row.get("common_core_size_minimum") == dimension - d_max, "core size")

    redundancy = n - dimension
    offset = w - low_max
    denominator_constant = offset * offset + redundancy
    denominator_decrement = redundancy - 2 * offset - 1
    require(
        (offset, denominator_constant, denominator_decrement)
        == (
            row.get("residual_agreement_offset"),
            row.get("johnson_denominator_constant"),
            row.get("johnson_denominator_decrement"),
        ),
        "Johnson polynomial",
    )

    list_bounds: list[int] = []
    for d in range(1, d_max + 1):
        residual_length = redundancy + d
        residual_agreement = d + offset
        denominator = residual_agreement**2 - residual_length * (d - 1)
        require(
            denominator == denominator_constant - denominator_decrement * d > 0,
            "positive Johnson denominator",
        )
        numerator = residual_length * (residual_agreement - d + 1)
        bound = numerator // denominator
        require(bound * denominator <= numerator < (bound + 1) * denominator, "floor")
        list_bounds.append(bound)

    endpoint_length = redundancy + d_max
    endpoint_agreement = d_max + offset
    endpoint_denominator = denominator_constant - denominator_decrement * d_max
    next_denominator = denominator_constant - denominator_decrement * (d_max + 1)
    pair_types = max(list_bounds)
    require(list_bounds == sorted(list_bounds), "monotone Johnson bounds")
    require(
        (
            endpoint_length,
            endpoint_agreement,
            endpoint_denominator,
            next_denominator,
            pair_types,
        )
        == tuple(
            row.get(key)
            for key in (
                "residual_length_at_endpoint",
                "residual_agreement_at_endpoint",
                "johnson_denominator_at_endpoint",
                "johnson_denominator_after_endpoint",
                "ordinary_list_bound",
            )
        )
        == (1053498, 72007, 744391, -170014, 94943),
        "Johnson endpoint",
    )
    require(pair_types * pair_types < p**extension, "interleaving field gate")

    per_pair = n - agreement + 1
    low = pair_types * per_pair
    total = row["near_charge"] + high + low
    slack = budget - total
    require(
        (per_pair, low, total, slack)
        == tuple(
            row.get(key)
            for key in (
                "pair_record_cap",
                "low_margin_cap",
                "total_cap",
                "budget_slack",
            )
        )
        == (981105, 93149052015, 274790217213713313, 190510897681774),
        "budget ledger",
    )
    scope = data.get("scope")
    require(isinstance(scope, dict), "scope")
    require("theta at most 387" in str(scope.get("premise")), "premise scope")
    require(str(total) in str(scope.get("conclusion")), "conclusion scope")
    require("smaller than K-4922" in str(scope.get("nonclaim")), "nonclaim scope")
    return {"dimensions": d_max, "pair_types": pair_types, "low": low, "slack": slack}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["official"].__setitem__("common_core_codimension_maximum", 4923),
        lambda item: item["official"].__setitem__("common_core_size_minimum", 1043653),
        lambda item: item["official"].__setitem__("ordinary_list_bound", 94942),
        lambda item: item["official"].__setitem__("extension_degree", 1),
        lambda item: item["official"].__setitem__("pair_record_cap", 981104),
        lambda item: item["official"].__setitem__("high_margin_cap", 274790124064526355),
        lambda item: item["official"].__setitem__("total_cap", 274790217213713312),
        lambda item: item["dependencies"].__setitem__("upstream_pr1168_head", "0" * 40),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_LARGE_SHARED_PAIR_CORE_PAYMENT_PASS "
        f"dimensions={result['dimensions']} pair_types={result['pair_types']} "
        f"low={result['low']} slack={result['slack']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
