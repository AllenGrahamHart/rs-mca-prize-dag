#!/usr/bin/env python3
"""Exact factorization of the cell-5 signed-pair primitive polynomial."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PRIMITIVE = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial_result.json"
)
REMOTE_PRIMITIVE = "/root/cell5_pair_primitive_polynomial.json"

app = modal.App("rs-mca-positive-433-1a-cell5-pair-primitive-factorization")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; "
        "Pkg.add([\"AbstractAlgebra\", \"Nemo\"]); Pkg.precompile()'"
    )
    .add_local_file(PRIMITIVE, REMOTE_PRIMITIVE)
)


@app.function(image=image, cpu=1.0, memory=8192, timeout=300)
def factor_polynomial():
    import hashlib
    import json
    import subprocess
    import tempfile

    primitive_path = Path(REMOTE_PRIMITIVE)
    raw = primitive_path.read_bytes()
    payload = json.loads(raw)
    if payload["status"] != "COMPLETE" or payload["returncode"] != 0:
        raise RuntimeError("primitive polynomial is incomplete")
    coefficients = sorted(payload["coefficients"], key=lambda item: item["degree"])
    if [item["degree"] for item in coefficients] != list(range(25)):
        raise RuntimeError("primitive coefficient coverage mismatch")
    assignments = [
        f"minimal += make_fraction({item['numerator']},{item['denominator']})*s^{item['degree']}"
        for item in coefficients
    ]
    program = "\n".join(
        (
            (
                'NemoModule=Base.require(Base.PkgId(Base.UUID('
                '"2edaba10-b0f1-5616-af89-8c11ac63239a"),"Nemo"))'
            ),
            "F=NemoModule.GF(2130706433)",
            'T,t=NemoModule.polynomial_ring(F,"t")',
            "K=NemoModule.fraction_field(T)",
            'R,s=NemoModule.polynomial_ring(K,"s")',
            "function make_fraction(numeratorCoefficients,denominatorCoefficients)",
            "  numerator=T([F(value) for value in numeratorCoefficients])",
            "  denominator=T([F(value) for value in denominatorCoefficients])",
            "  return numerator//denominator",
            "end",
            "minimal=zero(R)",
            *assignments,
            "@assert NemoModule.degree(minimal)==24",
            'println("PRIMITIVE_FACTORIZATION_START")',
            "factorization=NemoModule.factor(minimal)",
            "factors=collect(factorization)",
            "reconstructed=R(NemoModule.unit(factorization))",
            "for (value,multiplicity) in factors",
            "  global reconstructed *= value^multiplicity",
            "end",
            "@assert reconstructed==minimal",
            "function coefficient_list(value)",
            '  if iszero(value); return "0"; end',
            (
                "  return join([string(NemoModule.coeff(value,index)) "
                "for index in 0:NemoModule.degree(value)],\",\")"
            ),
            "end",
            'open("/tmp/cell5_primitive_factors.txt","w") do output',
            "  for (factorIndex,(value,multiplicity)) in enumerate(factors)",
            "    monicValue=value*inv(NemoModule.leading_coefficient(value))",
            "    for index in 0:NemoModule.degree(monicValue)",
            "      coefficient=NemoModule.coeff(monicValue,index)",
            (
                '      println(output,factorIndex,"\\t",multiplicity,"\\t",'
                "NemoModule.degree(monicValue),\"\\t\",index,\"\\t\","
                "coefficient_list(NemoModule.numerator(coefficient)),\"\\t\","
                "coefficient_list(NemoModule.denominator(coefficient)))"
            ),
            "    end",
            "  end",
            "end",
            'println("PRIMITIVE_FACTOR_COUNT ",length(factors))',
            'println("PRIMITIVE_FACTORIZATION_COMPLETE")',
        )
    )
    header = {
        "primitive_sha256": hashlib.sha256(raw).hexdigest(),
        "operator_sha256": payload["operator_sha256"],
        "basis_sha256": payload["basis_sha256"],
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "exact factorization over F_2130706433(t) of the degree-24 "
            "primitive polynomial for the generic localized signed-pair "
            "algebra; no exceptional-fiber, colored-edge, route, row, or "
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
    valid = process.returncode == 0 and "PRIMITIVE_FACTORIZATION_COMPLETE" in process.stdout
    result = {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    if valid:
        lines = Path("/tmp/cell5_primitive_factors.txt").read_text().splitlines()
        records = [
            {
                "factor": int(parts[0]),
                "multiplicity": int(parts[1]),
                "factor_degree": int(parts[2]),
                "coefficient_degree": int(parts[3]),
                "numerator": [int(value) for value in parts[4].split(",")],
                "denominator": [int(value) for value in parts[5].split(",")],
            }
            for line in lines
            for parts in (line.split("\t", 5),)
        ]
        result["factors"] = records
    return result


@app.local_entrypoint()
def main(output: str = ""):
    result = factor_polynomial.remote()
    compact = {key: value for key, value in result.items() if key != "factors"}
    print(json.dumps(compact, sort_keys=True))
    if output:
        Path(output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
