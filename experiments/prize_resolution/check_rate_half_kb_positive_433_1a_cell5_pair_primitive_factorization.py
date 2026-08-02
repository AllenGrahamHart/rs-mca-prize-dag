#!/usr/bin/env python3
"""Independent exact checker for the localized pair primitive factorization."""

import argparse
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).parent
PRIME = 2130706433
PRIMITIVE = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial_result.json"
)
FACTORIZATION = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json"
)
EXPECTED_PRIMITIVE_SHA256 = (
    "8867cfc4f2c4a5accd898382b687e5327f5f4c2cb793dfd34897137d3ffc5f7e"
)
EXPECTED_FACTORIZATION_SHA256 = (
    "00c4a7f0c90726b91b2310fa184d5eaf0ca3fab2b4d6a6ada1a4e1ae10f75cae"
)


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--factorization", type=Path, default=FACTORIZATION)
    return parser.parse_args()


def trim(polynomial):
    result = [value % PRIME for value in polynomial]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def poly_add(left, right):
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def poly_sub(left, right):
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else 0)
        - (right[index] if index < len(right) else 0)
        for index in range(size)
    ])


def poly_mul(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] = (
                result[left_index + right_index] + left_value * right_value
            ) % PRIME
    return trim(result)


def poly_divmod(dividend, divisor):
    dividend = list(trim(dividend))
    divisor = trim(divisor)
    require(divisor != (0,), "zero polynomial divisor")
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, PRIME)
    while len(dividend) >= len(divisor) and tuple(dividend) != (0,):
        shift = len(dividend) - len(divisor)
        scale = dividend[-1] * inverse % PRIME
        quotient[shift] = scale
        for index, value in enumerate(divisor):
            dividend[index + shift] = (dividend[index + shift] - scale * value) % PRIME
        dividend = list(trim(dividend))
    return trim(quotient), trim(dividend)


def poly_gcd(left, right):
    left, right = trim(left), trim(right)
    while right != (0,):
        _, remainder = poly_divmod(left, right)
        left, right = right, remainder
    inverse = pow(left[-1], -1, PRIME)
    return trim([value * inverse for value in left])


def rational(numerator, denominator):
    numerator, denominator = trim(numerator), trim(denominator)
    require(denominator != (0,), "zero rational denominator")
    common = poly_gcd(numerator, denominator)
    numerator, remainder = poly_divmod(numerator, common)
    require(remainder == (0,), "numerator gcd division failed")
    denominator, remainder = poly_divmod(denominator, common)
    require(remainder == (0,), "denominator gcd division failed")
    inverse = pow(denominator[-1], -1, PRIME)
    return (
        trim([value * inverse for value in numerator]),
        trim([value * inverse for value in denominator]),
    )


ZERO = ((0,), (1,))
ONE = ((1,), (1,))


def rational_add(left, right):
    return rational(
        poly_add(poly_mul(left[0], right[1]), poly_mul(right[0], left[1])),
        poly_mul(left[1], right[1]),
    )


def rational_mul(left, right):
    return rational(poly_mul(left[0], right[0]), poly_mul(left[1], right[1]))


def s_poly_mul(left, right):
    result = [ZERO] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] = rational_add(
                result[left_index + right_index],
                rational_mul(left_value, right_value),
            )
    return result


def evaluate(polynomial, value):
    result = 0
    for coefficient in reversed(polynomial):
        result = (result * value + coefficient) % PRIME
    return result


def evaluate_rational(value, fiber):
    denominator = evaluate(value[1], fiber)
    require(denominator != 0, f"factor pole at t={fiber}")
    return evaluate(value[0], fiber) * pow(denominator, -1, PRIME) % PRIME


def load_primitive():
    raw = PRIMITIVE.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == EXPECTED_PRIMITIVE_SHA256, "primitive hash mismatch")
    payload = json.loads(raw)
    require(payload["status"] == "COMPLETE" and payload["returncode"] == 0, "primitive incomplete")
    records = sorted(payload["coefficients"], key=lambda item: item["degree"])
    require([item["degree"] for item in records] == list(range(25)), "primitive coverage mismatch")
    return payload, [rational(item["numerator"], item["denominator"]) for item in records]


def load_factors(path):
    raw = path.read_bytes()
    if path.resolve() == FACTORIZATION.resolve():
        require(
            hashlib.sha256(raw).hexdigest() == EXPECTED_FACTORIZATION_SHA256,
            "factorization hash mismatch",
        )
    payload = json.loads(raw)
    require(payload["status"] == "COMPLETE" and payload["returncode"] == 0, "factorization incomplete")
    require("PRIMITIVE_FACTOR_COUNT 5" in payload["stdout"], "factor-count marker missing")
    groups = {}
    for item in payload["factors"]:
        groups.setdefault(item["factor"], []).append(item)
    require(set(groups) == set(range(1, 6)), "factor labels mismatch")
    factors = []
    for index in range(1, 6):
        records = sorted(groups[index], key=lambda item: item["coefficient_degree"])
        degree = records[0]["factor_degree"]
        require(
            all(item["factor_degree"] == degree and item["multiplicity"] == 1 for item in records),
            "factor degree or multiplicity mismatch",
        )
        require(
            [item["coefficient_degree"] for item in records] == list(range(degree + 1)),
            "factor coefficient coverage mismatch",
        )
        factor = [rational(item["numerator"], item["denominator"]) for item in records]
        require(factor[-1] == ONE, "factor is not monic")
        factors.append(factor)
    require(sorted(len(factor) - 1 for factor in factors) == [4, 4, 4, 4, 8], "factor degree ledger mismatch")
    return payload, factors, raw


def verify(path=FACTORIZATION):
    primitive_payload, primitive = load_primitive()
    payload, factors, raw = load_factors(path)
    require(payload["primitive_sha256"] == EXPECTED_PRIMITIVE_SHA256, "factor primitive provenance mismatch")
    require(payload["operator_sha256"] == primitive_payload["operator_sha256"], "operator provenance mismatch")
    product = [ONE]
    for factor in factors:
        product = s_poly_mul(product, factor)
    require(product == primitive, "exact rational-function factor product mismatch")
    specialized = [
        trim([evaluate_rational(value, 2) for value in factor])
        for factor in factors
    ]
    for factor in specialized:
        derivative = trim([
            index * factor[index] for index in range(1, len(factor))
        ])
        require(poly_gcd(factor, derivative) == (1,), "specialized factor is not squarefree")
    for left_index, left in enumerate(specialized):
        for right in specialized[left_index + 1:]:
            require(poly_gcd(left, right) == (1,), "specialized factors collide")
    return factors, raw


def main():
    args = parse_args()
    factors, raw = verify(args.factorization)
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_PRIMITIVE_FACTORIZATION_PASS "
        f"degrees={','.join(str(len(factor)-1) for factor in factors)} "
        "squarefree_pairwise_coprime_fiber=2 "
        f"factorization_sha256={hashlib.sha256(raw).hexdigest()}"
    )


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, ValueError) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_PRIMITIVE_FACTORIZATION_FAIL {error}")
        raise SystemExit(1)
