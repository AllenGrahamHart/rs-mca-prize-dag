#!/usr/bin/env python3
"""Independent audit for the fixed rank-nine split-pencil ledger."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "150863c70ede9590605eaa93eb97a16da4edb6883d6ede80c60c1c12d9795cf3"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> tuple[int, int]:
    require(isinstance(data, dict), "contract")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require(p["cell_size"] - p["cell_rank"] == p["kernel_dimension"] == 1, "rank")
    owner = p["n_minus_k"] - p["m_minus_k"] + 1
    require(owner == p["n_minus_m"] + 1 == p["fixed_owner_slope_cap"], "owner")
    petal = p["n_max"] - p["cell_size"]
    weighted = owner * petal
    require(weighted == p["weighted_petal_incidence_cap"], "petal")
    cell = (weighted + p["extension_floor"] - 1) // p["extension_floor"]
    require(cell == p["fixed_cell_record_cap"], "cell")
    require(len(data["identities"]) == 4, "identities")

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in ("sum_p C(t_p,2)=C(g,2)", "45153*g", "45567659"):
        require(token in statement, f"statement token {token}")
    for token in (
        "is a bijection from the parameter plane",
        "Summing extension incidences",
        "local to one fixed `B`",
    ):
        require(token in proof, f"proof token {token}")
    return weighted, cell


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    weighted, cell = audit(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("cell_size", 11),
        lambda item: item["parameters"].__setitem__("n_minus_m", 981103),
        lambda item: item["parameters"].__setitem__("weighted_petal_incidence_cap", 2057516501909),
        lambda item: item["parameters"].__setitem__("fixed_cell_record_cap", 45567660),
        lambda item: item["identities"].pop(),
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
        "RATE_HALF_MCA_RANK11_RANK9_SPLIT_PENCIL_CELL_LEDGER_AUDIT_PASS "
        f"weighted={weighted} cell={cell} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
