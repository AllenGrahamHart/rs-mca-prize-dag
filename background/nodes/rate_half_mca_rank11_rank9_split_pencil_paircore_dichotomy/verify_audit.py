#!/usr/bin/env python3
"""Independent audit for the split-pencil pair-core dichotomy."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "e899fbb6893e61495371f689f6a2ca5eb196d0bbc6d6ec8dc39b34eb9965c252"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> tuple[int, int, int]:
    require(isinstance(data, dict), "contract")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    n, m = p["n"], p["m"]
    d = n - m
    ell = 2 * m - n
    require((d, ell) == (981104, 134944), "row split")

    # The hardest low-core value is j=ell-1. Exhaust every possible owner
    # core and verify the ordered-pair petal inequality directly.
    j = ell - 1
    checks = 0
    for c in range(ell, m):
        t = (n - c) // (m - c)
        require(t * (t - 1) <= (d + 1) * (c - j), f"owner core {c}")
        checks += 1
    require(checks == m - ell == 981104, "exhaustive core count")

    q = (d + 1) * (n - 10)
    g = 1434405
    require(p["petal_resource_ceiling"] == n - 10, "petal resource")
    require(q == p["ordered_pair_resource_ceiling"], "resource")
    require(g == p["low_common_core_plane_cap"], "manifest cap")
    require(g * (g - 1) <= q < (g + 1) * g, "quadratic bracket")
    require(data.get("routes") == [
        "LOW_COMMON_CORE_PLANE_CAP",
        "SHARED_PAIR_CORE_AT_LEAST_134944",
    ], "routes")

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in ("134944", "1434405", "g(g-1)"):
        require(token in statement, f"statement token {token}")
    for token in (
        "S_gamma intersection S_delta subset C_p",
        "(D-yx)+(y-1)(x-1)",
        "2057519138430",
    ):
        require(token in proof, f"proof token {token}")
    return checks, q, g


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    checks, resource, cap = audit(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("n", 2097151),
        lambda item: item["parameters"].__setitem__("m", 1116047),
        lambda item: item["parameters"].__setitem__("petal_resource_ceiling", 2097141),
        lambda item: item["parameters"].__setitem__("low_common_core_plane_cap", 1434406),
        lambda item: item["routes"].pop(),
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
        "RATE_HALF_MCA_RANK11_RANK9_SPLIT_PENCIL_PAIRCORE_DICHOTOMY_AUDIT_PASS "
        f"core_checks={checks} resource={resource} cap={cap} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
