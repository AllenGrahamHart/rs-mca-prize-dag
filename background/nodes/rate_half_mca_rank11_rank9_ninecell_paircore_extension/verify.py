#!/usr/bin/env python3
"""Verify the rank-nine nine-cell pair-core scope extension."""

from __future__ import annotations

import copy
import hashlib
import json
from math import isqrt
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "8d91c142853cbc92720abb7372d677287dd1e83d3755e12361d322a617d2fe78"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-rank9-ninecell-paircore-extension-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_rank11_rank9_split_pencil_paircore_dichotomy"],
        "dependency",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    n, m = p["n"], p["m"]
    d = n - m
    require(d == p["outside_support_size"] == 981104, "outside")
    require(2 * m - n == p["two_support_intersection_floor"] == 134944, "intersection")
    require((p["fixed_cell_size"], p["fixed_cell_rank"], p["kernel_dimension"]) == (9, 9, 1), "cell")
    require(p["fixed_owner_slope_cap"] == d + 1 == 981105, "owner cap")
    petals = n - p["fixed_cell_size"]
    ordered = (d + 1) * petals
    require(petals == p["petal_resource_ceiling"] == 2097143, "petals")
    require(ordered == p["ordered_pair_resource_ceiling"] == 2057517483015, "ordered")
    cap = (1 + isqrt(1 + 4 * ordered)) // 2
    require(cap == p["low_common_core_plane_cap"] == 1434405, "cap")
    require(ordered - cap * (cap - 1) == p["cap_feasible_slack"] == 1213395, "lower slack")
    require((cap + 1) * cap - ordered == p["next_integer_fails_by"] == 1655415, "upper gap")
    require(data.get("routes") == [
        "NINECELL_LOW_COMMON_CORE_PLANE_CAP",
        "NINECELL_SHARED_PAIR_CORE_AT_LEAST_134944",
    ], "routes")
    require("does not count owner planes" in str(data.get("nonclaim")), "nonclaim")
    return {"ordered": ordered, "cap": cap}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("fixed_cell_size", 10),
        lambda item: item["parameters"].__setitem__("petal_resource_ceiling", 2097142),
        lambda item: item["parameters"].__setitem__("ordered_pair_resource_ceiling", 2057516501910),
        lambda item: item["parameters"].__setitem__("low_common_core_plane_cap", 1434406),
        lambda item: item["parameters"].__setitem__("next_integer_fails_by", 1655414),
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
        "RATE_HALF_MCA_RANK11_RANK9_NINECELL_PAIRCORE_EXTENSION_PASS "
        f"ordered={result['ordered']} cap={result['cap']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
