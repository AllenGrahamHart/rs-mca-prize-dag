#!/usr/bin/env python3
"""Verify the global-core direction-distance router."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "5ad7705fd960091ce2141871c0aee4fa2d7d95add3c12649b5084cde89151598"
PINNED = {
    "background/nodes/rate_half_mca_whole_line_global_core_router/statement.md": "fc7a61d44d6ee26e76db62973669930c65dc2acc6803046da33cdc8b633e90b9",
    "background/nodes/rate_half_mca_whole_line_global_core_router/proof.md": "7f599e0e15975df8563c5832fc730e1afea63090efec1a1f8ebe66630f514578",
    "background/nodes/rate_half_mca_supportwise_affine_span_compiler/statement.md": "08bd599c71cf40b4ee53a7eb7483f0b16f99f77616234ceb737ce08301922190",
    "background/nodes/rate_half_mca_supportwise_affine_span_compiler/proof.md": "97915ef59268ab5c1eb64e31b6947c6380ce2ee9cebbd95b61f66153d18e9ae3",
    "background/nodes/xr_direction_distance_ray_bound/statement.md": "141235560ab306944b79f4ecbb9c33d59589653b2ab19ab31e65f1ed138ed963",
    "background/nodes/xr_direction_distance_ray_bound/proof.md": "5348780eb93a22964a0f8303894e045b13e017b715a5a68afbca4d7cef2f1c1e",
}


class Reject(ValueError):
    pass


def paid_threshold(R: int, d: int, budget: int, s: int) -> int:
    n = R + s
    d0 = d * d - (R - 2 * d) * s
    positivity = (d0 - 1) // n
    budget_gate = (((budget + 1) * d0 - n * d) - 1) // (budget * n)
    return min(d - 1, positivity, budget_gate)


def ray_bound(R: int, d: int, s: int, j: int) -> int | None:
    n = R + s
    denominator = d * d - (R - 2 * d) * s - n * j
    if denominator <= 0 or d <= j:
        return None
    return n * (d - j) // denominator


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "formula", "rows"}:
        raise Reject("schema")
    if contract["schema"] != "rate-half-mca-global-core-direction-distance-router-v1":
        raise Reject("version")
    if contract["sources"] != {
        "whole_line_router": "rate_half_mca_whole_line_global_core_router",
        "supportwise_span": "rate_half_mca_supportwise_affine_span_compiler",
        "direction_distance": "xr_direction_distance_ray_bound",
    }:
        raise Reject("sources")
    if contract["formula"] != {
        "shortened_row": "(N,K,m)=(R+s,s,d+s)",
        "radius": "t=R-d",
        "direction_defect": "j=R-d_U(y_1)",
        "denominator": "D_s(j)=d^2-(R-2d)s-(R+s)j",
        "bound": "floor((R+s)(d-j)/D_s(j))",
        "exact_paid_threshold": "min(d-1,floor((D_s(0)-1)/(R+s)),floor((((B+1)D_s(0)-(R+s)d)-1)/(B(R+s))))",
    }:
        raise Reject("formula")

    expected = {
        "KoalaBear MCA": (1048576, 67472, 274980728111395087, 13, 14, 4982, 4329, 0, 168818566, 1356, 3156),
        "Mersenne-31 MCA": (1048576, 67448, 16777215, 5, 6, 4979, 4333, 0, 16131678, 1970, 2617),
    }
    expected_spikes = [
        [620, 3796, 3795], [930, 3525, 3524], [1436, 3083, 3082],
        [1727, 2829, 2828], [1829, 2740, 2739], [2056, 2542, 2541],
        [2220, 2399, 2398], [2609, 2060, 2059], [3081, 1649, 1648],
        [3289, 1468, 1467], [3412, 1361, 1360], [3925, 915, 914],
        [4813, 144, 143],
    ]
    rows = contract["rows"]
    if not isinstance(rows, list) or len(rows) != 2:
        raise Reject("rows")
    dimensions = 0
    for row in rows:
        name = row.get("name")
        values = tuple(
            row.get(key)
            for key in (
                "R", "d", "budget", "span_paid_through_s", "direction_start_s",
                "direction_last_s", "start_threshold_j", "last_threshold_j",
                "maximum_paid_bound", "maximum_at_s", "maximum_at_j",
            )
        )
        if values != expected.get(name):
            raise Reject("row constants")
        R, d, budget, span_last, start, last, start_j, last_j, maximum, max_s, max_j = values
        if start != span_last + 1 or d * d - (R - 2 * d) * last <= 0:
            raise Reject("range start")
        if d * d - (R - 2 * d) * (last + 1) > 0:
            raise Reject("range end")
        spikes = []
        observed_max = (-1, -1, -1)
        for s in range(start, last + 1):
            dimensions += 1
            n = R + s
            d0 = d * d - (R - 2 * d) * s
            positivity = (d0 - 1) // n
            threshold = paid_threshold(R, d, budget, s)
            if threshold < 0:
                raise Reject("empty paid gate")
            paid = ray_bound(R, d, s, threshold)
            if paid is None or paid > budget:
                raise Reject("paid endpoint")
            next_bound = ray_bound(R, d, s, threshold + 1)
            if next_bound is not None and next_bound <= budget:
                raise Reject("nonmaximal threshold")
            if threshold < positivity:
                spikes.append([s, positivity, threshold])
            if paid > observed_max[0]:
                observed_max = (paid, s, threshold)
        if paid_threshold(R, d, budget, start) != start_j or paid_threshold(R, d, budget, last) != last_j:
            raise Reject("threshold endpoints")
        if observed_max != (maximum, max_s, max_j):
            raise Reject("maximum")
        if spikes != row.get("positivity_spikes"):
            raise Reject("spikes")
        if name == "KoalaBear MCA" and spikes:
            raise Reject("Koala spikes")
        if name == "Mersenne-31 MCA" and spikes != expected_spikes:
            raise Reject("Mersenne spikes")
    return {"dimensions": dimensions, "spikes": len(expected_spikes)}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    for relative, digest in PINNED.items():
        if hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() != digest:
            raise Reject(f"source pin: {relative}")
    contract = json.loads(CONTRACT.read_text())
    result = validate(contract)
    controls = []
    mutations = (
        (0, "maximum_paid_bound", 1),
        (1, "direction_last_s", 1),
        (1, "start_threshold_j", 1),
    )
    for index, key, delta in mutations:
        changed = copy.deepcopy(contract)
        changed["rows"][index][key] += delta
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    changed = copy.deepcopy(contract)
    changed["rows"][1]["positivity_spikes"].pop()
    try:
        validate(changed)
    except Reject:
        controls.append(True)
    else:
        controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_GLOBAL_CORE_DIRECTION_DISTANCE_ROUTER_PASS "
        f"dimensions={result['dimensions']} spikes={result['spikes']} "
        f"mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
