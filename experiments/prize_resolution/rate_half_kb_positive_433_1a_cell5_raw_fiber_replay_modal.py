#!/usr/bin/env python3
"""Build raw multiplication matrices and replay the final eight cell-5 fibers."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
FILES = (
    "rate_half_kb_positive_433_1a_cell5_raw_fiber_profile_result.json",
    "probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_generic_guard_units.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_localized_operator.py",
    "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py",
    "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json",
)
REMOTE_DIRECTORY = "/root/cell5_raw_replay"
PRIME = 2130706433
FIBERS = (
    16711680, 16903576, 100334506, 1332924776,
    1474082935, 1665662739, 1729517783, 1783507114,
)

app = modal.App("rs-mca-positive-433-1a-cell5-raw-fiber-replay")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .pip_install("sympy==1.14.0")
    .run_commands(
        "julia -e 'using Pkg; "
        'Pkg.add(["AbstractAlgebra", "Groebner"]); Pkg.precompile()\''
    )
)
for name in FILES:
    image = image.add_local_file(DIRECTORY / name, f"{REMOTE_DIRECTORY}/{name}")


@app.function(image=image, cpu=1.0, memory=4096, timeout=300, max_containers=8)
def replay(fiber):
    import contextlib
    import hashlib
    import importlib
    import io
    import json
    import subprocess
    import sys
    import tempfile
    import time
    from pathlib import Path

    import sympy as sp

    started = time.monotonic()
    if fiber not in FIBERS:
        raise RuntimeError("fiber outside raw-basis route")
    sys.path.insert(0, REMOTE_DIRECTORY)
    probe = importlib.import_module(
        "probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber"
    )
    sparse = importlib.import_module(
        "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe"
    )
    profile_path = Path(
        REMOTE_DIRECTORY,
        "rate_half_kb_positive_433_1a_cell5_raw_fiber_profile_result.json",
    )
    profile_raw = profile_path.read_bytes()
    profiles = {item["fiber"]: item for item in json.loads(profile_raw)}
    record = profiles[fiber]
    if record["status"] != "COMPLETE" or record["quotient_dimension"] not in {23, 24}:
        raise RuntimeError("raw profile is incomplete")
    dimension = record["quotient_dimension"]
    basis_literal = ",\n".join(record["basis_lines"])
    program = "\n".join(
        (
            "using AbstractAlgebra, Groebner, SHA",
            f"F=GF({PRIME})",
            'R,(x1,x0,B,u)=polynomial_ring(F,["x1","x0","b","u"],internal_ordering=:degrevlex)',
            "b=B",
            f"basis=[{basis_literal}]",
            "@assert isgroebner(basis;ordering=DegRevLex())",
            "quotient_basis=Groebner.quotient_basis(basis;ordering=DegRevLex())",
            f"@assert length(quotient_basis)=={dimension}",
            "basis_index=Dict{Tuple{Vararg{Int}},Int}()",
            "for (index,value) in enumerate(quotient_basis)",
            "  basis_index[Tuple(exponent_vector(value,1))]=index",
            "end",
            "variables=[x1,x0,B]",
            'names=["x1","x0","b"]',
            'open("/tmp/cell5_raw_matrices.tsv","w") do output',
            "  for (name,variable) in zip(names,variables)",
            "    products=normalform(basis,[variable*value for value in quotient_basis];ordering=DegRevLex())",
            "    for column in 1:length(quotient_basis)",
            "      value=products[column]",
            "      for term_index in 1:length(value)",
            "        row=basis_index[Tuple(exponent_vector(value,term_index))]",
            '        println(output,name,"\\t",row,"\\t",column,"\\t",coeff(value,term_index))',
            "      end",
            "    end",
            "  end",
            "end",
            'open("/tmp/cell5_raw_quotient.txt","w") do output',
            "  for value in quotient_basis; println(output,value); end",
            "end",
            f'println("RAW_FIBER_MATRICES_COMPLETE dimension={dimension}")',
        )
    )
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jl") as handle:
        handle.write(program)
        handle.flush()
        try:
            process = subprocess.run(
                ["julia", "--startup-file=no", handle.name],
                capture_output=True,
                text=True,
                timeout=240,
            )
        except subprocess.TimeoutExpired as error:
            return {
                "status": "TIMEOUT",
                "fiber": fiber,
                "elapsed_seconds": round(time.monotonic() - started, 6),
                "stdout": (error.stdout or "")[-4000:],
                "stderr": (error.stderr or "")[-4000:],
            }
    marker = f"RAW_FIBER_MATRICES_COMPLETE dimension={dimension}"
    if process.returncode != 0 or marker not in process.stdout:
        return {
            "status": "ERROR",
            "fiber": fiber,
            "returncode": process.returncode,
            "elapsed_seconds": round(time.monotonic() - started, 6),
            "stdout": process.stdout[-4000:],
            "stderr": process.stderr[-4000:],
        }
    quotient_lines = Path("/tmp/cell5_raw_quotient.txt").read_text().splitlines()
    if quotient_lines != record["quotient_basis_lines"]:
        raise RuntimeError("imported quotient basis changed")
    matrices = {
        name: [[0] * dimension for _ in range(dimension)]
        for name in ("x1", "x0", "b")
    }
    seen = set()
    for line in Path("/tmp/cell5_raw_matrices.tsv").read_text().splitlines():
        name, row, column, value = line.split("\t")
        key = (name, int(row) - 1, int(column) - 1)
        if key in seen:
            raise RuntimeError("duplicate multiplication entry")
        seen.add(key)
        matrices[name][key[1]][key[2]] = int(value) % PRIME

    def matrix_linear(terms):
        return [
            [sum(scalar * matrix[row][column] for scalar, matrix in terms) % PRIME for column in range(dimension)]
            for row in range(dimension)
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
                if value not in output:
                    output.append(value)
        return output

    if any(
        matrix_multiply(matrices[left], matrices[right])
        != matrix_multiply(matrices[right], matrices[left])
        for left, right in (("x1", "x0"), ("x1", "b"), ("x0", "b"))
    ):
        raise RuntimeError("raw coordinate matrices do not commute")
    unit_index = quotient_lines.index("1")
    unit = [int(index == unit_index) for index in range(dimension)]
    selected = None
    for candidate_index, form in enumerate(primitive_candidates(), start=1):
        dynamic = matrix_linear(tuple(
            (coefficient, matrices[name])
            for coefficient, name in zip(form, ("x1", "x0", "b"))
            if coefficient
        ))
        powers = []
        current = unit
        for _ in range(dimension):
            powers.append(current)
            current = matrix_vector(dynamic, current)
        krylov = [
            [powers[column][row] for column in range(dimension)]
            for row in range(dimension)
        ]
        right_hand_sides = [
            matrix_vector(matrices[name], unit) for name in ("x1", "x0", "b")
        ] + [current]
        solutions = solve(krylov, right_hand_sides)
        if solutions is not None:
            selected = (candidate_index, form, dynamic, solutions)
            break
    if selected is None:
        return {
            "status": "NONMONOGENIC",
            "fiber": fiber,
            "dimension": dimension,
            "elapsed_seconds": round(time.monotonic() - started, 6),
        }
    candidate_index, form, dynamic, solutions = selected
    coordinate_coefficients = dict(zip(("x1", "x0", "b"), solutions[:3]))
    minimal_polynomial = [(-value) % PRIME for value in solutions[3]] + [1]
    identity = [
        [int(row == column) for column in range(dimension)]
        for row in range(dimension)
    ]
    powers = []
    current = identity
    for _ in range(dimension):
        powers.append(current)
        current = matrix_multiply(dynamic, current)
    for name in ("x1", "x0", "b"):
        reconstructed = matrix_linear(tuple(
            (coefficient, powers[degree])
            for degree, coefficient in enumerate(coordinate_coefficients[name])
            if coefficient
        ))
        if reconstructed != matrices[name]:
            raise RuntimeError(f"raw coordinate reconstruction fails for {name}")
    try:
        finite_factors = probe.split_specialized_factor(minimal_polynomial)
    except RuntimeError as error:
        return {
            "status": "NONREDUCED",
            "fiber": fiber,
            "dimension": dimension,
            "primitive_form": {"gamma": form[0], "alpha": form[1], "beta": form[2]},
            "minimal_polynomial": minimal_polynomial,
            "error": str(error),
            "elapsed_seconds": round(time.monotonic() - started, 6),
        }
    if sum(len(value) - 1 for value in finite_factors) != dimension:
        raise RuntimeError("raw factor degree coverage mismatch")
    atlas = json.loads(Path(REMOTE_DIRECTORY, "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json").read_text())
    chart = {item["basis_index"]: item for item in atlas["c_charts"]}[2]
    a2_source, a0_source, _, _, _ = sparse.sparse_product_kernel()
    dynamic_maps = {
        name: [{"numerator": [value], "denominator": [1]} for value in coordinate_coefficients[name]]
        for name in ("x1", "x0", "b")
    }
    dynamic_factors = [[([value], [1]) for value in factor] for factor in finite_factors]

    def dynamic_setup(_chart_index):
        return dynamic_maps, dynamic_factors, atlas, chart, [str(value) for value in a2_source], [str(value) for value in a0_source]

    original_setup = probe.setup
    probe.setup = dynamic_setup
    probe.T = fiber
    stream = io.StringIO()
    try:
        with contextlib.redirect_stdout(stream):
            probe.main(chart_index=2)
    finally:
        probe.setup = original_setup
    result = json.loads(stream.getvalue())
    if result["status"] != "COMPLETE" or result["fiber"] != fiber:
        raise RuntimeError("raw colored replay did not complete")
    guard = [[PRIME - 1], [0], [1]]
    rows = []
    for row in result["rows"]:
        gcd_class = "one" if row["gcd"] == [[1]] else "e2_minus_1" if row["gcd"] == guard else "outside"
        rows.append({**row, "gcd_class": gcd_class})
    classification = "EXCLUDED" if rows and all(row["gcd_class"] != "outside" for row in rows) else "SURVIVOR"
    source_sha256 = {
        name: hashlib.sha256(Path(REMOTE_DIRECTORY, name).read_bytes()).hexdigest()
        for name in FILES
    }
    return {
        "status": "COMPLETE",
        "fiber": fiber,
        "dimension": dimension,
        "classification": classification,
        "primitive_form": {"gamma": form[0], "alpha": form[1], "beta": form[2]},
        "candidate_index": candidate_index,
        "minimal_polynomial": minimal_polynomial,
        "factor_degrees": [len(value) - 1 for value in finite_factors],
        "coordinate_coefficients": coordinate_coefficients,
        "matrices": matrices,
        "rows": rows,
        "profile_sha256": hashlib.sha256(profile_raw).hexdigest(),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "source_sha256": source_sha256,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "scope": (
            "direct raw-basis multiplication, dynamic primitive coordinate, "
            "and exact DE+/DE-/BE replay at one final fiber; no other sign, "
            "cell, route, row, or Prize closure"
        ),
    }


@app.local_entrypoint()
def main(output: str = ""):
    results = []
    for fiber in FIBERS:
        result = replay.remote(fiber)
        results.append(result)
        compact = {
            key: value
            for key, value in result.items()
            if key not in {"rows", "matrices", "coordinate_coefficients", "minimal_polynomial", "source_sha256"}
        }
        if "rows" in result:
            compact["row_count"] = len(result["rows"])
        print(json.dumps(compact, sort_keys=True), flush=True)
    results.sort(key=lambda item: FIBERS.index(item["fiber"]))
    packet = {
        "schema": "rate-half-kb-positive-433-1a-cell5-raw-fiber-replay-v1",
        "status": "COMPLETE" if len(results) == len(FIBERS) and all(item["status"] == "COMPLETE" for item in results) else "PARTIAL",
        "characteristic": PRIME,
        "fibers": list(FIBERS),
        "results": results,
        "scope": (
            "direct raw-basis multiplication, dynamic primitive coordinates, "
            "and exact DE+/DE-/BE replay at the final eight fibers; no other "
            "sign, cell, route, row, or Prize closure"
        ),
    }
    if output:
        Path(output).write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
