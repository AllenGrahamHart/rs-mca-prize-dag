#!/usr/bin/env python3
"""Verify the scalar-dimension-two incidence exclusion."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "03ec061a245542f320e8fd1bb38c0d3b704b03b4639c414f496e87be25187c5d"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-pair-pencil-dimension-two-incidence-exclusion-v1",
        "schema",
    )
    n, m, K = data.get("n"), data.get("m"), data.get("K")
    q = data.get("selected_type_floor")
    s = data.get("pair_core_size")
    common = data.get("common_core_cap")
    outside = data.get("noncommon_coordinate_multiplicity_cap")
    require((n, m, K) == (2097152, 1116048, 1048576), "official row")
    require((q, s, common, outside) == (520, m - 2, K - 1, 15), "input pins")
    required = q * s
    capacity = q * common + outside * (n - common)
    margin = required - capacity
    require(data.get("required_incidence") == required == 580343920, "required")
    require(data.get("capacity") == capacity == 560987655, "capacity")
    require(data.get("contradiction_margin") == margin == 19356265, "margin")
    require(margin > 0, "contradiction")
    require(data.get("surviving_dimensions") == [3, 4], "dimensions")
    require("not paid" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    for dependency in (
        "rate_half_mca_rank11_pair_pencil_affine_line_cap_direction_router",
        "rate_half_mca_rank11_pair_pencil_dimension_two_common_core_shortening",
    ):
        require(nodes.get(dependency, {}).get("status") == "PROVED", f"dependency {dependency}")
    return {"required": required, "capacity": capacity, "margin": margin}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("n", 2097151),
        lambda item: item.__setitem__("selected_type_floor", 519),
        lambda item: item.__setitem__("pair_core_size", 1116045),
        lambda item: item.__setitem__("common_core_cap", 1048576),
        lambda item: item.__setitem__("noncommon_coordinate_multiplicity_cap", 16),
        lambda item: item.__setitem__("required_incidence", 580343919),
        lambda item: item.__setitem__("contradiction_margin", 19356264),
        lambda item: item.__setitem__("surviving_dimensions", [2, 3, 4]),
    )
    caught = 0
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutations")
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    checked = validate(data)
    if args.tamper_selftest:
        print(f"PAIR_PENCIL_DIM2_INCIDENCE_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "PAIR_PENCIL_DIM2_INCIDENCE_PASS "
        f"required={checked['required']} capacity={checked['capacity']} margin={checked['margin']}"
    )


if __name__ == "__main__":
    main()
