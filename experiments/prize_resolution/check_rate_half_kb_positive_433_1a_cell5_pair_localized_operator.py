#!/usr/bin/env python3
"""Exact finite-fiber audit for the localized signed-pair operator."""

import argparse
import hashlib
import json
import struct
from pathlib import Path


HERE = Path(__file__).parent
PRIME = 2130706433
DIMENSION = 24
AMBIENT_DIMENSION = 64
FIBER = 2
OPERATOR = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_localized_operator_merged_result.json"
)
EXPECTED_OPERATOR_SHA256 = (
    "d49311b27680acf3b4b548547a9c4f8c94f5d1ea63ae3154982e5972bc5de026"
)
SQUARE_PACKET = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients.bin"
)
SQUARE_METADATA = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients_meta.json"
)


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--operator", type=Path, default=OPERATOR)
    return parser.parse_args()


def evaluate(coefficients, value):
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % PRIME
    return result


def evaluate_fraction(entry, value):
    denominator = evaluate(entry["denominator"], value)
    require(denominator != 0, f"operator pole at t={value}")
    return evaluate(entry["numerator"], value) * pow(denominator, -1, PRIME) % PRIME


def read_square_stable_basis():
    metadata = json.loads(SQUARE_METADATA.read_text())
    raw = SQUARE_PACKET.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == metadata["packet_sha256"], "packet hash mismatch")
    view = memoryview(raw)
    require(bytes(view[:8]) == b"KBC5M02\n", "bad square-packet magic")
    offset = 8
    count = struct.unpack_from("<I", view, offset)[0]
    offset += 4
    basis_sha256 = bytes(view[offset:offset + 32]).hex()
    offset += 32
    coefficients_sha256 = bytes(view[offset:offset + 32]).hex()
    offset += 32
    require(basis_sha256 == metadata["basis_sha256"], "basis hash mismatch")
    require(coefficients_sha256 == metadata["coefficients_sha256"], "coefficient hash mismatch")
    stable = [[0] * DIMENSION for _ in range(AMBIENT_DIMENSION)]
    for _ in range(count):
        row, column, numerator_length, denominator_length = struct.unpack_from(
            "<BBHH", view, offset
        )
        offset += 6
        numerator = struct.unpack_from(f"<{numerator_length}I", view, offset)
        offset += 4 * numerator_length
        denominator = struct.unpack_from(f"<{denominator_length}I", view, offset)
        offset += 4 * denominator_length
        if column <= DIMENSION:
            denominator_value = evaluate(denominator, FIBER)
            require(denominator_value != 0, "stable-basis pole at t=2")
            stable[row - 1][column - 1] = (
                evaluate(numerator, FIBER) * pow(denominator_value, -1, PRIME)
            ) % PRIME
    require(offset == len(view), "trailing square-packet bytes")
    return metadata, stable


def multiply(left, right):
    transpose = list(zip(*right))
    return [
        [sum(a * b for a, b in zip(row, column)) % PRIME for column in transpose]
        for row in left
    ]


def matrix_vector(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) % PRIME for row in matrix]


def solve(matrix, target):
    size = len(matrix)
    work = [row[:] + [target[index]] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        require(pivot is not None, "singular Krylov matrix")
        work[column], work[pivot] = work[pivot], work[column]
        inverse = pow(work[column][column], -1, PRIME)
        work[column] = [value * inverse % PRIME for value in work[column]]
        for row in range(size):
            if row == column:
                continue
            scale = work[row][column]
            if scale:
                work[row] = [
                    (left - scale * right) % PRIME
                    for left, right in zip(work[row], work[column])
                ]
    return [work[row][-1] for row in range(size)]


def trim(polynomial):
    polynomial = list(polynomial)
    while len(polynomial) > 1 and polynomial[-1] == 0:
        polynomial.pop()
    return polynomial


def polynomial_divmod(dividend, divisor):
    dividend = trim(dividend)
    divisor = trim(divisor)
    require(divisor != [0], "zero polynomial divisor")
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    inverse = pow(divisor[-1], -1, PRIME)
    while len(dividend) >= len(divisor) and dividend != [0]:
        shift = len(dividend) - len(divisor)
        scale = dividend[-1] * inverse % PRIME
        quotient[shift] = scale
        for index, coefficient in enumerate(divisor):
            dividend[index + shift] = (dividend[index + shift] - scale * coefficient) % PRIME
        dividend = trim(dividend)
    return trim(quotient), dividend


def polynomial_gcd(left, right):
    left, right = trim(left), trim(right)
    while right != [0]:
        _, remainder = polynomial_divmod(left, right)
        left, right = right, remainder
    inverse = pow(left[-1], -1, PRIME)
    return trim([value * inverse % PRIME for value in left])


def verify(operator_path=OPERATOR):
    payload_raw = operator_path.read_bytes()
    if operator_path.resolve() == OPERATOR.resolve():
        require(
            hashlib.sha256(payload_raw).hexdigest() == EXPECTED_OPERATOR_SHA256,
            "operator packet hash mismatch",
        )
    payload = json.loads(payload_raw)
    require(payload["schema"].endswith("localized-operator-v1"), "operator schema mismatch")
    require(payload["alpha"] == 2 and payload["beta"] == 3, "operator element mismatch")
    require(payload["column_coverage"] == list(range(1, 25)), "operator coverage mismatch")
    metadata, stable = read_square_stable_basis()
    require(payload["basis_sha256"] == metadata["basis_sha256"], "operator basis mismatch")
    require(payload["square_packet_sha256"] == metadata["packet_sha256"], "operator packet mismatch")
    coordinates = [[0] * DIMENSION for _ in range(DIMENSION)]
    targets = [[0] * DIMENSION for _ in range(AMBIENT_DIMENSION)]
    coordinate_keys = set()
    for entry in payload["entries"]:
        row = entry["row"] - 1
        column = entry["column"] - 1
        value = evaluate_fraction(entry, FIBER)
        if entry["kind"] == "C":
            require(0 <= row < DIMENSION and 0 <= column < DIMENSION, "bad coordinate index")
            require((row, column) not in coordinate_keys, "duplicate coordinate")
            coordinate_keys.add((row, column))
            coordinates[row][column] = value
        elif entry["kind"] == "W":
            require(0 <= row < AMBIENT_DIMENSION and 0 <= column < DIMENSION, "bad target index")
            targets[row][column] = value
        else:
            raise CertificateError("unknown operator entry kind")
    require(len(coordinate_keys) == DIMENSION**2, "coordinate coverage mismatch")
    require(multiply(stable, coordinates) == targets, "stable operator identity fails at t=2")

    candidates = [
        [1] + [0] * (DIMENSION - 1),
        [1] * DIMENSION,
        list(range(1, DIMENSION + 1)),
    ]
    minimal = None
    cyclic_index = None
    for index, vector in enumerate(candidates):
        powers = []
        current = vector
        for _ in range(DIMENSION + 1):
            powers.append(current)
            current = matrix_vector(coordinates, current)
        krylov = [list(column) for column in zip(*powers[:DIMENSION])]
        try:
            relation = solve(krylov, powers[DIMENSION])
        except CertificateError:
            continue
        minimal = [(-value) % PRIME for value in relation] + [1]
        cyclic_index = index
        break
    require(minimal is not None, "no registered cyclic vector")
    derivative = [index * minimal[index] % PRIME for index in range(1, len(minimal))]
    gcd = polynomial_gcd(minimal, derivative)
    require(gcd == [1], "specialized minimal polynomial is not squarefree")
    return cyclic_index, minimal, gcd, payload_raw


def main():
    args = parse_args()
    cyclic_index, minimal, gcd, payload_raw = verify(args.operator)
    minimal_sha256 = hashlib.sha256(
        ",".join(map(str, minimal)).encode()
    ).hexdigest()
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_LOCALIZED_OPERATOR_PASS "
        f"fiber={FIBER} cyclic_vector={cyclic_index} degree={len(minimal)-1} "
        f"squarefree_gcd_degree={len(gcd)-1} "
        f"minimal_sha256={minimal_sha256} "
        f"operator_sha256={hashlib.sha256(payload_raw).hexdigest()}"
    )


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, ValueError, struct.error) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_LOCALIZED_OPERATOR_FAIL {error}")
        raise SystemExit(1)
