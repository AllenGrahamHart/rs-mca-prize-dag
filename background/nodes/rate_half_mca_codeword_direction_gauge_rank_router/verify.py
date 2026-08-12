#!/usr/bin/env python3
"""Verify the codeword-direction gauge rank router."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "eb086905c8b2f89769a5407875a8019f4cf7d9d04062aaf7e299efe22a9581a6"
PINNED = {
    "background/nodes/rate_half_mca_supportwise_affine_span_compiler/statement.md": "08bd599c71cf40b4ee53a7eb7483f0b16f99f77616234ceb737ce08301922190",
    "background/nodes/rate_half_mca_supportwise_affine_span_compiler/proof.md": "97915ef59268ab5c1eb64e31b6947c6380ce2ee9cebbd95b61f66153d18e9ae3",
    "background/nodes/rate_half_mca_global_core_direction_distance_router/statement.md": "0bdbd9585b37372cd9ff4ccc708d28ad1e3c2d28dc45e93f151b934e99ada8df",
    "background/nodes/rate_half_mca_global_core_direction_distance_router/proof.md": "22844c8398ab217e5bf238be97edd64c9e939d7803c4a40b0e31b95176641196",
}


class Reject(ValueError):
    pass


def falling(value: int, count: int) -> int:
    return math.prod(value - index for index in range(count))


def rising(value: int, count: int) -> int:
    return math.prod(value + index for index in range(count))


def affine_bound(R: int, d: int, K: int, rank: int) -> int:
    term1 = falling(R + K, rank + 1) // ((d + K) * rising(d, rank))
    term2 = falling(R + rank, rank + 1) // rising(d, rank + 1)
    return max(term1, term2)


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "theorem", "rows"}:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-codeword-direction-gauge-rank-router-v1":
        raise Reject("version")
    if contract["sources"] != {
        "supportwise_span": "rate_half_mca_supportwise_affine_span_compiler",
        "global_direction_router": "rate_half_mca_global_core_direction_distance_router",
    }:
        raise Reject("sources")
    if contract["theorem"] != {
        "gauge": "(r_0,r_1,c_gamma)->(r_0,r_1-b,c_gamma-gamma b) for b in C",
        "preserves": "slopes, exact agreement supports, and same-support pair noncontainment",
        "rank_shift": "|rank_aff(c_gamma)-rank_aff(c_gamma-gamma b)|<=1",
        "bound": "floor(max((R+K)_fall_(r+1)/((d+K)d_rise_r),(R+r)_fall_(r+1)/d_rise_(r+1)))",
    }:
        raise Reject("theorem")
    expected = {
        "KoalaBear MCA": (
            1048576, 67472, 274980728111395087, 1048576,
            [(11, 1048576, 49107626893329409, None, None),
             (12, 745260, 274980259855184513, 745261, 274981914318597687),
             (13, 289603, 274980152556476265, 289604, 274982259324238595),
             (14, None, None, 14, 743896698428332665)],
        ),
        "Mersenne-31 MCA": (
            1048576, 67448, 16777215, 1048576,
            [(4, 1048576, 1756139, None, None),
             (5, 482472, 16777192, 482473, 16777228),
             (6, None, None, 6, 219426634)],
        ),
    }
    scans = 0
    for row in contract["rows"]:
        walls = [
            (
                item.get("rank"), item.get("last_paid_K"), item.get("bound_last"),
                item.get("first_unpaid_K"), item.get("bound_first_unpaid"),
            )
            for item in row.get("rank_walls", ())
        ]
        values = (row.get("R"), row.get("d"), row.get("budget"), row.get("ambient_cap"), walls)
        if values != expected.get(row.get("name")):
            raise Reject("row constants")
        R, d, budget, cap, _ = values
        for rank, last, bound_last, first, bound_first in walls:
            observed_last = None
            seen_increase = False
            previous_term = None
            for K in range(rank, cap + 1):
                current = affine_bound(R, d, K, rank)
                scans += 1
                term1 = falling(R + K, rank + 1) // ((d + K) * rising(d, rank))
                if previous_term is not None:
                    if term1 > previous_term:
                        seen_increase = True
                    elif seen_increase and term1 < previous_term:
                        raise Reject("second turn")
                previous_term = term1
                if current <= budget:
                    observed_last = K
            if observed_last != last:
                raise Reject("last paid")
            if last is None:
                if first != rank or bound_last is not None:
                    raise Reject("empty interval")
            else:
                if affine_bound(R, d, last, rank) != bound_last:
                    raise Reject("last value")
                if last == cap:
                    if first is not None or bound_first is not None:
                        raise Reject("capped interval")
                    continue
                if first != last + 1:
                    raise Reject("adjacency")
            if affine_bound(R, d, first, rank) != bound_first or bound_first <= budget:
                raise Reject("first unpaid")
    return {"scans": scans}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINNED.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"source pin: {relative}")
    contract = json.loads(CONTRACT.read_text())
    result = validate(contract)
    controls = []
    for row_index, wall_index, key in (
        (0, 1, "last_paid_K"), (0, 2, "bound_first_unpaid"),
        (1, 1, "bound_last"),
    ):
        changed = copy.deepcopy(contract)
        changed["rows"][row_index]["rank_walls"][wall_index][key] += 1
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    changed = copy.deepcopy(contract)
    changed["rows"][1]["rank_walls"][2]["last_paid_K"] = 5
    try:
        validate(changed)
    except Reject:
        controls.append(True)
    else:
        controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_CODEWORD_DIRECTION_GAUGE_RANK_ROUTER_PASS "
        f"scans={result['scans']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
