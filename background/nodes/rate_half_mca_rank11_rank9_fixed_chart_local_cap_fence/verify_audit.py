#!/usr/bin/env python3
"""Independent audit of the weighted affine-plane countermodel."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "1cb156081477cb7438193899419d8c537054a9ee4570d5f6fdb5ec03868cdeca"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def toy_geometry() -> tuple[int, int]:
    heavy_count, light_count = 3, 5
    heavy = [(i * light_count, 0) for i in range(heavy_count)]
    light = [(j, 1) for j in range(light_count)]
    directions = set()
    checks = 0
    all_points = heavy + light
    for i, point_p in enumerate(heavy):
        for j, point_q in enumerate(light):
            gamma = point_p[0] - point_q[0]
            require(gamma not in directions, "toy direction collision")
            directions.add(gamma)
            constant = point_p[0]
            incident = [
                point for point in all_points
                if point[0] + gamma * point[1] == constant
            ]
            require(incident == [point_p, point_q], "toy collateral point")
            checks += 1
    return len(directions), checks


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    p = json.loads(CONTRACT.read_text())["parameters"]
    j = p["K"] - 1
    outside = p["n"] - j
    support = p["m"] - j
    heavy = support - 1
    light = outside - p["heavy_owner_count"] * heavy
    intervals = [
        (i * light - (light - 1), i * light)
        for i in range(p["heavy_owner_count"])
    ]
    for left, right in zip(intervals, intervals[1:]):
        require(left[1] + 1 == right[0], "difference intervals")
    interval_count = sum(high - low + 1 for low, high in intervals)
    require(interval_count == p["rich_slope_count"], "interval count")
    require(j + heavy + 1 == p["m"], "support reconstruction")
    require(j + heavy < p["m"], "pair containment fence")
    require(j + heavy > p["K"] - 1, "pair root bound")
    require(p["base_prime"] > p["forbidden_slope_count"] * interval_count, "translate count")
    toy_directions, toy_checks = toy_geometry()
    proof = (HERE / "proof.md").read_text()
    require("8M=4070408" in proof and "error affine rank" in proof, "proof pins")
    print(
        "RATE_HALF_MCA_RANK11_RANK9_FIXED_CHART_LOCAL_CAP_FENCE_AUDIT_PASS "
        f"intervals={len(intervals)} slopes={interval_count} "
        f"toy={toy_directions}/{toy_checks}"
    )


if __name__ == "__main__":
    main()
