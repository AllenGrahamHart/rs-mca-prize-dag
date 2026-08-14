#!/usr/bin/env python3
"""Independent semantic audit for the relative correction-space router."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "fdcd7e4edc3b587ca22390e620c6dc9f35af64763c520bf3cc0978819c70a43a"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> tuple[int, int]:
    require(isinstance(data, dict), "contract")
    row, proper, clone = (data.get(key) for key in ("official", "proper", "clone_tolerant"))
    require(all(isinstance(x, dict) for x in (row, proper, clone)), "sections")
    proper_caps = proper["caps"]
    clone_caps = clone["caps"]
    require(len(proper_caps) == 12 and len(clone_caps) == 10, "lengths")
    require(max(entry["cap"] for entry in proper_caps[:11]) < row["budget"], "proper payment")
    require(proper_caps[11]["cap"] > row["budget"], "proper wall")
    require(max(entry["cap"] for entry in clone_caps[:9]) < row["budget"], "clone payment")
    require(clone_caps[9]["cap"] > row["budget"], "clone wall")
    require(proper_caps[10]["worst_K"] == 11 and proper_caps[11]["worst_K"] == 12, "admissibility")
    require(data["routes"][0].startswith("DIM_GE_12"), "dimension route")
    require(data["routes"][3].startswith("ABSORB_HIGH"), "absorption route")

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in ("through `s=11`", "first adjacent method wall", "through `s=9`"):
        require(token in statement, f"statement token {token}")
    for token in (
        "Each factor decreases with `K'`",
        "evaluation rank-flat and exact polynomial clone alternatives",
        "|C_B| <= K'-a",
    ):
        require(token in proof, f"proof token {token}")
    return proper_caps[10]["cap"], clone_caps[8]["cap"]


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    proper11, clone9 = audit(data)
    mutations = (
        lambda item: item["official"].__setitem__("budget", 1),
        lambda item: item["proper"]["caps"][11].__setitem__("cap", 1),
        lambda item: item["clone_tolerant"]["caps"][9].__setitem__("cap", 1),
        lambda item: item["proper"]["caps"][10].__setitem__("worst_K", 10),
        lambda item: item["routes"].__setitem__(0, "PAID"),
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
        "RATE_HALF_MCA_RANK11_RELATIVE_CORRECTION_SPACE_ROUTER_AUDIT_PASS "
        f"proper11={proper11} clone9={clone9} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
