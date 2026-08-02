#!/usr/bin/env python3
"""Express b, x0, and x1 in the localized pair primitive coordinate."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
OPERATOR = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_localized_operator_merged_result.json"
)
COLUMNS = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_coordinate_columns_result.json"
)
REMOTE_OPERATOR = "/root/cell5_pair_localized_operator.json"
REMOTE_COLUMNS = "/root/cell5_pair_coordinate_columns.json"

app = modal.App("rs-mca-positive-433-1a-cell5-pair-primitive-coordinate-map")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; "
        "Pkg.add([\"AbstractAlgebra\", \"Nemo\"]); Pkg.precompile()'"
    )
    .add_local_file(OPERATOR, REMOTE_OPERATOR)
    .add_local_file(COLUMNS, REMOTE_COLUMNS)
)


@app.function(image=image, cpu=1.0, memory=8192, timeout=300)
def compute_map(name):
    import hashlib
    import json
    import subprocess
    import tempfile

    operator_raw = Path(REMOTE_OPERATOR).read_bytes()
    operator = json.loads(operator_raw)
    columns_raw = Path(REMOTE_COLUMNS).read_bytes()
    columns = json.loads(columns_raw)
    operator_entries = {
        (entry["row"], entry["column"]): entry
        for entry in operator["entries"]
        if entry["kind"] == "C"
    }
    if set(operator_entries) != {
        (row, column)
        for row in range(1, 25)
        for column in range(1, 25)
    }:
        raise RuntimeError("primitive operator coverage mismatch")
    forms = {
        (1, 0, 0): "x1",
        (0, 1, 0): "x0",
        (0, 0, 1): "b",
    }
    right_hand_sides = {}
    for shard in columns:
        key = (shard["gamma"], shard["alpha"], shard["beta"])
        if key not in forms or shard["status"] != "COMPLETE" or shard["returncode"] != 0:
            raise RuntimeError("coordinate-column shard mismatch")
        entries = {
            entry["row"]: entry
            for entry in shard["entries"]
            if entry["kind"] == "C" and entry["column"] == 1
        }
        if set(entries) != set(range(1, 25)):
            raise RuntimeError("coordinate-column coverage mismatch")
        right_hand_sides[forms[key]] = entries
    if set(right_hand_sides) != {"x1", "x0", "b"}:
        raise RuntimeError("coordinate form coverage mismatch")
    if name not in right_hand_sides:
        raise RuntimeError("unknown coordinate name")

    assignments = [
        f"L[{row},{column}]=make_fraction({entry['numerator']},{entry['denominator']})"
        for (row, column), entry in sorted(operator_entries.items())
    ]
    for row, entry in sorted(right_hand_sides[name].items()):
        assignments.append(
            f"rhs[{row},1]=make_fraction("
            f"{entry['numerator']},{entry['denominator']})"
        )
    program = "\n".join(
        (
            (
                'NemoModule=Base.require(Base.PkgId(Base.UUID('
                '"2edaba10-b0f1-5616-af89-8c11ac63239a"),"Nemo"))'
            ),
            (
                'AAModule=Base.require(Base.PkgId(Base.UUID('
                '"c3fe647b-3220-5bb0-a1ea-a7954cac585d"),'
                '"AbstractAlgebra"))'
            ),
            "F=NemoModule.GF(2130706433)",
            'T,t=NemoModule.polynomial_ring(F,"t")',
            "K=NemoModule.fraction_field(T)",
            "function make_fraction(numeratorCoefficients,denominatorCoefficients)",
            "  numerator=T([F(value) for value in numeratorCoefficients])",
            "  denominator=T([F(value) for value in denominatorCoefficients])",
            "  return numerator//denominator",
            "end",
            "L=NemoModule.zero_matrix(K,24,24)",
            "rhs=NemoModule.zero_matrix(K,24,1)",
            *assignments,
            "krylov=NemoModule.zero_matrix(K,24,24)",
            "current=NemoModule.zero_matrix(K,24,1)",
            "current[1,1]=K(1)",
            "for column in 1:24",
            "  krylov[:,column]=current",
            "  global current=L*current",
            "end",
            "coordinates=AAModule.Solve.solve(krylov,rhs;side=:right)",
            "@assert krylov*coordinates==rhs",
            "function coefficient_list(value)",
            '  if iszero(value); return "0"; end',
            (
                "  return join([string(NemoModule.coeff(value,index)) "
                "for index in 0:NemoModule.degree(value)],\",\")"
            ),
            "end",
            'open("/tmp/cell5_primitive_coordinate_map.txt","w") do output',
            "  for degree in 0:23",
            "    value=coordinates[degree+1,1]",
            (
                f'    println(output,"{name}","\\t",degree,"\\t",'
                "coefficient_list(NemoModule.numerator(value)),\"\\t\","
                "coefficient_list(NemoModule.denominator(value)))"
            ),
            "  end",
            "end",
            'println("PRIMITIVE_COORDINATE_MAP_COMPLETE")',
        )
    )
    header = {
        "operator_sha256": hashlib.sha256(operator_raw).hexdigest(),
        "coordinate_columns_sha256": hashlib.sha256(columns_raw).hexdigest(),
        "basis_sha256": operator["basis_sha256"],
        "name": name,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "exact degree-below-24 expressions for b,x0,x1 in the primitive "
            "coordinate of the generic localized squared signed-pair algebra; "
            "no source-root, exceptional-fiber, colored-edge, route, row, or "
            "Prize conclusion"
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
                timeout=240,
            )
        except subprocess.TimeoutExpired as error:
            def decoded(value):
                if isinstance(value, bytes):
                    return value.decode("utf-8", errors="replace")
                return value or ""

            return {
                **header,
                "status": "TIMEOUT",
                "stdout": decoded(error.stdout)[-4000:],
                "stderr": decoded(error.stderr)[-4000:],
            }
    valid = process.returncode == 0 and "PRIMITIVE_COORDINATE_MAP_COMPLETE" in process.stdout
    result = {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    if valid:
        lines = Path("/tmp/cell5_primitive_coordinate_map.txt").read_text().splitlines()
        result["coordinates"] = [
            {
                "name": parts[0],
                "degree": int(parts[1]),
                "numerator": [int(value) for value in parts[2].split(",")],
                "denominator": [int(value) for value in parts[3].split(",")],
            }
            for line in lines
            for parts in (line.split("\t", 3),)
        ]
    return result


@app.local_entrypoint()
def main(output: str = ""):
    results = list(compute_map.map(("x1", "x0", "b"), order_outputs=True))
    for result in results:
        compact = {key: value for key, value in result.items() if key != "coordinates"}
        print(json.dumps(compact, sort_keys=True), flush=True)
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
