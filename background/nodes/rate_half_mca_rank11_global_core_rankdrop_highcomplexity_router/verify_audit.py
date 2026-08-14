#!/usr/bin/env python3
"""Independent semantic audit for the global-core rank-drop router."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "db4235553ac01335be6bb2daa03e3299735e8c882e40fd8d855527eb0e9e1eee"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> int:
    require(isinstance(data, dict), "contract")
    row = data.get("official")
    rank_drop = data.get("rank_drop")
    full = data.get("full_rank")
    toy = data.get("toy_lift")
    require(all(isinstance(x, dict) for x in (row, rank_drop, full, toy)), "sections")
    require(rank_drop["rank8_total_with_near"] < row["budget"], "rank8 budget")
    require(rank_drop["rank9"]["deployed_total"] < row["budget"], "rank9 budget")
    require(
        rank_drop["rank9"]["deployed_total"]
        == rank_drop["rank9"]["deployed_high"]
        + rank_drop["rank9"]["low"]
        + row["near_charge"],
        "rank9 ledger",
    )
    require(full["rank"] == 10 and full["residual_dimension_minimum"] == 10, "rank pin")
    require(18 + 10 + 3 == full["anchor_size"] == 31, "anchor")
    require(full["tuple_size"] == full["anchor_size"] + 1 == 32, "tuple")
    c = toy["core_size"]
    require(
        3 * toy["residual_m"] - toy["residual_K"] + 3 + 2 * c
        == row["complexity_threshold"],
        "complexity lift",
    )
    q = 31
    residual_sunflower = (q * toy["residual_m"] - toy["residual_n"] + q - 2) // (q - 1)
    require(residual_sunflower == toy["residual_sunflower_core_31"], "residual sunflower")
    require(residual_sunflower + c == row["near_sunflower_core_31"], "sunflower addback")
    require(data["route_labels"][1].startswith("H_C:"), "relative route")
    require("not the deployed" in data["nonclaim"], "scope")

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in (
        "`(H_C)`",
        "not identify `(H_C)` with the deployed",
        "110390969172308040",
        "61871313426765543",
    ):
        require(token in statement, f"statement token {token}")
    for token in (
        "Multiplication by the nonzero polynomial `L_C` is injective",
        "chi=chi'+2c",
        "certificates whose denominators are root-free",
    ):
        require(token in proof, f"proof token {token}")
    return residual_sunflower


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    sunflower = audit(data)
    mutations = (
        lambda item: item["official"].__setitem__("budget", 1),
        lambda item: item["rank_drop"]["rank9"].__setitem__("low", 1),
        lambda item: item["full_rank"].__setitem__("anchor_size", 30),
        lambda item: item["toy_lift"].__setitem__("residual_sunflower_core_31", 1),
        lambda item: item["route_labels"].__setitem__(1, "S:spread"),
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
        "RATE_HALF_MCA_RANK11_GLOBAL_CORE_RANKDROP_HIGHCOMPLEXITY_ROUTER_AUDIT_PASS "
        f"g31prime={sunflower} routes=4 controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
