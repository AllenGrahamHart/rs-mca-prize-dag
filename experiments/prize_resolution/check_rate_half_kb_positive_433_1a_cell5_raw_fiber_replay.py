#!/usr/bin/env python3
"""Check the direct profiles and colored replays at the final eight fibers."""

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import check_rate_half_kb_positive_433_1a_cell5_pair_generic_guard_units as guards
import check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization as factorcheck
import probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber as probe
from rate_half_kb_positive_433_1a_cell5_sparse_edge_probe import sparse_product_kernel


PRIME = 2130706433
IOTA = 16711679
PROFILE = HERE / "rate_half_kb_positive_433_1a_cell5_raw_fiber_profile_result.json"
REPLAY = HERE / "rate_half_kb_positive_433_1a_cell5_raw_fiber_replay_result.json"
EXPECTED_PROFILE_SHA256 = (
    "7297479e0f5a6bce3b692f1e165470a21cc2dcc853fa6c4898fa19d6059943aa"
)
EXPECTED_REPLAY_SHA256 = (
    "50b235b26c5734fcb9d7775d4566a5e008d018e6c31b9acd5b9d9b209cac4710"
)
FIBERS = (
    16711680, 16903576, 100334506, 1332924776,
    1474082935, 1665662739, 1729517783, 1783507114,
)
EXPECTED_DIMENSIONS = {
    16711680: 24,
    16903576: 24,
    100334506: 24,
    1332924776: 23,
    1474082935: 24,
    1665662739: 24,
    1729517783: 24,
    1783507114: 24,
}
EXPECTED_PROFILE_PROGRAMS = {
    16711680: "6d91e13ae0200faa25ef967434dd43b9e77737c4f50530781b0c63368ff4e548",
    16903576: "9655944a48a8a2997c877073eca7cd46b96211c23e2c9de5ddd019549368ca11",
    100334506: "108f49bbb404e800f9f25fbd2caa34088db3807d2c037ed43de0b0ef8dc92124",
    1332924776: "8a72032b37e1a40bf25475c5f706152c3c2d3e8e85eccb9addd9747327a649b3",
    1474082935: "9b6593bf9a67abdec709ab32fb00db899722dc20bad00025321c868783fbfb73",
    1665662739: "8b936484fb670b6d42a91acb26e0344fde4efd50856c234f59e8c99be523969c",
    1729517783: "ac3d5ebb4fbef0c5ce332155bd0be2adb5ad0159392dd6e90d994925dcdb5ceb",
    1783507114: "ff73e7288312a4e53bf17f0b1674383d4fadf2b197a546745d3387a41f816ed4",
}
EXPECTED_REPLAY_PROGRAMS = {
    16711680: "d103ba54e3c45baae6aa044bf62db783dd11b9bf9b3d738af59cefdc4140bcfa",
    16903576: "f3885f29b56bb60943ea62e6baca55d4229a46a906a029a092f3f6055b277475",
    100334506: "553caf8fb0b1bb51d21f18f06911c189dcd4a4c6eaab01fc6ec85674eab31755",
    1332924776: "e3deed6e17adafd8a461c28f45b89264ed09e8d0cb6b43f90290a12330aafd36",
    1474082935: "c202b3c96fabe57bfb24c57f221a7e6bbbc69cf080703fb03f270094faf86158",
    1665662739: "8fcef15ba2d825d554aa4ce06256e83123fe7d685bc3dded4944b42b4adfe085",
    1729517783: "6ab132d3d717cdb03b01a7757b590882c7b2c13af50bdd3b79675147014ff3d1",
    1783507114: "141f503ba1f6ce69fe6c436b5118a2bc3853913d2ab8f231d60bb78a6f0a947e",
}
SOURCE_FILES = (
    "rate_half_kb_positive_433_1a_cell5_raw_fiber_profile_result.json",
    "probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_generic_guard_units.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_localized_operator.py",
    "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py",
    "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json",
)


class CertificateError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def matrix_zero(size):
    return [[0] * size for _ in range(size)]


def matrix_identity(size):
    return [[int(row == column) for column in range(size)] for row in range(size)]


def matrix_add(*matrices):
    size = len(matrices[0])
    return [
        [sum(matrix[row][column] for matrix in matrices) % PRIME for column in range(size)]
        for row in range(size)
    ]


def matrix_scale(matrix, scalar):
    return [[scalar * value % PRIME for value in row] for row in matrix]


def matrix_subtract(left, right):
    return matrix_add(left, matrix_scale(right, -1))


def matrix_multiply(left, right):
    columns = list(zip(*right))
    return [
        [sum(a * b for a, b in zip(row, column)) % PRIME for column in columns]
        for row in left
    ]


def matrix_power(matrix, exponent):
    result = matrix_identity(len(matrix))
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, matrix)
        matrix = matrix_multiply(matrix, matrix)
        exponent >>= 1
    return result


def matrix_vector(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) % PRIME for row in matrix]


def matrix_polynomial(coefficients, matrix):
    size = len(matrix)
    result = matrix_zero(size)
    identity = matrix_identity(size)
    for coefficient in reversed(coefficients):
        result = matrix_add(matrix_multiply(result, matrix), matrix_scale(identity, coefficient))
    return result


def matrix_rank(matrix):
    value = [row[:] for row in matrix]
    rows, columns = len(value), len(value[0])
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank, rows) if value[row][column]), None)
        if pivot is None:
            continue
        value[rank], value[pivot] = value[pivot], value[rank]
        inverse = pow(value[rank][column], -1, PRIME)
        value[rank] = [item * inverse % PRIME for item in value[rank]]
        for row in range(rows):
            if row == rank or value[row][column] == 0:
                continue
            scale = value[row][column]
            value[row] = [(left - scale * right) % PRIME for left, right in zip(value[row], value[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def solve(matrix, right_hand_sides):
    size = len(matrix)
    width = len(right_hand_sides)
    augmented = [
        list(matrix[row]) + [right_hand_sides[index][row] for index in range(width)]
        for row in range(size)
    ]
    for column in range(size):
        pivot = next((row for row in range(column, size) if augmented[row][column]), None)
        require(pivot is not None, "singular claimed raw Krylov matrix")
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
            if value not in output:
                output.append(value)
    return output


def reconstruct_profile(fiber, atlas):
    a0 = (
        pow(fiber, 4, PRIME) - 2 * IOTA * pow(fiber, 3, PRIME)
        - 4 * IOTA * fiber * fiber - 2 * IOTA * fiber - 1
    ) % PRIME
    a1 = (-8 * IOTA * (pow(fiber, 4, PRIME) + 1)) % PRIME
    a2 = (
        -2 * pow(fiber, 4, PRIME) + 4 * IOTA * pow(fiber, 3, PRIME)
        - 24 * IOTA * fiber * fiber + 4 * IOTA * fiber + 2
    ) % PRIME
    primitive = [a0, a1, a2, a1, a0]
    inverse = pow(primitive[-1], -1, PRIME)
    primitive = guards.trim([inverse * value for value in primitive])
    environment = {"b": [0, 1], "t": [fiber]}
    r_leading = guards.expression_mod(atlas["r_chart"]["leading"], environment, primitive)
    r_constant = guards.expression_mod(atlas["r_chart"]["constant"], environment, primitive)
    r = guards.negate(guards.multiply_mod(r_constant, guards.inverse_mod(r_leading, primitive), primitive))
    environment["r"] = r
    chart = {item["basis_index"]: item for item in atlas["c_charts"]}[2]
    c_leading = guards.expression_mod(chart["leading"], environment, primitive)
    c_constant = guards.expression_mod(chart["constant"], environment, primitive)
    c = guards.negate(guards.multiply_mod(c_constant, guards.inverse_mod(c_leading, primitive), primitive))
    environment["c"] = c
    a2_source, a0_source, _, _, _ = sparse_product_kernel()
    d_coefficients = [guards.expression_mod(str(value), environment, primitive) for value in a2_source]
    n_coefficients = [guards.expression_mod(str(value), environment, primitive) for value in a0_source]
    return primitive, r, c, d_coefficients, n_coefficients


def load_profiles(path):
    raw = path.read_bytes()
    if path == PROFILE:
        require(hashlib.sha256(raw).hexdigest() == EXPECTED_PROFILE_SHA256, "profile hash mismatch")
    payload = json.loads(raw)
    require(isinstance(payload, list) and [item["fiber"] for item in payload] == list(FIBERS), "profile coverage mismatch")
    atlas_raw = guards.ATLAS.read_bytes()
    atlas = json.loads(atlas_raw)
    profiles = {}
    for item in payload:
        fiber = item["fiber"]
        require(item["status"] == "COMPLETE" and item["returncode"] == 0, "profile incomplete")
        require(item["chart"] == 2 and item["quotient_dimension"] == EXPECTED_DIMENSIONS[fiber], "profile dimension mismatch")
        require(item["program_sha256"] == EXPECTED_PROFILE_PROGRAMS[fiber], "profile program mismatch")
        require(item["atlas_sha256"] == hashlib.sha256(atlas_raw).hexdigest(), "profile atlas mismatch")
        expected = reconstruct_profile(fiber, atlas)
        require(tuple(expected) == tuple(item[name] for name in ("primitive", "r", "c", "d_coefficients", "n_coefficients")), "profile coefficient reconstruction mismatch")
        require(hashlib.sha256("\n".join(item["basis_lines"]).encode()).hexdigest() == item["basis_sha256"], "basis hash mismatch")
        require(hashlib.sha256("\n".join(item["quotient_basis_lines"]).encode()).hexdigest() == item["quotient_basis_sha256"], "quotient basis hash mismatch")
        require(len(item["quotient_basis_lines"]) == item["quotient_dimension"] and item["quotient_basis_lines"].count("1") == 1, "quotient basis ledger mismatch")
        profiles[fiber] = item
    return profiles, raw


def verify_defining_relations(result, profile):
    dimension = result["dimension"]
    matrices = result["matrices"]
    require(set(matrices) == {"x1", "x0", "b"}, "raw matrix names mismatch")
    require(all(len(matrix) == dimension and all(len(row) == dimension for row in matrix) for matrix in matrices.values()), "raw matrix shape mismatch")
    require(all(isinstance(value, int) and 0 <= value < PRIME for matrix in matrices.values() for row in matrix for value in row), "raw matrix coefficient mismatch")
    x1, x0, b = matrices["x1"], matrices["x0"], matrices["b"]
    for left, right in ((x1, x0), (x1, b), (x0, b)):
        require(matrix_multiply(left, right) == matrix_multiply(right, left), "raw matrices do not commute")
    zero = matrix_zero(dimension)
    identity = matrix_identity(dimension)
    require(matrix_polynomial(profile["primitive"], b) == zero, "primitive relation fails")
    d = [matrix_polynomial(value, b) for value in profile["d_coefficients"]]
    n = [matrix_polynomial(value, b) for value in profile["n_coefficients"]]
    x0_squared = matrix_multiply(x0, x0)
    x1_squared = matrix_multiply(x1, x1)
    D0 = matrix_add(d[0], matrix_multiply(d[1], x0), matrix_multiply(d[2], x0_squared))
    D1 = matrix_add(d[0], matrix_multiply(d[1], x1), matrix_multiply(d[2], x1_squared))
    N0 = matrix_add(n[0], matrix_multiply(n[1], x0), matrix_multiply(n[2], x0_squared))
    N1 = matrix_add(n[0], matrix_multiply(n[1], x1), matrix_multiply(n[2], x1_squared))
    fiber = result["fiber"]
    beta_core = matrix_add(d[0], matrix_scale(d[1], fiber * fiber), matrix_scale(d[2], pow(fiber, 4, PRIME)))
    beta = matrix_scale(matrix_multiply(matrix_add(identity, b), beta_core), -fiber)
    beta_squared = matrix_multiply(beta, beta)
    Q0 = matrix_multiply(matrix_multiply(x0, beta_squared), matrix_power(matrix_subtract(x0, identity), 2))
    Q1 = matrix_multiply(matrix_multiply(x1, beta_squared), matrix_power(matrix_subtract(x1, identity), 2))
    g3 = matrix_add(matrix_multiply(N1, D0), matrix_multiply(N0, D1))
    delta = fiber * fiber % PRIME * ((fiber * fiber - 1) % PRIME) % PRIME
    h = matrix_add(
        matrix_multiply(Q1, matrix_power(D0, 2)),
        matrix_scale(matrix_multiply(Q0, matrix_power(D1, 2)), -1),
        matrix_scale(matrix_multiply(matrix_multiply(N0, D0), matrix_power(D1, 2)), 4 * delta * delta),
    )
    require(g3 == zero and h == zero, "raw signed-pair relation fails")
    guard_matrix = matrix_multiply(D0, D1)
    require(matrix_rank(guard_matrix) == dimension, "D0*D1 localization fails")
    return matrices


def verify_replay(path, profiles, profile_raw):
    raw = path.read_bytes()
    if path == REPLAY:
        require(hashlib.sha256(raw).hexdigest() == EXPECTED_REPLAY_SHA256, "raw replay hash mismatch")
    payload = json.loads(raw)
    require(payload["schema"].endswith("raw-fiber-replay-v1"), "raw replay schema mismatch")
    require(payload["status"] == "COMPLETE" and payload["characteristic"] == PRIME, "raw replay incomplete")
    require(payload["fibers"] == list(FIBERS), "raw replay route mismatch")
    results = payload["results"]
    require([item["fiber"] for item in results] == list(FIBERS), "raw replay coverage mismatch")
    expected_sources = {name: hashlib.sha256((HERE / name).read_bytes()).hexdigest() for name in SOURCE_FILES}
    candidates = primitive_candidates()
    gcd_counts = Counter()
    total_rows = 0
    atlas = json.loads(guards.ATLAS.read_text())
    chart = {item["basis_index"]: item for item in atlas["c_charts"]}[2]
    guard = [[PRIME - 1], [0], [1]]
    for result in results:
        fiber = result["fiber"]
        profile = profiles[fiber]
        dimension = EXPECTED_DIMENSIONS[fiber]
        require(result["status"] == "COMPLETE" and result["classification"] == "EXCLUDED", "raw fiber not excluded")
        require(result["dimension"] == dimension, "raw replay dimension mismatch")
        require(result["profile_sha256"] == hashlib.sha256(profile_raw).hexdigest(), "raw profile provenance mismatch")
        require(result["program_sha256"] == EXPECTED_REPLAY_PROGRAMS[fiber], "raw replay program mismatch")
        require(result["source_sha256"] == expected_sources, "raw replay source mismatch")
        matrices = verify_defining_relations(result, profile)
        form = tuple(result["primitive_form"][name] for name in ("gamma", "alpha", "beta"))
        require(form == (1, 2, 1) and result["candidate_index"] == candidates.index(form) + 1, "raw primitive form mismatch")
        dynamic = matrix_add(matrices["x1"], matrix_scale(matrices["x0"], 2), matrices["b"])
        unit_index = profile["quotient_basis_lines"].index("1")
        unit = [int(index == unit_index) for index in range(dimension)]
        vectors = []
        current_vector = unit
        for _ in range(dimension):
            vectors.append(current_vector)
            current_vector = matrix_vector(dynamic, current_vector)
        krylov = [[vectors[column][row] for column in range(dimension)] for row in range(dimension)]
        solutions = solve(
            krylov,
            [matrix_vector(matrices[name], unit) for name in ("x1", "x0", "b")] + [current_vector],
        )
        coordinates = dict(zip(("x1", "x0", "b"), solutions[:3]))
        require(coordinates == result["coordinate_coefficients"], "raw coordinate solve mismatch")
        minimal = [(-value) % PRIME for value in solutions[3]] + [1]
        require(minimal == result["minimal_polynomial"], "raw minimal polynomial mismatch")
        powers = []
        current_matrix = matrix_identity(dimension)
        for _ in range(dimension):
            powers.append(current_matrix)
            current_matrix = matrix_multiply(dynamic, current_matrix)
        for name in ("x1", "x0", "b"):
            reconstructed = matrix_zero(dimension)
            for degree, coefficient in enumerate(coordinates[name]):
                reconstructed = matrix_add(reconstructed, matrix_scale(powers[degree], coefficient))
            require(reconstructed == matrices[name], f"raw full coordinate reconstruction fails for {name}")
        rows = result["rows"]
        factors = [row["finite_factor_polynomial"] for row in rows]
        require(all(factor[-1] == 1 and probe.irreducible(factor) for factor in factors), "raw factor is not monic irreducible")
        require(len({tuple(factor) for factor in factors}) == len(factors), "raw repeated factor")
        product = (1,)
        for factor in factors:
            product = factorcheck.poly_mul(product, factor)
        require(product == tuple(minimal), "raw factor product mismatch")
        require([len(factor) - 1 for factor in factors] == result["factor_degrees"] and sum(result["factor_degrees"]) == dimension, "raw factor degree coverage mismatch")
        total_rows += len(rows)
        for factor_index, (factor, row) in enumerate(zip(factors, rows), start=1):
            require(row["factor"] == factor_index and row["finite_factor"] == 1, "raw factor indexing mismatch")
            row_coordinates = row["coordinates"]
            for name in ("x1", "x0", "b"):
                require(row_coordinates[name] == guards.reduce_mod(coordinates[name], factor), f"raw factor coordinate mismatch for {name}")
            relation = probe.ef_add(row_coordinates["x1"], probe.ef_add(probe.ef_scale(row_coordinates["x0"], 2, factor), row_coordinates["b"], factor), factor)
            require(relation == guards.reduce_mod([0, 1], factor), "raw primitive relation mismatch")
            environment = {"b": row_coordinates["b"], "t": [fiber]}
            expected_r = probe.ef_negate(
                probe.ef_multiply(
                    guards.expression_mod(atlas["r_chart"]["constant"], environment, factor),
                    guards.inverse_mod(guards.expression_mod(atlas["r_chart"]["leading"], environment, factor), factor),
                    factor,
                ),
                factor,
            )
            require(row_coordinates["r"] == expected_r, "raw r reconstruction mismatch")
            environment["r"] = expected_r
            expected_c = probe.ef_negate(
                probe.ef_multiply(
                    guards.expression_mod(chart["constant"], environment, factor),
                    guards.inverse_mod(guards.expression_mod(chart["leading"], environment, factor), factor),
                    factor,
                ),
                factor,
            )
            require(row_coordinates["c"] == expected_c, "raw c reconstruction mismatch")
            require(row["gcd_class"] in {"one", "e2_minus_1"}, "raw outside gcd")
            require(row["gcd"] == ([[1]] if row["gcd_class"] == "one" else guard), "raw gcd class mismatch")
            gcd_counts[row["gcd_class"]] += 1
    require(total_rows == 115 and gcd_counts == {"one": 35, "e2_minus_1": 80}, "raw gcd census mismatch")
    return results


def verify(profile_path=PROFILE, replay_path=REPLAY):
    profiles, profile_raw = load_profiles(profile_path)
    return verify_replay(replay_path, profiles, profile_raw)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=Path, default=PROFILE)
    parser.add_argument("--replay", type=Path, default=REPLAY)
    args = parser.parse_args()
    results = verify(args.profile, args.replay)
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_RAW_FIBER_REPLAY_PASS "
        f"fibers={len(results)} dimensions=24,24,24,23,24,24,24,24 "
        "rows=115 gcds=35,80"
    )


if __name__ == "__main__":
    try:
        main()
    except (CertificateError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"RATE_HALF_KB_POSITIVE_433_1A_CELL5_RAW_FIBER_REPLAY_FAIL {error}")
        raise SystemExit(1)
