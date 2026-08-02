#!/usr/bin/env python3
"""Independent specialization audit for the exact primitive polynomial."""

import argparse
import hashlib
import json
import sys
from pathlib import Path


HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import check_rate_half_kb_positive_433_1a_cell5_pair_localized_operator as operator_checker


PRIMITIVE = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial_result.json"
)
EXPECTED_PRIMITIVE_SHA256 = (
    "8867cfc4f2c4a5accd898382b687e5327f5f4c2cb793dfd34897137d3ffc5f7e"
)


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--primitive", type=Path, default=PRIMITIVE)
    return parser.parse_args()


def evaluate(coefficients, value):
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % operator_checker.PRIME
    return result


def verify(path=PRIMITIVE):
    raw = path.read_bytes()
    if path.resolve() == PRIMITIVE.resolve():
        require(
            hashlib.sha256(raw).hexdigest() == EXPECTED_PRIMITIVE_SHA256,
            "primitive packet hash mismatch",
        )
    payload = json.loads(raw)
    require(payload["status"] == "COMPLETE" and payload["returncode"] == 0, "primitive incomplete")
    require(
        "PRIMITIVE_KRYLOV_BUILT" in payload["stdout"]
        and "PRIMITIVE_POLYNOMIAL_COMPLETE" in payload["stdout"],
        "primitive completion markers missing",
    )
    require(
        payload["operator_sha256"] == operator_checker.EXPECTED_OPERATOR_SHA256,
        "operator provenance mismatch",
    )
    records = sorted(payload["coefficients"], key=lambda item: item["degree"])
    require([item["degree"] for item in records] == list(range(25)), "coefficient coverage mismatch")
    require(
        records[-1]["numerator"] == [1] and records[-1]["denominator"] == [1],
        "primitive polynomial is not monic",
    )
    _, specialized_minimal, _, _ = operator_checker.verify()
    specialized = []
    for item in records:
        denominator = evaluate(item["denominator"], operator_checker.FIBER)
        require(denominator != 0, "primitive coefficient pole at t=2")
        specialized.append(
            evaluate(item["numerator"], operator_checker.FIBER)
            * pow(denominator, -1, operator_checker.PRIME)
            % operator_checker.PRIME
        )
    require(specialized == specialized_minimal, "primitive specialization mismatch")
    digest = hashlib.sha256()
    for index, item in enumerate(records):
        if index:
            digest.update(b"\n")
        line = (
            f"{item['degree']}:{','.join(map(str,item['numerator']))}/"
            f"{','.join(map(str,item['denominator']))}"
        )
        digest.update(line.encode())
    return payload, digest.hexdigest(), raw


def main():
    args = parse_args()
    _, coefficient_sha256, raw = verify(args.primitive)
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_PRIMITIVE_POLYNOMIAL_PASS "
        f"degree=24 fiber=2 coefficient_sha256={coefficient_sha256} "
        f"primitive_sha256={hashlib.sha256(raw).hexdigest()}"
    )


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, ValueError) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_PRIMITIVE_POLYNOMIAL_FAIL {error}")
        raise SystemExit(1)
