#!/usr/bin/env python3
"""Independent exhaustive audit of the whole-line global-core router."""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "ff1e82e71742f132bd3bd39ccc5540cff8676c9b8b1b79d094cb9615b0d7ab16"
CONTROL = HERE.parent / "rate_half_mca_record_local_core_owner_noninvariance" / "source_contract.json"
CONTROL_SHA256 = "7a27aef1521b42bc9704c97345be34263e8b22980b5e7fd65f84560b92ff6c94"


class Reject(ValueError):
    pass


def evaluate(poly: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def audit(contract: object, control: object) -> dict[str, int]:
    if not isinstance(contract, dict) or not isinstance(control, dict):
        raise Reject("objects")
    p = control.get("field")
    domain = tuple(control.get("domain", ()))
    u = tuple(control.get("received_line", {}).get("u", ()))
    v = tuple(control.get("received_line", {}).get("v", ()))
    selected = tuple(contract.get("gf11_control", {}).get("selected_slopes", ()))
    explanations = {
        item.get("slope"): item
        for item in control.get("explanations", ())
        if item.get("slope") in selected
    }
    if p != 11 or len(explanations) != 7:
        raise Reject("fixture")
    core = set(domain)
    for item in explanations.values():
        core &= set(item.get("maximal_support", ()))
    if core != {10} or core != set(contract["gf11_control"]["global_core"]):
        raise Reject("global core")
    shortened_domain = tuple(x for x in domain if x != 10)
    u2 = tuple((u[i] - u[-1]) * pow((x - 10) % p, -1, p) % p for i, x in enumerate(shortened_domain))
    v2 = tuple((v[i] - v[-1]) * pow((x - 10) % p, -1, p) % p for i, x in enumerate(shortened_domain))

    codewords_checked = 0
    for slope in selected:
        word = tuple((a + slope * b) % p for a, b in zip(u2, v2))
        found = []
        for coefficients in itertools.product(range(p), repeat=4):
            support = tuple(
                x
                for x, value in zip(shortened_domain, word)
                if evaluate(coefficients, x, p) == value
            )
            codewords_checked += 1
            if len(support) >= 6:
                found.append((coefficients, support))
        if len(found) != 1:
            raise Reject("shortened list")
        expected_support = set(explanations[slope]["maximal_support"]) - {10}
        if set(found[0][1]) != expected_support:
            raise Reject("shortened support")

    official = contract.get("official_koalabear_boundaries", {})
    n, k, m = official.get("n"), official.get("k"), official.get("m")
    if (n, k, m) != (2097152, 1048576, 1116048):
        raise Reject("official row")
    reserve, defect = n - k, m - k
    b2 = min(math.comb(reserve + 2, defect + 2), math.comb(reserve + 2, 3))
    b3 = min(math.comb(reserve + 3, defect + 3), math.comb(reserve + 3, 4))
    def j_value(s: int) -> int:
        return math.prod(reserve + i for i in range(s + 1)) // math.prod(
            defect + i for i in range(s + 1)
        )
    if (b2, b3, j_value(13), j_value(14)) != (
        official.get("B_cell_s2"),
        official.get("B_cell_s3"),
        official.get("J_13"),
        official.get("J_14"),
    ):
        raise Reject("official walls")
    return {"slopes": len(selected), "codewords": codewords_checked}


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    if hashlib.sha256(CONTROL.read_bytes()).hexdigest() != CONTROL_SHA256:
        raise Reject("control hash")
    contract = json.loads(CONTRACT.read_text())
    control = json.loads(CONTROL.read_text())
    result = audit(contract, control)
    controls = []
    for key, value in (
        ("B_cell_s2", contract["official_koalabear_boundaries"]["B_cell_s2"] + 1),
        ("J_13", contract["official_koalabear_boundaries"]["J_13"] - 1),
    ):
        changed = copy.deepcopy(contract)
        changed["official_koalabear_boundaries"][key] = value
        try:
            audit(changed, control)
        except Reject:
            controls.append(True)
        else:
            controls.append(False)
    changed_control = copy.deepcopy(control)
    changed_control["explanations"][0]["maximal_support"][-1] = 9
    try:
        audit(contract, changed_control)
    except Reject:
        controls.append(True)
    else:
        controls.append(False)
    if not all(controls):
        raise AssertionError("audit controls")
    print(
        "RATE_HALF_MCA_WHOLE_LINE_GLOBAL_CORE_ROUTER_AUDIT_PASS "
        f"slopes={result['slopes']} codewords={result['codewords']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
