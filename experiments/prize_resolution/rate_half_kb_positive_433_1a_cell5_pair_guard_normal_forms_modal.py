#!/usr/bin/env python3
"""Parallel exact guard normal forms in the cell-5 signed-pair quotient."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
SPARSE = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
ATLAS = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"
BASIS = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_function_field_julia_basis_result.json"
)
REMOTE_SPARSE = "/root/rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
REMOTE_ATLAS = "/root/rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"
REMOTE_BASIS = "/root/cell5_pair_function_field_julia_basis_result.json"

app = modal.App("rs-mca-positive-433-1a-cell5-pair-guard-normal-forms")
image = (
    modal.Image.from_registry("julia:1.11-bookworm", add_python="3.12")
    .env({"JULIA_CPU_TARGET": "generic"})
    .pip_install("sympy==1.14.0")
    .run_commands(
        "julia -e 'using Pkg; "
        'Pkg.add(["AbstractAlgebra", "Groebner"]); Pkg.precompile()\''
    )
    .add_local_file(SPARSE, REMOTE_SPARSE)
    .add_local_file(ATLAS, REMOTE_ATLAS)
    .add_local_file(BASIS, REMOTE_BASIS)
)


@app.function(image=image, cpu=1.0, memory=3072, timeout=300)
def reduce_shard(payload):
    import hashlib
    import json
    import subprocess
    import sys
    import tempfile

    import sympy as sp

    power_text, start_text, stop_text = payload.split(":", 2)
    power = int(power_text)
    start = int(start_text)
    stop = int(stop_text)
    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_cell5_sparse_edge_probe import (
        sparse_product_kernel,
    )

    data = json.loads(Path(REMOTE_ATLAS).read_text())
    basis_data = json.loads(Path(REMOTE_BASIS).read_text())[0]
    basis_text = "\n".join(basis_data["basis_lines"])
    basis_sha256 = hashlib.sha256(basis_text.encode()).hexdigest()
    if basis_sha256 != basis_data["basis_sha256"]:
        raise RuntimeError("imported basis hash mismatch")

    prime = data["characteristic"]
    iota = data["iota"]
    chart = {item["basis_index"]: item for item in data["c_charts"]}[2]
    r, c, b, t = sp.symbols("r c b t")
    variables = (r, c, b, t)
    parse = {"r": r, "c": c, "b": b, "t": t}

    def julia(expression):
        return str(
            sp.Poly(sp.expand(expression), *variables, modulus=prime).as_expr()
        ).replace("**", "^")

    a0t = t**4 - 2 * iota * t**3 - 4 * iota * t**2 - 2 * iota * t - 1
    a1t = -8 * iota * (t**4 + 1)
    a2t = -2 * t**4 + 4 * iota * t**3 - 24 * iota * t**2 + 4 * iota * t + 2
    primitive = sp.expand(
        a0t * (b**4 + 1) + a1t * (b**3 + b) + a2t * b**2
    )
    r_leading = sp.sympify(data["r_chart"]["leading"], locals=parse)
    r_constant = sp.sympify(data["r_chart"]["constant"], locals=parse)
    c_leading = sp.sympify(chart["leading"], locals=parse)
    c_constant = sp.sympify(chart["constant"], locals=parse)
    a2_source, _, _, _, _ = sparse_product_kernel()
    basis_literal = ",\n".join(basis_data["basis_lines"])

    program = "\n".join(
        (
            "using AbstractAlgebra, Groebner, SHA",
            f"F=GF({prime})",
            'K,t=rational_function_field(F,"t")',
            'S,b=polynomial_ring(K,"b")',
            f"primitive={julia(primitive)}",
            "primitive=primitive*inv(leading_coefficient(primitive))",
            f"rLeading=S({julia(r_leading)})",
            f"rConstant=S({julia(r_constant)})",
            f"cLeading=S({julia(c_leading)})",
            f"cConstant=S({julia(c_constant)})",
            "function inverse_mod(value,modulus)",
            "  g,left,_=gcdx(value,modulus)",
            "  @assert degree(g)==0",
            "  return rem(left*inv(leading_coefficient(g)),modulus)",
            "end",
            "rValue=rem(-rConstant*inverse_mod(rLeading,primitive),primitive)",
            "cValue=rem(-cConstant*inverse_mod(cLeading,primitive),primitive)",
            "r=rValue",
            "c=cValue",
            *(f"a2_{index}=rem({julia(value)},primitive)"
              for index, value in enumerate(a2_source)),
            (
                'U,(x1,x0,BU)=polynomial_ring(K,["x1","x0","b"],'
                "internal_ordering=:degrevlex)"
            ),
            "function embed(value)",
            "  output=zero(U)",
            "  for index in 0:degree(value)",
            "    output += U(coeff(value,index))*BU^index",
            "  end",
            "  return output",
            "end",
            "a2=[embed(a2_0),embed(a2_1),embed(a2_2)]",
            "d0=a2[1]+a2[2]*x0+a2[3]*x0^2",
            "d1=a2[1]+a2[2]*x1+a2[3]*x1^2",
            "guard=d0*d1",
            "b=BU",
            f"basis=[{basis_literal}]",
            '@assert isgroebner(basis; ordering=DegRevLex())',
            (
                "quotientBasis=Groebner.quotient_basis(basis; "
                "ordering=DegRevLex())"
            ),
            "basisIndex=Dict{Tuple{Vararg{Int}},Int}()",
            (
                "for (index,value) in enumerate(quotientBasis); "
                "basisIndex[Tuple(exponent_vector(value,1))]=index; end"
            ),
            f"indices=collect({start}:{stop})",
            (
                f"products=normalform(basis,[guard^{power}*quotientBasis[index] "
                "for index in indices]; ordering=DegRevLex())"
            ),
            "function coefficient_list(value)",
            "  return join([string(coeff(value,index)) "
            "for index in 0:degree(value)],\",\")",
            "end",
            'open("/tmp/cell5_guard_normal_forms.txt","w") do io',
            "  for (offset,value) in enumerate(products)",
            "    column=indices[offset]",
            "    for termIndex in 1:length(value)",
            "      row=basisIndex[Tuple(exponent_vector(value,termIndex))]",
            (
                "      println(io,column,\"\\t\",row,\"\\t\","
                "coefficient_list(numerator(coeff(value,termIndex))),"
                "\"\\t\",coefficient_list(denominator(coeff(value,termIndex))))"
            ),
            "    end",
            "  end",
            "end",
            (
                f'println("GUARD_POWER_{power}_NORMAL_FORMS_COMPLETE ",'
                "first(indices),\" \",last(indices))"
            ),
        )
    )
    header = {
        "start": start,
        "stop": stop,
        "guard_power": power,
        "basis_sha256": basis_sha256,
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "scope": (
            f"exact columns of multiplication by (D0D1)^{power} in the generic-t "
            "64-dimensional squared signed-pair quotient; no rank, colored "
            "edge, route, row, or Prize conclusion"
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
        and f"GUARD_POWER_{power}_NORMAL_FORMS_COMPLETE" in process.stdout
    )
    result = {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }
    if valid:
        lines = Path("/tmp/cell5_guard_normal_forms.txt").read_text().splitlines()
        result["matrix_entries"] = [
            {
                "column": int(parts[0]),
                "row": int(parts[1]),
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
    start: int = 1,
    stop: int = 64,
    shard_size: int = 4,
    output: str = "",
):
    if power < 1:
        raise ValueError("power must be positive")
    if not 1 <= start <= stop <= 64:
        raise ValueError("columns must lie in 1..64")
    if shard_size < 1:
        raise ValueError("shard-size must be positive")
    payloads = [
        f"{power}:{first}:{min(first + shard_size - 1, stop)}"
        for first in range(start, stop + 1, shard_size)
    ]
    results = []
    for result in reduce_shard.map(payloads, order_outputs=True):
        results.append(result)
        compact = {
            key: value for key, value in result.items() if key != "matrix_entries"
        }
        print(json.dumps(compact, sort_keys=True), flush=True)
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
