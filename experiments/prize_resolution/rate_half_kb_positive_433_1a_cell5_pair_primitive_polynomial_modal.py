#!/usr/bin/env python3
"""Exact primitive polynomial of the localized cell-5 signed-pair algebra."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
OPERATOR = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_localized_operator_merged_result.json"
)
REMOTE_OPERATOR = "/root/cell5_pair_localized_operator.json"

app = modal.App("rs-mca-positive-433-1a-cell5-pair-primitive-polynomial")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; "
        "Pkg.add([\"AbstractAlgebra\", \"Nemo\"]); Pkg.precompile()'"
    )
    .add_local_file(OPERATOR, REMOTE_OPERATOR)
)


@app.function(image=image, cpu=1.0, memory=8192, timeout=300)
def compute_polynomial():
    import hashlib
    import json
    import subprocess
    import tempfile

    operator_path = Path(REMOTE_OPERATOR)
    raw = operator_path.read_bytes()
    payload = json.loads(raw)
    if payload["schema"] != "rate-half-kb-positive-433-1a-cell5-localized-operator-v1":
        raise RuntimeError("operator schema mismatch")
    coordinates = {
        (entry["row"], entry["column"]): entry
        for entry in payload["entries"]
        if entry["kind"] == "C"
    }
    if set(coordinates) != {
        (row, column)
        for row in range(1, 25)
        for column in range(1, 25)
    }:
        raise RuntimeError("operator coordinate coverage mismatch")
    assignments = []
    for (row, column), entry in sorted(coordinates.items()):
        assignments.append(
            f"L[{row},{column}]=make_fraction("
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
            *assignments,
            "krylov=NemoModule.zero_matrix(K,24,24)",
            "current=NemoModule.zero_matrix(K,24,1)",
            "current[1,1]=K(1)",
            "for column in 1:24",
            "  krylov[:,column]=current",
            "  global current=L*current",
            "end",
            "target=current",
            'println("PRIMITIVE_KRYLOV_BUILT")',
            "relation=AAModule.Solve.solve(krylov,target;side=:right)",
            "@assert krylov*relation==target",
            'R,s=NemoModule.polynomial_ring(K,"s")',
            "minimal=s^24",
            "for index in 1:24",
            "  global minimal -= relation[index,1]*s^(index-1)",
            "end",
            "@assert NemoModule.degree(minimal)==24",
            "@assert NemoModule.leading_coefficient(minimal)==K(1)",
            "function coefficient_list(value)",
            '  if iszero(value); return "0"; end',
            (
                "  return join([string(NemoModule.coeff(value,index)) "
                "for index in 0:NemoModule.degree(value)],\",\")"
            ),
            "end",
            'open("/tmp/cell5_primitive_polynomial.txt","w") do output',
            "  for index in 0:24",
            "    value=NemoModule.coeff(minimal,index)",
            (
                '    println(output,index,"\\t",'
                "coefficient_list(NemoModule.numerator(value)),\"\\t\","
                "coefficient_list(NemoModule.denominator(value)))"
            ),
            "  end",
            "end",
            'println("PRIMITIVE_POLYNOMIAL_COMPLETE")',
        )
    )
    header = {
        "operator_sha256": hashlib.sha256(raw).hexdigest(),
        "basis_sha256": payload["basis_sha256"],
        "alpha": payload["alpha"],
        "beta": payload["beta"],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "exact degree-24 Krylov minimal polynomial of multiplication by "
            "x1+2*x0+3*b on the generic localized signed-pair algebra; no "
            "factorization, exceptional-fiber, colored-edge, route, row, or "
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
    valid = process.returncode == 0 and "PRIMITIVE_POLYNOMIAL_COMPLETE" in process.stdout
    result = {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    if valid:
        lines = Path("/tmp/cell5_primitive_polynomial.txt").read_text().splitlines()
        result["coefficients"] = [
            {
                "degree": int(parts[0]),
                "numerator": [int(value) for value in parts[1].split(",")],
                "denominator": [int(value) for value in parts[2].split(",")],
            }
            for line in lines
            for parts in (line.split("\t", 2),)
        ]
    return result


@app.local_entrypoint()
def main(output: str = ""):
    result = compute_polynomial.remote()
    compact = {key: value for key, value in result.items() if key != "coefficients"}
    print(json.dumps(compact, sort_keys=True))
    if output:
        Path(output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
