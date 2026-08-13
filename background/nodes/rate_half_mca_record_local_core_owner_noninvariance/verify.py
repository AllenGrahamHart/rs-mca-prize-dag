#!/usr/bin/env python3
"""Verify the record-local common-core owner counterexample."""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "7a27aef1521b42bc9704c97345be34263e8b22980b5e7fd65f84560b92ff6c94"


class Reject(ValueError):
    pass


def integer(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise Reject("integer field")
    return value


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


def scale(poly: tuple[int, ...], scalar: int, p: int) -> tuple[int, ...]:
    return trim([scalar * value for value in poly], p)


def interpolate(
    points: tuple[int, ...], values: tuple[int, ...], p: int
) -> tuple[int, ...]:
    if len(points) != len(values) or len(set(points)) != len(points):
        raise Reject("interpolation input")
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


def validate(data: object) -> dict[str, int]:
    if not isinstance(data, dict) or set(data) != {
        "schema",
        "field",
        "domain",
        "k",
        "m",
        "critical_order",
        "received_line",
        "explanations",
        "records",
        "shared_slope",
        "claims",
    }:
        raise Reject("top-level schema")
    if data["schema"] != "rate-half-mca-record-local-core-owner-noninvariance-v1":
        raise Reject("schema")
    p = integer(data["field"])
    if p != 11 or any(p % divisor == 0 for divisor in range(2, int(p**0.5) + 1)):
        raise Reject("field")
    domain = tuple(integer(value) for value in data["domain"])
    if domain != tuple(range(1, p)):
        raise Reject("domain")
    n = len(domain)
    k = integer(data["k"])
    m = integer(data["m"])
    critical_order = integer(data["critical_order"])
    if (k, m, critical_order) != (5, 7, 2 * (n - k) // (m - k) + 1):
        raise Reject("row arithmetic")

    line = data["received_line"]
    if not isinstance(line, dict) or set(line) != {"u", "v"}:
        raise Reject("line schema")
    u = tuple(integer(value) % p for value in line["u"])
    v = tuple(integer(value) % p for value in line["v"])
    if len(u) != n or len(v) != n:
        raise Reject("line length")

    explanations = data["explanations"]
    if not isinstance(explanations, list) or len(explanations) != 7:
        raise Reject("explanation count")
    by_slope: dict[int, tuple[tuple[int, ...], set[int]]] = {}
    subset_checks = 0
    for item in explanations:
        if not isinstance(item, dict) or set(item) != {
            "slope",
            "coefficients",
            "maximal_support",
            "witness_support",
            "u_interpolant_degree",
            "v_interpolant_degree",
        }:
            raise Reject("explanation schema")
        slope = integer(item["slope"])
        if not 0 <= slope < p or slope in by_slope:
            raise Reject("slope")
        coefficients = trim([integer(value) for value in item["coefficients"]], p)
        if degree(coefficients) >= k:
            raise Reject("explanation degree")
        maximal = tuple(integer(value) for value in item["maximal_support"])
        witness = tuple(integer(value) for value in item["witness_support"])
        if (
            len(maximal) < m
            or len(witness) != m
            or len(set(maximal)) != len(maximal)
            or len(set(witness)) != len(witness)
            or not set(witness) <= set(maximal) <= set(domain)
        ):
            raise Reject("support")

        word = tuple((u_i + slope * v_i) % p for u_i, v_i in zip(u, v))
        computed_maximal = tuple(
            x for x, value in zip(domain, word) if evaluate(coefficients, x, p) == value
        )
        if computed_maximal != maximal:
            raise Reject("maximal support")

        # Any degree-<k explanation with at least m agreements is recovered
        # from one of its m-subsets. This proves uniqueness without enumerating
        # all p^k codewords.
        recovered: set[tuple[int, ...]] = set()
        for subset in itertools.combinations(domain, m):
            indices = tuple(domain.index(x) for x in subset)
            candidate = interpolate(subset, tuple(word[i] for i in indices), p)
            subset_checks += 1
            if degree(candidate) < k:
                support = {
                    x
                    for x, value in zip(domain, word)
                    if evaluate(candidate, x, p) == value
                }
                if len(support) >= m:
                    recovered.add(candidate)
        if recovered != {coefficients}:
            raise Reject("unique explanation")

        indices = tuple(domain.index(x) for x in witness)
        u_poly = interpolate(witness, tuple(u[i] for i in indices), p)
        v_poly = interpolate(witness, tuple(v[i] for i in indices), p)
        if (
            degree(u_poly) != integer(item["u_interpolant_degree"])
            or degree(v_poly) != integer(item["v_interpolant_degree"])
            or (degree(u_poly) < k and degree(v_poly) < k)
        ):
            raise Reject("same-support noncontainment")
        by_slope[slope] = (coefficients, set(maximal))

    records = data["records"]
    if not isinstance(records, list) or len(records) != 2:
        raise Reject("record count")
    record_slopes: list[tuple[int, ...]] = []
    record_cores: list[set[int]] = []
    for record in records:
        if not isinstance(record, dict) or set(record) != {"slopes", "common_core"}:
            raise Reject("record schema")
        slopes = tuple(integer(value) for value in record["slopes"])
        if len(slopes) != critical_order or len(set(slopes)) != len(slopes):
            raise Reject("record order")
        if any(slope not in by_slope for slope in slopes):
            raise Reject("record slope")
        core = set(domain)
        for slope in slopes:
            core &= by_slope[slope][1]
        if core != set(integer(value) for value in record["common_core"]):
            raise Reject("record core")

        first, second = slopes[:2]
        denominator = pow((second - first) % p, -1, p)
        left = by_slope[first][0]
        right = by_slope[second][0]
        width = max(len(left), len(right), k)
        left = left + (0,) * (width - len(left))
        right = right + (0,) * (width - len(right))
        direction = tuple((right[j] - left[j]) * denominator % p for j in range(width))
        origin = tuple((left[j] - first * direction[j]) % p for j in range(width))
        if all(
            tuple((origin[j] + slope * direction[j]) % p for j in range(width))
            == by_slope[slope][0] + (0,) * (width - len(by_slope[slope][0]))
            for slope in slopes
        ):
            raise Reject("global affine record")
        record_slopes.append(slopes)
        record_cores.append(core)

    shared = integer(data["shared_slope"])
    if shared != 0 or not all(shared in slopes for slopes in record_slopes):
        raise Reject("shared slope")
    if record_cores[0] == record_cores[1]:
        raise Reject("core invariance")
    if data["claims"] != {
        "unique_degree_below_k_explanation_per_listed_slope": True,
        "every_listed_slope_is_support_wise_bad": True,
        "both_records_are_non_global_affine": True,
        "record_local_common_core_is_not_a_slope_invariant": True,
    }:
        raise Reject("claims")
    return {
        "slopes": len(by_slope),
        "subset_checks": subset_checks,
        "records": len(records),
    }


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != SHA256:
        raise Reject("contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = []
    cases = []
    changed = copy.deepcopy(data)
    changed["received_line"]["u"][0] = 1
    cases.append(changed)
    changed = copy.deepcopy(data)
    changed["explanations"][0]["coefficients"][0] = 5
    cases.append(changed)
    changed = copy.deepcopy(data)
    changed["explanations"][1]["maximal_support"][0] = 2
    cases.append(changed)
    changed = copy.deepcopy(data)
    changed["records"][0]["common_core"] = [10]
    cases.append(changed)
    changed = copy.deepcopy(data)
    changed["records"][1]["slopes"][-1] = 8
    cases.append(changed)
    changed = copy.deepcopy(data)
    changed["claims"]["record_local_common_core_is_not_a_slope_invariant"] = False
    cases.append(changed)
    for changed in cases:
        try:
            validate(changed)
        except Reject:
            mutations.append(True)
        else:
            mutations.append(False)
    if not all(mutations):
        raise AssertionError("mutation controls")
    print(
        "RATE_HALF_MCA_RECORD_LOCAL_CORE_OWNER_NONINVARIANCE_PASS "
        f"slopes={result['slopes']} records={result['records']} "
        f"subset_checks={result['subset_checks']} mutations={sum(mutations)}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
