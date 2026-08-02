#!/usr/bin/env python3
"""Cancel primitive-map poles in the three coordinate multiplication matrices."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
OPERATOR = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_localized_operator_merged_result.json"
)
MAPS = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json"
)
REMOTE_OPERATOR = "/root/cell5_pair_localized_operator.json"
REMOTE_MAPS = "/root/cell5_pair_primitive_coordinate_maps.json"
PRIME = 2130706433
MAP_POLE_FIBERS = (
    59577338, 60142635, 259897937, 314606277, 350200897, 399214728,
    429335281, 534616264, 658388861, 719443868, 825068466, 898552563,
    967866903, 1108567599, 1112415117, 1156161765, 1157872027,
    1179254816, 1182328414, 1207246658, 1248074151, 1328213402,
    1379619328, 1410757125, 1502791638, 1548270121, 1552698975,
    1593520725, 1594419216, 1618157807, 1618717679, 1777239993,
    1910266670, 1969598264, 2026412590, 2029231698, 2042457704,
    2086242076,
)

app = modal.App("rs-mca-positive-433-1a-cell5-coordinate-operator-regularization")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands("julia -e 'using Pkg; Pkg.add([\"Nemo\"]); Pkg.precompile()'")
    .add_local_file(OPERATOR, REMOTE_OPERATOR)
    .add_local_file(MAPS, REMOTE_MAPS)
)


@app.function(image=image, cpu=2.0, memory=8192, timeout=600, max_containers=3)
def regularize_coordinate(name):
    import hashlib
    import json
    import subprocess
    import tempfile
    import time
    from pathlib import Path

    started = time.monotonic()
    if name not in {"x1", "x0", "b"}:
        raise RuntimeError("unknown coordinate")
    operator_raw = Path(REMOTE_OPERATOR).read_bytes()
    maps_raw = Path(REMOTE_MAPS).read_bytes()
    operator = json.loads(operator_raw)
    maps = {item["name"]: item for item in json.loads(maps_raw)}
    entries = {
        (entry["row"], entry["column"]): entry
        for entry in operator["entries"]
        if entry["kind"] == "C"
    }
    expected = {
        (row, column)
        for row in range(1, 25)
        for column in range(1, 25)
    }
    if set(entries) != expected or set(maps) != {"x1", "x0", "b"}:
        raise RuntimeError("source packet coverage mismatch")
    coefficients = sorted(maps[name]["coordinates"], key=lambda item: item["degree"])
    if [item["degree"] for item in coefficients] != list(range(24)):
        raise RuntimeError("coordinate-map degree coverage mismatch")

    assignments = [
        f"L[{row},{column}]=fraction({entry['numerator']},{entry['denominator']})"
        for (row, column), entry in sorted(entries.items())
    ]
    assignments.extend(
        f"coefficients[{item['degree'] + 1}]=fraction({item['numerator']},{item['denominator']})"
        for item in coefficients
    )
    program = "\n".join(
        (
            "using Nemo",
            "F=GF(2130706433)",
            'T,t=polynomial_ring(F,"t")',
            "K=fraction_field(T)",
            "function fraction(numerator_coefficients,denominator_coefficients)",
            "  numerator=T([F(value) for value in numerator_coefficients])",
            "  denominator=T([F(value) for value in denominator_coefficients])",
            "  return numerator//denominator",
            "end",
            "function coefficient_list(value)",
            '  if iszero(value); return "0"; end',
            '  return join([string(coeff(value,index)) for index in 0:degree(value)],",")',
            "end",
            "L=zero_matrix(K,24,24)",
            "coefficients=[K(0) for _ in 1:24]",
            *assignments,
            "answer=zero_matrix(K,24,24)",
            "power=identity_matrix(K,24)",
            "for index in 1:24",
            "  global answer=answer+coefficients[index]*power",
            "  if index<24; global power=L*power; end",
            "end",
            'open("/tmp/cell5_coordinate_operator.tsv","w") do output',
            "  for row in 1:24, column in 1:24",
            "    value=answer[row,column]",
            '    println(output,row,"\\t",column,"\\t",',
            '      coefficient_list(numerator(value)),"\\t",',
            '      coefficient_list(denominator(value)))',
            "  end",
            "end",
            f'println("COORDINATE_OPERATOR_REGULARIZATION_COMPLETE name={name}")',
        )
    )
    header = {
        "name": name,
        "operator_sha256": hashlib.sha256(operator_raw).hexdigest(),
        "maps_sha256": hashlib.sha256(maps_raw).hexdigest(),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "exact rational multiplication matrix p_u(L) for one coordinate; "
            "tests regularity at all 38 map-pole fibers; no finite-fiber, "
            "colored-edge, route, row, or Prize closure"
        ),
    }
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jl") as handle:
        handle.write(program)
        handle.flush()
        try:
            process = subprocess.run(
                ["julia", "--startup-file=no", handle.name],
                capture_output=True,
                text=True,
                timeout=540,
            )
        except subprocess.TimeoutExpired as error:
            def decoded(value):
                if isinstance(value, bytes):
                    return value.decode("utf-8", errors="replace")
                return value or ""

            return {
                **header,
                "status": "TIMEOUT",
                "elapsed_seconds": round(time.monotonic() - started, 6),
                "stdout": decoded(error.stdout)[-4000:],
                "stderr": decoded(error.stderr)[-4000:],
            }
    marker = f"COORDINATE_OPERATOR_REGULARIZATION_COMPLETE name={name}"
    valid = process.returncode == 0 and marker in process.stdout
    result = {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    if valid:
        records = []
        for line in Path("/tmp/cell5_coordinate_operator.tsv").read_text().splitlines():
            row, column, numerator, denominator = line.split("\t")
            records.append(
                {
                    "row": int(row),
                    "column": int(column),
                    "numerator": [int(value) for value in numerator.split(",")],
                    "denominator": [int(value) for value in denominator.split(",")],
                }
            )
        if {(item["row"], item["column"]) for item in records} != expected:
            raise RuntimeError("output matrix coverage mismatch")

        def evaluate(polynomial, point):
            value = 0
            for coefficient in reversed(polynomial):
                value = (value * point + coefficient) % PRIME
            return value

        poles = sorted(
            fiber
            for fiber in MAP_POLE_FIBERS
            if any(evaluate(item["denominator"], fiber) == 0 for item in records)
        )
        result["entries"] = records
        result["map_pole_fibers"] = list(MAP_POLE_FIBERS)
        result["uncancelled_poles"] = poles
        result["maximum_numerator_degree"] = max(
            len(item["numerator"]) - 1 for item in records
        )
        result["maximum_denominator_degree"] = max(
            len(item["denominator"]) - 1 for item in records
        )
    return result


@app.local_entrypoint()
def main(output: str = ""):
    results = []
    for result in regularize_coordinate.map(
        ("x1", "x0", "b"), order_outputs=False
    ):
        results.append(result)
        compact = {key: value for key, value in result.items() if key != "entries"}
        print(json.dumps(compact, sort_keys=True), flush=True)
    results.sort(key=lambda item: ("x1", "x0", "b").index(item["name"]))
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
