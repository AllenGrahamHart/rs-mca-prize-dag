#!/usr/bin/env python3
"""Independent null-relation audit for the support-wise compiler."""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "79c81b807ab3e176fdedff84a8cb2d204a8236fff2b001738c826488ce7d46c6"
CONTROL = HERE.parent / "rate_half_mca_record_local_core_owner_noninvariance" / "source_contract.json"
CONTROL_SHA256 = "7a27aef1521b42bc9704c97345be34263e8b22980b5e7fd65f84560b92ff6c94"


class Reject(ValueError):
    pass


def evaluate(poly: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def j_value(reserve: int, defect: int, s: int) -> int:
    return math.prod(reserve + index for index in range(s + 1)) // math.prod(
        defect + index for index in range(s + 1)
    )


def audit(contract: object, control: object) -> dict[str, int]:
    if not isinstance(contract, dict) or not isinstance(control, dict):
        raise Reject("objects")
    p = control.get("field")
    domain = tuple(control.get("domain", ()))
    line = control.get("received_line", {})
    u = tuple(line.get("u", ()))
    v = tuple(line.get("v", ()))
    explanations = control.get("explanations", ())
    if p != 11 or len(explanations) != 7:
        raise Reject("fixture")
    short_domain = tuple(x for x in domain if x != 10)
    v2 = tuple((v[i] - v[-1]) * pow((x - 10) % p, -1, p) % p for i, x in enumerate(short_domain))
    relation_checks = 0
    for item in explanations:
        support = tuple(x for x in item.get("maximal_support", ()) if x != 10)
        normals = [
            (v2[short_domain.index(x)],) + tuple((-pow(x, degree, p)) % p for degree in range(4))
            for x in support
        ]
        nulls = 0
        for vector in itertools.product(range(p), repeat=5):
            relation_checks += 1
            if all(sum(a * b for a, b in zip(vector, row)) % p == 0 for row in normals):
                nulls += 1
        if nulls != 1:
            raise Reject("nonzero normal relation")

    direction_best = 0
    for coefficients in itertools.product(range(p), repeat=4):
        direction_best = max(
            direction_best,
            sum(evaluate(coefficients, x, p) == value for x, value in zip(short_domain, v2)),
        )
    gf11 = contract.get("gf11_control", {})
    if direction_best != gf11.get("direction_max_agreement") or not gf11.get("direction_separation_fails"):
        raise Reject("direction control")

    for row in contract.get("deployed_boundaries", ()):
        reserve, defect = row.get("R"), row.get("d")
        if (
            j_value(reserve, defect, row.get("last_paid_s")) != row.get("J_last")
            or j_value(reserve, defect, row.get("first_unpaid_s")) != row.get("J_first_unpaid")
            or not row.get("J_last") <= row.get("B_star") < row.get("J_first_unpaid")
        ):
            raise Reject("boundary")
    return {"relations": relation_checks, "direction_max": direction_best}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    if hashlib.sha256(CONTROL.read_bytes()).hexdigest() != CONTROL_SHA256:
        raise Reject("control hash")
    contract = json.loads(CONTRACT.read_text())
    control = json.loads(CONTROL.read_text())
    result = audit(contract, control)
    controls = []
    changed = copy.deepcopy(contract)
    changed["gf11_control"]["direction_max_agreement"] = 5
    try:
        audit(changed, control)
    except Reject:
        controls.append(True)
    else:
        controls.append(False)
    for index, key in ((0, "J_first_unpaid"), (1, "J_last")):
        changed = copy.deepcopy(contract)
        changed["deployed_boundaries"][index][key] += 1
        try:
            audit(changed, control)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_SUPPORTWISE_AFFINE_SPAN_COMPILER_AUDIT_PASS "
        f"relation_checks={result['relations']} direction_max={result['direction_max']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
