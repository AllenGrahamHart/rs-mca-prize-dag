#!/usr/bin/env python3
"""Replay the 38 map-pole fibers through dynamically primitive coordinates."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
FILES = (
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
REMOTE_DIRECTORY = "/root/cell5_dynamic"
PRIME = 2130706433
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

app = modal.App("rs-mca-positive-433-1a-cell5-dynamic-fiber-replay")
image = modal.Image.debian_slim(python_version="3.12").pip_install("sympy==1.14.0")
for name in dict.fromkeys(FILES):
    image = image.add_local_file(DIRECTORY / name, f"{REMOTE_DIRECTORY}/{name}")


@app.function(image=image, cpu=1.0, memory=2048, timeout=300, max_containers=8)
def replay_batch(fibers):
    import contextlib
    import hashlib
    import importlib
    import io
    import json
    import sys
    import time
    from pathlib import Path

    import sympy as sp

    started = time.monotonic()
    if not fibers or any(fiber not in FIBERS for fiber in fibers):
        raise RuntimeError("fiber outside map-pole route")
    sys.path.insert(0, REMOTE_DIRECTORY)
    probe = importlib.import_module(
        "probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber"
    )
    operator_path = Path(
        REMOTE_DIRECTORY,
        "rate_half_kb_positive_433_1a_cell5_pair_localized_operator_merged_result.json",
    )
    regularized_path = Path(
        REMOTE_DIRECTORY,
        "rate_half_kb_positive_433_1a_cell5_coordinate_operator_regularization_result.json",
    )
    operator = json.loads(operator_path.read_text())
    regularized = json.loads(regularized_path.read_text())
    source_sha256 = {
        name: hashlib.sha256(Path(REMOTE_DIRECTORY, name).read_bytes()).hexdigest()
        for name in dict.fromkeys(FILES)
    }
    if (
        {item["name"] for item in regularized} != {"x1", "x0", "b"}
        or any(item["status"] != "COMPLETE" or item["uncancelled_poles"] for item in regularized)
    ):
        raise RuntimeError("coordinate-operator packet is incomplete")
    coordinate_entries = {
        item["name"]: {
            (entry["row"] - 1, entry["column"] - 1): entry
            for entry in item["entries"]
        }
        for item in regularized
    }
    operator_entries = {
        (entry["row"] - 1, entry["column"] - 1): entry
        for entry in operator["entries"]
        if entry["kind"] == "C"
    }
    expected = {(row, column) for row in range(24) for column in range(24)}
    if set(operator_entries) != expected or any(
        set(entries) != expected for entries in coordinate_entries.values()
    ):
        raise RuntimeError("operator matrix coverage mismatch")

    def evaluate(polynomial, point):
        value = 0
        for coefficient in reversed(polynomial):
            value = (value * point + coefficient) % PRIME
        return value

    def evaluate_matrix(entries, point):
        matrix = [[0] * 24 for _ in range(24)]
        for (row, column), entry in entries.items():
            denominator = evaluate(entry["denominator"], point)
            if denominator == 0:
                raise RuntimeError(f"operator pole at fiber {point}")
            matrix[row][column] = (
                evaluate(entry["numerator"], point) * pow(denominator, -1, PRIME)
            ) % PRIME
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
            if pivot is None:
                return None
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

    def scalar_roots(polynomial):
        if not polynomial or any(len(coefficient) != 1 for coefficient in polynomial):
            raise RuntimeError("nonscalar target gcd")
        e = sp.symbols("e")
        value = sp.Poly(
            sum(coefficient[0] * e**index for index, coefficient in enumerate(polynomial)),
            e,
            modulus=PRIME,
        )
        _, factors = sp.factor_list(value)
        roots = []
        for factor, _multiplicity in factors:
            if factor.degree() == 1:
                roots.append(
                    (-int(factor.nth(0)) * pow(int(factor.nth(1)), -1, PRIME))
                    % PRIME
                )
        return sorted(set(roots))

    def classify(row):
        guard = [[PRIME - 1], [0], [1]]
        if row["gcd"] in ([[1]], guard):
            return "bezout_guard", [], []
        if row["finite_factor_degree"] > 1:
            return "nonbase_primitive", [], []
        roots = scalar_roots(row["gcd"])
        coordinates = row["coordinates"]
        forbidden_squares = {
            1,
            coordinates["b"][0] ** 2 % PRIME,
            coordinates["c"][0] ** 2 % PRIME,
        }
        admissible = [
            root
            for root in roots
            if root != 0 and root * root % PRIME not in forbidden_squares
        ]
        return "survivor" if admissible else "target_collision", roots, admissible

    original_setup = probe.setup
    _, _, atlas, chart, a2_text, a0_text = original_setup(2)
    identity = [[int(row == column) for column in range(24)] for row in range(24)]
    unit = [1] + [0] * 23
    results = []
    for fiber in fibers:
        fiber_started = time.monotonic()
        try:
            matrices = {
                name: evaluate_matrix(entries, fiber)
                for name, entries in coordinate_entries.items()
            }
            old = evaluate_matrix(operator_entries, fiber)
            if matrix_linear(((1, matrices["x1"]), (2, matrices["x0"]), (3, matrices["b"]))) != old:
                raise RuntimeError("regularized coordinate identity mismatch")
            if any(
                matrix_multiply(matrices[left], matrices[right])
                != matrix_multiply(matrices[right], matrices[left])
                for left, right in (("x1", "x0"), ("x1", "b"), ("x0", "b"))
            ):
                raise RuntimeError("coordinate operators do not commute")
            selected = None
            for candidate_index, form in enumerate(primitive_candidates(), start=1):
                dynamic = matrix_linear(tuple(
                    (coefficient, matrices[name])
                    for coefficient, name in zip(form, ("x1", "x0", "b"))
                    if coefficient
                ))
                powers = []
                current = unit
                for _ in range(24):
                    powers.append(current)
                    current = matrix_vector(dynamic, current)
                krylov = [[powers[column][row] for column in range(24)] for row in range(24)]
                right_hand_sides = [
                    matrix_vector(matrices[name], unit) for name in ("x1", "x0", "b")
                ] + [current]
                solutions = solve(krylov, right_hand_sides)
                if solutions is not None:
                    selected = (candidate_index, form, dynamic, solutions)
                    break
            if selected is None:
                raise RuntimeError("no primitive form in deterministic candidate set")
            candidate_index, form, dynamic, solutions = selected
            coordinate_coefficients = dict(zip(("x1", "x0", "b"), solutions[:3]))
            minimal_polynomial = [(-value) % PRIME for value in solutions[3]] + [1]

            powers = []
            current = identity
            for _ in range(24):
                powers.append(current)
                current = matrix_multiply(dynamic, current)
            for name in ("x1", "x0", "b"):
                reconstructed = matrix_linear(tuple(
                    (coefficient, powers[degree])
                    for degree, coefficient in enumerate(coordinate_coefficients[name])
                    if coefficient
                ))
                if reconstructed != matrices[name]:
                    raise RuntimeError(f"dynamic coordinate reconstruction fails for {name}")

            finite_factors = probe.split_specialized_factor(minimal_polynomial)
            if sum(len(value) - 1 for value in finite_factors) != 24:
                raise RuntimeError("dynamic factor degree coverage mismatch")
            dynamic_maps = {
                name: [
                    {"numerator": [value], "denominator": [1]}
                    for value in coordinate_coefficients[name]
                ]
                for name in ("x1", "x0", "b")
            }
            dynamic_factors = [
                [([value], [1]) for value in factor]
                for factor in finite_factors
            ]

            def dynamic_setup(_chart_index):
                return dynamic_maps, dynamic_factors, atlas, chart, a2_text, a0_text

            probe.setup = dynamic_setup
            probe.T = fiber
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                probe.main(chart_index=2)
            replay = json.loads(stream.getvalue())
            if replay["status"] != "COMPLETE" or replay["fiber"] != fiber:
                raise RuntimeError("dynamic replay did not complete")
            rows = []
            for row in replay["rows"]:
                reason, roots, admissible = classify(row)
                rows.append(
                    {
                        **row,
                        "base_roots": roots,
                        "admissible_roots": admissible,
                        "closure_reason": reason,
                    }
                )
            classification = (
                "EXCLUDED"
                if rows and all(row["closure_reason"] != "survivor" for row in rows)
                else "SURVIVOR"
            )
            results.append(
                {
                    "status": "COMPLETE",
                    "fiber": fiber,
                    "chart": 2,
                    "classification": classification,
                    "primitive_form": {
                        "gamma": form[0], "alpha": form[1], "beta": form[2]
                    },
                    "candidate_index": candidate_index,
                    "minimal_polynomial": minimal_polynomial,
                    "factor_degrees": [len(value) - 1 for value in finite_factors],
                    "coordinate_coefficients": coordinate_coefficients,
                    "rows": rows,
                    "elapsed_seconds": round(time.monotonic() - fiber_started, 6),
                }
            )
        except Exception as error:
            results.append(
                {
                    "status": "ERROR",
                    "fiber": fiber,
                    "error": f"{type(error).__name__}: {error}",
                    "elapsed_seconds": round(time.monotonic() - fiber_started, 6),
                }
            )
        finally:
            probe.setup = original_setup
    return {
        "status": "COMPLETE" if all(item["status"] == "COMPLETE" for item in results) else "PARTIAL",
        "source_sha256": source_sha256,
        "results": results,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "scope": (
            "dynamic primitive-coordinate and exact DE+/DE-/BE replay on the "
            "38 map-pole fibers; no basis-pole, other-sign, cell, route, row, "
            "or Prize closure"
        ),
    }


@app.local_entrypoint()
def main(output: str = ""):
    batches = [list(FIBERS[index:index + 5]) for index in range(0, len(FIBERS), 5)]
    shards = []
    for shard in replay_batch.map(batches, order_outputs=False):
        shards.append(shard)
        compact = [
            {
                key: value
                for key, value in result.items()
                if key not in {"rows", "coordinate_coefficients", "minimal_polynomial"}
            }
            for result in shard["results"]
        ]
        print(json.dumps({"status": shard["status"], "results": compact}, sort_keys=True), flush=True)
    results = sorted(
        (result for shard in shards for result in shard["results"]),
        key=lambda item: FIBERS.index(item["fiber"]),
    )
    packet = {
        "schema": "rate-half-kb-positive-433-1a-cell5-dynamic-fiber-replay-v1",
        "status": "COMPLETE" if len(results) == len(FIBERS) and all(item["status"] == "COMPLETE" for item in results) else "PARTIAL",
        "characteristic": PRIME,
        "fibers": list(FIBERS),
        "source_sha256": shards[0]["source_sha256"] if shards else {},
        "results": results,
        "shards": [
            {key: value for key, value in shard.items() if key not in {"results", "source_sha256"}}
            for shard in shards
        ],
        "scope": (
            "dynamic primitive-coordinate and exact DE+/DE-/BE replay on the "
            "38 map-pole fibers; no basis-pole, other-sign, cell, route, row, "
            "or Prize closure"
        ),
    }
    if output:
        Path(output).write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
