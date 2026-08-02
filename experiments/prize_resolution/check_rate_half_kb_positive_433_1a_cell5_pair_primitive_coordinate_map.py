#!/usr/bin/env python3
"""Independent checker for the signed-pair primitive coordinate maps."""

import argparse
import hashlib
import json
import sys
from pathlib import Path


HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import check_rate_half_kb_positive_433_1a_cell5_pair_localized_operator as operator_checker


PRIME = 2130706433
PRIMITIVE_ROOT = 3
DIMENSION = 24
COORDINATE_COLUMNS = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_coordinate_columns_result.json"
)
COORDINATE_MAP = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json"
)
EXPECTED_COLUMNS_SHA256 = (
    "f5bfdb6cb515b6bbe54fa1abd19d1517759b0a584f501aa308e76f68e1ff1e25"
)
EXPECTED_MAP_SHA256 = (
    "001c959648176669651c87a913f2c830ad425a4f1e240041cc4edeb63d69a009"
)
EXPECTED_PROGRAM_SHA256 = {
    "x1": "a976c7a4ec20ad369d9ff688a63e91e7c70b7386afaf48ffd324b4b63b338794",
    "x0": "454180a8a2605fa2d4ca67c8cfe410f1186a7421186c64e8d7c4ba50d918f802",
    "b": "3075f2cf5812937899f6301a7da660bb8457a9ae3957e679f8694d72bfc22c80",
}
FORM_NAMES = {
    (1, 0, 0): "x1",
    (0, 1, 0): "x0",
    (0, 0, 1): "b",
}


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--coordinate-map", type=Path, default=COORDINATE_MAP)
    parser.add_argument("--coordinate-columns", type=Path, default=COORDINATE_COLUMNS)
    return parser.parse_args()


def trim(polynomial):
    result = [value % PRIME for value in polynomial]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_add(*polynomials):
    size = max(map(len, polynomials))
    return trim([
        sum(poly[index] if index < len(poly) else 0 for poly in polynomials)
        % PRIME
        for index in range(size)
    ])


def poly_scale(polynomial, scalar):
    return trim([scalar * value for value in polynomial])


def ntt(values, inverse=False):
    size = len(values)
    require(size and size & (size - 1) == 0, "NTT size is not a power of two")
    require((PRIME - 1) % size == 0, "NTT size does not divide field order")
    right = 0
    for left in range(1, size):
        bit = size >> 1
        while right & bit:
            right ^= bit
            bit >>= 1
        right ^= bit
        if left < right:
            values[left], values[right] = values[right], values[left]
    width = 2
    while width <= size:
        root = pow(PRIMITIVE_ROOT, (PRIME - 1) // width, PRIME)
        if inverse:
            root = pow(root, -1, PRIME)
        half = width >> 1
        for start in range(0, size, width):
            power = 1
            for offset in range(half):
                even = values[start + offset]
                odd = values[start + offset + half] * power % PRIME
                values[start + offset] = (even + odd) % PRIME
                values[start + offset + half] = (even - odd) % PRIME
                power = power * root % PRIME
        width <<= 1
    if inverse:
        inverse_size = pow(size, -1, PRIME)
        for index, value in enumerate(values):
            values[index] = value * inverse_size % PRIME


def poly_mul(left, right):
    left, right = trim(left), trim(right)
    if left == [0] or right == [0]:
        return [0]
    output_size = len(left) + len(right) - 1
    transform_size = 1
    while transform_size < output_size:
        transform_size <<= 1
    left_transform = left + [0] * (transform_size - len(left))
    right_transform = right + [0] * (transform_size - len(right))
    ntt(left_transform)
    ntt(right_transform)
    product = [
        left_value * right_value % PRIME
        for left_value, right_value in zip(left_transform, right_transform)
    ]
    ntt(product, inverse=True)
    return trim(product[:output_size])


def evaluate(polynomial, value):
    result = 0
    for coefficient in reversed(polynomial):
        result = (result * value + coefficient) % PRIME
    return result


def evaluate_fraction(record, value):
    denominator = evaluate(record["denominator"], value)
    require(denominator != 0, f"coordinate pole at t={value}")
    return evaluate(record["numerator"], value) * pow(denominator, -1, PRIME) % PRIME


def load_columns(path):
    raw = path.read_bytes()
    if path.resolve() == COORDINATE_COLUMNS.resolve():
        require(
            hashlib.sha256(raw).hexdigest() == EXPECTED_COLUMNS_SHA256,
            "coordinate-column packet hash mismatch",
        )
    payload = json.loads(raw)
    require(isinstance(payload, list) and len(payload) == 3, "coordinate-column shard count mismatch")
    columns = {}
    for shard in payload:
        key = (shard["gamma"], shard["alpha"], shard["beta"])
        require(key in FORM_NAMES and FORM_NAMES[key] not in columns, "coordinate-column form mismatch")
        require(shard["status"] == "COMPLETE" and shard["returncode"] == 0, "coordinate column incomplete")
        require(shard["basis_sha256"] == "8fd93095924f616770e49257ae45f255a8859f43c4f87100859cadfc8cc77ed6", "coordinate-column basis mismatch")
        records = {
            item["row"]: item
            for item in shard["entries"]
            if item["kind"] == "C" and item["column"] == 1
        }
        require(set(records) == set(range(1, DIMENSION + 1)), "coordinate-column coverage mismatch")
        columns[FORM_NAMES[key]] = records
    require(set(columns) == set(FORM_NAMES.values()), "coordinate-column forms incomplete")
    return columns, raw


def load_maps(path):
    raw = path.read_bytes()
    if path.resolve() == COORDINATE_MAP.resolve():
        require(
            hashlib.sha256(raw).hexdigest() == EXPECTED_MAP_SHA256,
            "coordinate-map packet hash mismatch",
        )
    payload = json.loads(raw)
    require(isinstance(payload, list) and len(payload) == 3, "coordinate-map count mismatch")
    maps = {}
    for item in payload:
        name = item["name"]
        require(name in EXPECTED_PROGRAM_SHA256 and name not in maps, "coordinate-map name mismatch")
        require(item["status"] == "COMPLETE" and item["returncode"] == 0, "coordinate map incomplete")
        require("PRIMITIVE_COORDINATE_MAP_COMPLETE" in item["stdout"], "coordinate-map marker missing")
        require(item["operator_sha256"] == operator_checker.EXPECTED_OPERATOR_SHA256, "coordinate-map operator provenance mismatch")
        require(item["coordinate_columns_sha256"] == EXPECTED_COLUMNS_SHA256, "coordinate-map column provenance mismatch")
        require(item["basis_sha256"] == "8fd93095924f616770e49257ae45f255a8859f43c4f87100859cadfc8cc77ed6", "coordinate-map basis mismatch")
        require(item["program_sha256"] == EXPECTED_PROGRAM_SHA256[name], "coordinate-map program mismatch")
        records = sorted(item["coordinates"], key=lambda record: record["degree"])
        require([record["degree"] for record in records] == list(range(DIMENSION)), "coordinate-map degree coverage mismatch")
        require(all(record["name"] == name for record in records), "coordinate-map record name mismatch")
        require(all(record["denominator"] != [0] for record in records), "zero coordinate denominator")
        maps[name] = records
    require(set(maps) == set(EXPECTED_PROGRAM_SHA256), "coordinate maps incomplete")
    return maps, raw


def verify_linear_identity(maps):
    for degree in range(DIMENSION):
        x1 = maps["x1"][degree]
        x0 = maps["x0"][degree]
        b = maps["b"][degree]
        x0_b_denominator = poly_mul(x0["denominator"], b["denominator"])
        x1_b_denominator = poly_mul(x1["denominator"], b["denominator"])
        x1_x0_denominator = poly_mul(x1["denominator"], x0["denominator"])
        common_denominator = poly_mul(x1["denominator"], x0_b_denominator)
        numerator = poly_add(
            poly_mul(x1["numerator"], x0_b_denominator),
            poly_scale(poly_mul(x0["numerator"], x1_b_denominator), 2),
            poly_scale(poly_mul(b["numerator"], x1_x0_denominator), 3),
        )
        expected = common_denominator if degree == 1 else [0]
        require(numerator == expected, f"x1+2*x0+3*b=s fails in degree {degree}")


def matrix_vector(matrix, vector):
    return [
        sum(left * right for left, right in zip(row, vector)) % PRIME
        for row in matrix
    ]


def verify_specialized_action(maps, columns):
    operator_checker.verify()
    operator = json.loads(operator_checker.OPERATOR.read_text())
    matrix = [[0] * DIMENSION for _ in range(DIMENSION)]
    seen = set()
    for entry in operator["entries"]:
        if entry["kind"] != "C":
            continue
        key = (entry["row"] - 1, entry["column"] - 1)
        require(key not in seen, "duplicate operator coordinate")
        seen.add(key)
        matrix[key[0]][key[1]] = operator_checker.evaluate_fraction(
            entry, operator_checker.FIBER
        )
    require(len(seen) == DIMENSION**2, "operator coordinate coverage mismatch")
    for name, records in maps.items():
        current = [1] + [0] * (DIMENSION - 1)
        result = [0] * DIMENSION
        for record in records:
            coefficient = evaluate_fraction(record, operator_checker.FIBER)
            result = [
                (left + coefficient * right) % PRIME
                for left, right in zip(result, current)
            ]
            current = matrix_vector(matrix, current)
        expected = [
            operator_checker.evaluate_fraction(columns[name][row], operator_checker.FIBER)
            for row in range(1, DIMENSION + 1)
        ]
        require(result == expected, f"{name} primitive action mismatch at t=2")


def verify(map_path=COORDINATE_MAP, columns_path=COORDINATE_COLUMNS):
    columns, columns_raw = load_columns(columns_path)
    maps, map_raw = load_maps(map_path)
    verify_linear_identity(maps)
    verify_specialized_action(maps, columns)
    max_degree = max(
        len(polynomial) - 1
        for records in maps.values()
        for record in records
        for polynomial in (record["numerator"], record["denominator"])
    )
    return maps, map_raw, columns_raw, max_degree


def main():
    args = parse_args()
    maps, map_raw, columns_raw, max_degree = verify(
        args.coordinate_map, args.coordinate_columns
    )
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_PRIMITIVE_COORDINATE_MAP_PASS "
        f"maps={','.join(sorted(maps))} degrees=0..23 max_t_degree={max_degree} "
        "identity=x1+2*x0+3*b=s specialized_action_fiber=2 "
        f"map_sha256={hashlib.sha256(map_raw).hexdigest()} "
        f"columns_sha256={hashlib.sha256(columns_raw).hexdigest()}"
    )


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, ValueError) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_PRIMITIVE_COORDINATE_MAP_FAIL {error}")
        raise SystemExit(1)
