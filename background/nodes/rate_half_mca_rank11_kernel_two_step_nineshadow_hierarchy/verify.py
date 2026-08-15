#!/usr/bin/env python3
"""Verify the two-step nine-shadow hierarchy constants."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "b62be3d37c39c2f482b2e50dcc638acf2c39fb49ebe14f56e11e7adb35eaf317"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def expected_rows() -> list[list[int]]:
    return [
        [d, comb(d + 2, 2), 67472 + d, 67471 + d, comb(67472 + d, 2), 11 - d, comb(11 - d, 2)]
        for d in range(3, 10)
    ]


def validate(data: object) -> int:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "rate-half-mca-rank11-kernel-two-step-nineshadow-hierarchy-v1", "schema")
    require(data.get("dependencies") == [
        "rate_half_mca_rank11_kernel_nine_shadow_coupling",
        "rate_half_mca_rank11_kernel_rank8_nineshadow_extension_deficit",
    ], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["support_offset"], p["corank_minimum"], p["corank_maximum"]) == (67472, 3, 9), "range")
    require(p["couplings"] == expected_rows(), "coupling rows")
    for d, shadows, outside, partners, pair_floor, coloops, multiplicity in p["couplings"]:
        require(outside == partners + 1, f"outside/partner d={d}")
        require(pair_floor == outside * partners // 2, f"pair floor d={d}")
        require(shadows == comb(d + 2, 2), f"shadow multiplicity d={d}")
        require(coloops == (12 - d) - 1, f"loopless coloop cap d={d}")
        require(multiplicity == comb(coloops, 2), f"target multiplicity d={d}")
        for kprime in (d + 11, 17609, 18102, 22525):
            extension = comb(kprime - d - 9, 2)
            require(extension > 0, f"extension d={d} K={kprime}")
            require(shadows * pair_floor > 0 and multiplicity > 0, f"coefficient signs d={d}")
    require("does not by itself" in str(data.get("nonclaim")), "nonclaim")
    return len(p["couplings"])


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    rows = validate(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("support_offset", 67471),
        lambda item: item["parameters"]["couplings"][0].__setitem__(4, 2276404074),
        lambda item: item["parameters"]["couplings"][1].__setitem__(6, 22),
        lambda item: item["parameters"].__setitem__("corank_maximum", 8),
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
    print(f"RATE_HALF_MCA_RANK11_KERNEL_TWO_STEP_NINESHADOW_HIERARCHY_PASS rows={rows} controls={caught}/{len(mutations)}")


if __name__ == "__main__":
    main()
