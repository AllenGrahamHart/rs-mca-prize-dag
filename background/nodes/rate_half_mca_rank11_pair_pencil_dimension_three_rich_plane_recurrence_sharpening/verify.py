#!/usr/bin/env python3
"""Verify the dimension-three rich-plane recurrence sharpening."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "62ff582fb5bdd34dbb15a7d8b73618f01139e7db68fb3a150af15e17c5f918ea"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-dimension-three-rich-plane-recurrence-v1",
        "schema",
    )
    v = data.get("selected_types")
    line_cap = data.get("line_occupancy_cap")
    plane_cap = data.get("plane_occupancy_cap")
    require((v, line_cap, plane_cap) == (520, 15, 218), "geometry pins")

    threshold = (v + 3 * line_cap) // 3 + 1
    require(threshold == 189, "threshold arithmetic")
    require(data.get("rich_plane_threshold") == threshold, "threshold pin")
    require(3 * threshold - 3 * line_cap > v, "three-plane obstruction")
    require(3 * (threshold - 1) - 3 * line_cap <= v, "threshold adjacency")
    require(data.get("rich_plane_count_ceiling") == 2, "plane count")
    require(data.get("rich_plane_recurrence_offset") == 2, "recurrence offset")

    n0 = data.get("residual_length_offset")
    s0 = data.get("residual_core_offset")
    require((n0, s0) == (1048576, 67470), "residual offsets")
    numerator = 188 * n0 - 520 * s0 - 60 * 2
    denominator = 520 - 188 - 60
    require((numerator, denominator) == (162047768, 272), "collected ledger")
    kmax, remainder = divmod(numerator, denominator)
    require((kmax, remainder) == (595763, 232), "endpoint division")
    require(data.get("residual_dimension_ceiling") == kmax, "dimension ceiling")
    require(data.get("common_core_floor") == n0 - kmax == 452813, "core floor")
    require(data.get("endpoint_capacity_slack") == remainder, "endpoint slack")
    require(data.get("adjacent_capacity_deficit") == denominator - remainder == 40,
            "adjacent deficit")
    require(data.get("previous_common_core_floor") == 407831, "previous core")
    require(data.get("previous_residual_dimension_ceiling") == 640745,
            "previous dimension")
    require("does not pay" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(
        nodes.get("rate_half_mca_rank11_pair_pencil_affine_plane_cap_218_sharpening", {})
        .get("status") == "PROVED",
        "dependency",
    )
    return {"threshold": threshold, "kmax": kmax, "core": n0 - kmax,
            "slack": remainder}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("selected_types", 519),
        lambda item: item.__setitem__("line_occupancy_cap", 16),
        lambda item: item.__setitem__("plane_occupancy_cap", 217),
        lambda item: item.__setitem__("rich_plane_threshold", 188),
        lambda item: item.__setitem__("rich_plane_count_ceiling", 3),
        lambda item: item.__setitem__("rich_plane_recurrence_offset", 1),
        lambda item: item.__setitem__("residual_dimension_ceiling", 595764),
        lambda item: item.__setitem__("common_core_floor", 452812),
        lambda item: item.__setitem__("endpoint_capacity_slack", 231),
        lambda item: item.__setitem__("adjacent_capacity_deficit", 39),
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
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256,
            "contract hash")
    data = json.loads(CONTRACT.read_text())
    checked = validate(data)
    if args.tamper_selftest:
        print(f"RANK11_D3_RICH_PLANE_TAMPER_PASS mutations={tamper_selftest(data)}/10")
        return
    print(
        "RANK11_D3_RICH_PLANE_PASS "
        f"threshold={checked['threshold']} Kmax={checked['kmax']} "
        f"core={checked['core']} slack={checked['slack']}"
    )


if __name__ == "__main__":
    main()
