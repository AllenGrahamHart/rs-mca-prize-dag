#!/usr/bin/env python3
"""Verify the exact affine-span MCA incidence counterexample."""

from __future__ import annotations

import copy
import hashlib
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "7c0d75814b99fa6272e8c005ee93fd78220bb5717ea9211a84dec67c0bcd9f8a"


class Reject(ValueError):
    pass


def construct(p: int) -> tuple[list[int], list[int], list[tuple[int, int]]]:
    q = [0] * 100
    r0 = [0] * 100
    slopes = list(range(1, 31))
    for i, x in enumerate(range(20, 50), 1):
        q[x] = i
        r0[x] = (-i * i) % p

    used = set(range(31))
    candidate = 31
    for x in range(50, 71):
        while candidate in used or any((1 + slope * candidate) % p == 0 for slope in slopes):
            candidate += 1
        q[x] = candidate
        r0[x] = 1
        used.add(candidate)
        candidate += 1

    for x in range(71, 100):
        while candidate in used:
            candidate += 1
        q[x] = candidate
        used.add(candidate)
        forbidden = {0, 1} | {(-slope * candidate) % p for slope in slopes}
        r0[x] = next(value for value in range(2, p) if value not in forbidden)
        candidate += 1
    return r0, q, [(slope, 0) for slope in slopes] + [(0, 1)]


def rank_two(normals: list[tuple[int, int]], p: int) -> bool:
    first = normals[0]
    return any((first[0] * b - first[1] * a) % p for a, b in normals[1:])


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {
        "schema", "field", "row", "partition", "selected", "expected"
    }:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-affine-span-incidence-counterexample-v1":
        raise Reject("version")
    p = contract["field"]
    if p != 1009 or any(p % divisor == 0 for divisor in range(2, int(p**0.5) + 1)):
        raise Reject("field")
    if contract["row"] != {"n": 100, "K": 1, "m": 21, "w": 20, "affine_dimension": 1}:
        raise Reject("row")

    r0, q, selected = construct(p)
    support_sizes = []
    for slope, explanation in selected:
        support = [
            x for x in range(100)
            if (r0[x] + slope * q[x] - explanation) % p == 0
        ]
        support_sizes.append(len(support))
        if len(support) != 21:
            raise Reject("maximal support")
        if len({r0[x] for x in support}) == 1 and len({q[x] for x in support}) == 1:
            raise Reject("pair containment")
        normals = [(q[x], -1 % p) for x in support]
        if not rank_two(normals, p):
            raise Reject("incident rank")

    direction_max = max(Counter(q).values())
    n, m, w = 100, 21, 20
    affine_bound = n * (n - 1) // (m * w)
    support_bound = (100 * 99 - 20 * 19) // (21 * 20)
    observed = {
        "support_size": min(support_sizes),
        "direction_max_agreement": direction_max,
        "affine_rank": len({explanation for _, explanation in selected}) - 1,
        "affine_span_bound": affine_bound,
        "support_bound": support_bound,
        "minimum_direction_support": 100 - direction_max,
    }
    if observed != contract["expected"]:
        raise Reject("expected")
    if len(selected) != contract["selected"]["count"] or not len(selected) > affine_bound > support_bound:
        raise Reject("violation")
    return {"slopes": len(selected), "supports": len(support_sizes)}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = validate(contract)
    controls = []
    for section, key in (
        ("expected", "support_size"),
        ("expected", "direction_max_agreement"),
        ("expected", "affine_span_bound"),
        ("selected", "count"),
    ):
        changed = copy.deepcopy(contract)
        changed[section][key] += 1
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_AFFINE_SPAN_INCIDENCE_COUNTEREXAMPLE_PASS "
        f"slopes={result['slopes']} supports={result['supports']} "
        f"mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
