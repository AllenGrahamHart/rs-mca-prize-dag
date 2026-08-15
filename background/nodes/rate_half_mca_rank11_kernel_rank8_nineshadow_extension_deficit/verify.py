#!/usr/bin/env python3
"""Verify the rank-eight nine-shadow extension deficit."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "f78e2d0d08b3c4535a1ef2db02e2bde7956b4c0eebe67e3de2c8cebc0441ec2a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-kernel-rank8-nineshadow-extension-deficit-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_rank11_kernel_nine_shadow_containment_coupling"],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["support_offset"] == 67472, "support offset")
    require((p["component_subset_size"], p["shadow_subset_size"]) == (11, 9), "subset sizes")
    require((p["rank8_closure_offset"], p["rank9_closure_offset"]) == (2, 1), "closure offsets")
    require(
        (p["outside_rank8_closure_minimum"], p["outside_parallel_class_partner_minimum"])
        == (67474, 67473),
        "outside floors",
    )
    pair_floor = comb(p["outside_rank8_closure_minimum"], 2)
    require(pair_floor == p["independent_pair_floor"] == 2276336601, "pair floor")

    checks = 0
    for kprime in (11, 12, 11773, 15446, 15671, 17609, 22525):
        support_size = p["support_offset"] + kprime
        for closure_size in range(9, kprime - 1):
            outside = support_size - closure_size
            parallel_cap = kprime - 1 - closure_size
            require(outside >= 67474, f"outside K={kprime}")
            require(parallel_cap >= 1, f"parallel cap K={kprime}")
            ordered_independent = outside * (outside - parallel_cap)
            require(ordered_independent >= 2 * pair_floor, f"pair floor K={kprime}")
            checks += 1
        unrestricted = comb(support_size - 9, 2)
        require(unrestricted - pair_floor < unrestricted, f"strict deficit K={kprime}")

    require("does not by itself pay" in str(data.get("nonclaim")), "nonclaim")
    return {"checks": checks, "pair_floor": pair_floor}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("support_offset", 67471),
        lambda item: item["parameters"].__setitem__("rank8_closure_offset", 1),
        lambda item: item["parameters"].__setitem__("outside_rank8_closure_minimum", 67473),
        lambda item: item["parameters"].__setitem__("outside_parallel_class_partner_minimum", 67472),
        lambda item: item["parameters"].__setitem__("independent_pair_floor", 2276336600),
        lambda item: item.__setitem__("nonclaim", "paid"),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_RANK8_NINESHADOW_EXTENSION_DEFICIT_PASS "
        f"checks={result['checks']} pair_floor={result['pair_floor']} "
        f"controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
