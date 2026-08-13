#!/usr/bin/env python3
"""Verify the scope-repaired direction-distance gate."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "1ca9c942f8e60deb9ffc7998a826cd32e9ba38bac106ffb0039828986d009bdf"
PINNED = {
    "background/nodes/rate_half_mca_whole_line_global_core_router/statement.md": "fc7a61d44d6ee26e76db62973669930c65dc2acc6803046da33cdc8b633e90b9",
    "background/nodes/xr_direction_distance_ray_bound/statement.md": "141235560ab306944b79f4ecbb9c33d59589653b2ab19ab31e65f1ed138ed963",
    "background/nodes/xr_direction_distance_ray_bound/proof.md": "5348780eb93a22964a0f8303894e045b13e017b715a5a68afbca4d7cef2f1c1e",
}


class Reject(ValueError):
    pass


def threshold(R: int, d: int, budget: int, s: int) -> int:
    n = R + s
    d0 = d * d - (R - 2 * d) * s
    positivity = (d0 - 1) // n
    budget_gate = (((budget + 1) * d0 - n * d) - 1) // (budget * n)
    return min(d - 1, positivity, budget_gate)


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {"schema", "sources", "formula", "rows"}:
        raise Reject("shape")
    if contract["schema"] != "rate-half-mca-global-core-direction-distance-gate-v2":
        raise Reject("schema")
    if contract["sources"] != {
        "whole_line_router": "rate_half_mca_whole_line_global_core_router",
        "direction_distance": "xr_direction_distance_ray_bound",
    }:
        raise Reject("sources")
    expected_formula = {
        "shortened_row": "(N,K,m)=(R+s,s,d+s)",
        "radius": "t=R-d",
        "direction_defect": "j=R-d_U(y_1)",
        "denominator": "D_s(j)=d^2-(R-2d)s-(R+s)j",
        "bound": "floor((R+s)(d-j)/D_s(j))",
        "exact_paid_threshold": "min(d-1,floor((D_s(0)-1)/(R+s)),floor((((B+1)D_s(0)-(R+s)d)-1)/(B(R+s))))",
    }
    if contract["formula"] != expected_formula:
        raise Reject("formula")
    expected = {
        "KoalaBear MCA": (1048576, 67472, 274980728111395087, 1, 4982, 4340, 0, 168818566, 1356, 3156, []),
        "Mersenne-31 MCA": (1048576, 67448, 16777215, 1, 4979, 4337, 0, 16131678, 1970, 2617,
          [[620,3796,3795],[930,3525,3524],[1436,3083,3082],[1727,2829,2828],[1829,2740,2739],[2056,2542,2541],[2220,2399,2398],[2609,2060,2059],[3081,1649,1648],[3289,1468,1467],[3412,1361,1360],[3925,915,914],[4813,144,143]]),
    }
    scans = 0
    for row in contract["rows"]:
        values = tuple(row.get(key) for key in (
            "R", "d", "budget", "direction_start_s", "direction_last_s",
            "start_threshold_j", "last_threshold_j", "maximum_paid_bound",
            "maximum_at_s", "maximum_at_j", "positivity_spikes"
        ))
        if values != expected.get(row.get("name")):
            raise Reject("row")
        R, d, budget, start, last = values[:5]
        observed_max = (-1, -1, -1)
        spikes = []
        endpoints = []
        for s in range(start, last + 1):
            n = R + s
            d0 = d * d - (R - 2 * d) * s
            j = threshold(R, d, budget, s)
            positivity = min(d - 1, (d0 - 1) // n)
            if j < 0:
                raise Reject("empty")
            denominator = d0 - n * j
            value = n * (d - j) // denominator
            if value > budget:
                raise Reject("budget")
            if j < positivity:
                spikes.append([s, positivity, j])
            if value > observed_max[0]:
                observed_max = (value, s, j)
            if s in (start, last):
                endpoints.append(j)
            scans += 1
        if d * d - (R - 2 * d) * (last + 1) > 0:
            raise Reject("terminal")
        if endpoints != [row["start_threshold_j"], row["last_threshold_j"]]:
            raise Reject("endpoints")
        if observed_max != (row["maximum_paid_bound"], row["maximum_at_s"], row["maximum_at_j"]):
            raise Reject("maximum")
        if spikes != row["positivity_spikes"]:
            raise Reject("spikes")
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
    for index, key in ((0, "start_threshold_j"), (1, "maximum_at_s")):
        changed = copy.deepcopy(contract)
        changed["rows"][index][key] += 1
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_GLOBAL_CORE_DIRECTION_DISTANCE_GATE_PASS "
        f"dimensions={result['scans']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
