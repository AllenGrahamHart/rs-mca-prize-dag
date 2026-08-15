#!/usr/bin/env python3
"""Verify the full circuit-deficit rank-nine shadow ledger."""

from __future__ import annotations

import copy
import hashlib
import json
from itertools import product
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "2a03a7595972ebd3708a681012fbd78799ea7132326d149d41d6534adfc1c69c"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema") == "rate-half-mca-rank9-full-circuit-deficit-ledger-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == [
            "rate_half_mca_rank9_sparse_shadow_joint_ledger",
            "rate_half_mca_sparse_circuit_universal_completion_incidence_cap",
        ],
        "dependencies",
    )
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    supports = list(range(2, 12))
    shadows = [55 - comb(11 - c, 2) for c in supports]
    deficits = [comb(11 - c, 2) for c in supports]
    require(p.get("component_subset_size") == 11, "component")
    require(p.get("shadow_subset_size") == 9, "shadow")
    require(p.get("total_shadow_count") == 55, "total")
    require(p.get("circuit_supports") == supports, "supports")
    require(p.get("rank9_shadow_counts") == shadows, "shadows")
    require(p.get("deficit_weights") == deficits, "deficits")
    require(all(x + y == 55 for x, y in zip(shadows, deficits)), "partition")
    require(deficits[-2:] == [0, 0], "zero deficits")
    require(
        p.get("joint_capacity_formula")
        == "floor((G+R*max_a(sum_(c=2)^9(C(11-c,2)*L_a_c)))/55)",
        "formula",
    )

    branch_checks = 0
    branch_vectors = ((1, 0, 2, 1, 0, 1, 0, 1), (0, 2, 1, 0, 2, 0, 1, 0))
    weights = deficits[:8]
    branch_max = max(
        sum(weight * cap for weight, cap in zip(weights, branch))
        for branch in branch_vectors
    )
    for branch in branch_vectors:
        for incidences in product(*(range(cap + 1) for cap in branch)):
            marked = sum(
                shadows[index] * count for index, count in enumerate(incidences)
            )
            deficit = sum(weight * count for weight, count in zip(weights, incidences))
            total = sum(incidences)
            require(55 * total == marked + deficit, "ledger identity")
            require(deficit <= branch_max, "branch maximum")
            branch_checks += 1
    require("No rank-nine chart cap" in str(data.get("nonclaim")), "nonclaim")
    return {"supports": len(supports), "branch_checks": branch_checks}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("total_shadow_count", 45),
        lambda item: item["parameters"]["rank9_shadow_counts"].__setitem__(0, 18),
        lambda item: item["parameters"]["deficit_weights"].__setitem__(4, 9),
        lambda item: item["parameters"].__setitem__("circuit_supports", list(range(2, 10))),
        lambda item: item["parameters"].__setitem__("joint_capacity_formula", "divide by 54"),
        lambda item: item.__setitem__("nonclaim", "rank-nine chart cap supplied"),
    )
    rejected = 0
    for mutation in mutations:
        hostile = copy.deepcopy(data)
        mutation(hostile)
        try:
            validate(hostile)
        except (Reject, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "tamper controls")
    return rejected


def main() -> None:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    controls = tamper_selftest(data)
    print(
        "RATE_HALF_MCA_RANK9_FULL_CIRCUIT_DEFICIT_LEDGER_PASS "
        f"supports={result['supports']} branch_checks={result['branch_checks']} "
        f"controls={controls}"
    )


if __name__ == "__main__":
    main()
