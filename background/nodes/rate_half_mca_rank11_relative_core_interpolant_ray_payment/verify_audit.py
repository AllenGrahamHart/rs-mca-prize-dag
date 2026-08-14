#!/usr/bin/env python3
"""Independent semantic audit for the relative one-ray payment."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "3b4b70627535065aeae69d5dfcf0bea11f067557e3512f23571a11eb41b04454"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> int:
    require(isinstance(data, dict), "contract")
    row, residual, ray = (data.get(key) for key in ("official", "residual_range", "ray"))
    require(all(isinstance(x, dict) for x in (row, residual, ray)), "sections")
    n_min = row["R"] + residual["K_min"]
    m_min = row["d"] + residual["K_min"]
    require(31 * n_min // m_min == residual["core_compatible_cap"], "core")
    require((31 * n_min - 32 * m_min) // m_min == residual["extra_core_compatible_cap"], "extra")
    require(row["n"] * (row["t"] + 1) == ray["uniform_affine_charge"], "affine")
    require(31 * comb(row["n"], 2) == ray["uniform_heterogeneous_pair_charge"], "pairs")
    require(
        ray["uniform_affine_charge"] + ray["uniform_heterogeneous_pair_charge"]
        == ray["uniform_ray_cap"],
        "ray ledger",
    )
    require(residual["core_compatible_cap"] + ray["uniform_ray_cap"] == ray["core_plus_ray"], "combined")
    require(ray["core_plus_ray"] < row["budget"], "budget")

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in ("at most `449`", "70227214729216", "one projective correction ray"):
        require(token in statement, f"statement token {token}")
    for token in (
        "at most `K'-1`",
        "least one heterogeneous unordered coordinate pair",
        "pair bound is a valid slope bound",
    ):
        require(token in proof, f"proof token {token}")
    return ray["core_plus_ray"]


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    total = audit(data)
    mutations = (
        lambda item: item["residual_range"].__setitem__("extra_core_compatible_cap", 448),
        lambda item: item["ray"].__setitem__("uniform_affine_charge", 1),
        lambda item: item["ray"].__setitem__("uniform_heterogeneous_pair_charge", 1),
        lambda item: item["ray"].__setitem__("core_plus_ray", 1),
        lambda item: item["official"].__setitem__("budget", 1),
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
        "RATE_HALF_MCA_RANK11_RELATIVE_CORE_INTERPOLANT_RAY_PAYMENT_AUDIT_PASS "
        f"total={total} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
