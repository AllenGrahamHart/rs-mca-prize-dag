#!/usr/bin/env python3
"""Independent audit for the relative correction ten-flat collapse."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "803cc5f5f922ffae6fe3b50439edf3baf73b1f4dd7e556e96e5361a8b22dcbec"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> tuple[int, int]:
    require(isinstance(data, dict), "contract")
    dimensions = data.get("dimensions")
    require(isinstance(dimensions, dict), "dimensions")
    lower = dimensions["correction_minimum_after_core_ray_payment"]
    upper = dimensions["correction_maximum"]
    require((lower, upper) == (2, 10), "range")
    require(upper == dimensions["deviation_space"], "containment cap")
    require(upper < dimensions["proper_paid_through"], "proper payment")
    require(dimensions["clone_tolerant_nonabsorbing_paid_through"] == upper - 1, "absorption")
    require(len(data["containments"]) == 4, "containments")
    require(all("ABSORB_HIGH" in route for route in data["routes"]), "routes")

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in ("W=span{P_gamma} <= V'", "`2<=dim W<=10`", "dimension-at-least-12"):
        require(token in statement, f"statement token {token}")
    for token in (
        "every coefficient of `D_H` belongs to",
        "If `dim W=1`",
        "two ten-dimensional spaces is equality",
    ):
        require(token in proof, f"proof token {token}")
    return lower, upper


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    lower, upper = audit(data)
    mutations = (
        lambda item: item["dimensions"].__setitem__("correction_maximum", 12),
        lambda item: item["dimensions"].__setitem__("proper_paid_through", 10),
        lambda item: item["dimensions"].__setitem__("clone_tolerant_nonabsorbing_paid_through", 8),
        lambda item: item["containments"].pop(),
        lambda item: item["routes"].__setitem__(0, "RANK_FLAT"),
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
        "RATE_HALF_MCA_RANK11_RELATIVE_CORRECTION_TENFLAT_COLLAPSE_AUDIT_PASS "
        f"dimension={lower}..{upper} routes=2 controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
