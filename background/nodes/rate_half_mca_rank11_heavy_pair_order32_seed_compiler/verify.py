#!/usr/bin/env python3
"""Verify the rank-eleven heavy-pair order-32 seed compiler ledger."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "378cf4a4c17f7fffc4ba9863d0dabef5fd85f9831dcde0481ed193ba26aa6b6a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def rank(rows: list[list[int]], p: int) -> int:
    matrix = [[value % p for value in row] for row in rows]
    if not matrix:
        return 0
    width = len(matrix[0])
    pivot = 0
    for column in range(width):
        row = next((i for i in range(pivot, len(matrix)) if matrix[i][column]), None)
        if row is None:
            continue
        matrix[pivot], matrix[row] = matrix[row], matrix[pivot]
        inverse = pow(matrix[pivot][column], -1, p)
        matrix[pivot] = [(inverse * value) % p for value in matrix[pivot]]
        for i in range(len(matrix)):
            if i == pivot or matrix[i][column] == 0:
                continue
            factor = matrix[i][column]
            matrix[i] = [
                (left - factor * right) % p
                for left, right in zip(matrix[i], matrix[pivot])
            ]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


def component_selection_control() -> tuple[int, int]:
    p = 101
    dimension = 10
    pair_components: list[tuple[list[int], list[int]]] = []
    for i in range(24):
        left = [0] * dimension
        right = [0] * dimension
        left[i % dimension] = 1
        right[(3 * i + 1) % dimension] = (i + 2) % p
        pair_components.append((left, right))
    all_rows = [row for pair in pair_components for row in pair]
    target_rank = rank(all_rows, p)
    selected: list[tuple[list[int], list[int]]] = []
    current_rows: list[list[int]] = []
    current_rank = 0
    for pair in pair_components:
        candidate = [*current_rows, pair[0], pair[1]]
        candidate_rank = rank(candidate, p)
        if candidate_rank > current_rank:
            selected.append(pair)
            current_rows = candidate
            current_rank = candidate_rank
        if current_rank == target_rank:
            break
    require(target_rank == dimension, "toy component rank")
    require(current_rank == target_rank and len(selected) <= dimension, "toy selection")
    return target_rank, len(selected)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-heavy-pair-order32-seed-compiler-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == {
            "pair_core_route_cut": "rate_half_mca_rank11_pair_core_route_cut_import",
            "shared_core_payment": "rate_half_mca_rank11_large_shared_pair_core_payment",
            "upstream_pr1168_head": "6a5dcdae1591fc7f044eda6a942bfe178521a48c",
        },
        "dependencies",
    )
    row = data.get("official")
    require(isinstance(row, dict), "official")
    require(
        tuple(
            row.get(key)
            for key in (
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
            )
        )
        == (
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
        ),
        "official constants",
    )
    n, dimension, agreement, w, budget = (
        row[key] for key in ("n", "K", "m", "w", "B_star")
    )
    pair_cap = comb(n - dimension + 10, 10) // comb(w - 387 + 10, 10)
    require(pair_cap == row.get("distinct_pair_cap") == 869784434119, "pair cap")
    require(row.get("heavy_pair_record_threshold") == 2, "heavy threshold")
    require(
        row.get("component_span_dimension_maximum")
        == row.get("explanation_affine_rank")
        == 10,
        "component dimension",
    )
    require(row.get("selected_heavy_pair_types_maximum") == 11, "selected pairs")
    require(row.get("selected_seed_records_maximum") == 22, "selected records")
    require(row.get("order32_size") == 32 > 22, "order size")
    require(
        row.get("common_core_size_threshold")
        == dimension - row.get("common_core_codimension_maximum")
        == 1043654,
        "core threshold",
    )

    fixed_pair_cap = n - agreement + 1
    shortened_types = row.get("shortened_heavy_pair_type_cap")
    singleton = pair_cap
    heavy = shortened_types * fixed_pair_cap
    low = singleton + heavy
    total = row.get("near_charge") + row.get("high_margin_cap") + low
    slack = budget - total
    unsafe_low = budget + 1 - row.get("near_charge") - row.get("high_margin_cap")
    require(row.get("near_charge") == 2 * w, "near")
    require(
        (shortened_types, fixed_pair_cap, singleton, heavy, low, total, slack, unsafe_low)
        == tuple(
            row.get(key)
            for key in (
                "shortened_heavy_pair_type_cap",
                "pair_record_cap",
                "singleton_record_cap",
                "heavy_record_cap",
                "low_margin_cap",
                "total_cap_if_large_heavy_core",
                "budget_slack_if_large_heavy_core",
                "unsafe_low_record_minimum",
            )
        )
        == (
            94943,
            981105,
            869784434119,
            93149052015,
            962933486134,
            274791086998147432,
            189641113247655,
            190604046733790,
        ),
        "payment ledger",
    )
    require(unsafe_low > pair_cap > 32, "heavy family and padding")
    toy_rank, toy_selected = component_selection_control()
    scope = data.get("scope")
    require(isinstance(scope, dict), "scope")
    require("more than B_star" in str(scope.get("premise")), "premise")
    require("32 distinct" in str(scope.get("conclusion")), "conclusion")
    require("does not classify" in str(scope.get("nonclaim")), "nonclaim")
    return {
        "pair_cap": pair_cap,
        "total": total,
        "slack": slack,
        "toy_rank": toy_rank,
        "toy_selected": toy_selected,
    }


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["official"].__setitem__("distinct_pair_cap", 869784434118),
        lambda item: item["official"].__setitem__("heavy_pair_record_threshold", 1),
        lambda item: item["official"].__setitem__("component_span_dimension_maximum", 20),
        lambda item: item["official"].__setitem__("selected_heavy_pair_types_maximum", 12),
        lambda item: item["official"].__setitem__("common_core_size_threshold", 1043653),
        lambda item: item["official"].__setitem__("low_margin_cap", 962933486133),
        lambda item: item["official"].__setitem__("unsafe_low_record_minimum", 190604046733789),
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
        "RATE_HALF_MCA_RANK11_HEAVY_PAIR_ORDER32_SEED_COMPILER_PASS "
        f"Q={result['pair_cap']} total={result['total']} slack={result['slack']} "
        f"basis={result['toy_selected']}/{result['toy_rank']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
