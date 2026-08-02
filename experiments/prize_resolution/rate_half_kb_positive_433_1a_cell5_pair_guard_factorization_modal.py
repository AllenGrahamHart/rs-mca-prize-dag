#!/usr/bin/env python3
"""Parallel exact rank-32 factorization of the cell-5 guard matrix."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
PACKET = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_matrix_coefficients.bin"
)
PACKET_METADATA = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_matrix_coefficients_meta.json"
)
PIVOTS = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_pivots_result.json"
)
SQUARE_PACKET = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients.bin"
)
SQUARE_PACKET_METADATA = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients_meta.json"
)
SQUARE_PIVOTS = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_pivots_result.json"
)
REMOTE_PACKET = "/root/cell5_pair_guard_matrix_coefficients.bin"
REMOTE_PACKET_METADATA = "/root/cell5_pair_guard_matrix_coefficients_meta.json"
REMOTE_PIVOTS = "/root/cell5_pair_guard_pivots_result.json"
REMOTE_SQUARE_PACKET = "/root/cell5_pair_guard_square_matrix_coefficients.bin"
REMOTE_SQUARE_PACKET_METADATA = (
    "/root/cell5_pair_guard_square_matrix_coefficients_meta.json"
)
REMOTE_SQUARE_PIVOTS = "/root/cell5_pair_guard_square_pivots_result.json"

app = modal.App("rs-mca-positive-433-1a-cell5-pair-guard-factorization")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .pip_install("sympy==1.14.0")
    .run_commands(
        "julia -e 'using Pkg; "
        'Pkg.add(["AbstractAlgebra", "Groebner"]); Pkg.precompile()\''
    )
    .add_local_file(PACKET, REMOTE_PACKET)
    .add_local_file(PACKET_METADATA, REMOTE_PACKET_METADATA)
    .add_local_file(PIVOTS, REMOTE_PIVOTS)
    .add_local_file(SQUARE_PACKET, REMOTE_SQUARE_PACKET)
    .add_local_file(SQUARE_PACKET_METADATA, REMOTE_SQUARE_PACKET_METADATA)
    .add_local_file(SQUARE_PIVOTS, REMOTE_SQUARE_PIVOTS)
)


@app.function(image=image, cpu=1.0, memory=8192, timeout=300)
def solve_shard(payload):
    import hashlib
    import json
    import subprocess
    import tempfile

    power_text, pivot_size_text, start_text, stop_text = payload.split(":", 3)
    power = int(power_text)
    pivot_size = int(pivot_size_text)
    start = int(start_text)
    stop = int(stop_text)
    if power == 1:
        packet_path = Path(REMOTE_PACKET)
        metadata_path = Path(REMOTE_PACKET_METADATA)
        pivots_path = Path(REMOTE_PIVOTS)
    elif power == 2:
        packet_path = Path(REMOTE_SQUARE_PACKET)
        metadata_path = Path(REMOTE_SQUARE_PACKET_METADATA)
        pivots_path = Path(REMOTE_SQUARE_PIVOTS)
    else:
        raise RuntimeError("only guard powers one and two are mounted")
    metadata = json.loads(metadata_path.read_text())
    pivots = json.loads(pivots_path.read_text())
    packet_sha256 = hashlib.sha256(packet_path.read_bytes()).hexdigest()
    if packet_sha256 != metadata["packet_sha256"]:
        raise RuntimeError("guard matrix packet hash mismatch")
    for key in ("basis_sha256", "coefficients_sha256", "packet_sha256"):
        if pivots[key] != metadata[key]:
            raise RuntimeError(f"pivot {key} mismatch")
    pivot_rows = pivots["pivot_rows"]
    pivot_columns = pivots["pivot_columns"]
    if (
        pivot_rows != list(range(1, pivot_size + 1))
        or pivot_columns != list(range(1, pivot_size + 1))
    ):
        raise RuntimeError("factorization compiler expects the top-left pivot block")

    program = "\n".join(
        (
            "using Groebner, SHA",
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
            "function read_u32_vector(io,count)",
            "  values=Vector{UInt32}(undef,count)",
            "  read!(io,values)",
            "  return Int.(ltoh.(values))",
            "end",
            f'io=open("{packet_path}","r")',
            f'@assert String(read(io,8))=="KBC5M{power:02d}\\n"',
            "entryCount=Int(ltoh(read(io,UInt32)))",
            "basisHash=bytes2hex(read(io,32))",
            "coefficientsHash=bytes2hex(read(io,32))",
            f'@assert basisHash=="{metadata["basis_sha256"]}"',
            f'@assert coefficientsHash=="{metadata["coefficients_sha256"]}"',
            "guardMatrix=NemoModule.zero_matrix(K,64,64)",
            "for index in 1:entryCount",
            "  row=Int(read(io,UInt8))",
            "  column=Int(read(io,UInt8))",
            "  numeratorLength=Int(ltoh(read(io,UInt16)))",
            "  denominatorLength=Int(ltoh(read(io,UInt16)))",
            "  numeratorCoefficients=read_u32_vector(io,numeratorLength)",
            "  denominatorCoefficients=read_u32_vector(io,denominatorLength)",
            (
                "  guardMatrix[row,column]=make_fraction("
                "numeratorCoefficients,denominatorCoefficients)"
            ),
            "end",
            "close(io)",
            f"pivot=guardMatrix[1:{pivot_size},1:{pivot_size}]",
            f"rightHandSide=guardMatrix[1:{pivot_size},{start}:{stop}]",
            (
                "coordinates=AAModule.Solve.solve(pivot,rightHandSide;"
                "side=:right)"
            ),
            "@assert pivot*coordinates==rightHandSide",
            (
                f"@assert guardMatrix[:,1:{pivot_size}]*coordinates=="
                f"guardMatrix[:,{start}:{stop}]"
            ),
            'println("GUARD_FACTOR_SHARD_VERIFIED")',
            "function coefficient_list(value)",
            (
                "  return join([string(NemoModule.coeff(value,index)) "
                "for index in 0:NemoModule.degree(value)],\",\")"
            ),
            "end",
            'open("/tmp/cell5_guard_factor_coordinates.txt","w") do output',
            "  for localColumn in 1:AAModule.ncols(coordinates)",
            "    for row in 1:AAModule.nrows(coordinates)",
            "      value=coordinates[row,localColumn]",
            (
                '      println(output,row,"\\t",'
                f"{start}-1+localColumn,\"\\t\","
                "coefficient_list(numerator(value)),\"\\t\","
                "coefficient_list(denominator(value)))"
            ),
            "    end",
            "  end",
            "end",
            f'println("GUARD_FACTOR_SHARD_COMPLETE {start} {stop}")',
        )
    )
    header = {
        "start": start,
        "stop": stop,
        "guard_power": power,
        "pivot_size": pivot_size,
        "basis_sha256": metadata["basis_sha256"],
        "coefficients_sha256": metadata["coefficients_sha256"],
        "packet_sha256": packet_sha256,
        "pivots_sha256": hashlib.sha256(pivots_path.read_bytes()).hexdigest(),
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            "exact rational-function coordinates for selected columns in the "
            f"rank-{pivot_size} factorization of guard-power-{power} multiplication; "
            "no stable-rank, "
            "colored-edge, route, row, or Prize conclusion"
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
    valid = (
        process.returncode == 0
        and "GUARD_FACTOR_SHARD_COMPLETE" in process.stdout
    )
    result = {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    if valid:
        lines = Path("/tmp/cell5_guard_factor_coordinates.txt").read_text().splitlines()
        result["coordinates"] = [
            {
                "row": int(parts[0]),
                "column": int(parts[1]),
                "numerator": [int(value) for value in parts[2].split(",")],
                "denominator": [int(value) for value in parts[3].split(",")],
            }
            for line in lines
            for parts in (line.split("\t", 3),)
        ]
    return result


@app.local_entrypoint()
def main(
    power: int = 1,
    pivot_size: int = 32,
    start: int = 33,
    stop: int = 36,
    shard_size: int = 4,
    output: str = "",
):
    if power not in (1, 2):
        raise ValueError("power must be one or two")
    if not 1 <= pivot_size < start <= stop <= 64:
        raise ValueError("columns must lie after the pivot block and within 1..64")
    if shard_size < 1:
        raise ValueError("shard-size must be positive")
    payloads = [
        f"{power}:{pivot_size}:{first}:{min(first + shard_size - 1, stop)}"
        for first in range(start, stop + 1, shard_size)
    ]
    results = []
    for result in solve_shard.map(payloads, order_outputs=True):
        results.append(result)
        compact = {key: value for key, value in result.items() if key != "coordinates"}
        print(json.dumps(compact, sort_keys=True), flush=True)
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
