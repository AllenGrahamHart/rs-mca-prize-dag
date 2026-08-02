#!/usr/bin/env python3
"""Check coordinate regularization and all 38 dynamic cell-5 replays."""

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import check_rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map as maps
import check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization as factorcheck
import probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber as probe


PRIME = 2130706433
REGULARIZED = HERE / (
    "rate_half_kb_positive_433_1a_cell5_coordinate_operator_regularization_result.json"
)
REPLAY = HERE / "rate_half_kb_positive_433_1a_cell5_dynamic_fiber_replay_result.json"
OPERATOR = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_localized_operator_merged_result.json"
)
COORDINATE_MAPS = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json"
)
EXPECTED_REGULARIZED_SHA256 = (
    "139f1367ec799f5884372f0d09841e5593036751dd1ceedf09df5d801879098a"
)
EXPECTED_REPLAY_SHA256 = (
    "1e20aefa7fa7e024ab0c133c961982793c031c5322fb9fc2325cb41215488c73"
)
EXPECTED_PROGRAM_HASHES = {
    "x1": "89d63391da575f423a0c9b46beb6ee0c100d697878776cb046ece971bfb15291",
    "x0": "bf1ab4b5b8670813696e2871537a0a3211b660200a01fa27e47f24ff51f6c823",
    "b": "c455c251260a679fb84e3ccab2ff5bc8e7d942f2b8dc71911498cbcd846a6eea",
}
FIBERS = (
    59577338, 60142635, 259897937, 314606277, 350200897, 399214728,
    429335281, 534616264, 658388861, 719443868, 825068466, 898552563,
    967866903, 1108567599, 1112415117, 1156161765, 1157872027,
    1179254816, 1182328414, 1207246658, 1248074151, 1328213402,
    1379619328, 1410757125, 1502791638, 1548270121, 1552698975,
    1593520725, 1594419216, 1618157807, 1618717679, 1777239993,
    1910266670, 1969598264, 2026412590, 2029231698, 2042457704,
    2086242076,
)
SOURCE_FILES = (
    "rate_half_kb_positive_433_1a_cell5_coordinate_operator_regularization_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_localized_operator_merged_result.json",
    "probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_generic_guard_units.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_localized_operator.py",
    "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py",
    "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_coordinate_columns_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients.bin",
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients_meta.json",
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial_result.json",
)


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def evaluate(polynomial, point):
    value = 0
    for coefficient in reversed(polynomial):
        value = (value * point + coefficient) % PRIME
    return value


def evaluate_entry(entry, point):
    denominator = evaluate(entry["denominator"], point)
    require(denominator != 0, f"matrix pole at {point}")
    return evaluate(entry["numerator"], point) * pow(denominator, -1, PRIME) % PRIME


def matrix_from_entries(entries, point):
    matrix = [[0] * 24 for _ in range(24)]
    for (row, column), entry in entries.items():
        matrix[row][column] = evaluate_entry(entry, point)
    return matrix


def matrix_linear(terms):
    return [
        [sum(scalar * matrix[row][column] for scalar, matrix in terms) % PRIME for column in range(24)]
        for row in range(24)
    ]


def matrix_vector(matrix, vector):
    return [
        sum(left * right for left, right in zip(row, vector)) % PRIME
        for row in matrix
    ]


def matrix_multiply(left, right):
    columns = list(zip(*right))
    return [
        [sum(a * b for a, b in zip(row, column)) % PRIME for column in columns]
        for row in left
    ]


def solve(matrix, right_hand_sides):
    size = len(matrix)
    width = len(right_hand_sides)
    augmented = [
        list(matrix[row]) + [right_hand_sides[index][row] for index in range(width)]
        for row in range(size)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if augmented[row][column] % PRIME),
            None,
        )
        require(pivot is not None, "singular claimed Krylov matrix")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        inverse = pow(augmented[column][column], -1, PRIME)
        augmented[column] = [value * inverse % PRIME for value in augmented[column]]
        for row in range(size):
            if row == column or augmented[row][column] == 0:
                continue
            scale = augmented[row][column]
            augmented[row] = [
                (left - scale * right) % PRIME
                for left, right in zip(augmented[row], augmented[column])
            ]
    return [
        [augmented[row][size + index] for row in range(size)]
        for index in range(width)
    ]


def primitive_candidates():
    output = []
    for value in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1)):
        if value not in output:
            output.append(value)
    for alpha in range(16):
        for beta in range(16):
            value = (1, alpha, beta)
            if value not in output and value != (1, 2, 3):
                output.append(value)
    return output


def canonical(entry):
    value = factorcheck.rational(entry["numerator"], entry["denominator"])
    require(
        value == (tuple(entry["numerator"]), tuple(entry["denominator"])),
        "noncanonical rational entry",
    )
    return value


def scalar(value):
    return ((value % PRIME,), (1,))


def load_regularized(path):
    raw = path.read_bytes()
    if path == REGULARIZED:
        require(hashlib.sha256(raw).hexdigest() == EXPECTED_REGULARIZED_SHA256, "regularized hash mismatch")
    payload = json.loads(raw)
    require(isinstance(payload, list) and len(payload) == 3, "regularized coordinate count mismatch")
    output = {}
    for item in payload:
        name = item["name"]
        require(name in EXPECTED_PROGRAM_HASHES and name not in output, "regularized coordinate name mismatch")
        require(item["status"] == "COMPLETE" and item["returncode"] == 0, "regularization incomplete")
        require(item["operator_sha256"] == maps.operator_checker.EXPECTED_OPERATOR_SHA256, "operator provenance mismatch")
        require(item["maps_sha256"] == maps.EXPECTED_MAP_SHA256, "map provenance mismatch")
        require(item["program_sha256"] == EXPECTED_PROGRAM_HASHES[name], "regularization program mismatch")
        require(item["map_pole_fibers"] == list(FIBERS), "map-pole route mismatch")
        require(not item["uncancelled_poles"], "coordinate has uncancelled pole")
        entries = {
            (entry["row"] - 1, entry["column"] - 1): entry
            for entry in item["entries"]
        }
        require(set(entries) == {(row, column) for row in range(24) for column in range(24)}, "matrix coverage mismatch")
        for entry in entries.values():
            canonical(entry)
            require(all(evaluate(entry["denominator"], fiber) for fiber in FIBERS), "listed map pole remains")
        output[name] = entries
    return output, raw


def verify_exact_coordinate_identity(entries):
    operator = json.loads(OPERATOR.read_text())
    old = {
        (entry["row"] - 1, entry["column"] - 1): entry
        for entry in operator["entries"]
        if entry["kind"] == "C"
    }
    require(set(old) == set(entries["x1"]), "old operator coverage mismatch")
    two, three = scalar(2), scalar(3)
    for key in old:
        expected = factorcheck.rational_add(
            canonical(entries["x1"][key]),
            factorcheck.rational_add(
                factorcheck.rational_mul(two, canonical(entries["x0"][key])),
                factorcheck.rational_mul(three, canonical(entries["b"][key])),
            ),
        )
        require(expected == canonical(old[key]), "exact coordinate-operator identity fails")
    return old


def verify_regular_fiber_action(entries, old):
    point = 2
    old_matrix = matrix_from_entries(old, point)
    powers = []
    current = [[int(row == column) for column in range(24)] for row in range(24)]
    for _ in range(24):
        powers.append(current)
        current = matrix_multiply(old_matrix, current)
    map_payload = {item["name"]: item for item in json.loads(COORDINATE_MAPS.read_text())}
    for name in ("x1", "x0", "b"):
        coefficients = [maps.evaluate_fraction(record, point) for record in sorted(map_payload[name]["coordinates"], key=lambda item: item["degree"])]
        reconstructed = matrix_linear(tuple(
            (coefficient, powers[degree])
            for degree, coefficient in enumerate(coefficients)
            if coefficient
        ))
        require(reconstructed == matrix_from_entries(entries[name], point), f"regular action mismatch for {name}")


def verify_replay(path, regularized_entries, old_entries):
    raw = path.read_bytes()
    if path == REPLAY:
        require(hashlib.sha256(raw).hexdigest() == EXPECTED_REPLAY_SHA256, "replay hash mismatch")
    payload = json.loads(raw)
    require(payload["schema"].endswith("dynamic-fiber-replay-v1"), "replay schema mismatch")
    require(payload["status"] == "COMPLETE" and payload["characteristic"] == PRIME, "replay incomplete")
    require(payload["fibers"] == list(FIBERS), "fiber route mismatch")
    expected_sources = {
        name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
        for name in SOURCE_FILES
    }
    require(payload["source_sha256"] == expected_sources, "replay source provenance mismatch")
    results = payload["results"]
    require(len(results) == 38 and [item["fiber"] for item in results] == list(FIBERS), "fiber coverage mismatch")
    candidates = primitive_candidates()
    reason_counts = Counter()
    gcd_counts = Counter()
    total_rows = 0
    forms = Counter()
    identity = [[int(row == column) for column in range(24)] for row in range(24)]
    unit = [1] + [0] * 23
    atlas = json.loads(probe.guards.ATLAS.read_text())
    chart = {item["basis_index"]: item for item in atlas["c_charts"]}[2]
    guard = [[PRIME - 1], [0], [1]]
    for result in results:
        fiber = result["fiber"]
        require(result["status"] == "COMPLETE" and result["classification"] == "EXCLUDED", "unclosed dynamic fiber")
        form = tuple(result["primitive_form"][name] for name in ("gamma", "alpha", "beta"))
        require(result["candidate_index"] == candidates.index(form) + 1, "candidate index mismatch")
        forms[form] += 1
        matrices = {
            name: matrix_from_entries(entries, fiber)
            for name, entries in regularized_entries.items()
        }
        old = matrix_from_entries(old_entries, fiber)
        require(
            matrix_linear(((1, matrices["x1"]), (2, matrices["x0"]), (3, matrices["b"]))) == old,
            "specialized old-coordinate identity fails",
        )
        for left, right in (("x1", "x0"), ("x1", "b"), ("x0", "b")):
            require(matrix_multiply(matrices[left], matrices[right]) == matrix_multiply(matrices[right], matrices[left]), "coordinate operators do not commute")
        dynamic = matrix_linear(tuple(
            (coefficient, matrices[name])
            for coefficient, name in zip(form, ("x1", "x0", "b"))
            if coefficient
        ))
        vectors = []
        current_vector = unit
        for _ in range(24):
            vectors.append(current_vector)
            current_vector = matrix_vector(dynamic, current_vector)
        krylov = [[vectors[column][row] for column in range(24)] for row in range(24)]
        solutions = solve(
            krylov,
            [matrix_vector(matrices[name], unit) for name in ("x1", "x0", "b")] + [current_vector],
        )
        coordinate_coefficients = dict(zip(("x1", "x0", "b"), solutions[:3]))
        require(coordinate_coefficients == result["coordinate_coefficients"], "coordinate solve mismatch")
        minimal_polynomial = [(-value) % PRIME for value in solutions[3]] + [1]
        require(minimal_polynomial == result["minimal_polynomial"], "minimal polynomial mismatch")
        powers = []
        current_matrix = identity
        for _ in range(24):
            powers.append(current_matrix)
            current_matrix = matrix_multiply(dynamic, current_matrix)
        for name in ("x1", "x0", "b"):
            reconstructed = matrix_linear(tuple(
                (coefficient, powers[degree])
                for degree, coefficient in enumerate(coordinate_coefficients[name])
                if coefficient
            ))
            require(reconstructed == matrices[name], f"full coordinate reconstruction fails for {name}")
        rows = result["rows"]
        factors = [row["finite_factor_polynomial"] for row in rows]
        require(all(factor[-1] == 1 and probe.irreducible(factor) for factor in factors), "dynamic factor is not monic irreducible")
        require(len({tuple(factor) for factor in factors}) == len(factors), "repeated dynamic factor")
        product = (1,)
        for factor in factors:
            product = factorcheck.poly_mul(product, factor)
        require(product == tuple(minimal_polynomial), "dynamic factor product mismatch")
        require([len(value) - 1 for value in factors] == result["factor_degrees"], "factor degree ledger mismatch")
        require(sum(result["factor_degrees"]) == 24, "factor coverage is not 24")
        require(len(rows) == len(factors), "row/factor coverage mismatch")
        total_rows += len(rows)
        for factor_index, (factor, row) in enumerate(zip(factors, rows), start=1):
            require(row["factor"] == factor_index and row["finite_factor"] == 1, "factor indexing mismatch")
            require(row["finite_factor_polynomial"] == factor, "finite factor mismatch")
            require(row["finite_factor_degree"] == len(factor) - 1, "finite factor degree mismatch")
            coordinates = row["coordinates"]
            for name in ("x1", "x0", "b"):
                require(
                    coordinates[name] == probe.guards.reduce_mod(coordinate_coefficients[name], factor),
                    f"factor coordinate mismatch for {name}",
                )
            relation = [0]
            for coefficient, name in zip(form, ("x1", "x0", "b")):
                relation = probe.ef_add(relation, probe.ef_scale(coordinates[name], coefficient, factor), factor)
            require(relation == probe.guards.reduce_mod([0, 1], factor), "dynamic primitive relation fails")
            environment = {"b": coordinates["b"], "t": [fiber]}
            expected_r = probe.ef_negate(
                probe.ef_multiply(
                    probe.guards.expression_mod(atlas["r_chart"]["constant"], environment, factor),
                    probe.guards.inverse_mod(
                        probe.guards.expression_mod(atlas["r_chart"]["leading"], environment, factor),
                        factor,
                    ),
                    factor,
                ),
                factor,
            )
            require(coordinates["r"] == expected_r, "r reconstruction mismatch")
            environment["r"] = expected_r
            expected_c = probe.ef_negate(
                probe.ef_multiply(
                    probe.guards.expression_mod(chart["constant"], environment, factor),
                    probe.guards.inverse_mod(
                        probe.guards.expression_mod(chart["leading"], environment, factor),
                        factor,
                    ),
                    factor,
                ),
                factor,
            )
            require(coordinates["c"] == expected_c, "c reconstruction mismatch")
            require(row["gcd"] in ([[1]], guard), "outside colored gcd")
            gcd_counts["one" if row["gcd"] == [[1]] else "guard"] += 1
            require(row["closure_reason"] == "bezout_guard", "wrong closure reason")
            require(not row["base_roots"] and not row["admissible_roots"], "unexpected root ledger")
            reason_counts[row["closure_reason"]] += 1
    require(total_rows == 804 and reason_counts == {"bezout_guard": 804}, "row census mismatch")
    require(gcd_counts == {"one": 220, "guard": 584}, "gcd census mismatch")
    require(forms == {(1, 2, 1): 33, (1, 3, 1): 5}, "primitive-form census mismatch")
    return results


def verify(regularized_path=REGULARIZED, replay_path=REPLAY):
    regularized_entries, _ = load_regularized(regularized_path)
    old_entries = verify_exact_coordinate_identity(regularized_entries)
    verify_regular_fiber_action(regularized_entries, old_entries)
    return verify_replay(replay_path, regularized_entries, old_entries)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--regularized", type=Path, default=REGULARIZED)
    parser.add_argument("--replay", type=Path, default=REPLAY)
    args = parser.parse_args()
    results = verify(args.regularized, args.replay)
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_DYNAMIC_FIBER_REPLAY_PASS "
        f"fibers={len(results)} rows=804 forms=33,5 gcds=220,584"
    )


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_DYNAMIC_FIBER_REPLAY_FAIL {error}")
        raise SystemExit(1)
