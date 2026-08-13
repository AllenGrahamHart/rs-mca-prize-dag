#!/usr/bin/env python3
"""Independent exhaustive integer audit of the direction-distance router."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "1ca9c942f8e60deb9ffc7998a826cd32e9ba38bac106ffb0039828986d009bdf"


class Reject(ValueError):
    pass


def audit(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict):
        raise Reject("contract")
    total_candidates = 0
    all_spikes = 0
    for row in contract.get("rows", ()):
        R, d, budget = row.get("R"), row.get("d"), row.get("budget")
        start, last = row.get("direction_start_s"), row.get("direction_last_s")
        if not all(isinstance(value, int) for value in (R, d, budget, start, last)):
            raise Reject("row types")
        observed_spikes = []
        observed_max = (-1, -1, -1)
        endpoints = []
        for s in range(start, last + 1):
            n = R + s
            d0 = d * d - (R - 2 * d) * s
            if d0 <= 0:
                raise Reject("positive range")
            positivity_last = -1
            paid_last = -1
            for j in range(d):
                denominator = d0 - n * j
                if denominator <= 0:
                    break
                positivity_last = j
                total_candidates += 1
                numerator = n * (d - j)
                if numerator < (budget + 1) * denominator:
                    paid_last = j
                    value = numerator // denominator
                    if value > observed_max[0]:
                        observed_max = (value, s, j)
            if paid_last < 0:
                raise Reject("no paid defect")
            if paid_last < positivity_last:
                observed_spikes.append([s, positivity_last, paid_last])
            if s in (start, last):
                endpoints.append(paid_last)
        if d * d - (R - 2 * d) * (last + 1) > 0:
            raise Reject("first nonpositive")
        if endpoints != [row.get("start_threshold_j"), row.get("last_threshold_j")]:
            raise Reject("endpoints")
        if observed_max != (
            row.get("maximum_paid_bound"), row.get("maximum_at_s"), row.get("maximum_at_j")
        ):
            raise Reject("maximum")
        if observed_spikes != row.get("positivity_spikes"):
            raise Reject("spikes")
        all_spikes += len(observed_spikes)
    return {"candidates": total_candidates, "spikes": all_spikes}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = audit(contract)
    controls = []
    for index, key in ((0, "maximum_at_s"), (1, "maximum_at_j")):
        changed = copy.deepcopy(contract)
        changed["rows"][index][key] += 1
        try:
            audit(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    changed = copy.deepcopy(contract)
    changed["rows"][1]["positivity_spikes"][0][2] += 1
    try:
        audit(changed)
    except Reject:
        controls.append(True)
    else:
        controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_GLOBAL_CORE_DIRECTION_DISTANCE_ROUTER_AUDIT_PASS "
        f"candidates={result['candidates']} spikes={result['spikes']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
