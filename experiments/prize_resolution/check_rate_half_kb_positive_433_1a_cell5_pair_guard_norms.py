#!/usr/bin/env python3
"""Check the exact cell-5 guard-norm root census."""

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).parent
RESULT = HERE / "rate_half_kb_positive_433_1a_cell5_pair_guard_norms_result.json"
PRIME = 2130706433
IOTA = 16711679
EXPECTED_RESULT_SHA256 = (
    "663ccab5f1189a6e93f90d7aeba324585161ce86cc8a2b9fe86348a0140f8527"
)
EXPECTED_FACTORIZATION_SHA256 = (
    "00c4a7f0c90726b91b2310fa184d5eaf0ca3fab2b4d6a6ada1a4e1ae10f75cae"
)
EXPECTED_COORDINATE_MAP_SHA256 = (
    "001c959648176669651c87a913f2c830ad425a4f1e240041cc4edeb63d69a009"
)
EXPECTED_ATLAS_SHA256 = (
    "a7610836af981845fca5bf13db61f15beb6df5da08f22338846142495825e548"
)
EXPECTED_PROGRAM_SHA256 = {
    1: "7fdd1fdaa4f4ad396d1a02af7744c44d456518559eb89f8982d136e44846fb61",
    2: "b6170c83fe05f51fbf76a80ec8f034c5475019c05676049b0d475d08409c90ad",
    3: "664dc794a2262e5a2ea2ff2e4a4de3286177fffd8d48a49ea03f39df145403b9",
    4: "8533d3a6eacb77438cd9e797eaa340b0ac329739debacb34659b51bb3414824d",
    5: "cf77f5c89ffd51a32a298289c85f3fa4ef863507e81c12466491c6d258975220",
}
EXPECTED_FACTOR_DEGREES = {1: 4, 2: 4, 3: 4, 4: 8, 5: 4}
CHART_GUARDS = {"r-leading", "c-leading"}
COMMON_GUARDS = {
    "t-1", "t+1", "r-1", "r+1", "r-iota", "r+iota", "t-r", "t+r",
    "t-iota*r", "t+iota*r", "t-iota", "t+iota", "r", "t", "b", "c",
    "b-1", "b+1", "c-1", "c+1", "c-b", "b+c",
}
OUTSIDE_GUARDS = {
    f"{name}{suffix}"
    for name in ("x0", "x1")
    for suffix in ("", "-1", "-t^4", "-r^4")
}
EXPECTED_NUMERATOR_ROOTS = {
    0, 1, IOTA, 33199819, 67070255, 461778186, 645288348, 749209962,
    1117681606, 1192073071, 1388698644, 1722212723, 1788857732,
    1860858030, 1920178763, 1995696621, PRIME - IOTA, PRIME - 1,
}
EXPECTED_DENOMINATOR_ROOTS = {IOTA, 1332924776, PRIME - 1}
FORBIDDEN_SOURCE_VALUES = {0, 1, PRIME - 1, IOTA, PRIME - IOTA}
EXPECTED_CANDIDATES = {
    33199819, 67070255, 461778186, 645288348, 749209962, 1117681606,
    1192073071, 1332924776, 1388698644, 1722212723, 1788857732,
    1860858030, 1920178763, 1995696621,
}


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def trim(value):
    value = [item % PRIME for item in value]
    while len(value) > 1 and value[-1] == 0:
        value.pop()
    return value


def add(left, right):
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(max(len(left), len(right)))
    ])


def negate(value):
    return trim([-item for item in value])


def subtract(left, right):
    return add(left, negate(right))


def multiply(left, right):
    value = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            value[left_index + right_index] = (
                value[left_index + right_index] + left_value * right_value
            ) % PRIME
    return trim(value)


def divmod_poly(dividend, divisor):
    dividend = trim(dividend)
    divisor = trim(divisor)
    require(divisor != [0], "zero polynomial divisor")
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, PRIME)
    while dividend != [0] and len(dividend) >= len(divisor):
        shift = len(dividend) - len(divisor)
        scale = dividend[-1] * inverse % PRIME
        quotient[shift] = scale
        for index, value in enumerate(divisor):
            dividend[index + shift] = (
                dividend[index + shift] - scale * value
            ) % PRIME
        dividend = trim(dividend)
    return trim(quotient), dividend


def reduce_mod(value, modulus):
    return divmod_poly(value, modulus)[1]


def power_mod(base, exponent, modulus):
    value = [1]
    base = reduce_mod(base, modulus)
    while exponent:
        if exponent & 1:
            value = reduce_mod(multiply(value, base), modulus)
        exponent >>= 1
        if exponent:
            base = reduce_mod(multiply(base, base), modulus)
    return value


def gcd(left, right):
    left, right = trim(left), trim(right)
    while right != [0]:
        left, right = right, divmod_poly(left, right)[1]
    require(left != [0], "zero gcd")
    scale = pow(left[-1], -1, PRIME)
    return trim([scale * item for item in left])


def evaluate(value, point):
    result = 0
    for coefficient in reversed(value):
        result = (result * point + coefficient) % PRIME
    return result


def check_root_list(polynomial, roots):
    require(
        isinstance(polynomial, list)
        and polynomial
        and all(isinstance(item, int) and 0 <= item < PRIME for item in polynomial),
        "invalid polynomial coefficients",
    )
    require(polynomial[-1] != 0, "noncanonical polynomial")
    require(
        isinstance(roots, list)
        and roots == sorted(set(roots))
        and all(isinstance(root, int) and 0 <= root < PRIME for root in roots),
        "invalid root list",
    )
    if len(polynomial) == 1:
        require(not roots, "constant polynomial has roots")
        return
    linear_part = gcd(
        polynomial,
        subtract(power_mod([0, 1], PRIME, polynomial), [0, 1]),
    )
    claimed = [1]
    for root in roots:
        require(evaluate(polynomial, root) == 0, "listed value is not a root")
        claimed = multiply(claimed, [(-root) % PRIME, 1])
    require(linear_part == claimed, "root list is incomplete or has extras")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", type=Path, default=RESULT)
    return parser.parse_args()


def verify(path=RESULT):
    raw = path.read_bytes()
    if path == RESULT:
        require(
            hashlib.sha256(raw).hexdigest() == EXPECTED_RESULT_SHA256,
            "guard-norm result hash mismatch",
        )
    payload = json.loads(raw)
    require(isinstance(payload, list) and len(payload) == 5, "bad shard count")
    require([item["factor"] for item in payload] == list(range(1, 6)), "bad factor order")
    numerator_roots = set()
    denominator_roots = set()
    maximum_numerator_degree = 0
    maximum_denominator_degree = 0
    for shard in payload:
        factor = shard["factor"]
        require(shard["status"] == "COMPLETE" and shard["returncode"] == 0, "incomplete shard")
        require(shard["factor_degree"] == EXPECTED_FACTOR_DEGREES[factor], "factor degree mismatch")
        require(shard["factorization_sha256"] == EXPECTED_FACTORIZATION_SHA256, "factorization hash mismatch")
        require(shard["coordinate_map_sha256"] == EXPECTED_COORDINATE_MAP_SHA256, "coordinate-map hash mismatch")
        require(shard["lift_atlas_sha256"] == EXPECTED_ATLAS_SHA256, "atlas hash mismatch")
        require(shard["program_sha256"] == EXPECTED_PROGRAM_SHA256[factor], "program hash mismatch")
        require(f"GUARD_NORMS_COMPLETE factor={factor}" in shard["stdout"], "completion marker missing")
        records = shard.get("records")
        require(isinstance(records, list) and len(records) == 32, "record coverage mismatch")
        seen = {(record["family"], record["guard"]) for record in records}
        expected = (
            {("chart", guard) for guard in CHART_GUARDS}
            | {("common", guard) for guard in COMMON_GUARDS}
            | {("outside_squared", guard) for guard in OUTSIDE_GUARDS}
        )
        require(len(seen) == len(records) and seen == expected, "guard-name coverage mismatch")
        for record in records:
            check_root_list(record["numerator"], record["numerator_roots"])
            check_root_list(record["denominator"], record["denominator_roots"])
            numerator_roots.update(record["numerator_roots"])
            denominator_roots.update(record["denominator_roots"])
            maximum_numerator_degree = max(maximum_numerator_degree, len(record["numerator"]) - 1)
            maximum_denominator_degree = max(maximum_denominator_degree, len(record["denominator"]) - 1)
    require(numerator_roots == EXPECTED_NUMERATOR_ROOTS, "numerator-root union mismatch")
    require(denominator_roots == EXPECTED_DENOMINATOR_ROOTS, "denominator-root union mismatch")
    candidates = (numerator_roots | denominator_roots) - FORBIDDEN_SOURCE_VALUES
    require(candidates == EXPECTED_CANDIDATES, "admissible candidate union mismatch")
    require((maximum_numerator_degree, maximum_denominator_degree) == (40, 16), "norm-degree ledger mismatch")
    return candidates


def main():
    args = parse_args()
    candidates = verify(args.result)
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_GUARD_NORMS_PASS "
        "factors=5 records=160 numerator_roots=18 denominator_roots=3 "
        f"candidate_fibers={len(candidates)} max_degrees=40,16"
    )


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_GUARD_NORMS_FAIL {error}")
        raise SystemExit(1)
