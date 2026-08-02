#!/usr/bin/env python3
"""Groebner.jl attack on the four-generator cell-5 signed-pair quotient."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
SPARSE = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
ATLAS = DIRECTORY / "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"
BASIS_EXPORT = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_function_field_julia_basis_result.json"
)
REMOTE_SPARSE = "/root/rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py"
REMOTE_ATLAS = "/root/rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json"
REMOTE_BASIS_EXPORT = "/root/cell5_pair_function_field_julia_basis_result.json"

app = modal.App("rs-mca-positive-433-1a-cell5-pair-ff-groebner-julia")
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
    .add_local_file(BASIS_EXPORT, REMOTE_BASIS_EXPORT)
)


@app.function(image=image, cpu=1.0, memory=4096, timeout=300)
def analyze(payload):
    import hashlib
    import json
    import subprocess
    import sys
    import tempfile

    import sympy as sp

    stage, chart_text = payload.split(":", 1)
    chart_index = int(chart_text)
    sys.path.insert(0, "/root")
    from rate_half_kb_positive_433_1a_cell5_sparse_edge_probe import (
        sparse_product_kernel,
    )

    data = json.loads(Path(REMOTE_ATLAS).read_text())
    prime = data["characteristic"]
    iota = data["iota"]
    charts = {item["basis_index"]: item for item in data["c_charts"]}
    chart = charts[chart_index]

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
    denominator_product = sp.expand(r_leading * c_leading)
    a2_source, a0_source, _, _, _ = sparse_product_kernel()

    source = "\n".join(
        (
            "using AbstractAlgebra, Groebner, SHA",
            f"F=GF({prime})",
            'K,t=rational_function_field(F,"t")',
            'S,b=polynomial_ring(K,"b")',
            f"primitive={julia(primitive)}",
            "primitive=primitive*inv(leading_coefficient(primitive))",
            f"rLeading={julia(r_leading)}",
            f"rConstant={julia(r_constant)}",
            f"cLeading={julia(c_leading)}",
            f"cConstant={julia(c_constant)}",
            "rLeading=S(rLeading)",
            "rConstant=S(rConstant)",
            "cLeading=S(cLeading)",
            "cConstant=S(cConstant)",
            "function inverse_mod(value, modulus)",
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
            *(f"a0_{index}=rem({julia(value)},primitive)"
              for index, value in enumerate(a0_source)),
            (
                'R,(e,z1,z0,B)=polynomial_ring(K,["e","z1","z0","b"],'
                "internal_ordering=:degrevlex)"
            ),
            "function embed(value)",
            "  output=zero(R)",
            "  for index in 0:degree(value)",
            "    output += R(coeff(value,index))*B^index",
            "  end",
            "  return output",
            "end",
            "P=embed(primitive)",
            "a2=[embed(a2_0),embed(a2_1),embed(a2_2)]",
            "a0=[embed(a0_0),embed(a0_1),embed(a0_2)]",
            "delta=t^2*(t^2-1)",
            "beta=-t*(1+B)*(a2[1]+a2[2]*t^2+a2[3]*t^4)",
            "d0=a2[1]+a2[2]*z0^2+a2[3]*z0^4",
            "d1=a2[1]+a2[2]*z1^2+a2[3]*z1^4",
            "n0=a0[1]+a0[2]*z0^2+a0[3]*z0^4",
            "n1=a0[1]+a0[2]*z1^2+a0[3]*z1^4",
            "q0=z0*beta*(z0^2-1)",
            "q1=z1*beta*(z1^2-1)",
            "g3=n1*d0+n0*d1",
            "g4=q0*d1-q1*d0+2*e*delta*d0*d1",
            "g5=delta*n0+e*q0+e^2*delta*d0",
            "system=[P,g3,g4,g5]",
            (
                'U,(x1,x0,BU)=polynomial_ring(K,["x1","x0","b"],'
                "internal_ordering=:degrevlex)"
            ),
            "function embed_squared(value)",
            "  output=zero(U)",
            "  for index in 0:degree(value)",
            "    output += U(coeff(value,index))*BU^index",
            "  end",
            "  return output",
            "end",
            "PU=embed_squared(primitive)",
            "a2U=[embed_squared(a2_0),embed_squared(a2_1),embed_squared(a2_2)]",
            "a0U=[embed_squared(a0_0),embed_squared(a0_1),embed_squared(a0_2)]",
            "betaU=-t*(1+BU)*(a2U[1]+a2U[2]*t^2+a2U[3]*t^4)",
            "d0U=a2U[1]+a2U[2]*x0+a2U[3]*x0^2",
            "d1U=a2U[1]+a2U[2]*x1+a2U[3]*x1^2",
            "n0U=a0U[1]+a0U[2]*x0+a0U[3]*x0^2",
            "n1U=a0U[1]+a0U[2]*x1+a0U[3]*x1^2",
            "q0Squared=x0*betaU^2*(x0-1)^2",
            "q1Squared=x1*betaU^2*(x1-1)^2",
            "g3U=n1U*d0U+n0U*d1U",
            (
            "hU=q1Squared*d0U^2-q0Squared*d1U^2+"
                "4*delta^2*n0U*d0U*d1U^2"
            ),
            "squaredSystem=[PU,g3U,hU]",
            "d0Guarded=a2[1]+a2[2]*z0+a2[3]*z0^2",
            "d1Guarded=a2[1]+a2[2]*z1+a2[3]*z1^2",
            "n0Guarded=a0[1]+a0[2]*z0+a0[3]*z0^2",
            "n1Guarded=a0[1]+a0[2]*z1+a0[3]*z1^2",
            "q0SquaredGuarded=z0*beta^2*(z0-1)^2",
            "q1SquaredGuarded=z1*beta^2*(z1-1)^2",
            "g3Guarded=n1Guarded*d0Guarded+n0Guarded*d1Guarded",
            (
                "hGuarded=q1SquaredGuarded*d0Guarded^2-"
                "q0SquaredGuarded*d1Guarded^2+"
                "4*delta^2*n0Guarded*d0Guarded*d1Guarded^2"
            ),
            "denominatorGuard=e*d0Guarded*d1Guarded-1",
            "guardedSquaredSystem=[P,g3Guarded,hGuarded,denominatorGuard]",
            'println("DENOMINATOR_GCD_DEGREES ",degree(gcd(rLeading,primitive)),'
            '",",degree(gcd(cLeading,primitive)))',
            *(f'println("LEDGER {name} ",total_degree({name})," ",length({name}))'
              for name in ("P", "g3", "g4", "g5")),
            *(f'println("SQUARED_LEDGER {name} ",total_degree({name})," ",length({name}))'
              for name in ("PU", "g3U", "hU")),
            *(f'println("GUARDED_LEDGER {name} ",total_degree({name})," ",length({name}))'
              for name in ("P", "g3Guarded", "hGuarded", "denominatorGuard")),
        )
    )
    if stage == "ledger":
        computation = 'println("PAIR_JULIA_FF_LEDGER_COMPLETE")'
        expected = "PAIR_JULIA_FF_LEDGER_COMPLETE"
    elif stage == "groebner":
        computation = "\n".join(
            (
                'println("PAIR_JULIA_FF_BASIS_START")',
                (
                    "basis=groebner(system; ordering=DegRevLex(), "
                    "linalg=:deterministic, tasks=1)"
                ),
                'println("PAIR_JULIA_FF_BASIS_COMPLETE ",length(basis))',
                (
                    'for (index,value) in enumerate(basis); println("BASIS ",'
                    'index," ",total_degree(value)," ",length(value)); end'
                ),
                '@assert isgroebner(basis; ordering=DegRevLex())',
                'println("PAIR_JULIA_FF_CERTIFIED")',
            )
        )
        expected = "PAIR_JULIA_FF_CERTIFIED"
    elif stage == "squared-ledger":
        computation = 'println("PAIR_JULIA_FF_SQUARED_LEDGER_COMPLETE")'
        expected = "PAIR_JULIA_FF_SQUARED_LEDGER_COMPLETE"
    elif stage == "squared-groebner":
        computation = "\n".join(
            (
                'println("PAIR_JULIA_FF_SQUARED_BASIS_START")',
                (
                    "squaredBasis=groebner(squaredSystem; ordering=DegRevLex(), "
                    "linalg=:deterministic, tasks=1)"
                ),
                (
                    'println("PAIR_JULIA_FF_SQUARED_BASIS_COMPLETE ",'
                    "length(squaredBasis))"
                ),
                (
                    'for (index,value) in enumerate(squaredBasis); '
                    'println("SQUARED_BASIS ",index," ",total_degree(value),'
                    '",",length(value)); end'
                ),
                '@assert isgroebner(squaredBasis; ordering=DegRevLex())',
                (
                    'println("PAIR_JULIA_FF_SQUARED_BASIS_SHA256 ",'
                    'bytes2hex(sha256(join(string.(squaredBasis),"\\n"))))'
                ),
                'println("PAIR_JULIA_FF_SQUARED_CERTIFIED")',
            )
        )
        expected = "PAIR_JULIA_FF_SQUARED_CERTIFIED"
    elif stage == "squared-profile":
        computation = "\n".join(
            (
                'println("PAIR_JULIA_FF_SQUARED_PROFILE_START")',
                (
                    "squaredBasis=groebner(squaredSystem; ordering=DegRevLex(), "
                    "linalg=:deterministic, tasks=1)"
                ),
                '@assert isgroebner(squaredBasis; ordering=DegRevLex())',
                "squaredDimension=Groebner.dimension(squaredBasis)",
                'println("SQUARED_DIMENSION ",squaredDimension)',
                "@assert squaredDimension==0",
                (
                    "quotientBasis=Groebner.quotient_basis(squaredBasis; "
                    "ordering=DegRevLex())"
                ),
                'println("SQUARED_QUOTIENT_DIMENSION ",length(quotientBasis))',
                (
                    'println("PAIR_JULIA_FF_SQUARED_BASIS_SHA256 ",'
                    'bytes2hex(sha256(join(string.(squaredBasis),"\\n"))))'
                ),
                'println("PAIR_JULIA_FF_SQUARED_PROFILE_COMPLETE")',
            )
        )
        expected = "PAIR_JULIA_FF_SQUARED_PROFILE_COMPLETE"
    elif stage == "squared-export":
        computation = "\n".join(
            (
                'println("PAIR_JULIA_FF_SQUARED_EXPORT_START")',
                (
                    "squaredBasis=groebner(squaredSystem; ordering=DegRevLex(), "
                    "linalg=:deterministic, tasks=1)"
                ),
                '@assert isgroebner(squaredBasis; ordering=DegRevLex())',
                (
                    'open("/tmp/cell5_pair_squared_basis.txt","w") do io; '
                    "for value in squaredBasis; println(io,value); end; end"
                ),
                (
                    'println("PAIR_JULIA_FF_SQUARED_BASIS_SHA256 ",'
                    'bytes2hex(sha256(join(string.(squaredBasis),"\\n"))))'
                ),
                'println("PAIR_JULIA_FF_SQUARED_EXPORT_COMPLETE")',
            )
        )
        expected = "PAIR_JULIA_FF_SQUARED_EXPORT_COMPLETE"
    elif stage == "guarded-profile":
        computation = "\n".join(
            (
                'println("PAIR_JULIA_FF_GUARDED_PROFILE_START")',
                (
                    "guardedBasis=groebner(guardedSquaredSystem; "
                    "ordering=DegRevLex(), linalg=:deterministic, tasks=1)"
                ),
                '@assert isgroebner(guardedBasis; ordering=DegRevLex())',
                "guardedDimension=Groebner.dimension(guardedBasis)",
                'println("GUARDED_DIMENSION ",guardedDimension)',
                "@assert guardedDimension==0",
                (
                    "guardedQuotientBasis=Groebner.quotient_basis(guardedBasis; "
                    "ordering=DegRevLex())"
                ),
                (
                    'println("GUARDED_QUOTIENT_DIMENSION ",'
                    "length(guardedQuotientBasis))"
                ),
                (
                    'println("PAIR_JULIA_FF_GUARDED_BASIS_SHA256 ",'
                    'bytes2hex(sha256(join(string.(guardedBasis),"\\n"))))'
                ),
                'println("PAIR_JULIA_FF_GUARDED_PROFILE_COMPLETE")',
            )
        )
        expected = "PAIR_JULIA_FF_GUARDED_PROFILE_COMPLETE"
    elif stage == "guard-rank":
        computation = "\n".join(
            (
                'println("PAIR_JULIA_FF_GUARD_RANK_START")',
                (
                    "squaredBasis=groebner(squaredSystem; ordering=DegRevLex(), "
                    "linalg=:deterministic, tasks=1)"
                ),
                '@assert isgroebner(squaredBasis; ordering=DegRevLex())',
                (
                    "quotientBasis=Groebner.quotient_basis(squaredBasis; "
                    "ordering=DegRevLex())"
                ),
                "basisIndex=Dict{Tuple{Vararg{Int}},Int}()",
                (
                    "for (index,value) in enumerate(quotientBasis); "
                    "basisIndex[Tuple(exponent_vector(value,1))]=index; end"
                ),
                "guardU=d0U*d1U",
                (
                    "products=normalform(squaredBasis,"
                    "[guardU*value for value in quotientBasis]; "
                    "ordering=DegRevLex())"
                ),
                "quotientDimension=length(quotientBasis)",
                "guardMatrix=zero_matrix(K,quotientDimension,quotientDimension)",
                "for column in 1:quotientDimension",
                "  value=products[column]",
                "  for termIndex in 1:length(value)",
                "    row=basisIndex[Tuple(exponent_vector(value,termIndex))]",
                "    guardMatrix[row,column]=coeff(value,termIndex)",
                "  end",
                "end",
                "powerMatrix=guardMatrix",
                "previousRank=-1",
                "for exponent in 1:8",
                "  currentRank=rank(powerMatrix)",
                '  println("GUARD_POWER_RANK ",exponent," ",currentRank)',
                "  if currentRank==previousRank; break; end",
                "  previousRank=currentRank",
                "  powerMatrix=powerMatrix*guardMatrix",
                "end",
                'println("PAIR_JULIA_FF_GUARD_RANK_COMPLETE")',
            )
        )
        expected = "PAIR_JULIA_FF_GUARD_RANK_COMPLETE"
    elif stage == "guard-rank-import":
        export = json.loads(Path(REMOTE_BASIS_EXPORT).read_text())[0]
        basis_text = "\n".join(export["basis_lines"])
        if hashlib.sha256(basis_text.encode()).hexdigest() != export["basis_sha256"]:
            raise RuntimeError("imported squared basis hash mismatch")
        basis_literal = ",\n".join(export["basis_lines"])
        computation = "\n".join(
            (
                'println("PAIR_JULIA_FF_GUARD_RANK_IMPORT_START")',
                "b=BU",
                f"squaredBasis=[{basis_literal}]",
                '@assert isgroebner(squaredBasis; ordering=DegRevLex())',
                'println("GUARD_RANK_IMPORTED_BASIS ",length(squaredBasis))',
                (
                    "quotientBasis=Groebner.quotient_basis(squaredBasis; "
                    "ordering=DegRevLex())"
                ),
                'println("GUARD_RANK_QUOTIENT_BASIS ",length(quotientBasis))',
                "basisIndex=Dict{Tuple{Vararg{Int}},Int}()",
                (
                    "for (index,value) in enumerate(quotientBasis); "
                    "basisIndex[Tuple(exponent_vector(value,1))]=index; end"
                ),
                "guardU=d0U*d1U",
                (
                    "products=normalform(squaredBasis,"
                    "[guardU*value for value in quotientBasis]; "
                    "ordering=DegRevLex())"
                ),
                'println("GUARD_RANK_NORMAL_FORMS ",length(products))',
                "quotientDimension=length(quotientBasis)",
                "guardMatrix=zero_matrix(K,quotientDimension,quotientDimension)",
                "for column in 1:quotientDimension",
                "  value=products[column]",
                "  for termIndex in 1:length(value)",
                "    row=basisIndex[Tuple(exponent_vector(value,termIndex))]",
                "    guardMatrix[row,column]=coeff(value,termIndex)",
                "  end",
                "end",
                'println("GUARD_RANK_MATRIX_COMPLETE")',
                "powerMatrix=guardMatrix",
                "previousRank=-1",
                "for exponent in 1:8",
                "  currentRank=rank(powerMatrix)",
                '  println("GUARD_POWER_RANK ",exponent," ",currentRank)',
                "  if currentRank==previousRank; break; end",
                "  previousRank=currentRank",
                "  powerMatrix=powerMatrix*guardMatrix",
                "end",
                'println("PAIR_JULIA_FF_GUARD_RANK_IMPORT_COMPLETE")',
            )
        )
        expected = "PAIR_JULIA_FF_GUARD_RANK_IMPORT_COMPLETE"
    else:
        raise ValueError(
            "stage must be ledger, groebner, squared-ledger, or "
            "squared-groebner/profile/export/guarded-profile/guard-rank/import"
        )
    program = source + "\n" + computation + "\n"
    header = {
        "chart_index": chart_index,
        "stage": stage,
        "field": f"GF({prime})(t)",
        "program_sha256": hashlib.sha256(program.encode()).hexdigest(),
        "denominator_product_sha256": hashlib.sha256(
            julia(denominator_product).encode()
        ).hexdigest(),
        "scope": (
            "generic-t reconstructed DE+/DE- pair on one c chart in the "
            "four-generator reciprocal quotient; no exceptional t fibers, "
            "colored edge, remaining guards, route, row, or Prize conclusion"
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
                "stdout": decoded(error.stdout)[-10000:],
                "stderr": decoded(error.stderr)[-4000:],
            }
    valid = process.returncode == 0 and expected in process.stdout
    result = {
        **header,
        "status": "COMPLETE" if valid else "ERROR",
        "returncode": process.returncode,
        "stdout": process.stdout[-10000:],
        "stderr": process.stderr[-4000:],
    }
    if stage == "squared-export" and valid:
        basis_text = Path("/tmp/cell5_pair_squared_basis.txt").read_text().rstrip("\n")
        result["basis_lines"] = basis_text.splitlines()
        result["basis_sha256"] = hashlib.sha256(basis_text.encode()).hexdigest()
    return result


@app.local_entrypoint()
def main(charts: str = "2", stage: str = "ledger", output: str = ""):
    indices = [int(value) for value in charts.split(",")]
    if any(value not in {2, 3, 4, 5} for value in indices):
        raise ValueError("charts must be a comma-separated subset of 2,3,4,5")
    if stage not in {
        "ledger",
        "groebner",
        "squared-ledger",
        "squared-groebner",
        "squared-profile",
        "squared-export",
        "guarded-profile",
        "guard-rank",
        "guard-rank-import",
    }:
        raise ValueError(
            "stage must be ledger, groebner, squared-ledger, or "
            "squared-groebner/profile/export/guarded-profile/guard-rank/import"
        )
    results = []
    for result in analyze.map(
        [f"{stage}:{index}" for index in indices], order_outputs=True
    ):
        results.append(result)
        compact = {key: value for key, value in result.items() if key != "basis_lines"}
        print(json.dumps(compact, sort_keys=True), flush=True)
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
