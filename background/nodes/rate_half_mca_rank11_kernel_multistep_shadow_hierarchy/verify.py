#!/usr/bin/env python3
"""Verify the multi-step shadow hierarchy constants."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "c7561d9192a00cd97530d61adff244cccfec97ce248fbe23c6074d641c33053b"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def triple_rows() -> list[list[int]]:
    return [
        [d, comb(d + 2, 3), 67472 + d, comb(67472 + d, 3), 12 - d, comb(12 - d, 3)]
        for d in range(4, 10)
    ]


def validate(data: object) -> int:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-multistep-shadow-hierarchy-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_nine_shadow_coupling",
        "rate_half_mca_rank11_kernel_two_step_nineshadow_hierarchy",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["support_offset"], p["corank_minimum"], p["corank_maximum"], p["step_minimum"]) == (67472, 3, 9, 2), "range")
    require(p["coupling_count"] == sum(d - 2 for d in range(3, 10)) == 28, "coupling count")
    require(p["triple_couplings"] == triple_rows(), "triple rows")
    checks = 0
    for d in range(3, 10):
        for step in range(2, d):
            shadow = comb(d + 2, step)
            raising = comb(67472 + d, step)
            coloops = 9 - d + step
            target = comb(coloops, step)
            require(shadow > 0 and raising > 0 and target > 0, f"positive row t={step} d={d}")
            for kprime in (d + 12, 18102, 18159, 22525):
                extension = comb(kprime - d - 11 + step, step)
                require(extension > 0, f"extension t={step} d={d} K={kprime}")
            checks += 1
    require("does not by itself" in str(data.get("nonclaim")), "nonclaim")
    return checks


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    checks = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("support_offset", 67471),
        lambda item: item["parameters"].__setitem__("coupling_count", 27),
        lambda item: item["parameters"]["triple_couplings"][1].__setitem__(3, 51203156926449),
        lambda item: item["parameters"]["triple_couplings"][5].__setitem__(5, 2),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered)
        except (ValueError, KeyError, TypeError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_KERNEL_MULTISTEP_SHADOW_HIERARCHY_PASS "
        f"couplings={checks} triples=6 controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
