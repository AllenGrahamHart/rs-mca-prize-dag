#!/usr/bin/env python3
"""Check the exact generic-gcd packet and replay its Bezout data at t=2."""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization as factors
import probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber as fiber


RESULT = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_colored_generic_gcd_result.json"
)
EXPECTED_RESULT_SHA256 = (
    "710b438062fc2e80f5c7b14ffb987d8f36a02d4b57953b30419bb320b88877a7"
)
MAPS = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json"
)
FACTORIZATION = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json"
)
ATLAS = HERE / "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"
KERNEL = HERE / "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
EXPECTED_NAMES = {
    "PAIR",
    "COLORED",
    "COMMON",
    "BEZOUT_PAIR",
    "BEZOUT_COLORED",
    "GUARD_PART",
    "OUTSIDE",
}
MARKER = re.compile(
    r"COLORED_GENERIC_GCD_COMPLETE factor=(\d+) factor_degree=(\d+) "
    r"pair_degree=(\d+) colored_degree=(\d+) gcd_degree=(\d+) "
    r"guard_part_degree=(\d+) outside_degree=(\d+)"
)


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def evaluate(polynomial, value):
    result = 0
    for coefficient in reversed(polynomial):
        result = (result * value + coefficient) % fiber.P
    return result


def evaluate_fraction(record, value):
    denominator = evaluate(record["denominator"], value)
    require(denominator != 0, f"certificate pole at t={value}")
    return evaluate(record["numerator"], value) * pow(
        denominator, -1, fiber.P
    ) % fiber.P


def specialized_polynomial(records, name, modulus):
    selected = [record for record in records if record["name"] == name]
    require(selected, f"missing {name} records")
    max_e = max(record["e_degree"] for record in selected)
    output = []
    for e_degree in range(max_e + 1):
        coefficient_records = [
            record for record in selected if record["e_degree"] == e_degree
        ]
        require(coefficient_records, f"missing {name} e^{e_degree} coefficient")
        max_s = max(record["s_degree"] for record in coefficient_records)
        coefficient = [0] * (max_s + 1)
        seen = set()
        for record in coefficient_records:
            s_degree = record["s_degree"]
            require(s_degree not in seen, f"duplicate {name} coefficient")
            seen.add(s_degree)
            coefficient[s_degree] = evaluate_fraction(record, fiber.T)
        output.append(fiber.guards.reduce_mod(fiber.guards.trim(coefficient), modulus))
    return fiber.ep_trim(output)


def verify_row(row, generic_factors):
    require(row["status"] == "COMPLETE" and row["returncode"] == 0,
            f"factor {row.get('factor')} incomplete")
    factor_index = row["factor"]
    require(factor_index in range(1, 6), "factor index outside 1..5")
    require(
        row["coordinate_map_sha256"] == hashlib.sha256(MAPS.read_bytes()).hexdigest(),
        "coordinate-map provenance mismatch",
    )
    require(
        row["primitive_factorization_sha256"]
        == hashlib.sha256(FACTORIZATION.read_bytes()).hexdigest(),
        "factorization provenance mismatch",
    )
    require(
        row["lift_atlas_sha256"] == hashlib.sha256(ATLAS.read_bytes()).hexdigest(),
        "lift-atlas provenance mismatch",
    )
    require(
        row["sparse_kernel_sha256"] == hashlib.sha256(KERNEL.read_bytes()).hexdigest(),
        "sparse-kernel provenance mismatch",
    )
    match = MARKER.search(row["stdout"])
    require(match is not None, "completion marker missing")
    marker = tuple(map(int, match.groups()))
    require(marker[0] == factor_index, "completion factor mismatch")
    require(marker[1] == row["factor_degree"], "completion factor degree mismatch")
    require(marker[2] == 4 and marker[3] == 4, "necessary polynomial degree mismatch")
    require(marker[6] == 0, "generic gcd has support outside the collision guard")

    records = row["records"]
    require({record["name"] for record in records} == EXPECTED_NAMES,
            "certificate record names mismatch")
    require(all(record["numerator"] and record["denominator"] for record in records),
            "empty rational-function coefficient")
    specialized_parent = fiber.guards.trim([
        factors.evaluate_rational(value, fiber.T)
        for value in generic_factors[factor_index - 1]
    ])
    finite_factors = fiber.split_specialized_factor(specialized_parent)
    for finite_factor in finite_factors:
        polynomials = {
            name: specialized_polynomial(records, name, finite_factor)
            for name in EXPECTED_NAMES
        }
        lhs = fiber.ep_add(
            fiber.ep_multiply(
                polynomials["BEZOUT_PAIR"], polynomials["PAIR"], finite_factor
            ),
            fiber.ep_multiply(
                polynomials["BEZOUT_COLORED"],
                polynomials["COLORED"],
                finite_factor,
            ),
            finite_factor,
        )
        require(lhs == polynomials["COMMON"], "specialized Bezout identity failed")
        require(
            fiber.ep_gcd(
                polynomials["PAIR"], polynomials["COLORED"], finite_factor
            )
            == polynomials["COMMON"],
            "specialized common gcd mismatch",
        )
        guard = [[fiber.P - 1], fiber.ZERO, fiber.ONE]
        require(
            fiber.ep_gcd(polynomials["COMMON"], guard, finite_factor)
            == polynomials["GUARD_PART"],
            "specialized guard gcd mismatch",
        )
        require(
            fiber.ep_multiply(
                polynomials["GUARD_PART"], polynomials["OUTSIDE"], finite_factor
            )
            == polynomials["COMMON"],
            "specialized guard quotient mismatch",
        )
        require(len(polynomials["OUTSIDE"]) == 1, "outside quotient is nonconstant")
    return marker


def verify(path=RESULT):
    raw = path.read_bytes()
    if path.resolve() == RESULT.resolve():
        require(
            hashlib.sha256(raw).hexdigest() == EXPECTED_RESULT_SHA256,
            "result packet hash mismatch",
        )
    payload = json.loads(raw)
    require(isinstance(payload, list) and len(payload) == 5, "result shard count mismatch")
    require([row["factor"] for row in payload] == list(range(1, 6)),
            "factor coverage mismatch")
    generic_factors, _ = factors.verify()
    markers = [verify_row(row, generic_factors) for row in payload]
    return payload, markers


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", type=Path, default=RESULT)
    args = parser.parse_args()
    payload, markers = verify(args.result)
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_COLORED_GENERIC_GCD_PASS "
        f"factors={len(payload)} gcd_degrees={','.join(str(row[4]) for row in markers)} "
        f"guard_part_degrees={','.join(str(row[5]) for row in markers)} "
        "outside_degrees=0,0,0,0,0 specialized_bezout_fiber=2"
    )


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, ValueError) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_COLORED_GENERIC_GCD_FAIL {error}")
        raise SystemExit(1)
