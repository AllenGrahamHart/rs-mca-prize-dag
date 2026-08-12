#!/usr/bin/env python3
"""Verify the whole-line global-core cancellation router."""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "fe6d62769c4a6cbd7897087b96892f763aaf229e6169afb0ab476d18a752aaa0"
CONTROL = HERE.parent / "rate_half_mca_record_local_core_owner_noninvariance" / "source_contract.json"
CONTROL_SHA256 = "7a27aef1521b42bc9704c97345be34263e8b22980b5e7fd65f84560b92ff6c94"


class Reject(ValueError):
    pass


def trim(poly: list[int], p: int) -> tuple[int, ...]:
    out = [value % p for value in poly]
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)


def degree(poly: tuple[int, ...]) -> int:
    return len(poly) - 1


def evaluate(poly: tuple[int, ...], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def multiply(
    left: tuple[int, ...], right: tuple[int, ...], p: int
) -> tuple[int, ...]:
    if not left or not right:
        return ()
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out, p)


def divide_exact(
    numerator: tuple[int, ...], denominator: tuple[int, ...], p: int
) -> tuple[int, ...]:
    if not denominator or denominator[-1] % p == 0:
        raise Reject("division denominator")
    remainder = list(numerator)
    quotient = [0] * max(0, len(numerator) - len(denominator) + 1)
    while remainder and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        factor = remainder[-1] * pow(denominator[-1], -1, p) % p
        quotient[shift] = factor
        for index, coefficient in enumerate(denominator):
            remainder[index + shift] = (
                remainder[index + shift] - factor * coefficient
            ) % p
        remainder = list(trim(remainder, p))
    if remainder:
        raise Reject("nonexact division")
    return trim(quotient, p)


def add(left: tuple[int, ...], right: tuple[int, ...], p: int) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[i] if i < len(left) else 0)
            + (right[i] if i < len(right) else 0)
            for i in range(size)
        ],
        p,
    )


def scale(poly: tuple[int, ...], scalar: int, p: int) -> tuple[int, ...]:
    return trim([scalar * value for value in poly], p)


def interpolate(
    points: tuple[int, ...], values: tuple[int, ...], p: int
) -> tuple[int, ...]:
    result: tuple[int, ...] = ()
    for i, (x_i, y_i) in enumerate(zip(points, values)):
        basis = (1,)
        denominator = 1
        for j, x_j in enumerate(points):
            if i == j:
                continue
            basis = multiply(basis, ((-x_j) % p, 1), p)
            denominator = denominator * (x_i - x_j) % p
        result = add(result, scale(basis, y_i * pow(denominator, -1, p), p), p)
    return result


def validate(contract: object, control: object) -> dict[str, int]:
    if not isinstance(contract, dict) or set(contract) != {
        "schema",
        "inputs",
        "theorem",
        "gf11_control",
        "official_koalabear_boundaries",
    }:
        raise Reject("contract schema")
    if contract["schema"] != "rate-half-mca-whole-line-global-core-router-v1":
        raise Reject("schema")
    inputs = contract["inputs"]
    if inputs != {
        "common_core_import_node": "rate_half_kb_common_core_shortening_adapter_staircase_import",
        "common_core_import_upstream_head": "e26c15b2d2c2f98ae12dda17b97c40981f76e1ff",
        "local_owner_cut_node": "rate_half_mca_record_local_core_owner_noninvariance",
        "local_owner_cut_contract_sha256": CONTROL_SHA256,
    }:
        raise Reject("input pins")
    theorem = contract["theorem"]
    if theorem != {
        "owner": "one global intersection of all declared selected maximal supports on one received line",
        "slope_map": "identity",
        "slope_fiber": 1,
        "preserved_invariants": ["m-k", "n-k", "n-m"],
        "paid_or_residual_outcomes": [
            "GLOBAL_AFFINE",
            "GLOBAL_CORE_S_LE_2",
            "GLOBAL_CORE_DIRECTION_SEPARATED_3_LE_S_LE_13",
            "DIRECTION_LIST_SHORTENED_S",
            "GLOBAL_CORE_SHORTENED_S_GE_14",
        ],
    }:
        raise Reject("theorem")
    if not isinstance(control, dict):
        raise Reject("control")

    p = control["field"]
    domain = tuple(control["domain"])
    k = control["k"]
    m = control["m"]
    u = tuple(control["received_line"]["u"])
    v = tuple(control["received_line"]["v"])
    selected = tuple(contract["gf11_control"]["selected_slopes"])
    explanations = {
        item["slope"]: item for item in control["explanations"] if item["slope"] in selected
    }
    if set(explanations) != set(selected):
        raise Reject("selected explanations")
    global_core = set(domain)
    for item in explanations.values():
        global_core &= set(item["maximal_support"])
    if global_core != set(contract["gf11_control"]["global_core"]) or global_core != {10}:
        raise Reject("global core")

    c = len(global_core)
    shortened_domain = tuple(x for x in domain if x not in global_core)
    n2, k2, m2 = len(domain) - c, k - c, m - c
    gf11 = contract["gf11_control"]
    if (
        n2,
        k2,
        m2,
        m2 - k2,
        n2 - k2,
        n2 - m2,
    ) != (
        gf11["shortened_n"],
        gf11["shortened_k"],
        gf11["shortened_m"],
        gf11["shortened_d"],
        gf11["shortened_R"],
        gf11["shortened_t"],
    ):
        raise Reject("shortened parameters")

    core_point = next(iter(global_core))
    a0 = (u[domain.index(core_point)],)
    a1 = (v[domain.index(core_point)],)
    locator = ((-core_point) % p, 1)
    shortened_u = tuple(
        (u[domain.index(x)] - a0[0]) * pow((x - core_point) % p, -1, p) % p
        for x in shortened_domain
    )
    shortened_v = tuple(
        (v[domain.index(x)] - a1[0]) * pow((x - core_point) % p, -1, p) % p
        for x in shortened_domain
    )

    shortened_explanations: dict[int, tuple[int, ...]] = {}
    for slope in selected:
        item = explanations[slope]
        source_poly = tuple(item["coefficients"])
        correction = (-(a0[0] + slope * a1[0])) % p
        numerator = add(source_poly, (correction,), p)
        quotient = divide_exact(numerator, locator, p)
        if degree(quotient) >= k2:
            raise Reject("shortened explanation degree")
        if multiply(locator, quotient, p) != numerator:
            raise Reject("inverse polynomial")
        support = tuple(x for x in item["maximal_support"] if x != core_point)
        if len(support) != m2:
            raise Reject("shortened support size")
        slope_word = tuple(
            (shortened_u[i] + slope * shortened_v[i]) % p
            for i in range(len(shortened_domain))
        )
        computed_support = tuple(
            x
            for x, value in zip(shortened_domain, slope_word)
            if evaluate(quotient, x, p) == value
        )
        if computed_support != support:
            raise Reject("shortened maximal support")
        indices = tuple(shortened_domain.index(x) for x in support)
        u_poly = interpolate(support, tuple(shortened_u[i] for i in indices), p)
        v_poly = interpolate(support, tuple(shortened_v[i] for i in indices), p)
        if degree(u_poly) < k2 and degree(v_poly) < k2:
            raise Reject("shortened pair containment")
        shortened_explanations[slope] = quotient
    if len(shortened_explanations) != len(selected):
        raise Reject("identity slope fiber")

    best_direction_agreement = 0
    for support in itertools.combinations(shortened_domain, k2):
        indices = tuple(shortened_domain.index(x) for x in support)
        candidate = interpolate(support, tuple(shortened_v[i] for i in indices), p)
        agreement = sum(
            evaluate(candidate, x, p) == value
            for x, value in zip(shortened_domain, shortened_v)
        )
        best_direction_agreement = max(best_direction_agreement, agreement)
    if best_direction_agreement != gf11["direction_max_agreement"] or gf11["outcome"] != "DIRECTION_LIST_SHORTENED_S":
        raise Reject("direction residual")

    official = contract["official_koalabear_boundaries"]
    n = official["n"]
    official_k = official["k"]
    official_m = official["m"]
    reserve = n - official_k
    defect = official_m - official_k
    b2 = min(math.comb(reserve + 2, defect + 2), math.comb(reserve + 2, 3))
    b3 = min(math.comb(reserve + 3, defect + 3), math.comb(reserve + 3, 4))
    def j_value(s: int) -> int:
        numerator = math.prod(reserve + i for i in range(s + 1))
        denominator = math.prod(defect + i for i in range(s + 1))
        return numerator // denominator
    if (
        b2 != official["B_cell_s2"]
        or b3 != official["B_cell_s3"]
        or j_value(13) != official["J_13"]
        or j_value(14) != official["J_14"]
        or not b2 <= official["B_star"] < b3
        or not official["J_13"] <= official["B_star"] < official["J_14"]
    ):
        raise Reject("official boundaries")
    return {
        "slopes": len(selected),
        "global_core": c,
        "direction_max": best_direction_agreement,
    }


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    if hashlib.sha256(CONTROL.read_bytes()).hexdigest() != CONTROL_SHA256:
        raise Reject("control hash")
    contract = json.loads(CONTRACT.read_text())
    control = json.loads(CONTROL.read_text())
    result = validate(contract, control)
    cases = []
    changed = copy.deepcopy(contract)
    changed["gf11_control"]["global_core"] = [9]
    cases.append(changed)
    changed = copy.deepcopy(contract)
    changed["gf11_control"]["shortened_k"] = 5
    cases.append(changed)
    changed = copy.deepcopy(contract)
    changed["gf11_control"]["outcome"] = "GLOBAL_CORE_DIRECTION_SEPARATED_3_LE_S_LE_13"
    cases.append(changed)
    changed = copy.deepcopy(contract)
    changed["official_koalabear_boundaries"]["J_14"] -= 1
    cases.append(changed)
    caught = 0
    for changed in cases:
        try:
            validate(changed, control)
        except Reject:
            caught += 1
    if caught != len(cases):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_WHOLE_LINE_GLOBAL_CORE_ROUTER_PASS "
        f"slopes={result['slopes']} global_core={result['global_core']} "
        f"direction_max={result['direction_max']} mutations={caught}/{len(cases)}"
    )


if __name__ == "__main__":
    main()
