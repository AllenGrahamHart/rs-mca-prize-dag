#!/usr/bin/env python3
"""Verify the rank-nine split-pencil pair-core dichotomy."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "e899fbb6893e61495371f689f6a2ca5eb196d0bbc6d6ec8dc39b34eb9965c252"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-rank9-split-pencil-paircore-dichotomy-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_rank11_rank9_split_pencil_cell_ledger"],
        "dependency",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    n, m = p["n"], p["m"]
    outside = n - m
    intersection = 2 * m - n
    require(outside == p["outside_support_size"] == 981104, "outside size")
    require(
        intersection == p["two_support_intersection_floor"] == 134944,
        "intersection floor",
    )
    require(outside + intersection == m, "rate-half split")
    require(p["fixed_owner_slope_cap"] == outside + 1 == 981105, "owner cap")
    require(p["lifted_common_core_floor"] == 10, "core floor")
    petals = n - p["lifted_common_core_floor"]
    require(petals == p["petal_resource_ceiling"] == 2097142, "petals")
    ordered = (outside + 1) * petals
    require(
        ordered == p["ordered_pair_resource_ceiling"] == 2057516501910,
        "ordered pairs",
    )
    root = math.isqrt(1 + 4 * ordered)
    cap = (1 + root) // 2
    require(cap == p["low_common_core_plane_cap"] == 1434405, "plane cap")
    require(cap * (cap - 1) <= ordered, "cap feasible")
    fail_by = (cap + 1) * cap - ordered
    require(fail_by == p["next_integer_fails_by"] == 2636520, "adjacent failure")
    require(data.get("routes") == [
        "LOW_COMMON_CORE_PLANE_CAP",
        "SHARED_PAIR_CORE_AT_LEAST_134944",
    ], "routes")
    require(len(data.get("identities", [])) == 5, "identities")
    require("does not count planes" in str(data.get("nonclaim")), "nonclaim")
    return {"intersection": intersection, "ordered": ordered, "cap": cap}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("two_support_intersection_floor", 134943),
        lambda item: item["parameters"].__setitem__("lifted_common_core_floor", 9),
        lambda item: item["parameters"].__setitem__("fixed_owner_slope_cap", 981104),
        lambda item: item["parameters"].__setitem__("ordered_pair_resource_ceiling", 2057516501909),
        lambda item: item["parameters"].__setitem__("low_common_core_plane_cap", 1434404),
        lambda item: item["parameters"].__setitem__("next_integer_fails_by", 2636519),
        lambda item: item["identities"].pop(),
        lambda item: item["routes"].pop(),
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
        "RATE_HALF_MCA_RANK11_RANK9_SPLIT_PENCIL_PAIRCORE_DICHOTOMY_PASS "
        f"intersection={result['intersection']} ordered={result['ordered']} "
        f"cap={result['cap']} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
