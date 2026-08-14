#!/usr/bin/env python3
"""Independent audit for the absorbing clone-to-affine collapse."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "345259da825c04a6634a371abf6ba4d3857c880271088824e619e83be8f8df8a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> int:
    require(isinstance(data, dict), "contract")
    dimensions, invariants = (data.get(key) for key in ("dimensions", "invariants"))
    require(isinstance(dimensions, dict) and isinstance(invariants, dict), "sections")
    require(dimensions["received_line_degree"] == 1, "received degree")
    require(dimensions["slope_degree_maximum"] == 31, "core degree")
    require(invariants["affine_owner_cap"] == invariants["R"] - invariants["d"] + 1, "cap")
    require(data["routes"] == ["AFFINE_OWNER_COMPONENT", "EVALUATION_RANK_FLAT"], "routes")

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in ("P_(B,j)=-H_j", "global affine codeword owner line", "does not sum"):
        require(token in statement, f"statement token {token}")
    for token in (
        "Their sum is therefore a word of `W`",
        "All coefficients of `H+P_B`",
        "Different clone components may",
    ):
        require(token in proof, f"proof token {token}")
    return invariants["affine_owner_cap"]


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    cap = audit(data)
    mutations = (
        lambda item: item["dimensions"].__setitem__("received_line_degree", 2),
        lambda item: item["invariants"].__setitem__("affine_owner_cap", 1),
        lambda item: item["routes"].append("CLONE"),
        lambda item: item["routes"].pop(0),
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
        "RATE_HALF_MCA_RANK11_RELATIVE_ABSORBING_CLONE_AFFINE_COLLAPSE_AUDIT_PASS "
        f"owner_cap={cap} routes=2 controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
