#!/usr/bin/env python3
"""Exact multiplication operator on the localized cell-5 signed-pair algebra."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
BASIS = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_function_field_julia_basis_result.json"
)
SQUARE_PACKET = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients.bin"
)
SQUARE_METADATA = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients_meta.json"
)
REMOTE_BASIS = "/root/cell5_pair_function_field_julia_basis_result.json"
REMOTE_SQUARE_PACKET = "/root/cell5_pair_guard_square_matrix_coefficients.bin"
REMOTE_SQUARE_METADATA = "/root/cell5_pair_guard_square_matrix_coefficients_meta.json"

app = modal.App("rs-mca-positive-433-1a-cell5-pair-localized-operator")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; "
        'Pkg.add(["AbstractAlgebra", "Groebner"]); Pkg.precompile()\''
    )
    .add_local_file(BASIS, REMOTE_BASIS)
    .add_local_file(SQUARE_PACKET, REMOTE_SQUARE_PACKET)
    .add_local_file(SQUARE_METADATA, REMOTE_SQUARE_METADATA)
)


@app.function(image=image, cpu=1.0, memory=4096, timeout=300)
def operator_shard(payload):
    import hashlib
    import json
    import subprocess
    import tempfile

    alpha_text, beta_text, start_text, stop_text = payload.split(":", 3)
    alpha = int(alpha_text)
    beta = int(beta_text)
    start = int(start_text)
    stop = int(stop_text)
    basis_data = json.loads(Path(REMOTE_BASIS).read_text())[0]
    basis_text = "\n".join(basis_data["basis_lines"])
    basis_sha256 = hashlib.sha256(basis_text.encode()).hexdigest()
    if basis_sha256 != basis_data["basis_sha256"]:
        raise RuntimeError("imported basis hash mismatch")
    metadata = json.loads(Path(REMOTE_SQUARE_METADATA).read_text())
    packet_sha256 = hashlib.sha256(Path(REMOTE_SQUARE_PACKET).read_bytes()).hexdigest()
    if packet_sha256 != metadata["packet_sha256"]:
        raise RuntimeError("square packet hash mismatch")
    if metadata["basis_sha256"] != basis_sha256:
        raise RuntimeError("square packet basis mismatch")
    basis_literal = ",\n".join(basis_data["basis_lines"])

    program = "\n".join(
        (
            "using AbstractAlgebra, Groebner, SHA",
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
            (
                'U,(x1,x0,b)=NemoModule.polynomial_ring(K,["x1","x0","b"],'
                "internal_ordering=:degrevlex)"
            ),
            f"basis=[{basis_literal}]",
            '@assert isgroebner(basis; ordering=DegRevLex())',
            (
                "quotientBasis=Groebner.quotient_basis(basis; "
                "ordering=DegRevLex())"
            ),
            "@assert length(quotientBasis)==64",
            "basisIndex=Dict{Tuple{Vararg{Int}},Int}()",
            (
                "for (index,value) in enumerate(quotientBasis); "
                "basisIndex[Tuple(exponent_vector(value,1))]=index; end"
            ),
            "function make_fraction(numeratorCoefficients,denominatorCoefficients)",
            "  numerator=T([F(value) for value in numeratorCoefficients])",
            "  denominator=T([F(value) for value in denominatorCoefficients])",
            "  return numerator//denominator",
            "end",
            "function read_u32_vector(io,count)",
            "  values=Vector{UInt32}(undef,count)",
            "  read!(io,values)",
            "  return Int.(ltoh.(values))",
            "end",
            f'io=open("{REMOTE_SQUARE_PACKET}","r")',
            '@assert String(read(io,8))=="KBC5M02\\n"',
            "entryCount=Int(ltoh(read(io,UInt32)))",
            "basisHash=bytes2hex(read(io,32))",
            "coefficientsHash=bytes2hex(read(io,32))",
            f'@assert basisHash=="{metadata["basis_sha256"]}"',
            f'@assert coefficientsHash=="{metadata["coefficients_sha256"]}"',
            "squareMatrix=NemoModule.zero_matrix(K,64,64)",
            "for index in 1:entryCount",
            "  row=Int(read(io,UInt8))",
            "  column=Int(read(io,UInt8))",
            "  numeratorLength=Int(ltoh(read(io,UInt16)))",
            "  denominatorLength=Int(ltoh(read(io,UInt16)))",
            "  numeratorCoefficients=read_u32_vector(io,numeratorLength)",
            "  denominatorCoefficients=read_u32_vector(io,denominatorLength)",
            (
                "  squareMatrix[row,column]=make_fraction("
                "numeratorCoefficients,denominatorCoefficients)"
            ),
            "end",
            "close(io)",
            "stableBasis=squareMatrix[:,1:24]",
            "pivot=stableBasis[1:24,:]",
            "@assert !iszero(NemoModule.det(pivot))",
            f"ell=x1+K({alpha})*x0+K({beta})*b",
            f"indices=collect({start}:{stop})",
            (
                "products=normalform(basis,[ell*value for value in quotientBasis]; "
                "ordering=DegRevLex())"
            ),
            "ellMatrix=NemoModule.zero_matrix(K,64,64)",
            "for (column,value) in enumerate(products)",
            "  for termIndex in 1:length(value)",
            "    row=basisIndex[Tuple(exponent_vector(value,termIndex))]",
            "    ellMatrix[row,column]=coeff(value,termIndex)",
            "  end",
            "end",
            "targets=ellMatrix*stableBasis[:,indices]",
            (
                "coordinates=AAModule.Solve.solve(pivot,targets[1:24,:];"
                "side=:right)"
            ),
            "@assert pivot*coordinates==targets[1:24,:]",
            "@assert stableBasis*coordinates==targets",
            "function coefficient_list(value)",
            '  if iszero(value); return "0"; end',
            (
                "  return join([string(NemoModule.coeff(value,index)) "
                "for index in 0:NemoModule.degree(value)],\",\")"
            ),
            "end",
            'open("/tmp/cell5_localized_operator.txt","w") do output',
            "  for localColumn in 1:length(indices)",
            "    column=indices[localColumn]",
            "    for row in 1:24",
            "      value=coordinates[row,localColumn]",
            (
                '      println(output,"C\\t",row,"\\t",column,"\\t",'
                "coefficient_list(numerator(value)),\"\\t\","
                "coefficient_list(denominator(value)))"
            ),
            "    end",
            "    for row in 1:64",
            "      value=targets[row,localColumn]",
            "      if !iszero(value)",
            (
                '        println(output,"W\\t",row,"\\t",column,"\\t",'
                "coefficient_list(numerator(value)),\"\\t\","
                "coefficient_list(denominator(value)))"
            ),
            "      end",
            "    end",
            "  end",
            "end",
            (
                f'println("LOCALIZED_OPERATOR_SHARD_COMPLETE {alpha} {beta} ",'
                "first(indices),\" \",last(indices))"
            ),
        )
    )
    header = {
        "alpha": alpha,
        "beta": beta,
        "start": start,
        "stop": stop,
        "basis_sha256": basis_sha256,
        "square_packet_sha256": packet_sha256,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "exact multiplication by x1+alpha*x0+beta*b on the 24-dimensional "
            "stable image of guard squared; no reducedness, component, colored-edge, "
            "route, row, or Prize conclusion"
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
    marker = f"LOCALIZED_OPERATOR_SHARD_COMPLETE {alpha} {beta}"
    valid = process.returncode == 0 and marker in process.stdout
    result = {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    if valid:
        lines = Path("/tmp/cell5_localized_operator.txt").read_text().splitlines()
        result["entries"] = [
            {
                "kind": parts[0],
                "row": int(parts[1]),
                "column": int(parts[2]),
                "numerator": [int(value) for value in parts[3].split(",")],
                "denominator": [int(value) for value in parts[4].split(",")],
            }
            for line in lines
            for parts in (line.split("\t", 4),)
        ]
    return result


@app.local_entrypoint()
def main(
    alpha: int = 2,
    beta: int = 3,
    start: int = 1,
    stop: int = 24,
    shard_size: int = 2,
    output: str = "",
):
    if not 1 <= start <= stop <= 24:
        raise ValueError("columns must lie in 1..24")
    if shard_size < 1:
        raise ValueError("shard-size must be positive")
    payloads = [
        f"{alpha}:{beta}:{first}:{min(first + shard_size - 1, stop)}"
        for first in range(start, stop + 1, shard_size)
    ]
    results = []
    for result in operator_shard.map(payloads, order_outputs=True):
        results.append(result)
        compact = {key: value for key, value in result.items() if key != "entries"}
        print(json.dumps(compact, sort_keys=True), flush=True)
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
