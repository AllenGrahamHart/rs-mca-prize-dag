#!/usr/bin/env python3
"""Verify the rank-three bounded-parallel basis-floor contract."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "a765b84a8cff00ae03d2cc33a6ad9be904200612d1628f94f5700cd94e5500fb"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def validate(data: object) -> int:
    require(isinstance(data, dict), "contract")
    require(data.get("schema") == "matroid-rank3-bounded-parallel-basis-floor-v1", "schema")
    require(data.get("dependencies") == [], "dependencies")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    require((p["rank"], p["minimum_ground_size"], p["minimum_parallel_ceiling"]) == (3, 3, 1), "range")
    require(p["loopless"] is True, "loopless")
    require(p["basis_floor"] == "2*b(M)>=(m-1)*(m-1-a)", "floor")
    require(p["induction_slack"] == "a-1", "induction slack")
    ceilings = p["audited_parallel_ceilings"]
    require(ceilings == list(range(1, 13)), "ceiling grid")

    checks = 0
    for a in ceilings:
        for m in range(3, 97):
            target = (m - 1) * (m - 1 - a)
            coloop_twice = (m - 1) * (m - 1) - a * (m - 1)
            require(coloop_twice == target, "coloop square bound")
            deletion_twice = (m - 2) * (m - 2 - a)
            require(deletion_twice + 2 * (m - 2) - target == a - 1, "induction identity")
            checks += 2
        for c in range(1, 17):
            for m in range(max(3, 3 * c), 3 * c + 17):
                require(c * (m - 2 * c) >= m - 2, "contraction floor")
                checks += 1
        for classes in range(2, 9):
            m = classes * a + 1
            bases = classes * (classes - 1) * a * a // 2
            require(2 * bases == (m - 1) * (m - 1 - a), "sharp family")
            checks += 1
    require("does not establish" in str(data.get("nonclaim")), "nonclaim")
    return checks


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    checks = validate(data)
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("rank", 4),
        lambda item: item["parameters"].__setitem__("loopless", False),
        lambda item: item["parameters"].__setitem__("basis_floor", "b(M)>=m-1"),
        lambda item: item["parameters"].__setitem__("induction_slack", "a"),
        lambda item: item["parameters"].__setitem__("audited_parallel_ceilings", list(range(1, 12))),
    )
    caught = 0
    for mutation in mutations:
        altered = copy.deepcopy(data)
        mutation(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutation controls")
    print(
        "MATROID_RANK3_BOUNDED_PARALLEL_BASIS_FLOOR_PASS "
        f"checks={checks} ceilings=12 controls={caught}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
