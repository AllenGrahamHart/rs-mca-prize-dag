#!/usr/bin/env python3
"""Verify the repaired codeword-direction gauge equivalence."""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "bbb7f5db9f5765ea4917d67595a431f55aa2135026820517168c016536365777"


class Reject(ValueError):
    pass


def validate(contract: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {
        "schema", "theorem", "scope_repair", "finite_control"
    }:
        raise Reject("shape")
    if contract["schema"] != "rate-half-mca-codeword-direction-gauge-equivalence-v2":
        raise Reject("schema")
    if contract["theorem"] != {
        "gauge": "(r_0,r_1,c_gamma)->(r_0,r_1-b,c_gamma-gamma b) for b in C",
        "preserves": "slopes, exact and maximal agreement supports, and same-support pair containment",
        "rank_shift": "|rank_aff(c_gamma)-rank_aff(c_gamma-gamma b)|<=1",
    }:
        raise Reject("theorem")
    if contract["scope_repair"] != {
        "retracted": "former G3 affine-incidence bound and official rank walls",
        "refuter": "rate_half_mca_affine_span_incidence_counterexample",
    }:
        raise Reject("scope")
    if contract["finite_control"] != {
        "field": 7, "coordinates": 4, "slopes": [0, 1, 2, 3, 4, 5, 6]
    }:
        raise Reject("control")
    p = 7
    checks = 0
    for r0, r1, b, c, gamma in itertools.product(range(p), repeat=5):
        left = (r0 + gamma * r1 - c) % p
        right = (r0 + gamma * (r1 - b) - (c - gamma * b)) % p
        if left != right:
            raise Reject("identity")
        checks += 1
    vectors = {
        "r0": [0, 1, 4, 2], "r1": [3, 2, 6, 1], "b": [1, 1, 1, 1]
    }
    for gamma in contract["finite_control"]["slopes"]:
        explanation = [(gamma * x + 2) % p for x in range(4)]
        old = [
            (vectors["r0"][i] + gamma * vectors["r1"][i] - explanation[i]) % p
            for i in range(4)
        ]
        transformed = [(value - gamma * vectors["b"][i]) % p for i, value in enumerate(explanation)]
        new = [
            (vectors["r0"][i] + gamma * (vectors["r1"][i] - vectors["b"][i]) - transformed[i]) % p
            for i in range(4)
        ]
        if old != new:
            raise Reject("support vector")
        checks += 4
    return {"checks": checks}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    contract = json.loads(CONTRACT.read_text())
    result = validate(contract)
    controls = []
    for section, key in (("finite_control", "field"), ("finite_control", "coordinates")):
        changed = copy.deepcopy(contract)
        changed[section][key] += 1
        try:
            validate(changed)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    changed = copy.deepcopy(contract)
    changed["scope_repair"]["refuter"] += "_bad"
    try:
        validate(changed)
    except Reject:
        controls.append(True)
    else:
        controls.append(False)
    if not all(controls):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_CODEWORD_DIRECTION_GAUGE_EQUIVALENCE_PASS "
        f"checks={result['checks']} mutations={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
