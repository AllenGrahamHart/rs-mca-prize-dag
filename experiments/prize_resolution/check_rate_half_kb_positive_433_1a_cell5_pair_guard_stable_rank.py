#!/usr/bin/env python3
"""Independent exact checker for the cell-5 guard stable-rank certificate."""

import argparse
import hashlib
import json
import struct
from pathlib import Path

HERE = Path(__file__).parent
PRIME = 2130706433
MATRIX_SIZE = 64
PIVOT_SIZE = 24
BASIS_RESULT = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_function_field_julia_basis_result.json"
)
EXPECTED_BASIS_FILE_SHA256 = (
    "576df7138502bf60657c7386d7dbc6eb6a4b9ea60a8f65d3745af3f5fd91820d"
)
EXPECTED_BASIS_SHA256 = (
    "8fd93095924f616770e49257ae45f255a8859f43c4f87100859cadfc8cc77ed6"
)
EXPECTED_PROGRAM_SHA256 = (
    "fbe8f00d663dd381c1fb1f57e231a04e0645e0c6b839368386f22aaee88737ba"
)
SQUARE_PACKET = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients.bin"
)
SQUARE_METADATA = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients_meta.json"
)
SQUARE_PIVOTS = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_pivots_result.json"
)
FACTORIZATION = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_"
    "factorization_structured_result.json"
)
GUARD_PACKET = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_matrix_coefficients.bin"
)
GUARD_METADATA = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_matrix_coefficients_meta.json"
)
CLEARED_PACKET = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_cleared.bin"
)
CLEARED_METADATA = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_cleared_meta.json"
)


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def parse_leading_monomial(polynomial):
    term = polynomial.split(" + ", 1)[0]
    exponents = {"x1": 0, "x0": 0, "b": 0}
    for factor in term.split("*"):
        variable, separator, exponent = factor.partition("^")
        require(variable in exponents, "nonmonic or unknown leading term")
        exponents[variable] += int(exponent) if separator else 1
    return exponents["x1"], exponents["x0"], exponents["b"]


def read_basis_provenance():
    raw = BASIS_RESULT.read_bytes()
    require(
        hashlib.sha256(raw).hexdigest() == EXPECTED_BASIS_FILE_SHA256,
        "basis-result file hash mismatch",
    )
    payload = json.loads(raw)
    require(isinstance(payload, list) and len(payload) == 1, "bad basis result")
    result = payload[0]
    require(
        result["status"] == "COMPLETE" and result["returncode"] == 0,
        "basis computation did not complete",
    )
    require(
        result["field"] == f"GF({PRIME})(t)"
        and result["chart_index"] == 2
        and result["stage"] == "squared-export",
        "basis scope mismatch",
    )
    require(
        result["program_sha256"] == EXPECTED_PROGRAM_SHA256,
        "basis program hash mismatch",
    )
    stdout = result["stdout"]
    require(
        "PAIR_JULIA_FF_SQUARED_EXPORT_START" in stdout
        and "PAIR_JULIA_FF_SQUARED_EXPORT_COMPLETE" in stdout,
        "basis Groebner-stage markers missing",
    )
    basis_lines = result["basis_lines"]
    require(len(basis_lines) == 18, "unexpected Groebner basis size")
    basis_text = "\n".join(basis_lines)
    basis_sha256 = hashlib.sha256(basis_text.encode()).hexdigest()
    require(
        basis_sha256 == result["basis_sha256"] == EXPECTED_BASIS_SHA256,
        "canonical Groebner basis hash mismatch",
    )
    leading = tuple(parse_leading_monomial(line) for line in basis_lines)
    expected_leading = (
        (0, 0, 4),
        (2, 2, 1),
        (2, 1, 3),
        (4, 0, 2),
        (4, 1, 1),
        (5, 0, 1),
        (3, 3, 0),
        (4, 2, 0),
        (5, 1, 0),
        (6, 0, 0),
        (1, 3, 3),
        (1, 4, 2),
        (0, 6, 1),
        (1, 5, 1),
        (0, 7, 0),
        (1, 6, 0),
        (2, 5, 0),
        (0, 5, 3),
    )
    require(leading == expected_leading, "leading-monomial ledger mismatch")
    standard_count = sum(
        1
        for x1 in range(6)
        for x0 in range(7)
        for b in range(4)
        if not any(
            x1 >= lead_x1 and x0 >= lead_x0 and b >= lead_b
            for lead_x1, lead_x0, lead_b in leading
        )
    )
    require(standard_count == MATRIX_SIZE, "standard-monomial count mismatch")
    return result


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--factorization", type=Path, default=FACTORIZATION)
    parser.add_argument("--columns", default="25:64")
    return parser.parse_args()


def read_packet(path, metadata_path, expected_power):
    metadata = json.loads(metadata_path.read_text())
    raw = path.read_bytes()
    require(
        hashlib.sha256(raw).hexdigest() == metadata["packet_sha256"],
        "packet hash mismatch",
    )
    require(metadata.get("guard_power", 1) == expected_power, "guard-power mismatch")
    data = memoryview(raw)
    require(bytes(data[:8]) == f"KBC5M{expected_power:02d}\n".encode(), "bad magic")
    offset = 8
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
        require((row, column) not in entries, "duplicate packet entry")
        require(
            numerator
            and denominator
            and any(denominator)
            and all(value < PRIME for value in numerator + denominator),
            "invalid packet coefficient",
        )
        entries[(row, column)] = (numerator, denominator)
    require(offset == len(data), "trailing or truncated packet bytes")
    require(len(entries) == count, "packet entry-count mismatch")
    require(basis_sha256 == metadata["basis_sha256"], "basis hash mismatch")
    require(
        coefficients_sha256 == metadata["coefficients_sha256"],
        "coefficient hash mismatch",
    )

    digest = hashlib.sha256()
    for index, ((row, column), (numerator, denominator)) in enumerate(
        sorted(entries.items())
    ):
        if index:
            digest.update(b"\n")
        line = (
            f"{row},{column}:{','.join(map(str, numerator))}/"
            f"{','.join(map(str, denominator))}"
        )
        digest.update(line.encode())
    require(digest.hexdigest() == coefficients_sha256, "canonical hash mismatch")
    return metadata, entries


def validate_coefficients(numerator, denominator):
    require(
        isinstance(numerator, list)
        and isinstance(denominator, list)
        and numerator
        and denominator,
        "empty coordinate coefficient vector",
    )
    require(
        all(isinstance(value, int) and 0 <= value < PRIME
            for value in numerator + denominator),
        "coordinate outside deployed field",
    )
    require(any(denominator), "zero coordinate denominator")


def collect_coordinates(data, square_metadata, pivots_hash):
    require(isinstance(data, list), "factorization root is not a list")
    coordinates = {}
    covered = set()
    basis_hash = square_metadata["basis_sha256"]
    coefficient_hash = square_metadata["coefficients_sha256"]
    packet_hash = square_metadata["packet_sha256"]
    for shard in data:
        require(shard["status"] == "COMPLETE", "incomplete factorization shard")
        require(shard["returncode"] == 0, "nonzero factorization return code")
        require(shard["guard_power"] == 2, "factorization guard-power mismatch")
        require(shard["pivot_size"] == PIVOT_SIZE, "factorization pivot mismatch")
        require(shard["basis_sha256"] == basis_hash, "shard basis hash mismatch")
        require(
            shard["coefficients_sha256"] == coefficient_hash,
            "shard coefficient hash mismatch",
        )
        require(shard["packet_sha256"] == packet_hash, "shard packet hash mismatch")
        require(shard["pivots_sha256"] == pivots_hash, "shard pivot hash mismatch")
        require(
            "GUARD_FACTOR_SHARD_VERIFIED" in shard["stdout"],
            "primary exact-verification marker missing",
        )
        for column in range(shard["start"], shard["stop"] + 1):
            require(column not in covered, "duplicate factorization column")
            covered.add(column)
        for item in shard["coordinates"]:
            row = item["row"]
            column = item["column"]
            require(
                1 <= row <= PIVOT_SIZE and 25 <= column <= MATRIX_SIZE,
                "coordinate index out of range",
            )
            validate_coefficients(item["numerator"], item["denominator"])
            key = (row, column)
            require(key not in coordinates, "duplicate factorization coordinate")
            coordinates[key] = (
                tuple(item["numerator"]),
                tuple(item["denominator"]),
            )
    require(covered == set(range(25, 65)), "factorization column coverage mismatch")
    require(
        set(coordinates) == {
            (row, column)
            for row in range(1, PIVOT_SIZE + 1)
            for column in range(25, MATRIX_SIZE + 1)
        },
        "factorization coordinate coverage mismatch",
    )
    return coordinates


def expected_cleared_keys():
    keys = {("E", row, 0) for row in range(1, 65)}
    keys |= {
        ("P", row, column)
        for row in range(1, 65)
        for column in range(1, 25)
    }
    keys |= {
        ("B", row, column)
        for row in range(1, 65)
        for column in range(25, 65)
    }
    keys |= {("D", 0, column) for column in range(25, 65)}
    keys |= {
        ("Y", row, column)
        for row in range(1, 25)
        for column in range(25, 65)
    }
    return keys


def read_cleared_packet(square_metadata, factorization_path):
    metadata = json.loads(CLEARED_METADATA.read_text())
    raw = CLEARED_PACKET.read_bytes()
    require(
        hashlib.sha256(raw).hexdigest() == metadata["cleared_packet_sha256"],
        "cleared packet hash mismatch",
    )
    require(
        metadata["basis_sha256"] == square_metadata["basis_sha256"]
        and metadata["coefficients_sha256"] == square_metadata["coefficients_sha256"]
        and metadata["packet_sha256"] == square_metadata["packet_sha256"],
        "cleared packet matrix provenance mismatch",
    )
    require(
        hashlib.sha256(factorization_path.read_bytes()).hexdigest()
        == metadata["factorization_sha256"],
        "cleared packet factorization provenance mismatch",
    )
    data = memoryview(raw)
    require(bytes(data[:8]) == b"KBC5CLR\n", "bad cleared packet magic")
    offset = 8
    count = struct.unpack_from("<I", data, offset)[0]
    offset += 4
    header_names = (
        "basis_sha256",
        "coefficients_sha256",
        "packet_sha256",
        "factorization_sha256",
        "cleared_sha256",
    )
    for name in header_names:
        value = bytes(data[offset:offset + 32]).hex()
        offset += 32
        require(value == metadata[name], f"cleared header {name} mismatch")
    tags = {1: "E", 2: "P", 3: "B", 4: "D", 5: "Y"}
    records = {}
    for _ in range(count):
        tag_number, row, column, length = struct.unpack_from("<BBBH", data, offset)
        offset += 5
        coefficients = struct.unpack_from(f"<{length}I", data, offset)
        offset += 4 * length
        require(tag_number in tags, "unknown cleared record tag")
        require(
            coefficients and all(value < PRIME for value in coefficients),
            "invalid cleared coefficients",
        )
        key = (tags[tag_number], row, column)
        require(key not in records, "duplicate cleared record")
        records[key] = coefficients
    require(offset == len(data), "trailing or truncated cleared packet")
    require(set(records) == expected_cleared_keys(), "cleared record coverage mismatch")
    digest = hashlib.sha256()
    for index, ((tag, row, column), coefficients) in enumerate(sorted(records.items())):
        if index:
            digest.update(b"\n")
        digest.update(
            f"{tag},{row},{column}:{','.join(map(str, coefficients))}".encode()
        )
    require(digest.hexdigest() == metadata["cleared_sha256"], "cleared hash mismatch")
    return metadata, records


def evaluate(coefficients, value):
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % PRIME
    return result


def matrix_at(entries, value):
    matrix = [[0] * MATRIX_SIZE for _ in range(MATRIX_SIZE)]
    for (row, column), (numerator, denominator) in entries.items():
        denominator_value = evaluate(denominator, value)
        require(denominator_value != 0, f"pole at t={value}")
        matrix[row - 1][column - 1] = (
            evaluate(numerator, value) * pow(denominator_value, -1, PRIME)
        ) % PRIME
    return matrix


def multiply(left, right):
    transpose = list(zip(*right))
    return [
        [
            sum(a * b for a, b in zip(row, column)) % PRIME
            for column in transpose
        ]
        for row in left
    ]


def rank(matrix):
    work = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        selected = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if selected is None:
            continue
        work[pivot_row], work[selected] = work[selected], work[pivot_row]
        inverse = pow(work[pivot_row][column], -1, PRIME)
        work[pivot_row] = [
            value * inverse % PRIME for value in work[pivot_row]
        ]
        for row in range(pivot_row + 1, len(work)):
            scale = work[row][column]
            if scale:
                work[row] = [
                    (left - scale * right) % PRIME
                    for left, right in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


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


def finite_rank_audit(guard_entries, square_entries, pivots):
    expected = [(32, 24, 24)] * 4
    observed = []
    for value in (2, 3, 4, 5):
        guard = matrix_at(guard_entries, value)
        square = matrix_at(square_entries, value)
        computed_square = multiply(guard, guard)
        require(square == computed_square, f"guard-square mismatch at t={value}")
        cube = multiply(square, guard)
        observed.append((rank(guard), rank(square), rank(cube)))
    require(observed == expected, f"specialized rank pattern mismatch: {observed}")
    square_at_two = matrix_at(square_entries, 2)
    minor = [row[:PIVOT_SIZE] for row in square_at_two[:PIVOT_SIZE]]
    require(
        determinant(minor) == pivots["pivot_determinant"] != 0,
        "pivot determinant mismatch",
    )


def primitive_root():
    for candidate in range(2, 1000):
        if (
            pow(candidate, (PRIME - 1) // 2, PRIME) != 1
            and pow(candidate, (PRIME - 1) // 127, PRIME) != 1
        ):
            return candidate
    raise CertificateError("failed to find a primitive root")


def ntt(coefficients, size, root):
    values = list(coefficients) + [0] * (size - len(coefficients))
    require(len(values) == size, "polynomial exceeds NTT size")
    j = 0
    for index in range(1, size):
        bit = size >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if index < j:
            values[index], values[j] = values[j], values[index]
    length = 2
    while length <= size:
        step = pow(root, size // length, PRIME)
        half = length // 2
        for start in range(0, size, length):
            omega = 1
            for offset in range(half):
                left = values[start + offset]
                right = values[start + offset + half] * omega % PRIME
                values[start + offset] = (left + right) % PRIME
                values[start + offset + half] = (left - right) % PRIME
                omega = omega * step % PRIME
        length *= 2
    return tuple(values)


def exact_factorization(square_entries, coordinates, cleared, selected_columns):
    max_degree = 0

    def include(left, right):
        nonlocal max_degree
        max_degree = max(max_degree, len(left) + len(right) - 2)

    for row in range(1, 65):
        common = cleared[("E", row, 0)]
        for column in range(1, 25):
            numerator, denominator = square_entries[(row, column)]
            include(cleared[("P", row, column)], denominator)
            include(numerator, common)
        for column in selected_columns:
            numerator, denominator = square_entries[(row, column)]
            include(cleared[("B", row, column)], denominator)
            include(numerator, common)
    for column in selected_columns:
        common = cleared[("D", 0, column)]
        for row in range(1, 25):
            numerator, denominator = coordinates[(row, column)]
            include(cleared[("Y", row, column)], denominator)
            include(numerator, common)
    for row in range(1, 65):
        for column in selected_columns:
            for index in range(1, 25):
                include(
                    cleared[("P", row, index)],
                    cleared[("Y", index, column)],
                )
            include(
                cleared[("B", row, column)],
                cleared[("D", 0, column)],
            )
    size = 1
    while size <= max_degree:
        size *= 2
    require(size <= 2**24 and (PRIME - 1) % size == 0, "invalid NTT size")
    generator = primitive_root()
    root = pow(generator, (PRIME - 1) // size, PRIME)
    require(pow(root, size, PRIME) == 1, "NTT root has wrong order")
    if size > 1:
        require(pow(root, size // 2, PRIME) != 1, "NTT root is not primitive")
    cache = {}

    def transform(polynomial):
        polynomial = tuple(polynomial)
        if polynomial not in cache:
            cache[polynomial] = ntt(polynomial, size, root)
        return cache[polynomial]

    def product_equal(left, right, other_left, other_right, message):
        left_values = transform(left)
        right_values = transform(right)
        other_left_values = transform(other_left)
        other_right_values = transform(other_right)
        require(
            all(
                (a * b - c * d) % PRIME == 0
                for a, b, c, d in zip(
                    left_values,
                    right_values,
                    other_left_values,
                    other_right_values,
                )
            ),
            message,
        )

    for row in range(1, 65):
        common = cleared[("E", row, 0)]
        for column in range(1, 25):
            numerator, denominator = square_entries[(row, column)]
            product_equal(
                cleared[("P", row, column)],
                denominator,
                numerator,
                common,
                f"pivot clearing mismatch row={row} column={column}",
            )
        for column in selected_columns:
            numerator, denominator = square_entries[(row, column)]
            product_equal(
                cleared[("B", row, column)],
                denominator,
                numerator,
                common,
                f"target clearing mismatch row={row} column={column}",
            )
    for column in selected_columns:
        common = cleared[("D", 0, column)]
        for row in range(1, 25):
            numerator, denominator = coordinates[(row, column)]
            product_equal(
                cleared[("Y", row, column)],
                denominator,
                numerator,
                common,
                f"coordinate clearing mismatch row={row} column={column}",
            )

    for row in range(1, 65):
        pivot_values = [
            transform(cleared[("P", row, index)])
            for index in range(1, 25)
        ]
        for column in selected_columns:
            coordinate_values = [
                transform(cleared[("Y", index, column)])
                for index in range(1, 25)
            ]
            target_values = transform(cleared[("B", row, column)])
            common_values = transform(cleared[("D", 0, column)])
            for point in range(size):
                value = 0
                for index in range(24):
                    value += (
                        pivot_values[index][point]
                        * coordinate_values[index][point]
                    )
                require(
                    value % PRIME
                    == target_values[point] * common_values[point] % PRIME,
                    f"exact factorization mismatch row={row} column={column}",
                )
    return size, max_degree


def load_certificate(factorization_path=FACTORIZATION):
    basis_result = read_basis_provenance()
    square_metadata, square_entries = read_packet(
        SQUARE_PACKET, SQUARE_METADATA, 2
    )
    guard_metadata, guard_entries = read_packet(GUARD_PACKET, GUARD_METADATA, 1)
    require(
        square_metadata["basis_sha256"]
        == guard_metadata["basis_sha256"]
        == basis_result["basis_sha256"],
        "guard packets use different quotient bases",
    )
    pivots = json.loads(SQUARE_PIVOTS.read_text())
    pivots_hash = hashlib.sha256(SQUARE_PIVOTS.read_bytes()).hexdigest()
    require(pivots["guard_power"] == 2, "pivot guard-power mismatch")
    require(pivots["pivot_rows"] == list(range(1, 25)), "pivot rows mismatch")
    require(pivots["pivot_columns"] == list(range(1, 25)), "pivot columns mismatch")
    require(
        pivots["packet_sha256"] == square_metadata["packet_sha256"],
        "pivot packet hash mismatch",
    )
    data = json.loads(factorization_path.read_text())
    coordinates = collect_coordinates(data, square_metadata, pivots_hash)
    cleared_metadata, cleared = read_cleared_packet(
        square_metadata, factorization_path
    )
    return (
        square_metadata,
        square_entries,
        guard_entries,
        pivots,
        data,
        coordinates,
        cleared_metadata,
        cleared,
    )


def verify(factorization_path=FACTORIZATION, selected_columns=range(25, 65)):
    (
        square_metadata,
        square_entries,
        guard_entries,
        pivots,
        _,
        coordinates,
        cleared_metadata,
        cleared,
    ) = load_certificate(factorization_path)
    finite_rank_audit(guard_entries, square_entries, pivots)
    ntt_size, max_degree = exact_factorization(
        square_entries, coordinates, cleared, selected_columns
    )
    return square_metadata, cleared_metadata, ntt_size, max_degree


def main():
    args = parse_args()
    first, last = (int(value) for value in args.columns.split(":", 1))
    require(25 <= first <= last <= 64, "column selection must lie in 25..64")
    try:
        metadata, cleared_metadata, ntt_size, max_degree = verify(
            args.factorization, range(first, last + 1)
        )
    except (CertificateError, KeyError, ValueError, struct.error) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_GUARD_STABLE_RANK_FAIL {error}")
        raise SystemExit(1)
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_GUARD_STABLE_RANK_PASS "
        f"columns={first}:{last} generic_rank_M2=24 "
        f"ntt_size={ntt_size} max_degree={max_degree} "
        f"packet_sha256={metadata['packet_sha256']} "
        f"cleared_sha256={cleared_metadata['cleared_packet_sha256']}"
    )


if __name__ == "__main__":
    main()
