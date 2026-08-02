#!/usr/bin/env python3
"""Choose exact pivot rows/columns for a packed cell-5 guard-power matrix."""

import argparse
import hashlib
import json
import struct
from pathlib import Path


DIRECTORY = Path(__file__).parent
PACKET = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_matrix_coefficients.bin"
)
PACKET_METADATA = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_matrix_coefficients_meta.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_pivots_result.json"
)
PRIME = 2130706433
T_VALUES = (2, 3, 4, 5)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", type=Path, default=PACKET)
    parser.add_argument("--metadata", type=Path, default=PACKET_METADATA)
    parser.add_argument("--result", type=Path, default=RESULT)
    parser.add_argument("--expected-ranks", default="32,24,24")
    return parser.parse_args()


def read_packet(path, power):
    data = memoryview(path.read_bytes())
    offset = 0
    if bytes(data[:8]) != f"KBC5M{power:02d}\n".encode():
        raise RuntimeError("bad packet magic")
    offset += 8
    count = struct.unpack_from("<I", data, offset)[0]
    offset += 4
    basis_sha256 = bytes(data[offset:offset + 32]).hex()
    offset += 32
    coefficients_sha256 = bytes(data[offset:offset + 32]).hex()
    offset += 32
    entries = {}
    for _ in range(count):
        row, column, numerator_length, denominator_length = struct.unpack_from(
            "<BBHH", data, offset
        )
        offset += 6
        numerator = struct.unpack_from(f"<{numerator_length}I", data, offset)
        offset += 4 * numerator_length
        denominator = struct.unpack_from(f"<{denominator_length}I", data, offset)
        offset += 4 * denominator_length
        entries[(row - 1, column - 1)] = (numerator, denominator)
    if offset != len(data) or len(entries) != count:
        raise RuntimeError("packet coverage mismatch")
    return basis_sha256, coefficients_sha256, entries


def evaluate(coefficients, value):
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % PRIME
    return result


def matrix_at(entries, value):
    matrix = [[0] * 64 for _ in range(64)]
    for (row, column), (numerator, denominator) in entries.items():
        denominator_value = evaluate(denominator, value)
        if denominator_value == 0:
            raise RuntimeError(f"denominator vanishes at t={value}")
        matrix[row][column] = (
            evaluate(numerator, value) * pow(denominator_value, -1, PRIME)
        ) % PRIME
    return matrix


def rank_and_pivots(matrix):
    work = [row[:] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    pivot_columns = []
    pivot_row = 0
    for column in range(columns):
        selected = next(
            (row for row in range(pivot_row, rows) if work[row][column]),
            None,
        )
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, PRIME)
        work[pivot_row] = [(value * inverse) % PRIME for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or work[row][column] == 0:
                continue
            scale = work[row][column]
            work[row] = [
                (left - scale * right) % PRIME
                for left, right in zip(work[row], work[pivot_row])
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row, pivot_columns


def multiply(left, right):
    transpose = list(zip(*right))
    return [
        [sum(a * b for a, b in zip(row, column)) % PRIME for column in transpose]
        for row in left
    ]


def determinant(matrix):
    work = [row[:] for row in matrix]
    result = 1
    for column in range(len(work)):
        selected = next(
            (row for row in range(column, len(work)) if work[row][column]),
            None,
        )
        if selected is None:
            return 0
        if selected != column:
            work[column], work[selected] = work[selected], work[column]
            result = -result
        pivot = work[column][column]
        result = result * pivot % PRIME
        inverse = pow(pivot, -1, PRIME)
        for row in range(column + 1, len(work)):
            scale = work[row][column] * inverse % PRIME
            for index in range(column, len(work)):
                work[row][index] = (
                    work[row][index] - scale * work[column][index]
                ) % PRIME
    return result % PRIME


def main():
    args = parse_args()
    expected_ranks = tuple(int(value) for value in args.expected_ranks.split(","))
    if len(expected_ranks) != 3:
        raise RuntimeError("expected-ranks must contain three comma-separated integers")
    metadata = json.loads(args.metadata.read_text())
    power = metadata.get("guard_power", 1)
    packet_sha256 = hashlib.sha256(args.packet.read_bytes()).hexdigest()
    if packet_sha256 != metadata["packet_sha256"]:
        raise RuntimeError("packet hash mismatch")
    basis_sha256, coefficients_sha256, entries = read_packet(args.packet, power)
    if basis_sha256 != metadata["basis_sha256"]:
        raise RuntimeError("basis hash mismatch")
    if coefficients_sha256 != metadata["coefficients_sha256"]:
        raise RuntimeError("coefficient hash mismatch")

    samples = []
    pivot_rows = None
    pivot_columns = None
    pivot_determinant = None
    for value in T_VALUES:
        matrix = matrix_at(entries, value)
        rank, columns = rank_and_pivots(matrix)
        squared = multiply(matrix, matrix)
        squared_rank, _ = rank_and_pivots(squared)
        cubed_rank, _ = rank_and_pivots(multiply(squared, matrix))
        samples.append(
            {
                "t": value,
                "rank": rank,
                "squared_rank": squared_rank,
                "cubed_rank": cubed_rank,
            }
        )
        if value == T_VALUES[0]:
            selected = [[matrix[row][column] for column in columns] for row in range(64)]
            _, rows = rank_and_pivots([list(row) for row in zip(*selected)])
            pivot_rows = rows
            pivot_columns = columns
            pivot_matrix = [
                [matrix[row][column] for column in pivot_columns]
                for row in pivot_rows
            ]
            pivot_determinant = determinant(pivot_matrix)
    if any(
        (item["rank"], item["squared_rank"], item["cubed_rank"])
        != expected_ranks
        for item in samples
    ):
        raise RuntimeError(
            f"specialized rank pattern is not {expected_ranks}: {samples}"
        )
    expected_rank = expected_ranks[0]
    if (
        len(pivot_rows) != expected_rank
        or len(pivot_columns) != expected_rank
        or not pivot_determinant
    ):
        raise RuntimeError(f"failed to choose an invertible {expected_rank}x{expected_rank} minor")
    result = {
        "schema": "rate-half-kb-positive-433-1a-cell5-guard-power-pivots-v1",
        "guard_power": power,
        "basis_sha256": basis_sha256,
        "coefficients_sha256": coefficients_sha256,
        "packet_sha256": packet_sha256,
        "samples": samples,
        "pivot_t": T_VALUES[0],
        "pivot_rows": [value + 1 for value in pivot_rows],
        "pivot_columns": [value + 1 for value in pivot_columns],
        "pivot_determinant": pivot_determinant,
        "scope": (
            "exact deployed-field specializations used only to choose a minor; "
            "generic rank still requires the rational-function factorization"
        ),
    }
    args.result.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_GUARD_PIVOTS_PASS "
        f"ranks={expected_ranks} determinant={pivot_determinant}"
    )


if __name__ == "__main__":
    main()
