#!/usr/bin/env python3
"""Compile cleared-denominator data for the cell-5 guard rank certificate."""

import hashlib
import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PACKET = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients.bin"
)
PACKET_METADATA = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients_meta.json"
)
FACTORIZATION = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_"
    "factorization_structured_result.json"
)
REMOTE_PACKET = "/root/cell5_guard_square_matrix.bin"
REMOTE_METADATA = "/root/cell5_guard_square_matrix_meta.json"
REMOTE_FACTORIZATION = "/root/cell5_guard_square_factorization.json"

app = modal.App("rs-mca-positive-433-1a-cell5-guard-cleared-certificate")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .run_commands(
        "julia -e 'using Pkg; "
        'Pkg.add(["AbstractAlgebra", "Groebner", "JSON3"]); Pkg.precompile()\''
    )
    .add_local_file(PACKET, REMOTE_PACKET)
    .add_local_file(PACKET_METADATA, REMOTE_METADATA)
    .add_local_file(FACTORIZATION, REMOTE_FACTORIZATION)
)


@app.function(image=image, cpu=1.0, memory=4096, timeout=240)
def compile_shard(payload):
    import hashlib
    import json
    import subprocess
    import tempfile

    kind, index_text = payload.split(":", 1)
    index = int(index_text)
    metadata = json.loads(Path(REMOTE_METADATA).read_text())
    packet_sha256 = hashlib.sha256(Path(REMOTE_PACKET).read_bytes()).hexdigest()
    factorization_sha256 = hashlib.sha256(
        Path(REMOTE_FACTORIZATION).read_bytes()
    ).hexdigest()
    if packet_sha256 != metadata["packet_sha256"]:
        raise RuntimeError("square packet hash mismatch")
    factorization = json.loads(Path(REMOTE_FACTORIZATION).read_text())
    if (
        len(factorization) != 40
        or any(item["status"] != "COMPLETE" for item in factorization)
    ):
        raise RuntimeError("factorization coverage is incomplete")

    row_block = (
        f"rowIndex={index}\n"
        "denominators=[denominator(guardMatrix[rowIndex,column]) "
        "for column in 1:64]\n"
        "common=foldl(lcm,denominators)\n"
        'println(output,"E\\t",rowIndex,"\\t",coefficient_list(common))\n'
        "for column in 1:24\n"
        "  cleared=numerator(guardMatrix[rowIndex,column])*"
        "AAModule.divexact(common,denominator(guardMatrix[rowIndex,column]))\n"
        '  println(output,"P\\t",rowIndex,"\\t",column,"\\t",'
        "coefficient_list(cleared))\n"
        "end\n"
        "for column in 25:64\n"
        "  cleared=numerator(guardMatrix[rowIndex,column])*"
        "AAModule.divexact(common,denominator(guardMatrix[rowIndex,column]))\n"
        '  println(output,"B\\t",rowIndex,"\\t",column,"\\t",'
        "coefficient_list(cleared))\n"
        "end"
    )
    column_block = (
        f"columnIndex={index}\n"
        "values=[coordinateMap[(row,columnIndex)] for row in 1:24]\n"
        "common=foldl(lcm,[denominator(value) for value in values])\n"
        'println(output,"D\\t",columnIndex,"\\t",coefficient_list(common))\n'
        "for row in 1:24\n"
        "  value=values[row]\n"
        "  cleared=numerator(value)*"
        "AAModule.divexact(common,denominator(value))\n"
        '  println(output,"Y\\t",row,"\\t",columnIndex,"\\t",'
        "coefficient_list(cleared))\n"
        "end"
    )
    block = row_block if kind == "r" else column_block
    program = "\n".join(
        (
            "using JSON3",
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
            "  numerator=T([F(Int(value)) for value in numeratorCoefficients])",
            "  denominator=T([F(Int(value)) for value in denominatorCoefficients])",
            "  return numerator//denominator",
            "end",
            "function read_u32_vector(io,count)",
            "  values=Vector{UInt32}(undef,count)",
            "  read!(io,values)",
            "  return Int.(ltoh.(values))",
            "end",
            f'io=open("{REMOTE_PACKET}","r")',
            '@assert String(read(io,8))=="KBC5M02\\n"',
            "entryCount=Int(ltoh(read(io,UInt32)))",
            "basisHash=bytes2hex(read(io,32))",
            "coefficientsHash=bytes2hex(read(io,32))",
            f'@assert basisHash=="{metadata["basis_sha256"]}"',
            f'@assert coefficientsHash=="{metadata["coefficients_sha256"]}"',
            "guardMatrix=NemoModule.zero_matrix(K,64,64)",
            "for entryIndex in 1:entryCount",
            "  row=Int(read(io,UInt8))",
            "  column=Int(read(io,UInt8))",
            "  numeratorLength=Int(ltoh(read(io,UInt16)))",
            "  denominatorLength=Int(ltoh(read(io,UInt16)))",
            "  numeratorCoefficients=read_u32_vector(io,numeratorLength)",
            "  denominatorCoefficients=read_u32_vector(io,denominatorLength)",
            "  guardMatrix[row,column]=make_fraction("
            "numeratorCoefficients,denominatorCoefficients)",
            "end",
            "close(io)",
            f'factorization=JSON3.read(read("{REMOTE_FACTORIZATION}",String))',
            "coordinateMap=Dict{Tuple{Int,Int},Any}()",
            "for shard in factorization",
            "  for item in shard.coordinates",
            "    coordinateMap[(Int(item.row),Int(item.column))]="
            "make_fraction(item.numerator,item.denominator)",
            "  end",
            "end",
            "@assert length(coordinateMap)==960",
            "function coefficient_list(value)",
            "  return join([string(NemoModule.coeff(value,index)) "
            "for index in 0:NemoModule.degree(value)],\",\")",
            "end",
            'open("/tmp/cell5_guard_cleared.txt","w") do output',
            block,
            "end",
            f'println("CLEARED_SHARD_COMPLETE {kind} {index}")',
        )
    )
    header = {
        "kind": kind,
        "index": index,
        "basis_sha256": metadata["basis_sha256"],
        "coefficients_sha256": metadata["coefficients_sha256"],
        "packet_sha256": packet_sha256,
        "factorization_sha256": factorization_sha256,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "cleared-denominator polynomial data for the exact rank-24 "
            "factorization; no quotient, colored-edge, route, row, or Prize conclusion"
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
                timeout=210,
            )
        except subprocess.TimeoutExpired as error:
            return {
                **header,
                "status": "TIMEOUT",
                "stdout": (error.stdout or "")[-4000:],
                "stderr": (error.stderr or "")[-4000:],
            }
    valid = (
        process.returncode == 0
        and f"CLEARED_SHARD_COMPLETE {kind} {index}" in process.stdout
    )
    result = {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    if valid:
        records = []
        for line in Path("/tmp/cell5_guard_cleared.txt").read_text().splitlines():
            parts = line.split("\t")
            tag = parts[0]
            if tag in {"E", "D"}:
                records.append(
                    {
                        "tag": tag,
                        "index": int(parts[1]),
                        "coefficients": [int(value) for value in parts[2].split(",")],
                    }
                )
            else:
                records.append(
                    {
                        "tag": tag,
                        "row": int(parts[1]),
                        "column": int(parts[2]),
                        "coefficients": [int(value) for value in parts[3].split(",")],
                    }
                )
        result["records"] = records
    return result


@app.local_entrypoint()
def main(kind: str = "all", index: int = 0, output: str = ""):
    if kind == "all":
        payloads = [f"r:{row}" for row in range(1, 65)]
        payloads.extend(f"c:{column}" for column in range(25, 65))
    elif kind == "r" and 1 <= index <= 64:
        payloads = [f"r:{index}"]
    elif kind == "c" and 25 <= index <= 64:
        payloads = [f"c:{index}"]
    else:
        raise ValueError("kind/index must be all, r:1..64, or c:25..64")
    results = []
    for result in compile_shard.map(payloads, order_outputs=True):
        results.append(result)
        compact = {key: value for key, value in result.items() if key != "records"}
        print(json.dumps(compact, sort_keys=True), flush=True)
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
