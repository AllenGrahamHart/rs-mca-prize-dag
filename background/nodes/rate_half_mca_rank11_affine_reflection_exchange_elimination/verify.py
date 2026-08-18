#!/usr/bin/env python3
"""Verify the affine-reflection exchange-elimination composition."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "062484bfac76ff44a138738ff35308268a50d5ce262edfb69ed2eff93c555c9b"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-affine-reflection-exchange-elimination-v1",
        "schema",
    )
    require(
        (data.get("official_base_prime"), data.get("official_domain_order"))
        == (2130706433, 2**21),
        "official row",
    )
    require(data.get("exception_degree") == 2, "degree")
    require(data.get("reflection_constant_nonzero") is True, "nonzero c")
    anchor = data.get("synchronized_anchor_fibers")
    cap = data.get("fixed_pencil_fiber_cap")
    margin = data.get("strict_fiber_margin")
    require((anchor, cap, margin) == (5524, 1154, 4370), "fiber pins")
    require(anchor - cap == margin > 0, "contradiction")
    require(data.get("high_complexity_threshold") == 2299571, "chi")
    dependencies = (
        data.get("synchronization_dependency"),
        data.get("census_dependency"),
    )
    require(
        dependencies
        == (
            "rate_half_mca_rank11_anchor_exchange_split_pencil_synchronization",
            "rate_half_mca_rank11_exception_spi_affine_reflection_fixed_pencil_cap",
        ),
        "dependencies",
    )
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(all(nodes.get(dep, {}).get("status") == "PROVED" for dep in dependencies), "proved dependencies")
    remaining = data.get("remaining_classes")
    require(
        remaining
        == [
            "antipodal-c-zero",
            "other-fractional-involutions",
            "extension-field-normalization",
            "nonquadratic-or-primitive",
        ],
        "remaining classes",
    )
    require("does not pay" in str(data.get("nonclaim")).lower(), "nonclaim")
    return {"anchor": anchor, "cap": cap, "margin": margin}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("exception_degree", 3),
        lambda item: item.__setitem__("reflection_constant_nonzero", False),
        lambda item: item.__setitem__("synchronized_anchor_fibers", 1154),
        lambda item: item.__setitem__("fixed_pencil_fiber_cap", 5524),
        lambda item: item.__setitem__("strict_fiber_margin", 4369),
        lambda item: item.__setitem__("high_complexity_threshold", 2299570),
        lambda item: item.__setitem__("synchronization_dependency", "missing"),
        lambda item: item.__setitem__("remaining_classes", []),
        lambda item: item.__setitem__("nonclaim", "pays high complexity"),
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
        print(f"RANK11_AFFINE_EXCHANGE_ELIMINATION_TAMPER_PASS mutations={tamper_selftest(data)}/9")
        return
    print(
        "RANK11_AFFINE_EXCHANGE_ELIMINATION_PASS "
        f"anchor={checked['anchor']} cap={checked['cap']} margin={checked['margin']}"
    )


if __name__ == "__main__":
    main()
