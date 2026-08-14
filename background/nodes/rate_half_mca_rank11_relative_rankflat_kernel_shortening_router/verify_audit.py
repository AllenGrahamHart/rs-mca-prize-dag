#!/usr/bin/env python3
"""Independent audit for the rank-flat kernel-shortening router."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "7adb6a91110bfaceb837d610c00b278bdc95b5cd79c1599603749fc53d742cdc"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> tuple[int, int]:
    require(isinstance(data, dict), "contract")
    dimensions = data.get("dimensions")
    invariants = data.get("shortening_invariants")
    require(isinstance(dimensions, dict) and isinstance(invariants, dict), "sections")
    require(dimensions["kernel_minimum"] == 1, "kernel nonzero")
    require(dimensions["kernel_maximum"] == dimensions["component_maximum"] - 1 == 9, "rank drop")
    require(dimensions["kernel_maximum"] <= dimensions["paid_rank_maximum"], "paid")
    require(invariants["vertical_component_slope_cap"] == 1, "vertical")
    require(data["routes"][1].endswith("RANKDROP_PAID"), "route")

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in ("`U=ker(ev_T)`", "u=s-r <= s-1 <=9", "does not sum"):
        require(token in statement, f"statement token {token}")
    for token in (
        "Choose a complement `W_0`",
        "received columns vanish on `T`",
        "The proof treats one irreducible component",
    ):
        require(token in proof, f"proof token {token}")
    return dimensions["kernel_maximum"], invariants["vertical_component_slope_cap"]


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    kernel, vertical = audit(data)
    mutations = (
        lambda item: item["dimensions"].__setitem__("kernel_maximum", 10),
        lambda item: item["dimensions"].__setitem__("paid_rank_maximum", 8),
        lambda item: item["shortening_invariants"].__setitem__("vertical_component_slope_cap", 2),
        lambda item: item["routes"].__setitem__(1, "UNPAID"),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            audit(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_RELATIVE_RANKFLAT_KERNEL_SHORTENING_ROUTER_AUDIT_PASS "
        f"kernel_max={kernel} vertical={vertical} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
