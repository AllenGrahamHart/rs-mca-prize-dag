#!/usr/bin/env python3
"""Verify the dimension-two common-core shortening contract."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "6d5c814be1bf2e0e9947cb36115891b9fa38441f2d81e1a3156efc121ec027f7"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank11-pair-pencil-dimension-two-common-core-shortening-v1",
        "schema",
    )
    n, m, K = data.get("n"), data.get("m"), data.get("K")
    t = data.get("direction_count")
    roots = data.get("direction_intersection_floor")
    require((n, m, K) == (2097152, 1116048, 1048576), "official row")
    require((t, roots) == (38, 134940), "direction pins")
    core = math.ceil((t * roots - n) / (t - 1))
    require(data.get("common_core_floor") == core == 81908, "core floor")
    slack = (n - core) - t * (roots - core)
    require(data.get("residual_petal_slack_at_floor") == slack == 28, "slack")
    require(data.get("preserved_excess") == m - K == 67472, "excess")
    require(data.get("quotient_core_deficiency") == 2, "deficiency")
    require(data.get("other_dimensions") == [3, 4], "other dimensions")
    require("not paid" in str(data.get("nonclaim")).lower(), "nonclaim")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    dependency = "rate_half_mca_rank11_pair_pencil_affine_line_cap_direction_router"
    require(nodes.get(dependency, {}).get("status") == "PROVED", "dependency")
    return {"directions": t, "roots": roots, "core": core, "slack": slack}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("n", 2097151),
        lambda item: item.__setitem__("direction_count", 37),
        lambda item: item.__setitem__("direction_intersection_floor", 134939),
        lambda item: item.__setitem__("common_core_floor", 81907),
        lambda item: item.__setitem__("residual_petal_slack_at_floor", 29),
        lambda item: item.__setitem__("preserved_excess", 67471),
        lambda item: item.__setitem__("quotient_core_deficiency", 3),
        lambda item: item.__setitem__("other_dimensions", [2, 3, 4]),
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
        print(f"PAIR_PENCIL_DIM2_COMMON_CORE_TAMPER_PASS mutations={tamper_selftest(data)}/8")
        return
    print(
        "PAIR_PENCIL_DIM2_COMMON_CORE_PASS "
        f"directions={checked['directions']} roots={checked['roots']} "
        f"core={checked['core']} slack={checked['slack']}"
    )


if __name__ == "__main__":
    main()
